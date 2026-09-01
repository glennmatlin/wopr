"""Handoff provider-pickup documentation tests."""

from __future__ import annotations

from pathlib import Path


def test_handoff_records_provider_preset_pickup_state() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "| HTTP provider presets | done |" in text
    assert "provider preset work is implemented" in text
    assert "small provider-backed LLM and Concordia runs" in text
    assert "next implementation topic is a small provider abstraction" not in text
    assert "Do not start provider-system or live endpoint work" not in text
