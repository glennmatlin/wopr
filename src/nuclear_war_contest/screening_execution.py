"""Approval-gated, resumable execution for the three-model screen."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .admissibility import validate_result_artifacts
from .executor_identity import verify_executor_revision
from .ledger import is_terminal, latest_attempts
from .manifest import manifest_hash
from .receipt_io import write_json
from .runner_budget import enforce_channel_caps
from .runner_cell import run_cell_attempt
from .runner_cost import initial_cost_state
from .runner_execution import run_payload
from .runner_helpers import validate_latest_attempts
from .runner_receipts import attempt_id, read_attempt
from .screening_execution_support import (
    build_screening_study_manifest,
    screening_approval_hash,
    validate_screening_approval,
)
from .screening_selection import build_screening_selection
from .screening_types import ScreeningManifest


def run_screening(
    manifest: ScreeningManifest,
    manifest_sha256: str,
    approval: dict[str, Any],
    executor_revision: str,
    *,
    allow_network: bool,
    out_dir: Path,
) -> dict[str, Any]:
    spend = validate_screening_approval(
        manifest, manifest_sha256, approval, executor_revision
    )
    if not allow_network:
        raise ValueError("Screening requires --allow-network")
    verify_executor_revision(executor_revision)
    approval_digest = screening_approval_hash(approval)
    study = build_screening_study_manifest(
        manifest,
        spend,
        execution_manifest_hash=manifest_sha256,
        approval_hash=approval_digest,
        executor_revision=executor_revision,
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_execution_manifest(
        out_dir, study, manifest_sha256, approval_digest, executor_revision
    )
    ledger_path = out_dir / "run_ledger.jsonl"
    latest = validate_latest_attempts(
        out_dir, study, latest_attempts(ledger_path)
    )
    cost_state = initial_cost_state(latest)
    rows: list[dict[str, Any]] = []
    for cell in study.cells:
        attempt = attempt_id(study, cell)
        record = latest.get(attempt)
        if is_terminal(record):
            rows.append(read_attempt(out_dir, attempt, study, cell))
            continue
        rows.append(
            run_cell_attempt(
                study,
                cell,
                attempt,
                out_dir,
                ledger_path,
                record,
                cost_state,
                _screening_payload,
                None,
                validate_result_artifacts,
                enforce_channel_caps,
            )
        )
    summary = {
        "schema_version": 1,
        "manifest_sha256": manifest_sha256,
        "approval_sha256": approval_digest,
        "executor_revision": executor_revision,
        "study_manifest_hash": manifest_hash(study),
        "approval_status": "approved",
        "screening_status": (
            "completed"
            if all(row.get("status") == "completed" for row in rows)
            else "completed_with_failures"
        ),
        "attempts": rows,
        "selection": build_screening_selection(manifest, rows),
    }
    write_json(out_dir / "screening_summary.json", summary)
    return summary


def _screening_payload(
    payload: dict[str, Any],
    budget: Any,
    prior_metrics: dict[str, Any] | None = None,
    cost_state: dict[str, float] | None = None,
) -> dict[str, Any]:
    return run_payload(
        payload,
        budget,
        prior_metrics=prior_metrics,
        cost_state=cost_state,
    )


def _write_execution_manifest(
    out_dir: Path,
    study: Any,
    manifest_sha256: str,
    approval_hash: str,
    executor_revision: str,
) -> None:
    payload = {
        "schema_version": 1,
        "screening_manifest_sha256": manifest_sha256,
        "approval_sha256": approval_hash,
        "executor_revision": executor_revision,
        "study_manifest_hash": manifest_hash(study),
        "study_id": study.study_id,
        "source_revision": study.source_revision,
        "seeds": list(study.seeds),
        "models": [model.model_id for model in study.models],
        "condition": "screening_press_light",
    }
    path = out_dir / "SCREENING_EXECUTION_MANIFEST.json"
    if path.exists() and path.read_text(encoding="utf-8") != _json(payload):
        raise ValueError("Screening execution manifest already differs")
    if not path.exists():
        path.write_text(_json(payload), encoding="utf-8")

def _json(payload: dict[str, Any]) -> str:
    import json

    return json.dumps(payload, indent=2, sort_keys=True)


__all__ = ["run_screening"]
