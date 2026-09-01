"""Validate that a billable study is bound to an approved preflight packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .executor_identity import verify_executor_revision
from .manifest_types import StudyManifest
from .preflight import (
    build_preflight_receipt,
    candidate_manifest_hash,
    load_candidate_manifest,
)
from .preflight_study_binding import validate_study_binding

__all__ = ["validate_live_preflight"]


def validate_live_preflight(manifest: StudyManifest) -> None:
    receipt_path, candidate_path = _authorization_paths(manifest)
    receipt_bytes = receipt_path.read_bytes()
    if hashlib.sha256(receipt_bytes).hexdigest() != manifest.preflight_receipt_hash:
        raise ValueError("Preflight receipt hash does not match the receipt file")
    receipt = _object(receipt_bytes, "Preflight receipt")
    candidate = load_candidate_manifest(
        _object(candidate_path.read_bytes(), "Candidate manifest"),
        base_dir=candidate_path.parent,
    )
    _validate_receipt(receipt, candidate, manifest)
    verify_executor_revision(manifest.preflight_executor_revision or "")
    validate_study_binding(manifest, candidate)


def _authorization_paths(manifest: StudyManifest) -> tuple[Path, Path]:
    required = {
        "preflight_receipt_hash": manifest.preflight_receipt_hash,
        "preflight_receipt_path": manifest.preflight_receipt_path,
        "preflight_candidate_manifest_path": manifest.preflight_candidate_manifest_path,
        "preflight_candidate_manifest_hash": manifest.preflight_candidate_manifest_hash,
    }
    if any(value is None for value in required.values()):
        raise ValueError("Live study models require a receipt-backed preflight packet")
    receipt_path = Path(manifest.preflight_receipt_path or "")
    candidate_path = Path(manifest.preflight_candidate_manifest_path or "")
    if not receipt_path.is_file() or not candidate_path.is_file():
        raise ValueError("Preflight packet files must exist before a live study")
    return receipt_path, candidate_path


def _object(content: bytes, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} must be valid JSON") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{label} must be an object")
    return payload


def _validate_receipt(
    receipt: dict[str, Any], candidate: Any, manifest: StudyManifest
) -> None:
    if (
        receipt.get("status") != "approved"
        or receipt.get("approval_status") != "approved"
        or manifest.preflight_approval_status != "approved"
        or receipt.get("credentials_read") is not True
    ):
        raise ValueError("Live study models require an approved preflight receipt")
    if (
        receipt.get("candidate_manifest_hash")
        != manifest.preflight_candidate_manifest_hash
    ):
        raise ValueError("Preflight receipt is not bound to the candidate manifest")
    if candidate_manifest_hash(candidate) != manifest.preflight_candidate_manifest_hash:
        raise ValueError("Candidate manifest hash does not match the study manifest")
    expected = build_preflight_receipt(candidate)
    expected["status"] = "approved"
    expected["approval_status"] = "approved"
    expected["credentials_read"] = True
    extras = set(receipt) - set(expected) - {"live_preflight"}
    if extras or any(receipt.get(key) != value for key, value in expected.items()):
        raise ValueError("Preflight receipt does not match the candidate manifest")
    live_receipt = receipt.get("live_preflight")
    if live_receipt is None:
        raise ValueError("Approved live study requires a promoted live preflight")
    from .live_preflight_validation import validate_live_preflight_receipt

    validate_live_preflight_receipt(live_receipt, candidate)
    if live_receipt.get("approval_status") != "approved":
        raise ValueError("Promoted live preflight receipt is not owner approved")
    if manifest.preflight_executor_revision != live_receipt.get("executor_revision"):
        raise ValueError("Study executor revision is not bound to the live receipt")
