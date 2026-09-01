"""Fail-closed DATE candidate-profile shape validation."""

from __future__ import annotations

from typing import Any

from .core_validation import IDENTITY_FIELDS, validate_core_records
from .profile_metadata_validation import validate_profile_metadata
from .profile_template_validation import validate_authored_templates
from .projections import project_outcomes

PROFILE_FIELDS = {
    "schema_version",
    "profile_id",
    "profile_version",
    "setup_id",
    "setup_family",
    "seed_id",
    "status",
    "episode",
    "road_to_war",
    "initial_core",
    "partner_request",
    "escalation_ladder",
    "audience_ids",
    "evidence_ids",
    "terminal_policy",
    "authored_event_templates",
    "patch_templates",
    "risk_probe_ids",
    "outcome_projection_ids",
}
CORE_FIELDS = {
    "schema_version",
    "core_version",
    "actors",
    "locations",
    "activities",
    "force_packages",
    "affordances",
    "ground_truth",
    "authorizations",
    "commitments",
    "clocks",
    "escalation_state",
    "terminal_state",
    "outcome_projections",
}


def _require_text(payload: dict[str, Any], field: str) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value:
        raise ValueError(f"DATE profile {field} is invalid")
    return value


def _require_text_list(payload: dict[str, Any], field: str) -> list[str]:
    value = payload.get(field)
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item for item in value
    ):
        raise ValueError(f"DATE profile {field} is invalid")
    if len(value) != len(set(value)):
        raise ValueError(f"DATE profile {field} has duplicate_id")
    return value


def _validate_unique_records(core: dict[str, Any]) -> None:
    all_identities: list[object] = []
    for collection, identity_field in IDENTITY_FIELDS.items():
        records = core.get(collection)
        if not isinstance(records, list) or any(
            not isinstance(record, dict) for record in records
        ):
            raise ValueError(f"DATE Core {collection} is invalid")
        identities = [record.get(identity_field) for record in records]
        if any(
            not isinstance(identity, str) or not identity for identity in identities
        ):
            raise ValueError(f"DATE Core {collection} identity is invalid")
        if len(identities) != len(set(identities)):
            raise ValueError(f"DATE Core {collection} has duplicate_id")
        all_identities.extend(identities)
    if len(all_identities) != len(set(all_identities)):
        raise ValueError("DATE Core entity namespace has duplicate_id")


def _validate_core(payload: dict[str, Any]) -> None:
    core = payload.get("initial_core")
    if not isinstance(core, dict) or set(core) != CORE_FIELDS:
        raise ValueError("DATE Core fields are invalid")
    if core.get("schema_version") != "date-core.v0.2":
        raise ValueError("DATE Core schema_version is invalid")
    version = core.get("core_version")
    if isinstance(version, bool) or not isinstance(version, int) or version != 0:
        raise ValueError("DATE Core core_version is invalid")
    _validate_unique_records(core)
    validate_core_records(core)
    projections = core.get("outcome_projections")
    if not isinstance(projections, dict) or any(
        not isinstance(key, str) or not key for key in projections
    ):
        raise ValueError("DATE Core outcome projections are invalid")
    declared = _require_text_list(payload, "outcome_projection_ids")
    if list(projections) != declared:
        raise ValueError("DATE outcome projection IDs do not match")
    project_outcomes(core)


def validate_profile(payload: dict[str, Any]) -> None:
    if set(payload) != PROFILE_FIELDS:
        raise ValueError("DATE profile fields are invalid")
    if payload.get("schema_version") != "date-profile.v0.2":
        raise ValueError("DATE profile schema_version is invalid")
    for field in (
        "profile_id",
        "profile_version",
        "setup_id",
        "setup_family",
        "seed_id",
    ):
        _require_text(payload, field)
    for field in ("audience_ids", "evidence_ids", "risk_probe_ids"):
        _require_text_list(payload, field)
    _validate_core(payload)
    validate_profile_metadata(payload)
    validate_authored_templates(payload)


__all__ = ["validate_profile"]
