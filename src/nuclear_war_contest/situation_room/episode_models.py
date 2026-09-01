"""Immutable deterministic two-cycle episode artifacts."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from nuclear_war_contest.date_world.profile import DateProfile

from .charter import UsCharter
from .cycle_fixture import UsCycleFixture
from .proposal_bridge_models import ProposalBridgeFixture
from .source_register import SourceRegister


@dataclass(frozen=True)
class TwoCycleFixture:
    fixture_id: str
    content_hash: str
    source: SourceRegister
    charter: UsCharter
    cycle1: UsCycleFixture
    bridge: ProposalBridgeFixture
    profile_value: DateProfile
    cycle2: UsCycleFixture
    _payload: dict[str, Any]
    _receipts: dict[str, dict[str, Any]]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)

    def receipts(self) -> dict[str, dict[str, Any]]:
        return deepcopy(self._receipts)

    def cycle1_fixture(self) -> UsCycleFixture:
        return self.cycle1

    def cycle2_fixture(self) -> UsCycleFixture:
        return self.cycle2

    def bridge_fixture(self) -> ProposalBridgeFixture:
        return self.bridge

    def profile(self) -> DateProfile:
        return self.profile_value


@dataclass(frozen=True)
class TwoCycleRun:
    content_hash: str
    _receipt: dict[str, Any]
    _fixture: TwoCycleFixture

    def receipt(self) -> dict[str, Any]:
        return deepcopy(self._receipt)

    def fixture(self) -> TwoCycleFixture:
        return self._fixture


__all__ = ["TwoCycleFixture", "TwoCycleRun"]
