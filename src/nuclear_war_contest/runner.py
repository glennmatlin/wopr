"""Resumable matched-study runner with append-only attempt receipts."""

from __future__ import annotations

from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from .admissibility import validate_result_artifacts
from .analysis import build_paired_analysis
from .ledger import is_terminal, latest_attempts
from .manifest import manifest_hash
from .manifest_types import StudyCell, StudyManifest
from .receipt_io import write_json, write_manifest
from .runner_budget import enforce_channel_caps
from .runner_cell import run_cell_attempt
from .runner_cost import initial_cost_state
from .runner_execution import run_payload, validate_execution_budget
from .runner_helpers import has_live_models, validate_latest_attempts
from .runner_receipts import attempt_id, read_attempt

StudyRunner = Callable[[dict[str, Any]], dict[str, Any]]


def run_matched_study(
    manifest: StudyManifest,
    out_dir: Path,
    runner: StudyRunner | None = None,
    *,
    max_workers: int = 1,
) -> dict[str, Any]:
    if max_workers < 1:
        raise ValueError("max_workers must be positive")
    validate_execution_budget(manifest)
    if runner is not None and has_live_models(manifest):
        raise ValueError("Live study execution requires the shared guarded runner")
    out_dir.mkdir(parents=True, exist_ok=True)
    write_manifest(out_dir, manifest)
    ledger_path = out_dir / "run_ledger.jsonl"
    latest = validate_latest_attempts(out_dir, manifest, latest_attempts(ledger_path))
    cost_state = initial_cost_state(latest)
    rows_by_attempt: dict[str, dict[str, Any]] = {}
    pending: list[tuple[StudyCell, str, dict[str, Any] | None]] = []
    for cell in manifest.cells:
        attempt = attempt_id(manifest, cell)
        record = latest.get(attempt)
        if is_terminal(record):
            rows_by_attempt[attempt] = read_attempt(out_dir, attempt, manifest, cell)
            continue
        attempt_dir = out_dir / "attempts" / attempt
        if attempt_dir.exists() and (record or {}).get("status") != "failed_retryable":
            raise ValueError(f"Unfinished attempt requires inspection: {attempt}")
        pending.append((cell, attempt, record))

    def run_pending(
        task: tuple[StudyCell, str, dict[str, Any] | None],
    ) -> dict[str, Any]:
        cell, attempt, record = task
        return run_cell_attempt(
            manifest,
            cell,
            attempt,
            out_dir,
            ledger_path,
            record,
            cost_state,
            run_payload,
            runner,
            validate_result_artifacts,
            enforce_channel_caps,
        )

    if max_workers == 1:
        pending_rows = [run_pending(task) for task in pending]
    else:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            pending_rows = list(executor.map(run_pending, pending))
    for index, (_, attempt, _) in enumerate(pending):
        rows_by_attempt[attempt] = pending_rows[index]
    rows = [rows_by_attempt[attempt_id(manifest, cell)] for cell in manifest.cells]
    analysis = build_paired_analysis([row for row in rows if "measures" in row])
    write_json(out_dir / "analysis.json", analysis)
    summary = {
        "manifest_hash": manifest_hash(manifest),
        "attempts": rows,
        "analysis": analysis,
    }
    write_json(out_dir / "study_summary.json", summary)
    return summary


_run_payload = run_payload

__all__ = ["StudyRunner", "run_matched_study"]
