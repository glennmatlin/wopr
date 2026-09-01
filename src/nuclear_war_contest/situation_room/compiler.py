"""Deterministic compilation of validated U.S. Room Charters."""

from __future__ import annotations

from itertools import combinations
from typing import Any

from .charter import UsCharter
from .compiled_models import CompiledSeat, CompiledUsCharter


def _active_seats(payload: dict[str, Any]) -> dict[str, CompiledSeat]:
    predicate_values = {
        item["activation_predicate_id"]: item["first_episode_value"]
        for item in payload["activation_predicates"]
    }
    seats: dict[str, CompiledSeat] = {}
    for item in payload["institution_registry"]["seats"]:
        if any(predicate_values[value] for value in item["activation_predicate_ids"]):
            seat = CompiledSeat(item["seat_id"], item["adviser_status"])
            seats[seat.seat_id] = seat
    return seats


def _active_groups(
    payload: dict[str, Any], seats: dict[str, CompiledSeat]
) -> dict[str, tuple[CompiledSeat, ...]]:
    predicate_values = {
        item["activation_predicate_id"]: item["first_episode_value"]
        for item in payload["activation_predicates"]
    }
    groups: dict[str, tuple[CompiledSeat, ...]] = {}
    ordered = sorted(
        payload["groups"], key=lambda item: (item["collection_order"], item["group_id"])
    )
    for item in ordered:
        if predicate_values[item["activation_predicate_id"]]:
            groups[item["group_id"]] = tuple(
                seats[seat_id]
                for seat_id in item["ordered_eligible_member_ids"]
                if seat_id in seats
            )
    return groups


def _dependency_closure(payload: dict[str, Any]) -> dict[str, frozenset[str]]:
    direct = {
        item["group_id"]: set(item["dependency_group_ids"])
        for item in payload["groups"]
    }
    closure: dict[str, frozenset[str]] = {}
    for group_id in direct:
        found: set[str] = set()
        pending = list(direct[group_id])
        while pending:
            dependency = pending.pop()
            if dependency not in found:
                found.add(dependency)
                pending.extend(direct[dependency])
        closure[group_id] = frozenset(found)
    return closure


def _barriers(
    groups: dict[str, tuple[CompiledSeat, ...]],
) -> dict[tuple[str, str], tuple[str, ...]]:
    barriers: dict[tuple[str, str], tuple[str, ...]] = {}
    for first, second in combinations(groups, 2):
        first_ids = {seat.seat_id for seat in groups[first]}
        second_ids = {seat.seat_id for seat in groups[second]}
        shared = tuple(sorted(first_ids & second_ids))
        if shared:
            key = (first, second) if first <= second else (second, first)
            barriers[key] = shared
    return barriers


def _recipients(
    payload: dict[str, Any],
    seats: dict[str, CompiledSeat],
    groups: dict[str, tuple[CompiledSeat, ...]],
) -> dict[tuple[str, str], tuple[str, ...]]:
    recipients_by_key: dict[tuple[str, str], set[str]] = {}
    for permission in payload["disclosure_permissions"]:
        recipients: set[str] = set()
        for recipient_id in permission["recipient_ids"]:
            if recipient_id in groups:
                recipients.update(seat.seat_id for seat in groups[recipient_id])
            elif recipient_id in seats:
                recipients.add(recipient_id)
        for sender_id in permission["sender_ids"]:
            key = (permission["information_class_id"], sender_id)
            recipients_by_key.setdefault(key, set()).update(recipients)
    return {
        key: tuple(sorted(recipients)) for key, recipients in recipients_by_key.items()
    }


def compile_us_charter(charter: UsCharter) -> CompiledUsCharter:
    payload = charter.payload()
    seats = _active_seats(payload)
    groups = _active_groups(payload, seats)
    declared_seats = payload["institution_registry"]["seats"]
    seat_groups = {
        item["seat_id"]: tuple(
            group_id for group_id in item["group_ids"] if group_id in groups
        )
        for item in declared_seats
        if item["seat_id"] in seats
    }
    routes = {
        item["action_class"]: item["route_id"] for item in payload["decision_routes"]
    }
    return CompiledUsCharter(
        charter_hash=charter.content_hash,
        _seats=seats,
        _group_members=groups,
        _seat_groups=seat_groups,
        _barriers=_barriers(groups),
        _dependencies=_dependency_closure(payload),
        _recipients=_recipients(payload, seats, groups),
        _routes=routes,
    )


__all__ = ["compile_us_charter"]
