from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

import yaml


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"


def load_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    if not isinstance(config, dict):
        raise ValueError(f"Configuration file is empty or invalid: {path}")
    classification = config.get("classification")
    if not isinstance(classification, dict):
        raise ValueError("Missing required config section: classification")
    if not isinstance(classification.get("categories"), dict):
        raise ValueError("Missing required config section: classification.categories")
    if not isinstance(classification.get("category_priority"), list):
        raise ValueError("Missing required config key: classification.category_priority")
    return config


def normalize_text(text: str | None) -> str:
    if not text:
        return ""
    normalized = unicodedata.normalize("NFKC", str(text)).lower()
    normalized = re.sub(r"[\u2010-\u2015\-_/]+", " ", normalized)
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def _contains(normalized_text: str, normalized_keyword: str) -> bool:
    if not normalized_text or not normalized_keyword:
        return False
    pattern = rf"(?<![a-z0-9]){re.escape(normalized_keyword)}(?![a-z0-9])"
    return re.search(pattern, normalized_text) is not None


def _keyword_weight(keyword: str, location: str, representative: bool) -> int:
    if representative:
        return 8 if location == "title" else 6
    is_phrase = len(normalize_text(keyword).split()) > 1
    if location == "title":
        return 4 if is_phrase else 2
    return 2 if is_phrase else 1


def _match_keywords(
    keywords: list[str],
    title_norm: str,
    abstract_norm: str,
    representative_keywords: set[str] | None = None,
) -> tuple[int, list[str], list[str]]:
    representative_keywords = representative_keywords or set()
    score = 0
    matched: list[str] = []
    reasons: list[str] = []

    for keyword in keywords:
        keyword_norm = normalize_text(keyword)
        if not keyword_norm:
            continue
        representative = keyword_norm in representative_keywords
        title_hit = _contains(title_norm, keyword_norm)
        abstract_hit = _contains(abstract_norm, keyword_norm)
        if not title_hit and not abstract_hit:
            continue

        matched.append(keyword)
        if title_hit:
            weight = _keyword_weight(keyword, "title", representative)
            score += weight
            if representative:
                reasons.append(f"Matched representative model name in title: {keyword}")
            elif len(keyword_norm.split()) > 1:
                reasons.append(f"Matched title phrase: {keyword}")
            else:
                reasons.append(f"Matched title keyword: {keyword}")
        if abstract_hit:
            weight = _keyword_weight(keyword, "abstract", representative)
            score += weight
            if representative:
                reasons.append(f"Matched representative model name in abstract: {keyword}")
            elif len(keyword_norm.split()) > 1:
                reasons.append(f"Matched abstract phrase: {keyword}")
            else:
                reasons.append(f"Matched abstract keyword: {keyword}")

    return score, matched, reasons


def _unique_in_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        key = normalize_text(value)
        if key in seen:
            continue
        seen.add(key)
        output.append(value)
    return output


def _score_exclusions(
    title_norm: str,
    abstract_norm: str,
    classification_config: dict[str, Any],
) -> tuple[list[str], list[str], list[str]]:
    exclude_keywords = classification_config.get("exclude_keywords", [])
    strict_exclude_keywords = classification_config.get("strict_exclude_keywords", [])
    rescue_keywords = classification_config.get("exclusion_rescue_keywords", [])
    if (
        not isinstance(exclude_keywords, list)
        or not isinstance(strict_exclude_keywords, list)
        or not isinstance(rescue_keywords, list)
    ):
        raise ValueError(
            "classification.exclude_keywords, strict_exclude_keywords, and exclusion_rescue_keywords must be lists"
        )

    text_norm = f"{title_norm} {abstract_norm}".strip()
    excluded = [
        keyword
        for keyword in exclude_keywords
        if _contains(text_norm, normalize_text(str(keyword)))
    ]
    strict_excluded = [
        keyword
        for keyword in strict_exclude_keywords
        if _contains(text_norm, normalize_text(str(keyword)))
    ]
    rescued = [
        keyword
        for keyword in rescue_keywords
        if _contains(text_norm, normalize_text(str(keyword)))
    ]
    return _unique_in_order(excluded), _unique_in_order(strict_excluded), _unique_in_order(rescued)


