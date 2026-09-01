"""Attributable proposal effect result records."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def effect_result(
    proposal: dict[str, Any],
    effect: dict[str, Any],
    clarification: dict[str, Any] | None,
    consequence: dict[str, Any],
) -> dict[str, Any]:
    return {
        "proposal_id": proposal["proposal_id"],
        "effect_id": effect["effect_id"],
        "source_component_ids": deepcopy(effect["source_component_ids"]),
        "status": "pending",
        "reason_codes": [],
        "original_effect": deepcopy(effect),
        "resolved_effect": None,
        "clarification": deepcopy(clarification),
        "authority_result": None,
        "capability_results": [],
        "consequence_proposal": deepcopy(consequence),
        "world_event": None,
        "state_patch": deepcopy(consequence["state_patch"]),
        "world_receipt": None,
    }


def block_effect(result: dict[str, Any], *reasons: str) -> dict[str, Any]:
    result["status"] = "blocked"
    result["reason_codes"] = list(reasons)
    return result


__all__ = ["block_effect", "effect_result"]
