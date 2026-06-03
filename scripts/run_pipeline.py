from __future__ import annotations

import argparse
import logging
from pathlib import Path

from scripts.analysis_io import ensure_state_shape, load_json, write_json_atomic
from scripts.deepseek_client import DeepSeekClient
from scripts.fetch_new_papers import fetch_new_papers
from scripts.generate_daily_report import generate_daily_report
from scripts.generate_readme import load_config, write_readme
from scripts.parse_interests import parse_interests
from scripts.summarize_abstracts import summarize_abstracts
from scripts.summarize_full_text import summarize_full_texts


LOGGER = logging.getLogger("geometry_vision_daily.pipeline")
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"


def run_pipeline(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, int]:
    config = load_config(config_path)
    analysis_config = config.get("analysis", {})
    papers_path = Path(config.get("output", {}).get("json_path", "data/papers.json"))
    processed_path = Path(analysis_config.get("processed_path", "data/processed_papers.json"))
    interests_path = Path(analysis_config.get("interests_path", "interests.md"))
    papers = load_json(papers_path, [])
    if not isinstance(papers, list):
        raise ValueError(f"Expected paper list in {papers_path}")
    state = ensure_state_shape(load_json(processed_path, {"papers": {}, "reports": {}}))
    interests = parse_interests(interests_path)
    max_papers = int(analysis_config.get("max_papers_per_run", 10))
    brief_prompt_version = str(analysis_config.get("brief_prompt_version", "brief-v1"))
    new_papers = fetch_new_papers(papers, state, max_papers, brief_prompt_version)

    always_report = bool(analysis_config.get("always_generate_daily_report", True))
    client_needed = (
        bool(new_papers)
        or "full-text analysis" in interests.tasks
        or "generate daily trend report" in interests.tasks
        or (always_report and bool(papers))
    )
    client = DeepSeekClient(config) if client_needed else None

    brief_count = 0
    full_text_count = 0
    if new_papers and client is not None:
        brief_count = summarize_abstracts(new_papers, state, config, interests, client)
    if client is not None:
        full_text_count = summarize_full_texts(papers, state, config, interests, client)
    report_path = generate_daily_report(papers, state, config, interests, client)

    write_json_atomic(processed_path, state)
    write_readme(papers, config, config.get("output", {}).get("readme_path", "README.md"))

    summary = {
        "papers_total": len(papers),
        "new_papers": len(new_papers),
        "brief_summaries": brief_count,
        "full_text_summaries": full_text_count,
        "daily_reports": 1 if report_path.exists() else 0,
    }
    for key, value in summary.items():
        print(f"{key}: {value}")
    return summary


def main() -> None:
    logging.basicConfig(
        format="[%(asctime)s %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    parser = argparse.ArgumentParser(description="Run daily AI analysis pipeline.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="Path to config.yaml")
    args = parser.parse_args()
    run_pipeline(args.config)


if __name__ == "__main__":
    main()
