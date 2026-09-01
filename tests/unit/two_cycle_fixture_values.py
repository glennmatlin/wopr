"""Shared values for deterministic two-cycle development fixtures."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world import (
    admit_transition,
    initialize_run,
    instantiate_patch,
    load_profile,
)
from nuclear_war_contest.date_world.identity import core_hash

CONTEST_PATH = Path(__file__).parents[2] / "docs" / "contest"
ARTIFACT_NAMES = {
    "source_register": "US_SOURCE_REGISTER.candidate.json",
    "charter": "US_CHARTER.candidate.json",
    "ratification": "US_CHARTER_RATIFICATION.json",
    "cycle1_fixture": "US_CYCLE1_FIXTURE.development.json",
    "cycle1_receipt": "US_CYCLE1_RECEIPT.json",
    "bridge_fixture": "US_PROPOSAL_BRIDGE_FIXTURE.development.json",
    "bridge_receipt": "US_PROPOSAL_BRIDGE_RECEIPT.json",
    "date_profile": "DATE_PROFILE.candidate.json",
    "date_tracer_receipt": "DATE_TRACER_RECEIPT.json",
    "cycle2_fixture": "US_CYCLE2_FIXTURE.development.json",
}
WORLD_PARENT_IDS = [
    "EXCON_CONSEQUENCE_PREPARATION_001",
    "WX_RIDGE_FRONT_01",
    "OBS_WX_RIDGE_CONFIRMED_01",
]


def load_json(name: str) -> dict[str, Any]:
    payload = json.loads((CONTEST_PATH / name).read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def replace_cycle_ids(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("USC1_", "USC2_").replace("CYCLE_1", "CYCLE_2")
    if isinstance(value, list):
        return [replace_cycle_ids(item) for item in value]
    if isinstance(value, dict):
        return {key: replace_cycle_ids(item) for key, item in value.items()}
    return deepcopy(value)


def barrier_core_binding() -> dict[str, Any]:
    profile = load_profile(CONTEST_PATH / ARTIFACT_NAMES["date_profile"])
    bridge = load_json(ARTIFACT_NAMES["bridge_receipt"])
    admitted = next(
        item for item in bridge["run"]["effect_results"] if item["status"] == "admitted"
    )
    run = initialize_run(profile, "two-cycle-fixture-binding")
    run = admit_transition(
        profile, run, profile.event_template("OBS_WX_RIDGE_FORECAST_01")
    ).run
    run = admit_transition(profile, run, admitted["world_event"]).run
    patch = instantiate_patch(run, profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01"))
    run = admit_transition(
        profile, run, profile.event_template("WX_RIDGE_FRONT_01"), patch
    ).run
    run = admit_transition(
        profile, run, profile.event_template("OBS_WX_RIDGE_CONFIRMED_01")
    ).run
    return {
        "core_version": run.current_core()["core_version"],
        "core_hash": core_hash(run.current_core()),
    }


__all__ = [
    "ARTIFACT_NAMES",
    "CONTEST_PATH",
    "WORLD_PARENT_IDS",
    "barrier_core_binding",
    "load_json",
    "replace_cycle_ids",
]
