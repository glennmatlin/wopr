"""Offline factorial study pipeline integration gate."""

from __future__ import annotations

import json
import threading
from pathlib import Path

import pytest

from nuclear_war_contest.manifest import load_study_manifest
from nuclear_war_contest.runner import _run_payload, run_matched_study


def test_offline_run_supports_bounded_workers_and_preserves_cell_order(
    tmp_path: Path,
) -> None:
    manifest_path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    manifest = load_study_manifest(
        json.loads(manifest_path.read_text(encoding="utf-8"))
    )
    pair_started = threading.Barrier(2)

    def concurrent_runner(payload: dict[str, object]) -> dict[str, object]:
        pair_started.wait(timeout=5)
        return _run_payload(payload)

    summary = run_matched_study(
        manifest,
        tmp_path,
        runner=concurrent_runner,
        max_workers=2,
    )

    assert all(row["status"] == "completed" for row in summary["attempts"])
    assert [row["cell_id"] for row in summary["attempts"]] == [
        cell.cell_id for cell in manifest.cells
    ]
    records = [
        json.loads(line)
        for line in (tmp_path / "run_ledger.jsonl").read_text().splitlines()
    ]
    assert len(records) == 16
    assert [record["status"] for record in records].count("started") == 8
    assert [record["status"] for record in records].count("completed") == 8


def test_offline_factorial_run_resumes_without_overwriting_attempts(
    tmp_path: Path,
) -> None:
    manifest_path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    manifest = load_study_manifest(
        json.loads(manifest_path.read_text(encoding="utf-8"))
    )

    first = run_matched_study(manifest, tmp_path)
    ledger = tmp_path / "run_ledger.jsonl"
    first_lines = ledger.read_text(encoding="utf-8").splitlines()
    second = run_matched_study(manifest, tmp_path)

    assert len(first["attempts"]) == 8
    assert all(row["status"] == "completed" for row in first["attempts"])
    assert all(
        row["manifest_hash"] == first["manifest_hash"] for row in first["attempts"]
    )
    assert all(row["backend"] == "concordia_first_legal" for row in first["attempts"])
    assert all(row["admissibility"]["tier"] == "A" for row in first["attempts"])
    assert all("measures" in row for row in first["attempts"])
    assert all(row["measures"]["population_loss"] >= 0 for row in first["attempts"])
    assert all(row["condition_hash"] for row in first["attempts"])
    assert all(row["model_manifest_hash"] for row in first["attempts"])
    assert all(row["role_prompt_hashes"] for row in first["attempts"])
    assert all(row["artifacts"] for row in first["attempts"])
    assert any(
        row["measures"]["communication"]["message_count"] > 0
        for row in first["attempts"]
        if row["communication"] == "full_press"
    )
    assert all(
        row["measures"]["communication"]["message_count"] == 0
        for row in first["attempts"]
        if row["communication"] == "no_press"
    )
    assert len(first["analysis"]["primary"]["pairs"]) == 4
    assert len(first["analysis"]["exploratory"]["pairs"]) == 10
    assert len(second["attempts"]) == 8
    assert ledger.read_text(encoding="utf-8").splitlines() == first_lines
    assert (tmp_path / "analysis.json").is_file()
    assert (tmp_path / "study_summary.json").is_file()


def test_resume_rejects_tampered_terminal_receipt(tmp_path: Path) -> None:
    manifest_path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    manifest = load_study_manifest(
        json.loads(manifest_path.read_text(encoding="utf-8"))
    )
    run_matched_study(manifest, tmp_path)
    receipt = next((tmp_path / "attempts").glob("*/attempt.json"))
    payload = json.loads(receipt.read_text(encoding="utf-8"))
    payload["seed"] = 999
    receipt.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="identity mismatch"):
        run_matched_study(manifest, tmp_path)


def test_resume_rejects_extra_terminal_receipt_fields(tmp_path: Path) -> None:
    manifest_path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    manifest = load_study_manifest(
        json.loads(manifest_path.read_text(encoding="utf-8"))
    )
    run_matched_study(manifest, tmp_path)
    receipt = next((tmp_path / "attempts").glob("*/attempt.json"))
    payload = json.loads(receipt.read_text(encoding="utf-8"))
    payload["unbound_evidence"] = True
    receipt.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="receipt fields"):
        run_matched_study(manifest, tmp_path)


def test_resume_rejects_artifact_path_escape(tmp_path: Path) -> None:
    manifest_path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    manifest = load_study_manifest(
        json.loads(manifest_path.read_text(encoding="utf-8"))
    )
    run_matched_study(manifest, tmp_path)
    receipt = next((tmp_path / "attempts").glob("*/attempt.json"))
    payload = json.loads(receipt.read_text(encoding="utf-8"))
    payload["artifacts"]["replay_path"] = "../STUDY_MANIFEST.json"
    receipt.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="path is invalid"):
        run_matched_study(manifest, tmp_path)


def test_runner_classifies_over_cap_attempts_before_artifact_write(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    manifest_path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    payload["request_budget"] = {
        "max_c2_calls_per_game": 1,
        "max_press_calls_per_game": 0,
    }
    manifest = load_study_manifest(payload)
    monkeypatch.setattr(
        "nuclear_war_contest.runner.validate_result_artifacts", lambda result: None
    )

    def over_cap_result(_: dict[str, object]) -> dict[str, object]:
        return {
            "summary": {
                "channel_metrics": {
                    "c2": {"call_count": 2},
                    "press": {"call_count": 0},
                }
            }
        }

    summary = run_matched_study(manifest, tmp_path, runner=over_cap_result)

    assert all(row["admissibility"]["tier"] == "C" for row in summary["attempts"])
    assert all(
        row["admissibility"]["reasons"] == ["channel_cap_exceeded"]
        for row in summary["attempts"]
    )
    assert all(
        row["admissibility"]["channel_metrics"]["c2"]["call_count"] == 2
        for row in summary["attempts"]
    )
    assert not list((tmp_path / "attempts").glob("*/wopr/replay.json"))
