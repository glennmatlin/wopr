"""Accepted minimum Counterpart Charter contract tests."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest

from nuclear_war_contest.situation_room import (
    ActorSourceRegister,
    load_actor_source_register,
    load_counterpart_charter,
)

ROOT = Path(__file__).parents[2]
CONTEST = ROOT / "docs/contest"


def _load_himaldesh_bundle() -> tuple[ActorSourceRegister, dict[str, Any]]:
    source = load_actor_source_register(
        CONTEST / "HIMALDESH_SOURCE_REGISTER.candidate.json"
    )
    charter_path = CONTEST / "HIMALDESH_CHARTER.candidate.json"
    payload = json.loads(charter_path.read_text(encoding="utf-8"))
    return source, payload


def _write_payload(tmp_path: Path, payload: dict[str, Any]) -> Path:
    path = tmp_path / "counterpart-charter.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_loads_exact_ratified_actor_bundles() -> None:
    expected = {
        "HIMALDESH": (
            "ACTOR_HIMALDESH",
            "6a2ad9ea06a462c3283ecdc8a14dccee0ffe9830f20bf961deddb830ed308f25",
            "c7184d1866913782fce5afea3edf1cc3a26942699973eb232e3bbee1782cb822",
        ),
        "OLVANA": (
            "ACTOR_OLVANA",
            "932c12452ccb3373ccf4fc07c7d91f290d6812d1d8d1b227f49f0cf8eb4e06d5",
            "0aa48c3cb8e2980324b3db6d4c5426fb5ff67f746775728a0b00f38897fe389a",
        ),
    }
    for prefix, (actor_id, source_hash, charter_hash) in expected.items():
        source = load_actor_source_register(
            CONTEST / f"{prefix}_SOURCE_REGISTER.candidate.json"
        )
        charter = load_counterpart_charter(
            CONTEST / f"{prefix}_CHARTER.candidate.json", source
        )

        assert source.actor_id == actor_id
        assert source.content_hash == source_hash
        assert charter.actor_id == actor_id
        assert charter.source_register_hash == source_hash
        assert charter.content_hash == charter_hash


def test_rejects_route_authority_without_declared_role(tmp_path: Path) -> None:
    source, payload = _load_himaldesh_bundle()
    seats = payload["institution_registry"]["seats"]
    prime_minister = next(
        seat for seat in seats if seat["seat_id"] == "HD_SEAT_PRIME_MINISTER"
    )
    prime_minister["decision_route_roles"] = []

    with pytest.raises(ValueError, match="inferred_delegation"):
        load_counterpart_charter(_write_payload(tmp_path, payload), source)


def test_rejects_confirmation_outside_its_required_route(tmp_path: Path) -> None:
    source, payload = _load_himaldesh_bundle()
    confirmations = payload["required_confirmations"]
    defense = next(
        item
        for item in confirmations
        if item["confirmation_id"] == "HD_CONFIRM_DEFENSE_FEASIBILITY"
    )
    defense["applicability_action_classes"] = [
        "interior_force_transfer_to_defense_control",
        "strategic_readiness_signaling_or_use",
    ]

    with pytest.raises(ValueError, match="incomplete_route"):
        load_counterpart_charter(_write_payload(tmp_path, payload), source)


def test_rejects_delivery_to_a_seat_without_entitlement(tmp_path: Path) -> None:
    source, payload = _load_himaldesh_bundle()
    permissions = payload["disclosure_permissions"]
    permission = next(
        item
        for item in permissions
        if item["permission_id"] == "HD_PERMISSION_EXTERNAL_PRIVATE"
    )
    permission["recipient_ids"] = ["HD_SEAT_PRIME_MINISTER"]

    with pytest.raises(ValueError, match="entitlement_leak"):
        load_counterpart_charter(_write_payload(tmp_path, payload), source)


def test_rejects_duplicate_runnable_action_class(tmp_path: Path) -> None:
    source, payload = _load_himaldesh_bundle()
    duplicate = deepcopy(payload["decision_routes"][0])
    duplicate["route_id"] = "HD_ROUTE_DUPLICATE_ACTION"
    payload["decision_routes"].append(duplicate)

    with pytest.raises(ValueError, match="incomplete_route"):
        load_counterpart_charter(_write_payload(tmp_path, payload), source)


def test_rejects_objective_without_source_scope(tmp_path: Path) -> None:
    source, payload = _load_himaldesh_bundle()
    payload["objective_ids"] = ["HD_OBJECTIVE_UNSUPPORTED"]

    with pytest.raises(ValueError, match="unknown_reference"):
        load_counterpart_charter(_write_payload(tmp_path, payload), source)
