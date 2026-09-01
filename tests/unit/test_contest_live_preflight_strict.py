"""Strict evidence and cap tamper checks for live preflight receipts."""

from __future__ import annotations

import pytest
from tests.unit.test_contest_live_preflight_validation import _receipt

from nuclear_war_contest.live_preflight import validate_live_preflight_receipt


def test_live_preflight_receipt_rejects_unknown_attempt_fields(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    receipt["attempts"][0]["unbound_evidence"] = True

    with pytest.raises(ValueError, match="attempt fields"):
        validate_live_preflight_receipt(receipt, manifest)


def test_live_preflight_receipt_rejects_per_attempt_cap_drift(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    receipt["attempts"][0]["provider_attempts"] = 4
    receipt["attempts"][0]["provider_transport_retries"] = 3
    receipt["network_calls"] += 3

    with pytest.raises(ValueError, match="per-attempt request cap"):
        validate_live_preflight_receipt(receipt, manifest)


def test_live_preflight_receipt_requires_success_usage(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    receipt["attempts"][0]["provider_usage"] = None

    with pytest.raises(ValueError, match="usage"):
        validate_live_preflight_receipt(receipt, manifest)
