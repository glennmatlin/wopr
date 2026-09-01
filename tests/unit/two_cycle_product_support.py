"""Authored Cycle 2 product changes for no-model episode tests."""

from __future__ import annotations

from typing import Any

from tests.unit.two_cycle_fixture_values import WORLD_PARENT_IDS


def apply_cycle2_reassessment(
    payload: dict[str, Any], reassessment: dict[str, Any]
) -> None:
    products = {item["group_id"]: item for item in payload["group_products"]}
    for product in products.values():
        product["content"]["cycle2_changed_evidence_ids"] = list(WORLD_PARENT_IDS)
    package = products["GROUP_PC"]["content"]
    package["package_version"] = "US_POLICY_PACKAGE_001.v2"
    package["current_assessment"] = (
        "The intelligence package is prepared, but ridge observation is intermittent "
        "and South Pass support is restricted; recipient clearance remains unresolved."
    )
    package["reassessment"] = reassessment
    package["decision_or_return_record"] = (
        "Condition the prior package on degraded access and the unresolved "
        "recipient gate."
    )
    for item in package["components"]:
        if item["component_id"] == "COMP_INTELLIGENCE_SHARING":
            item["content"] = (
                "Retain the prepared package and do not transmit until a compliant "
                "recipient channel is confirmed."
            )
            item["timing"] = "conditioned after the six-hour reassessment"
    record = products["GROUP_NSC"]["content"]
    record["reassessment"] = reassessment
    record["presidential_decision"] = (
        "Condition the prior package: retain preparation, withhold transmission, "
        "and reassess after recipient and access conditions change."
    )
    record["what_was_not_decided"] = [
        "No intelligence transmission was authorized.",
        "No U.S. target selection, fires, or combat force was authorized.",
        "No effect-level authority or capability was inferred from this record.",
    ]
    record["reassessment_point"] = "Upon recipient clearance or material access change."


__all__ = ["apply_cycle2_reassessment"]
