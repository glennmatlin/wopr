"""No-model proposal bridge development fixture loading."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json
from nuclear_war_contest.date_world.profile import DateProfile

from .proposal_bridge_fixture_references import (
    validate_bridge_fixture_references,
)
from .proposal_bridge_fixture_validation import validate_bridge_fixture_shape
from .proposal_bridge_models import ProposalBridgeFixture

D64_PROFILE_HASH = "64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477"
D68_RECEIPT_HASH = "7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186"
D68_RUN_HASH = "08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6"


def load_proposal_bridge_fixture(
    path: Path, cycle_receipt_path: Path, profile: DateProfile
) -> ProposalBridgeFixture:
    payload = load_strict_json(path)
    cycle = _load_d68_receipt(cycle_receipt_path)
    if not isinstance(payload, dict):
        raise ValueError("invalid_envelope: proposal bridge must be an object")
    validate_bridge_fixture_shape(payload)
    if profile.content_hash != D64_PROFILE_HASH:
        raise ValueError("identity_mismatch: D64 profile identity is invalid")
    identities = {
        "cycle_receipt_hash": D68_RECEIPT_HASH,
        "cycle_run_hash": D68_RUN_HASH,
        "date_profile_hash": D64_PROFILE_HASH,
    }
    if any(payload.get(key) != value for key, value in identities.items()):
        raise ValueError("identity_mismatch: proposal bridge upstream identity changed")
    validate_bridge_fixture_references(payload, cycle, profile)
    return ProposalBridgeFixture(
        fixture_id=payload["fixture_id"],
        cycle_receipt_hash=D68_RECEIPT_HASH,
        date_profile_hash=D64_PROFILE_HASH,
        content_hash=canonical_hash(payload),
        _payload=deepcopy(payload),
        _cycle_receipt=deepcopy(cycle),
    )


def _load_d68_receipt(path: Path) -> dict[str, Any]:
    payload = load_strict_json(path)
    if not isinstance(payload, dict):
        raise ValueError("invalid_envelope: D68 receipt must be an object")
    embedded_hash = payload.get("receipt_hash")
    body = {key: value for key, value in payload.items() if key != "receipt_hash"}
    run = payload.get("run")
    valid = (
        embedded_hash == D68_RECEIPT_HASH
        and canonical_hash(body) == D68_RECEIPT_HASH
        and payload.get("run_hash") == D68_RUN_HASH
        and isinstance(run, dict)
        and run.get("decision_supported") is True
        and run.get("world_effects_admitted") is False
    )
    if not valid:
        raise ValueError("identity_mismatch: exact D68 receipt is required")
    return payload


__all__ = ["ProposalBridgeFixture", "load_proposal_bridge_fixture"]
