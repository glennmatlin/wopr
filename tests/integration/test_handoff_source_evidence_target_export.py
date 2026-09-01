"""Handoff coverage for the source evidence target export merge."""

from __future__ import annotations

from pathlib import Path


def test_handoff_records_source_evidence_target_export_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence target export command merged in" in text.lower()
    assert "PR [#59](https://github.com/eilab-gt/WOPR/pull/59)" in text
    assert "| Source evidence target export | done |" in text
    assert "| Source evidence target export | current branch |" not in text
    assert "nuclear-war source-evidence-targets" in text
