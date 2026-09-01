"""Validation for append-only retry receipt chains."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from typing import Any

from .failure_receipt_validation import validate_failure_receipt
from .manifest_types import StudyCell, StudyManifest
from .runner_receipts import attempt_row


def validate_prior_receipt(
    payload: dict[str, Any],
    root: Path,
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
) -> None:
    binding = _binding(payload)
    if binding is None:
        return
    path_value, hash_value, _ = binding
    path = _safe_child(root, path_value, "prior attempt receipt")
    if not path.is_file() or sha256(path.read_bytes()).hexdigest() != hash_value:
        raise ValueError("Prior attempt receipt binding is invalid")
    _validate_failure_chain(
        _read_json(path), root, set(), 0, payload, manifest, cell, attempt
    )


def _validate_failure_chain(
    payload: dict[str, Any],
    root: Path,
    seen: set[str],
    depth: int,
    child: dict[str, Any],
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
) -> None:
    if depth >= 32:
        raise ValueError("Prior attempt receipt chain is invalid")
    failure = payload.get("admissibility")
    if payload.get("status") != "failed" or not isinstance(failure, dict):
        raise ValueError("Prior attempt receipt failure is missing")
    _validate_exact_receipt(payload, failure, manifest, cell, attempt)
    binding = _binding(payload)
    if child.get("prior_budget_metrics") != failure.get("channel_metrics"):
        raise ValueError("Prior budget metrics are not bound to the receipt")
    validate_failure_receipt(failure)
    artifact = payload["failure_artifact"]
    artifact_path = _safe_child(root, artifact, "prior failure artifact")
    if not artifact_path.is_file() or _read_json(artifact_path) != failure:
        raise ValueError("Prior attempt failure artifact is invalid")
    if binding is None:
        return
    path_value, hash_value, _ = binding
    if path_value in seen:
        raise ValueError("Prior attempt receipt chain is cyclic")
    path = _safe_child(root, path_value, "prior attempt receipt")
    if not path.is_file() or sha256(path.read_bytes()).hexdigest() != hash_value:
        raise ValueError("Prior attempt receipt binding is invalid")
    seen.add(path_value)
    _validate_failure_chain(
        _read_json(path), root, seen, depth + 1, payload, manifest, cell, attempt
    )


def _validate_exact_receipt(
    payload: dict[str, Any],
    failure: dict[str, Any],
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
) -> None:
    expected = attempt_row(
        manifest,
        cell,
        attempt,
        None,
        failure,
        _dict_value(payload, "budget_metrics"),
        _dict_value(payload, "prior_budget_metrics"),
        _str_value(payload, "prior_attempt_receipt_path"),
        _str_value(payload, "prior_attempt_receipt_sha256"),
    )
    allowed = set(expected) | {"failure_artifact"}
    if set(payload) != allowed:
        raise ValueError("Prior attempt receipt fields are invalid")
    for field, value in expected.items():
        if payload.get(field) != value:
            raise ValueError(f"Prior attempt receipt identity mismatch: {field}")


def _binding(
    payload: dict[str, Any],
) -> tuple[str, str, dict[str, Any] | None] | None:
    values = tuple(payload.get(field) for field in _BINDING_FIELDS)
    if all(value is None for value in values):
        return None
    path_value, hash_value, metrics = values
    if not isinstance(path_value, str) or not isinstance(hash_value, str):
        raise ValueError("Prior attempt receipt binding is invalid")
    if metrics is not None and not isinstance(metrics, dict):
        raise ValueError("Prior attempt receipt binding is invalid")
    return path_value, hash_value, metrics


def _dict_value(payload: dict[str, Any], field: str) -> dict[str, Any] | None:
    value = payload.get(field)
    return value if isinstance(value, dict) else None


def _str_value(payload: dict[str, Any], field: str) -> str | None:
    value = payload.get(field)
    return value if isinstance(value, str) else None


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Artifact must be an object: {path}")
    return value


def _safe_child(root: Path, relative: str, label: str) -> Path:
    path = Path(relative)
    resolved_root = root.resolve()
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Attempt receipt {label} path is invalid")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(resolved_root):
        raise ValueError(f"Attempt receipt {label} path is invalid")
    return resolved


_BINDING_FIELDS = (
    "prior_attempt_receipt_path",
    "prior_attempt_receipt_sha256",
    "prior_budget_metrics",
)

__all__ = ["validate_prior_receipt"]
