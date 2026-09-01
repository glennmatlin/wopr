"""Seat calls and validators for scripted Room rehearsal."""

from __future__ import annotations

from typing import Any

from .free_output_models import SeatProductCall
from .scripted_rehearsal_ids import (
    confirmation_call_id,
    group_product_call_id,
    portfolio_call_id,
)
from .scripted_rehearsal_output_schemas import (
    confirmation_output_schema,
    group_output_schema,
    portfolio_output_schema,
)


def portfolio_product(cycle_id: str, group_id: str, seat_id: str) -> dict[str, Any]:
    return {
        "schema_version": "portfolio-product.v0.1",
        "product_id": f"PORTFOLIO::{cycle_id}::{group_id}::{seat_id}",
        "cycle_id": cycle_id,
        "group_id": group_id,
        "seat_id": seat_id,
        "position": {"summary": "Scripted rehearsal contribution."},
        "evidence_basis": [],
        "uncertainty": [],
        "blockers": [],
        "coordination_needs": [],
        "material_dissent": [],
    }


def portfolio_call(
    cycle_id: str,
    group: dict[str, Any],
    seat: dict[str, Any],
    deliveries: tuple[dict[str, Any], ...],
) -> SeatProductCall:
    return SeatProductCall(
        call_id=portfolio_call_id(cycle_id, group["group_id"], seat["seat_id"]),
        cycle_id=cycle_id,
        group_id=group["group_id"],
        mandate=seat["mandate"],
        group_role="Contribute an attributable Portfolio Product.",
        authorized_deliveries=deliveries,
        upstream_products=(),
        output_schema=portfolio_output_schema(
            cycle_id, group["group_id"], seat["seat_id"]
        ),
    )


def group_call(
    cycle_id: str,
    group: dict[str, Any],
    recorder: dict[str, Any],
    deliveries: tuple[dict[str, Any], ...],
    contributions: tuple[dict[str, Any], ...],
    schema: dict[str, Any],
    contract: dict[str, Any] | None = None,
) -> SeatProductCall:
    return SeatProductCall(
        call_id=group_product_call_id(cycle_id, group["group_id"], recorder["seat_id"]),
        cycle_id=cycle_id,
        group_id=group["group_id"],
        mandate=recorder["mandate"],
        group_role="Record the group product without adding authority.",
        authorized_deliveries=deliveries,
        upstream_products=contributions,
        output_schema=group_output_schema(group, schema, contract),
    )


def confirmation_call(
    cycle_id: str,
    group_id: str,
    seat: dict[str, Any],
    specification: dict[str, Any],
    decision: dict[str, Any],
) -> SeatProductCall:
    return SeatProductCall(
        call_id=confirmation_call_id(
            cycle_id, specification["confirmation_id"], seat["seat_id"]
        ),
        cycle_id=cycle_id,
        group_id=group_id,
        mandate=seat["mandate"],
        group_role=specification["description"],
        authorized_deliveries=(),
        upstream_products=(decision,),
        output_schema=confirmation_output_schema(
            specification, seat["seat_id"], decision
        ),
    )


__all__ = ["confirmation_call", "group_call", "portfolio_call", "portfolio_product"]
