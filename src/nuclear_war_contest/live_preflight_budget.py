"""Request and price envelopes for the live preflight matrix."""

from __future__ import annotations

from .preflight_types import CandidateManifest


def request_bound(manifest: CandidateManifest) -> dict[str, int]:
    attempts_per_seed = manifest.transport_retry_margin + 1
    return {
        "provider_attempts": len(manifest.models)
        * len(manifest.preflight_seeds)
        * attempts_per_seed,
        "input_tokens_per_attempt": manifest.input_tokens_bound,
        "output_tokens_per_attempt": manifest.max_tokens,
    }


def cost_bound(manifest: CandidateManifest) -> dict[str, float]:
    attempts = manifest.transport_retry_margin + 1
    total = 0.0
    for model in manifest.models:
        input_cost = manifest.input_tokens_bound * model.input_usd_per_million
        output_cost = manifest.max_tokens * model.output_usd_per_million
        total += (
            attempts
            * len(manifest.preflight_seeds)
            * (input_cost + output_cost)
            / 1_000_000
        )
    return {
        "upper_bound_usd": round(total, 9),
        "study_max_cost_usd": manifest.proposed_max_cost_usd,
    }


__all__ = ["cost_bound", "request_bound"]
