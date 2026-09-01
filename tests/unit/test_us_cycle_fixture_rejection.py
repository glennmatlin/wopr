"""Strict nested U.S. cycle fixture rejection tests."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest
from tests.unit.us_cycle_test_support import RATIFICATION_PATH, loaded_cycle_fixture

from nuclear_war_contest.situation_room import load_us_cycle_fixture


@pytest.mark.parametrize(
    ("case_id", "reason_code"),
    [
        ("invalid_status", "invalid_envelope"),
        ("unexpected_input_field", "invalid_envelope"),
        ("duplicate_product_id", "duplicate_id"),
        ("unknown_information_class", "unknown_reference"),
        ("undeclared_watch_permission", "unknown_reference"),
        ("inactive_group_product", "unknown_reference"),
    ],
)
def test_fixture_rejects_invalid_nested_contract(
    tmp_path: Path, case_id: str, reason_code: str
) -> None:
    charter, complete = loaded_cycle_fixture(tmp_path, complete=True)
    payload = complete.payload()
    if case_id == "invalid_status":
        payload["status"] = "evidence"
    elif case_id == "unexpected_input_field":
        payload["watch_inputs"][0]["unexpected"] = True
    elif case_id == "duplicate_product_id":
        payload["group_products"].append(deepcopy(payload["group_products"][0]))
    elif case_id == "unknown_information_class":
        payload["watch_inputs"][0]["information_class_id"] = "INFO_UNKNOWN"
    elif case_id == "undeclared_watch_permission":
        payload["watch_inputs"][0]["information_class_id"] = "INFO_DECISION_RECORD"
    else:
        payload["group_products"][0]["group_id"] = "GROUP_HOMELAND_CONSEQUENCES"
        payload["group_products"][0]["product_schema_id"] = (
            "PRODUCT_HOMELAND_CONSEQUENCES"
        )
    fixture_path = tmp_path / f"{case_id}.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match=reason_code):
        load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)
