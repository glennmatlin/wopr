"""Validation helpers for the offline candidate model manifest."""

from __future__ import annotations

from typing import Any

from nuclear_war_env.integer_validation import is_strict_int

from .manifest_parameter_validation import validate_client, validate_role_prompt_hashes
from .preflight_scalars import nonnegative_int, rate, text
from .preflight_types import CandidateManifest, CandidateModel

_MODEL_FIELDS = {
    "model_id",
    "model_family",
    "backend",
    "provider",
    "client",
    "max_retries",
    "role_prompt_hashes",
    "input_usd_per_million",
    "output_usd_per_million",
}


def load_models(value: Any) -> tuple[CandidateModel, ...]:
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError("Candidate manifest must contain exactly two models")
    models = tuple(_load_model(item) for item in _objects(value))
    if len({model.model_id for model in models}) != len(models):
        raise ValueError("Candidate model ids must be unique")
    if len({model.model_family for model in models}) != len(models):
        raise ValueError("Candidate model families must be distinct")
    if len({model.client["model"] for model in models}) != len(models):
        raise ValueError("Candidate provider model ids must be unique")
    return models


def validate_manifest(manifest: CandidateManifest) -> None:
    if set(manifest.preflight_seeds) & set(manifest.study_seeds):
        raise ValueError("Candidate preflight and study seeds must be disjoint")
    if manifest.output_retries != 1:
        raise ValueError("Candidate output_retries must be one")
    if manifest.transport_retry_margin != 2:
        raise ValueError("Candidate transport_retry_margin must be two")
    if manifest.condition_count != 4:
        raise ValueError("Candidate condition_count must be four")
    if manifest.seeds_per_condition != len(manifest.study_seeds):
        raise ValueError("Candidate seeds_per_condition must match study_seeds")
    if manifest.max_c2_calls_per_game != 2048:
        raise ValueError("Candidate max_c2_calls_per_game must be 2048")
    if manifest.max_press_calls_per_game != 160:
        raise ValueError("Candidate max_press_calls_per_game must be 160")
    if manifest.max_tokens != 512 or manifest.input_tokens_bound < 8192:
        raise ValueError("Candidate request token bounds are too small")
    if (
        manifest.observed_c2_calls_per_game > manifest.max_c2_calls_per_game
        or manifest.observed_press_calls_per_game > manifest.max_press_calls_per_game
    ):
        raise ValueError("Candidate observed fixture counts exceed hard caps")
    if any(model.backend != "concordia_http" for model in manifest.models):
        raise ValueError("Candidate models must use the concordia_http backend")
    if any(model.max_retries != manifest.output_retries for model in manifest.models):
        raise ValueError("Candidate max_retries must match output_retries")
    if any(
        model.client["max_tokens"] != manifest.max_tokens for model in manifest.models
    ):
        raise ValueError("Candidate client max_tokens must match request budget")


def candidate_client(value: Any, provider: str) -> dict[str, Any]:
    client = validate_client(value, provider)
    required = {
        "provider",
        "base_url",
        "model",
        "api_key_env",
        "provider_label",
        "timeout_seconds",
        "temperature",
        "max_tokens",
        "reasoning_enabled",
        "stream",
    }
    if set(client) != required and set(client) != required | {"reasoning_effort"}:
        raise ValueError("Candidate client must pin an exact model and settings")
    if "model_env" in client or "base_url_env" in client:
        raise ValueError("Candidate client must pin an exact model and endpoint")
    if (
        provider != "together"
        or client["provider"] != provider
        or client["base_url"] != "https://api.together.ai/v1"
        or client["provider_label"] != "together"
    ):
        raise ValueError("Candidate models must use the Together provider")
    if client["api_key_env"] != "TOGETHER_API_KEY":
        raise ValueError("Candidate client must use TOGETHER_API_KEY")
    if not isinstance(client["model"], str) or "/" not in client["model"]:
        raise ValueError("Candidate client model must be a provider model id")
    if (
        not isinstance(client["temperature"], int | float)
        or isinstance(client["temperature"], bool)
        or not 0 <= client["temperature"] <= 2
    ):
        raise ValueError("Candidate client temperature is invalid")
    if not is_strict_int(client["timeout_seconds"]) or client["timeout_seconds"] < 1:
        raise ValueError("Candidate client timeout_seconds is invalid")
    if client["reasoning_enabled"] is not False or client["stream"] is not True:
        raise ValueError(
            "Candidate client reasoning and streaming controls are invalid"
        )
    return client


def _load_model(item: dict[str, Any]) -> CandidateModel:
    provider = text(item["provider"], "provider")
    return CandidateModel(
        model_id=text(item["model_id"], "model_id"),
        model_family=text(item["model_family"], "model_family"),
        backend=text(item["backend"], "backend"),
        provider=provider,
        client=candidate_client(item["client"], provider),
        max_retries=nonnegative_int(item["max_retries"], "max_retries"),
        role_prompt_hashes=validate_role_prompt_hashes(item["role_prompt_hashes"]),
        input_usd_per_million=rate(
            item["input_usd_per_million"], "input_usd_per_million"
        ),
        output_usd_per_million=rate(
            item["output_usd_per_million"], "output_usd_per_million"
        ),
    )


def _objects(value: list[Any]) -> list[dict[str, Any]]:
    objects: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, dict) or set(item) != _MODEL_FIELDS:
            raise ValueError("Candidate model fields are invalid")
        objects.append(item)
    return objects
