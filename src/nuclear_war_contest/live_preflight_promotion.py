"""Owner promotion of a completed live preflight receipt."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from typing import Any

from .live_preflight_auth import validate_live_preflight_approval
from .preflight_receipt import build_preflight_receipt
from .preflight_types import CandidateManifest


def live_preflight_receipt_hash(receipt: dict[str, Any]) -> str:
    pending = deepcopy(receipt)
    if pending.get("approval_status") == "approved":
        pending["approval_status"] = "pending_owner"
        pending["promotion_approval"] = None
    encoded = json.dumps(pending, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode()).hexdigest()


def build_live_preflight_promotion_approval(
    approval: dict[str, Any], receipt: dict[str, Any]
) -> dict[str, Any]:
    promoted = deepcopy(approval)
    promoted["live_receipt_sha256"] = live_preflight_receipt_hash(receipt)
    return promoted


def validate_live_preflight_promotion_approval(
    manifest: CandidateManifest,
    approval: Any,
    receipt: dict[str, Any],
) -> None:
    if not isinstance(approval, dict):
        raise ValueError("Live preflight promotion approval must be an object")
    expected = {
        "schema_version",
        "candidate_manifest_hash",
        "approved",
        "max_spend_usd",
        "model_ids",
        "endpoints",
        "credential_envs",
        "executor_revision",
        "live_receipt_sha256",
    }
    if set(approval) != expected:
        raise ValueError("Live preflight promotion approval fields are invalid")
    executor_revision = approval.get("executor_revision")
    if not isinstance(executor_revision, str):
        raise ValueError("Live preflight promotion executor revision is invalid")
    base = {
        key: value for key, value in approval.items() if key != "live_receipt_sha256"
    }
    validate_live_preflight_approval(manifest, base, executor_revision)
    if approval["live_receipt_sha256"] != live_preflight_receipt_hash(receipt):
        raise ValueError("Live preflight promotion is not bound to the receipt")


def promote_live_preflight_receipt(
    manifest: CandidateManifest,
    receipt: dict[str, Any],
    approval: dict[str, Any],
) -> dict[str, Any]:
    """Bind a separately reviewed, receipt-hash-bound result into the study."""
    from .live_preflight_validation import validate_live_preflight_receipt

    validate_live_preflight_receipt(receipt, manifest)
    if receipt.get("status") != "passed":
        raise ValueError("Only a passed live preflight can be promoted")
    validate_live_preflight_promotion_approval(manifest, approval, receipt)
    promoted_live = deepcopy(receipt)
    promoted_live["approval_status"] = "approved"
    promoted_live["promotion_approval"] = approval
    promoted = build_preflight_receipt(manifest)
    promoted.update(
        status="approved",
        approval_status="approved",
        credentials_read=True,
        live_preflight=promoted_live,
    )
    return promoted


__all__ = [
    "build_live_preflight_promotion_approval",
    "live_preflight_receipt_hash",
    "promote_live_preflight_receipt",
    "validate_live_preflight_promotion_approval",
]
