"""Study-wide spend state reconstructed from append-only attempt receipts."""

from __future__ import annotations

import math
from collections.abc import Mapping
from typing import Any


def initial_cost_state(records: Mapping[str, dict[str, Any]]) -> dict[str, float]:
    return {
        "reserved_cost_usd": _aggregate(records, "reserved_cost_usd"),
        "actual_cost_usd": _aggregate(records, "actual_cost_usd"),
    }


def _aggregate(records: Mapping[str, dict[str, Any]], field: str) -> float:
    scoped: list[float] = []
    local: list[float] = []
    scoped_field = f"study_{field}"
    for record in records.values():
        metrics = _metrics(record)
        if not isinstance(metrics, dict):
            continue
        scoped_value = _number(metrics.get(scoped_field))
        local_value = _number(metrics.get(field))
        if scoped_value is not None:
            scoped.append(scoped_value)
        elif local_value is not None:
            local.append(local_value)
    return max(scoped, default=0.0) + sum(local)


def _metrics(record: dict[str, Any]) -> dict[str, Any] | None:
    budget = record.get("budget_metrics")
    if isinstance(budget, dict):
        return budget
    admissibility = record.get("admissibility")
    if isinstance(admissibility, dict):
        metrics = admissibility.get("channel_metrics")
        if isinstance(metrics, dict):
            return metrics
    return None


def _number(value: Any) -> float | None:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or value < 0
        or not math.isfinite(float(value))
    ):
        return None
    return float(value)


__all__ = ["initial_cost_state"]
