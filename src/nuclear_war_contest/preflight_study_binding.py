"""Checks that a study manifest is exactly the approved candidate design."""

from __future__ import annotations

import math
from typing import Any

from .manifest_types import StudyManifest, StudyModel


def validate_study_binding(manifest: StudyManifest, candidate: Any) -> None:
    if manifest.request_budget is None:
        raise ValueError("Live study models require a frozen request_budget")
    if manifest.source_revision != candidate.source_revision:
        raise ValueError("Study source revision is not bound to the candidate")
    model_subset = False
    if manifest.study_variant == "room_instrument":
        if list(manifest.seeds) != [51, 52, 53]:
            raise ValueError("Study seeds are not the locked Sounding seeds")
        if len(manifest.conditions) != 3:
            raise ValueError(
                "Study conditions are not the three Organizational Presets"
            )
    elif manifest.study_variant == "room_instrument_smoke":
        if list(manifest.seeds) != [51] or manifest.max_turns != 2:
            raise ValueError("Composition smoke must use seed 51 and two turns")
        if len(manifest.models) != 1:
            raise ValueError("Composition smoke must use one approved candidate model")
        if len(manifest.conditions) != 3:
            raise ValueError(
                "Composition smoke conditions are not the three Organizational Presets"
            )
        model_subset = True
    elif manifest.study_variant == "room_instrument_demo":
        if list(manifest.seeds) != [51]:
            raise ValueError("Room Instrument Demo must use seed 51")
        if len(manifest.models) != 1:
            raise ValueError(
                "Room Instrument Demo must use one approved candidate model"
            )
        model_subset = True
    elif manifest.seeds != candidate.study_seeds:
        raise ValueError("Study seeds are not bound to the preflight candidate")
    if (
        manifest.study_variant == "full_factorial"
        and len(manifest.conditions) != candidate.condition_count
    ):
        raise ValueError("Study conditions are not bound to the preflight candidate")
    if manifest.request_budget.max_c2_calls_per_game != candidate.max_c2_calls_per_game:
        raise ValueError("Study C2 cap is not bound to the preflight candidate")
    if (
        manifest.request_budget.max_press_calls_per_game
        != candidate.max_press_calls_per_game
    ):
        raise ValueError("Study press cap is not bound to the preflight candidate")
    if (
        manifest.study_variant
        not in {"room_instrument", "room_instrument_smoke", "room_instrument_demo"}
        and len(manifest.seeds) != candidate.seeds_per_condition
    ):
        raise ValueError("Study seed count is not bound to the preflight candidate")
    _validate_budget(manifest.request_budget, candidate)
    _validate_models(
        manifest.models,
        candidate.models,
        candidate.max_tokens,
        allow_subset=model_subset,
    )


def _validate_budget(budget: Any, candidate: Any) -> None:
    expected = {
        "input_tokens_bound": candidate.input_tokens_bound,
        "max_output_tokens": candidate.max_tokens,
        "max_cost_usd": candidate.proposed_max_cost_usd,
        "transport_retry_margin": candidate.transport_retry_margin,
    }
    for field, value in expected.items():
        if getattr(budget, field) != value:
            raise ValueError(f"Study {field} is not bound to the preflight candidate")
    max_request_cost = max(
        model.input_usd_per_million * candidate.input_tokens_bound / 1_000_000
        + model.output_usd_per_million * candidate.max_tokens / 1_000_000
        for model in candidate.models
    )
    if not math.isclose(
        budget.max_cost_per_request_usd or -1,
        max_request_cost,
        rel_tol=0,
        abs_tol=1e-12,
    ):
        raise ValueError("Study request cost cap is not bound to the candidate")


def _validate_models(
    study_models: tuple[StudyModel, ...],
    candidate_models: tuple[Any, ...],
    max_tokens: int,
    *,
    allow_subset: bool = False,
) -> None:
    candidate_by_id = {model.model_id: model for model in candidate_models}
    study_model_ids = {model.model_id for model in study_models}
    expected_model_ids = set(candidate_by_id)
    if (
        not study_model_ids
        or (allow_subset and not study_model_ids <= expected_model_ids)
        or (not allow_subset and study_model_ids != expected_model_ids)
    ):
        raise ValueError("Study models are not bound to the preflight candidate")
    for study_model in study_models:
        candidate_model = candidate_by_id[study_model.model_id]
        if (
            study_model.backend != candidate_model.backend
            or study_model.provider != candidate_model.provider
            or study_model.client != candidate_model.client
            or study_model.max_retries != candidate_model.max_retries
            or study_model.role_prompt_hashes != candidate_model.role_prompt_hashes
            or study_model.client.get("max_tokens") != max_tokens
        ):
            raise ValueError("Study model settings are not bound to the candidate")


__all__ = ["validate_study_binding"]
