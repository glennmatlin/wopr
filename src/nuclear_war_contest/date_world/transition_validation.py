"""Ordered fail-closed validation for DATE World transitions."""

from __future__ import annotations

from typing import Any

from .models import DateRun, PatchInstance
from .patch_validation import (
    validate_patch_envelope,
    validate_patch_identity,
    validate_patch_references,
)
from .profile import DateProfile

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


def _event_envelope(event: dict[str, Any]) -> str | None:
    if set(event) != EVENT_FIELDS:
        return "invalid_envelope"
    hour = event["episode_hour"]
    patch_id = event["patch_template_id"]
    scalar_fields = ("template_id", "event_kind", "source", "content")
    if any(
        not isinstance(event[field], str) or not event[field] for field in scalar_fields
    ):
        return "invalid_envelope"
    if isinstance(hour, bool) or not isinstance(hour, int):
        return "invalid_envelope"
    if patch_id is not None and (not isinstance(patch_id, str) or not patch_id):
        return "invalid_envelope"
    for field in (
        "causal_parent_ids",
        "affected_entity_ids",
        "audience_ids",
        "evidence_ids",
        "assumptions",
    ):
        if not _text_list(event[field]):
            return "invalid_envelope"
        if len(event[field]) != len(set(event[field])):
            return "duplicate_id"
    if not isinstance(event["uncertainty"], dict):
        return "invalid_envelope"
    if event["source"] not in {
        "authored_msel",
        "excon_consequence",
        "tracer_fixture",
    }:
        return "invalid_envelope"
    return None


def _event_references(
    profile: DateProfile, run: DateRun, event: dict[str, Any]
) -> str | None:
    if not set(event["affected_entity_ids"]) <= profile.entity_ids():
        return "unknown_reference"
    if not set(event["audience_ids"]) <= profile.declared_ids("audience_ids"):
        return "unknown_reference"
    if not set(event["evidence_ids"]) <= profile.declared_ids("evidence_ids"):
        return "unknown_reference"
    ledger_ids = {entry["template_id"] for entry in run.ledger()}
    if not set(event["causal_parent_ids"]) <= ledger_ids:
        return "causal_mismatch"
    return None


def _event_state(run: DateRun, event: dict[str, Any]) -> str | None:
    ledger = run.ledger()
    if event["template_id"] in {entry["template_id"] for entry in ledger}:
        return "duplicate_id"
    if ledger and event["episode_hour"] < ledger[-1]["episode_hour"]:
        return "retroactive_time"
    if run.current_core()["terminal_state"] != "open":
        return "terminal_world"
    return None


def _authored_event(profile: DateProfile, event: dict[str, Any]) -> str | None:
    try:
        authored = profile.event_template(event["template_id"])
    except ValueError:
        authored = None
    if event["source"] == "authored_msel" and event != authored:
        return "template_mismatch"
    if event["source"] != "authored_msel" and authored is not None:
        return "template_mismatch"
    return None


def validate_transition(
    profile: DateProfile,
    run: DateRun,
    event: dict[str, Any],
    patch: PatchInstance | None,
) -> str | None:
    if reason := _event_envelope(event):
        return reason
    if patch is not None and (reason := validate_patch_envelope(patch)):
        return reason
    if reason := _event_references(profile, run, event):
        return reason
    if patch is not None and (reason := validate_patch_references(run, event, patch)):
        return reason
    if reason := _event_state(run, event):
        return reason
    if reason := _authored_event(profile, event):
        return reason
    if patch is None:
        return "partial_patch" if event["patch_template_id"] is not None else None
    if event["patch_template_id"] is None:
        return "template_mismatch"
    return validate_patch_identity(profile, run, event, patch)


__all__ = ["validate_transition"]
