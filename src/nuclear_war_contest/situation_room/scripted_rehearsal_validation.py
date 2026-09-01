"""Output validation for scripted Room rehearsal."""

from __future__ import annotations

import json
from typing import Any

from .compiled_models import CompiledUsCharter
from .cycle_products import collect_product_attempt
from .free_output_models import ProductValidator
from .scripted_rehearsal_calls import portfolio_product

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


def portfolio_validator(cycle_id: str, group_id: str, seat_id: str) -> ProductValidator:
    def validate(product: dict[str, Any]) -> None:
        expected = portfolio_product(cycle_id, group_id, seat_id)
        fixed = ("schema_version", "product_id", "cycle_id", "group_id", "seat_id")
        if set(product) != _PORTFOLIO_FIELDS:
            raise ValueError(
                "Portfolio Product envelope keys are invalid: "
                f"expected {_encoded(sorted(_PORTFOLIO_FIELDS))}, "
                f"got {_encoded(sorted(product))}"
            )
        if any(product.get(field) != expected[field] for field in fixed):
            raise ValueError("Portfolio Product envelope is invalid")
        if not isinstance(product["position"], dict) or any(
            not isinstance(product[field], list)
            for field in (
                "evidence_basis",
                "uncertainty",
                "blockers",
                "coordination_needs",
                "material_dissent",
            )
        ):
            raise ValueError("Portfolio Product body is invalid")

    return validate


def group_validator(
    group: dict[str, Any],
    schema: dict[str, Any],
    compiled: CompiledUsCharter,
    contract: dict[str, Any] | None = None,
) -> ProductValidator:
    def validate(product: dict[str, Any]) -> None:
        fields = {"product_id", "group_id", "product_schema_id", "content"}
        if set(product) != fields:
            raise ValueError(
                "Group product envelope keys are invalid: "
                f"expected {_encoded(sorted(fields))}, "
                f"got {_encoded(sorted(product))}"
            )
        if product.get("group_id") != group["group_id"]:
            raise ValueError("Group product envelope is invalid")
        mismatch = (
            _contract_mismatch(product, contract) if contract is not None else None
        )
        if mismatch is not None:
            path, expected, actual = mismatch
            raise ValueError(
                f"Group product contract is invalid at {path}: "
                f"expected {_encoded(expected)}, got {_encoded(actual)}"
            )
        _attempt, failure = collect_product_attempt(
            group["group_id"], group, schema, compiled, product
        )
        if failure is not None:
            raise ValueError(f"Group product is invalid: {failure['reason_code']}")

    return validate


def _contract_mismatch(
    actual: Any, expected: Any, path: str = ""
) -> tuple[str, Any, Any] | None:
    if not isinstance(expected, dict):
        return None if actual == expected else (path, expected, actual)
    if not isinstance(actual, dict):
        return path or "<root>", expected, actual
    for key, expected_value in expected.items():
        child_path = f"{path}.{key}" if path else key
        if key not in actual:
            return child_path, expected_value, "<missing>"
        mismatch = _contract_mismatch(actual[key], expected_value, child_path)
        if mismatch is not None:
            return mismatch
    return None


def _encoded(value: Any) -> str:
    return json.dumps(value, allow_nan=False, ensure_ascii=False, sort_keys=True)


def confirmation_validator(
    cycle_id: str, specification: dict[str, Any], seat_id: str, record_id: str
) -> ProductValidator:
    expected = {
        "confirmation_id": specification["confirmation_id"],
        "confirmer_seat_id": seat_id,
        "confirmed_record_id": record_id,
        "status": "confirmed",
    }

    def validate(product: dict[str, Any]) -> None:
        if product != expected:
            raise ValueError(f"{cycle_id} seat confirmation is invalid")

    return validate


__all__ = [
    "confirmation_validator",
    "group_validator",
    "portfolio_validator",
]
