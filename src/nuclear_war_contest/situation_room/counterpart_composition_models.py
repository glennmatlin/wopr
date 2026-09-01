"""Immutable artifacts for counterpart Room composition."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from .episode_models import TwoCycleFixture


@dataclass(frozen=True)
class CounterpartCompositionFixture:
    fixture_id: str
    content_hash: str
    two_cycle: TwoCycleFixture
    _payload: dict[str, Any]
    _receipts: dict[str, dict[str, Any]]
    _counterparts: tuple[dict[str, Any], ...]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)

    def receipts(self) -> dict[str, dict[str, Any]]:
        return deepcopy(self._receipts)

    def counterparts(self) -> list[dict[str, Any]]:
        return deepcopy(list(self._counterparts))

    def two_cycle_fixture(self) -> TwoCycleFixture:
        return self.two_cycle


@dataclass(frozen=True)
class CounterpartCompositionRun:
    content_hash: str
    _receipt: dict[str, Any]
    _fixture: CounterpartCompositionFixture

    def receipt(self) -> dict[str, Any]:
        return deepcopy(self._receipt)

    def fixture(self) -> CounterpartCompositionFixture:
        return self._fixture


__all__ = ["CounterpartCompositionFixture", "CounterpartCompositionRun"]
