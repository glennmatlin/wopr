"""Deterministic U.S. Room Charter compiler tests."""

from __future__ import annotations

import json
from pathlib import Path

from tests.unit.us_compiler_test_support import compilable_us_charter
from tests.unit.us_source_test_support import minimal_source_register

from nuclear_war_contest.situation_room import (
    compile_us_charter,
    load_source_register,
    load_us_charter,
)


def _compiled_charter(tmp_path: Path):
    source_path = tmp_path / "source-register.json"
    source_path.write_text(json.dumps(minimal_source_register()), encoding="utf-8")
    source_register = load_source_register(source_path)
    charter_path = tmp_path / "charter.json"
    charter_path.write_text(
        json.dumps(compilable_us_charter(source_register.content_hash)),
        encoding="utf-8",
    )
    return compile_us_charter(load_us_charter(charter_path, source_register))


def test_compiler_preserves_one_seat_across_groups(tmp_path: Path) -> None:
    compiled = _compiled_charter(tmp_path)

    nsc_dni = compiled.group_members("GROUP_NSC")[1]
    intel_dni = compiled.group_members("GROUP_INTEL")[0]

    assert nsc_dni is intel_dni
    assert compiled.seat_groups("SEAT_DNI") == ("GROUP_NSC", "GROUP_INTEL")


def test_compiler_derives_entitlements_barriers_and_concurrency(tmp_path: Path) -> None:
    compiled = _compiled_charter(tmp_path)

    assert compiled.recipients_for("INFO_PRIVATE", "SERVICE_WATCH") == ("SEAT_DNI",)
    assert compiled.barrier_seat_ids("GROUP_NSC", "GROUP_INTEL") == ("SEAT_DNI",)
    assert not compiled.can_run_concurrently("GROUP_NSC", "GROUP_INTEL")
    assert compiled.can_run_concurrently("GROUP_INTEL", "GROUP_DIPLOMACY")


def test_compiler_excludes_advisers_from_consensus_and_indexes_routes(
    tmp_path: Path,
) -> None:
    compiled = _compiled_charter(tmp_path)

    assert compiled.voting_member_ids("GROUP_NSC") == ("SEAT_PRESIDENT",)
    assert compiled.route_id_for("presidential_policy") == "ROUTE_PRESIDENTIAL"


def test_compiler_unions_split_permissions_for_one_delivery_key(tmp_path: Path) -> None:
    source_path = tmp_path / "source-register.json"
    source_path.write_text(json.dumps(minimal_source_register()), encoding="utf-8")
    source_register = load_source_register(source_path)
    payload = compilable_us_charter(source_register.content_hash)
    payload["institution_registry"]["seats"][0]["information_entitlement_ids"].append(
        "INFO_PRIVATE"
    )
    permission = payload["disclosure_permissions"][-1].copy()
    permission["permission_id"] = "PERMISSION_PRIVATE_PRESIDENT"
    permission["recipient_ids"] = ["SEAT_PRESIDENT"]
    payload["disclosure_permissions"].append(permission)
    charter_path = tmp_path / "charter.json"
    charter_path.write_text(json.dumps(payload), encoding="utf-8")

    compiled = compile_us_charter(load_us_charter(charter_path, source_register))

    assert compiled.recipients_for("INFO_PRIVATE", "SERVICE_WATCH") == (
        "SEAT_DNI",
        "SEAT_PRESIDENT",
    )
