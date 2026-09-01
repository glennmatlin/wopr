"""Deterministic boundary responses for offline Room rehearsal."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from threading import Lock
from typing import Any

from nuclear_war_agents import LLMCompletion

from .compiler import compile_us_charter
from .episode_models import TwoCycleFixture
from .scripted_rehearsal_calls import portfolio_product
from .scripted_rehearsal_ids import (
    confirmation_call_id,
    group_product_call_id,
    portfolio_call_id,
)

ScriptedResponse = str | Exception
ScriptedResponses = dict[str, dict[str, ScriptedResponse]]
_CALL_PATTERN = re.compile(r'"call_id":"([^"]+)"')


class ScriptedRoomClient:
    def __init__(self, responses: Mapping[str, ScriptedResponse]) -> None:
        self._responses = dict(responses)
        self._used: set[str] = set()
        self._lock = Lock()

    def complete(self, prompt: str) -> LLMCompletion:
        call_id = _current_call_id(prompt)
        with self._lock:
            if call_id in self._used or call_id not in self._responses:
                raise ValueError(f"Scripted rehearsal call is unavailable: {call_id}")
            self._used.add(call_id)
            response = self._responses[call_id]
        if isinstance(response, Exception):
            raise response
        return LLMCompletion(
            raw_response=response,
            provider_label="offline-scripted-rehearsal",
            provider_model="retained-fixture-bytes",
        )


def build_scripted_responses(fixture: TwoCycleFixture) -> ScriptedResponses:
    compiled = compile_us_charter(fixture.charter)
    responses: ScriptedResponses = {
        seat_id: {} for seat_id in compiled.active_seat_ids()
    }
    for cycle in (fixture.cycle1_fixture(), fixture.cycle2_fixture()):
        _add_cycle_responses(responses, fixture, cycle.payload())
    return responses


def _add_cycle_responses(
    responses: ScriptedResponses,
    fixture: TwoCycleFixture,
    cycle: dict[str, Any],
) -> None:
    charter = fixture.charter.payload()
    compiled = compile_us_charter(fixture.charter)
    products = {item["group_id"]: item for item in cycle["group_products"]}
    for group_id in compiled.active_group_ids():
        members = compiled.group_members(group_id)
        for member in members:
            call_id = portfolio_call_id(cycle["cycle_id"], group_id, member.seat_id)
            product = portfolio_product(cycle["cycle_id"], group_id, member.seat_id)
            responses[member.seat_id][call_id] = _encode(product)
        recorder = members[0].seat_id
        call_id = group_product_call_id(cycle["cycle_id"], group_id, recorder)
        responses[recorder][call_id] = _encode(products[group_id])
    _add_confirmation_responses(responses, charter, cycle)


def _add_confirmation_responses(
    responses: ScriptedResponses,
    charter: dict[str, Any],
    cycle: dict[str, Any],
) -> None:
    specs = {
        item["confirmation_id"]: item for item in charter["required_confirmations"]
    }
    for confirmation in cycle["confirmations"]:
        specification = specs[confirmation["confirmation_id"]]
        for seat_id in specification["confirmer_seat_ids"]:
            call_id = confirmation_call_id(
                cycle["cycle_id"], confirmation["confirmation_id"], seat_id
            )
            response = {
                "confirmation_id": confirmation["confirmation_id"],
                "confirmer_seat_id": seat_id,
                "confirmed_record_id": confirmation["confirmed_record_id"],
                "status": confirmation["status"],
            }
            responses[seat_id][call_id] = _encode(response)


def _current_call_id(prompt: str) -> str:
    matches = _CALL_PATTERN.findall(prompt)
    if not matches:
        raise ValueError("Scripted rehearsal prompt has no call identity")
    return matches[-1]


def _encode(value: dict[str, Any]) -> str:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


__all__ = [
    "ScriptedResponse",
    "ScriptedResponses",
    "ScriptedRoomClient",
    "build_scripted_responses",
]
