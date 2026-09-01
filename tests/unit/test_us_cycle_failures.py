"""Fail-closed no-model U.S. cycle behavior tests."""

from __future__ import annotations

import json
from pathlib import Path

from tests.unit.us_cycle_test_support import RATIFICATION_PATH, loaded_cycle_fixture

from nuclear_war_contest.situation_room import (
    load_us_cycle_fixture,
    run_no_model_us_cycle,
)


def test_missing_required_confirmation_preserves_record_without_decision(
    tmp_path: Path,
) -> None:
    charter, complete = loaded_cycle_fixture(tmp_path, complete=True)
    payload = complete.payload()
    payload["confirmations"] = payload["confirmations"][1:]
    fixture_path = tmp_path / "missing-confirmation.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    missing = [
        item
        for item in receipt["failures"]
        if item["reason_code"] == "missing_confirmation"
    ]
    assert receipt["status"] == "failed"
    assert receipt["decision_record"]["product_id"] == ("PRODUCT_INSTANCE::GROUP_NSC")
    assert receipt["decision_supported"] is False
    assert [item["confirmation_id"] for item in missing] == [
        "CONFIRM_NSC_PRESIDENTIAL_DECISION"
    ]
    assert receipt["world_effects_admitted"] is False


def test_route_mismatch_preserves_rejected_decision_record(tmp_path: Path) -> None:
    charter, complete = loaded_cycle_fixture(tmp_path, complete=True)
    payload = complete.payload()
    record = next(
        item for item in payload["group_products"] if item["group_id"] == "GROUP_NSC"
    )
    record["content"]["route_id"] = "ROUTE_UNDECLARED"
    fixture_path = tmp_path / "route-mismatch.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    route_failures = [
        item for item in receipt["failures"] if item["reason_code"] == "route_mismatch"
    ]
    assert receipt["status"] == "failed"
    assert receipt["decision_record"]["content"]["route_id"] == ("ROUTE_UNDECLARED")
    assert receipt["decision_supported"] is False
    assert len(route_failures) == 1


def test_missing_declared_consultation_rejects_decision_record(tmp_path: Path) -> None:
    charter, complete = loaded_cycle_fixture(tmp_path, complete=True)
    payload = complete.payload()
    record = next(
        item for item in payload["group_products"] if item["group_id"] == "GROUP_NSC"
    )
    record["content"]["consultations"] = ["GROUP_PC"]
    fixture_path = tmp_path / "missing-consultation.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    assert receipt["status"] == "failed"
    assert receipt["decision_supported"] is False
    assert "route_mismatch" in {item["reason_code"] for item in receipt["failures"]}
