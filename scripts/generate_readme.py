from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import yaml


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"
DISCLAIMER = """## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv."""


def load_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    if not isinstance(config, dict):
        raise ValueError(f"Configuration file is empty or invalid: {path}")
    return config


def load_papers(json_path: str | Path) -> list[dict[str, Any]]:
    path = Path(json_path)
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON list in {path}")
    return [paper for paper in data if isinstance(paper, dict)]


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
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _date_label(value: str | None) -> str:
    parsed = parse_datetime(value)
    if parsed is None:
        return "unknown-date"
    return parsed.date().isoformat()


def _month_label(value: str | None) -> str:
    parsed = parse_datetime(value)
    if parsed is None:
        return "unknown-month"
    return parsed.strftime("%Y-%m")


def _markdown_escape(text: Any) -> str:
    cleaned = re.sub(r"\s+", " ", str(text or "")).strip()
    return cleaned.replace("|", "\\|")


def _latest_first_seen(papers: list[dict[str, Any]]) -> str | None:
    values = [
        paper.get("first_seen")
        for paper in papers
        if isinstance(paper.get("first_seen"), str) and paper.get("first_seen")
    ]
    return max(values) if values else None


def _latest_update_label(papers: list[dict[str, Any]]) -> str:
    latest = _latest_first_seen(papers)
    if not latest:
        return "No papers collected yet"
    return latest


def _count_added_in_latest_update(papers: list[dict[str, Any]]) -> int:
    latest = _latest_first_seen(papers)
    if not latest:
        return 0
    return sum(1 for paper in papers if paper.get("first_seen") == latest)


def _sort_key(paper: dict[str, Any]) -> tuple[datetime, str]:
    published = parse_datetime(paper.get("published")) or datetime.min.replace(tzinfo=timezone.utc)
    return published, str(paper.get("arxiv_id", ""))


def _paper_is_recent(paper: dict[str, Any], cutoff: datetime) -> bool:
    published = parse_datetime(paper.get("published"))
    return published is not None and published >= cutoff


def render_readme(
    papers: list[dict[str, Any]],
    config: dict[str, Any],
    now: datetime | None = None,
) -> str:
    project = config.get("project", {})
    output = config.get("output", {})
    classification = config.get("classification", {})
    arxiv = config.get("arxiv", {})

    title = project.get("readme_title", "Geometry Vision Daily")
    description = project.get(
        "description",
        "A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.",
    )
    category_order = list(classification.get("category_priority", []))
    readme_days = int(output.get("readme_days", output.get("retention_days", 7)))
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    cutoff = now.astimezone(timezone.utc) - timedelta(days=readme_days)

    lines: list[str] = [
        f"# {title}",
        "",
        str(description),
        "",
        f"**Last updated:** {_latest_update_label(papers)}",
        f"**Total number of papers:** {len(papers)}",
        f"**Number of papers added in the latest update:** {_count_added_in_latest_update(papers)}",
        f"**Categories tracked:** {', '.join(arxiv.get('categories', []))}",
        "",
        "Paper metadata is collected from the public arXiv API and stored as structured JSON. PDF files are not downloaded, mirrored, or redistributed.",
        "",
        f"Rolling {readme_days}-day structured archive: [data/papers.json](data/papers.json)",
        "",
        "## Table of Contents",
        "",
    ]
    for category in category_order:
        lines.append(f"- [{category}](#{_anchor(category)})")
    lines.extend(["", "## How It Works", ""])
    lines.extend(
        [
            "1. GitHub Actions runs the update workflow every day.",
            "2. The update script searches candidate papers from the latest configured lookback window.",
            "3. A deterministic rule-based classifier filters and categorizes papers.",
            "4. Papers are deduplicated by normalized arXiv ID.",
            f"5. README displays papers from the latest {readme_days} days.",
            f"6. The rolling {readme_days}-day archive is kept in data/papers.json.",
            "7. PDF files are never stored in this repository.",
            "",
            "## Run Locally",
            "",
            "```bash",
            "python -m venv .venv",
            "source .venv/bin/activate",
            "pip install -r requirements.txt",
            "pytest",
            "python scripts/update_papers.py",
            "```",
            "",
            "Windows PowerShell activation:",
            "",
            "```powershell",
            ".venv\\Scripts\\Activate.ps1",
            "```",
            "",
            "## Configuration",
            "",
            "Users can edit config.yaml to adjust arXiv categories, include keywords, exclude keywords, category priority, lookback days, README display days, request interval, and classification thresholds.",
            "",
            "## Manual Update",
            "",
            "Use the Actions tab on GitHub and run the workflow_dispatch trigger manually.",
            "",
        ]
    )

    recent_papers = [paper for paper in papers if _paper_is_recent(paper, cutoff)]
    for category in category_order:
        lines.extend([f"## {category}", ""])
        category_papers = [
            paper
            for paper in recent_papers
            if paper.get("primary_category") == category
        ]
        if not category_papers:
            lines.extend(["No papers in the current README window.", ""])
            continue
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for paper in sorted(category_papers, key=_sort_key, reverse=True):
            grouped[_month_label(paper.get("published"))].append(paper)
        for month in sorted(grouped.keys(), reverse=True):
            lines.extend([f"### {month}", ""])
            for paper in grouped[month]:
                title_text = _markdown_escape(paper.get("title", "Untitled"))
                authors = ", ".join(str(author) for author in paper.get("authors", []) if author)
                secondary = paper.get("secondary_categories") or []
                matched = paper.get("matched_keywords") or []
                abstract = str(paper.get("abstract", "")).strip()
                lines.extend(
                    [
                        f"#### {_date_label(paper.get('published'))} - {title_text}",
                        "",
                        f"**Authors:** {_markdown_escape(authors) if authors else 'Unknown'}",
                        f"**Links:** [abs]({paper.get('abstract_url', '')}) - [pdf]({paper.get('pdf_url', '')})",
                        f"**Primary category:** {_markdown_escape(paper.get('primary_category', 'Unknown'))}",
                        f"**Secondary categories:** {_markdown_escape(', '.join(secondary)) if secondary else 'None'}",
                        f"**Matched keywords:** {_markdown_escape(', '.join(matched)) if matched else 'None'}",
                        "",
                        "<details>",
                        "<summary>Abstract</summary>",
                        "",
                        abstract or "No abstract available.",
                        "",
                        "</details>",
                        "",
                    ]
                )

    lines.extend([DISCLAIMER, ""])
    return "\n".join(lines)


def _anchor(text: str) -> str:
    anchor = text.lower()
    anchor = anchor.replace("/", "")
    anchor = re.sub(r"[^a-z0-9\s-]", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor.strip())
    return anchor


def write_readme(
    papers: list[dict[str, Any]],
    config: dict[str, Any],
    readme_path: str | Path | None = None,
) -> None:
    output = config.get("output", {})
    path = Path(readme_path or output.get("readme_path", "README.md"))
    path.write_text(render_readme(papers, config), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Geometry Vision Daily README.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="Path to config.yaml")
    args = parser.parse_args()
    config = load_config(args.config)
    json_path = Path(config.get("output", {}).get("json_path", "data/papers.json"))
    papers = load_papers(json_path)
    write_readme(papers, config, config.get("output", {}).get("readme_path", "README.md"))


if __name__ == "__main__":
    main()
