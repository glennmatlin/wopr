"""Pair construction for simple and factorial study contrasts."""

from __future__ import annotations

from typing import Any

from .analysis_spec import NUMERIC_MEASURES, PRIMARY_MEASURES


def condition_pairs(
    index: dict[tuple[str, int, str], dict[str, Any]],
    model_id: str,
    seed: int,
    contrasts: tuple[tuple[str, str, str], ...],
) -> list[dict[str, Any]]:
    pairs = []
    for contrast, baseline_id, treatment_id in contrasts:
        baseline_key = (model_id, seed, baseline_id)
        treatment_key = (model_id, seed, treatment_id)
        if baseline_key in index and treatment_key in index:
            pairs.append(
                pair(
                    contrast,
                    model_id,
                    seed,
                    "organizational_type",
                    index[baseline_key],
                    index[treatment_key],
                )
            )
    return pairs


def simple_pairs(
    index: dict[tuple[str, int, str, str], dict[str, Any]],
    model_id: str,
    seed: int,
    contrasts: tuple[tuple[str, str, str], ...],
) -> list[dict[str, Any]]:
    pairs = []
    for contrast, fixed_factor, varied in contrasts:
        if varied == "communication":
            baseline_key = (model_id, seed, "no_press", fixed_factor)
            treatment_key = (model_id, seed, "full_press", fixed_factor)
        else:
            baseline_key = (model_id, seed, fixed_factor, "sole_authority")
            treatment_key = (model_id, seed, fixed_factor, "council")
        if baseline_key in index and treatment_key in index:
            pairs.append(
                pair(
                    contrast,
                    model_id,
                    seed,
                    fixed_factor,
                    index[baseline_key],
                    index[treatment_key],
                )
            )
    return pairs


def interaction_pair(
    index: dict[tuple[str, int, str, str], dict[str, Any]],
    model_id: str,
    seed: int,
) -> dict[str, Any] | None:
    keys = {
        "no_press_sole_authority": (model_id, seed, "no_press", "sole_authority"),
        "full_press_sole_authority": (model_id, seed, "full_press", "sole_authority"),
        "no_press_council": (model_id, seed, "no_press", "council"),
        "full_press_council": (model_id, seed, "full_press", "council"),
    }
    if not all(key in index for key in keys.values()):
        return None
    cells = {name: index[key] for name, key in keys.items()}
    deltas = {
        measure: _difference(
            cells["full_press_council"]["measures"],
            measure,
            cells["no_press_council"]["measures"],
            measure,
        )
        - _difference(
            cells["full_press_sole_authority"]["measures"],
            measure,
            cells["no_press_sole_authority"]["measures"],
            measure,
        )
        for measure in NUMERIC_MEASURES
    }
    return {
        "contrast": "factorial_interaction",
        "model_id": model_id,
        "seed": seed,
        "fixed_factor": "2x2",
        "cell_condition_ids": {
            name: row["condition_id"] for name, row in cells.items()
        },
        "deltas": deltas,
    }


def pair(
    contrast: str,
    model_id: str,
    seed: int,
    fixed_factor: str,
    baseline: dict[str, Any],
    treatment: dict[str, Any],
) -> dict[str, Any]:
    return {
        "contrast": contrast,
        "model_id": model_id,
        "seed": seed,
        "fixed_factor": fixed_factor,
        "baseline_condition_id": baseline["condition_id"],
        "treatment_condition_id": treatment["condition_id"],
        "paired_values": {
            measure: {
                "baseline": value(baseline["measures"], measure),
                "treatment": value(treatment["measures"], measure),
            }
            for measure in PRIMARY_MEASURES
        },
        "deltas": {
            measure: _difference(
                treatment["measures"], measure, baseline["measures"], measure
            )
            for measure in NUMERIC_MEASURES
        },
    }


def _difference(
    left: dict[str, Any], left_path: str, right: dict[str, Any], right_path: str
) -> float:
    left_value = value(left, left_path)
    right_value = value(right, right_path)
    if not _numeric(left_value) or not _numeric(right_value):
        return 0.0
    return float(left_value) - float(right_value)


def value(measures: dict[str, Any], path: str) -> Any:
    current: Any = measures
    for part in path.split("."):
        current = current[part]
    return current


def _numeric(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


__all__ = ["condition_pairs", "interaction_pair", "pair", "simple_pairs"]
