"""Pure DATE World transition admission."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .identity import canonical_hash, core_hash
from .models import DateRun, PatchInstance, TransitionResult, ValidationReceipt
from .operations import AdmissionError, apply_operations
from .profile import DateProfile
from .transition_validation import validate_transition


def initialize_run(profile: DateProfile, run_id: str) -> DateRun:
    if not isinstance(run_id, str) or not run_id:
        raise ValueError("DATE run_id is invalid")
    core = profile.initial_core()
    return DateRun(
        run_id=run_id,
        profile_hash=profile.content_hash,
        _initial_core=deepcopy(core),
        _current_core=core,
    )


def _make_receipt(
    run: DateRun,
    event_template: dict[str, Any],
    patch_instance: PatchInstance | None,
    accepted: bool,
    reason_codes: tuple[str, ...],
    next_core: dict[str, Any],
) -> ValidationReceipt:
    before = run.current_core()
    template_id = event_template.get("template_id")
    payload = {
        "accepted": accepted,
        "core_hash_after": core_hash(next_core),
        "core_hash_before": core_hash(before),
        "core_version_after": next_core["core_version"],
        "core_version_before": before["core_version"],
        "event_template_hash": canonical_hash(event_template),
        "event_template_id": (
            template_id if isinstance(template_id, str) else "<invalid>"
        ),
        "patch_instance_id": (
            patch_instance.patch_instance_id if patch_instance is not None else None
        ),
        "reason_codes": reason_codes,
        "run_id": run.run_id,
    }
    return ValidationReceipt(receipt_id=canonical_hash(payload), **payload)


def _reject(
    run: DateRun,
    event_template: dict[str, Any],
    patch_instance: PatchInstance | None,
    reason_code: str,
) -> TransitionResult:
    core = run.current_core()
    receipt = _make_receipt(
        run, event_template, patch_instance, False, (reason_code,), core
    )
    next_run = DateRun(
        run_id=run.run_id,
        profile_hash=run.profile_hash,
        _initial_core=run.initial_core(),
        _current_core=core,
        _ledger=run.ledger(),
        _receipts=(*run.receipts(), receipt),
        _accepted_transitions=run.accepted_transitions(),
    )
    return TransitionResult(run=next_run, receipt=receipt)


def admit_transition(
    profile: DateProfile,
    run: DateRun,
    event_template: dict[str, Any],
    patch_instance: PatchInstance | None = None,
) -> TransitionResult:
    if run.profile_hash != profile.content_hash:
        raise ValueError("DATE run profile identity does not match")
    if reason := validate_transition(profile, run, event_template, patch_instance):
        return _reject(run, event_template, patch_instance, reason)
    core = run.current_core()
    if patch_instance is None:
        next_core = core
    else:
        patch_template = patch_instance.template()
        try:
            next_core = apply_operations(core, patch_template.get("operations"))
        except AdmissionError as error:
            return _reject(run, event_template, patch_instance, error.reason_code)
    receipt = _make_receipt(run, event_template, patch_instance, True, (), next_core)
    ledger_entry = deepcopy(event_template)
    ledger_entry.update(
        {
            "run_id": run.run_id,
            "entry_index": len(run.ledger()),
            "core_version_before": core["core_version"],
            "core_version_after": next_core["core_version"],
            "validator_receipt_id": receipt.receipt_id,
        }
    )
    transition = {
        "event_template": deepcopy(event_template),
        "patch_instance": deepcopy(patch_instance),
    }
    next_run = DateRun(
        run_id=run.run_id,
        profile_hash=run.profile_hash,
        _initial_core=run.initial_core(),
        _current_core=next_core,
        _ledger=(*run.ledger(), ledger_entry),
        _receipts=(*run.receipts(), receipt),
        _accepted_transitions=(*run.accepted_transitions(), transition),
    )
    return TransitionResult(run=next_run, receipt=receipt)


__all__ = ["admit_transition", "initialize_run"]
