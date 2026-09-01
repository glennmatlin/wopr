"""Conservative, offline request and cost bounds for candidate models."""

from __future__ import annotations

from typing import Any

from .preflight_types import CandidateManifest, CandidateModel


def build_budget(manifest: CandidateManifest) -> dict[str, Any]:
    games_per_model = manifest.condition_count * manifest.seeds_per_condition
    games = games_per_model * len(manifest.models)
    calls_per_game = manifest.max_c2_calls_per_game + manifest.max_press_calls_per_game
    retry_multiplier = (manifest.output_retries + 1) * (
        manifest.transport_retry_margin + 1
    )
    requests_per_game = calls_per_game * retry_multiplier
    requests_per_model = games_per_model * requests_per_game
    model_rows = [
        _model_budget(model, requests_per_model, manifest) for model in manifest.models
    ]
    upper_bound = sum(row["cost_usd"] for row in model_rows)
    return {
        "study_games": games,
        "games_per_model": games_per_model,
        "base_calls_per_game": calls_per_game,
        "output_retries": manifest.output_retries,
        "transport_retry_margin": manifest.transport_retry_margin,
        "retry_multiplier": retry_multiplier,
        "provider_request_attempts": games * requests_per_game,
        "input_tokens_per_request": manifest.input_tokens_bound,
        "output_tokens_per_request": manifest.max_tokens,
        "input_tokens": games * requests_per_game * manifest.input_tokens_bound,
        "output_tokens": games * requests_per_game * manifest.max_tokens,
        "models": model_rows,
        "upper_bound_usd": round(upper_bound, 6),
    }


def _model_budget(
    model: CandidateModel,
    requests: int,
    manifest: CandidateManifest,
) -> dict[str, Any]:
    input_tokens = requests * manifest.input_tokens_bound
    output_tokens = requests * manifest.max_tokens
    cost = input_tokens / 1_000_000 * model.input_usd_per_million
    cost += output_tokens / 1_000_000 * model.output_usd_per_million
    return {
        "model_id": model.model_id,
        "provider_model": model.client["model"],
        "provider_request_attempts": requests,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "cost_usd": round(cost, 6),
    }


def enforce_channel_caps(
    manifest: CandidateManifest,
    c2_calls: int,
    press_calls: int,
) -> None:
    if c2_calls < 0 or press_calls < 0:
        raise ValueError("Observed channel calls must be nonnegative")
    if c2_calls > manifest.max_c2_calls_per_game:
        raise ValueError("C2 channel cap exceeded")
    if press_calls > manifest.max_press_calls_per_game:
        raise ValueError("Press channel cap exceeded")


__all__ = ["build_budget", "enforce_channel_caps"]
