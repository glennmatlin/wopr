"""Candidate-bound owner authorization for live model preflights."""

from __future__ import annotations

import math
import string
from typing import Any

from .preflight import candidate_manifest_hash
from .preflight_types import CandidateManifest


def build_live_preflight_approval(
    manifest: CandidateManifest,
    executor_revision: str,
    max_spend_usd: float | None = None,
) -> dict[str, Any]:
    """Build a redacted approval payload for an explicitly bounded run."""
    return {
        "schema_version": 1,
        "candidate_manifest_hash": candidate_manifest_hash(manifest),
        "approved": True,
        "max_spend_usd": (
            manifest.proposed_max_cost_usd if max_spend_usd is None else max_spend_usd
        ),
        "model_ids": sorted(model.model_id for model in manifest.models),
        "endpoints": sorted(_endpoints(manifest)),
        "credential_envs": sorted(_credential_envs(manifest)),
        "executor_revision": executor_revision,
    }


def validate_live_preflight_approval(
    manifest: CandidateManifest,
    approval: Any,
    executor_revision: str,
) -> None:
    if not isinstance(approval, dict):
        raise ValueError("Live preflight approval must be an object")
    expected_keys = {
        "schema_version",
        "candidate_manifest_hash",
        "approved",
        "max_spend_usd",
        "model_ids",
        "endpoints",
        "credential_envs",
        "executor_revision",
    }
    if set(approval) != expected_keys:
        raise ValueError("Live preflight approval fields are invalid")
    if approval["schema_version"] != 1 or approval["approved"] is not True:
        raise ValueError("Live preflight approval is not approved")
    if approval["candidate_manifest_hash"] != candidate_manifest_hash(manifest):
        raise ValueError("Live preflight approval is not bound to the candidate")
    if approval["executor_revision"] != executor_revision:
        raise ValueError("Live preflight approval executor revision does not match")
    if not _revision(executor_revision):
        raise ValueError("Live preflight executor revision must be a full SHA")
    spend = approval["max_spend_usd"]
    from .live_preflight_budget import cost_bound

    minimum_spend = max(
        manifest.proposed_max_cost_usd,
        cost_bound(manifest)["upper_bound_usd"],
    )
    if (
        isinstance(spend, bool)
        or not isinstance(spend, int | float)
        or not math.isfinite(float(spend))
        or float(spend) < minimum_spend
    ):
        raise ValueError("Live preflight approval spend cap is below the candidate")
    if approval["model_ids"] != sorted(model.model_id for model in manifest.models):
        raise ValueError("Live preflight approval models do not match candidate")
    if approval["endpoints"] != sorted(_endpoints(manifest)):
        raise ValueError("Live preflight approval endpoints do not match candidate")
    if approval["credential_envs"] != sorted(_credential_envs(manifest)):
        raise ValueError("Live preflight approval credentials do not match candidate")


def _endpoints(manifest: CandidateManifest) -> set[str]:
    return {str(model.client.get("base_url", "")) for model in manifest.models}


def _credential_envs(manifest: CandidateManifest) -> set[str]:
    return {str(model.client.get("api_key_env", "")) for model in manifest.models}


def _revision(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(character in string.hexdigits for character in value)
    )


__all__ = [
    "build_live_preflight_approval",
    "validate_live_preflight_approval",
]
