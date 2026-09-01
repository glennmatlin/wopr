"""Frozen factorial study manifest loading and identity hashing."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from .manifest_overlay import validate_overlay
from .manifest_policy import (
    load_request_budget,
    manifest_positive_int,
    manifest_text,
    optional_choice,
    optional_sha256,
    optional_text,
    request_budget_payload,
)
from .manifest_types import (
    StudyCell,  # noqa: F401
    StudyCondition,  # noqa: F401
    StudyManifest,
    StudyModel,  # noqa: F401
    StudyRequestBudget,  # noqa: F401
)
from .manifest_validation import (
    load_conditions,
    load_models,
    load_seeds,
    validate_factorial_conditions,
)
from .manifest_variants import STUDY_VARIANTS

SCHEMA_VERSION = 1


def load_study_manifest(payload: Any) -> StudyManifest:
    if not isinstance(payload, dict):
        raise ValueError("Study manifest must be an object")
    required = {
        "schema_version",
        "study_id",
        "protocol_revision",
        "source_revision",
        "players",
        "max_turns",
        "seeds",
        "conditions",
        "models",
    }
    optional = {
        "request_budget",
        "study_variant",
        "preflight_receipt_hash",
        "preflight_approval_status",
        "preflight_receipt_path",
        "preflight_candidate_manifest_path",
        "preflight_candidate_manifest_hash",
        "preflight_executor_revision",
        "execution_manifest_hash",
        "execution_approval_hash",
        "execution_executor_revision",
        "overlay",
        "overlay_pack_hash",
    }
    if not required <= set(payload) or set(payload) - required - optional:
        raise ValueError("Study manifest fields are invalid")
    if payload["schema_version"] != SCHEMA_VERSION:
        raise ValueError("Study manifest schema_version is invalid")
    request_budget = (
        load_request_budget(payload["request_budget"])
        if "request_budget" in payload
        else None
    )
    receipt_hash = optional_sha256(payload, "preflight_receipt_hash")
    approval_status = optional_choice(
        payload, "preflight_approval_status", {"pending_owner", "approved"}
    )
    study_variant = optional_choice(payload, "study_variant", STUDY_VARIANTS)
    overlay = optional_choice(payload, "overlay", {"off", "neutral_staff"})
    manifest = StudyManifest(
        study_id=manifest_text(payload["study_id"], "study_id"),
        protocol_revision=manifest_text(
            payload["protocol_revision"], "protocol_revision"
        ),
        source_revision=manifest_text(payload["source_revision"], "source_revision"),
        players=manifest_positive_int(payload["players"], "players", minimum=2),
        max_turns=manifest_positive_int(payload["max_turns"], "max_turns"),
        seeds=load_seeds(payload["seeds"]),
        conditions=load_conditions(payload["conditions"]),
        models=load_models(payload["models"]),
        study_variant=study_variant or "full_factorial",
        overlay=overlay or "off",
        overlay_pack_hash=optional_sha256(payload, "overlay_pack_hash"),
        request_budget=request_budget,
        preflight_receipt_hash=receipt_hash,
        preflight_approval_status=approval_status,
        preflight_receipt_path=optional_text(payload, "preflight_receipt_path"),
        preflight_candidate_manifest_path=optional_text(
            payload, "preflight_candidate_manifest_path"
        ),
        preflight_candidate_manifest_hash=optional_sha256(
            payload, "preflight_candidate_manifest_hash"
        ),
        preflight_executor_revision=optional_text(
            payload, "preflight_executor_revision"
        ),
        execution_manifest_hash=optional_sha256(payload, "execution_manifest_hash"),
        execution_approval_hash=optional_sha256(payload, "execution_approval_hash"),
        execution_executor_revision=optional_text(
            payload, "execution_executor_revision"
        ),
    )
    validate_factorial_conditions(manifest.conditions, manifest.study_variant)
    validate_overlay(manifest)
    return manifest


def manifest_payload(manifest: StudyManifest) -> dict[str, Any]:
    payload = {
        "schema_version": SCHEMA_VERSION,
        "study_id": manifest.study_id,
        "protocol_revision": manifest.protocol_revision,
        "source_revision": manifest.source_revision,
        "players": manifest.players,
        "max_turns": manifest.max_turns,
        "seeds": list(manifest.seeds),
        "conditions": [condition.__dict__ for condition in manifest.conditions],
        "models": [model.__dict__ for model in manifest.models],
    }
    if manifest.request_budget is not None:
        payload["request_budget"] = request_budget_payload(manifest.request_budget)
    if manifest.study_variant != "full_factorial":
        payload["study_variant"] = manifest.study_variant
    if manifest.overlay != "off":
        payload["overlay"] = manifest.overlay
    if manifest.overlay_pack_hash:
        payload["overlay_pack_hash"] = manifest.overlay_pack_hash
    for field in (
        "preflight_receipt_hash",
        "preflight_approval_status",
        "preflight_receipt_path",
        "preflight_candidate_manifest_path",
        "preflight_candidate_manifest_hash",
        "preflight_executor_revision",
        "execution_manifest_hash",
        "execution_approval_hash",
        "execution_executor_revision",
    ):
        if value := getattr(manifest, field):
            payload[field] = value
    return payload


def manifest_hash(manifest: StudyManifest) -> str:
    encoded = json.dumps(
        manifest_payload(manifest), sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()
