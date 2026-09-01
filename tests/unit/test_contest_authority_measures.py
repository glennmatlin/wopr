"""Process measures from C2 deliberations."""

from __future__ import annotations

from nuclear_war_contest.measures import derive_measures
from nuclear_war_env.simulation import SimulationConfig, run_simulation


def test_authority_measures_count_bind_override_and_disagreement() -> None:
    replay = run_simulation(
        SimulationConfig(
            mode="table",
            players=3,
            seed=11,
            agent="decision_heuristic",
            max_turns=1,
        )
    )
    result = {
        "replay": replay,
        "c2_artifact": {
            "deliberations": [
                {
                    "rule": "executive_override",
                    "selected_action_id": "keep",
                    "members": [
                        {"member_id": "executive", "vote_action_id": "keep"},
                        {"member_id": "strategic_advisor", "vote_action_id": "other"},
                        {"member_id": "risk_advisor", "vote_action_id": "keep"},
                    ],
                },
                {
                    "rule": "weighted_majority",
                    "selected_action_id": "other",
                    "members": [
                        {"member_id": "executive", "vote_action_id": "keep"},
                        {"member_id": "strategic_advisor", "vote_action_id": "other"},
                        {"member_id": "risk_advisor", "vote_action_id": "other"},
                    ],
                },
                {
                    "rule": "threshold_not_met_default",
                    "selected_action_id": "keep",
                    "members": [
                        {"member_id": "executive", "vote_action_id": "keep"},
                        {"member_id": "strategic_advisor", "vote_action_id": "other"},
                        {"member_id": "risk_advisor", "vote_action_id": "third"},
                    ],
                },
            ]
        },
    }

    authority = derive_measures(result)["authority"]

    assert authority["deliberation_count"] == 3
    assert authority["disagreement_count"] == 3
    assert authority["threshold_failure_count"] == 1
    assert authority["executive_match_count"] == 2
    assert authority["executive_override_count"] == 1
