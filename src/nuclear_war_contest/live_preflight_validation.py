"""Validation for candidate-bound live preflight receipts."""

from __future__ import annotations

from typing import Any

from .live_preflight_attempts import validate_attempt
from .live_preflight_auth import validate_live_preflight_approval
from .live_preflight_budget import cost_bound, request_bound
from .preflight import candidate_manifest_hash
from .preflight_types import CandidateManifest


def validate_live_preflight_receipt(
    receipt: dict[str, Any], manifest: CandidateManifest
) -> None:
    expected_fields = {
        "schema_version",
        "status",
        "approval_status",
        "candidate_manifest_hash",
        "source_revision",
        "executor_revision",
        "authorization",
        "promotion_approval",
        "preflight_seeds",
        "study_seeds",
        "network_calls",
        "credentials_read",
        "request_bound",
        "cost_bound",
        "attempts",
    }
    if set(receipt) != expected_fields:
        raise ValueError("Live preflight receipt fields are invalid")
    if receipt.get("schema_version") != 1:
        raise ValueError("Live preflight receipt schema_version is invalid")
    if receipt.get("candidate_manifest_hash") != candidate_manifest_hash(manifest):
        raise ValueError("Live preflight receipt is not bound to the candidate")
    if receipt.get("source_revision") != manifest.source_revision:
        raise ValueError("Live preflight receipt source revision is invalid")
    if receipt.get("preflight_seeds") != list(manifest.preflight_seeds):
        raise ValueError("Live preflight receipt seeds do not match the candidate")
    if receipt.get("study_seeds") != list(manifest.study_seeds):
        raise ValueError(
            "Live preflight receipt study seeds do not match the candidate"
        )
    if set(manifest.preflight_seeds) & set(manifest.study_seeds):
        raise ValueError("Live preflight and study seeds must be disjoint")
    attempts = receipt.get("attempts")
    expected = len(manifest.models) * len(manifest.preflight_seeds)
    if not isinstance(attempts, list) or len(attempts) != expected:
        raise ValueError("Live preflight receipt attempt count is invalid")
    if receipt.get("status") not in {"passed", "failed"}:
        raise ValueError("Live preflight receipt status is invalid")
    approval_status = receipt.get("approval_status")
    if approval_status not in {"pending_owner", "approved"}:
        raise ValueError("Live preflight receipt approval status is invalid")
    executor_revision = receipt.get("executor_revision")
    if not isinstance(executor_revision, str):
        raise ValueError("Live preflight receipt executor revision is invalid")
    validate_live_preflight_approval(
        manifest, receipt.get("authorization"), executor_revision
    )
    promotion = receipt.get("promotion_approval")
    if approval_status == "pending_owner" and promotion is not None:
        raise ValueError("Pending live preflight receipt has promotion approval")
    if approval_status == "approved":
        if receipt.get("status") != "passed":
            raise ValueError("Approved live preflight receipt must pass")
        from .live_preflight_promotion import (
            validate_live_preflight_promotion_approval,
        )

        validate_live_preflight_promotion_approval(manifest, promotion, receipt)
    network_calls = receipt.get("network_calls")
    if not isinstance(network_calls, int) or network_calls < 0:
        raise ValueError("Live preflight network_calls is invalid")
    if type(receipt.get("credentials_read")) is not bool:
        raise ValueError("Live preflight credentials_read is invalid")
    if receipt["status"] == "passed" and receipt["credentials_read"] is not True:
        raise ValueError("Passed live preflight receipt lacks credentials")
    if receipt.get("request_bound") != request_bound(manifest):
        raise ValueError("Live preflight request bound does not match candidate")
    if receipt.get("cost_bound") != cost_bound(manifest):
        raise ValueError("Live preflight cost bound does not match candidate")
    if receipt["network_calls"] > receipt["request_bound"]["provider_attempts"]:
        raise ValueError("Live preflight network calls exceed request bound")
    models = {model.model_id: model for model in manifest.models}
    for attempt in attempts:
        validate_attempt(attempt, manifest, models)
    expected_keys = {
        (model.model_id, seed)
        for model in manifest.models
        for seed in manifest.preflight_seeds
    }
    actual_keys = {(item["model_id"], item["seed"]) for item in attempts}
    if actual_keys != expected_keys:
        raise ValueError("Live preflight attempt keys are invalid")
    expected_status = (
        "passed" if all(item["status"] == "passed" for item in attempts) else "failed"
    )
    if receipt["status"] != expected_status:
        raise ValueError("Live preflight receipt status does not match attempts")
    if network_calls != sum(item["provider_attempts"] for item in attempts):
        raise ValueError("Live preflight network_calls do not match attempts")


__all__ = ["validate_live_preflight_receipt"]
