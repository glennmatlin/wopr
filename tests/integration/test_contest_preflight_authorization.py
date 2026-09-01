"""Receipt-backed authorization gates for live contest execution."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

import pytest
from tests.integration.preflight_authorization_support import (
    approved_live_payload,
    base_payload,
)

from nuclear_war_contest.manifest import load_study_manifest
from nuclear_war_contest.preflight import (
    candidate_manifest_hash,
    load_candidate_manifest,
)
from nuclear_war_contest.runner import run_matched_study
from nuclear_war_contest.runner_execution import validate_execution_budget


def test_live_manifest_requires_budget_before_runner_call(tmp_path: Path) -> None:
    payload = base_payload()
    payload["models"][0].update(backend="concordia_http", provider="together")  # type: ignore[index]
    manifest = load_study_manifest(payload)
    called = False

    def unexpected_runner(_: dict[str, object]) -> dict[str, object]:
        nonlocal called
        called = True
        return {}

    with pytest.raises(ValueError, match="frozen request_budget"):
        run_matched_study(manifest, tmp_path, runner=unexpected_runner)
    assert not called


def test_live_manifest_requires_receipt_packet(tmp_path: Path) -> None:
    payload = base_payload()
    payload["models"][0].update(backend="concordia_http", provider="together")  # type: ignore[index]
    payload["request_budget"] = {
        "max_c2_calls_per_game": 2048,
        "max_press_calls_per_game": 160,
    }
    manifest = load_study_manifest(payload)
    with pytest.raises(ValueError, match="receipt-backed preflight packet"):
        run_matched_study(manifest, tmp_path, runner=lambda _: {})
    assert not (tmp_path / "STUDY_MANIFEST.json").exists()


def test_live_manifest_binds_promoted_packet_and_settings(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    payload = approved_live_payload(tmp_path, monkeypatch)
    validate_execution_budget(load_study_manifest(payload))
    payload["models"][0]["client"]["temperature"] = 0.5  # type: ignore[index]
    with pytest.raises(ValueError, match="model settings"):
        validate_execution_budget(load_study_manifest(payload))


def test_live_manifest_rechecks_executor_identity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    payload = approved_live_payload(tmp_path, monkeypatch)
    monkeypatch.setattr(
        "nuclear_war_contest.preflight_authorization.verify_executor_revision",
        lambda _: (_ for _ in ()).throw(ValueError("dirty executor")),
    )

    with pytest.raises(ValueError, match="dirty executor"):
        validate_execution_budget(load_study_manifest(payload))


def test_checked_in_candidate_study_manifest_stays_pending_owner(
    tmp_path: Path,
) -> None:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.candidate.json"
    )
    manifest = load_study_manifest(json.loads(path.read_text(encoding="utf-8")))
    docs = path.parent
    receipt_path = docs / "MODEL_PREFLIGHT_RECEIPT.json"
    candidate_path = docs / "MODEL_MANIFEST.candidate.json"
    candidate = load_candidate_manifest(
        json.loads(candidate_path.read_text(encoding="utf-8")), base_dir=docs
    )
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))

    assert (
        sha256(receipt_path.read_bytes()).hexdigest() == manifest.preflight_receipt_hash
    )
    assert (
        candidate_manifest_hash(candidate) == manifest.preflight_candidate_manifest_hash
    )
    assert (
        receipt["candidate_manifest_hash"] == manifest.preflight_candidate_manifest_hash
    )
    with pytest.raises(ValueError, match="approved preflight receipt"):
        run_matched_study(manifest, tmp_path, runner=lambda _: {})
    assert not (tmp_path / "STUDY_MANIFEST.json").exists()
