"""Consequence proposal fixture shape validation."""

from __future__ import annotations

from typing import Any

from .proposal_bridge_schema import CORE_READ_FIELDS
from .proposal_bridge_validation_helpers import (
    require_text_list,
    require_texts,
)


def validate_consequence(item: dict[str, Any]) -> None:
    require_texts(
        item,
        (
            "consequence_proposal_id",
            "source_proposal_id",
            "effect_id",
            "adjudicator_id",
            "evidence_status",
            "content",
        ),
    )
    for field in (
        "artifact_parent_ids",
        "world_parent_event_ids",
        "affected_entity_ids",
        "audience_ids",
        "evidence_ids",
        "assumptions",
        "alternatives",
        "represented_room_decision_actor_ids",
    ):
        require_text_list(item[field], field)
    core_read = item["core_read"]
    if not isinstance(core_read, dict) or set(core_read) != CORE_READ_FIELDS:
        raise ValueError("invalid_envelope: consequence Core read is invalid")
    require_texts(core_read, ("profile_hash", "core_hash"))
    require_text_list(core_read["entity_ids"], "Core read entities")
    _require_integer(item["episode_hour"], "consequence hour")
    _require_integer(core_read["core_version"], "Core read version")
    if not isinstance(item["uncertainty"], dict):
        raise ValueError("invalid_envelope: consequence uncertainty is invalid")
    if item["evidence_status"] != "development_fixture_non_evidence":
        raise ValueError("invalid_envelope: consequence evidence is invalid")
    if item["adjudicator_id"] != "EXCON_DEVELOPMENT_FIXTURE":
        raise ValueError("invalid_envelope: consequence adjudicator is invalid")
    if not isinstance(item["resulting_injects"], list):
        raise ValueError("invalid_envelope: resulting injects are invalid")
    if item["state_patch"] is not None and not isinstance(item["state_patch"], dict):
        raise ValueError("invalid_envelope: consequence State Patch is invalid")
    if not isinstance(item["open_content"], dict):
        raise ValueError("invalid_envelope: consequence open content is invalid")


def _require_integer(value: object, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"invalid_envelope: {label} is invalid")


__all__ = ["validate_consequence"]