def classify_paper(
    title: str,
    abstract: str,
    arxiv_categories: list[str] | None = None,
    config: dict[str, Any] | None = None,
) -> dict[str, Any]:
    config = config or load_config()
    classification_config = config["classification"]
    priority: list[str] = classification_config["category_priority"]
    category_config: dict[str, Any] = classification_config["categories"]
    relevance_threshold = int(classification_config.get("relevance_threshold", 4))
    secondary_threshold = int(classification_config.get("secondary_category_threshold", 3))

    title_norm = normalize_text(title)
    abstract_norm = normalize_text(abstract)
    excluded_keywords, strict_excluded_keywords, rescue_keywords = _score_exclusions(
        title_norm, abstract_norm, classification_config
    )

    if strict_excluded_keywords or (excluded_keywords and not rescue_keywords):
        matched_exclusions = strict_excluded_keywords or excluded_keywords
        return {
            "is_relevant": False,
            "primary_category": None,
            "secondary_categories": [],
            "matched_keywords": matched_exclusions,
            "classification_score": 0,
            "classification_reasons": [
                "Excluded by non-geometry topic keywords: " + ", ".join(matched_exclusions)
            ],
        }

    representative_config = classification_config.get("representative_models", {})
    scores: dict[str, int] = {}
    matched_by_category: dict[str, list[str]] = {}
    reasons_by_category: dict[str, list[str]] = {}

    for category in priority:
        data = category_config.get(category)
        if not isinstance(data, dict):
            raise ValueError(f"Missing category configuration for: {category}")
        keywords = data.get("include_keywords")
        if not isinstance(keywords, list):
            raise ValueError(f"Category include_keywords must be a list: {category}")
        representative_keywords = {
            normalize_text(str(keyword))
            for keyword in representative_config.get(category, [])
        }
        score, matched, reasons = _match_keywords(
            [str(keyword) for keyword in keywords],
            title_norm,
            abstract_norm,
            representative_keywords,
        )
        scores[category] = score
        matched_by_category[category] = matched
        reasons_by_category[category] = reasons

    embodied_category = "Embodied / Robotics / AR Applications"
    if scores.get(embodied_category, 0) > 0:
        has_geometry_support = bool(rescue_keywords) or any(
            scores.get(category, 0) >= secondary_threshold
            for category in priority
            if category != embodied_category
        )
        if not has_geometry_support:
            scores[embodied_category] = 0
            matched_by_category[embodied_category] = []
            reasons_by_category[embodied_category] = [
                "Ignored application keywords without explicit geometry, reconstruction, localization, or mapping support."
            ]

    eligible = [category for category in priority if scores.get(category, 0) >= relevance_threshold]
    if not eligible:
        reasons = []
        if excluded_keywords and rescue_keywords:
            reasons.append(
                "Rescued from exclusion by geometry keywords: " + ", ".join(rescue_keywords)
            )
        return {
            "is_relevant": False,
            "primary_category": None,
            "secondary_categories": [],
            "matched_keywords": _unique_in_order(
                [keyword for category in priority for keyword in matched_by_category[category]]
            ),
            "classification_score": max(scores.values(), default=0),
            "classification_reasons": reasons or ["No category reached the relevance threshold."],
        }

    primary_category = eligible[0]
    secondary_categories = [
        category
        for category in priority
        if category != primary_category and scores.get(category, 0) >= secondary_threshold
    ]
    matched_keywords = _unique_in_order(
        [keyword for category in priority for keyword in matched_by_category[category]]
    )
    reasons = []
    if excluded_keywords and rescue_keywords:
        reasons.append("Rescued from exclusion by geometry keywords: " + ", ".join(rescue_keywords))
    for category in [primary_category, *secondary_categories]:
        reasons.extend(reasons_by_category[category])

    return {
        "is_relevant": True,
        "primary_category": primary_category,
        "secondary_categories": secondary_categories,
        "matched_keywords": matched_keywords,
        "classification_score": scores[primary_category],
        "classification_reasons": _unique_in_order(reasons),
    }


__all__ = ["classify_paper", "load_config", "normalize_text"]
