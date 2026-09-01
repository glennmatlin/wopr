"""Validation helpers for the offline model-screening packet."""

from __future__ import annotations

from typing import Any

from .manifest_parameter_validation import validate_role_prompt_hashes
from .preflight_scalars import nonnegative_int, rate, text
from .preflight_validation import candidate_client
from .screening_types import ScreeningModel

_MODEL_FIELDS = {
    "model_id",
    "model_family",
    "provider_model",
    "backend",
    "provider",
    "client",
    "max_retries",
    "role_prompt_hashes",
    "input_usd_per_million",
    "output_usd_per_million",
}


def load_screening_models(
    value: Any, provider: dict[str, Any], screening: dict[str, Any]
) -> tuple[ScreeningModel, ...]:
    if not isinstance(value, list) or len(value) != 3:
        raise ValueError("Screening manifest must contain exactly three models")
    models = tuple(_load_model(item, provider, screening) for item in value)
    if len({model.model_id for model in models}) != 3:
        raise ValueError("Screening model ids must be unique")
    if len({model.model_family for model in models}) != 3:
        raise ValueError("Screening model families must be distinct")
    if len({model.provider_model for model in models}) != 3:
        raise ValueError("Screening provider model ids must be unique")
    return models


def _load_model(
    item: Any, provider: dict[str, Any], screening: dict[str, Any]
) -> ScreeningModel:
    if not isinstance(item, dict) or set(item) != _MODEL_FIELDS:
        raise ValueError("Screening model fields are invalid")
    model_provider = text(item["provider"], "model provider")
    client = candidate_client(item["client"], model_provider)
    provider_model = text(item["provider_model"], "provider_model")
    _validate_client(
        client,
        provider_model,
        model_provider,
        text(item["backend"], "backend"),
        provider,
        screening,
    )
    return ScreeningModel(
        model_id=text(item["model_id"], "model_id"),
        model_family=text(item["model_family"], "model_family"),
        provider_model=provider_model,
        backend=text(item["backend"], "backend"),
        provider=model_provider,
        client=client,
        max_retries=nonnegative_int(item["max_retries"], "max_retries"),
        role_prompt_hashes=validate_role_prompt_hashes(item["role_prompt_hashes"]),
        input_usd_per_million=rate(
            item["input_usd_per_million"], "input_usd_per_million"
        ),
        output_usd_per_million=rate(
            item["output_usd_per_million"], "output_usd_per_million"
        ),
    )


def _validate_client(
    client: dict[str, Any],
    provider_model: str,
    model_provider: str,
    backend: str,
    provider: dict[str, Any],
    screening: dict[str, Any],
) -> None:
    if backend != "concordia_http" or model_provider != provider["name"]:
        raise ValueError("Screening models must use the pinned HTTP provider")
    if client["model"] != provider_model:
        raise ValueError("Screening client model must match provider_model")
    if client["base_url"] != provider["base_url"]:
        raise ValueError("Screening client base_url does not match provider")
    if client["api_key_env"] != provider["api_key_env"]:
        raise ValueError("Screening client credential environment does not match")
    for field in ("temperature", "max_tokens", "reasoning_enabled", "stream"):
        if client[field] != screening[field]:
            raise ValueError(f"Screening client {field} is not frozen")


__all__ = ["load_screening_models"]
