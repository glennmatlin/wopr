"""Read-only DATE outcome projections."""

from __future__ import annotations

from typing import Any


def _record_value(
    core: dict[str, Any],
    collection: str,
    identity_field: str,
    identity: object,
    value_field: str,
) -> object:
    records = core.get(collection)
    if not isinstance(records, list) or not isinstance(identity, str):
        raise ValueError("Outcome projection target is invalid")
    matches = [record for record in records if record.get(identity_field) == identity]
    if len(matches) != 1 or value_field not in matches[0]:
        raise ValueError("Outcome projection target is unresolved")
    return matches[0][value_field]


def _project_selector(core: dict[str, Any], selector: dict[str, Any]) -> object:
    kind = selector.get("selector")
    if kind == "location_control":
        _validate_selector_fields(selector, {"selector", "location_id"})
        return _record_value(
            core,
            "locations",
            "location_id",
            selector.get("location_id"),
            "controller_actor_id",
        )
    if kind == "authorization_state":
        _validate_selector_fields(selector, {"selector", "authorization_id"})
        return _record_value(
            core,
            "authorizations",
            "authorization_id",
            selector.get("authorization_id"),
            "state",
        )
    if kind == "commitment_state":
        _validate_selector_fields(selector, {"selector", "commitment_id"})
        return _record_value(
            core,
            "commitments",
            "commitment_id",
            selector.get("commitment_id"),
            "state",
        )
    if kind == "affordance_state":
        _validate_selector_fields(selector, {"selector", "affordance_id"})
        return _record_value(
            core,
            "affordances",
            "affordance_id",
            selector.get("affordance_id"),
            "state",
        )
    if kind in {"escalation_state", "terminal_state"}:
        _validate_selector_fields(selector, {"selector"})
        if kind not in core:
            raise ValueError("Outcome projection target is unresolved")
        return core[kind]
    raise ValueError("Outcome projection selector is unknown")


def _validate_selector_fields(selector: dict[str, Any], expected: set[str]) -> None:
    if set(selector) != expected:
        raise ValueError("Outcome projection selector fields are invalid")


def project_outcomes(core: dict[str, Any]) -> dict[str, object]:
    projections = core.get("outcome_projections")
    if not isinstance(projections, dict):
        raise ValueError("Core outcome_projections is invalid")
    outcomes: dict[str, object] = {}
    for projection_id, selector in projections.items():
        if not isinstance(selector, dict):
            raise ValueError("Outcome projection selector is invalid")
        outcomes[projection_id] = _project_selector(core, selector)
    return outcomes


__all__ = ["project_outcomes"]
