"""Immutable no-model proposal bridge artifacts."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ProposalBridgeFixture:
    fixture_id: str
    cycle_receipt_hash: str
    date_profile_hash: str
    content_hash: str
    _payload: dict[str, Any]
    _cycle_receipt: dict[str, Any]

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)

    def cycle_receipt(self) -> dict[str, Any]:
        return deepcopy(self._cycle_receipt)


@dataclass(frozen=True)
class ProposalBridgeRun:
    content_hash: str
    _receipt: dict[str, Any]
    _fixture: ProposalBridgeFixture

    def receipt(self) -> dict[str, Any]:
        return deepcopy(self._receipt)

    def fixture(self) -> ProposalBridgeFixture:
        return self._fixture


__all__ = ["ProposalBridgeFixture", "ProposalBridgeRun"]
