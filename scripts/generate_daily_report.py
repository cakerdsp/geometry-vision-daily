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
    deterministic = build_deterministic_report(papers, interests)
    ai_report = ""
    if "generate daily trend report" in interests.tasks:
        if client is None:
            raise ValueError("Daily trend report requires a DeepSeek client.")
        ai_report = generate_ai_trend_report(papers, state, config, interests, client)

    body = deterministic
    if ai_report:
        body += "\n\n## interests.md 指令分析\n\n" + ai_report.strip()
    else:
        body += "\n\n## interests.md 指令分析\n\n未指定 `generate daily trend report`，因此未执行额外趋势报告任务。"
    output_path.write_text(body.strip() + "\n", encoding="utf-8")
    reports = state.setdefault("reports", {})
    reports[date] = {
        "status": "success",
        "updated_at": utc_now_iso(),
        "path": str(output_path.as_posix()),
        "tasks": sorted(interests.tasks),
    }
    return output_path


def build_deterministic_report(papers: list[dict[str, Any]], interests: InterestProfile) -> str:
    category_counts = Counter(str(paper.get("primary_category", "未分类")) for paper in papers)
    total = len(papers)
    lines = [
        "# 每日总览",
        "",
        "来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。",
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
        entries.append(
            f"- {paper.get('title', '')}\n  分类：{paper.get('primary_category', '')}\n  简析：{brief.get('markdown', '暂无简析')[:1200]}"
        )
    prompt = f"""请基于今天的论文列表和简析，生成中文每日趋势报告。

兴趣指令：
{interests.instructions or "未提供额外兴趣方向。"}

论文列表：
{chr(10).join(entries)}

输出结构：
### 今日总体趋势
### 值得优先关注的论文
### 与兴趣方向的对应关系
### 可能的研究机会
### 明日继续观察的问题
"""
    result = client.chat(
        [
            {
                "role": "system",
                "content": "你是计算机视觉研究趋势分析助手。输出必须是简体中文 Markdown，避免编造论文未给出的细节。",
            },
            {"role": "user", "content": prompt},
        ],
        task="daily_trend_report",
        max_tokens=int(analysis_config.get("max_tokens", {}).get("daily_report", 1800)),
    )
    return result.content.strip()
