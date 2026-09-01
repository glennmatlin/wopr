"""Bounded request execution and transport evidence for live preflight."""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass, field
from typing import Any

from nuclear_war_agents import HTTPClientConfig, LLMHttpClient
from nuclear_war_agents.llm_http_transport import HTTPTransport
from nuclear_war_env.local_env import load_local_dotenv

from .live_preflight_evidence import (
    expected_response,
    preflight_prompt,
    prompt_sha256,
    response_model,
    response_sha256,
)
from .preflight_types import CandidateModel


@dataclass
class CountingTransport:
    delegate: HTTPTransport
    limit: int
    count: int = 0
    request_hashes: list[str] = field(default_factory=list)
    response_models: list[str | None] = field(default_factory=list)

    def __call__(self, url: str, headers: dict[str, str], body: bytes, timeout: int):
        if self.count >= self.limit:
            raise RuntimeError("live preflight request budget exceeded")
        self.count += 1
        self.request_hashes.append(hashlib.sha256(body).hexdigest())
        try:
            response = self.delegate(url, headers, body, timeout)
        except Exception:
            self.response_models.append(None)
            raise
        self.response_models.append(response_model(response.body))
        return response


def run_attempt(
    model: CandidateModel,
    seed: int,
    transport: HTTPTransport,
    input_tokens_bound: int,
) -> tuple[dict[str, Any], bool]:
    config = HTTPClientConfig(**model.client)
    prompt = preflight_prompt(seed)
    prompt_hash = prompt_sha256(seed)
    if max(1, (len(prompt) + 3) // 4) > input_tokens_bound:
        return _failed(model, seed, prompt_hash, "input_token_bound"), False
    load_local_dotenv()
    key_present = bool(config.api_key_env and os.environ.get(config.api_key_env))
    try:
        completion = LLMHttpClient(config, transport=transport).complete(prompt)
    except Exception as exc:
        return _failed(model, seed, prompt_hash, type(exc).__name__), key_present
    if not expected_response(completion.raw_response):
        return (
            _failed_with_completion(
                model, seed, prompt_hash, completion, "unexpected_response"
            ),
            key_present,
        )
    usage = completion.provider_usage
    if usage is not None and not _valid_usage(usage):
        return (
            _failed_with_completion(
                model, seed, prompt_hash, completion, "invalid_usage"
            ),
            key_present,
        )
    return (
        {
            "model_id": model.model_id,
            "seed": seed,
            "status": "passed",
            "prompt_sha256": prompt_hash,
            "response_sha256": response_sha256(completion.raw_response),
            "response_contract": {"preflight": "ok"},
            "response_chars": len(completion.raw_response),
            "provider_model": completion.provider_model,
            "provider_latency_ms": completion.provider_latency_ms,
            "provider_transport_retries": completion.provider_transport_retries,
            "provider_usage": usage,
        },
        key_present,
    )


def _failed(
    model: CandidateModel, seed: int, prompt_hash: str, error_type: str
) -> dict[str, Any]:
    return {
        "model_id": model.model_id,
        "seed": seed,
        "status": "failed",
        "prompt_sha256": prompt_hash,
        "error_type": error_type,
    }


def _failed_with_completion(
    model: CandidateModel,
    seed: int,
    prompt_hash: str,
    completion: Any,
    error_type: str,
) -> dict[str, Any]:
    attempt = _failed(model, seed, prompt_hash, error_type)
    usage = completion.provider_usage
    attempt.update(
        response_sha256=response_sha256(completion.raw_response),
        response_contract=None,
        response_chars=len(completion.raw_response),
        provider_model=completion.provider_model,
        provider_latency_ms=completion.provider_latency_ms,
        provider_transport_retries=completion.provider_transport_retries,
        provider_usage=usage if usage is None or _valid_usage(usage) else None,
    )
    return attempt


def _valid_usage(usage: dict[str, int | float]) -> bool:
    return {"prompt_tokens", "completion_tokens"} <= set(usage) and all(
        isinstance(value, int | float) and not isinstance(value, bool) and value >= 0
        for value in usage.values()
    )


__all__ = ["CountingTransport", "run_attempt"]
