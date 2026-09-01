"""Retry and failure-receipt integration gates."""

from __future__ import annotations

import json
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import pytest

from nuclear_war_contest import runner as runner_module
from nuclear_war_contest.manifest import load_study_manifest
from nuclear_war_contest.manifest_types import StudyManifest, StudyRequestBudget
from nuclear_war_contest.runner import _run_payload, run_matched_study


def _manifest() -> StudyManifest:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    return load_study_manifest(json.loads(path.read_text(encoding="utf-8")))


def test_retryable_attempt_reuses_directory_and_completes_on_resume(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    calls = 0

    def flaky_runner(payload: dict[str, object]) -> dict[str, object]:
        nonlocal calls
        calls += 1
        if calls == 1:
            raise TimeoutError("offline retry test")
        return _run_payload(payload)

    first = run_matched_study(manifest, tmp_path, runner=flaky_runner)
    assert first["attempts"][0]["admissibility"]["retryable"] is True
    second = run_matched_study(manifest, tmp_path, runner=flaky_runner)

    assert all(row["status"] == "completed" for row in second["attempts"])
    retry_receipt = next(
        path for path in (tmp_path / "attempts").glob("*/attempt.json")
        if json.loads(path.read_text())["prior_attempt_receipt_path"] is not None
    )
    retry_payload = json.loads(retry_receipt.read_text())
    prior_path = retry_receipt.parent / retry_payload["prior_attempt_receipt_path"]
    assert prior_path.is_file()
    assert retry_payload["prior_attempt_receipt_sha256"]
    statuses = [
        json.loads(line)["status"]
        for line in (tmp_path / "run_ledger.jsonl").read_text().splitlines()
    ]
    assert "failed_retryable" in statuses
    run_matched_study(manifest, tmp_path, runner=flaky_runner)
    prior_path.unlink()
    with pytest.raises(ValueError, match="Prior attempt receipt binding"):
        run_matched_study(manifest, tmp_path, runner=flaky_runner)


def test_terminal_failure_artifact_is_checked_on_resume(tmp_path: Path) -> None:
    manifest = _manifest()

    def terminal_failure(_: dict[str, object]) -> dict[str, object]:
        raise ValueError("terminal")

    run_matched_study(manifest, tmp_path, runner=terminal_failure)
    receipt = next((tmp_path / "attempts").glob("*/attempt.json"))
    payload = json.loads(receipt.read_text(encoding="utf-8"))
    failure = receipt.parent / payload["failure_artifact"]
    content = json.loads(failure.read_text(encoding="utf-8"))
    content["tier"] = "A"
    failure.write_text(json.dumps(content), encoding="utf-8")

    with pytest.raises(ValueError, match="failure artifact"):
        run_matched_study(manifest, tmp_path)


def test_resume_rejects_tampered_prior_ancestor_identity(tmp_path: Path) -> None:
    manifest = _manifest()
    calls = 0

    def flaky_runner(payload: dict[str, object]) -> dict[str, object]:
        nonlocal calls
        calls += 1
        if calls == 1:
            raise TimeoutError("offline retry test")
        return _run_payload(payload)

    run_matched_study(manifest, tmp_path, runner=flaky_runner)
    run_matched_study(manifest, tmp_path, runner=flaky_runner)
    receipt = next(
        path
        for path in (tmp_path / "attempts").glob("*/attempt.json")
        if json.loads(path.read_text())["prior_attempt_receipt_path"]
    )
    payload = json.loads(receipt.read_text())
    prior_path = receipt.parent / payload["prior_attempt_receipt_path"]
    prior = json.loads(prior_path.read_text())
    prior["model_id"] = "tampered"
    prior_path.write_text(json.dumps(prior))
    payload["prior_attempt_receipt_sha256"] = sha256(
        prior_path.read_bytes()
    ).hexdigest()
    receipt.write_text(json.dumps(payload))

    with pytest.raises(ValueError, match="Prior attempt receipt identity mismatch"):
        run_matched_study(manifest, tmp_path, runner=flaky_runner)


def test_retry_resume_validates_prior_metrics_and_checks_cumulative_delta(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = _manifest()
    manifest = replace(
        source,
        models=(source.models[0],),
        conditions=(source.conditions[0],),
        seeds=(source.seeds[0],),
        request_budget=StudyRequestBudget(2048, 160),
    )
    payload_runner = runner_module.run_payload
    calls = 0

    def flaky_payload(
        payload: dict[str, object],
        budget: StudyRequestBudget | None = None,
        prior_metrics: dict[str, object] | None = None,
        cost_state: dict[str, float] | None = None,
    ) -> dict[str, object]:
        nonlocal calls
        calls += 1
        result = payload_runner(payload, budget, prior_metrics, cost_state)
        if calls == 1:
            error = TimeoutError("retry after provider use")
            error.partial_metrics = result["summary"]["budget_metrics"]  # type: ignore[attr-defined]
            raise error
        return result

    monkeypatch.setattr(runner_module, "run_payload", flaky_payload)
    first = run_matched_study(manifest, tmp_path)
    assert first["attempts"][0]["admissibility"]["retryable"] is True
    second = run_matched_study(manifest, tmp_path)

    assert second["attempts"][0]["status"] == "completed"
    assert second["attempts"][0]["prior_budget_metrics"]["c2"]["call_count"] > 0
