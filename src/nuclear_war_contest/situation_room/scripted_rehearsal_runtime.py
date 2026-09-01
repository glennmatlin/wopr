"""Persistent seat runtimes for scripted Room rehearsal."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from threading import Lock
from typing import Any

from nuclear_war_agents import LLMModelClient

from .charter import UsCharter
from .compiler import compile_us_charter
from .free_output_adapter import (
    ConcordiaFreeOutputSeat,
    build_concordia_free_output_seat,
)
from .free_output_models import ProductValidator, SeatProductCall, SeatProductResult
from .scripted_rehearsal_scripts import ScriptedResponse, ScriptedRoomClient

ClientFactory = Callable[[str, Mapping[str, ScriptedResponse]], LLMModelClient]


@dataclass
class SeatRuntime:
    seat: ConcordiaFreeOutputSeat
    lock: Lock

    def produce(
        self, call: SeatProductCall, validator: ProductValidator
    ) -> SeatProductResult:
        with self.lock:
            return self.seat.produce(call, validator)

    def observe(self, scene: str) -> None:
        with self.lock:
            self.seat.observe(scene)


def build_seat_runtimes(
    charter: UsCharter,
    responses: dict[str, dict[str, ScriptedResponse]],
    factory: ClientFactory,
    *,
    max_output_retries: int = 0,
    attempt_sink: Callable[[str, dict[str, Any], dict[str, Any]], None] | None = None,
) -> dict[str, SeatRuntime]:
    payload = charter.payload()
    seats = {item["seat_id"]: item for item in payload["institution_registry"]["seats"]}
    runtimes: dict[str, SeatRuntime] = {}
    for seat_id in compile_us_charter(charter).active_seat_ids():
        seat = seats[seat_id]
        client = factory(seat_id, responses[seat_id])
        entity = build_concordia_free_output_seat(
            seat_id=seat_id,
            identity={"name": seat["office_class"]},
            client=client,
            max_output_retries=max_output_retries,
            attempt_sink=attempt_sink,
        )
        runtimes[seat_id] = SeatRuntime(entity, Lock())
    return runtimes


def default_client_factory(
    _seat_id: str, responses: Mapping[str, ScriptedResponse]
) -> LLMModelClient:
    return ScriptedRoomClient(responses)


__all__ = [
    "ClientFactory",
    "SeatRuntime",
    "build_seat_runtimes",
    "default_client_factory",
]
