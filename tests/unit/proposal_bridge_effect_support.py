"""Resolved dependent effect fixture for proposal bridge tests."""

from __future__ import annotations

from copy import deepcopy

from tests.unit.proposal_bridge_test_support import copied_payload

from nuclear_war_contest.date_world.identity import canonical_hash


def resolved_second_effect_payload():
    payload = copied_payload()
    effect = payload["proposals"][0]["effects"][1]
    effect["authority_record_id"] = "AUTH_EFFECT_TRANSMIT_001"
    effect["capability_record_ids"] = ["CAP_ACTIVITY_US_TRANSMIT_001"]
    clarification = payload["clarifications"][1]
    clarification["original_effect_hash"] = canonical_hash(effect)
    clarification["status"] = "resolved"
    clarification["resolved_fields"] = {
        "object_or_audience": ["Himaldesh liaison channel"]
    }
    resolved = deepcopy(effect)
    resolved["object_or_audience"] = ["Himaldesh liaison channel"]
    resolved["unresolved_field_ids"] = []
    authority = deepcopy(payload["effect_authority_records"][0])
    authority.update(
        {
            "authority_record_id": effect["authority_record_id"],
            "effect_id": effect["effect_id"],
            "resolved_effect_hash": canonical_hash(resolved),
        }
    )
    payload["effect_authority_records"].append(authority)
    capability = deepcopy(payload["capability_records"][0])
    capability.update(
        {
            "capability_record_id": effect["capability_record_ids"][0],
            "effect_id": effect["effect_id"],
        }
    )
    payload["capability_records"].append(capability)
    return payload


__all__ = ["resolved_second_effect_payload"]
