"""Execution adapters and billable-backend policy checks."""

from __future__ import annotations

from typing import Any

from nuclear_war_concordia.call_budget import ChannelCallBudget
from nuclear_war_concordia.config import load_concordia_no_press_config
from nuclear_war_concordia.harness import run_concordia_no_press_game

from .manifest_types import StudyManifest, StudyRequestBudget
from .preflight_authorization import validate_live_preflight


def run_payload(
    payload: dict[str, Any],
    budget: StudyRequestBudget | None = None,
    prior_metrics: dict[str, Any] | None = None,
    cost_state: dict[str, float] | None = None,
) -> dict[str, Any]:
    config = load_concordia_no_press_config(payload)
    call_budget = (
        ChannelCallBudget(
            c2_cap=budget.max_c2_calls_per_game,
            press_cap=budget.max_press_calls_per_game,
            provider_attempt_multiplier=_retry_multiplier(config, budget),
            input_tokens_bound=getattr(budget, "input_tokens_bound", None),
            max_cost_usd=getattr(budget, "max_cost_usd", None),
            max_cost_per_request_usd=getattr(budget, "max_cost_per_request_usd", None),
            initial_metrics=prior_metrics,
            shared_cost_state=cost_state,
        )
        if budget is not None
        else None
    )
    return run_concordia_no_press_game(config, call_budget)


def validate_execution_budget(manifest: StudyManifest) -> None:
    live_models = [
        model
        for model in manifest.models
        if model.provider != "offline"
        or model.backend in {"concordia_http", "concordia_native_http"}
    ]
    if not live_models:
        return
    if manifest.request_budget is None:
        raise ValueError("Live study models require a frozen request_budget")
    validate_live_preflight(manifest)


__all__ = ["run_payload", "validate_execution_budget"]


def _retry_multiplier(config: Any, budget: StudyRequestBudget) -> int:
    retries = max(
        (seat.max_retries for seat in config.seats.values()),
        default=0,
    )
    transport_margin = getattr(budget, "transport_retry_margin", 0) or 0
    return (retries + 1) * (transport_margin + 1)
