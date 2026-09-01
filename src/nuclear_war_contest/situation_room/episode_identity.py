"""Exact upstream identities for the deterministic two-cycle tracer."""

from __future__ import annotations

from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash

CYCLE1_RECEIPT_HASH = "7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186"
CYCLE1_RUN_HASH = "08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6"
BRIDGE_RECEIPT_HASH = "cf78c92190e8b2739923c0977a0af316b332643b563d0ad4818b13048c726ec4"
BRIDGE_RUN_HASH = "d43ad8544af90f8e44736133c11b6e8443275c901049ffb0800efd2e0978b996"
BRIDGE_FIXTURE_HASH = "4b47bc86dad3226692146cc92b21f7b3da61a5919b87ce26924514d7f44ce465"
DATE_PROFILE_HASH = "64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477"
DATE_RECEIPT_HASH = "4a582d72b6d8ff753c3e06adea4d36aef3c3b39b5284e4050ce9ed35e39815e3"


def validate_upstream_receipts(receipts: dict[str, dict[str, Any]]) -> None:
    expected = {
        "cycle1": (CYCLE1_RECEIPT_HASH, CYCLE1_RUN_HASH),
        "bridge": (BRIDGE_RECEIPT_HASH, BRIDGE_RUN_HASH),
        "date": (DATE_RECEIPT_HASH, None),
    }
    for key, (receipt_hash, run_hash) in expected.items():
        payload = receipts[key]
        retained = payload.get("receipt_hash")
        without_hash = {
            name: value for name, value in payload.items() if name != "receipt_hash"
        }
        if retained != receipt_hash or canonical_hash(without_hash) != receipt_hash:
            raise ValueError(f"identity_mismatch: exact {key} receipt is invalid")
        if run_hash is not None and payload.get("run_hash") != run_hash:
            raise ValueError(f"identity_mismatch: exact {key} run is invalid")
    if receipts["bridge"].get("fixture_hash") != BRIDGE_FIXTURE_HASH:
        raise ValueError("identity_mismatch: exact bridge fixture is invalid")
    if receipts["date"].get("profile_hash") != DATE_PROFILE_HASH:
        raise ValueError("identity_mismatch: exact DATE profile is invalid")


__all__ = [
    "BRIDGE_FIXTURE_HASH",
    "BRIDGE_RECEIPT_HASH",
    "BRIDGE_RUN_HASH",
    "CYCLE1_RECEIPT_HASH",
    "CYCLE1_RUN_HASH",
    "DATE_PROFILE_HASH",
    "DATE_RECEIPT_HASH",
    "validate_upstream_receipts",
]
