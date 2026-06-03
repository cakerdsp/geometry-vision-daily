from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts.analysis_io import (
    paper_ai_input,
    paper_input_hash,
    paper_state,
    safe_slug,
    utc_now_iso,
)
from scripts.deepseek_client import DeepSeekClient
from scripts.parse_interests import InterestProfile


def summarize_abstracts(
    papers: list[dict[str, Any]],
    state: dict[str, Any],
    config: dict[str, Any],
    interests: InterestProfile,
    client: DeepSeekClient,
) -> int:
    output_dir = Path(config.get("analysis", {}).get("brief_summary_dir", "summaries/brief"))
    output_dir.mkdir(parents=True, exist_ok=True)
    max_tokens = int(config.get("analysis", {}).get("max_tokens", {}).get("brief_summary", 1200))
    completed = 0
    for paper in papers:
        arxiv_id = str(paper.get("arxiv_id", "")).strip()
        if not arxiv_id:
            continue
        prompt = build_brief_prompt(paper, interests)
        result = client.chat(
            [
                {
                    "role": "system",
                    "content": "你是严谨的计算机视觉论文分析助手。只能根据用户提供的标题、作者、摘要和元数据分析；不得编造正文中未提供的信息。输出必须是简体中文 Markdown。",
                },
                {"role": "user", "content": prompt},
            ],
            task="brief_summary",
            max_tokens=max_tokens,
            arxiv_id=arxiv_id,
        )
        markdown = normalize_brief_markdown(result.content)
        summary_path = output_dir / f"{safe_slug(arxiv_id)}.md"
        summary_path.write_text(markdown + "\n", encoding="utf-8")
        record = paper_state(state, arxiv_id)
        record["brief"] = {
            "status": "success",
            "input_hash": paper_input_hash(paper),
            "updated_at": utc_now_iso(),
            "path": str(summary_path.as_posix()),
            "markdown": markdown,
        }
        completed += 1
    return completed


def build_brief_prompt(paper: dict[str, Any], interests: InterestProfile) -> str:
    payload = paper_ai_input(paper)
    interest_block = interests.instructions.strip() or "未提供额外兴趣方向。"
    return f"""请仅基于以下论文元数据和摘要，生成简体中文简要分析。不要使用外部知识补全论文实验细节。

兴趣和任务指令：
{interest_block}

论文输入：
- title: {payload["title"]}
- authors: {", ".join(payload.get("authors", []))}
- abstract: {payload["abstract"]}
- published: {payload["published"]}
- primary_category: {payload["primary_category"]}
- secondary_categories: {", ".join(payload.get("secondary_categories", []))}
- abstract_url: {payload["abstract_url"]}
- pdf_url: {payload["pdf_url"]}

请严格使用以下 Markdown 结构：

### Metadata
- 标题：
- 作者：
- 出版日期：
- 分类：
- 链接：

### 一句话总结

### 研究问题

### 核心思路/方法

### 主要贡献

### 与相关方法的关系
说明它与 VGGT、DUSt3R、MASt3R、CroCo、NeRF、Gaussian Splatting、动态场景重建方法的关系；没有依据时明确写“摘要未提供足够信息”。

### 局限性
正文未提供的信息必须注明“摘要未提供足够信息”。

### 阅读优先级
给出 高 / 中 / 低，并说明理由。
"""


def normalize_brief_markdown(markdown: str) -> str:
    return markdown.strip()
