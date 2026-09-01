"""Authored DATE State Patch template shape validation."""

from __future__ import annotations

from typing import Any

from .operations import AFFORDANCE_VALUES, READINESS_VALUES

PATCH_FIELDS = {"template_id", "effective_hour", "causal_parent_ids", "operations"}


def _text_list(value: object) -> bool:
    return isinstance(value, list) and all(
        isinstance(item, str) and item for item in value
    )


def _validate_operation(operation: object, core: dict[str, Any]) -> None:
    if not isinstance(operation, dict):
        raise ValueError("DATE patch operation is invalid")
    kind = operation.get("operation")
    if kind == "set_force_package_readiness":
        target_key = "force_package_id"
        targets = {item[target_key] for item in core["force_packages"]}
        allowed = READINESS_VALUES
    elif kind == "set_affordance_state":
        target_key = "affordance_id"
        targets = {item[target_key] for item in core["affordances"]}
        allowed = AFFORDANCE_VALUES
    else:
        raise ValueError("DATE patch has undeclared_operation")
    if set(operation) != {"operation", target_key, "expected", "value"}:
        raise ValueError("DATE patch operation fields are invalid")
    if operation[target_key] not in targets:
        raise ValueError("DATE patch operation has unknown_reference")
    if operation["expected"] not in allowed or operation["value"] not in allowed:
        raise ValueError("DATE patch operation value is invalid")


def validate_patch_templates(
    patches: list[dict[str, Any]], core: dict[str, Any]
) -> None:
    for patch in patches:
        if set(patch) != PATCH_FIELDS:
            raise ValueError("DATE patch template fields are invalid")
        hour = patch["effective_hour"]
        if isinstance(hour, bool) or not isinstance(hour, int):
            raise ValueError("DATE patch template effective_hour is invalid")
        parents = patch["causal_parent_ids"]
        if not _text_list(parents) or len(parents) != len(set(parents)):
            raise ValueError("DATE patch template causal parents are invalid")
        operations = patch["operations"]
        if not isinstance(operations, list) or not operations:
            raise ValueError("DATE patch template operations are invalid")
        for operation in operations:
            _validate_operation(operation, core)


__all__ = ["validate_patch_templates"]
