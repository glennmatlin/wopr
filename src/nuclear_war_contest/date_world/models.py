"""Immutable DATE World transition models."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ValidationReceipt:
    receipt_id: str
    run_id: str
    accepted: bool
    reason_codes: tuple[str, ...]
    event_template_id: str
    event_template_hash: str
    patch_instance_id: str | None
    core_version_before: int
    core_version_after: int
    core_hash_before: str
    core_hash_after: str


@dataclass(frozen=True)
class PatchInstance:
    patch_instance_id: str
    run_id: str
    template_id: str
    template_hash: str
    base_core_version: int
    base_core_hash: str
    _template: dict[str, Any]

    def template(self) -> dict[str, Any]:
        return deepcopy(self._template)


@dataclass(frozen=True)
class DateRun:
    run_id: str
    profile_hash: str
    _initial_core: dict[str, Any]
    _current_core: dict[str, Any]
    _ledger: tuple[dict[str, Any], ...] = ()
    _receipts: tuple[ValidationReceipt, ...] = ()
    _accepted_transitions: tuple[dict[str, Any], ...] = ()

    def initial_core(self) -> dict[str, Any]:
        return deepcopy(self._initial_core)

    def current_core(self) -> dict[str, Any]:
        return deepcopy(self._current_core)

    def ledger(self) -> tuple[dict[str, Any], ...]:
        return deepcopy(self._ledger)

    def receipts(self) -> tuple[ValidationReceipt, ...]:
        return self._receipts

    def accepted_transitions(self) -> tuple[dict[str, Any], ...]:
        return deepcopy(self._accepted_transitions)


@dataclass(frozen=True)
class TransitionResult:
    run: DateRun
    receipt: ValidationReceipt


__all__ = ["DateRun", "PatchInstance", "TransitionResult", "ValidationReceipt"]
