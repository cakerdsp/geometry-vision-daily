from __future__ import annotations

from typing import Any

from scripts.analysis_io import paper_input_hash


def fetch_new_papers(
    papers: list[dict[str, Any]],
    processed_state: dict[str, Any],
    max_papers: int,
    prompt_version: str = "brief-v1",
) -> list[dict[str, Any]]:
    processed = processed_state.get("papers", {})
    new_papers: list[dict[str, Any]] = []
    for paper in papers:
        arxiv_id = str(paper.get("arxiv_id", "")).strip()
        if not arxiv_id:
            continue
        current_hash = paper_input_hash(paper)
        record = processed.get(arxiv_id, {}) if isinstance(processed, dict) else {}
        brief = record.get("brief", {}) if isinstance(record, dict) else {}
        if (
            brief.get("status") == "success"
            and brief.get("input_hash") == current_hash
            and brief.get("prompt_version") == prompt_version
        ):
            continue
        new_papers.append(paper)
        if len(new_papers) >= max_papers:
            break
    return new_papers
