"""Factor and model validation for contest study manifests."""

from __future__ import annotations

from typing import Any

from nuclear_war_env.integer_validation import is_strict_int

from .manifest_parameter_validation import (
    validate_authority_parameters,
    validate_client,
    validate_role_prompt_hashes,
)
from .manifest_types import StudyCondition, StudyModel
from .manifest_variants import validate_study_conditions

COMMUNICATIONS = {"no_press", "press_light", "full_press"}
AUTHORITIES = {"sole_authority", "council"}
_CONDITION_FIELDS = {
    "condition_id",
    "communication",
    "authority",
    "authority_parameters",
    "press_passes",
}
_MODEL_FIELDS = {
    "model_id",
    "backend",
    "provider",
    "client",
    "max_retries",
    "role_prompt_hashes",
}


def load_conditions(value: Any) -> tuple[StudyCondition, ...]:
    if not isinstance(value, list) or not value:
        raise ValueError("Study manifest conditions must be a nonempty list")
    conditions = tuple(
        StudyCondition(
            condition_id=_text(item["condition_id"], "condition_id"),
            communication=_choice(
                item["communication"], COMMUNICATIONS, "communication"
            ),
            authority=_choice(item["authority"], AUTHORITIES, "authority"),
            authority_parameters=_object(
                item["authority_parameters"], "authority_parameters"
            ),
            press_passes=_positive_int(item["press_passes"], "press_passes"),
        )
        for item in _objects(value, _CONDITION_FIELDS, "condition")
    )
    if len({condition.condition_id for condition in conditions}) != len(conditions):
        raise ValueError("Study manifest condition ids must be unique")
    for condition in conditions:
        validate_authority_parameters(
            condition.authority, condition.authority_parameters
        )
    return conditions


def load_models(value: Any) -> tuple[StudyModel, ...]:
    if not isinstance(value, list) or not value:
        raise ValueError("Study manifest models must be a nonempty list")
    models = tuple(
        StudyModel(
            model_id=_text(item["model_id"], "model_id"),
            backend=_text(item["backend"], "backend"),
            provider=_text(item["provider"], "provider"),
            client=validate_client(item["client"], item["provider"]),
            max_retries=_nonnegative_int(item["max_retries"], "max_retries"),
            role_prompt_hashes=validate_role_prompt_hashes(item["role_prompt_hashes"]),
        )
        for item in _objects(value, _MODEL_FIELDS, "model")
    )
    if len({model.model_id for model in models}) != len(models):
        raise ValueError("Study manifest model ids must be unique")
    return models


def load_seeds(value: Any) -> tuple[int, ...]:
    if not isinstance(value, list) or not value:
        raise ValueError("Study manifest seeds must be a nonempty list")
    seeds = tuple(_positive_int(item, "seed", minimum=0) for item in value)
    if len(set(seeds)) != len(seeds):
        raise ValueError("Study manifest seeds must be unique")
    return seeds


def validate_factorial_conditions(
    conditions: tuple[StudyCondition, ...], variant: str = "full_factorial"
) -> None:
    validate_study_conditions(conditions, variant)


def _objects(value: list[Any], fields: set[str], label: str) -> list[dict[str, Any]]:
    objects: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict) or set(item) != fields:
            raise ValueError(f"Study manifest {label} {index} fields are invalid")
        objects.append(item)
    return objects


def _object(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"Study manifest {field} must be an object")
    return dict(value)


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"Study manifest {field} must be a nonempty string")
    return value


def _choice(value: Any, choices: set[str], field: str) -> str:
    text = _text(value, field)
    if text not in choices:
        raise ValueError(f"Study manifest {field} is invalid")
    return text


def _positive_int(value: Any, field: str, minimum: int = 1) -> int:
    if not is_strict_int(value) or value < minimum:
        raise ValueError(f"Study manifest {field} must be an integer >= {minimum}")
    return value


def _nonnegative_int(value: Any, field: str) -> int:
    return _positive_int(value, field, minimum=0)
