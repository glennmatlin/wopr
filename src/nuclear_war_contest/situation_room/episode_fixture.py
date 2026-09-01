"""Strict loading of one deterministic two-cycle episode fixture."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from nuclear_war_contest.date_world.identity import canonical_hash, load_strict_json
from nuclear_war_contest.date_world.profile import load_profile

from .charter import load_us_charter
from .cycle_fixture import load_us_cycle_fixture, load_us_cycle_fixture_payload
from .episode_artifact_validation import ARTIFACT_KEYS
from .episode_fixture_links import validate_episode_fixture_links
from .episode_fixture_validation import validate_episode_fixture_shape
from .episode_identity import (
    BRIDGE_FIXTURE_HASH,
    CYCLE1_RUN_HASH,
    DATE_PROFILE_HASH,
    validate_upstream_receipts,
)
from .episode_models import TwoCycleFixture
from .proposal_bridge_fixture import load_proposal_bridge_fixture
from .source_register import load_source_register


def load_two_cycle_fixture(path: Path) -> TwoCycleFixture:
    payload = load_strict_json(path)
    if not isinstance(payload, dict):
        raise ValueError("invalid_envelope: episode fixture must be an object")
    validate_episode_fixture_shape(payload)
    artifact_paths = {
        key: path.parent / payload["artifact_paths"][key] for key in ARTIFACT_KEYS
    }
    artifacts = _load_artifacts(artifact_paths, payload["artifact_hashes"])
    receipts = {
        "cycle1": artifacts["cycle1_receipt"],
        "bridge": artifacts["bridge_receipt"],
        "date": artifacts["date_tracer_receipt"],
    }
    validate_upstream_receipts(receipts)
    if payload["upstream_receipt_hashes"] != {
        key: value["receipt_hash"] for key, value in receipts.items()
    }:
        raise ValueError("identity_mismatch: upstream receipt manifest is invalid")
    source = load_source_register(artifact_paths["source_register"])
    charter = load_us_charter(artifact_paths["charter"], source)
    cycle1 = load_us_cycle_fixture(
        artifact_paths["cycle1_fixture"], charter, artifact_paths["ratification"]
    )
    profile = load_profile(artifact_paths["date_profile"])
    if profile.content_hash != DATE_PROFILE_HASH:
        raise ValueError("identity_mismatch: exact DATE profile is invalid")
    bridge = load_proposal_bridge_fixture(
        artifact_paths["bridge_fixture"], artifact_paths["cycle1_receipt"], profile
    )
    if bridge.content_hash != BRIDGE_FIXTURE_HASH:
        raise ValueError("identity_mismatch: exact bridge fixture is invalid")
    ratification = artifacts["ratification"]
    cycle2 = load_us_cycle_fixture_payload(
        artifacts["cycle2_fixture"],
        charter,
        ratification,
        expected_cycle_id="CYCLE_2",
        external_parent_ids=frozenset(payload["cycle2_external_parent_ids"]),
    )
    _validate_cycle1_artifact(cycle1.content_hash, receipts["cycle1"])
    validate_episode_fixture_links(payload, cycle1, receipts["bridge"], profile, cycle2)
    return TwoCycleFixture(
        fixture_id=payload["fixture_id"],
        content_hash=canonical_hash(payload),
        source=source,
        charter=charter,
        cycle1=cycle1,
        bridge=bridge,
        profile_value=profile,
        cycle2=cycle2,
        _payload=payload,
        _receipts=receipts,
    )


def _load_artifacts(
    paths: dict[str, Path], expected_hashes: dict[str, str]
) -> dict[str, dict[str, Any]]:
    artifacts: dict[str, dict[str, Any]] = {}
    for key, artifact_path in paths.items():
        value = load_strict_json(artifact_path)
        if not isinstance(value, dict):
            raise ValueError(f"invalid_envelope: artifact {key} must be an object")
        if canonical_hash(value) != expected_hashes[key]:
            raise ValueError(f"identity_mismatch: artifact {key} hash is invalid")
        artifacts[key] = value
    return artifacts


def _validate_cycle1_artifact(fixture_hash: str, receipt: dict[str, Any]) -> None:
    if (
        receipt.get("fixture_hash") != fixture_hash
        or receipt.get("run_hash") != CYCLE1_RUN_HASH
    ):
        raise ValueError("identity_mismatch: exact Cycle 1 artifact is invalid")


__all__ = ["TwoCycleFixture", "load_two_cycle_fixture"]
