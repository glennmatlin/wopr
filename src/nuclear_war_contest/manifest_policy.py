"""Validation helpers for optional study execution policy fields."""

from __future__ import annotations

import math
import string
from typing import Any

from nuclear_war_env.integer_validation import is_strict_int

from .manifest_types import StudyRequestBudget


def load_request_budget(value: Any) -> StudyRequestBudget:
    required = {
        "max_c2_calls_per_game",
        "max_press_calls_per_game",
    }
    optional = {
        "input_tokens_bound",
        "max_output_tokens",
        "max_cost_usd",
        "max_cost_per_request_usd",
        "transport_retry_margin",
    }
    if (
        not isinstance(value, dict)
        or not required <= set(value)
        or set(value) - required - optional
    ):
        raise ValueError("Study manifest request_budget fields are invalid")
    return StudyRequestBudget(
        max_c2_calls_per_game=manifest_positive_int(
            value["max_c2_calls_per_game"], "max_c2_calls_per_game"
        ),
        max_press_calls_per_game=manifest_positive_int(
            value["max_press_calls_per_game"],
            "max_press_calls_per_game",
            minimum=0,
        ),
        input_tokens_bound=_optional_int(value, "input_tokens_bound"),
        max_output_tokens=_optional_int(value, "max_output_tokens"),
        max_cost_usd=_optional_cost(value, "max_cost_usd"),
        max_cost_per_request_usd=_optional_cost(value, "max_cost_per_request_usd"),
        transport_retry_margin=_optional_int(
            value, "transport_retry_margin", minimum=0
        ),
    )


def request_budget_payload(budget: StudyRequestBudget) -> dict[str, int | float]:
    return {key: value for key, value in budget.__dict__.items() if value is not None}


def optional_text(payload: dict[str, Any], field: str) -> str | None:
    if field not in payload:
        return None
    value = payload[field]
    if not isinstance(value, str) or not value:
        raise ValueError(f"Study manifest {field} must be a nonempty string")
    return value


def optional_choice(
    payload: dict[str, Any], field: str, choices: set[str]
) -> str | None:
    value = optional_text(payload, field)
    if value is not None and value not in choices:
        raise ValueError(f"Study manifest {field} is invalid")
    return value


def optional_sha256(payload: dict[str, Any], field: str) -> str | None:
    value = optional_text(payload, field)
    if value is not None and (
        len(value) != 64
        or any(character not in string.hexdigits for character in value)
    ):
        raise ValueError(f"Study manifest {field} must be a SHA-256 digest")
    return value


def manifest_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"Study manifest {field} must be a nonempty string")
    return value


def manifest_positive_int(value: Any, field: str, minimum: int = 1) -> int:
    if not is_strict_int(value) or value < minimum:
        raise ValueError(f"Study manifest {field} must be an integer >= {minimum}")
    return value


def _optional_int(payload: dict[str, Any], field: str, minimum: int = 1) -> int | None:
    if field not in payload:
        return None
    return manifest_positive_int(payload[field], field, minimum)


def _optional_cost(payload: dict[str, Any], field: str) -> float | None:
    if field not in payload:
        return None
    value = payload[field]
    if not isinstance(value, int | float) or isinstance(value, bool):
        raise ValueError(f"Study manifest {field} must be a finite nonnegative number")
    number = float(value)
    if number < 0 or not math.isfinite(number):
        raise ValueError(f"Study manifest {field} must be a finite nonnegative number")
    return number


__all__ = [
    "load_request_budget",
    "optional_choice",
    "optional_sha256",
    "optional_text",
    "request_budget_payload",
]
