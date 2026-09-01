"""Decision result model for counterpart Room traces."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class CounterpartDecision:
    route: dict[str, Any] | None
    record: dict[str, Any] | None
    confirmations: list[dict[str, Any]]
    projection: dict[str, Any] | None
    output: dict[str, Any] | None
    failures: list[dict[str, Any]]
    supported: bool


__all__ = ["CounterpartDecision"]
