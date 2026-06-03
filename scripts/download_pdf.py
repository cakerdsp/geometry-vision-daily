from __future__ import annotations

from pathlib import Path

import requests


def download_pdf(pdf_url: str, output_path: str | Path, timeout_seconds: int = 60) -> Path:
    if not pdf_url:
        raise ValueError("Missing PDF URL.")
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(pdf_url, timeout=timeout_seconds)
    response.raise_for_status()
    content = response.content
    if not content.startswith(b"%PDF"):
        raise ValueError(f"Downloaded content does not look like a PDF: {pdf_url}")
    path.write_bytes(content)
    return path
