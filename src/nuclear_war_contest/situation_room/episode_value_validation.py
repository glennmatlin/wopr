"""Nested value validation for strict two-cycle fixtures."""

from __future__ import annotations

from typing import Any


def validate_episode_values(payload: dict[str, Any]) -> None:
    forecast = payload["forecast_binding"]
    _strings(forecast, ("cycle1_input_id", "world_event_id", "relationship"))
    _text_list(forecast["shared_entity_ids"], "forecast entities", allow_empty=False)

    external = payload["cycle2_external_parent_ids"]
    _text_list(external, "external parents", allow_empty=False)
    reassessment = payload["cycle2_reassessment"]
    _strings(reassessment, ("prior_decision_id", "disposition"))
    _hash(reassessment["prior_decision_hash"], "prior decision hash")
    _hash(reassessment["core_hash"], "Core hash")
    version = reassessment["core_version"]
    if isinstance(version, bool) or not isinstance(version, int) or version < 0:
        raise ValueError("invalid_envelope: Core version is invalid")
    _text_list(reassessment["changed_evidence_ids"], "changed evidence", False)

    adjudication = payload["final_adjudication"]
    _text_list(adjudication["source_component_ids"], "source components", False)
    _text_list(adjudication["reason_codes"], "reason codes", False)
    _text_list(
        adjudication["represented_room_decision_actor_ids"],
        "represented Room decisions",
        True,
    )
    event = adjudication["world_event"]
    _strings(event, ("template_id", "event_kind", "source", "content"))
    hour = event["episode_hour"]
    if isinstance(hour, bool) or not isinstance(hour, int) or hour < 0:
        raise ValueError("invalid_envelope: event hour is invalid")
    for field in (
        "causal_parent_ids",
        "affected_entity_ids",
        "audience_ids",
        "evidence_ids",
        "assumptions",
    ):
        _text_list(event[field], f"event {field}", field == "assumptions")
    if not isinstance(event["uncertainty"], dict):
        raise ValueError("invalid_envelope: event uncertainty is invalid")


def _strings(item: dict[str, Any], fields: tuple[str, ...]) -> None:
    if any(not isinstance(item.get(field), str) or not item[field] for field in fields):
        raise ValueError("invalid_envelope: episode string is invalid")


def _text_list(value: Any, label: str, allow_empty: bool) -> None:
    if (
        not isinstance(value, list)
        or (not allow_empty and not value)
        or not all(isinstance(item, str) and item for item in value)
        or len(value) != len(set(value))
    ):
        raise ValueError(f"invalid_envelope: {label} are invalid")


def _hash(value: Any, label: str) -> None:
    if not (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    ):
        raise ValueError(f"invalid_envelope: {label} is invalid")


__all__ = ["validate_episode_values"]
