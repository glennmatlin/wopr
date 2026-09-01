"""Actor-specific decision and output checks for counterpart traces."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

EXPECTED_OUTPUT_HASHES = {
    "ACTOR_HIMALDESH": (
        "317c977a6656a4125e28e025323363a386dddcb394fe8bcf81e94f2f71d7aea2"
    ),
    "ACTOR_OLVANA": (
        "c1362fc0bdab5b9f18dd70f7750911bb31d88004d360a8325115d28c20ff27fe"
    ),
}


def decision_record_is_valid(
    actor_id: str, record: dict[str, Any], action: str
) -> bool:
    content = record.get("content")
    if not isinstance(content, dict) or content.get("action_class") != action:
        return False
    if actor_id == "ACTOR_HIMALDESH":
        prime_minister = content.get("prime_minister_position")
        president = content.get("president_position")
        return (
            isinstance(prime_minister, dict)
            and prime_minister.get("position") == "concur"
            and isinstance(president, dict)
            and president.get("position") == "concur"
        )
    decision = content.get("general_secretary_decision")
    return isinstance(decision, dict) and decision.get("decision") == (
        "approve_bounded_posture"
    )


def output_projection_is_valid(
    actor_id: str, projection: dict[str, Any], record: dict[str, Any]
) -> bool:
    content = record["content"]
    valid = projection["source_decision_record_id"] == record["product_id"]
    if actor_id == "ACTOR_HIMALDESH":
        valid = (
            valid and projection["output"]["content"] == content["output_components"]
        )
    else:
        components = content["output_components"]
        valid = valid and components.get("no_further_advance") is True
    return (
        valid
        and canonical_hash(projection["output"]) == EXPECTED_OUTPUT_HASHES[actor_id]
    )


__all__ = ["decision_record_is_valid", "output_projection_is_valid"]
