"""Cross-artifact reference checks for two-cycle fixtures."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.profile import DateProfile

from .cycle_fixture import UsCycleFixture


def validate_episode_fixture_links(
    payload: dict[str, Any],
    cycle1: UsCycleFixture,
    bridge_receipt: dict[str, Any],
    profile: DateProfile,
    cycle2: UsCycleFixture,
) -> None:
    _forecast_link(payload["forecast_binding"], cycle1, profile)
    external = payload["cycle2_external_parent_ids"]
    expected = _expected_world_parents(bridge_receipt)
    if external != expected:
        raise ValueError("unknown_reference: Cycle 2 World parents are invalid")
    cycle2_payload = cycle2.payload()
    common = _one(
        cycle2_payload["watch_inputs"],
        "input_id",
        "USC2_INPUT_COMMON_WORLD_001",
        "Cycle 2 common input",
    )
    if (
        common["information_class_id"] != "INFO_COMMON_CRISIS_PICTURE"
        or common["causal_parent_ids"] != external
        or common["content"].get("matched_pressure") != external[1:]
        or common["content"].get("endogenous_consequences") != external[:1]
    ):
        raise ValueError("causal_mismatch: Cycle 2 common provenance is invalid")
    _institutional_identity(cycle1.payload(), cycle2_payload)
    _reassessment_link(payload, cycle2_payload)
    _adjudication_link(payload["final_adjudication"], cycle2_payload, external)


def _forecast_link(
    binding: dict[str, Any], cycle1: UsCycleFixture, profile: DateProfile
) -> None:
    source = _one(
        cycle1.payload()["watch_inputs"],
        "input_id",
        binding["cycle1_input_id"],
        "Cycle 1 forecast input",
    )
    event = profile.event_template(binding["world_event_id"])
    if (
        binding["relationship"] != "authored_summary_of"
        or source["information_class_id"] != "INFO_RAW_WEATHER_FORECAST"
        or event["template_id"] != "OBS_WX_RIDGE_FORECAST_01"
        or binding["shared_entity_ids"] != event["affected_entity_ids"]
    ):
        raise ValueError("causal_mismatch: forecast binding is invalid")


def _expected_world_parents(bridge: dict[str, Any]) -> list[str]:
    admitted = [
        item for item in bridge["run"]["effect_results"] if item["status"] == "admitted"
    ]
    if len(admitted) != 1:
        raise ValueError("identity_mismatch: D69 admitted effect is invalid")
    return [
        admitted[0]["world_event"]["template_id"],
        "WX_RIDGE_FRONT_01",
        "OBS_WX_RIDGE_CONFIRMED_01",
    ]


def _reassessment_link(payload: dict[str, Any], cycle2: dict[str, Any]) -> None:
    products = {item["group_id"]: item for item in cycle2["group_products"]}
    package = products["GROUP_PC"]["content"].get("reassessment")
    decision = products["GROUP_NSC"]["content"].get("reassessment")
    expected = payload["cycle2_reassessment"]
    if package != expected or decision != expected:
        raise ValueError("causal_mismatch: Cycle 2 reassessment is inconsistent")
    if expected["disposition"] not in {
        "reaffirm",
        "change",
        "condition",
        "withdraw",
        "decline",
    }:
        raise ValueError("invalid_envelope: adaptation disposition is invalid")


def _institutional_identity(cycle1: dict[str, Any], cycle2: dict[str, Any]) -> None:
    def product_shape(item: dict[str, Any]) -> tuple[str, str]:
        return item["group_id"], item["product_schema_id"]

    def confirmation_shape(item: dict[str, Any]) -> tuple[str, list[str], str]:
        return item["confirmation_id"], item["confirmer_seat_ids"], item["status"]

    if (
        cycle2["action_class"] != cycle1["action_class"]
        or [product_shape(item) for item in cycle2["group_products"]]
        != [product_shape(item) for item in cycle1["group_products"]]
        or [confirmation_shape(item) for item in cycle2["confirmations"]]
        != [confirmation_shape(item) for item in cycle1["confirmations"]]
    ):
        raise ValueError("identity_mismatch: Cycle 2 institutional structure changed")


def _adjudication_link(
    item: dict[str, Any], cycle2: dict[str, Any], external: list[str]
) -> None:
    decision = next(
        product
        for product in cycle2["group_products"]
        if product["group_id"] == "GROUP_NSC"
    )
    if item["decision_record_id"] != decision["product_id"]:
        raise ValueError(
            "causal_mismatch: final decision record is not Cycle 2's decision"
        )
    package = next(
        product
        for product in cycle2["group_products"]
        if product["group_id"] == "GROUP_PC"
    )
    component_ids = {
        component["component_id"] for component in package["content"]["components"]
    }
    if not set(item["source_component_ids"]) <= component_ids:
        raise ValueError("unknown_reference: final component is unknown")
    if not set(item["world_event"]["causal_parent_ids"]) <= set(external):
        raise ValueError("unknown_reference: final World parent is unknown")


def _one(
    items: list[dict[str, Any]], field: str, value: str, label: str
) -> dict[str, Any]:
    matches = [item for item in items if item.get(field) == value]
    if len(matches) != 1:
        raise ValueError(f"unknown_reference: {label} is unresolved")
    return matches[0]


__all__ = ["validate_episode_fixture_links"]
