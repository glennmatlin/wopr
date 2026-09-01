"""Typed identity and reference checks for the first DATE Core."""

from __future__ import annotations

from typing import Any

from .operations import AFFORDANCE_VALUES, READINESS_VALUES

RECORD_FIELDS = {
    "actors": {"actor_id", "name"},
    "locations": {"location_id", "kind", "controller_actor_id"},
    "activities": {"activity_id", "owner_actor_id", "kind"},
    "force_packages": {
        "force_package_id",
        "owner_actor_id",
        "function",
        "location_id",
        "posture",
        "readiness",
    },
    "affordances": {
        "affordance_id",
        "controller_actor_id",
        "beneficiary_actor_id",
        "dependency_id",
        "state",
    },
    "authorizations": {"authorization_id", "actor_id", "state"},
    "commitments": {"commitment_id", "actor_id", "state"},
    "clocks": {"clock_id", "due_hour", "state"},
}
IDENTITY_FIELDS = {
    "actors": "actor_id",
    "locations": "location_id",
    "activities": "activity_id",
    "force_packages": "force_package_id",
    "affordances": "affordance_id",
    "authorizations": "authorization_id",
    "commitments": "commitment_id",
    "clocks": "clock_id",
}


def core_entity_ids(core: dict[str, Any]) -> set[str]:
    return {
        record[IDENTITY_FIELDS[collection]]
        for collection in IDENTITY_FIELDS
        for record in core[collection]
    }


def _validate_record_fields(core: dict[str, Any]) -> None:
    for collection, fields in RECORD_FIELDS.items():
        for record in core[collection]:
            if set(record) != fields:
                raise ValueError(f"DATE Core {collection} record fields are invalid")
            for field, value in record.items():
                if field == "due_hour":
                    if isinstance(value, bool) or not isinstance(value, int):
                        raise ValueError("DATE Core clock due_hour is invalid")
                elif not isinstance(value, str) or not value:
                    raise ValueError(f"DATE Core {collection} record value is invalid")


def _validate_references(core: dict[str, Any]) -> None:
    actor_ids = {record["actor_id"] for record in core["actors"]}
    location_ids = {record["location_id"] for record in core["locations"]}
    dependency_ids = {
        *[record["activity_id"] for record in core["activities"]],
        *[record["force_package_id"] for record in core["force_packages"]],
    }
    actor_refs = [
        *[record["controller_actor_id"] for record in core["locations"]],
        *[record["owner_actor_id"] for record in core["activities"]],
        *[record["owner_actor_id"] for record in core["force_packages"]],
        *[record["controller_actor_id"] for record in core["affordances"]],
        *[record["beneficiary_actor_id"] for record in core["affordances"]],
        *[record["actor_id"] for record in core["authorizations"]],
        *[record["actor_id"] for record in core["commitments"]],
    ]
    if not set(actor_refs) <= actor_ids:
        raise ValueError("DATE Core actor has unknown_reference")
    if not {record["location_id"] for record in core["force_packages"]} <= location_ids:
        raise ValueError("DATE Core location has unknown_reference")
    if (
        not {record["dependency_id"] for record in core["affordances"]}
        <= dependency_ids
    ):
        raise ValueError("DATE Core dependency has unknown_reference")


def validate_core_records(core: dict[str, Any]) -> None:
    _validate_record_fields(core)
    ground_truth = core.get("ground_truth")
    expected_truth = {
        "olvana_seizure_authority",
        "olvana_objective",
        "olvana_general_war_expectation",
    }
    if not isinstance(ground_truth, dict) or set(ground_truth) != expected_truth:
        raise ValueError("DATE Core ground_truth fields are invalid")
    if any(not isinstance(value, str) or not value for value in ground_truth.values()):
        raise ValueError("DATE Core ground_truth value is invalid")
    states = (core["escalation_state"], core["terminal_state"])
    if any(not isinstance(state, str) or not state for state in states):
        raise ValueError("DATE Core state is invalid")
    if not {item["readiness"] for item in core["force_packages"]} <= READINESS_VALUES:
        raise ValueError("DATE Core force-package readiness is invalid")
    if not {item["state"] for item in core["affordances"]} <= AFFORDANCE_VALUES:
        raise ValueError("DATE Core affordance state is invalid")
    _validate_references(core)


__all__ = ["IDENTITY_FIELDS", "core_entity_ids", "validate_core_records"]
