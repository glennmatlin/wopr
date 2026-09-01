"""Validation for frozen command-authority parameters and role hashes."""

from __future__ import annotations

from typing import Any

from .prompt_identity import role_prompt_hashes

ROLE_IDS = {"executive", "strategic_advisor", "risk_advisor"}
CLIENT_FIELDS = {
    "provider",
    "base_url",
    "base_url_env",
    "model",
    "model_env",
    "api_key_env",
    "provider_label",
    "timeout_seconds",
    "temperature",
    "max_tokens",
    "reasoning_effort",
    "reasoning_enabled",
    "stream",
}


def validate_role_prompt_hashes(value: Any) -> dict[str, str]:
    expected = role_prompt_hashes()
    if not isinstance(value, dict) or set(value) != ROLE_IDS:
        raise ValueError("Study manifest role_prompt_hashes must name all member roles")
    if not all(
        isinstance(key, str) and isinstance(item, str) and item
        for key, item in value.items()
    ):
        raise ValueError(
            "Study manifest role_prompt_hashes must map strings to strings"
        )
    if value != expected:
        raise ValueError("Study manifest role_prompt_hashes do not match role prompts")
    return dict(value)


def validate_client(value: Any, provider: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("Study manifest client must be an object")
    if set(value) - CLIENT_FIELDS:
        raise ValueError("Study manifest client fields are invalid")
    if value and value.get("provider", provider) != provider:
        raise ValueError("Study manifest client provider does not match model provider")
    forbidden = {"api_key", "token", "secret", "authorization"}
    if any(key.lower() in forbidden for key in value):
        raise ValueError(
            "Study manifest client must use environment-backed credentials"
        )
    return dict(value)


def validate_authority_parameters(
    authority: str,
    parameters: dict[str, Any],
) -> None:
    if authority == "sole_authority":
        if set(parameters) != {"deference"} or not _bounded(parameters["deference"]):
            raise ValueError("Study manifest sole-authority parameters are invalid")
        return
    if set(parameters) != {"threshold", "weights"}:
        raise ValueError("Study manifest council parameters are invalid")
    if not _positive_bounded(parameters["threshold"]):
        raise ValueError("Study manifest council threshold is invalid")
    weights = parameters["weights"]
    if not isinstance(weights, dict) or set(weights) != ROLE_IDS:
        raise ValueError("Study manifest council weights are invalid")
    if not all(_positive_number(value) for value in weights.values()):
        raise ValueError("Study manifest council weights must be positive")


def _bounded(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and 0 <= value <= 1
    )


def _positive_bounded(value: Any) -> bool:
    return _bounded(value) and value > 0


def _positive_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0
