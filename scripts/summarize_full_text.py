from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

from scripts.analysis_io import paper_state, safe_slug, today_utc, utc_now_iso
from scripts.deepseek_client import DeepSeekClient
from scripts.download_pdf import download_pdf
from scripts.extract_pdf_text import extract_pdf_text
from scripts.parse_interests import InterestProfile
from scripts.rank_by_interests import rank_by_interests
from scripts.split_sections import split_sections


def summarize_full_texts(
    papers: list[dict[str, Any]],
    state: dict[str, Any],
    config: dict[str, Any],
    interests: InterestProfile,
    client: DeepSeekClient,
) -> int:
    if "full-text analysis" not in interests.tasks:
        return 0

    analysis_config = config.get("analysis", {})
    top_n = int(analysis_config.get("max_full_text_summaries_per_run", 3))
    chunk_size = int(analysis_config.get("chunk_size", 12000))
    max_chunks = int(analysis_config.get("max_chunks_per_paper", 8))
    output_dir = Path(analysis_config.get("interests_output_dir", "interests"))
    mirror_dir = Path(analysis_config.get("full_text_summary_dir", "summaries/full-text"))
    output_dir.mkdir(parents=True, exist_ok=True)
    mirror_dir.mkdir(parents=True, exist_ok=True)
    selected = rank_by_interests(papers, interests, top_n)
    completed = 0

    for paper in selected:
        arxiv_id = str(paper.get("arxiv_id", "")).strip()
        record = paper_state(state, arxiv_id)
        if record.get("full_text", {}).get("status") == "success":
            continue
        with tempfile.TemporaryDirectory() as tmp_dir:
            pdf_path = Path(tmp_dir) / f"{safe_slug(arxiv_id)}.pdf"
            download_pdf(str(paper.get("pdf_url", "")), pdf_path)
            text = extract_pdf_text(pdf_path)
        chunks = split_sections(text, chunk_size)[:max_chunks]
        if not chunks:
            record["full_text"] = {
                "status": "failed",
                "updated_at": utc_now_iso(),
                "error": "未能从 PDF 提取正文。",
            }
            continue

        chunk_summaries: list[str] = []
        for index, chunk in enumerate(chunks, start=1):
            result = client.chat(
                [
                    {
                        "role": "system",
                        "content": "你是计算机视觉论文全文分析助手。输出必须是简体中文，基于给定正文片段，不得编造。",
                    },
                    {
                        "role": "user",
                        "content": build_chunk_prompt(paper, chunk, index, len(chunks), interests),
                    },
                ],
                task="full_text_chunk",
                max_tokens=int(analysis_config.get("max_tokens", {}).get("chunk_summary", 1400)),
                arxiv_id=arxiv_id,
            )
            chunk_summaries.append(result.content.strip())

        final_result = client.chat(
            [
                {
                    "role": "system",
                    "content": "你是计算机视觉论文全文分析助手。请把分块笔记汇总为结构化中文 Markdown。",
                },
                {
                    "role": "user",
                    "content": build_full_text_synthesis_prompt(paper, chunk_summaries, interests),
                },
            ],
            task="full_text_synthesis",
            max_tokens=int(analysis_config.get("max_tokens", {}).get("full_text_synthesis", 2000)),
            arxiv_id=arxiv_id,
        )
        markdown = final_result.content.strip()
        dated_path = output_dir / f"full-text-{today_utc()}-{safe_slug(arxiv_id)}.md"
        mirror_path = mirror_dir / f"{safe_slug(arxiv_id)}.md"
        dated_path.write_text(markdown + "\n", encoding="utf-8")
        mirror_path.write_text(markdown + "\n", encoding="utf-8")
        record["full_text"] = {
            "status": "success",
            "updated_at": utc_now_iso(),
            "path": str(dated_path.as_posix()),
            "mirror_path": str(mirror_path.as_posix()),
        }
        completed += 1
    return completed


def build_chunk_prompt(
    paper: dict[str, Any],
    chunk: str,
    index: int,
    total: int,
    interests: InterestProfile,
) -> str:
    return f"""请分析论文正文片段 {index}/{total}。

论文标题：{paper.get("title", "")}
兴趣指令：
{interests.instructions or "未提供额外兴趣方向。"}

正文片段：
{chunk}

请输出：
- 本片段核心内容
- 方法细节
- 实验或数据集信息
- 与几何基础模型、NeRF/Gaussian Splatting、动态重建的关系
- 本片段无法判断的信息
"""


def build_full_text_synthesis_prompt(
    paper: dict[str, Any],
    chunk_summaries: list[str],
    interests: InterestProfile,
) -> str:
    joined = "\n\n---\n\n".join(chunk_summaries)
    return f"""请基于以下分块笔记，生成该论文的全文分析 Markdown。

论文标题：{paper.get("title", "")}
兴趣指令：
{interests.instructions or "未提供额外兴趣方向。"}

分块笔记：
{joined}

输出结构：
## 全文分析
### 核心结论
### 方法拆解
### 实验和证据
### 与用户兴趣方向的关系
### 值得精读的部分
### 局限性和不确定信息
"""
