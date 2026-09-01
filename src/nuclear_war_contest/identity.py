"""Stable hashes for study conditions, models, and execution provenance."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from .manifest_types import StudyCondition, StudyModel


def condition_hash(condition: StudyCondition) -> str:
    return canonical_hash(
        {
            "condition_id": condition.condition_id,
            "communication": condition.communication,
            "authority": condition.authority,
            "authority_parameters": condition.authority_parameters,
            "press_passes": condition.press_passes,
        }
    )


def model_manifest_hash(model: StudyModel) -> str:
    return canonical_hash(
        {
            "model_id": model.model_id,
            "backend": model.backend,
            "provider": model.provider,
            "client": model.client,
            "max_retries": model.max_retries,
            "role_prompt_hashes": model.role_prompt_hashes,
        }
    )


def canonical_hash(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


__all__ = ["canonical_hash", "condition_hash", "model_manifest_hash"]
