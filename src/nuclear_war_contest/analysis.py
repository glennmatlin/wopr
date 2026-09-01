"""Paired seed-level analysis for the institutional sensitivity profile."""

from __future__ import annotations

from collections import defaultdict
from statistics import median
from typing import Any

from .analysis_pairs import condition_pairs, interaction_pair, simple_pairs
from .analysis_spec import (
    ANALYSIS_SCHEMA_VERSION,
    EXPLORATORY_CONTRASTS,
    PRIMARY_CONTRASTS,
    PRIMARY_MEASURES,
    ROOM_INSTRUMENT_CONDITION_IDS,
    ROOM_INSTRUMENT_PRIMARY_CONTRASTS,
)


def build_paired_analysis(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": ANALYSIS_SCHEMA_VERSION,
        "primary": _analysis_for_tiers(rows, {"A"}, PRIMARY_CONTRASTS),
        "sensitivity": _analysis_for_tiers(rows, {"A", "B"}, PRIMARY_CONTRASTS),
        "exploratory": _analysis_for_tiers(
            rows, {"A"}, EXPLORATORY_CONTRASTS, include_interaction=True
        ),
    }


def _analysis_for_tiers(
    rows: list[dict[str, Any]],
    allowed_tiers: set[str],
    contrasts: tuple[tuple[str, str, str], ...],
    include_interaction: bool = False,
) -> dict[str, Any]:
    eligible = [
        row for row in rows if row.get("admissibility", {}).get("tier") in allowed_tiers
    ]
    room_instrument = any(
        row.get("condition_id") in ROOM_INSTRUMENT_CONDITION_IDS for row in eligible
    )
    if room_instrument:
        index = {
            (row["model_id"], row["seed"], row["condition_id"]): row
            for row in eligible
        }
        pairs: list[dict[str, Any]] = []
        for model_id, seed in sorted(
            {(row["model_id"], row["seed"]) for row in eligible}
        ):
            pairs.extend(
                condition_pairs(
                    index, model_id, seed, ROOM_INSTRUMENT_PRIMARY_CONTRASTS
                )
            )
    else:
        index = {
            (row["model_id"], row["seed"], row["communication"], row["authority"]): row
            for row in eligible
        }
        pairs = []
        for model_id, seed in sorted(
            {(row["model_id"], row["seed"]) for row in eligible}
        ):
            pairs.extend(simple_pairs(index, model_id, seed, contrasts))
            if include_interaction:
                interaction = interaction_pair(index, model_id, seed)
                if interaction is not None:
                    pairs.append(interaction)
    return {
        "eligible_rows": len(eligible),
        "pairs": pairs,
        "summary": _summaries(pairs),
    }


def _summaries(pairs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str], list[float]] = defaultdict(list)
    for pair in pairs:
        for measure, delta in pair["deltas"].items():
            grouped[
                (pair["contrast"], pair["model_id"], pair["fixed_factor"], measure)
            ].append(delta)
    return [
        {
            "contrast": contrast,
            "model_id": model_id,
            "fixed_factor": fixed_factor,
            "measure": measure,
            "n": len(values),
            "median": median(values),
            "min": min(values),
            "max": max(values),
            "positive_count": sum(value > 0 for value in values),
            "negative_count": sum(value < 0 for value in values),
            "zero_count": sum(value == 0 for value in values),
        }
        for (contrast, model_id, fixed_factor, measure), values in sorted(
            grouped.items()
        )
    ]


__all__ = ["ANALYSIS_SCHEMA_VERSION", "PRIMARY_MEASURES", "build_paired_analysis"]
