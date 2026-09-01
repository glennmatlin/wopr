"""Execute one resumable contest cell and write its receipt."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

from nuclear_war_concordia.artifacts import write_concordia_no_press_artifacts

from .admissibility import classify_failure, classify_result
from .config_builder import build_concordia_payload
from .ledger import append_ledger_record
from .manifest_types import StudyCell, StudyManifest
from .measures import derive_measures
from .receipt_io import artifact_paths, write_json
from .runner_budget import validate_budget_metrics
from .runner_helpers import (
    preserve_retry_receipt,
    validated_prior_budget_metrics,
)
from .runner_receipts import attempt_row, ledger_start

PayloadRunner = Callable[[dict[str, Any]], dict[str, Any]]
PayloadExecutor = Callable[..., dict[str, Any]]
ResultValidator = Callable[[dict[str, Any]], None]
CapEnforcer = Callable[..., None]


def run_cell_attempt(
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
    out_dir: Path,
    ledger_path: Path,
    latest_record: dict[str, Any] | None,
    cost_state: dict[str, float],
    execute_payload: PayloadExecutor,
    runner: PayloadRunner | None,
    validate_result: ResultValidator,
    enforce_caps: CapEnforcer,
) -> dict[str, Any]:
    attempt_dir = out_dir / "attempts" / attempt
    attempt_dir.mkdir(parents=True, exist_ok=True)
    prior_metrics = validated_prior_budget_metrics(
        out_dir, attempt, latest_record, manifest, cell
    )
    prior_path, prior_hash = preserve_retry_receipt(
        out_dir, attempt, latest_record
    )
    append_ledger_record(ledger_path, ledger_start(manifest, cell, attempt))
    try:
        payload = build_concordia_payload(manifest, cell)
        result = (
            runner(payload)
            if runner is not None
            else execute_payload(
                payload,
                manifest.request_budget,
                prior_metrics=prior_metrics,
                cost_state=cost_state,
            )
        )
        validate_result(result)
        _validate_budget(result, manifest, prior_metrics, enforce_caps)
        paths = write_concordia_no_press_artifacts(attempt_dir, result)
        row = attempt_row(
            manifest,
            cell,
            attempt,
            derive_measures(result),
            classify_result(result),
            budget_metrics=_budget_metrics(result),
            prior_budget_metrics=prior_metrics,
            prior_attempt_receipt_path=prior_path,
            prior_attempt_receipt_sha256=prior_hash,
        )
        row["artifacts"] = artifact_paths(paths, attempt_dir)
        write_json(attempt_dir / "attempt.json", row)
        _finish(ledger_path, manifest, cell, attempt, row, "completed")
        return row
    except Exception as exc:
        admissibility = classify_failure(exc)
        row = attempt_row(
            manifest,
            cell,
            attempt,
            None,
            admissibility,
            prior_budget_metrics=prior_metrics,
            prior_attempt_receipt_path=prior_path,
            prior_attempt_receipt_sha256=prior_hash,
        )
        failure_path = attempt_dir / f"failure-{_failure_number(attempt_dir)}.json"
        write_json(failure_path, admissibility)
        row["failure_artifact"] = str(failure_path.relative_to(attempt_dir))
        write_json(attempt_dir / "attempt.json", row)
        status = (
            "failed_retryable" if admissibility.get("retryable") else "failed_terminal"
        )
        _finish(ledger_path, manifest, cell, attempt, row, status)
        return row


def _validate_budget(
    result: dict[str, Any],
    manifest: StudyManifest,
    prior: dict[str, Any] | None,
    enforce_caps: CapEnforcer,
) -> None:
    if manifest.request_budget is None:
        return
    if "budget_metrics" in result.get("summary", {}):
        validate_budget_metrics(result, initial_metrics=prior)
    enforce_caps(result, manifest.request_budget, initial_metrics=prior)


def _budget_metrics(result: dict[str, Any]) -> dict[str, Any] | None:
    value = result.get("summary", {}).get("budget_metrics")
    return value if isinstance(value, dict) else None


def _failure_number(attempt_dir: Path) -> int:
    return len(list(attempt_dir.glob("failure-*.json"))) + 1


def _finish(
    ledger_path: Path,
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
    row: dict[str, Any],
    status: str,
) -> None:
    append_ledger_record(
        ledger_path,
        {**row, "status": status},
    )


__all__ = ["PayloadExecutor", "PayloadRunner", "run_cell_attempt"]
