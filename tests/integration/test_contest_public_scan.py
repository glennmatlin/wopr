"""Read-only publication-boundary checks for the contest packet."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.public_scan import audit_public_packet


def test_checked_in_contest_packet_has_no_scan_findings() -> None:
    root = Path(__file__).parents[2] / "docs" / "contest"
    report = audit_public_packet(root)

    assert report["ok"] is True
    assert report["findings"] == []
    warnings = report["warnings"]
    assert isinstance(warnings, list)
    assert any("local checkout link" in item for item in warnings)
    assert isinstance(report["files_scanned"], int)
    assert isinstance(report["local_links_checked"], int)
    assert report["files_scanned"] > 0
    assert report["local_links_checked"] > 0


def test_public_scan_rejects_credentials_exclusions_and_broken_links(
    tmp_path: Path,
) -> None:
    packet = tmp_path / "packet"
    packet.mkdir()
    (packet / "index.md").write_text(
        '[missing](missing.md)\n"api_key": "01234567890123456789"\n',
        encoding="utf-8",
    )
    private = packet / "private"
    private.mkdir()
    (private / "notes.txt").write_text("owner note", encoding="utf-8")

    report = audit_public_packet(packet)

    assert report["ok"] is False
    findings = report["findings"]
    assert isinstance(findings, list)
    assert any("broken local link" in item for item in findings)
    assert any("credential-like value" in item for item in findings)
    assert any("excluded path" in item for item in findings)
