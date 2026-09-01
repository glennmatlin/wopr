"""DATE validator-order test."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.date_world import (
    admit_transition,
    initialize_run,
    instantiate_patch,
    load_profile,
)
from nuclear_war_contest.date_world.tracer_fixtures import fixture_event

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)


def test_patch_envelope_failure_precedes_retroactive_time() -> None:
    profile = load_profile(PROFILE_PATH)
    forecast = admit_transition(
        profile,
        initialize_run(profile, "validator-order-run"),
        profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
    ).run
    event = fixture_event(
        "MALFORMED_RETROACTIVE",
        hour=0,
        patch_id="PATCH_MALFORMED_RETROACTIVE",
    )
    malformed_patch = {
        "template_id": "PATCH_MALFORMED_RETROACTIVE",
        "effective_hour": 0,
        "causal_parent_ids": ["FIXTURE_MALFORMED_RETROACTIVE"],
        "operations": [],
        "arbitrary_path": "actors.USA",
    }

    result = admit_transition(
        profile,
        forecast,
        event,
        instantiate_patch(forecast, malformed_patch),
    )

    assert result.receipt.reason_codes == ("invalid_envelope",)
