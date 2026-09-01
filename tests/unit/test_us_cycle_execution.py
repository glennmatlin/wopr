"""Deterministic no-model U.S. Cycle 1 execution tests."""

import json
from pathlib import Path

from tests.unit.us_cycle_test_support import RATIFICATION_PATH, loaded_cycle_fixture

from nuclear_war_contest.situation_room import (
    compile_us_charter,
    load_us_cycle_fixture,
    run_no_model_us_cycle,
)


def test_cycle_delivers_watch_inputs_without_private_information_leak(
    tmp_path: Path,
) -> None:
    charter, fixture = loaded_cycle_fixture(tmp_path)

    run = run_no_model_us_cycle(charter, fixture)
    receipt = run.receipt()

    compiled = compile_us_charter(charter)
    common_recipients = tuple(
        item["recipient_seat_id"]
        for item in receipt["deliveries"]
        if item["input_id"] == "INPUT_COMMON_001"
    )
    private_recipients = tuple(
        item["recipient_seat_id"]
        for item in receipt["deliveries"]
        if item["input_id"] == "INPUT_DNI_PRIVATE_001"
    )
    assert common_recipients == compiled.active_seat_ids()
    assert private_recipients == ("SEAT_DNI",)
    assert receipt["status"] == "failed"
    assert "missing_product" in {item["reason_code"] for item in receipt["failures"]}
    assert receipt["world_effects_admitted"] is False


def test_cycle_executes_charter_graph_and_routes_the_policy_package(
    tmp_path: Path,
) -> None:
    charter, fixture = loaded_cycle_fixture(tmp_path, complete=True)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    assert receipt["status"] == "passed"
    assert receipt["schedule"] == [
        ["GROUP_THREAT_ATTRIBUTION"],
        ["GROUP_DIPLOMATIC_ECONOMIC", "GROUP_NUCLEAR_RADIOLOGICAL"],
        ["GROUP_DEFENSE_ESCALATION"],
        ["GROUP_LEGAL_AUTHORITY"],
        ["GROUP_PRESIDENTIAL_SYNTHESIS"],
        ["GROUP_PC"],
        ["GROUP_NSC"],
    ]
    assert [item["group_id"] for item in receipt["group_attempts"]] == [
        group_id for wave in receipt["schedule"] for group_id in wave
    ]
    assert receipt["policy_package"]["product_id"] == ("PRODUCT_INSTANCE::GROUP_PC")
    assert receipt["decision_route"]["route_id"] == "ROUTE_PRESIDENTIAL_POLICY"
    assert receipt["decision_record"]["product_id"] == ("PRODUCT_INSTANCE::GROUP_NSC")
    assert {item["confirmation_id"] for item in receipt["confirmations"]} == {
        "CONFIRM_NSC_PRESIDENTIAL_DECISION",
        "CONFIRM_NSC_AUTHORITY_RECORD",
    }
    assert receipt["failures"] == []
    assert receipt["world_effects_admitted"] is False


def test_missing_product_blocks_only_descendants_and_preserves_attempt(
    tmp_path: Path,
) -> None:
    charter, complete = loaded_cycle_fixture(tmp_path, complete=True)
    payload = complete.payload()
    payload["group_products"] = [
        item
        for item in payload["group_products"]
        if item["group_id"] != "GROUP_THREAT_ATTRIBUTION"
    ]
    fixture_path = tmp_path / "missing-product.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    attempts = {item["group_id"]: item for item in receipt["group_attempts"]}
    failures = {item["group_id"]: item for item in receipt["failures"]}
    assert attempts["GROUP_THREAT_ATTRIBUTION"]["status"] == "failed"
    assert attempts["GROUP_DIPLOMATIC_ECONOMIC"]["status"] == "accepted"
    assert attempts["GROUP_NUCLEAR_RADIOLOGICAL"]["status"] == "accepted"
    assert failures["GROUP_THREAT_ATTRIBUTION"]["reason_code"] == ("missing_product")
    assert {
        group_id
        for group_id, failure in failures.items()
        if failure["reason_code"] == "blocked_dependency"
    } == {
        "GROUP_DEFENSE_ESCALATION",
        "GROUP_LEGAL_AUTHORITY",
        "GROUP_PRESIDENTIAL_SYNTHESIS",
        "GROUP_PC",
        "GROUP_NSC",
    }
    assert receipt["policy_package"] is None
    assert receipt["decision_record"] is None
