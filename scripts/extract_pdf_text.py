from __future__ import annotations

from pathlib import Path


def extract_pdf_text(pdf_path: str | Path) -> str:
    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError("PyMuPDF is required for PDF text extraction.") from exc

    path = Path(pdf_path)
    parts: list[str] = []
    with fitz.open(path) as document:
        for page_index, page in enumerate(document, start=1):
            text = page.get_text("text").strip()
            if text:
                parts.append(f"\n\n[Page {page_index}]\n{text}")
    return "\n".join(parts).strip()
