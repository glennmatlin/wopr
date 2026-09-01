"""Typed values for the separate model-screening packet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ScreeningModel:
    model_id: str
    model_family: str
    provider_model: str
    backend: str
    provider: str
    client: dict[str, Any]
    max_retries: int
    role_prompt_hashes: dict[str, str]
    input_usd_per_million: float
    output_usd_per_million: float


@dataclass(frozen=True)
class ScreeningManifest:
    manifest_id: str
    source_revision: str
    selection_status: str
    full_design_model_selection: str
    catalog_path: str
    catalog_sha256: str
    budget_path: str
    budget_sha256: str
    final_candidate_path: str
    final_candidate_sha256: str
    screening_seeds: tuple[int, ...]
    study_seeds: tuple[int, ...]
    mode: str
    players: int
    max_turns: int
    temperature: float
    max_tokens: int
    reasoning_enabled: bool
    stream: bool
    output_retries: int
    transport_retry_margin: int
    provider_name: str
    base_url: str
    api_key_env: str
    owner_total_cap_usd: float
    approval_status: str
    network_calls: int
    credentials_read: bool
    models: tuple[ScreeningModel, ...]

__all__ = ["ScreeningManifest", "ScreeningModel"]
