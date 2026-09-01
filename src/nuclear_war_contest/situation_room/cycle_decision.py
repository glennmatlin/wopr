"""Deterministic U.S. decision routing and record confirmation."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from .charter import UsCharter
from .cycle_fixture import UsCycleFixture


@dataclass(frozen=True)
class CycleDecision:
    policy_package: dict[str, Any] | None
    route: dict[str, Any] | None
    record: dict[str, Any] | None
    confirmations: list[dict[str, Any]]
    failures: list[dict[str, Any]]
    supported: bool


def resolve_cycle_decision(
    charter: UsCharter,
    fixture: UsCycleFixture,
    attempts: list[dict[str, Any]],
    product_failures: list[dict[str, Any]],
) -> CycleDecision:
    payload = fixture.payload()
    route = _decision_route(charter, payload["action_class"])
    by_group = {
        item["group_id"]: item for item in attempts if item["status"] == "accepted"
    }
    package = by_group.get("GROUP_PC")
    record = by_group.get(route["eligible_forum_group_id"])
    if product_failures or package is None or record is None:
        return CycleDecision(package, None, record, [], [], False)
    route_view = {
        "route_id": route["route_id"],
        "action_class": route["action_class"],
        "owning_authority_seat_id": route["owning_authority_seat_id"],
        "eligible_forum_group_id": route["eligible_forum_group_id"],
        "consultation_group_ids": route["consultation_group_ids"],
        "required_confirmation_ids": route["required_confirmation_ids"],
    }
    failures = _route_failures(route, package, record)
    confirmations, confirmation_failures = _confirmations(
        charter, payload, route, record
    )
    failures.extend(confirmation_failures)
    return CycleDecision(
        package,
        route_view,
        record,
        confirmations,
        failures,
        not failures,
    )


def _decision_route(charter: UsCharter, action_class: str) -> dict[str, Any]:
    matches = [
        item
        for item in charter.payload()["decision_routes"]
        if item["action_class"] == action_class
    ]
    if len(matches) != 1:
        raise ValueError("route_mismatch: cycle action class is unresolved")
    return matches[0]


def _route_failures(
    route: dict[str, Any],
    package: dict[str, Any],
    record: dict[str, Any],
) -> list[dict[str, Any]]:
    content = record["content"]
    valid = (
        content.get("route_id") == route["route_id"]
        and content.get("policy_package_id") == package["product_id"]
        and content.get("consultations") == route["consultation_group_ids"]
        and content.get("required_confirmations") == route["required_confirmation_ids"]
    )
    if valid:
        return []
    return [
        {
            "failure_id": f"FAILURE::{route['route_id']}",
            "reason_code": "route_mismatch",
            "group_id": route["eligible_forum_group_id"],
        }
    ]


def _confirmations(
    charter: UsCharter,
    fixture: dict[str, Any],
    route: dict[str, Any],
    record: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    specs = {
        item["confirmation_id"]: item
        for item in charter.payload()["required_confirmations"]
    }
    provided = {item["confirmation_id"]: item for item in fixture["confirmations"]}
    retained: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for confirmation_id in route["required_confirmation_ids"]:
        item = provided.get(confirmation_id)
        if item is None:
            failures.append(
                _confirmation_failure(confirmation_id, "missing_confirmation")
            )
            continue
        spec = specs[confirmation_id]
        valid = (
            item.get("status") == "confirmed"
            and item.get("confirmer_seat_ids") == spec["confirmer_seat_ids"]
            and item.get("confirmed_record_id") == record["product_id"]
        )
        if not valid:
            failures.append(
                _confirmation_failure(confirmation_id, "invalid_confirmation")
            )
        retained.append(deepcopy(item))
    return retained, failures


def _confirmation_failure(confirmation_id: str, reason: str) -> dict[str, Any]:
    return {
        "failure_id": f"FAILURE::{confirmation_id}",
        "reason_code": reason,
        "confirmation_id": confirmation_id,
        "group_id": "GROUP_NSC",
    }


__all__ = ["CycleDecision", "resolve_cycle_decision"]
