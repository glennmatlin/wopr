"""Seat and group graph compilation for counterpart Charters."""

from __future__ import annotations

from itertools import combinations
from typing import Any

from .counterpart_compiled_models import (
    CompiledCounterpartGroup,
    CompiledCounterpartSeat,
)


def compile_active_seats(payload: dict[str, Any]) -> dict[str, CompiledCounterpartSeat]:
    predicates = {
        item["activation_predicate_id"]: item["first_episode_value"]
        for item in payload["activation_predicates"]
    }
    seats: dict[str, CompiledCounterpartSeat] = {}
    for item in payload["institution_registry"]["seats"]:
        if any(predicates[value] for value in item["activation_predicate_ids"]):
            seat = CompiledCounterpartSeat(
                seat_id=item["seat_id"],
                participation_class=item["participation_class"],
            )
            seats[seat.seat_id] = seat
    return seats


def compile_active_groups(
    payload: dict[str, Any], seats: dict[str, CompiledCounterpartSeat]
) -> dict[str, CompiledCounterpartGroup]:
    predicates = {
        item["activation_predicate_id"]: item["first_episode_value"]
        for item in payload["activation_predicates"]
    }
    groups: dict[str, CompiledCounterpartGroup] = {}
    ordered = sorted(
        payload["groups"], key=lambda item: (item["collection_order"], item["group_id"])
    )
    for item in ordered:
        if predicates[item["activation_predicate_id"]]:
            group = CompiledCounterpartGroup(
                group_id=item["group_id"],
                members=tuple(
                    seats[value] for value in item["ordered_eligible_member_ids"]
                ),
                input_entitlement_ids=tuple(item["input_entitlement_ids"]),
                dependency_group_ids=tuple(item["dependency_group_ids"]),
                shared_seat_barrier_ids=tuple(item["shared_seat_barrier_ids"]),
                product_schema_id=item["product_schema_id"],
                collection_order=item["collection_order"],
                failure_effect=item["failure_effect"],
            )
            groups[group.group_id] = group
    return groups


def dependency_closure(
    groups: dict[str, CompiledCounterpartGroup],
) -> dict[str, frozenset[str]]:
    direct = {
        group_id: set(group.dependency_group_ids) for group_id, group in groups.items()
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


def shared_seat_barriers(
    groups: dict[str, CompiledCounterpartGroup],
) -> dict[tuple[str, str], tuple[str, ...]]:
    barriers: dict[tuple[str, str], tuple[str, ...]] = {}
    for first, second in combinations(groups, 2):
        first_ids = {seat.seat_id for seat in groups[first].members}
        second_ids = {seat.seat_id for seat in groups[second].members}
        shared = tuple(sorted(first_ids & second_ids))
        if shared:
            key = (first, second) if first <= second else (second, first)
            barriers[key] = shared
    return barriers


__all__ = [
    "compile_active_groups",
    "compile_active_seats",
    "dependency_closure",
    "shared_seat_barriers",
]
