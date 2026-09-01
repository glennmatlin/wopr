"""Fail-closed DATE State Patch validation."""

from __future__ import annotations

from typing import Any

from .identity import canonical_hash, core_hash
from .models import DateRun, PatchInstance
from .profile import DateProfile

PATCH_FIELDS = {"template_id", "effective_hour", "causal_parent_ids", "operations"}


def _text_list(value: object) -> bool:
    return isinstance(value, list) and all(
        isinstance(item, str) and item for item in value
    )


def validate_patch_envelope(patch: PatchInstance) -> str | None:
    template = patch.template()
    if set(template) != PATCH_FIELDS:
        return "invalid_envelope"
    if not isinstance(template.get("template_id"), str):
        return "invalid_envelope"
    hour = template.get("effective_hour")
    if isinstance(hour, bool) or not isinstance(hour, int):
        return "invalid_envelope"
    parents = template.get("causal_parent_ids")
    if not isinstance(parents, list) or not _text_list(parents):
        return "invalid_envelope"
    if len(parents) != len(set(parents)):
        return "invalid_envelope"
    operations = template.get("operations")
    if not isinstance(operations, list) or not operations:
        return "invalid_envelope"
    if any(not isinstance(operation, dict) for operation in operations):
        return "invalid_envelope"
    return None


def validate_patch_references(
    run: DateRun, event: dict[str, Any], patch: PatchInstance
) -> str | None:
    parents = patch.template()["causal_parent_ids"]
    ledger_ids = {entry["template_id"] for entry in run.ledger()}
    if event["template_id"] not in parents or not set(parents) <= (
        ledger_ids | {event["template_id"]}
    ):
        return "causal_mismatch"
    return None


def _authored_identity(
    profile: DateProfile, event: dict[str, Any], patch: PatchInstance
) -> str | None:
    template = patch.template()
    try:
        authored = profile.patch_template(patch.template_id)
    except ValueError:
        authored = None
    if event["source"] == "authored_msel" and template != authored:
        authored_ops = authored.get("operations") if authored else None
        if isinstance(authored_ops, list) and isinstance(
            template.get("operations"), list
        ):
            if len(template["operations"]) < len(authored_ops):
                return "partial_patch"
        return "template_mismatch"
    if event["source"] != "authored_msel" and authored is not None:
        return "template_mismatch"
    return None


def _binding(run: DateRun, patch: PatchInstance) -> str | None:
    template_hash = canonical_hash(patch.template())
    binding = {
        "base_core_hash": patch.base_core_hash,
        "base_core_version": patch.base_core_version,
        "run_id": patch.run_id,
        "template_hash": template_hash,
        "template_id": patch.template_id,
    }
    if patch.template_hash != template_hash:
        return "template_mismatch"
    if patch.patch_instance_id != canonical_hash(binding) or patch.run_id != run.run_id:
        return "template_mismatch"
    core = run.current_core()
    if patch.base_core_version != core["core_version"]:
        return "stale_core"
    if patch.base_core_hash != core_hash(core):
        return "stale_core"
    return None


def validate_patch_identity(
    profile: DateProfile,
    run: DateRun,
    event: dict[str, Any],
    patch: PatchInstance,
) -> str | None:
    template = patch.template()
    if event["patch_template_id"] != patch.template_id:
        return "template_mismatch"
    if template["template_id"] != patch.template_id:
        return "template_mismatch"
    if template["effective_hour"] != event["episode_hour"]:
        return "template_mismatch"
    return _authored_identity(profile, event, patch) or _binding(run, patch)


__all__ = [
    "validate_patch_envelope",
    "validate_patch_identity",
    "validate_patch_references",
]
