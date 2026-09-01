"""Strict envelope validation for the two-cycle episode fixture."""

from __future__ import annotations

from typing import Any

from .episode_artifact_validation import validate_episode_artifacts
from .episode_value_validation import validate_episode_values

_FIELDS = frozenset(
    {
        "schema_version",
        "fixture_id",
        "fixture_version",
        "status",
        "artifact_paths",
        "artifact_hashes",
        "forecast_binding",
        "cycle2_external_parent_ids",
        "cycle2_reassessment",
        "final_adjudication",
        "upstream_receipt_hashes",
    }
)
_FORECAST_FIELDS = frozenset(
    {"cycle1_input_id", "world_event_id", "relationship", "shared_entity_ids"}
)
_REASSESSMENT_FIELDS = frozenset(
    {
        "prior_decision_id",
        "prior_decision_hash",
        "changed_evidence_ids",
        "core_version",
        "core_hash",
        "disposition",
    }
)
_ADJUDICATION_FIELDS = frozenset(
    {
        "adjudication_id",
        "cycle_id",
        "actor_id",
        "decision_record_id",
        "source_component_ids",
        "status",
        "original_language",
        "reason_codes",
        "adjudicator_id",
        "evidence_status",
        "represented_room_decision_actor_ids",
        "world_event",
    }
)
_EVENT_FIELDS = frozenset(
    {
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
)


def validate_episode_fixture_shape(payload: dict[str, Any]) -> None:
    if set(payload) != _FIELDS:
        raise ValueError("invalid_envelope: episode fixture fields are invalid")
    fixed = {
        "schema_version": "us-two-cycle-fixture.v0.1",
        "status": "development_fixture_non_evidence",
    }
    if any(payload.get(key) != value for key, value in fixed.items()):
        raise ValueError("invalid_envelope: episode fixed fields are invalid")
    _strings(payload, ("fixture_id", "fixture_version"))
    validate_episode_artifacts(payload)
    _record(payload["forecast_binding"], _FORECAST_FIELDS, "forecast binding")
    _record(payload["cycle2_reassessment"], _REASSESSMENT_FIELDS, "reassessment")
    _record(payload["final_adjudication"], _ADJUDICATION_FIELDS, "adjudication")
    _record(payload["final_adjudication"]["world_event"], _EVENT_FIELDS, "event")
    validate_episode_values(payload)
    _validate_adjudication(payload["final_adjudication"])


def _validate_adjudication(item: dict[str, Any]) -> None:
    _strings(
        item,
        (
            "adjudication_id",
            "cycle_id",
            "actor_id",
            "decision_record_id",
            "status",
            "original_language",
            "adjudicator_id",
            "evidence_status",
        ),
    )
    if (
        item["cycle_id"] != "CYCLE_2"
        or item["actor_id"] != "USA"
        or item["status"] != "recorded_non_action"
        or item["evidence_status"] != "development_fixture_non_evidence"
        or item["adjudicator_id"].startswith("SEAT_")
        or item["represented_room_decision_actor_ids"]
    ):
        raise ValueError("invalid_envelope: final adjudication boundary is invalid")
    event = item["world_event"]
    if (
        event["event_kind"] != "excon_consequence"
        or event["source"] != "excon_consequence"
        or event["patch_template_id"] is not None
    ):
        raise ValueError("invalid_envelope: final consequence boundary is invalid")


def _record(value: Any, fields: frozenset[str], label: str) -> None:
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"invalid_envelope: {label} fields are invalid")


def _strings(item: dict[str, Any], fields: tuple[str, ...]) -> None:
    if any(not isinstance(item.get(field), str) or not item[field] for field in fields):
        raise ValueError("invalid_envelope: episode string is invalid")


__all__ = ["validate_episode_fixture_shape"]
