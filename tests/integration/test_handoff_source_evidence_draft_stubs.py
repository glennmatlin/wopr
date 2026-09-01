"""Handoff coverage for source-evidence draft stub export."""

from __future__ import annotations

from pathlib import Path


def test_handoff_records_source_evidence_draft_stub_export_branch() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence draft stub export" in text.lower()
    assert "PR [#65](https://github.com/eilab-gt/WOPR/pull/65)" in text
    assert "| Source evidence draft stub export | done |" in text
    assert "| Source evidence draft stub export | current branch |" not in text
    assert "source-evidence-draft-stubs" in text
    assert "2026-06-21-source-evidence-draft-stub-export.md" in text
    assert "2026-06-21-source-evidence-draft-stub-merge-handoff.md" in text
    assert "current branch plan for public-safe draft JSONL stub export" not in text
    assert "current branch plan for recording the PR #65 merge state" not in text
