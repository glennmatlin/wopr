"""Fixed control and authorization checks for model screening."""

from __future__ import annotations

from .screening_types import ScreeningManifest


def validate_screening_manifest(manifest: ScreeningManifest) -> None:
    _validate_seed_assignment(manifest)
    _validate_selection(manifest)
    _validate_controls(manifest)
    _validate_authorization(manifest)
    _validate_retries(manifest)


def _validate_seed_assignment(manifest: ScreeningManifest) -> None:
    if manifest.screening_seeds != (101, 102, 103) or manifest.study_seeds != (
        51,
        52,
        53,
        54,
        55,
    ):
        raise ValueError("Screening seed assignments are invalid")


def _validate_selection(manifest: ScreeningManifest) -> None:
    if manifest.selection_status != "screening_only":
        raise ValueError("Screening manifest must remain screening_only")
    if manifest.full_design_model_selection != "deferred_after_screen":
        raise ValueError("Screening full-design selection must remain deferred")


def _validate_controls(manifest: ScreeningManifest) -> None:
    if (
        manifest.mode != "press_light"
        or manifest.players != 4
        or manifest.max_turns != 3
        or manifest.temperature != 0.7
        or manifest.max_tokens != 512
        or manifest.reasoning_enabled is not False
        or manifest.stream is not True
    ):
        raise ValueError("Screening gameplay controls are invalid")


def _validate_authorization(manifest: ScreeningManifest) -> None:
    if manifest.approval_status != "pending_owner" or manifest.network_calls != 0:
        raise ValueError("Screening manifest cannot authorize network calls")
    if (
        manifest.credentials_read
        or manifest.owner_total_cap_usd != 1000.0
        or manifest.owner_total_cap_usd <= 0
    ):
        raise ValueError("Screening spend boundary is invalid")


def _validate_retries(manifest: ScreeningManifest) -> None:
    if manifest.output_retries != 1 or manifest.transport_retry_margin != 2:
        raise ValueError("Screening retry controls are invalid")
    if any(model.max_retries != manifest.output_retries for model in manifest.models):
        raise ValueError("Screening model retries are not frozen")


__all__ = ["validate_screening_manifest"]
