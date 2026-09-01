"""Authored DATE event and patch template validation."""

from __future__ import annotations

from typing import Any

from .core_validation import core_entity_ids
from .profile_patch_template_validation import validate_patch_templates

EVENT_FIELDS = {
    "template_id",
    "event_kind",
    "episode_hour",
    "causal_parent_ids",
    "source",
    "affected_entity_ids",
    "audience_ids",
    "evidence_ids",
    "assumptions",
    "uncertainty",
    "content",
    "patch_template_id",
}


def _text_list(value: object) -> bool:
    return isinstance(value, list) and all(
        isinstance(item, str) and item for item in value
    )


def _unique_templates(templates: object, label: str) -> list[dict[str, Any]]:
    if not isinstance(templates, list) or any(
        not isinstance(item, dict) for item in templates
    ):
        raise ValueError(f"DATE {label} templates are invalid")
    identities = [item.get("template_id") for item in templates]
    if any(not isinstance(item, str) or not item for item in identities):
        raise ValueError(f"DATE {label} template identity is invalid")
    if len(identities) != len(set(identities)):
        raise ValueError(f"DATE {label} templates have duplicate_id")
    return templates


def _validate_event_shape(event: dict[str, Any]) -> None:
    if set(event) != EVENT_FIELDS:
        raise ValueError("DATE event template fields are invalid")
    for field in ("template_id", "event_kind", "source", "content"):
        if not isinstance(event[field], str) or not event[field]:
            raise ValueError(f"DATE event template {field} is invalid")
    hour = event["episode_hour"]
    if isinstance(hour, bool) or not isinstance(hour, int):
        raise ValueError("DATE event template episode_hour is invalid")
    if event["source"] != "authored_msel":
        raise ValueError("DATE event template source is invalid")
    for field in (
        "causal_parent_ids",
        "affected_entity_ids",
        "audience_ids",
        "evidence_ids",
        "assumptions",
    ):
        if not _text_list(event[field]) or len(event[field]) != len(set(event[field])):
            raise ValueError(f"DATE event template {field} is invalid")
    if not isinstance(event["uncertainty"], dict):
        raise ValueError("DATE event template uncertainty is invalid")
    uncertainty = event["uncertainty"]
    allowed_uncertainty = {"confidence", "earliest_hour", "latest_hour", "through_hour"}
    if "confidence" not in uncertainty or not set(uncertainty) <= allowed_uncertainty:
        raise ValueError("DATE event template uncertainty fields are invalid")
    if not isinstance(uncertainty["confidence"], str) or not uncertainty["confidence"]:
        raise ValueError("DATE event template uncertainty confidence is invalid")
    for field in set(uncertainty) - {"confidence"}:
        if isinstance(uncertainty[field], bool) or not isinstance(
            uncertainty[field], int
        ):
            raise ValueError("DATE event template uncertainty hour is invalid")
    patch_id = event["patch_template_id"]
    if patch_id is not None and (not isinstance(patch_id, str) or not patch_id):
        raise ValueError("DATE event template patch identity is invalid")


def validate_authored_templates(payload: dict[str, Any]) -> None:
    core = payload["initial_core"]
    events = _unique_templates(payload["authored_event_templates"], "event")
    patches = _unique_templates(payload["patch_templates"], "patch")
    for event in events:
        _validate_event_shape(event)
    validate_patch_templates(patches, core)
    event_by_id = {item["template_id"]: item for item in events}
    event_positions = {item["template_id"]: index for index, item in enumerate(events)}
    patch_by_id = {item["template_id"]: item for item in patches}
    entities = core_entity_ids(core)
    for event in events:
        if not set(event["affected_entity_ids"]) <= entities:
            raise ValueError("DATE event template has unknown_reference")
        if not set(event["audience_ids"]) <= set(payload["audience_ids"]):
            raise ValueError("DATE event audience has unknown_reference")
        if not set(event["evidence_ids"]) <= set(payload["evidence_ids"]):
            raise ValueError("DATE event evidence has unknown_reference")
        if not set(event["causal_parent_ids"]) <= set(event_by_id):
            raise ValueError("DATE event causal parent has unknown_reference")
        if any(
            event_positions[parent] >= event_positions[event["template_id"]]
            for parent in event["causal_parent_ids"]
        ):
            raise ValueError("DATE event causal parent is not prior")
        if any(
            event_by_id[parent]["episode_hour"] > event["episode_hour"]
            for parent in event["causal_parent_ids"]
        ):
            raise ValueError("DATE event causal parent is retroactive")
        patch_id = event["patch_template_id"]
        if patch_id is not None and patch_id not in patch_by_id:
            raise ValueError("DATE event patch has unknown_reference")
        if patch_id is not None:
            patch = patch_by_id[patch_id]
            if patch["effective_hour"] != event["episode_hour"]:
                raise ValueError("DATE event patch time does not match")
            if event["template_id"] not in patch["causal_parent_ids"]:
                raise ValueError("DATE event patch causal parent does not match")
    for patch in patches:
        if not set(patch["causal_parent_ids"]) <= set(event_by_id):
            raise ValueError("DATE patch causal parent has unknown_reference")


__all__ = ["validate_authored_templates"]
