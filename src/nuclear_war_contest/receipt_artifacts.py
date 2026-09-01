"""Filesystem and prior-chain validation for contest receipts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from nuclear_war_concordia.press_artifacts import validate_press_artifact
from nuclear_war_env.llm_trace_artifacts import read_trace_artifact
from nuclear_war_env.replay import read_replay

from .admissibility import validate_result_artifacts
from .manifest_types import StudyManifest
from .measures import derive_measures
from .receipt_prior_validation import validate_prior_receipt
from .runner_budget import (
    enforce_channel_caps,
    validate_budget_metrics,
    validate_channel_metrics,
)

ARTIFACT_KEYS = {
    "replay_path",
    "trace_path",
    "c2_path",
    "summary_path",
    "config_path",
    "agent_metadata_path",
    "runtime_path",
}


def validate_artifact_contents(
    payload: dict[str, Any], root: Path, manifest: StudyManifest
) -> None:
    artifacts = payload["artifacts"]
    replay = read_replay(safe_child(root, artifacts["replay_path"], "replay artifact"))
    trace = read_trace_artifact(
        safe_child(root, artifacts["trace_path"], "trace artifact"), replay
    )
    c2 = read_json(safe_child(root, artifacts["c2_path"], "C2 artifact"))
    summary = read_json(safe_child(root, artifacts["summary_path"], "summary artifact"))
    config = read_json(safe_child(root, artifacts["config_path"], "config artifact"))
    result: dict[str, Any] = {
        "replay": replay,
        "trace_artifact": trace,
        "c2_artifact": c2,
        "config_snapshot": config,
        "summary": summary,
    }
    if payload.get("budget_metrics") != summary.get("budget_metrics"):
        raise ValueError("Attempt receipt budget metrics do not match summary")
    if "press_path" in artifacts:
        press = read_json(safe_child(root, artifacts["press_path"], "press artifact"))
        validate_press_artifact(press, replay)
        result["press_artifact"] = press
    validate_result_artifacts(result)
    validate_channel_metrics(result)
    if manifest.request_budget is not None:
        prior = payload.get("prior_budget_metrics")
        validate_budget_metrics(result, initial_metrics=prior)
        enforce_channel_caps(result, manifest.request_budget, initial_metrics=prior)
    if payload.get("measures") != derive_measures(result):
        raise ValueError("Attempt receipt measures do not match artifacts")


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Artifact must be an object: {path}")
    return value


def safe_child(root: Path, relative: str, label: str) -> Path:
    path = Path(relative)
    resolved_root = root.resolve()
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Attempt receipt {label} path is invalid")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(resolved_root):
        raise ValueError(f"Attempt receipt {label} path is invalid")
    return resolved


__all__ = [
    "ARTIFACT_KEYS",
    "read_json",
    "safe_child",
    "validate_artifact_contents",
    "validate_prior_receipt",
]
