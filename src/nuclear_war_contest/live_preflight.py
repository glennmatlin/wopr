"""Explicitly authorized, candidate-bound live model preflight."""

from __future__ import annotations

from typing import Any

from nuclear_war_agents.llm_http_transport import HTTPTransport, send_http

from .executor_identity import verify_executor_revision
from .live_preflight_auth import validate_live_preflight_approval
from .live_preflight_budget import cost_bound, request_bound
from .live_preflight_execution import CountingTransport, run_attempt
from .live_preflight_validation import (
    validate_live_preflight_receipt,
)
from .preflight import candidate_manifest_hash
from .preflight_types import CandidateManifest


def run_candidate_preflight(
    manifest: CandidateManifest,
    *,
    transport: HTTPTransport | None = None,
    allow_network: bool = False,
    authorization: dict[str, Any] | None = None,
    executor_revision: str | None = None,
) -> dict[str, Any]:
    """Run one bounded request per model and preflight seed."""
    if not allow_network:
        raise ValueError("Live preflight requires allow_network=True")
    if authorization is None or executor_revision is None:
        raise ValueError("Live preflight requires candidate-bound owner approval")
    validate_live_preflight_approval(manifest, authorization, executor_revision)
    verify_executor_revision(executor_revision)
    delegate = transport or send_http
    attempts: list[dict[str, Any]] = []
    network_calls = 0
    credentials_read = False
    for model in manifest.models:
        counter = CountingTransport(
            delegate,
            len(manifest.preflight_seeds) * (manifest.transport_retry_margin + 1),
        )
        for seed in manifest.preflight_seeds:
            before = counter.count
            attempt, read_key = run_attempt(
                model, seed, counter, manifest.input_tokens_bound
            )
            _attach_transport_evidence(attempt, counter, before, model)
            attempts.append(attempt)
            network_calls += attempt["provider_attempts"]
            credentials_read = credentials_read or read_key
    receipt = {
        "schema_version": 1,
        "status": "passed"
        if all(item["status"] == "passed" for item in attempts)
        else "failed",
        "approval_status": "pending_owner",
        "candidate_manifest_hash": candidate_manifest_hash(manifest),
        "source_revision": manifest.source_revision,
        "executor_revision": executor_revision,
        "authorization": authorization,
        "promotion_approval": None,
        "preflight_seeds": list(manifest.preflight_seeds),
        "study_seeds": list(manifest.study_seeds),
        "network_calls": network_calls,
        "credentials_read": credentials_read,
        "request_bound": request_bound(manifest),
        "cost_bound": cost_bound(manifest),
        "attempts": attempts,
    }
    validate_live_preflight_receipt(receipt, manifest)
    return receipt


def _attach_transport_evidence(
    attempt: dict[str, Any],
    counter: CountingTransport,
    before: int,
    model: Any,
) -> None:
    calls = counter.count - before
    attempt["provider_attempts"] = calls
    attempt.setdefault("provider_transport_retries", max(0, calls - 1))
    if calls:
        attempt["request_body_sha256"] = counter.request_hashes[-1]
        response_model = counter.response_models[-1]
        attempt["response_model"] = response_model
        if attempt["status"] == "passed" and response_model != model.client["model"]:
            attempt["status"] = "failed"
            attempt["error_type"] = "unexpected_provider_model"


__all__ = ["run_candidate_preflight", "validate_live_preflight_receipt"]
