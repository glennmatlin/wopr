"""Bounded proposal clarification validation."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .proposal_bridge_fixture_shape import CLARIFIABLE_FIELDS


def validate_clarification_references(
    clarifications: list[dict[str, Any]],
    effects: dict[str, tuple[str, dict[str, Any]]],
) -> None:
    by_effect: set[str] = set()
    for item in clarifications:
        effect_id = item["effect_id"]
        if effect_id not in effects or effect_id in by_effect:
            reason = "duplicate_id" if effect_id in by_effect else "unknown_reference"
            raise ValueError(f"{reason}: clarification effect is invalid")
        by_effect.add(effect_id)
        proposal_id, effect = effects[effect_id]
        if item["proposal_id"] != proposal_id:
            raise ValueError("unknown_reference: clarification proposal is invalid")
        if item["original_effect_hash"] != canonical_hash(effect):
            raise ValueError("identity_mismatch: clarification effect hash is invalid")
        requested = set(item["requested_field_ids"])
        if not requested <= set(effect["unresolved_field_ids"]):
            raise ValueError("invalid_clarification: field was not unresolved")
        if any(effect[field] is not None for field in requested):
            detail = "existing policy cannot be rewritten"
            raise ValueError(f"invalid_clarification: {detail}")
        resolved = item["resolved_fields"]
        if item["status"] == "unresolved" and resolved:
            detail = "unresolved response changed policy"
            raise ValueError(f"invalid_clarification: {detail}")
        if item["status"] == "resolved" and set(resolved) != requested:
            raise ValueError("invalid_clarification: resolved fields are incomplete")
        for field, value in resolved.items():
            _validate_resolution(field, value)


def _validate_resolution(field: str, value: object) -> None:
    if field not in CLARIFIABLE_FIELDS:
        raise ValueError("invalid_clarification: resolved field is invalid")
    if field in {"intended_effect", "timing"}:
        if not isinstance(value, str) or not value:
            raise ValueError("invalid_clarification: resolved text is invalid")
        return
    if (
        not isinstance(value, list)
        or not value
        or any(not isinstance(item, str) or not item for item in value)
    ):
        raise ValueError("invalid_clarification: resolved list is invalid")


__all__ = ["validate_clarification_references"]
