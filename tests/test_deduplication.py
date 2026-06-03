import json

from datetime import datetime, timezone

from scripts.update_papers import (
    normalize_arxiv_id,
    prune_papers_by_retention,
    upsert_papers,
    write_json_atomic,
)


def test_normalize_arxiv_id_removes_version_suffix() -> None:
    assert normalize_arxiv_id("2501.01234v2") == ("2501.01234", "v2")
    assert normalize_arxiv_id("https://arxiv.org/abs/2501.01234v1") == ("2501.01234", "v1")


def test_same_arxiv_id_is_not_written_twice() -> None:
    merged, new_count, updated_count = upsert_papers(
        [],
        [_paper("2501.01234v1"), _paper("2501.01234v2", title="Updated Paper", version="v2")],
        "2026-06-03T08:17:00-04:00",
    )

    assert len(merged) == 1
    assert merged[0]["arxiv_id"] == "2501.01234"
    assert merged[0]["version"] == "v2"
    assert new_count == 1
    assert updated_count == 1


def test_v2_update_preserves_first_seen_and_updates_last_seen() -> None:
    existing = [
        {
            **_paper("2501.01234", version="v1"),
            "first_seen": "2026-06-01T08:17:00-04:00",
            "last_seen": "2026-06-01T08:17:00-04:00",
        }
    ]

    merged, new_count, updated_count = upsert_papers(
        existing,
        [_paper("2501.01234v2", title="Updated Paper", version="v2")],
        "2026-06-03T08:17:00-04:00",
    )

    assert len(merged) == 1
    assert new_count == 0
    assert updated_count == 1
    assert merged[0]["version"] == "v2"
    assert merged[0]["title"] == "Updated Paper"
    assert merged[0]["first_seen"] == "2026-06-01T08:17:00-04:00"
    assert merged[0]["last_seen"] == "2026-06-03T08:17:00-04:00"


def test_atomic_write_keeps_valid_json(tmp_path) -> None:
    path = tmp_path / "papers.json"
    papers = [_paper("2501.01234")]

    write_json_atomic(path, papers)

    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    assert loaded == papers


def test_prune_papers_by_retention_removes_entries_older_than_window() -> None:
    papers = [
        _paper("2501.01234", title="Recent Paper", published="2026-06-02T12:00:00Z"),
        _paper("2501.01235", title="Expired Paper", published="2026-05-24T12:00:00Z"),
    ]

    kept, removed_count = prune_papers_by_retention(
        papers,
        retention_days=7,
        now=datetime(2026, 6, 3, 12, 0, tzinfo=timezone.utc),
    )

    assert removed_count == 1
    assert [paper["title"] for paper in kept] == ["Recent Paper"]


def _paper(
    arxiv_id: str,
    title: str = "Example Paper",
    version: str = "v1",
    published: str = "2026-06-02T12:00:00Z",
) -> dict:
    normalized_id, parsed_version = normalize_arxiv_id(arxiv_id)
    return {
        "arxiv_id": normalized_id,
        "version": parsed_version or version,
        "title": title,
        "authors": ["Author One", "Author Two"],
        "abstract": "Paper abstract about 3D reconstruction.",
        "published": published,
        "updated": published,
        "primary_arxiv_category": "cs.CV",
        "arxiv_categories": ["cs.CV"],
        "primary_category": "3D Reconstruction & Multi-view Geometry",
        "secondary_categories": [],
        "matched_keywords": ["3D reconstruction"],
        "classification_score": 4,
        "classification_reasons": ["Matched title phrase: 3D reconstruction"],
        "abstract_url": f"https://arxiv.org/abs/{normalized_id}",
        "pdf_url": f"https://arxiv.org/pdf/{normalized_id}",
    }
