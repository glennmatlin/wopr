"""Shared no-model U.S. cycle fixtures."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from tests.unit.us_cycle_fixture_values import (
    CHARTER_PATH,
    POLICY_DOMAINS,
    RATIFICATION_HASH,
    RATIFICATION_PATH,
    SOURCE_PATH,
    development_counterparts,
)

from nuclear_war_contest.situation_room import (
    compile_us_charter,
    load_source_register,
    load_us_charter,
    load_us_cycle_fixture,
)


def complete_products(charter) -> list[dict[str, Any]]:
    payload = charter.payload()
    compiled = compile_us_charter(charter)
    groups = {item["group_id"]: item for item in payload["groups"]}
    schemas = {item["product_schema_id"]: item for item in payload["product_schemas"]}
    products: list[dict[str, Any]] = []
    for group_id in compiled.active_group_ids():
        group = groups[group_id]
        schema = schemas[group["product_schema_id"]]
        content = {field: f"{group_id}:{field}" for field in schema["required_fields"]}
        content["source_fact_ids"] = schema["fact_ids"]
        if "objective_ids" in content:
            content["objective_ids"] = payload["objective_ids"]
        if "components" in content:
            content["components"] = []
        if "domain_dispositions" in content:
            content["domain_dispositions"] = [
                {
                    "domain_id": domain_id,
                    "responsible_seat_ids": ["SEAT_NSA"],
                    "deciding_forum_group_id": "GROUP_NSC",
                    "reason": "authored no-model fixture",
                    "disposition": "conditional_action",
                }
                for domain_id in POLICY_DOMAINS
            ]
        if group_id == "GROUP_NSC":
            content["route_id"] = "ROUTE_PRESIDENTIAL_POLICY"
            content["policy_package_id"] = "PRODUCT_INSTANCE::GROUP_PC"
            content["consultations"] = ["GROUP_PC", "GROUP_LEGAL_AUTHORITY"]
            content["required_confirmations"] = [
                "CONFIRM_NSC_PRESIDENTIAL_DECISION",
                "CONFIRM_NSC_AUTHORITY_RECORD",
            ]
        products.append(
            {
                "product_id": f"PRODUCT_INSTANCE::{group_id}",
                "group_id": group_id,
                "product_schema_id": group["product_schema_id"],
                "content": content,
            }
        )
    return list(reversed(products))


def confirmations(charter) -> list[dict[str, Any]]:
    payload = charter.payload()
    route = next(
        item
        for item in payload["decision_routes"]
        if item["action_class"] == "presidential_policy_direction"
    )
    by_id = {
        item["confirmation_id"]: item for item in payload["required_confirmations"]
    }
    return [
        {
            "confirmation_id": confirmation_id,
            "confirmer_seat_ids": by_id[confirmation_id]["confirmer_seat_ids"],
            "confirmed_record_id": "PRODUCT_INSTANCE::GROUP_NSC",
            "status": "confirmed",
        }
        for confirmation_id in route["required_confirmation_ids"]
    ]


def loaded_cycle_fixture(tmp_path: Path, *, complete: bool = False):
    source = load_source_register(SOURCE_PATH)
    charter = load_us_charter(CHARTER_PATH, source)
    payload = {
        "schema_version": "us-cycle-fixture.v0.1",
        "fixture_id": "US_CYCLE1_NO_MODEL.watch-test",
        "fixture_version": "0.1.0",
        "status": "development_fixture_non_evidence",
        "actor_id": "ACTOR_UNITED_STATES",
        "cycle_id": "CYCLE_1",
        "ratification_id": "US_PUBLIC_2026Q3.ratification.D67",
        "ratification_hash": RATIFICATION_HASH,
        "source_register_hash": source.content_hash,
        "charter_hash": charter.content_hash,
        "action_class": "presidential_policy_direction",
        "counterpart_fixtures": development_counterparts(),
        "watch_inputs": [
            {
                "input_id": "INPUT_COMMON_001",
                "information_class_id": "INFO_COMMON_CRISIS_PICTURE",
                "sender_id": "SERVICE_WATCH",
                "causal_parent_ids": [
                    "HIM_OUTPUT_REQUEST_001",
                    "OLV_OUTPUT_POSTURE_001",
                ],
                "content": {"report": "common synthetic crisis picture"},
            },
            {
                "input_id": "INPUT_DNI_PRIVATE_001",
                "information_class_id": "INFO_INTELLIGENCE_PRIVATE",
                "sender_id": "SERVICE_WATCH",
                "causal_parent_ids": [],
                "content": {"report": "synthetic DNI-only confidence detail"},
            },
        ],
        "group_products": complete_products(charter) if complete else [],
        "confirmations": confirmations(charter) if complete else [],
    }
    fixture_path = tmp_path / "cycle.json"
    fixture_path.write_text(json.dumps(payload), encoding="utf-8")
    fixture = load_us_cycle_fixture(fixture_path, charter, RATIFICATION_PATH)
    return charter, fixture
