"""Required failure matrix for the no-model DATE tracer."""

from __future__ import annotations

from dataclasses import replace
from typing import Any

from .identity import core_hash
from .models import DateRun
from .patching import instantiate_patch
from .profile import DateProfile
from .tracer_fixtures import fixture_event, operation_patch
from .tracer_operation_rejections import exercise_operation_rejections
from .transition import admit_transition


def retain_rejection(
    profile: DateProfile,
    run: DateRun,
    case_id: str,
    event: dict[str, Any],
    patch_template: dict[str, Any] | None = None,
    *,
    patch_run: DateRun | None = None,
) -> dict[str, str]:
    patch = (
        instantiate_patch(patch_run or run, patch_template)
        if patch_template is not None
        else None
    )
    before_hash = core_hash(run.current_core())
    before_ledger = run.ledger()
    result = admit_transition(profile, run, event, patch)
    if result.receipt.accepted:
        raise ValueError(f"DATE tracer unexpectedly accepted {case_id}")
    if core_hash(result.run.current_core()) != before_hash:
        raise ValueError(f"DATE rejection changed Core for {case_id}")
    if result.run.ledger() != before_ledger:
        raise ValueError(f"DATE rejection changed ledger for {case_id}")
    return {
        "case_id": case_id,
        "reason_code": result.receipt.reason_codes[0],
        "receipt_id": result.receipt.receipt_id,
    }


def exercise_rejections(
    profile: DateProfile, fork: DateRun, final: DateRun
) -> list[dict[str, str]]:
    invalid = fixture_event("INVALID_ENVELOPE", hour=7)
    invalid.pop("content")
    causal = fixture_event("CAUSAL_MISMATCH", hour=7, parents=["MISSING_PARENT"])
    terminal_core = final.current_core()
    terminal_core["terminal_state"] = "terminated"
    terminal = replace(final, _current_core=terminal_core)
    mismatch = profile.event_template("WX_RIDGE_FRONT_01")
    mismatch["content"] = "Altered authored content."
    stale_event = fixture_event("STALE_CORE", hour=7, patch_id="PATCH_STALE_CORE")
    stale_template = operation_patch(
        stale_event,
        {
            "operation": "set_force_package_readiness",
            "force_package_id": "HIM_RECAPTURE_GROUP",
            "expected": "prepared",
            "value": "ready",
        },
    )
    partial = fixture_event("PARTIAL_PATCH", hour=7, patch_id="PATCH_PARTIAL")
    results = [
        retain_rejection(profile, final, "INVALID_ENVELOPE", invalid),
        retain_rejection(
            profile,
            fork,
            "DUPLICATE_ID",
            profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
        ),
        retain_rejection(
            profile,
            final,
            "UNKNOWN_ACTOR",
            fixture_event("UNKNOWN_ACTOR", hour=7, affected_ids=["ACTOR_UNEARNED"]),
        ),
        retain_rejection(profile, final, "CAUSAL_MISMATCH", causal),
        retain_rejection(
            profile,
            final,
            "RETROACTIVE_TIME",
            fixture_event("RETROACTIVE_TIME", hour=0),
        ),
        retain_rejection(
            profile, terminal, "TERMINAL_WORLD", fixture_event("TERMINAL_WORLD", hour=7)
        ),
        retain_rejection(
            profile,
            fork,
            "TEMPLATE_MISMATCH",
            mismatch,
            profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01"),
        ),
        retain_rejection(
            profile, final, "STALE_CORE", stale_event, stale_template, patch_run=fork
        ),
        retain_rejection(profile, final, "PARTIAL_PATCH", partial),
    ]
    return [*results, *exercise_operation_rejections(profile, final)]


__all__ = ["exercise_rejections", "retain_rejection"]
