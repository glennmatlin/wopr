"""Execution context and mutable cycle state for Room rehearsal."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .charter import UsCharter
from .compiled_models import CompiledUsCharter
from .cycle_fixture import UsCycleFixture
from .scripted_rehearsal_runtime import SeatRuntime


@dataclass(frozen=True)
class CycleContext:
    charter: UsCharter
    fixture: UsCycleFixture
    compiled: CompiledUsCharter
    groups: dict[str, dict[str, Any]]
    schemas: dict[str, dict[str, Any]]
    seats: dict[str, dict[str, Any]]
    runtimes: dict[str, SeatRuntime]
    product_contracts: dict[str, dict[str, Any]]


@dataclass(frozen=True)
class GroupContext:
    cycle_id: str
    group: dict[str, Any]
    schema: dict[str, Any]
    seats: dict[str, dict[str, Any]]
    compiled: CompiledUsCharter
    runtimes: dict[str, SeatRuntime]
    deliveries: list[dict[str, Any]]
    catalog: dict[str, dict[str, Any]]
    product_contract: dict[str, Any] | None


@dataclass
class CycleState:
    remaining: tuple[str, ...]
    initial_deliveries: list[dict[str, Any]]
    deliveries: list[dict[str, Any]]
    catalog: dict[str, dict[str, Any]]
    completed: set[str] = field(default_factory=set)
    schedule: list[list[str]] = field(default_factory=list)
    attempts: list[dict[str, Any]] = field(default_factory=list)
    products: list[dict[str, Any]] = field(default_factory=list)
    portfolio_traces: list[dict[str, Any]] = field(default_factory=list)
    group_traces: list[dict[str, Any]] = field(default_factory=list)
    failures: list[dict[str, Any]] = field(default_factory=list)


__all__ = ["CycleContext", "CycleState", "GroupContext"]
