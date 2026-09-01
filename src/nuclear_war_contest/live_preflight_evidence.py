"""Deterministic evidence helpers for live preflight requests."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from nuclear_war_agents import HTTPClientConfig
from nuclear_war_agents.llm_http_config import request_body
from nuclear_war_agents.llm_http_response import response_json

from .preflight_types import CandidateModel

PROMPT_PREFIX = (
    "Reply with exactly this JSON and nothing else: "
    '{"preflight":"ok"}. Candidate seed: '
)


def preflight_prompt(seed: int) -> str:
    return f"{PROMPT_PREFIX}{seed}"


def prompt_sha256(seed: int) -> str:
    return hashlib.sha256(preflight_prompt(seed).encode()).hexdigest()


def request_body_sha256(model: CandidateModel, seed: int) -> str:
    config = HTTPClientConfig(**model.client)
    body = request_body(preflight_prompt(seed), model.client["model"], config)
    return hashlib.sha256(body).hexdigest()


def response_sha256(raw_response: str) -> str:
    return hashlib.sha256(raw_response.encode()).hexdigest()


def expected_response(raw_response: str) -> bool:
    try:
        return json.loads(raw_response) == {"preflight": "ok"}
    except json.JSONDecodeError:
        return False


def response_model(body: str) -> str | None:
    try:
        value: Any = response_json(body).get("model")
    except Exception:
        return None
    return value if isinstance(value, str) and value else None


__all__ = [
    "expected_response",
    "preflight_prompt",
    "prompt_sha256",
    "request_body_sha256",
    "response_model",
    "response_sha256",
]
