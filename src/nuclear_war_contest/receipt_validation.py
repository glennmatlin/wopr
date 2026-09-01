"""Validation for terminal contest attempt receipts before reuse."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .failure_receipt_validation import validate_failure_receipt
from .manifest_types import StudyCell, StudyManifest
from .receipt_artifacts import (
    ARTIFACT_KEYS,
    read_json,
    safe_child,
    validate_artifact_contents,
    validate_prior_receipt,
)
from .runner_receipts import attempt_row


def validate_attempt_receipt(
    payload: dict[str, Any],
    out_dir: Path,
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
) -> None:
    admissibility = payload.get("admissibility")
    if not isinstance(admissibility, dict):
        raise ValueError("Attempt receipt admissibility is missing")
    expected = attempt_row(
        manifest,
        cell,
        attempt,
        payload.get("measures") if isinstance(payload.get("measures"), dict) else None,
        admissibility,
        _dict_value(payload, "budget_metrics"),
        _dict_value(payload, "prior_budget_metrics"),
        _str_value(payload, "prior_attempt_receipt_path"),
        _str_value(payload, "prior_attempt_receipt_sha256"),
    )
    expected_status = expected["status"]
    allowed_fields = set(expected)
    allowed_fields.add(
        "failure_artifact" if expected_status == "failed" else "artifacts"
    )
    if set(payload) != allowed_fields:
        raise ValueError("Attempt receipt fields are invalid")
    for field in expected:
        if payload.get(field) != expected[field]:
            raise ValueError(f"Attempt receipt identity mismatch: {field}")
    root = out_dir / "attempts" / attempt
    if expected_status == "failed":
        _validate_failure(payload, root, admissibility, manifest, cell, attempt)
        return
    artifacts = payload.get("artifacts")
    if not isinstance(artifacts, dict) or not artifacts:
        raise ValueError("Attempt receipt artifacts are missing")
    if not ARTIFACT_KEYS <= set(artifacts) or set(artifacts) - (
        ARTIFACT_KEYS | {"press_path"}
    ):
        raise ValueError("Attempt receipt artifact keys are invalid")
    for relative in artifacts.values():
        if (
            not isinstance(relative, str)
            or not safe_child(root, relative, "artifact").is_file()
        ):
            raise ValueError("Attempt receipt artifact is missing")
    validate_prior_receipt(payload, root, manifest, cell, attempt)
    validate_artifact_contents(payload, root, manifest)


def _validate_failure(
    payload: dict[str, Any],
    root: Path,
    admissibility: dict[str, Any],
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
) -> None:
    failure_artifact = payload.get("failure_artifact")
    if not isinstance(failure_artifact, str):
        raise ValueError("Attempt receipt failure artifact is missing")
    failure_path = safe_child(root, failure_artifact, "failure artifact")
    if not failure_path.is_file():
        raise ValueError("Attempt receipt failure artifact is missing")
    failure = read_json(failure_path)
    if failure != admissibility:
        raise ValueError("Attempt receipt failure artifact does not match")
    validate_failure_receipt(failure)
    validate_prior_receipt(payload, root, manifest, cell, attempt)


def _dict_value(payload: dict[str, Any], field: str) -> dict[str, Any] | None:
    value = payload.get(field)
    return value if isinstance(value, dict) else None


def _str_value(payload: dict[str, Any], field: str) -> str | None:
    value = payload.get(field)
    return value if isinstance(value, str) else None


__all__ = ["validate_attempt_receipt"]
