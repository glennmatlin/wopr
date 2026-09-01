"""Approval and resumability gates for the bounded three-model screen."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
from tests.integration.contest_model_screening_support import (
    offline_runner,
    one_failure_runner,
)

from nuclear_war_contest.screening_execution import run_screening
from nuclear_war_contest.screening_manifest import load_screening_manifest_file

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCREENING_MANIFEST = PROJECT_ROOT / "docs/contest/MODEL_SCREENING.candidate.json"


def test_screening_rejects_pending_approval_before_output_or_runner(
    tmp_path: Path,
) -> None:
    manifest, digest = _manifest_and_hash()
    approval = _approval(manifest, digest)
    approval["approved"] = False
    with pytest.raises(ValueError, match="not approved"):
        run_screening(
            manifest,
            digest,
            approval,
            "0" * 40,
            allow_network=True,
            out_dir=tmp_path,
        )
    assert not list(tmp_path.iterdir())


def test_screening_requires_explicit_network_flag(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    manifest, digest = _manifest_and_hash()
    approval = _approval(manifest, digest)
    monkeypatch.setattr(
        "nuclear_war_contest.screening_execution.verify_executor_revision",
        lambda _: None,
    )

    with pytest.raises(ValueError, match="allow-network"):
        run_screening(
            manifest,
            digest,
            approval,
            "0" * 40,
            allow_network=False,
            out_dir=tmp_path,
        )
    assert not list(tmp_path.iterdir())


def test_screening_approval_binds_exact_provider_model_ids(
    tmp_path: Path,
) -> None:
    manifest, digest = _manifest_and_hash()
    approval = _approval(manifest, digest)
    approval["model_ids"] = sorted(model.model_id for model in manifest.models)

    with pytest.raises(ValueError, match="models do not match"):
        run_screening(
            manifest,
            digest,
            approval,
            "0" * 40,
            allow_network=True,
            out_dir=tmp_path,
        )


def test_screening_uses_nonbillable_transport_fixture_and_writes_nine_receipts(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    manifest, digest = _manifest_and_hash()
    approval = _approval(manifest, digest)
    monkeypatch.setattr(
        "nuclear_war_contest.screening_execution.verify_executor_revision",
        lambda _: None,
    )

    monkeypatch.setattr(
        "nuclear_war_contest.screening_execution.run_payload", offline_runner
    )

    summary = run_screening(
        manifest,
        digest,
        approval,
        "0" * 40,
        allow_network=True,
        out_dir=tmp_path,
    )

    assert len(summary["attempts"]) == 9
    assert all(row["status"] == "completed" for row in summary["attempts"])
    assert all(row["communication"] == "press_light" for row in summary["attempts"])
    assert all(row["execution_approval_hash"] for row in summary["attempts"])
    assert summary["selection"]["selection_status"] == "insufficient"
    assert summary["selection"]["eligible_model_ids"] == []
    execution = json.loads(
        (tmp_path / "SCREENING_EXECUTION_MANIFEST.json").read_text()
    )
    assert execution["executor_revision"] == "0" * 40
    assert execution["study_manifest_hash"] == summary["study_manifest_hash"]
    assert len(list((tmp_path / "attempts").glob("*/attempt.json"))) == 9
    assert (tmp_path / "screening_summary.json").is_file()


def test_screening_summary_exposes_failed_cells(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    manifest, digest = _manifest_and_hash()
    approval = _approval(manifest, digest)
    monkeypatch.setattr(
        "nuclear_war_contest.screening_execution.verify_executor_revision",
        lambda _: None,
    )
    monkeypatch.setattr(
        "nuclear_war_contest.screening_execution.run_payload",
        one_failure_runner(),
    )

    summary = run_screening(
        manifest,
        digest,
        approval,
        "0" * 40,
        allow_network=True,
        out_dir=tmp_path,
    )

    assert summary["screening_status"] == "completed_with_failures"
    assert sum(row["status"] == "failed" for row in summary["attempts"]) == 1
    assert summary["selection"]["selection_status"] == "insufficient"


def _manifest_and_hash():
    return (
        load_screening_manifest_file(SCREENING_MANIFEST),
        hashlib.sha256(SCREENING_MANIFEST.read_bytes()).hexdigest(),
    )


def _approval(manifest, digest: str) -> dict[str, object]:
    return {
        "schema_version": 1,
        "manifest_sha256": digest,
        "approved": True,
        "max_spend_usd": 1000.0,
        "model_ids": sorted(model.provider_model for model in manifest.models),
        "endpoints": sorted(model.client["base_url"] for model in manifest.models),
        "credential_envs": sorted(
            model.client["api_key_env"] for model in manifest.models
        ),
        "executor_revision": "0" * 40,
    }
