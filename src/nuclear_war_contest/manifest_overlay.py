"""Overlay field rules for study manifests."""

from __future__ import annotations

from .manifest_types import StudyManifest
from .overlay_packs import overlay_pack_hash


def validate_overlay(manifest: StudyManifest) -> None:
    if manifest.study_variant == "room_instrument_demo":
        if manifest.overlay != "neutral_staff":
            raise ValueError("room_instrument_demo requires overlay neutral_staff")
        if manifest.overlay_pack_hash != overlay_pack_hash():
            raise ValueError("overlay_pack_hash does not match Neutral Staff")
        return
    if manifest.overlay != "off":
        raise ValueError("Sounding study variants require overlay off")
    if manifest.overlay_pack_hash is not None:
        raise ValueError("Sounding study variants must omit overlay_pack_hash")


__all__ = ["validate_overlay"]
