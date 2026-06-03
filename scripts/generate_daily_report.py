from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from scripts.analysis_io import today_utc, utc_now_iso
from scripts.deepseek_client import DeepSeekClient
from scripts.parse_interests import InterestProfile


def generate_daily_report(
    papers: list[dict[str, Any]],
    state: dict[str, Any],
    config: dict[str, Any],
    interests: InterestProfile,
    client: DeepSeekClient | None = None,
) -> Path:
    analysis_config = config.get("analysis", {})
    output_dir = Path(analysis_config.get("daily_report_dir", "reports/daily"))
    output_dir.mkdir(parents=True, exist_ok=True)
    date = today_utc()
    output_path = output_dir / f"{date}.md"

    deterministic = build_data_overview(papers, interests)
    ai_report = ""
    always_report = bool(analysis_config.get("always_generate_daily_report", True))
    should_generate_ai_report = always_report or "generate daily trend report" in interests.tasks
    if should_generate_ai_report and papers:
        if client is None:
            ai_report = "未检测到可用的 DeepSeek 客户端，无法生成科研趋势综合分析。"
        else:
            ai_report = generate_ai_trend_report(papers, state, config, interests, client)

    body = deterministic
    body += "\n\n## 科研趋势综合分析\n\n"
    body += ai_report.strip() if ai_report else "当前没有可分析论文。"
    if interests.instructions.strip():
        body += "\n\n## interests.md 指令分析\n\n"
        body += f"已结合 `interests.md` 中的兴趣方向和任务指令：\n\n{interests.instructions.strip()}"
    else:
        body += "\n\n## interests.md 指令分析\n\n未指定额外兴趣方向或任务。"

    output_path.write_text(body.strip() + "\n", encoding="utf-8")
    reports = state.setdefault("reports", {})
    reports[date] = {
        "status": "success",
        "updated_at": utc_now_iso(),
        "path": str(output_path.as_posix()),
        "tasks": sorted(interests.tasks),
        "ai_trend_report": bool(ai_report and client is not None),
    }
    return output_path


def build_data_overview(papers: list[dict[str, Any]], interests: InterestProfile) -> str:
    category_counts = Counter(str(paper.get("primary_category", "未分类")) for paper in papers)
    total = len(papers)
    lines = [
        "# 每日 AI 分析",
        "",
        "来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。",
        "",
        "## 数据概况",
        "",
        f"- 当前滚动窗口论文数：{total}",
        "- 分类分布：",
    ]
    if category_counts:
        for category, count in category_counts.most_common():
            lines.append(f"  - {category}: {count}")
    else:
        lines.append("  - 暂无论文")
    if interests.keywords:
        lines.append("- 当前兴趣方向：" + "、".join(interests.keywords))
    else:
        lines.append("- 当前兴趣方向：未指定")
    if interests.tasks:
        lines.append("- 当前显式任务：" + "、".join(sorted(interests.tasks)))
    else:
        lines.append("- 当前显式任务：未指定")
    return "\n".join(lines)


def generate_ai_trend_report(
    papers: list[dict[str, Any]],
    state: dict[str, Any],
    config: dict[str, Any],
    interests: InterestProfile,
    client: DeepSeekClient,
) -> str:
    analysis_config = config.get("analysis", {})
    max_papers = int(analysis_config.get("max_daily_report_papers", 20))
    entries: list[str] = []
    processed = state.get("papers", {})
    for paper in papers[:max_papers]:
        arxiv_id = str(paper.get("arxiv_id", ""))
        brief = processed.get(arxiv_id, {}).get("brief", {}) if isinstance(processed, dict) else {}
        brief_text = str(brief.get("markdown", "")).strip()
        abstract = str(paper.get("abstract", "")).strip()
        entries.append(
            "\n".join(
                [
                    f"- 标题：{paper.get('title', '')}",
                    f"  arXiv ID：{arxiv_id}",
                    f"  分类：{paper.get('primary_category', '')}",
                    f"  次级分类：{', '.join(paper.get('secondary_categories', []) or []) or '无'}",
                    f"  摘要：{abstract[:900]}",
                    f"  已有简析：{brief_text[:900] if brief_text else '暂无简析'}",
                ]
            )
        )
    prompt = f"""请基于今天滚动窗口内的论文列表，生成中文科研趋势综合分析。不要只统计数量；需要归纳这些新论文反映出的研究方向变化、技术路线、潜在机会和阅读优先级。

兴趣指令：
{interests.instructions or "未提供额外兴趣方向。"}

论文列表：
{chr(10).join(entries)}

请输出 Markdown，并严格包含以下部分：

### 今日主要趋势
概括 3-5 条真实趋势，每条需要对应到若干论文或类别。

### 技术路线观察
比较这些论文在几何基础模型、3D/4D 重建、神经场景表示、机器人/AR 应用等方向上的技术侧重点。

### 值得优先阅读的论文
给出 5 篇以内，并说明为什么优先读。

### 可能的研究机会
从这些论文中提炼可跟进的研究空白或组合方向。

### 风险和不确定性
说明哪些结论只基于摘要，哪些需要全文验证。
"""
    result = client.chat(
        [
            {
                "role": "system",
                "content": (
                    "你是计算机视觉和三维重建方向的科研趋势分析助手。"
                    "输出必须是简体中文 Markdown，避免编造论文未给出的细节。"
                ),
            },
            {"role": "user", "content": prompt},
        ],
        task="daily_trend_report",
        max_tokens=int(analysis_config.get("max_tokens", {}).get("daily_report", 1800)),
    )
    return result.content.strip()
