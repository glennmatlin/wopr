"""Consequence proposal reference validation."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.profile import DateProfile


def validate_consequence_references(
    payload: dict[str, Any],
    effects: dict[str, tuple[str, dict[str, Any]]],
    profile: DateProfile,
    actors: set[str],
) -> None:
    items = payload["consequence_proposals"]
    ids = [item["consequence_proposal_id"] for item in items]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate_id: duplicate consequence proposal")
    by_id = {item["consequence_proposal_id"]: item for item in items}
    entity_ids = profile.entity_ids()
    audiences = profile.declared_ids("audience_ids")
    evidence = profile.declared_ids("evidence_ids")
    for item in items:
        effect_entry = effects.get(item["effect_id"])
        if effect_entry is None or item["source_proposal_id"] != effect_entry[0]:
            raise ValueError("unknown_reference: consequence effect is invalid")
        core_read = item["core_read"]
        if core_read["profile_hash"] != profile.content_hash:
            raise ValueError("identity_mismatch: consequence profile is invalid")
        if not set(core_read["entity_ids"]) <= entity_ids:
            raise ValueError("unknown_reference: consequence Core read is invalid")
        if not set(item["affected_entity_ids"]) <= entity_ids:
            raise ValueError("unknown_reference: consequence entity is invalid")
        if not set(item["audience_ids"]) <= audiences:
            raise ValueError("unknown_reference: consequence audience is invalid")
        if not set(item["evidence_ids"]) <= evidence:
            raise ValueError("unknown_reference: consequence evidence is invalid")
        if not set(item["represented_room_decision_actor_ids"]) <= actors:
            raise ValueError("unknown_reference: represented actor is invalid")
    for _, effect in effects.values():
        consequence = by_id.get(effect["consequence_proposal_id"])
        if consequence is None or consequence["effect_id"] != effect["effect_id"]:
            raise ValueError("unknown_reference: effect consequence is invalid")


__all__ = ["validate_consequence_references"]
