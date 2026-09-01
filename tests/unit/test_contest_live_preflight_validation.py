"""Tamper checks for live preflight receipts."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

import pytest
from tests.unit.test_contest_live_preflight import RecordingTransport, _candidate

from nuclear_war_contest.live_preflight import (
    run_candidate_preflight,
    validate_live_preflight_receipt,
)
from nuclear_war_contest.live_preflight_auth import (
    build_live_preflight_approval,
    validate_live_preflight_approval,
)
from nuclear_war_contest.preflight_types import CandidateManifest

EXECUTOR_REVISION = "a" * 40


def _receipt(
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[CandidateManifest, dict[str, Any]]:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    manifest = _candidate()
    receipt = run_candidate_preflight(
        manifest,
        transport=RecordingTransport(),
        allow_network=True,
        authorization=build_live_preflight_approval(
            manifest, EXECUTOR_REVISION, manifest.proposed_max_cost_usd
        ),
        executor_revision=EXECUTOR_REVISION,
    )
    return manifest, receipt


def test_live_preflight_receipt_rejects_duplicate_attempts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    tampered = deepcopy(receipt)
    tampered["attempts"][-1] = deepcopy(tampered["attempts"][0])

    with pytest.raises(ValueError, match="attempt keys"):
        validate_live_preflight_receipt(tampered, manifest)


def test_live_preflight_receipt_rejects_study_seed_drift(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    receipt["study_seeds"] = [51]

    with pytest.raises(ValueError, match="study seeds"):
        validate_live_preflight_receipt(receipt, manifest)


def test_live_preflight_receipt_rejects_zero_attempt_for_passed_call(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    receipt["attempts"][0]["provider_attempts"] = 0
    receipt["network_calls"] -= 1

    with pytest.raises(ValueError, match="passed attempt"):
        validate_live_preflight_receipt(receipt, manifest)


def test_live_preflight_receipt_rejects_retry_accounting_drift(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    receipt["attempts"][0]["provider_attempts"] = 2
    receipt["network_calls"] += 1

    with pytest.raises(ValueError, match="retry accounting"):
        validate_live_preflight_receipt(receipt, manifest)


def test_live_preflight_receipt_rejects_request_bound_drift(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    receipt["request_bound"]["provider_attempts"] = 1

    with pytest.raises(ValueError, match="request bound"):
        validate_live_preflight_receipt(receipt, manifest)


def test_live_preflight_receipt_rejects_prompt_hash_drift(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest, receipt = _receipt(monkeypatch)
    receipt["attempts"][0]["prompt_sha256"] = "bad"

    with pytest.raises(ValueError, match="prompt hash"):
        validate_live_preflight_receipt(receipt, manifest)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("candidate_manifest_hash", "bad", "candidate"),
        ("endpoints", ["https://wrong.example"], "endpoints"),
        ("max_spend_usd", 1.0, "spend"),
        ("executor_revision", "b" * 40, "executor revision"),
    ],
)
def test_live_preflight_approval_is_candidate_bound(
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    value: object,
    message: str,
) -> None:
    monkeypatch.setenv("TOGETHER_API_KEY", "test-secret")
    manifest = _candidate()
    approval = build_live_preflight_approval(
        manifest, EXECUTOR_REVISION, manifest.proposed_max_cost_usd
    )
    approval[field] = value

    with pytest.raises(ValueError, match=message):
        validate_live_preflight_approval(manifest, approval, EXECUTOR_REVISION)
