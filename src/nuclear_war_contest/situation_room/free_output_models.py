"""Public call and result types for free-output Room seats."""

from __future__ import annotations

from collections.abc import Callable
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any

ProductValidator = Callable[[dict[str, Any]], None]


@dataclass(frozen=True)
class SeatProductCall:
    call_id: str
    cycle_id: str
    group_id: str
    mandate: str
    group_role: str
    authorized_deliveries: tuple[dict[str, Any], ...]
    upstream_products: tuple[dict[str, Any], ...]
    output_schema: dict[str, Any]
    _payload: dict[str, Any] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "_payload", self._build_payload())

    def payload(self) -> dict[str, Any]:
        return deepcopy(self._payload)

    def _build_payload(self) -> dict[str, Any]:
        return deepcopy(
            {
                "call_id": self.call_id,
                "cycle_id": self.cycle_id,
                "group_id": self.group_id,
                "mandate": self.mandate,
                "group_role": self.group_role,
                "authorized_deliveries": self.authorized_deliveries,
                "upstream_products": self.upstream_products,
                "output_schema": self.output_schema,
            }
        )


@dataclass(frozen=True)
class SeatProductResult:
    _product: dict[str, Any]
    _trace: dict[str, Any]

    def product(self) -> dict[str, Any]:
        return deepcopy(self._product)

    def trace(self) -> dict[str, Any]:
        return deepcopy(self._trace)


@dataclass
class SeatProductFailure(ValueError):
    message: str
    snapshot: dict[str, Any]

    def __post_init__(self) -> None:
        ValueError.__init__(self, self.message)


__all__ = [
    "ProductValidator",
    "SeatProductCall",
    "SeatProductFailure",
    "SeatProductResult",
]
