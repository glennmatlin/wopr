"""Exact D70 fixture handoff from scripted Room outputs."""

from __future__ import annotations

from copy import deepcopy

from nuclear_war_contest.date_world.identity import canonical_hash

from .cycle_fixture import UsCycleFixture
from .episode_models import TwoCycleFixture
from .scripted_rehearsal_models import CycleRehearsal


def materialize_rehearsed_fixture(
    source: TwoCycleFixture,
    cycle1: CycleRehearsal,
    cycle2: CycleRehearsal,
) -> TwoCycleFixture:
    rehearsed_cycle1 = _cycle_fixture(source.cycle1_fixture(), cycle1)
    rehearsed_cycle2 = _cycle_fixture(source.cycle2_fixture(), cycle2)
    return TwoCycleFixture(
        fixture_id=source.fixture_id,
        content_hash=source.content_hash,
        source=source.source,
        charter=source.charter,
        cycle1=rehearsed_cycle1,
        bridge=source.bridge_fixture(),
        profile_value=source.profile(),
        cycle2=rehearsed_cycle2,
        _payload=source.payload(),
        _receipts=source.receipts(),
    )


def _cycle_fixture(source: UsCycleFixture, rehearsal: CycleRehearsal) -> UsCycleFixture:
    payload = source.payload()
    payload["group_products"] = deepcopy(rehearsal.products)
    payload["confirmations"] = deepcopy(rehearsal.confirmations)
    content_hash = canonical_hash(payload)
    if content_hash != source.content_hash:
        raise ValueError("scripted Room outputs changed the retained cycle fixture")
    return UsCycleFixture(
        fixture_id=source.fixture_id,
        cycle_id=source.cycle_id,
        ratification_hash=source.ratification_hash,
        content_hash=content_hash,
        _payload=payload,
    )


__all__ = ["materialize_rehearsed_fixture"]
