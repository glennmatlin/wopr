"""Ordered DATE World barriers for the two-cycle episode."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from nuclear_war_contest.date_world import (
    DateProfile,
    DateRun,
    ValidationReceipt,
    admit_transition,
    initialize_run,
    instantiate_patch,
)
from nuclear_war_contest.date_world.identity import core_hash


@dataclass(frozen=True)
class BarrierResult:
    run: DateRun
    receipt: dict[str, Any]
    core_hash: str


def initialize_episode_world(
    profile: DateProfile, run_id: str
) -> tuple[DateRun, dict[str, Any]]:
    run = initialize_run(profile, run_id)
    result = admit_transition(
        profile, run, profile.event_template("OBS_WX_RIDGE_FORECAST_01")
    )
    return _accepted(result.run, result.receipt, "forecast"), _receipt(result.receipt)


def admit_bridge_consequence(
    profile: DateProfile, run: DateRun, bridge: dict[str, Any]
) -> tuple[DateRun, dict[str, Any]]:
    admitted = [
        item for item in bridge["effect_results"] if item["status"] == "admitted"
    ]
    blocked = [item for item in bridge["effect_results"] if item["status"] == "blocked"]
    if len(admitted) != 1 or len(blocked) != 1:
        raise ValueError("bridge_result_mismatch")
    result = admit_transition(profile, run, admitted[0]["world_event"])
    return _accepted(result.run, result.receipt, "bridge"), _receipt(result.receipt)


def admit_matched_weather(profile: DateProfile, run: DateRun) -> BarrierResult:
    patch = instantiate_patch(run, profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01"))
    weather = admit_transition(
        profile, run, profile.event_template("WX_RIDGE_FRONT_01"), patch
    )
    current = _accepted(weather.run, weather.receipt, "weather")
    confirmation = admit_transition(
        profile, current, profile.event_template("OBS_WX_RIDGE_CONFIRMED_01")
    )
    final = _accepted(confirmation.run, confirmation.receipt, "confirmation")
    return BarrierResult(
        run=final,
        receipt={
            "weather": _receipt(weather.receipt),
            "confirmation": _receipt(confirmation.receipt),
            "patch_instance_id": patch.patch_instance_id,
            "patch_template_hash": patch.template_hash,
        },
        core_hash=core_hash(final.current_core()),
    )


def _accepted(run: DateRun, receipt: ValidationReceipt, label: str) -> DateRun:
    if not receipt.accepted:
        raise ValueError(f"{label}_rejected:{receipt.reason_codes}")
    return run


def _receipt(receipt: ValidationReceipt) -> dict[str, Any]:
    from dataclasses import asdict

    return asdict(receipt)


__all__ = [
    "BarrierResult",
    "admit_bridge_consequence",
    "admit_matched_weather",
    "initialize_episode_world",
]
