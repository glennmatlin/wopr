"""Small policy helpers for matched-study orchestration."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from typing import Any

from .manifest_types import StudyCell, StudyManifest
from .runner_receipts import attempt_id, read_attempt


def has_live_models(manifest: StudyManifest) -> bool:
    return any(
        model.provider != "offline"
        or model.backend in {"concordia_http", "concordia_native_http"}
        for model in manifest.models
    )


def prior_budget_metrics(record: dict[str, Any] | None) -> dict[str, Any] | None:
    if not isinstance(record, dict):
        return None
    admissibility = record.get("admissibility")
    if not isinstance(admissibility, dict):
        return None
    metrics = admissibility.get("channel_metrics")
    return metrics if isinstance(metrics, dict) else None


def validated_prior_budget_metrics(
    out_dir: Path,
    attempt: str,
    record: dict[str, Any] | None,
    manifest: StudyManifest,
    cell: StudyCell,
) -> dict[str, Any] | None:
    if isinstance(record, dict) and record.get("status") == "failed_retryable":
        record = read_attempt(out_dir, attempt, manifest, cell)
    return prior_budget_metrics(record)


def validate_latest_attempts(
    out_dir: Path,
    manifest: StudyManifest,
    latest: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    expected = {attempt_id(manifest, cell): cell for cell in manifest.cells}
    if set(latest) - set(expected):
        raise ValueError("Ledger contains an unknown attempt")
    for attempt, record in latest.items():
        status = record.get("status")
        if status == "started":
            raise ValueError(f"Unfinished attempt requires inspection: {attempt}")
        if status not in {"completed", "failed_terminal", "failed_retryable"}:
            raise ValueError(f"Ledger attempt status is invalid: {attempt}")
        receipt = read_attempt(out_dir, attempt, manifest, expected[attempt])
        _check_ledger_receipt(record, receipt, status)
    return latest


def preserve_retry_receipt(
    out_dir: Path, attempt: str, record: dict[str, Any] | None
) -> tuple[str | None, str | None]:
    if not isinstance(record, dict) or record.get("status") != "failed_retryable":
        return None, None
    root = out_dir / "attempts" / attempt
    source = root / "attempt.json"
    if not source.is_file():
        raise ValueError(f"Retryable attempt receipt is missing: {attempt}")
    index = len(list(root.glob("prior-attempt-*.json"))) + 1
    path = root / f"prior-attempt-{index}.json"
    content = source.read_bytes()
    path.write_bytes(content)
    return path.name, sha256(content).hexdigest()


def _check_ledger_receipt(
    ledger: dict[str, Any], receipt: dict[str, Any], status: str
) -> None:
    expected_status = "completed" if status == "completed" else "failed"
    if receipt.get("status") != expected_status:
        raise ValueError("Ledger status does not match attempt receipt")
    ledger_fields = {
        key: value
        for key, value in ledger.items()
        if key not in {"recorded_at", "status"}
    }
    receipt_fields = {
        key: value for key, value in receipt.items() if key != "status"
    }
    if ledger_fields != receipt_fields:
        raise ValueError("Ledger and attempt receipt differ")


__all__ = [
    "has_live_models",
    "prior_budget_metrics",
    "validated_prior_budget_metrics",
]
