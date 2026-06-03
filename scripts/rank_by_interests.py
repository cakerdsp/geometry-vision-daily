from __future__ import annotations

import re
from typing import Any

from scripts.parse_interests import InterestProfile


def rank_by_interests(
    papers: list[dict[str, Any]],
    interests: InterestProfile,
    top_n: int,
) -> list[dict[str, Any]]:
    ranked = sorted(
        papers,
        key=lambda paper: (_score_paper(paper, interests), str(paper.get("published", ""))),
        reverse=True,
    )
    return ranked[:top_n]


def _score_paper(paper: dict[str, Any], interests: InterestProfile) -> int:
    text = " ".join(
        [
            str(paper.get("title", "")),
            str(paper.get("abstract", "")),
            str(paper.get("primary_category", "")),
            " ".join(str(value) for value in paper.get("secondary_categories", [])),
        ]
    ).lower()
    score = int(paper.get("classification_score", 0) or 0)
    for keyword in interests.keywords:
        normalized = keyword.lower().strip()
        if not normalized:
            continue
        if re.search(re.escape(normalized), text):
            score += 10
    return score
