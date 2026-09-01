"""DATE multi-operation atomicity test."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.date_world import (
    admit_transition,
    initialize_run,
    instantiate_patch,
    load_profile,
)
from nuclear_war_contest.date_world.tracer_fixtures import (
    fixture_event,
    operations_patch,
)

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)


def test_second_failed_precondition_rolls_back_the_first_operation() -> None:
    profile = load_profile(PROFILE_PATH)
    forecast = admit_transition(
        profile,
        initialize_run(profile, "atomic-rejection-run"),
        profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
    ).run
    event = fixture_event(
        "ATOMIC_PRECONDITION",
        hour=5,
        patch_id="PATCH_ATOMIC_PRECONDITION",
        affected_ids=[
            "AFF_US_RIDGE_ISR_WINDOW",
            "AFF_HIM_SOUTH_PASS_SUPPORT_WINDOW",
        ],
    )
    operations = [
        {
            "operation": "set_affordance_state",
            "affordance_id": "AFF_US_RIDGE_ISR_WINDOW",
            "expected": "available",
            "value": "intermittent",
        },
        {
            "operation": "set_affordance_state",
            "affordance_id": "AFF_HIM_SOUTH_PASS_SUPPORT_WINDOW",
            "expected": "intermittent",
            "value": "restricted",
        },
    ]
    patch = instantiate_patch(forecast, operations_patch(event, operations))

    result = admit_transition(profile, forecast, event, patch)

    assert result.receipt.reason_codes == ("failed_precondition",)
    assert result.run.current_core() == forecast.current_core()
    assert result.run.ledger() == forecast.ledger()
