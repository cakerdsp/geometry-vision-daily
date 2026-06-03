from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


KNOWN_TASKS = {
    "summarize abstracts": ("summarize abstracts", "简析", "摘要分析"),
    "full-text analysis": ("full-text analysis", "全文分析", "全文解读"),
    "generate daily trend report": ("generate daily trend report", "每日趋势报告", "趋势报告"),
}


@dataclass
class InterestProfile:
    raw_text: str
    tasks: set[str]
    keywords: list[str]
    instructions: str
    experimental_tasks: list[str]


def parse_interests(path: str | Path) -> InterestProfile:
    file_path = Path(path)
    raw_text = file_path.read_text(encoding="utf-8") if file_path.exists() else ""
    active_lines = [
        line.strip(" \t-")
        for line in raw_text.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    active_text = "\n".join(active_lines)
    lowered = active_text.lower()

    tasks: set[str] = set()
    for task, aliases in KNOWN_TASKS.items():
        if any(alias.lower() in lowered for alias in aliases):
            tasks.add(task)

    keywords: list[str] = []
    experimental_tasks: list[str] = []
    for line in active_lines:
        normalized = line.lower()
        if any(alias.lower() in normalized for aliases in KNOWN_TASKS.values() for alias in aliases):
            continue
        if "experimental" in normalized or "实验性" in normalized:
            experimental_tasks.append(line)
            continue
        candidates = re.split(r"[，,、;；]", line)
        for candidate in candidates:
            value = candidate.strip()
            if value and len(value) <= 80:
                keywords.append(value)

    return InterestProfile(
        raw_text=raw_text,
        tasks=tasks,
        keywords=_unique(keywords),
        instructions=active_text,
        experimental_tasks=experimental_tasks,
    )


def _unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        output.append(value)
    return output
