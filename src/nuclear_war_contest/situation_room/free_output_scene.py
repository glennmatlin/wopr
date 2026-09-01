"""Canonical scenes and free-action requests for Room seat products."""

from __future__ import annotations

import json
from typing import Any

from nuclear_war_concordia.native_entity import _free_action_spec

from .free_output_models import SeatProductCall


def action_spec(call: SeatProductCall, feedback: list[str]) -> Any:
    output_schema = call.payload()["output_schema"]
    encoded_schema = json.dumps(
        output_schema,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    required_keys = json.dumps(
        output_schema.get("required", []), ensure_ascii=False, separators=(",", ":")
    )
    call_to_action = (
        "Return one JSON object for the current call only. Treat authorized "
        "deliveries and upstream products as input evidence, not output templates."
    )
    if feedback:
        encoded = json.dumps(feedback, ensure_ascii=False)
        call_to_action = f"{call_to_action} Correct these errors: {encoded}"
    call_to_action = (
        f"{call_to_action} The current call ID is {json.dumps(call.call_id)}. "
        "The following JSON is the response schema, not the response itself. "
        "Return an instance that follows its constants and types. Do not return "
        "the schema or a wrapper containing call_id or output_schema. The response "
        f"must contain exactly these top-level keys: {required_keys}.\n"
        f"Response schema for validation only:\n{encoded_schema}"
    )
    return _free_action_spec(
        call_to_action=call_to_action,
        tag="situation_room_product",
    )


def render_scene(call: SeatProductCall) -> str:
    encoded = json.dumps(
        call.payload(),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return f"Situation Room product call.\nScene JSON:\n{encoded}\n"


__all__ = ["action_spec", "render_scene"]
