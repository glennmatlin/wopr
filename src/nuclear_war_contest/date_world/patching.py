"""Run-bound DATE State Patch instances."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .identity import canonical_hash, core_hash
from .models import DateRun, PatchInstance


def instantiate_patch(run: DateRun, patch_template: dict[str, Any]) -> PatchInstance:
    template_id = patch_template.get("template_id")
    if not isinstance(template_id, str) or not template_id:
        raise ValueError("DATE patch template identity is invalid")
    core = run.current_core()
    template_hash = canonical_hash(patch_template)
    binding = {
        "base_core_hash": core_hash(core),
        "base_core_version": core["core_version"],
        "run_id": run.run_id,
        "template_hash": template_hash,
        "template_id": template_id,
    }
    return PatchInstance(
        patch_instance_id=canonical_hash(binding),
        run_id=run.run_id,
        template_id=template_id,
        template_hash=template_hash,
        base_core_version=core["core_version"],
        base_core_hash=core_hash(core),
        _template=deepcopy(patch_template),
    )


__all__ = ["instantiate_patch"]
