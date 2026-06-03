from datetime import datetime, timezone

from scripts.generate_readme import DISCLAIMER, load_config, render_readme


CONFIG = load_config()
NOW = datetime(2026, 6, 3, 12, 0, tzinfo=timezone.utc)


def test_readme_category_order_is_stable() -> None:
    readme = render_readme([], CONFIG, now=NOW)

    expected = [
        "## Geometry Foundation Models",
        "## Dynamic / 4D Reconstruction",
        "## 3D Reconstruction & Multi-view Geometry",
        "## Neural Scene Representations & Rendering",
        "## Embodied / Robotics / AR Applications",
    ]
    positions = [readme.index(item) for item in expected]
    assert positions == sorted(positions)


def test_readme_date_sorting_and_links() -> None:
    papers = [
        _paper("2501.00001", "Older Recent Paper", "2026-06-01T12:00:00Z"),
        _paper("2501.00002", "Newest Recent Paper", "2026-06-02T12:00:00Z"),
    ]

    readme = render_readme(papers, CONFIG, now=NOW)

    assert readme.index("Newest Recent Paper") < readme.index("Older Recent Paper")
    assert "[abs](https://arxiv.org/abs/2501.00002)" in readme
    assert "[pdf](https://arxiv.org/pdf/2501.00002)" in readme


def test_readme_hides_papers_outside_configured_window_but_keeps_archive_link() -> None:
    papers = [
        _paper("2501.00001", "Recent Paper", "2026-06-01T12:00:00Z"),
        _paper("2412.99999", "Old Paper", "2026-05-20T12:00:00Z"),
    ]

    readme = render_readme(papers, CONFIG, now=NOW)

    assert "Recent Paper" in readme
    assert "Old Paper" not in readme
    assert "Rolling 7-day structured archive: [data/papers.json](data/papers.json)" in readme


def test_same_input_generates_identical_readme() -> None:
    papers = [_paper("2501.00001", "Deterministic Paper", "2026-06-01T12:00:00Z")]

    first = render_readme(papers, CONFIG, now=NOW)
    second = render_readme(papers, CONFIG, now=NOW)

    assert first == second


def test_readme_contains_complete_disclaimer() -> None:
    readme = render_readme([], CONFIG, now=NOW)

    assert DISCLAIMER in readme


def _paper(arxiv_id: str, title: str, published: str) -> dict:
    return {
        "arxiv_id": arxiv_id,
        "version": "v1",
        "title": title,
        "authors": ["Author One", "Author Two"],
        "abstract": "This paper studies 3D reconstruction from multiple images.",
        "published": published,
        "updated": published,
        "primary_arxiv_category": "cs.CV",
        "arxiv_categories": ["cs.CV"],
        "primary_category": "Geometry Foundation Models",
        "secondary_categories": ["3D Reconstruction & Multi-view Geometry"],
        "matched_keywords": ["VGGT", "3D reconstruction"],
        "classification_score": 8,
        "classification_reasons": ["Matched representative model name: VGGT"],
        "abstract_url": f"https://arxiv.org/abs/{arxiv_id}",
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
        "first_seen": "2026-06-03T08:17:00-04:00",
        "last_seen": "2026-06-03T08:17:00-04:00",
    }
