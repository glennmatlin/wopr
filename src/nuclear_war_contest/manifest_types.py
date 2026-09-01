"""Typed values used by the contest study manifest."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class StudyCondition:
    condition_id: str
    communication: str
    authority: str
    authority_parameters: dict[str, Any]
    press_passes: int


@dataclass(frozen=True)
class StudyModel:
    model_id: str
    backend: str
    provider: str
    client: dict[str, Any]
    max_retries: int
    role_prompt_hashes: dict[str, str]


@dataclass(frozen=True)
class StudyCell:
    cell_id: str
    condition_id: str
    model_id: str
    seed: int


@dataclass(frozen=True)
class StudyRequestBudget:
    max_c2_calls_per_game: int
    max_press_calls_per_game: int
    input_tokens_bound: int | None = None
    max_output_tokens: int | None = None
    max_cost_usd: float | None = None
    max_cost_per_request_usd: float | None = None
    transport_retry_margin: int | None = None


@dataclass(frozen=True)
class StudyManifest:
    study_id: str
    protocol_revision: str
    source_revision: str
    players: int
    max_turns: int
    seeds: tuple[int, ...]
    conditions: tuple[StudyCondition, ...]
    models: tuple[StudyModel, ...]
    request_budget: StudyRequestBudget | None = None
    preflight_receipt_hash: str | None = None
    preflight_approval_status: str | None = None
    preflight_receipt_path: str | None = None
    preflight_candidate_manifest_path: str | None = None
    preflight_candidate_manifest_hash: str | None = None
    preflight_executor_revision: str | None = None
    execution_manifest_hash: str | None = None
    execution_approval_hash: str | None = None
    execution_executor_revision: str | None = None
    study_variant: str = "full_factorial"
    overlay: str = "off"
    overlay_pack_hash: str | None = None

    @property
    def cells(self) -> tuple[StudyCell, ...]:
        return tuple(
            StudyCell(
                cell_id=f"{model.model_id}:{condition.condition_id}:seed-{seed}",
                condition_id=condition.condition_id,
                model_id=model.model_id,
                seed=seed,
            )
            for model in self.models
            for condition in self.conditions
            for seed in self.seeds
        )
