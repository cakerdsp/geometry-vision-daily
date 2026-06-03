from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

from scripts.analysis_io import load_json, write_json_atomic


LOGGER = logging.getLogger("geometry_vision_daily.analysis")


class DeepSeekError(RuntimeError):
    pass


class DeepSeekAuthError(DeepSeekError):
    pass


class BudgetExceededError(DeepSeekError):
    pass


@dataclass
class ChatResult:
    content: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    estimated_cost_usd: float
    estimated_cost_cny: float


class DeepSeekClient:
    def __init__(self, config: dict[str, Any]) -> None:
        analysis = config.get("analysis", {})
        self.model = str(analysis.get("model", "deepseek-v4-flash"))
        self.base_url = str(analysis.get("base_url", "https://api.deepseek.com")).rstrip("/")
        self.timeout = int(analysis.get("timeout_seconds", 60))
        self.max_retries = int(analysis.get("max_retries", 3))
        self.retry_initial_seconds = float(analysis.get("retry_initial_seconds", 2))
        self.usage_log_path = Path(analysis.get("usage_log_path", "data/usage_log.json"))
        self.monthly_budget_cny = float(analysis.get("monthly_budget_cny", 50))
        self.usd_to_cny = float(analysis.get("usd_to_cny", 7.2))
        pricing = analysis.get("pricing_per_1m_tokens_usd", {})
        self.input_price = float(pricing.get("input_cache_miss", 0.14))
        self.output_price = float(pricing.get("output", 0.28))
        self.api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
        if not self.api_key:
            raise DeepSeekAuthError(
                "缺少 DEEPSEEK_API_KEY。请在 GitHub repository secret 中配置该变量。"
            )

    def build_payload(self, messages: list[dict[str, str]], max_tokens: int) -> dict[str, Any]:
        return {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "thinking": {"type": "disabled"},
        }

    def chat(
        self,
        messages: list[dict[str, str]],
        task: str,
        max_tokens: int,
        arxiv_id: str | None = None,
    ) -> ChatResult:
        estimated_input_tokens = estimate_tokens(
            "\n".join(message.get("content", "") for message in messages)
        )
        estimated_cost_cny = self._estimate_cost_cny(estimated_input_tokens, max_tokens)
        self._assert_budget(estimated_cost_cny)

        payload = self.build_payload(messages, max_tokens=max_tokens)
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        last_error: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=self.timeout)
                if response.status_code in (401, 402):
                    raise DeepSeekAuthError(
                        f"DeepSeek API 返回 {response.status_code}，请检查 API Key 或账户余额。"
                    )
                if response.status_code in (429, 500, 503):
                    raise requests.HTTPError(
                        f"DeepSeek API temporary status {response.status_code}",
                        response=response,
                    )
                response.raise_for_status()
                result = response.json()
                content = (
                    result.get("choices", [{}])[0]
                    .get("message", {})
                    .get("content", "")
                    .strip()
                )
                if not content:
                    raise DeepSeekError("DeepSeek API 返回空内容。")
                usage = result.get("usage", {}) if isinstance(result, dict) else {}
                prompt_tokens = int(usage.get("prompt_tokens") or estimated_input_tokens)
                completion_tokens = int(usage.get("completion_tokens") or estimate_tokens(content))
                total_tokens = int(usage.get("total_tokens") or prompt_tokens + completion_tokens)
                cost_usd = self._estimate_cost_usd(prompt_tokens, completion_tokens)
                cost_cny = cost_usd * self.usd_to_cny
                self._append_usage(
                    {
                        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
                        "task": task,
                        "arxiv_id": arxiv_id,
                        "model": self.model,
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "total_tokens": total_tokens,
                        "estimated_cost_usd": round(cost_usd, 8),
                        "estimated_cost_cny": round(cost_cny, 6),
                    }
                )
                return ChatResult(content, prompt_tokens, completion_tokens, total_tokens, cost_usd, cost_cny)
            except DeepSeekAuthError:
                raise
            except (requests.RequestException, ValueError, DeepSeekError) as exc:
                last_error = exc
                if attempt >= self.max_retries:
                    break
                sleep_seconds = min(self.retry_initial_seconds * (2 ** (attempt - 1)), 60)
                LOGGER.warning("DeepSeek 调用临时失败，准备重试 %s/%s。", attempt, self.max_retries)
                time.sleep(sleep_seconds)
        raise DeepSeekError(f"DeepSeek 调用失败，已重试 {self.max_retries} 次：{last_error}") from last_error

    def _append_usage(self, record: dict[str, Any]) -> None:
        usage_log = load_json(self.usage_log_path, [])
        if not isinstance(usage_log, list):
            raise ValueError(f"usage log must be a list: {self.usage_log_path}")
        usage_log.append(record)
        write_json_atomic(self.usage_log_path, usage_log)

    def _assert_budget(self, next_estimated_cost_cny: float) -> None:
        month = datetime.now(timezone.utc).strftime("%Y-%m")
        usage_log = load_json(self.usage_log_path, [])
        spent = 0.0
        if isinstance(usage_log, list):
            for record in usage_log:
                if not isinstance(record, dict):
                    continue
                if str(record.get("timestamp", "")).startswith(month):
                    spent += float(record.get("estimated_cost_cny", 0) or 0)
        if spent + next_estimated_cost_cny > self.monthly_budget_cny:
            raise BudgetExceededError(
                f"本月 DeepSeek 估算费用 {spent:.4f} 元，下一次调用预计 {next_estimated_cost_cny:.4f} 元，超过预算 {self.monthly_budget_cny:.2f} 元。"
            )

    def _estimate_cost_usd(self, prompt_tokens: int, completion_tokens: int) -> float:
        return (prompt_tokens / 1_000_000) * self.input_price + (
            completion_tokens / 1_000_000
        ) * self.output_price

    def _estimate_cost_cny(self, prompt_tokens: int, completion_tokens: int) -> float:
        return self._estimate_cost_usd(prompt_tokens, completion_tokens) * self.usd_to_cny


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)
