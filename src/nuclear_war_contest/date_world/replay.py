"""Deterministic DATE World replay."""

from __future__ import annotations

from .identity import core_hash
from .models import DateRun
from .profile import DateProfile


def replay_run(profile: DateProfile, source: DateRun) -> DateRun:
    from .transition import admit_transition, initialize_run

    replayed = initialize_run(profile, source.run_id)
    if core_hash(replayed.initial_core()) != core_hash(source.initial_core()):
        raise ValueError("DATE replay initial Core does not match")
    for transition in source.accepted_transitions():
        result = admit_transition(
            profile,
            replayed,
            transition["event_template"],
            transition["patch_instance"],
        )
        if not result.receipt.accepted:
            raise ValueError(
                f"DATE replay rejected transition: {result.receipt.reason_codes}"
            )
        replayed = result.run
    if core_hash(replayed.current_core()) != core_hash(source.current_core()):
        raise ValueError("DATE replay final Core does not match")
    if replayed.ledger() != source.ledger():
        raise ValueError("DATE replay ledger does not match")
    return replayed


__all__ = ["replay_run"]
