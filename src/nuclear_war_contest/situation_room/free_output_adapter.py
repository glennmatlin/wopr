"""Contest-scoped Concordia adapter for open Room products."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from nuclear_war_agents import LLMCompletion, LLMModelClient
from nuclear_war_agents.llm_http_transport import LLMHttpError
from nuclear_war_concordia.native_entity import _entity
from nuclear_war_concordia.native_helpers import entity_log
from nuclear_war_concordia.native_http_model import ConcordiaHTTPChoiceModel

from .free_output_models import (
    ProductValidator,
    SeatProductCall,
    SeatProductFailure,
    SeatProductResult,
)
from .free_output_scene import action_spec, render_scene
from .free_output_trace import (
    attempt_payload,
    trace_payload,
    transport_attempt_payload,
)
from .free_output_validation import parse_product

ROOM_OBSERVATION_HISTORY_LENGTH = 2


@dataclass
class ConcordiaFreeOutputSeat:
    seat_id: str
    entity: Any
    model: ConcordiaHTTPChoiceModel
    max_output_retries: int = 1
    attempt_sink: Callable[[str, dict[str, Any], dict[str, Any]], None] | None = None

    def observe(self, scene: str) -> None:
        self.entity.observe(scene)

    def produce(
        self, call: SeatProductCall, validator: ProductValidator
    ) -> SeatProductResult:
        if self.max_output_retries < 0:
            raise ValueError("Free-output retry count must be non-negative")
        scene = render_scene(call)
        self.entity.observe(scene)
        attempts: list[dict[str, Any]] = []
        completions: list[LLMCompletion] = []
        feedback: list[str] = []
        for attempt_number in range(1, self.max_output_retries + 2):
            product, attempt, completion = self._attempt_or_fail(
                call, attempts, completions, attempt_number, feedback, validator
            )
            attempts.append(attempt)
            if self.attempt_sink is not None:
                self.attempt_sink(self.seat_id, call.payload(), attempt)
            if completion is not None:
                completions.append(completion)
            if product is not None:
                return SeatProductResult(
                    product, self._trace(call, attempts, completions, "accepted")
                )
            feedback.append(str(attempt["validation_error"]))
        raise SeatProductFailure(
            "Free-output Room product exhausted its retry budget",
            self._trace(call, attempts, completions, "failed"),
        )

    def _attempt_or_fail(
        self,
        call: SeatProductCall,
        attempts: list[dict[str, Any]],
        completions: list[LLMCompletion],
        attempt_number: int,
        feedback: list[str],
        validator: ProductValidator,
    ) -> tuple[dict[str, Any] | None, dict[str, Any], LLMCompletion | None]:
        try:
            return self._attempt(call, attempt_number, feedback, validator)
        except (LLMHttpError, OSError) as exc:
            attempt = transport_attempt_payload(
                attempt_number, self.model.last_prompt, exc
            )
            attempts.append(attempt)
            if self.attempt_sink is not None:
                self.attempt_sink(self.seat_id, call.payload(), attempt)
            raise SeatProductFailure(
                "Free-output Room product transport failed",
                self._trace(call, attempts, completions, "failed"),
            ) from exc

    def _attempt(
        self,
        call: SeatProductCall,
        attempt_number: int,
        feedback: list[str],
        validator: ProductValidator,
    ) -> tuple[dict[str, Any] | None, dict[str, Any], LLMCompletion | None]:
        self.model.last_completion = None
        self.model.last_prompt = None
        raw_response = self.entity.act(action_spec(call, feedback))
        product: dict[str, Any] | None = None
        validation_error: str | None = None
        try:
            product = parse_product(raw_response)
            validator(product)
        except ValueError as exc:
            validation_error = str(exc)
            product = None
        attempt = attempt_payload(
            attempt_number,
            self.model.last_prompt,
            raw_response,
            product,
            validation_error,
            entity_log(self.entity),
            completion=self.model.last_completion,
        )
        return product, attempt, self.model.last_completion

    def _trace(
        self,
        call: SeatProductCall,
        attempts: list[dict[str, Any]],
        completions: list[LLMCompletion],
        status: str,
    ) -> dict[str, Any]:
        return trace_payload(
            self.seat_id, call, attempts, completions, status, self.max_output_retries
        )


def build_concordia_free_output_seat(
    *,
    seat_id: str,
    identity: Mapping[str, str],
    client: LLMModelClient,
    max_output_retries: int = 1,
    attempt_sink: Callable[[str, dict[str, Any], dict[str, Any]], None] | None = None,
) -> ConcordiaFreeOutputSeat:
    model = ConcordiaHTTPChoiceModel(client)
    entity = _entity(
        identity, model, observation_history_length=ROOM_OBSERVATION_HISTORY_LENGTH
    )
    return ConcordiaFreeOutputSeat(
        seat_id, entity, model, max_output_retries, attempt_sink
    )
