"""DATE World transition behavior tests."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.date_world import (
    admit_transition,
    core_hash,
    initialize_run,
    instantiate_patch,
    load_profile,
    project_outcomes,
    replay_run,
)

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)


def test_authored_forecast_is_a_ledger_only_transition() -> None:
    profile = load_profile(PROFILE_PATH)
    original = initialize_run(profile, "forecast-run")
    before = original.current_core()

    result = admit_transition(
        profile,
        original,
        profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
    )

    assert result.receipt.accepted is True
    assert result.receipt.patch_instance_id is None
    assert len(result.receipt.event_template_hash) == 64
    assert result.receipt.reason_codes == ()
    assert result.run.current_core()["core_version"] == 0
    assert core_hash(result.run.current_core()) == core_hash(before)
    assert result.run.ledger()[0]["template_id"] == "OBS_WX_RIDGE_FORECAST_01"
    assert original.current_core() == before
    assert original.ledger() == ()


def test_weather_patch_atomically_updates_both_affordances() -> None:
    profile = load_profile(PROFILE_PATH)
    forecast = admit_transition(
        profile,
        initialize_run(profile, "weather-run"),
        profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
    ).run
    patch = instantiate_patch(
        forecast, profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01")
    )

    result = admit_transition(
        profile,
        forecast,
        profile.event_template("WX_RIDGE_FRONT_01"),
        patch,
    )

    outcomes = project_outcomes(result.run.current_core())
    assert result.receipt.accepted is True
    assert result.receipt.patch_instance_id == patch.patch_instance_id
    assert result.run.current_core()["core_version"] == 1
    assert outcomes["us_observation_state"] == "intermittent"
    assert outcomes["himaldesh_support_state"] == "restricted"
    assert forecast.current_core()["core_version"] == 0

    replayed = replay_run(profile, result.run)
    assert core_hash(replayed.current_core()) == core_hash(result.run.current_core())
    assert replayed.ledger() == result.run.ledger()
