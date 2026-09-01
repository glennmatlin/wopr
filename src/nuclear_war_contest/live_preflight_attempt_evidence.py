"""Validation of response evidence attached to preflight attempts."""

from __future__ import annotations

import string
from typing import Any

from .preflight_types import CandidateModel


def validate_success(attempt: dict[str, Any], model: CandidateModel) -> None:
    if attempt.get("response_contract") != {"preflight": "ok"}:
        raise ValueError("Live preflight response contract is invalid")
    response_chars = attempt.get("response_chars")
    if not isinstance(response_chars, int) or response_chars < 1:
        raise ValueError("Live preflight passed response is invalid")
    if not _hash(attempt.get("response_sha256")):
        raise ValueError("Live preflight response hash is invalid")
    if attempt.get("response_model") != model.client.get("model"):
        raise ValueError("Live preflight response model is invalid")
    if not isinstance(attempt.get("provider_model"), str):
        raise ValueError("Live preflight provider model is invalid")
    latency = attempt.get("provider_latency_ms")
    if not isinstance(latency, int) or latency < 0:
        raise ValueError("Live preflight provider latency is invalid")
    if not _usage(attempt.get("provider_usage"), require_tokens=True):
        raise ValueError("Live preflight usage is invalid")


def validate_failure(attempt: dict[str, Any]) -> None:
    evidence = {
        "response_sha256",
        "response_contract",
        "response_chars",
        "provider_model",
        "provider_latency_ms",
        "provider_usage",
    }
    if not evidence & set(attempt):
        return
    if not _hash(attempt.get("response_sha256")):
        raise ValueError("Live preflight failure response hash is invalid")
    chars = attempt.get("response_chars")
    if not isinstance(chars, int) or chars < 1:
        raise ValueError("Live preflight failure response is invalid")
    if not _usage(attempt.get("provider_usage"), require_tokens=False):
        raise ValueError("Live preflight failure usage is invalid")
    latency = attempt.get("provider_latency_ms")
    if latency is not None and (not isinstance(latency, int) or latency < 0):
        raise ValueError("Live preflight failure latency is invalid")


def _usage(value: Any, *, require_tokens: bool) -> bool:
    if value is None and not require_tokens:
        return True
    if not isinstance(value, dict):
        return False
    if require_tokens and not {"prompt_tokens", "completion_tokens"} <= set(value):
        return False
    return all(
        isinstance(item, int | float) and not isinstance(item, bool) and item >= 0
        for item in value.values()
    )


def _hash(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in string.hexdigits for character in value)
    )


__all__ = ["validate_failure", "validate_success"]
