"""Clarification, authority, and capability resolution for proposal effects."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash


def resolve_effect(
    effect: dict[str, Any], clarification: dict[str, Any] | None
) -> tuple[dict[str, Any] | None, str | None]:
    resolved = deepcopy(effect)
    unresolved = set(resolved["unresolved_field_ids"])
    if not unresolved:
        return resolved, None
    if clarification is None or clarification["status"] != "resolved":
        return None, "unresolved_clarification"
    for field, value in clarification["resolved_fields"].items():
        resolved[field] = deepcopy(value)
        unresolved.discard(field)
    resolved["unresolved_field_ids"] = [
        field for field in effect["unresolved_field_ids"] if field in unresolved
    ]
    if unresolved:
        return None, "unresolved_clarification"
    return resolved, None


def validate_effect_authority(
    effect: dict[str, Any],
    proposal: dict[str, Any],
    authority: dict[str, Any] | None,
    decision_record_id: str,
    owning_authority_seat_id: str,
) -> tuple[dict[str, Any], str | None]:
    result = {"record": deepcopy(authority), "valid": False}
    if effect["authority_record_id"] is None or authority is None:
        return result, "missing_effect_authority"
    valid = (
        authority["authority_record_id"] == effect["authority_record_id"]
        and authority["effect_id"] == effect["effect_id"]
        and authority["resolved_effect_hash"] == canonical_hash(effect)
        and authority["actor_id"] == proposal["actor_id"]
        and authority["decision_record_id"] == decision_record_id
        and authority["authorizing_seat_id"] == owning_authority_seat_id
        and authority["status"] == "authorized"
        and authority["evidence_status"] == "development_fixture_non_evidence"
    )
    result["valid"] = valid
    return result, None if valid else "invalid_effect_authority"


def validate_effect_capabilities(
    effect: dict[str, Any],
    proposal_actor_id: str,
    capability_by_id: dict[str, dict[str, Any]],
    core: dict[str, Any],
) -> tuple[list[dict[str, Any]], str | None]:
    record_ids = effect["capability_record_ids"]
    if not record_ids:
        return [], "missing_capability"
    results: list[dict[str, Any]] = []
    for record_id in record_ids:
        record = capability_by_id[record_id]
        satisfied = (
            record["effect_id"] == effect["effect_id"]
            and record["actor_id"] == proposal_actor_id
            and _satisfied(record, core)
        )
        results.append({"record": deepcopy(record), "satisfied": satisfied})
    all_satisfied = all(item["satisfied"] for item in results)
    reason = None if all_satisfied else "missing_capability"
    return results, reason


def _satisfied(record: dict[str, Any], core: dict[str, Any]) -> bool:
    predicate = record["predicate_type"]
    entity_id = record["entity_id"]
    actor_id = record["actor_id"]
    expected = record["expected_value"]
    if predicate == "activity_owned_by":
        return expected is None and _field_matches(
            core["activities"], "activity_id", entity_id, "owner_actor_id", actor_id
        )
    if predicate == "affordance_controlled_by":
        return expected is None and _field_matches(
            core["affordances"],
            "affordance_id",
            entity_id,
            "controller_actor_id",
            actor_id,
        )
    if predicate == "affordance_state_is":
        return _field_matches(
            core["affordances"], "affordance_id", entity_id, "state", expected
        )
    if predicate == "force_package_owned_by":
        return expected is None and _field_matches(
            core["force_packages"],
            "force_package_id",
            entity_id,
            "owner_actor_id",
            actor_id,
        )
    return False


def _field_matches(
    records: list[dict[str, Any]],
    identity_field: str,
    identity: str,
    field: str,
    expected: object,
) -> bool:
    matches = [item for item in records if item[identity_field] == identity]
    return len(matches) == 1 and matches[0][field] == expected


__all__ = [
    "resolve_effect",
    "validate_effect_authority",
    "validate_effect_capabilities",
]
