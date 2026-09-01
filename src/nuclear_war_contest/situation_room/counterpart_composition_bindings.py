"""Counterpart output-to-U.S. causal binding checks."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

from .episode_models import TwoCycleFixture


def _one(items: list[dict[str, Any]], field: str, value: str) -> dict[str, Any]:
    matches = [item for item in items if item.get(field) == value]
    if len(matches) != 1:
        raise ValueError(f"unknown_reference: composition {value} is unresolved")
    return matches[0]


def _target_input_ids(cycle1: dict[str, Any], output_id: str) -> list[str]:
    return [
        item["input_id"]
        for item in cycle1["watch_inputs"]
        if output_id in item["causal_parent_ids"]
    ]


def _observed_binding(
    binding: dict[str, Any], receipt: dict[str, Any], cycle1: dict[str, Any]
) -> tuple[Any, ...]:
    output = receipt["run"].get("output")
    projection = receipt["run"].get("output_projection")
    if not isinstance(output, dict) or not isinstance(projection, dict):
        raise ValueError("causal_mismatch: counterpart Room output is absent")
    return (
        receipt.get("actor_id"),
        binding["receipt_key"],
        projection.get("projection_owner"),
        projection.get("mapping_type"),
        projection.get("projection_id"),
        projection.get("source_decision_record_id"),
        output.get("output_id"),
        canonical_hash(output),
        _target_input_ids(cycle1, binding["output_id"]),
    )


def _expected_binding(binding: dict[str, Any]) -> tuple[Any, ...]:
    return (
        binding["actor_id"],
        binding["receipt_key"],
        binding["mapping_owner"],
        binding["mapping_type"],
        binding["projection_id"],
        binding["source_decision_record_id"],
        binding["output_id"],
        binding["output_hash"],
        binding["us_cycle1_input_ids"],
    )


def _counterpart_record(
    binding: dict[str, Any], receipt: dict[str, Any], cycle1: dict[str, Any]
) -> dict[str, Any]:
    if _observed_binding(binding, receipt, cycle1) != _expected_binding(binding):
        raise ValueError("causal_mismatch: counterpart output binding is invalid")
    run = receipt["run"]
    output = run["output"]
    historical = _one(cycle1["counterpart_fixtures"], "actor_id", binding["actor_id"])
    if historical.get("outputs") != [output]:
        raise ValueError("causal_mismatch: counterpart migration bytes changed")
    return {
        "actor_id": binding["actor_id"],
        "source_register_hash": receipt["source_register_hash"],
        "charter_hash": receipt["charter_hash"],
        "room_fixture_hash": receipt["fixture_hash"],
        "room_run_hash": receipt["run_hash"],
        "room_receipt_hash": receipt["receipt_hash"],
        "decision_route_id": run["decision_route"]["route_id"],
        "mapping_owner": binding["mapping_owner"],
        "mapping_type": binding["mapping_type"],
        "projection_id": binding["projection_id"],
        "source_decision_record_id": binding["source_decision_record_id"],
        "output_id": binding["output_id"],
        "output_hash": binding["output_hash"],
        "us_cycle1_input_ids": deepcopy(binding["us_cycle1_input_ids"]),
    }


def validate_counterpart_output_bindings(
    payload: dict[str, Any],
    two_cycle: TwoCycleFixture,
    receipts: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], ...]:
    bindings = payload["output_bindings"]
    observed_keys = [(item["actor_id"], item["receipt_key"]) for item in bindings]
    expected_keys = [
        ("ACTOR_HIMALDESH", "himaldesh"),
        ("ACTOR_OLVANA", "olvana"),
    ]
    if observed_keys != expected_keys:
        raise ValueError("identity_mismatch: counterpart binding order is invalid")
    cycle1 = two_cycle.cycle1_fixture().payload()
    return tuple(
        _counterpart_record(item, receipts[item["receipt_key"]], cycle1)
        for item in bindings
    )


__all__ = ["validate_counterpart_output_bindings"]
