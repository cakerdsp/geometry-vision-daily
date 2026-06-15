from datetime import datetime, timezone
from pathlib import Path

from scripts.analysis_io import ensure_state_shape
from scripts.fetch_new_papers import fetch_new_papers
from scripts.generate_readme import load_config, render_readme
from scripts.parse_interests import parse_interests
from scripts.summarize_abstracts import build_brief_prompt
from scripts.summarize_abstracts import summarize_abstracts
from scripts.summarize_full_text import summarize_full_texts


class FakeClient:
    def __init__(self) -> None:
        self.calls = []

    def chat(self, messages, task, max_tokens, arxiv_id=None):
        self.calls.append(
            {
                "messages": messages,
                "task": task,
                "max_tokens": max_tokens,
                "arxiv_id": arxiv_id,
            }
        )
        content = "### Metadata\n- 标题：测试论文\n\n### 一句话总结\n这是一段中文分析。"
        if task == "full_text_synthesis":
            content = "## 全文分析\n### 核心结论\n这是全文中文分析。"
        if task == "full_text_chunk":
            content = "- 本片段核心内容：测试片段。"
        return type(
            "Result",
            (),
            {
                "content": content,
                "prompt_tokens": 10,
                "completion_tokens": 10,
                "total_tokens": 20,
                "estimated_cost_usd": 0.0,
                "estimated_cost_cny": 0.0,
            },
        )()


def test_parse_interests_supports_tasks_and_keywords(tmp_path) -> None:
    interests_path = tmp_path / "interests.md"
    interests_path.write_text(
        """
# today
- full-text analysis
- generate daily trend report
- VGGT、动态场景重建
""",
        encoding="utf-8",
    )

    profile = parse_interests(interests_path)

    assert "full-text analysis" in profile.tasks
    assert "generate daily trend report" in profile.tasks
    assert "VGGT" in profile.keywords
    assert "动态场景重建" in profile.keywords


def test_summarize_abstracts_writes_state_and_markdown(tmp_path) -> None:
    config = _analysis_config(tmp_path)
    interests = parse_interests(tmp_path / "missing.md")
    state = ensure_state_shape({})
    client = FakeClient()

    count = summarize_abstracts([_paper()], state, config, interests, client)

    assert count == 1
    brief = state["papers"]["2606.00001"]["brief"]
    assert brief["status"] == "success"
    assert "中文分析" in brief["markdown"]
    assert Path(brief["path"]).exists()


def test_brief_prompt_does_not_request_related_method_section(tmp_path) -> None:
    interests = parse_interests(tmp_path / "missing.md")

    prompt = build_brief_prompt(_paper(), interests)

    assert "### 与相关方法的关系" not in prompt
    assert "VGGT、DUSt3R、MASt3R、CroCo" not in prompt


def test_prompt_version_change_requeues_existing_brief_summary() -> None:
    paper = _paper()
    state = {
        "papers": {
            "2606.00001": {
                "brief": {
                    "status": "success",
                    "input_hash": "stale",
                    "prompt_version": "brief-v1",
                }
            }
        }
    }

    selected = fetch_new_papers([paper], state, max_papers=10, prompt_version="brief-v2-no-related-methods")

    assert selected == [paper]


def test_full_text_analysis_downloads_temporarily_and_writes_links(tmp_path, monkeypatch) -> None:
    config = _analysis_config(tmp_path)
    interests_path = tmp_path / "interests.md"
    interests_path.write_text("full-text analysis\nVGGT", encoding="utf-8")
    interests = parse_interests(interests_path)
    state = ensure_state_shape({})
    client = FakeClient()

    def fake_download(pdf_url, output_path, timeout_seconds=60):
        path = Path(output_path)
        path.write_bytes(b"%PDF fake")
        return path

    monkeypatch.setattr("scripts.summarize_full_text.download_pdf", fake_download)
    monkeypatch.setattr(
        "scripts.summarize_full_text.extract_pdf_text",
        lambda path: "Introduction\nThis paper studies VGGT and 3D reconstruction.\nConclusion\nDone.",
    )

    count = summarize_full_texts([_paper()], state, config, interests, client)

    assert count == 1
    full_text = state["papers"]["2606.00001"]["full_text"]
    assert full_text["status"] == "success"
    assert Path(full_text["path"]).exists()
    assert "全文分析" in Path(full_text["path"]).read_text(encoding="utf-8")


def test_readme_includes_daily_report_and_brief_analysis() -> None:
    config = load_config()
    processed = {
        "papers": {
            "2606.00001": {
                "brief": {
                    "status": "success",
                    "markdown": "### 一句话总结\n中文简析。",
                },
                "full_text": {
                    "status": "success",
                    "path": "interests/full-text-2026-06-03-2606.00001.md",
                },
            }
        }
    }

    readme = render_readme(
        [_paper()],
        config,
        now=datetime(2026, 6, 4, tzinfo=timezone.utc),
        processed_state=processed,
        daily_report_markdown="# 每日总览\n\n来源：测试。",
    )

    assert "<!-- DAILY_REPORT_START -->" in readme
    assert "中文简析" in readme
    assert "interests/full-text-2026-06-03-2606.00001.md" in readme


def _analysis_config(tmp_path) -> dict:
    return {
        "analysis": {
            "brief_summary_dir": str(tmp_path / "summaries" / "brief"),
            "interests_output_dir": str(tmp_path / "interests"),
            "full_text_summary_dir": str(tmp_path / "summaries" / "full-text"),
            "max_full_text_summaries_per_run": 1,
            "chunk_size": 200,
            "max_chunks_per_paper": 2,
            "max_tokens": {
                "brief_summary": 200,
                "chunk_summary": 200,
                "full_text_synthesis": 200,
            },
        }
    }


def _paper() -> dict:
    return {
        "arxiv_id": "2606.00001",
        "title": "VGGT for 3D Reconstruction",
        "authors": ["Author One"],
        "abstract": "We study camera prediction and 3D reconstruction.",
        "published": "2026-06-03T00:00:00Z",
        "primary_category": "Geometry Foundation Models",
        "secondary_categories": ["3D Reconstruction & Multi-view Geometry"],
        "abstract_url": "https://arxiv.org/abs/2606.00001",
        "pdf_url": "https://arxiv.org/pdf/2606.00001",
        "matched_keywords": ["VGGT"],
        "classification_score": 10,
    }
