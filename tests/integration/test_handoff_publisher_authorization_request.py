"""Handoff coverage for publisher authorization request packet branch."""

from __future__ import annotations

from pathlib import Path


def test_handoff_records_publisher_authorization_request_branch() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "publisher authorization request packet" in text.lower()
    assert "| Publisher authorization request packet | done |" in text
    assert "PUBLISHER_AUTHORIZATION_REQUEST.md" in text


def test_handoff_records_public_source_leads_branch() -> None:
    text = Path("docs/AGENT_HANDOFF.md").read_text(encoding="utf-8")

    assert "official public source leads inventory" in text.lower()
    assert "PR [#63](https://github.com/eilab-gt/WOPR/pull/63)" in text
    assert "| Official public source leads inventory | done |" in text
    assert "| Official public source leads inventory | current branch |" not in text
    assert "2026-06-21-public-source-leads-inventory.md" in text
    assert "2026-06-21-public-source-leads-merge-handoff.md" in text
    assert "PUBLIC_SOURCE_LEADS.md" in text
