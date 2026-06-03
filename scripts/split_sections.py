from __future__ import annotations

import re


SECTION_PATTERN = re.compile(
    r"(?im)^(abstract|introduction|related work|method|methods|approach|experiments|results|discussion|conclusion|references)\b.*$"
)


def split_sections(text: str, chunk_size: int) -> list[str]:
    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        return []
    sections = _split_by_headings(text)
    chunks: list[str] = []
    for section in sections or [cleaned]:
        chunks.extend(_split_by_chars(section, chunk_size))
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def _split_by_headings(text: str) -> list[str]:
    matches = list(SECTION_PATTERN.finditer(text))
    if len(matches) < 2:
        return []
    sections: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[start:end].strip()
        if section:
            sections.append(section)
    return sections


def _split_by_chars(text: str, chunk_size: int) -> list[str]:
    if len(text) <= chunk_size:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        if end < len(text):
            boundary = text.rfind("。", start, end)
            if boundary <= start:
                boundary = text.rfind(".", start, end)
            if boundary > start:
                end = boundary + 1
        chunks.append(text[start:end])
        start = end
    return chunks
