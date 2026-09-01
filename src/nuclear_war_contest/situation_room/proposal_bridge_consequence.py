"""State-bounded consequence proposal admission into the DATE kernel."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from nuclear_war_contest.date_world.identity import core_hash
from nuclear_war_contest.date_world.models import DateRun
from nuclear_war_contest.date_world.patching import instantiate_patch
from nuclear_war_contest.date_world.profile import DateProfile
from nuclear_war_contest.date_world.transition import admit_transition


@dataclass(frozen=True)
class ConsequenceOutcome:
    run: DateRun
    event: dict[str, Any] | None
    world_receipt: dict[str, Any] | None
    reason_codes: tuple[str, ...]


def admit_consequence_proposal(
    profile: DateProfile,
    run: DateRun,
    proposal: dict[str, Any],
    effect: dict[str, Any],
    consequence: dict[str, Any],
    decision_record_id: str,
    capability_results: list[dict[str, Any]],
    required_world_parent_ids: list[str],
) -> ConsequenceOutcome:
    core = run.current_core()
    core_read = consequence["core_read"]
    if (
        core_read["profile_hash"] != profile.content_hash
        or core_read["core_version"] != core["core_version"]
        or core_read["core_hash"] != core_hash(core)
    ):
        return ConsequenceOutcome(run, None, None, ("stale_core",))
    expected_parents = {
        decision_record_id,
        proposal["proposal_id"],
        effect["effect_id"],
    }
    if set(consequence["artifact_parent_ids"]) != expected_parents:
        return ConsequenceOutcome(run, None, None, ("causal_mismatch",))
    if not set(required_world_parent_ids) <= set(consequence["world_parent_event_ids"]):
        return ConsequenceOutcome(run, None, None, ("causal_mismatch",))
    disclosed_entities = set(core_read["entity_ids"])
    capability_entities = {item["record"]["entity_id"] for item in capability_results}
    affected_entities = set(consequence["affected_entity_ids"])
    if not (capability_entities | affected_entities) <= disclosed_entities:
        return ConsequenceOutcome(run, None, None, ("causal_mismatch",))
    patch_targets = _patch_target_ids(consequence["state_patch"])
    if not patch_targets <= (disclosed_entities & affected_entities):
        return ConsequenceOutcome(run, None, None, ("causal_mismatch",))
    if consequence["represented_room_decision_actor_ids"]:
        return ConsequenceOutcome(run, None, None, ("represented_room_decision",))
    event = _world_event(consequence)
    patch = None
    if consequence["state_patch"] is not None:
        try:
            patch = instantiate_patch(run, consequence["state_patch"])
        except ValueError:
            return ConsequenceOutcome(run, event, None, ("invalid_envelope",))
    result = admit_transition(profile, run, event, patch)
    return ConsequenceOutcome(
        result.run,
        event,
        asdict(result.receipt),
        result.receipt.reason_codes,
    )


def _world_event(consequence: dict[str, Any]) -> dict[str, Any]:
    state_patch = consequence["state_patch"]
    return {
        "template_id": consequence["consequence_proposal_id"],
        "event_kind": "excon_consequence",
        "episode_hour": consequence["episode_hour"],
        "causal_parent_ids": consequence["world_parent_event_ids"],
        "source": "excon_consequence",
        "affected_entity_ids": consequence["affected_entity_ids"],
        "audience_ids": consequence["audience_ids"],
        "evidence_ids": consequence["evidence_ids"],
        "assumptions": consequence["assumptions"],
        "uncertainty": consequence["uncertainty"],
        "content": consequence["content"],
        "patch_template_id": (
            state_patch.get("template_id") if state_patch is not None else None
        ),
    }


def _patch_target_ids(state_patch: dict[str, Any] | None) -> set[str]:
    if state_patch is None or not isinstance(state_patch.get("operations"), list):
        return set()
    targets: set[str] = set()
    for operation in state_patch["operations"]:
        if not isinstance(operation, dict):
            continue
        if operation.get("operation") == "set_affordance_state":
            target = operation.get("affordance_id")
        elif operation.get("operation") == "set_force_package_readiness":
            target = operation.get("force_package_id")
        else:
            continue
        if isinstance(target, str):
            targets.add(target)
    return targets


__all__ = ["ConsequenceOutcome", "admit_consequence_proposal"]
