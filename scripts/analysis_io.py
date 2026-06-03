from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: str | Path, default: Any) -> Any:
    file_path = Path(path)
    if not file_path.exists():
        return default
    try:
        with file_path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {file_path}: {exc}") from exc


def write_json_atomic(path: str | Path, data: Any) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = file_path.with_suffix(file_path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(temp_path, file_path)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    cleaned = value.strip()
    if cleaned.endswith("Z"):
        cleaned = cleaned[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(cleaned)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def today_utc() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "untitled"


def paper_ai_input(paper: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": paper.get("title", ""),
        "authors": paper.get("authors", []),
        "abstract": paper.get("abstract", ""),
        "published": paper.get("published", ""),
        "primary_category": paper.get("primary_category", ""),
        "secondary_categories": paper.get("secondary_categories", []),
        "abstract_url": paper.get("abstract_url", ""),
        "pdf_url": paper.get("pdf_url", ""),
    }


def paper_input_hash(paper: dict[str, Any]) -> str:
    payload = json.dumps(paper_ai_input(paper), ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def ensure_state_shape(state: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(state, dict):
        state = {}
    papers = state.get("papers")
    reports = state.get("reports")
    if not isinstance(papers, dict):
        state["papers"] = {}
    if not isinstance(reports, dict):
        state["reports"] = {}
    return state


def paper_state(state: dict[str, Any], arxiv_id: str) -> dict[str, Any]:
    papers = state.setdefault("papers", {})
    item = papers.setdefault(arxiv_id, {})
    if not isinstance(item, dict):
        item = {}
        papers[arxiv_id] = item
    return item
