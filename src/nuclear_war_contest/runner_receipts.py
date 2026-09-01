"""Receipt and filesystem helpers for resumable contest attempts."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from typing import Any

from .identity import condition_hash, model_manifest_hash
from .manifest import manifest_hash
from .manifest_policy import request_budget_payload
from .manifest_types import StudyCell, StudyCondition, StudyManifest, StudyModel
from .overlay_packs import overlay_pack_hash


def attempt_id(manifest: StudyManifest, cell: StudyCell) -> str:
    source = f"{manifest_hash(manifest)}:{cell.cell_id}"
    return sha256(source.encode("utf-8")).hexdigest()[:20]


def ledger_start(
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
) -> dict[str, Any]:
    condition = _condition(manifest, cell.condition_id)
    model = _model(manifest, cell.model_id)
    return {
        "attempt_id": attempt,
        "status": "started",
        "study_id": manifest.study_id,
        "manifest_hash": manifest_hash(manifest),
        "source_revision": manifest.source_revision,
        "cell_id": cell.cell_id,
        "condition_id": cell.condition_id,
        "model_id": cell.model_id,
        "seed": cell.seed,
        **_provenance(manifest, condition, model),
    }


def attempt_row(
    manifest: StudyManifest,
    cell: StudyCell,
    attempt: str,
    measures: dict[str, Any] | None,
    admissibility: dict[str, Any],
    budget_metrics: dict[str, Any] | None = None,
    prior_budget_metrics: dict[str, Any] | None = None,
    prior_attempt_receipt_path: str | None = None,
    prior_attempt_receipt_sha256: str | None = None,
) -> dict[str, Any]:
    condition = _condition(manifest, cell.condition_id)
    model = _model(manifest, cell.model_id)
    row = {
        "status": "completed" if measures is not None else "failed",
        "study_id": manifest.study_id,
        "source_revision": manifest.source_revision,
        "manifest_hash": manifest_hash(manifest),
        "attempt_id": attempt,
        "preflight_receipt_hash": manifest.preflight_receipt_hash,
        "preflight_approval_status": manifest.preflight_approval_status,
        "cell_id": cell.cell_id,
        "condition_id": cell.condition_id,
        "model_id": cell.model_id,
        "seed": cell.seed,
        "communication": condition.communication,
        "authority": condition.authority,
        "condition_snapshot": {
            "authority_parameters": condition.authority_parameters,
            "press_passes": condition.press_passes,
        },
        "backend": model.backend,
        "provider": model.provider,
        "role_prompt_hashes": model.role_prompt_hashes,
        "overlay": manifest.overlay,
        "request_policy": _request_policy(manifest, model),
        "execution_manifest_hash": manifest.execution_manifest_hash,
        "execution_approval_hash": manifest.execution_approval_hash,
        "execution_executor_revision": manifest.execution_executor_revision,
        "prior_budget_metrics": prior_budget_metrics,
        "prior_attempt_receipt_path": prior_attempt_receipt_path,
        "prior_attempt_receipt_sha256": prior_attempt_receipt_sha256,
        "condition_hash": condition_hash(condition),
        "model_manifest_hash": model_manifest_hash(model),
        "admissibility": admissibility,
    }
    if manifest.overlay != "off":
        row["overlay_pack_hash"] = overlay_pack_hash()
    if measures is not None:
        row["measures"] = measures
    if budget_metrics is not None:
        row["budget_metrics"] = budget_metrics
    return row


def read_attempt(
    out_dir: Path,
    attempt: str,
    manifest: StudyManifest | None = None,
    cell: StudyCell | None = None,
) -> dict[str, Any]:
    path = out_dir / "attempts" / attempt / "attempt.json"
    if not path.exists():
        raise ValueError(f"Terminal attempt is missing receipt: {attempt}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Attempt receipt must be an object: {attempt}")
    if manifest is not None and cell is not None:
        from .receipt_validation import validate_attempt_receipt

        validate_attempt_receipt(payload, out_dir, manifest, cell, attempt)
    return payload


def _provenance(
    manifest: StudyManifest,
    condition: StudyCondition,
    model: StudyModel,
) -> dict[str, Any]:
    return {
        "condition_hash": condition_hash(condition),
        "model_manifest_hash": model_manifest_hash(model),
        "backend": model.backend,
        "provider": model.provider,
        "role_prompt_hashes": model.role_prompt_hashes,
        "request_policy": _request_policy(manifest, model),
    }


def _condition(manifest: StudyManifest, condition_id: str) -> StudyCondition:
    return next(
        item for item in manifest.conditions if item.condition_id == condition_id
    )


def _model(manifest: StudyManifest, model_id: str) -> StudyModel:
    return next(item for item in manifest.models if item.model_id == model_id)


def _request_policy(manifest: StudyManifest, model: StudyModel) -> dict[str, Any]:
    policy: dict[str, Any] = {
        "max_retries": model.max_retries,
        "client": model.client,
        "preflight_receipt_hash": manifest.preflight_receipt_hash,
        "preflight_approval_status": manifest.preflight_approval_status,
        "preflight_receipt_path": manifest.preflight_receipt_path,
        "preflight_candidate_manifest_path": manifest.preflight_candidate_manifest_path,
        "preflight_candidate_manifest_hash": manifest.preflight_candidate_manifest_hash,
    }
    if manifest.request_budget is not None:
        policy["channel_caps"] = request_budget_payload(manifest.request_budget)
    return policy
