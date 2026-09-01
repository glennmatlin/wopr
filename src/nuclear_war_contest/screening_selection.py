"""Deterministic, behavior-independent retention of screened models."""

from __future__ import annotations

import math
from typing import Any

from .screening_types import ScreeningManifest


def build_screening_selection(
    manifest: ScreeningManifest, attempts: list[dict[str, Any]]
) -> dict[str, Any]:
    reports = [_model_report(manifest, model, attempts) for model in manifest.models]
    eligible = sorted(
        (report for report in reports if report["eligible"]),
        key=lambda report: (
            report["output_reprompt_count"],
            report["transport_retry_count"],
            report["provider_attempt_count"],
            report["actual_cost_usd"],
            report["provider_model"],
        ),
    )
    ranked = [report["model_id"] for report in eligible]
    return {
        "schema_version": 1,
        "selection_status": "ready" if len(eligible) >= 2 else "insufficient",
        "eligible_model_ids": ranked,
        "ranked_model_ids": ranked,
        "retained_model_ids": ranked[:2],
        "all_three_eligible": len(eligible) == 3,
        "requires_protocol_amendment_for_all_three": len(eligible) == 3,
        "models": reports,
    }


def _model_report(
    manifest: ScreeningManifest, model: Any, attempts: list[dict[str, Any]]
) -> dict[str, Any]:
    rows = [row for row in attempts if row.get("model_id") == model.model_id]
    reasons: list[str] = []
    if len(rows) != len(manifest.screening_seeds):
        reasons.append("missing_seed_attempt")
    for row in rows:
        _row_reasons(row, reasons)
    metrics = _metrics(rows)
    if metrics is None:
        reasons.append("missing_operational_metrics")
        metrics = {
            "output_reprompt_count": 0,
            "transport_retry_count": 0,
            "provider_attempt_count": 0,
            "actual_cost_usd": None,
        }
    elif metrics["provider_attempt_count"] == 0:
        reasons.append("zero_provider_attempts")
    return {
        "model_id": model.model_id,
        "provider_model": model.provider_model,
        "eligible": not reasons,
        "reasons": sorted(set(reasons)),
        **metrics,
    }


def _row_reasons(row: dict[str, Any], reasons: list[str]) -> None:
    if row.get("status") != "completed":
        reasons.append("failed_attempt")
    admissibility = row.get("admissibility")
    if not isinstance(admissibility, dict):
        reasons.append("missing_admissibility")
        return
    if admissibility.get("tier") not in {"A", "B"}:
        reasons.append("invalid_or_nonadmitted_tier")
    if admissibility.get("tier") == "C":
        reasons.append("tier_c_attempt")
    if admissibility.get("fallback_count", 0) != 0:
        reasons.append("fallback_used")
    if "provider_or_runner_error" in admissibility.get("reasons", []):
        reasons.append("provider_error")


def _metrics(rows: list[dict[str, Any]]) -> dict[str, int | float] | None:
    if not rows:
        return None
    output_reprompts = 0
    transport_retries = 0
    provider_attempts = 0
    actual_cost = 0.0
    for row in rows:
        admissibility = row.get("admissibility")
        budget = row.get("budget_metrics")
        if not isinstance(admissibility, dict) or not isinstance(budget, dict):
            return None
        output_reprompts += _counter(admissibility, "output_reprompt_count")
        transport_retries += _counter(admissibility, "transport_retry_count")
        provider_attempts += _budget_attempts(budget)
        cost = budget.get("actual_cost_usd")
        if not isinstance(cost, (int, float)) or isinstance(cost, bool):
            return None
        if not math.isfinite(float(cost)) or cost < 0:
            return None
        actual_cost += float(cost)
    return {
        "output_reprompt_count": output_reprompts,
        "transport_retry_count": transport_retries,
        "provider_attempt_count": provider_attempts,
        "actual_cost_usd": round(actual_cost, 9),
    }


def _counter(payload: dict[str, Any], field: str) -> int:
    value = payload.get(field, 0)
    return value if isinstance(value, int) and not isinstance(value, bool) else 0


def _budget_attempts(budget: dict[str, Any]) -> int:
    total = 0
    for channel in ("strategic", "c2", "press"):
        values = budget.get(channel)
        if isinstance(values, dict):
            count = values.get("provider_attempt_count", 0)
            if isinstance(count, int) and not isinstance(count, bool) and count >= 0:
                total += count
    return total


__all__ = ["build_screening_selection"]
