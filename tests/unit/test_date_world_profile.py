"""DATE candidate-profile behavior tests."""

from __future__ import annotations

from pathlib import Path

from nuclear_war_contest.date_world import load_profile, project_outcomes

PROFILE_PATH = (
    Path(__file__).parents[2] / "docs" / "contest" / "DATE_PROFILE.candidate.json"
)
PROFILE_HASH = "64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477"


def test_load_candidate_profile_binds_identity_and_initial_core() -> None:
    profile = load_profile(PROFILE_PATH)

    assert profile.profile_id == "ridge_seizure.limited_fait_accompli.default.v0_1"
    assert profile.profile_version == "0.1.1"
    assert profile.content_hash == PROFILE_HASH
    assert profile.initial_core()["core_version"] == 0


def test_project_outcomes_resolves_declared_core_selectors_without_mutation() -> None:
    core = load_profile(PROFILE_PATH).initial_core()
    original_core = load_profile(PROFILE_PATH).initial_core()

    outcomes = project_outcomes(core)

    assert outcomes == {
        "ridge_control": "OLV",
        "talus_control": "OLV",
        "himaldesh_recapture_status": "not_authorized",
        "us_commitment_state": "none",
        "escalation_state": "conventional_crisis",
        "us_observation_state": "available",
        "himaldesh_support_state": "available",
        "terminal_state": "open",
    }
    assert core == original_core
