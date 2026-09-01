"""Final explicit non-action adjudication and delivery."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from nuclear_war_contest.date_world import DateProfile, DateRun, admit_transition


def admit_final_adjudication(
    profile: DateProfile,
    run: DateRun,
    adjudication: dict[str, Any],
    cycle2: dict[str, Any],
) -> tuple[DateRun, dict[str, Any], str | None]:
    decision = cycle2.get("decision_record")
    if decision is None or decision["product_id"] != adjudication["decision_record_id"]:
        return run, {}, "decision_mismatch"
    result = admit_transition(profile, run, adjudication["world_event"])
    retained = {
        **adjudication,
        "world_receipt": asdict(result.receipt),
    }
    reason = result.receipt.reason_codes[0] if result.receipt.reason_codes else None
    return result.run, retained, reason


def final_consequence_deliveries(
    adjudication: dict[str, Any], active_seat_ids: list[str]
) -> list[dict[str, str]]:
    event_id = adjudication["world_event"]["template_id"]
    return [
        {
            "delivery_id": f"DELIVERY::{event_id}::{seat_id}",
            "artifact_id": event_id,
            "recipient_seat_id": seat_id,
            "information_class_id": "INFO_COMMON_CRISIS_PICTURE",
        }
        for seat_id in active_seat_ids
    ]


__all__ = ["admit_final_adjudication", "final_consequence_deliveries"]
