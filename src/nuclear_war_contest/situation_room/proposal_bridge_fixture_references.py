"""Proposal bridge fixture identity and reference validation."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from nuclear_war_contest.date_world.profile import DateProfile

from .proposal_bridge_clarification_validation import (
    validate_clarification_references,
)
from .proposal_bridge_consequence_references import validate_consequence_references


def validate_bridge_fixture_references(
    payload: dict[str, Any], cycle: dict[str, Any], profile: DateProfile
) -> None:
    proposals = payload["proposals"]
    _unique(proposals, "proposal_id")
    effects = _effect_index(proposals)
    cycle_run = cycle["run"]
    package = cycle_run["policy_package"]
    decision = cycle_run["decision_record"]
    component_ids = {item["component_id"] for item in package["content"]["components"]}
    actors = {item["actor_id"] for item in profile.initial_core()["actors"]}
    for proposal in proposals:
        if proposal["actor_id"] not in actors:
            raise ValueError("unknown_reference: proposal actor is invalid")
        if proposal["source_policy_package_id"] != package["product_id"]:
            raise ValueError("unknown_reference: proposal package is invalid")
        if proposal["institutional_decision_record_id"] != decision["product_id"]:
            raise ValueError("unknown_reference: proposal decision is invalid")
        if not set(proposal["source_component_ids"]) <= component_ids:
            raise ValueError("unknown_reference: proposal component is invalid")
        _validate_effect_order(proposal, component_ids)
    validate_clarification_references(payload["clarifications"], effects)
    _validate_authorities(payload, effects, cycle, actors)
    _validate_capabilities(payload, effects, profile, actors)
    validate_consequence_references(payload, effects, profile, actors)


def _effect_index(
    proposals: list[dict[str, Any]],
) -> dict[str, tuple[str, dict[str, Any]]]:
    indexed: dict[str, tuple[str, dict[str, Any]]] = {}
    for proposal in proposals:
        for effect in proposal["effects"]:
            effect_id = effect["effect_id"]
            if effect_id in indexed:
                raise ValueError("duplicate_id: duplicate proposal effect_id")
            indexed[effect_id] = (proposal["proposal_id"], effect)
    return indexed


def _validate_effect_order(proposal: dict[str, Any], component_ids: set[str]) -> None:
    seen: set[str] = set()
    proposal_components = set(proposal["source_component_ids"])
    for effect in proposal["effects"]:
        if not set(effect["source_component_ids"]) <= (
            component_ids & proposal_components
        ):
            raise ValueError("unknown_reference: effect component is invalid")
        if not set(effect["dependency_effect_ids"]) <= seen:
            raise ValueError("dependency_order: effect dependency requires reordering")
        seen.add(effect["effect_id"])


def _validate_authorities(
    payload: dict[str, Any],
    effects: dict[str, tuple[str, dict[str, Any]]],
    cycle: dict[str, Any],
    actors: set[str],
) -> None:
    records = payload["effect_authority_records"]
    _unique(records, "authority_record_id")
    by_id = {item["authority_record_id"]: item for item in records}
    decision_id = cycle["run"]["decision_record"]["product_id"]
    active_seats = set(cycle["run"]["active_seat_ids"])
    for item in records:
        if item["effect_id"] not in effects or item["actor_id"] not in actors:
            raise ValueError("unknown_reference: effect authority target is invalid")
        if item["decision_record_id"] != decision_id:
            raise ValueError("unknown_reference: authority decision is invalid")
        if item["authorizing_seat_id"] not in active_seats:
            raise ValueError("unknown_reference: authority seat is invalid")
    for _, effect in effects.values():
        authority_id = effect["authority_record_id"]
        if authority_id is not None and authority_id not in by_id:
            raise ValueError("unknown_reference: effect authority record is unknown")


def _validate_capabilities(
    payload: dict[str, Any],
    effects: dict[str, tuple[str, dict[str, Any]]],
    profile: DateProfile,
    actors: set[str],
) -> None:
    records = payload["capability_records"]
    _unique(records, "capability_record_id")
    by_id = {item["capability_record_id"]: item for item in records}
    core = profile.initial_core()
    targets = {
        "activity_owned_by": {item["activity_id"] for item in core["activities"]},
        "affordance_controlled_by": {
            item["affordance_id"] for item in core["affordances"]
        },
        "affordance_state_is": {item["affordance_id"] for item in core["affordances"]},
        "force_package_owned_by": {
            item["force_package_id"] for item in core["force_packages"]
        },
    }
    for item in records:
        if item["effect_id"] not in effects or item["actor_id"] not in actors:
            raise ValueError("unknown_reference: capability target is invalid")
        if item["entity_id"] not in targets[item["predicate_type"]]:
            raise ValueError("unknown_reference: capability entity is invalid")
    for _, effect in effects.values():
        if not set(effect["capability_record_ids"]) <= set(by_id):
            raise ValueError("unknown_reference: effect capability record is unknown")


def _unique(items: Iterable[dict[str, Any]], field: str) -> None:
    values = [item[field] for item in items]
    if len(values) != len(set(values)):
        raise ValueError(f"duplicate_id: duplicate proposal bridge {field}")
