"""Deterministic no-model proposal bridge replay."""

from __future__ import annotations

from nuclear_war_contest.date_world.profile import DateProfile

from .proposal_bridge_execution import run_no_model_proposal_bridge
from .proposal_bridge_models import ProposalBridgeRun


def replay_proposal_bridge(
    profile: DateProfile, source: ProposalBridgeRun
) -> ProposalBridgeRun:
    replayed = run_no_model_proposal_bridge(profile, source.fixture())
    if replayed.content_hash != source.content_hash:
        raise ValueError("replay_mismatch: proposal bridge run changed")
    if replayed.receipt() != source.receipt():
        raise ValueError("replay_mismatch: proposal bridge receipt changed")
    return replayed


__all__ = ["replay_proposal_bridge"]
