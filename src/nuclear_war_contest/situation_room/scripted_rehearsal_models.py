"""Immutable scripted Room rehearsal artifacts."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from .episode_models import TwoCycleFixture


@dataclass(frozen=True)
class GroupRehearsal:
    group_id: str
    product: dict[str, Any] | None
    portfolio_traces: list[dict[str, Any]]
    group_trace: dict[str, Any] | None
    failures: list[dict[str, Any]]


@dataclass(frozen=True)
class CycleRehearsal:
    cycle_id: str
    schedule: list[list[str]]
    products: list[dict[str, Any]]
    confirmations: list[dict[str, Any]]
    portfolio_traces: list[dict[str, Any]]
    group_traces: list[dict[str, Any]]
    confirmation_traces: list[dict[str, Any]]
    failures: list[dict[str, Any]]


@dataclass(frozen=True)
class ScriptedRehearsalRun:
    content_hash: str
    _receipt: dict[str, Any]
    _fixture: TwoCycleFixture

    def receipt(self) -> dict[str, Any]:
        return deepcopy(self._receipt)

    def fixture(self) -> TwoCycleFixture:
        return self._fixture


__all__ = ["CycleRehearsal", "GroupRehearsal", "ScriptedRehearsalRun"]
