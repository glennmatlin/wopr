"""Frozen Room Instrument study is receipt-bound and approved."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

from nuclear_war_contest.manifest import load_study_manifest
from nuclear_war_contest.preflight import (
    candidate_manifest_hash,
    load_candidate_manifest,
)
from nuclear_war_contest.preflight_study_binding import validate_study_binding

DOCS = Path(__file__).resolve().parents[2] / "docs" / "contest"


def test_frozen_room_instrument_study_is_approved_and_bound() -> None:
    study_path = DOCS / "STUDY_MANIFEST.room_instrument.json"
    manifest_path = DOCS / "MODEL_MANIFEST.json"
    receipt_path = DOCS / "MODEL_PREFLIGHT_RECEIPT.live.json"
    study = load_study_manifest(json.loads(study_path.read_text(encoding="utf-8")))
    candidate = load_candidate_manifest(
        json.loads(manifest_path.read_text(encoding="utf-8")),
        base_dir=manifest_path.parent,
    )
    validate_study_binding(study, candidate)

    assert study.preflight_approval_status == "approved"
    assert len(study.cells) == 18
    assert study.preflight_executor_revision == (
        "09421afee7a0c763127d0ec5e460f7d94a596bdc"
    )
    assert candidate_manifest_hash(candidate) == study.preflight_candidate_manifest_hash
    assert sha256(receipt_path.read_bytes()).hexdigest() == study.preflight_receipt_hash
    assert json.loads(receipt_path.read_text(encoding="utf-8"))["status"] == "approved"
