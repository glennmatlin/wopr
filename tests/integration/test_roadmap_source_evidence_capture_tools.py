"""Roadmap coverage for source-evidence capture support tools."""

from __future__ import annotations

from pathlib import Path


def test_roadmap_tracks_source_evidence_capture_support_tools() -> None:
    text = Path("docs/roadmap.md").read_text(encoding="utf-8")

    assert "source-evidence target export" in text
    assert "draft preflight target details" in text
    assert "missing and unverified capture queues" in text
    assert "do not supply source evidence" in text
