"""Immutable compiled views of a counterpart Room Charter."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompiledCounterpartSeat:
    seat_id: str
    participation_class: str


@dataclass(frozen=True)
class CompiledCounterpartGroup:
    group_id: str
    members: tuple[CompiledCounterpartSeat, ...]
    input_entitlement_ids: tuple[str, ...]
    dependency_group_ids: tuple[str, ...]
    shared_seat_barrier_ids: tuple[str, ...]
    product_schema_id: str
    collection_order: int
    failure_effect: str


@dataclass(frozen=True)
class CompiledCounterpartRoute:
    route_id: str
    action_class: str
    decision_authority_seat_ids: tuple[str, ...]
    decision_rule: str
    eligible_forum_group_id: str
    consultation_group_ids: tuple[str, ...]
    required_confirmation_ids: tuple[str, ...]
    final_decision_record_schema_id: str
    failure_effect: str


@dataclass(frozen=True)
class CompiledCounterpartConfirmation:
    confirmation_id: str
    requester_seat_ids: tuple[str, ...]
    confirmer_seat_ids: tuple[str, ...]
    applicability_action_classes: tuple[str, ...]
    failure_effect: str


@dataclass(frozen=True)
class CompiledCounterpartCharter:
    actor_id: str
    source_register_hash: str
    charter_hash: str
    _seats: dict[str, CompiledCounterpartSeat]
    _groups: dict[str, CompiledCounterpartGroup]
    _dependencies: dict[str, frozenset[str]]
    _barriers: dict[tuple[str, str], tuple[str, ...]]
    _recipients: dict[tuple[str, str], tuple[str, ...]]
    _routes: dict[str, CompiledCounterpartRoute]
    _confirmations: dict[str, CompiledCounterpartConfirmation]
    _blocked_gaps: dict[str, tuple[str, ...]]

    def seat(self, seat_id: str) -> CompiledCounterpartSeat:
        return self._seats[seat_id]

    def active_seat_ids(self) -> tuple[str, ...]:
        return tuple(self._seats)

    def active_group_ids(self) -> tuple[str, ...]:
        return tuple(self._groups)

    def group(self, group_id: str) -> CompiledCounterpartGroup:
        return self._groups[group_id]

    def group_members(self, group_id: str) -> tuple[CompiledCounterpartSeat, ...]:
        return self._groups[group_id].members

    def dependency_ids(self, group_id: str) -> frozenset[str]:
        return self._dependencies[group_id]

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

    def route_for(self, action_class: str) -> CompiledCounterpartRoute:
        return self._routes[action_class]

    def confirmation(self, confirmation_id: str) -> CompiledCounterpartConfirmation:
        return self._confirmations[confirmation_id]

    def blocked_gap_ids(self, action_class: str) -> tuple[str, ...]:
        return self._blocked_gaps.get(action_class, ())


__all__ = [
    "CompiledCounterpartCharter",
    "CompiledCounterpartConfirmation",
    "CompiledCounterpartGroup",
    "CompiledCounterpartRoute",
    "CompiledCounterpartSeat",
]
