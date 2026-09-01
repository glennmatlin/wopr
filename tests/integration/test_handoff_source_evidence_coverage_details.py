"""Handoff coverage for the source evidence coverage target details merge."""

from __future__ import annotations

from pathlib import Path


def test_handoff_records_source_evidence_coverage_target_details_merged() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "source evidence coverage target details merged in" in text.lower()
    assert "PR [#60](https://github.com/eilab-gt/WOPR/pull/60)" in text
    assert "| Source evidence coverage target details | done |" in text
    assert "| Source evidence coverage target details | current branch |" not in text
    assert "card_effect_evidence_target_details" in text
    assert "expansion_composition_evidence_target_details" in text
    assert "without creating evidence or clearing blockers" in text
