"""Ordered no-model execution of authored proposal effects."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.models import DateRun
from nuclear_war_contest.date_world.profile import DateProfile

from .proposal_bridge_consequence import admit_consequence_proposal
from .proposal_bridge_effect_results import block_effect, effect_result
from .proposal_bridge_models import ProposalBridgeFixture
from .proposal_bridge_resolution import (
    resolve_effect,
    validate_effect_authority,
    validate_effect_capabilities,
)


def execute_proposal_effects(
    profile: DateProfile, fixture: ProposalBridgeFixture, world: DateRun
) -> tuple[list[dict[str, Any]], DateRun]:
    payload = fixture.payload()
    cycle = fixture.cycle_receipt()
    clarifications = {item["effect_id"]: item for item in payload["clarifications"]}
    authorities = {
        item["authority_record_id"]: item
        for item in payload["effect_authority_records"]
    }
    capabilities = {
        item["capability_record_id"]: item for item in payload["capability_records"]
    }
    consequences = {
        item["consequence_proposal_id"]: item
        for item in payload["consequence_proposals"]
    }
    decision_id = cycle["run"]["decision_record"]["product_id"]
    authority_seat_id = cycle["run"]["decision_route"]["owning_authority_seat_id"]
    statuses: dict[str, str] = {}
    world_event_ids: dict[str, str] = {}
    results: list[dict[str, Any]] = []
    for proposal in payload["proposals"]:
        for effect in proposal["effects"]:
            consequence = consequences[effect["consequence_proposal_id"]]
            clarification = clarifications.get(effect["effect_id"])
            base = effect_result(proposal, effect, clarification, consequence)
            dependencies = effect["dependency_effect_ids"]
            if any(statuses[item] != "admitted" for item in dependencies):
                result = block_effect(base, "blocked_dependency")
            else:
                result, world = _execute_effect(
                    profile,
                    world,
                    proposal,
                    effect,
                    base,
                    authorities,
                    capabilities,
                    consequence,
                    decision_id,
                    authority_seat_id,
                    [world_event_ids[item] for item in dependencies],
                )
            statuses[effect["effect_id"]] = result["status"]
            if result["status"] == "admitted":
                world_event_ids[effect["effect_id"]] = result["world_event"][
                    "template_id"
                ]
            results.append(result)
    return results, world


def _execute_effect(
    profile: DateProfile,
    world: DateRun,
    proposal: dict[str, Any],
    effect: dict[str, Any],
    base: dict[str, Any],
    authorities: dict[str, dict[str, Any]],
    capabilities: dict[str, dict[str, Any]],
    consequence: dict[str, Any],
    decision_id: str,
    authority_seat_id: str,
    required_world_parent_ids: list[str],
) -> tuple[dict[str, Any], DateRun]:
    resolved, reason = resolve_effect(effect, base["clarification"])
    if reason or resolved is None:
        return block_effect(base, reason or "unresolved_clarification"), world
    base["resolved_effect"] = resolved
    authority_id = resolved["authority_record_id"]
    authority, reason = validate_effect_authority(
        resolved,
        proposal,
        authorities.get(authority_id) if authority_id is not None else None,
        decision_id,
        authority_seat_id,
    )
    base["authority_result"] = authority
    if reason:
        return block_effect(base, reason), world
    capability_results, reason = validate_effect_capabilities(
        resolved, proposal["actor_id"], capabilities, world.current_core()
    )
    base["capability_results"] = capability_results
    if reason:
        return block_effect(base, reason), world
    outcome = admit_consequence_proposal(
        profile,
        world,
        proposal,
        resolved,
        consequence,
        decision_id,
        capability_results,
        required_world_parent_ids,
    )
    base["world_event"] = outcome.event
    base["world_receipt"] = outcome.world_receipt
    if outcome.reason_codes:
        return block_effect(base, *outcome.reason_codes), outcome.run
    base["status"] = "admitted"
    return base, outcome.run


__all__ = ["execute_proposal_effects"]
