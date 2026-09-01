"""Fresh-process no-model DATE World transition tracer."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .identity import canonical_hash, core_hash
from .models import DateRun, PatchInstance, TransitionResult
from .patching import instantiate_patch
from .profile import DateProfile, load_profile
from .projections import project_outcomes
from .replay import replay_run
from .tracer_fixtures import readiness_fixture
from .tracer_rejections import exercise_rejections
from .transition import admit_transition, initialize_run


@dataclass(frozen=True)
class _BranchTrace:
    run: DateRun
    weather_patch: PatchInstance
    receipt: dict[str, Any]


def _require_accepted(result: TransitionResult, label: str) -> DateRun:
    if not result.receipt.accepted:
        raise ValueError(f"DATE tracer rejected {label}: {result.receipt.reason_codes}")
    return result.run


def _package_readiness(run: DateRun) -> str:
    matches = [
        item
        for item in run.current_core()["force_packages"]
        if item["force_package_id"] == "HIM_RECAPTURE_GROUP"
    ]
    if len(matches) != 1:
        raise ValueError("DATE tracer recapture package identity is unresolved")
    return matches[0]["readiness"]


def _run_branch(profile: DateProfile, fork: DateRun, value: str) -> _BranchTrace:
    branch_event, branch_template = readiness_fixture(value)
    branch_patch = instantiate_patch(fork, branch_template)
    branch = _require_accepted(
        admit_transition(profile, fork, branch_event, branch_patch),
        f"{value} branch fixture",
    )
    weather_patch = instantiate_patch(
        branch, profile.patch_template("PATCH_WX_RIDGE_DEGRADE_01")
    )
    weather = _require_accepted(
        admit_transition(
            profile,
            branch,
            profile.event_template("WX_RIDGE_FRONT_01"),
            weather_patch,
        ),
        f"{value} weather",
    )
    final = _require_accepted(
        admit_transition(
            profile,
            weather,
            profile.event_template("OBS_WX_RIDGE_CONFIRMED_01"),
        ),
        f"{value} confirmation",
    )
    replayed = replay_run(profile, final)
    replay_matched = (
        core_hash(replayed.current_core()) == core_hash(final.current_core())
        and replayed.ledger() == final.ledger()
        and project_outcomes(replayed.current_core())
        == project_outcomes(final.current_core())
    )
    receipt = {
        "core_hash": core_hash(final.current_core()),
        "core_version": final.current_core()["core_version"],
        "ledger_hash": canonical_hash(final.ledger()),
        "ledger_template_ids": [item["template_id"] for item in final.ledger()],
        "outcomes": project_outcomes(final.current_core()),
        "readiness": _package_readiness(final),
        "replay_matched": replay_matched,
        "weather_patch_instance_id": weather_patch.patch_instance_id,
        "weather_template_hash": weather_patch.template_hash,
    }
    return _BranchTrace(run=final, weather_patch=weather_patch, receipt=receipt)


def run_tracer(profile_path: Path, executor_revision: str) -> dict[str, Any]:
    if len(executor_revision) != 40 or any(
        character not in "0123456789abcdef" for character in executor_revision
    ):
        raise ValueError("DATE tracer executor revision is invalid")
    profile = load_profile(profile_path)
    initial = initialize_run(profile, "date-world-tracer-001")
    initial_hash = core_hash(initial.current_core())
    forecast = _require_accepted(
        admit_transition(
            profile,
            initial,
            profile.event_template("OBS_WX_RIDGE_FORECAST_01"),
        ),
        "forecast",
    )
    ready = _run_branch(profile, forecast, "ready")
    delayed = _run_branch(profile, forecast, "delayed")
    receipt: dict[str, Any] = {
        "schema_version": "date-tracer-receipt.v0.1",
        "tracer_id": "d62-date-world-transition-v1",
        "status": "passed",
        "executor_revision": executor_revision,
        "profile_id": profile.profile_id,
        "profile_version": profile.profile_version,
        "profile_hash": profile.content_hash,
        "forecast_core_unchanged": core_hash(forecast.current_core()) == initial_hash,
        "weather_template_hash_equal": (
            ready.weather_patch.template_hash == delayed.weather_patch.template_hash
        ),
        "weather_instance_ids_distinct": (
            ready.weather_patch.patch_instance_id
            != delayed.weather_patch.patch_instance_id
        ),
        "branches": {"ready": ready.receipt, "delayed": delayed.receipt},
        "rejections": exercise_rejections(profile, forecast, ready.run),
    }
    receipt["receipt_hash"] = canonical_hash(receipt)
    return receipt


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: date_world.tracer PROFILE EXECUTOR_REVISION")
    receipt = run_tracer(Path(sys.argv[1]), sys.argv[2])
    sys.stdout.write(json.dumps(receipt, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
