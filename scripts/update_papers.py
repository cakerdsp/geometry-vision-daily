from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from email.utils import parsedate_to_datetime
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from zoneinfo import ZoneInfo

import feedparser
import requests
import yaml

if __package__:
    from .classification import classify_paper
    from .generate_readme import write_readme
else:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts.classification import classify_paper
    from scripts.generate_readme import write_readme


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"
LOGGER = logging.getLogger("geometry_vision_daily")


def load_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    if not isinstance(config, dict):
        raise ValueError(f"Configuration file is empty or invalid: {path}")
    for key in ("arxiv", "classification", "output"):
        if key not in config:
            raise ValueError(f"Missing required config section: {key}")
    return config


def normalize_arxiv_id(raw_id: str | None) -> tuple[str, str | None]:
    if not raw_id:
        return "", None
    value = raw_id.strip()
    value = value.rsplit("/", 1)[-1]
    value = value.replace("arXiv:", "")
    match = re.match(r"^(?P<base>.+?)(?P<version>v\d+)?$", value)
    if not match:
        return value, None
    return match.group("base"), match.group("version")


def parse_arxiv_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    cleaned = value.strip()
    if cleaned.endswith("Z"):
        cleaned = cleaned[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(cleaned)
    except ValueError:
        parsed_struct = feedparser._parse_date(value)
        if not parsed_struct:
            return None
        parsed = datetime(*parsed_struct[:6], tzinfo=timezone.utc)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def iso_utc(value: datetime | None) -> str:
    if value is None:
        return ""
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


class ArxivClient:
    def __init__(self, config: dict[str, Any]) -> None:
        arxiv_config = config["arxiv"]
        self.base_url = str(arxiv_config["base_url"])
        self.timeout = int(arxiv_config.get("timeout_seconds", 30))
        self.max_retries = int(arxiv_config.get("max_retries", 3))
        self.request_interval = float(arxiv_config.get("request_interval_seconds", 3))
        self.retry_429_seconds = float(arxiv_config.get("retry_429_seconds", 60))
        self.retry_5xx_seconds = float(arxiv_config.get("retry_5xx_seconds", 10))
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": str(arxiv_config["user_agent"])})
        self._last_request_time: float | None = None

    def _wait_for_rate_limit(self) -> None:
        if self._last_request_time is None:
            return
        elapsed = time.monotonic() - self._last_request_time
        remaining = self.request_interval - elapsed
        if remaining > 0:
            time.sleep(remaining)

    def query(self, search_query: str, start: int, max_results: int) -> feedparser.FeedParserDict:
        params = {
            "search_query": search_query,
            "start": start,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = f"{self.base_url}?{urlencode(params)}"
        last_error: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            self._wait_for_rate_limit()
            self._last_request_time = time.monotonic()
            try:
                response = self.session.get(url, timeout=self.timeout)
                if response.status_code == 429 or response.status_code >= 500:
                    raise requests.HTTPError(
                        f"Temporary arXiv HTTP status {response.status_code}",
                        response=response,
                    )
                response.raise_for_status()
                parsed = feedparser.parse(response.text)
                if getattr(parsed, "bozo", False):
                    raise ValueError(f"Failed to parse arXiv Atom feed: {parsed.bozo_exception}")
                return parsed
            except (requests.RequestException, ValueError) as exc:
                last_error = exc
                if attempt >= self.max_retries:
                    break
                sleep_seconds = self._sleep_seconds_for_error(exc, attempt)
                LOGGER.warning(
                    "arXiv request failed on attempt %s/%s; sleeping %.1fs before retry: %s",
                    attempt,
                    self.max_retries,
                    sleep_seconds,
                    exc,
                )
                time.sleep(sleep_seconds)
        raise RuntimeError(f"arXiv query failed after {self.max_retries} attempts: {last_error}") from last_error

    def _sleep_seconds_for_error(self, exc: Exception, attempt: int) -> float:
        if isinstance(exc, requests.HTTPError) and exc.response is not None:
            status_code = exc.response.status_code
            if status_code == 429:
                retry_after = self._retry_after_seconds(exc.response)
                if retry_after is not None:
                    return min(max(retry_after, self.request_interval), 300)
                return min(self.retry_429_seconds * (2 ** (attempt - 1)), 300)
            if status_code >= 500:
                return min(self.retry_5xx_seconds * (2 ** (attempt - 1)), 120)
        return min(self.request_interval * (2 ** (attempt - 1)), 120)

    def _retry_after_seconds(self, response: requests.Response) -> float | None:
        value = response.headers.get("Retry-After")
        if not value:
            return None
        try:
            return float(value)
        except ValueError:
            try:
                retry_at = parsedate_to_datetime(value)
            except (TypeError, ValueError):
                return None
            if retry_at.tzinfo is None:
                retry_at = retry_at.replace(tzinfo=timezone.utc)
            return max(0.0, (retry_at.astimezone(timezone.utc) - datetime.now(timezone.utc)).total_seconds())


def _feed_total_results(feed: feedparser.FeedParserDict) -> int | None:
    for key in ("opensearch_totalresults", "opensearch_totalResults"):
        value = feed.feed.get(key)
        if value is not None:
            try:
                return int(value)
            except (TypeError, ValueError):
                return None
    return None


def fetch_candidate_entries(config: dict[str, Any]) -> list[dict[str, Any]]:
    arxiv_config = config["arxiv"]
    categories = arxiv_config.get("categories", [])
    if not isinstance(categories, list) or not categories:
        raise ValueError("arxiv.categories must be a non-empty list")
    max_results = int(arxiv_config.get("max_results_per_query", 300))
    page_size = min(int(arxiv_config.get("page_size", 100)), max_results)
    client = ArxivClient(config)
    entries_by_id: dict[str, dict[str, Any]] = {}

    for category in categories:
        search_query = f"cat:{category}"
        start = 0
        while start < max_results:
            batch_size = min(page_size, max_results - start)
            LOGGER.info("Fetching arXiv category=%s start=%s max_results=%s", category, start, batch_size)
            feed = client.query(search_query, start=start, max_results=batch_size)
            entries = list(feed.entries)
            if not entries:
                break
            for entry in entries:
                arxiv_id, _ = normalize_arxiv_id(entry.get("id"))
                if arxiv_id:
                    entries_by_id[arxiv_id] = entry
            total = _feed_total_results(feed)
            start += len(entries)
            if total is not None and start >= min(total, max_results):
                break
            if len(entries) < batch_size:
                break

    return list(entries_by_id.values())


def paper_from_entry(entry: dict[str, Any], config: dict[str, Any]) -> dict[str, Any] | None:
    arxiv_id, version = normalize_arxiv_id(entry.get("id"))
    if not arxiv_id:
        LOGGER.warning("Skipping entry without arXiv ID: %s", entry.get("title", "<missing title>"))
        return None

    title = _clean_text(entry.get("title", ""))
    abstract = _clean_text(entry.get("summary", ""))
    authors = [
        str(author.get("name", "")).strip()
        for author in entry.get("authors", [])
        if isinstance(author, dict) and author.get("name")
    ]
    tags = entry.get("tags", [])
    arxiv_categories = [
        str(tag.get("term")).strip()
        for tag in tags
        if isinstance(tag, dict) and tag.get("term")
    ]
    primary = entry.get("arxiv_primary_category", {})
    primary_arxiv_category = ""
    if isinstance(primary, dict):
        primary_arxiv_category = str(primary.get("term", "")).strip()
    if not primary_arxiv_category and arxiv_categories:
        primary_arxiv_category = arxiv_categories[0]

    classification = classify_paper(title, abstract, arxiv_categories, config)
    if not classification["is_relevant"]:
        return None

    published = parse_arxiv_datetime(entry.get("published"))
    updated = parse_arxiv_datetime(entry.get("updated"))
    return {
        "arxiv_id": arxiv_id,
        "version": version,
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "published": iso_utc(published),
        "updated": iso_utc(updated),
        "primary_arxiv_category": primary_arxiv_category,
        "arxiv_categories": arxiv_categories,
        "primary_category": classification["primary_category"],
        "secondary_categories": classification["secondary_categories"],
        "matched_keywords": classification["matched_keywords"],
        "classification_score": classification["classification_score"],
        "classification_reasons": classification["classification_reasons"],
        "abstract_url": f"https://arxiv.org/abs/{arxiv_id}",
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
    }


def _clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def filter_by_lookback(entries: list[dict[str, Any]], lookback_days: int, now: datetime | None = None) -> list[dict[str, Any]]:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    cutoff = now.astimezone(timezone.utc) - timedelta(days=lookback_days)
    output = []
    for entry in entries:
        published = parse_arxiv_datetime(entry.get("published"))
        if published is not None and published >= cutoff:
            output.append(entry)
    return output


def load_existing_papers(json_path: str | Path) -> list[dict[str, Any]]:
    path = Path(json_path)
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}; refusing to overwrite corrupted data: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON list in {path}; refusing to overwrite corrupted data")
    return [paper for paper in data if isinstance(paper, dict)]


def upsert_papers(
    existing_papers: list[dict[str, Any]],
    incoming_papers: list[dict[str, Any]],
    seen_at: str,
) -> tuple[list[dict[str, Any]], int, int]:
    papers_by_id: dict[str, dict[str, Any]] = {}
    for paper in existing_papers:
        arxiv_id, _ = normalize_arxiv_id(str(paper.get("arxiv_id", "")))
        if not arxiv_id:
            continue
        normalized = dict(paper)
        normalized["arxiv_id"] = arxiv_id
        papers_by_id[arxiv_id] = normalized

    new_count = 0
    updated_count = 0
    mutable_fields = [
        "version",
        "title",
        "authors",
        "abstract",
        "published",
        "updated",
        "primary_arxiv_category",
        "arxiv_categories",
        "primary_category",
        "secondary_categories",
        "matched_keywords",
        "classification_score",
        "classification_reasons",
        "abstract_url",
        "pdf_url",
    ]

    for incoming in incoming_papers:
        arxiv_id, version = normalize_arxiv_id(str(incoming.get("arxiv_id", "")))
        if not arxiv_id:
            continue
        record = dict(incoming)
        record["arxiv_id"] = arxiv_id
        if version and not record.get("version"):
            record["version"] = version
        if arxiv_id not in papers_by_id:
            record["first_seen"] = seen_at
            record["last_seen"] = seen_at
            papers_by_id[arxiv_id] = record
            new_count += 1
            continue

        existing = papers_by_id[arxiv_id]
        changed = False
        for field in mutable_fields:
            if existing.get(field) != record.get(field):
                existing[field] = record.get(field)
                changed = True
        existing.setdefault("first_seen", seen_at)
        existing["last_seen"] = seen_at
        if changed:
            updated_count += 1

    merged = sorted(
        papers_by_id.values(),
        key=lambda paper: (
            parse_arxiv_datetime(paper.get("published")) or datetime.min.replace(tzinfo=timezone.utc),
            str(paper.get("arxiv_id", "")),
        ),
        reverse=True,
    )
    return merged, new_count, updated_count


def reclassify_existing_papers(
    existing_papers: list[dict[str, Any]],
    config: dict[str, Any],
) -> tuple[list[dict[str, Any]], int]:
    reclassified: list[dict[str, Any]] = []
    removed_count = 0
    for paper in existing_papers:
        classification = classify_paper(
            str(paper.get("title", "")),
            str(paper.get("abstract", "")),
            [str(category) for category in paper.get("arxiv_categories", [])],
            config,
        )
        if not classification["is_relevant"]:
            removed_count += 1
            continue
        updated = dict(paper)
        updated["primary_category"] = classification["primary_category"]
        updated["secondary_categories"] = classification["secondary_categories"]
        updated["matched_keywords"] = classification["matched_keywords"]
        updated["classification_score"] = classification["classification_score"]
        updated["classification_reasons"] = classification["classification_reasons"]
        reclassified.append(updated)
    return reclassified, removed_count


def prune_papers_by_retention(
    papers: list[dict[str, Any]],
    retention_days: int,
    now: datetime | None = None,
) -> tuple[list[dict[str, Any]], int]:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    cutoff = now.astimezone(timezone.utc) - timedelta(days=retention_days)
    kept: list[dict[str, Any]] = []
    removed_count = 0
    for paper in papers:
        published = parse_arxiv_datetime(paper.get("published"))
        if published is not None and published >= cutoff:
            kept.append(paper)
        else:
            removed_count += 1
    return kept, removed_count


def write_json_atomic(json_path: str | Path, papers: list[dict[str, Any]]) -> None:
    path = Path(json_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as handle:
        json.dump(papers, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(temp_path, path)


def current_seen_at(config: dict[str, Any]) -> str:
    timezone_name = config.get("schedule", {}).get("timezone", "America/New_York")
    try:
        tz = ZoneInfo(str(timezone_name))
    except Exception:
        tz = timezone.utc
    return datetime.now(tz).replace(microsecond=0).isoformat()


def is_arxiv_rate_limit_error(exc: Exception) -> bool:
    current: BaseException | None = exc
    while current is not None:
        if isinstance(current, requests.HTTPError) and current.response is not None:
            if current.response.status_code == 429:
                return True
        message = str(current).lower()
        if "429" in message and "arxiv" in message:
            return True
        current = current.__cause__ or current.__context__
    return False


def run_update(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, int]:
    config = load_config(config_path)
    output_config = config["output"]
    arxiv_config = config["arxiv"]
    json_path = Path(output_config.get("json_path", "data/papers.json"))
    lookback_days = int(arxiv_config.get("lookback_days", 3))
    retention_days = int(output_config.get("retention_days", output_config.get("readme_days", 7)))
    existing = load_existing_papers(json_path)

    try:
        candidates = fetch_candidate_entries(config)
    except Exception as exc:
        allow_stale = bool(arxiv_config.get("allow_stale_on_arxiv_rate_limit", False))
        if not allow_stale or not existing or not is_arxiv_rate_limit_error(exc):
            raise
        LOGGER.warning(
            "arXiv returned rate limits; using existing data/papers.json and keeping workflow successful."
        )
        existing, removed_count = reclassify_existing_papers(existing, config)
        merged, expired_count = prune_papers_by_retention(existing, retention_days)
        write_json_atomic(json_path, merged)
        write_readme(merged, config, output_config.get("readme_path", "README.md"))
        summary = {
            "fetched_candidates": 0,
            "recent_candidates": 0,
            "relevant_papers": 0,
            "new_papers": 0,
            "updated_papers": 0,
            "removed_papers": removed_count,
            "expired_papers": expired_count,
            "ignored_papers": 0,
            "total_stored_papers": len(merged),
            "used_stale_data": 1,
        }
        print("arXiv rate limited; used existing data/papers.json.")
        print(f"Total stored papers: {summary['total_stored_papers']}")
        return summary

    recent_entries = filter_by_lookback(candidates, lookback_days)
    relevant_papers = [
        paper
        for entry in recent_entries
        if (paper := paper_from_entry(entry, config)) is not None
    ]

    existing, removed_count = reclassify_existing_papers(existing, config)
    seen_at = current_seen_at(config)
    merged, new_count, updated_count = upsert_papers(existing, relevant_papers, seen_at)
    merged, expired_count = prune_papers_by_retention(merged, retention_days)
    write_json_atomic(json_path, merged)
    write_readme(merged, config, output_config.get("readme_path", "README.md"))

    ignored_count = len(candidates) - len(relevant_papers)
    summary = {
        "fetched_candidates": len(candidates),
        "recent_candidates": len(recent_entries),
        "relevant_papers": len(relevant_papers),
        "new_papers": new_count,
        "updated_papers": updated_count,
        "removed_papers": removed_count,
        "expired_papers": expired_count,
        "ignored_papers": max(ignored_count, 0),
        "total_stored_papers": len(merged),
        "used_stale_data": 0,
    }
    LOGGER.info("Fetched candidates: %s", summary["fetched_candidates"])
    LOGGER.info("Relevant papers: %s", summary["relevant_papers"])
    LOGGER.info("New papers: %s", summary["new_papers"])
    LOGGER.info("Updated papers: %s", summary["updated_papers"])
    LOGGER.info("Removed papers: %s", summary["removed_papers"])
    LOGGER.info("Expired papers: %s", summary["expired_papers"])
    LOGGER.info("Ignored papers: %s", summary["ignored_papers"])
    LOGGER.info("Total stored papers: %s", summary["total_stored_papers"])
    print(f"Fetched candidates: {summary['fetched_candidates']}")
    print(f"Relevant papers: {summary['relevant_papers']}")
    print(f"New papers: {summary['new_papers']}")
    print(f"Updated papers: {summary['updated_papers']}")
    print(f"Removed papers: {summary['removed_papers']}")
    print(f"Expired papers: {summary['expired_papers']}")
    print(f"Ignored papers: {summary['ignored_papers']}")
    print(f"Total stored papers: {summary['total_stored_papers']}")
    return summary


def main() -> None:
    logging.basicConfig(
        format="[%(asctime)s %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    parser = argparse.ArgumentParser(description="Update Geometry Vision Daily papers from arXiv.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="Path to config.yaml")
    args = parser.parse_args()
    run_update(args.config)


if __name__ == "__main__":
    main()
