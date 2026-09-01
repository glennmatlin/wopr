"""Closed semantic operations for DATE State Patches."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

READINESS_VALUES = {"active", "prepared", "ready", "delayed"}
AFFORDANCE_VALUES = {"available", "intermittent", "restricted"}


@dataclass(frozen=True)
class AdmissionError(Exception):
    reason_code: str


def _replace_state(
    core: dict[str, Any],
    operation: dict[str, Any],
    collection: str,
    identity_field: str,
    identity_key: str,
    allowed_values: set[str],
) -> None:
    expected_fields = {"operation", identity_key, "expected", "value"}
    if set(operation) != expected_fields:
        raise AdmissionError("forbidden_write")
    identity = operation[identity_key]
    records = core[collection]
    matches = [record for record in records if record[identity_field] == identity]
    if len(matches) != 1:
        raise AdmissionError("unknown_reference")
    value = operation["value"]
    expected = operation["expected"]
    if not isinstance(value, str) or value not in allowed_values:
        raise AdmissionError("invalid_value")
    if not isinstance(expected, str) or expected not in allowed_values:
        raise AdmissionError("invalid_value")
    field = "readiness" if collection == "force_packages" else "state"
    if matches[0][field] != expected:
        raise AdmissionError("failed_precondition")
    matches[0][field] = value


def apply_operations(
    current_core: dict[str, Any], operations: object
) -> dict[str, Any]:
    if not isinstance(operations, list) or not operations:
        raise AdmissionError("partial_patch")
    next_core = deepcopy(current_core)
    for operation in operations:
        if not isinstance(operation, dict):
            raise AdmissionError("invalid_envelope")
        kind = operation.get("operation")
        if kind == "set_force_package_readiness":
            _replace_state(
                next_core,
                operation,
                "force_packages",
                "force_package_id",
                "force_package_id",
                READINESS_VALUES,
            )
        elif kind == "set_affordance_state":
            _replace_state(
                next_core,
                operation,
                "affordances",
                "affordance_id",
                "affordance_id",
                AFFORDANCE_VALUES,
            )
        else:
            raise AdmissionError("undeclared_operation")
    next_core["core_version"] += 1
    return next_core


__all__ = ["AdmissionError", "apply_operations"]
