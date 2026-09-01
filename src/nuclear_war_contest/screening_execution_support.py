"""Authorization and ephemeral study-manifest helpers for model screening."""

from __future__ import annotations

import json
import math
import string
from hashlib import sha256
from typing import Any

from .manifest_types import (
    StudyCondition,
    StudyManifest,
    StudyModel,
    StudyRequestBudget,
)
from .screening_types import ScreeningManifest


def validate_screening_approval(
    manifest: ScreeningManifest,
    manifest_sha256: str,
    approval: Any,
    executor_revision: str,
) -> float:
    expected = {
        "schema_version",
        "manifest_sha256",
        "approved",
        "max_spend_usd",
        "model_ids",
        "endpoints",
        "credential_envs",
        "executor_revision",
    }
    if not isinstance(approval, dict) or set(approval) != expected:
        raise ValueError("Screening approval fields are invalid")
    if approval["schema_version"] != 1 or approval["approved"] is not True:
        raise ValueError("Screening approval is not approved")
    if approval["manifest_sha256"] != manifest_sha256 or not _hex(manifest_sha256, 64):
        raise ValueError("Screening approval is not bound to the manifest")
    if approval["executor_revision"] != executor_revision or not _hex(
        executor_revision, 40
    ):
        raise ValueError("Screening approval executor revision is invalid")
    spend = approval["max_spend_usd"]
    if (
        isinstance(spend, bool)
        or not isinstance(spend, int | float)
        or not math.isfinite(float(spend))
        or float(spend) < _planning_bound(manifest)
        or float(spend) > manifest.owner_total_cap_usd
    ):
        raise ValueError("Screening approval spend cap is invalid")
    if approval["model_ids"] != sorted(
        model.provider_model for model in manifest.models
    ):
        raise ValueError("Screening approval models do not match manifest")
    if approval["endpoints"] != sorted(
        model.client["base_url"] for model in manifest.models
    ):
        raise ValueError("Screening approval endpoints do not match manifest")
    if approval["credential_envs"] != sorted(
        model.client["api_key_env"] for model in manifest.models
    ):
        raise ValueError("Screening approval credentials do not match manifest")
    return float(spend)


def build_screening_study_manifest(
    manifest: ScreeningManifest,
    max_spend_usd: float,
    *,
    execution_manifest_hash: str | None = None,
    approval_hash: str | None = None,
    executor_revision: str | None = None,
) -> StudyManifest:
    condition = StudyCondition(
        condition_id="screening_press_light",
        communication="press_light",
        authority="sole_authority",
        authority_parameters={"deference": 0.0},
        press_passes=1,
    )
    models = tuple(
        StudyModel(
            model_id=model.model_id,
            backend=model.backend,
            provider=model.provider,
            client=dict(model.client),
            max_retries=model.max_retries,
            role_prompt_hashes=dict(model.role_prompt_hashes),
        )
        for model in manifest.models
    )
    budget = StudyRequestBudget(
        max_c2_calls_per_game=2048,
        max_press_calls_per_game=160,
        input_tokens_bound=8192,
        max_output_tokens=manifest.max_tokens,
        max_cost_usd=max_spend_usd,
        max_cost_per_request_usd=max(_request_cost(model) for model in manifest.models),
        transport_retry_margin=manifest.transport_retry_margin,
    )
    return StudyManifest(
        study_id=manifest.manifest_id,
        protocol_revision="screening-2026-08-16",
        source_revision=manifest.source_revision,
        players=manifest.players,
        max_turns=manifest.max_turns,
        seeds=manifest.screening_seeds,
        conditions=(condition,),
        models=models,
        request_budget=budget,
        execution_manifest_hash=execution_manifest_hash,
        execution_approval_hash=approval_hash,
        execution_executor_revision=executor_revision,
    )


def _planning_bound(manifest: ScreeningManifest) -> float:
    attempts = len(manifest.screening_seeds) * 624 * 6
    return sum(
        attempts
        * (8192 * model.input_usd_per_million + 512 * model.output_usd_per_million)
        / 1_000_000
        for model in manifest.models
    )


def _request_cost(model: Any) -> float:
    return (
        8192 * model.input_usd_per_million + 512 * model.output_usd_per_million
    ) / 1_000_000


def screening_approval_hash(approval: dict[str, Any]) -> str:
    encoded = json.dumps(approval, sort_keys=True, separators=(",", ":"))
    return sha256(encoded.encode("utf-8")).hexdigest()


def _hex(value: Any, length: int) -> bool:
    return (
        isinstance(value, str)
        and len(value) == length
        and all(character in string.hexdigits for character in value)
    )
