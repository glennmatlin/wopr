"""Request-budget and sidecar-integrity integration gates."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nuclear_war_contest.manifest import load_study_manifest
from nuclear_war_contest.runner import run_matched_study


def _manifest_payload() -> dict[str, object]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


def test_default_runner_stops_before_the_first_over_budget_request(
    tmp_path: Path,
) -> None:
    payload = _manifest_payload()
    payload["request_budget"] = {
        "max_c2_calls_per_game": 1,
        "max_press_calls_per_game": 0,
    }
    manifest = load_study_manifest(payload)
    summary = run_matched_study(manifest, tmp_path)
    assert all(row["admissibility"]["tier"] == "C" for row in summary["attempts"])
    failure = next((tmp_path / "attempts").glob("*/failure-1.json"))
    failure_payload = json.loads(failure.read_text(encoding="utf-8"))
    assert failure_payload["reasons"] == ["channel_cap_exceeded"]
    assert failure_payload["channel_metrics"]["c2"]["call_count"] == 1


def test_resume_rejects_tampered_channel_metrics(tmp_path: Path) -> None:
    payload = _manifest_payload()
    payload["request_budget"] = {
        "max_c2_calls_per_game": 2048,
        "max_press_calls_per_game": 160,
    }
    manifest = load_study_manifest(payload)
    run_matched_study(manifest, tmp_path)
    receipt = next((tmp_path / "attempts").glob("*/attempt.json"))
    attempt = json.loads(receipt.read_text(encoding="utf-8"))
    summary_path = receipt.parent / attempt["artifacts"]["summary_path"]
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["channel_metrics"]["c2"]["call_count"] = 2049
    summary_path.write_text(json.dumps(summary), encoding="utf-8")
    with pytest.raises(ValueError, match="Stored channel metrics"):
        run_matched_study(manifest, tmp_path)


def test_resume_rejects_tampered_failure_metrics(tmp_path: Path) -> None:
    payload = _manifest_payload()
    payload["request_budget"] = {
        "max_c2_calls_per_game": 1,
        "max_press_calls_per_game": 0,
    }
    manifest = load_study_manifest(payload)
    run_matched_study(manifest, tmp_path)
    receipt = next((tmp_path / "attempts").glob("*/attempt.json"))
    attempt = json.loads(receipt.read_text(encoding="utf-8"))
    failure_path = receipt.parent / attempt["failure_artifact"]
    failure = json.loads(failure_path.read_text(encoding="utf-8"))
    failure["channel_metrics"]["c2"]["provider_attempt_count"] = 0
    attempt["admissibility"] = failure
    failure_path.write_text(json.dumps(failure), encoding="utf-8")
    receipt.write_text(json.dumps(attempt), encoding="utf-8")

    with pytest.raises(ValueError, match="Failure receipt c2 attempts"):
        run_matched_study(manifest, tmp_path)


def test_resume_rejects_ledger_cost_drift_before_execution(tmp_path: Path) -> None:
    payload = _manifest_payload()
    payload["request_budget"] = {
        "max_c2_calls_per_game": 2048,
        "max_press_calls_per_game": 160,
        "max_cost_usd": 100.0,
        "max_cost_per_request_usd": 0.01,
    }
    manifest = load_study_manifest(payload)
    run_matched_study(manifest, tmp_path)
    ledger = tmp_path / "run_ledger.jsonl"
    lines = ledger.read_text().splitlines()
    records = [json.loads(line) for line in lines]
    terminal = next(record for record in records if record["status"] == "completed")
    terminal["budget_metrics"]["study_reserved_cost_usd"] = 0.0
    ledger.write_text(
        "\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n"
    )

    with pytest.raises(ValueError, match="Ledger and attempt receipt differ"):
        run_matched_study(manifest, tmp_path)


@pytest.mark.parametrize("invalid_cost", [float("nan"), float("inf")])
def test_resume_rejects_nonfinite_terminal_cost(
    tmp_path: Path, invalid_cost: float
) -> None:
    payload = _manifest_payload()
    payload["request_budget"] = {
        "max_c2_calls_per_game": 2048,
        "max_press_calls_per_game": 160,
        "max_cost_usd": 100.0,
        "max_cost_per_request_usd": 0.01,
    }
    manifest = load_study_manifest(payload)
    run_matched_study(manifest, tmp_path)
    receipt = next((tmp_path / "attempts").glob("*/attempt.json"))
    attempt = json.loads(receipt.read_text(encoding="utf-8"))
    attempt["budget_metrics"]["actual_cost_usd"] = invalid_cost
    summary_path = receipt.parent / attempt["artifacts"]["summary_path"]
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["budget_metrics"]["actual_cost_usd"] = invalid_cost
    receipt.write_text(json.dumps(attempt), encoding="utf-8")
    summary_path.write_text(json.dumps(summary), encoding="utf-8")

    with pytest.raises(ValueError):
        run_matched_study(manifest, tmp_path)


def test_resume_rejects_ledger_budget_field_omission(tmp_path: Path) -> None:
    payload = _manifest_payload()
    payload["request_budget"] = {
        "max_c2_calls_per_game": 2048,
        "max_press_calls_per_game": 160,
    }
    manifest = load_study_manifest(payload)
    run_matched_study(manifest, tmp_path)
    ledger = tmp_path / "run_ledger.jsonl"
    records = [json.loads(line) for line in ledger.read_text().splitlines()]
    terminal = next(record for record in records if record["status"] == "completed")
    terminal.pop("budget_metrics", None)
    ledger.write_text(
        "\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n"
    )

    with pytest.raises(ValueError, match="Ledger and attempt receipt differ"):
        run_matched_study(manifest, tmp_path)
