"""Semantic consistency rejection tests for U.S. Room Charters."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest
from tests.unit.us_charter_test_support import minimal_us_charter
from tests.unit.us_compiler_test_support import compilable_us_charter
from tests.unit.us_source_test_support import minimal_source_register

from nuclear_war_contest.situation_room import load_source_register, load_us_charter


def _load_mutated(tmp_path: Path, payload: dict[str, Any]) -> None:
    source_path = tmp_path / "source-register.json"
    source_path.write_text(json.dumps(minimal_source_register()), encoding="utf-8")
    source = load_source_register(source_path)
    payload["source_register_hash"] = source.content_hash
    charter_path = tmp_path / "charter.json"
    charter_path.write_text(json.dumps(payload), encoding="utf-8")
    load_us_charter(charter_path, source)


def _private_information() -> dict[str, Any]:
    return {
        "information_class_id": "INFO_PRIVATE",
        "description": "Private synthetic information.",
        "sensitivity": "seat_private",
        "fact_ids": [],
        "inference_ids": [],
    }


def _permission(permission_id: str, recipient_id: str, mode: str) -> dict[str, Any]:
    return {
        "permission_id": permission_id,
        "information_class_id": "INFO_PRIVATE",
        "sender_ids": ["SERVICE_WATCH"],
        "recipient_ids": [recipient_id],
        "delivery_mode": mode,
        "fact_ids": [],
        "inference_ids": [],
    }


def test_rejects_objective_without_source_scope(tmp_path: Path) -> None:
    payload = minimal_us_charter("replaced")
    payload["objective_ids"] = ["OBJ_UNKNOWN"]

    with pytest.raises(ValueError, match="unknown_reference"):
        _load_mutated(tmp_path, payload)


def test_rejects_nonreciprocal_seat_group_membership(tmp_path: Path) -> None:
    payload = minimal_us_charter("replaced")
    payload["institution_registry"]["seats"][0]["group_ids"] = []

    with pytest.raises(ValueError, match="invalid_envelope"):
        _load_mutated(tmp_path, payload)


def test_rejects_incorrect_shared_seat_barrier(tmp_path: Path) -> None:
    payload = compilable_us_charter("replaced")
    payload["groups"][0]["shared_seat_barrier_ids"] = []

    with pytest.raises(ValueError, match="invalid_envelope"):
        _load_mutated(tmp_path, payload)


def test_rejects_direct_delivery_without_entitlement(tmp_path: Path) -> None:
    payload = minimal_us_charter("replaced")
    payload["information_classes"].append(_private_information())
    payload["disclosure_permissions"].append(
        _permission("PERMISSION_PRIVATE_DIRECT", "SEAT_PRESIDENT", "direct")
    )

    with pytest.raises(ValueError, match="entitlement_leak"):
        _load_mutated(tmp_path, payload)


def test_rejects_group_delivery_without_member_entitlement(tmp_path: Path) -> None:
    payload = deepcopy(compilable_us_charter("replaced"))
    payload["disclosure_permissions"].append(
        _permission("PERMISSION_PRIVATE_GROUP", "GROUP_NSC", "group_delivery")
    )

    with pytest.raises(ValueError, match="entitlement_leak"):
        _load_mutated(tmp_path, payload)
