"""Validation for individual live preflight attempts."""

from __future__ import annotations

from typing import Any

from .live_preflight_attempt_evidence import validate_failure, validate_success
from .live_preflight_evidence import prompt_sha256, request_body_sha256
from .preflight_types import CandidateManifest, CandidateModel


def validate_attempt(
    attempt: Any, manifest: CandidateManifest, models: dict[str, CandidateModel]
) -> None:
    if not isinstance(attempt, dict):
        raise ValueError("Live preflight attempt must be an object")
    model_id = attempt.get("model_id")
    seed = attempt.get("seed")
    if model_id not in models or seed not in manifest.preflight_seeds:
        raise ValueError("Live preflight attempt identity is invalid")
    if attempt.get("status") not in {"passed", "failed"}:
        raise ValueError("Live preflight attempt status is invalid")
    base_fields = {
        "model_id",
        "seed",
        "status",
        "prompt_sha256",
        "provider_attempts",
        "provider_transport_retries",
    }
    allowed = base_fields | {
        "request_body_sha256",
        "response_model",
        "error_type",
    }
    if attempt["status"] == "passed":
        allowed |= {
            "response_sha256",
            "response_contract",
            "response_chars",
            "provider_model",
            "provider_latency_ms",
            "provider_usage",
        }
    else:
        allowed |= {
            "response_sha256",
            "response_contract",
            "response_chars",
            "provider_model",
            "provider_latency_ms",
            "provider_usage",
        }
    if set(attempt) - allowed:
        raise ValueError("Live preflight attempt fields are invalid")
    if attempt.get("prompt_sha256") != prompt_sha256(seed):
        raise ValueError("Live preflight prompt hash is invalid")
    calls = attempt.get("provider_attempts")
    retries = attempt.get("provider_transport_retries")
    if (
        not isinstance(calls, int)
        or isinstance(calls, bool)
        or calls < 0
        or not isinstance(retries, int)
        or isinstance(retries, bool)
        or retries < 0
    ):
        raise ValueError("Live preflight provider attempt accounting is invalid")
    if calls != retries + 1 and calls > 0:
        raise ValueError("Live preflight retry accounting is invalid")
    if calls == 0 and retries != 0:
        raise ValueError("Live preflight zero-call retry accounting is invalid")
    if calls > manifest.transport_retry_margin + 1:
        raise ValueError("Live preflight per-attempt request cap is invalid")
    if attempt["status"] == "passed" and calls < 1:
        raise ValueError("Live preflight passed attempt has no provider request")
    if calls:
        if attempt.get("request_body_sha256") != request_body_sha256(
            models[model_id], seed
        ):
            raise ValueError("Live preflight request body hash is invalid")
    if attempt["status"] == "passed":
        validate_success(attempt, models[model_id])
    else:
        if not isinstance(attempt.get("error_type"), str) or not attempt["error_type"]:
            raise ValueError("Live preflight failed attempt error is invalid")
        validate_failure(attempt)


__all__ = ["validate_attempt"]
