"""Fail-closed channel-cap enforcement for study attempts."""

from __future__ import annotations

from typing import Any

from nuclear_war_env.integer_validation import is_strict_int

from .manifest_types import StudyRequestBudget
from .runner_budget_validation import (
    derived_metrics,
    validate_budget_metrics,
    validate_channel_metrics,
    validate_stored_metrics,
)


class ChannelCapExceeded(ValueError):
    """Raised when a completed attempt exceeds its frozen channel budget."""

    def __init__(self, channel: str, observed: int, cap: int) -> None:
        self.channel = channel
        self.observed = observed
        self.cap = cap
        self.partial_metrics: dict[str, Any] | None = None
        super().__init__(f"{channel} channel cap exceeded: {observed} > {cap}")


def enforce_channel_caps(
    result: dict[str, Any],
    budget: StudyRequestBudget,
    initial_metrics: dict[str, Any] | None = None,
) -> None:
    metrics = derived_metrics(result)
    summary = result.get("summary")
    stored = summary.get("channel_metrics") if isinstance(summary, dict) else None
    if metrics is not None:
        validate_stored_metrics(stored, metrics)
    budget_metrics = (
        summary.get("budget_metrics") if isinstance(summary, dict) else None
    )
    if isinstance(budget_metrics, dict):
        validate_budget_metrics(result, initial_metrics=initial_metrics)
        metrics = budget_metrics
    if metrics is None:
        metrics = result.get("channel_metrics")
        if not isinstance(metrics, dict) and isinstance(summary, dict):
            metrics = summary.get("channel_metrics")
    if not isinstance(metrics, dict):
        raise ValueError("Channel metrics are required for budget enforcement")
    _check_channel(metrics, "c2", budget.max_c2_calls_per_game)
    _check_channel(metrics, "press", budget.max_press_calls_per_game)


def _check_channel(metrics: dict[str, Any], channel: str, cap: int) -> None:
    payload = metrics.get(channel)
    if not isinstance(payload, dict) or not is_strict_int(payload.get("call_count")):
        raise ValueError(f"Channel metrics are missing {channel} call_count")
    observed = payload["call_count"]
    if observed < 0:
        raise ValueError(f"Channel metrics are negative for {channel}")
    if observed > cap:
        error = ChannelCapExceeded(channel, observed, cap)
        error.partial_metrics = metrics
        raise error
__all__ = [
    "ChannelCapExceeded",
    "enforce_channel_caps",
    "validate_budget_metrics",
    "validate_channel_metrics",
]
