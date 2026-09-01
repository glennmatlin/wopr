"""Concurrent execution of independent scripted Room groups."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from typing import Any

from .scripted_rehearsal_context import CycleContext, GroupContext
from .scripted_rehearsal_group import rehearse_group
from .scripted_rehearsal_models import GroupRehearsal


def rehearse_wave(
    context: CycleContext,
    wave: tuple[str, ...],
    deliveries: list[dict[str, Any]],
    catalog: dict[str, dict[str, Any]],
) -> list[GroupRehearsal]:
    if len(wave) == 1:
        return [rehearse_group(_group_context(context, wave[0], deliveries, catalog))]
    with ThreadPoolExecutor(max_workers=len(wave)) as executor:
        futures = {
            group_id: executor.submit(
                rehearse_group, _group_context(context, group_id, deliveries, catalog)
            )
            for group_id in wave
        }
        return [futures[group_id].result() for group_id in wave]


def _group_context(
    context: CycleContext,
    group_id: str,
    deliveries: list[dict[str, Any]],
    catalog: dict[str, dict[str, Any]],
) -> GroupContext:
    group = context.groups[group_id]
    return GroupContext(
        context.fixture.cycle_id,
        group,
        context.schemas[group["product_schema_id"]],
        context.seats,
        context.compiled,
        context.runtimes,
        deliveries,
        catalog,
        context.product_contracts.get(group_id),
    )


__all__ = ["rehearse_wave"]
