"""Immutable compiled U.S. Room Charter views."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompiledSeat:
    seat_id: str
    adviser_status: str


@dataclass(frozen=True)
class CompiledUsCharter:
    charter_hash: str
    _seats: dict[str, CompiledSeat]
    _group_members: dict[str, tuple[CompiledSeat, ...]]
    _seat_groups: dict[str, tuple[str, ...]]
    _barriers: dict[tuple[str, str], tuple[str, ...]]
    _dependencies: dict[str, frozenset[str]]
    _recipients: dict[tuple[str, str], tuple[str, ...]]
    _routes: dict[str, str]

    def seat(self, seat_id: str) -> CompiledSeat:
        return self._seats[seat_id]

    def active_seat_ids(self) -> tuple[str, ...]:
        return tuple(self._seats)

    def active_group_ids(self) -> tuple[str, ...]:
        return tuple(self._group_members)

    def dependency_ids(self, group_id: str) -> frozenset[str]:
        return self._dependencies[group_id]

    def group_members(self, group_id: str) -> tuple[CompiledSeat, ...]:
        return self._group_members[group_id]

    def seat_groups(self, seat_id: str) -> tuple[str, ...]:
        return self._seat_groups[seat_id]

    def voting_member_ids(self, group_id: str) -> tuple[str, ...]:
        return tuple(
            seat.seat_id
            for seat in self._group_members[group_id]
            if seat.adviser_status == "voting_principal"
        )

    def barrier_seat_ids(self, first: str, second: str) -> tuple[str, ...]:
        key = (first, second) if first <= second else (second, first)
        return self._barriers.get(key, ())

    def can_run_concurrently(self, first: str, second: str) -> bool:
        if first == second or self.barrier_seat_ids(first, second):
            return False
        return (
            first not in self._dependencies[second]
            and second not in self._dependencies[first]
        )

    def recipients_for(
        self, information_class_id: str, sender_id: str
    ) -> tuple[str, ...]:
        return self._recipients.get((information_class_id, sender_id), ())

    def route_id_for(self, action_class: str) -> str:
        return self._routes[action_class]


__all__ = ["CompiledSeat", "CompiledUsCharter"]
