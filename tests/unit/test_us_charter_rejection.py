"""Fail-closed U.S. Room Charter tests."""

from __future__ import annotations

import json
from collections.abc import Callable
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest
from tests.unit.us_charter_test_support import minimal_us_charter
from tests.unit.us_source_test_support import minimal_source_register

from nuclear_war_contest.situation_room import load_source_register, load_us_charter


def _leak_world_truth(payload: dict[str, Any]) -> None:
    payload["information_classes"].append(
        {
            "information_class_id": "INFO_WORLD_GROUND_TRUTH",
            "description": "Hidden World truth.",
            "sensitivity": "world_ground_truth",
            "fact_ids": [],
            "inference_ids": [],
        }
    )
    payload["institution_registry"]["seats"][0]["information_entitlement_ids"].append(
        "INFO_WORLD_GROUND_TRUTH"
    )


def _break_final_record_route(payload: dict[str, Any]) -> None:
    payload["product_schemas"][0]["producing_group_ids"] = []


def _duplicate_action_class(payload: dict[str, Any]) -> None:
    route = deepcopy(payload["decision_routes"][0])
    route["route_id"] = "ROUTE_DUPLICATE_ACTION_CLASS"
    payload["decision_routes"].append(route)


@pytest.mark.parametrize(
    ("mutation", "reason_code"),
    [
        (lambda payload: payload.update({"unknown": True}), "invalid_envelope"),
        (
            lambda payload: payload["institution_registry"]["seats"].append(
                payload["institution_registry"]["seats"][0]
            ),
            "duplicate_id",
        ),
        (
            lambda payload: payload["institution_registry"]["seats"][0].update(
                {"group_ids": ["GROUP_UNKNOWN"]}
            ),
            "unknown_reference",
        ),
        (
            lambda payload: payload["institution_registry"]["seats"][0].update(
                {"fact_ids": ["FACT_UNKNOWN"]}
            ),
            "unbound_fact",
        ),
        (
            lambda payload: payload["institution_registry"]["seats"][0].update(
                {"inference_ids": ["INFERENCE_UNKNOWN"]}
            ),
            "unbound_inference",
        ),
        (
            lambda payload: payload["institution_registry"]["seats"][0].update(
                {"current_officeholder": "forbidden"}
            ),
            "forbidden_officeholder_field",
        ),
        (_leak_world_truth, "entitlement_leak"),
        (
            lambda payload: payload["activation_predicates"][0].update(
                {"first_episode_value": "yes"}
            ),
            "activation_error",
        ),
        (
            lambda payload: payload["groups"][0].update(
                {"dependency_group_ids": ["GROUP_NSC"]}
            ),
            "dependency_cycle",
        ),
        (
            lambda payload: payload["institution_registry"]["seats"][0].update(
                {"decision_route_roles": []}
            ),
            "inferred_delegation",
        ),
        (
            lambda payload: payload["institution_registry"]["seats"][0].update(
                {"adviser_status": "chair_weighted"}
            ),
            "invalid_adviser_status",
        ),
        (_break_final_record_route, "incomplete_route"),
        (_duplicate_action_class, "incomplete_route"),
        (
            lambda payload: payload["decision_routes"][0].update(
                {"required_confirmation_ids": ["CONFIRM_MISSING"]}
            ),
            "unknown_reference",
        ),
    ],
)
def test_us_charter_fails_closed(
    tmp_path: Path,
    mutation: Callable[[dict[str, Any]], None],
    reason_code: str,
) -> None:
    source_path = tmp_path / "source-register.json"
    source_path.write_text(json.dumps(minimal_source_register()), encoding="utf-8")
    source_register = load_source_register(source_path)
    payload = minimal_us_charter(source_register.content_hash)
    mutation(payload)
    charter_path = tmp_path / "charter.json"
    charter_path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match=reason_code):
        load_us_charter(charter_path, source_register)
