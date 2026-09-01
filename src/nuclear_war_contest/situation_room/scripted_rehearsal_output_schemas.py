"""Model-facing output schemas for scripted Room products."""

from __future__ import annotations

from typing import Any

from .cycle_policy import policy_package_domain_dispositions_schema

_PORTFOLIO_FIELDS = {
    "schema_version",
    "product_id",
    "cycle_id",
    "group_id",
    "seat_id",
    "position",
    "evidence_basis",
    "uncertainty",
    "blockers",
    "coordination_needs",
    "material_dissent",
}


def portfolio_output_schema(
    cycle_id: str, group_id: str, seat_id: str
) -> dict[str, Any]:
    constants = {
        "schema_version": "portfolio-product.v0.1",
        "product_id": f"PORTFOLIO::{cycle_id}::{group_id}::{seat_id}",
        "cycle_id": cycle_id,
        "group_id": group_id,
        "seat_id": seat_id,
    }
    properties = {field: {"type": "string"} for field in constants}
    properties.update(
        {
            "position": {"type": "object"},
            "evidence_basis": {"type": "array"},
            "uncertainty": {"type": "array"},
            "blockers": {"type": "array"},
            "coordination_needs": {"type": "array"},
            "material_dissent": {"type": "array"},
        }
    )
    return _schema(sorted(_PORTFOLIO_FIELDS), constants, properties)


def group_output_schema(
    group: dict[str, Any],
    schema: dict[str, Any],
    contract: dict[str, Any] | None,
) -> dict[str, Any]:
    constants = {
        "group_id": group["group_id"],
        "product_schema_id": group["product_schema_id"],
    }
    if contract is not None:
        constants.update(contract)
    content_schema: dict[str, Any] = {"type": "object"}
    if group["group_id"] == "GROUP_PC":
        content_schema["properties"] = {
            "domain_dispositions": policy_package_domain_dispositions_schema()
        }
    output = _schema(
        ["product_id", "group_id", "product_schema_id", "content"],
        constants,
        {
            "product_id": {"type": "string"},
            "group_id": {"type": "string"},
            "product_schema_id": {"type": "string"},
            "content": content_schema,
        },
    )
    output["content_required"] = schema["required_fields"]
    return output


def confirmation_output_schema(
    specification: dict[str, Any], seat_id: str, decision: dict[str, Any]
) -> dict[str, Any]:
    constants = {
        "confirmation_id": specification["confirmation_id"],
        "confirmer_seat_id": seat_id,
        "confirmed_record_id": decision["product_id"],
        "status": "confirmed",
    }
    properties = {field: {"type": "string"} for field in constants}
    return _schema(list(constants), constants, properties)


def _schema(
    required: list[str], constants: dict[str, Any], properties: dict[str, Any]
) -> dict[str, Any]:
    return {
        "type": "object",
        "additionalProperties": False,
        "required": required,
        "constants": constants,
        "properties": properties,
    }


__all__ = [
    "confirmation_output_schema",
    "group_output_schema",
    "portfolio_output_schema",
]
