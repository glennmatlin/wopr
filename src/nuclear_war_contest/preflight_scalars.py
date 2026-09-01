"""Scalar validators for the offline candidate model manifest."""

from __future__ import annotations

import math
from typing import Any

from nuclear_war_env.integer_validation import is_strict_int


def seeds(value: Any, field: str) -> tuple[int, ...]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"Candidate {field} must be a nonempty list")
    result = tuple(nonnegative_int(item, "seed") for item in value)
    if len(set(result)) != len(result):
        raise ValueError(f"Candidate {field} must be unique")
    return result


def text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"Candidate {field} must be a nonempty string")
    return value


def positive_int(value: Any, field: str) -> int:
    if not is_strict_int(value) or value < 1:
        raise ValueError(f"Candidate {field} must be a positive integer")
    return value


def nonnegative_int(value: Any, field: str) -> int:
    if not is_strict_int(value) or value < 0:
        raise ValueError(f"Candidate {field} must be a nonnegative integer")
    return value


def rate(value: Any, field: str) -> float:
    if not isinstance(value, int | float) or isinstance(value, bool):
        raise ValueError(f"Candidate {field} must be a finite nonnegative number")
    number = float(value)
    if number < 0 or not math.isfinite(number):
        raise ValueError(f"Candidate {field} must be a finite nonnegative number")
    return number
