"""U.S. cycle product-delivery and authorized-input tests."""

from __future__ import annotations

from pathlib import Path

from tests.unit.us_cycle_test_support import loaded_cycle_fixture

from nuclear_war_contest.situation_room import (
    compile_us_charter,
    run_no_model_us_cycle,
)


def test_products_follow_declared_permissions_and_feed_dependencies(
    tmp_path: Path,
) -> None:
    charter, fixture = loaded_cycle_fixture(tmp_path, complete=True)

    receipt = run_no_model_us_cycle(charter, fixture).receipt()

    compiled = compile_us_charter(charter)
    threat_recipients = tuple(
        item["recipient_seat_id"]
        for item in receipt["deliveries"]
        if item.get("product_id") == "PRODUCT_INSTANCE::GROUP_THREAT_ATTRIBUTION"
    )
    decision_recipients = tuple(
        item["recipient_seat_id"]
        for item in receipt["deliveries"]
        if item.get("product_id") == "PRODUCT_INSTANCE::GROUP_NSC"
    )
    attempts = {item["group_id"]: item for item in receipt["group_attempts"]}

    threat_audience = {
        seat.seat_id
        for group_id in (
            "GROUP_DEFENSE_ESCALATION",
            "GROUP_PRESIDENTIAL_SYNTHESIS",
        )
        for seat in compiled.group_members(group_id)
    }
    assert threat_recipients == tuple(
        seat_id for seat_id in compiled.active_seat_ids() if seat_id in threat_audience
    )
    assert decision_recipients == compiled.active_seat_ids()
    assert (
        "PRODUCT_INSTANCE::GROUP_THREAT_ATTRIBUTION"
        in (attempts["GROUP_DEFENSE_ESCALATION"]["authorized_input_ids"])
    )
    assert {
        "PRODUCT_INSTANCE::GROUP_THREAT_ATTRIBUTION",
        "PRODUCT_INSTANCE::GROUP_DIPLOMATIC_ECONOMIC",
        "PRODUCT_INSTANCE::GROUP_NUCLEAR_RADIOLOGICAL",
        "PRODUCT_INSTANCE::GROUP_DEFENSE_ESCALATION",
        "PRODUCT_INSTANCE::GROUP_LEGAL_AUTHORITY",
    } <= set(attempts["GROUP_PRESIDENTIAL_SYNTHESIS"]["authorized_input_ids"])
