"""Trace payloads for free-output Room seat calls."""

from __future__ import annotations

from typing import Any

from nuclear_war_agents import LLMCompletion
from nuclear_war_agents.llm_http_transport import provider_attempts_from_error
from nuclear_war_concordia.provider_metadata import provider_metadata

from .free_output_models import SeatProductCall


def attempt_payload(
    attempt: int,
    prompt: str | None,
    raw_response: str | None,
    product: dict[str, Any] | None,
    validation_error: str | None,
    log: dict[str, Any] | None,
    *,
    completion: LLMCompletion | None = None,
    provider_attempts: int | None = None,
    exception: dict[str, str] | None = None,
) -> dict[str, Any]:
    attempts = provider_attempts
    if attempts is None:
        attempts = 1 + (completion.provider_transport_retries if completion else 0)
    return {
        "attempt": attempt,
        "prompt": prompt,
        "raw_response": raw_response,
        "parsed_product": product,
        "validation_error": validation_error,
        "entity_log": log,
        "provider_attempts": attempts,
        "exception": exception,
    }


def transport_attempt_payload(
    attempt: int, prompt: str | None, error: Exception
) -> dict[str, Any]:
    return attempt_payload(
        attempt,
        prompt,
        None,
        None,
        None,
        None,
        provider_attempts=provider_attempts_from_error(error),
        exception={
            "type": type(error).__name__,
            "module": type(error).__module__,
            "message": str(error),
        },
    )


def trace_payload(
    seat_id: str,
    call: SeatProductCall,
    attempts: list[dict[str, Any]],
    completions: list[LLMCompletion],
    status: str,
    max_output_retries: int,
) -> dict[str, Any]:
    metadata = provider_metadata(completions)
    metadata["provider_attempts"] = sum(item["provider_attempts"] for item in attempts)
    metadata["provider_transport_retries"] = sum(
        max(0, item["provider_attempts"] - 1) for item in attempts
    )
    return {
        "schema_version": "situation-room-seat-product-trace.v0.1",
        "status": status,
        "seat_id": seat_id,
        "call": call.payload(),
        "controls": {"max_output_retries": max_output_retries},
        "attempts": list(attempts),
        "provider_metadata": metadata,
    }


__all__ = ["attempt_payload", "trace_payload", "transport_attempt_payload"]
