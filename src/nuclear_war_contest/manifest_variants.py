"""Predeclared condition sets for factorial and paired contest studies."""

from __future__ import annotations

from .manifest_types import StudyCondition

STUDY_VARIANTS = {
    "full_factorial",
    "communication_sole_authority",
    "authority_no_press",
    "room_instrument",
    "room_instrument_smoke",
    "room_instrument_demo",
}

_CONDITION_IDS = {
    "full_factorial": {
        "no_press_sole_authority",
        "full_press_sole_authority",
        "no_press_council",
        "full_press_council",
    },
    "communication_sole_authority": {
        "no_press_sole_authority",
        "full_press_sole_authority",
    },
    "authority_no_press": {
        "no_press_sole_authority",
        "no_press_council",
    },
    "room_instrument": {
        "full_press_presidential_staff",
        "full_press_equal_council",
        "full_press_chair_weighted_council",
    },
    "room_instrument_smoke": {
        "full_press_presidential_staff",
        "full_press_equal_council",
        "full_press_chair_weighted_council",
    },
    "room_instrument_demo": {
        "full_press_equal_council",
    },
}
_CONDITION_SPECS = {
    "no_press_sole_authority": {
        "communication": "no_press",
        "authority": "sole_authority",
        "authority_parameters": {"deference": 0.0},
        "press_passes": 1,
    },
    "full_press_sole_authority": {
        "communication": "full_press",
        "authority": "sole_authority",
        "authority_parameters": {"deference": 0.0},
        "press_passes": 1,
    },
    "no_press_council": {
        "communication": "no_press",
        "authority": "council",
        "authority_parameters": {
            "threshold": 0.6666666667,
            "weights": {
                "executive": 1.0,
                "strategic_advisor": 1.0,
                "risk_advisor": 1.0,
            },
        },
        "press_passes": 1,
    },
    "full_press_council": {
        "communication": "full_press",
        "authority": "council",
        "authority_parameters": {
            "threshold": 0.6666666667,
            "weights": {
                "executive": 1.0,
                "strategic_advisor": 1.0,
                "risk_advisor": 1.0,
            },
        },
        "press_passes": 1,
    },
    "full_press_presidential_staff": {
        "communication": "full_press",
        "authority": "sole_authority",
        "authority_parameters": {"deference": 0.0},
        "press_passes": 1,
    },
    "full_press_equal_council": {
        "communication": "full_press",
        "authority": "council",
        "authority_parameters": {
            "threshold": 0.6666666667,
            "weights": {
                "executive": 1.0,
                "strategic_advisor": 1.0,
                "risk_advisor": 1.0,
            },
        },
        "press_passes": 1,
    },
    "full_press_chair_weighted_council": {
        "communication": "full_press",
        "authority": "council",
        "authority_parameters": {
            "threshold": 0.6666666667,
            "weights": {
                "executive": 2.0,
                "strategic_advisor": 1.0,
                "risk_advisor": 1.0,
            },
        },
        "press_passes": 1,
    },
}


def validate_study_conditions(
    conditions: tuple[StudyCondition, ...], variant: str
) -> None:
    expected = _CONDITION_IDS.get(variant)
    if expected is None:
        raise ValueError("Study manifest study_variant is invalid")
    actual = {condition.condition_id for condition in conditions}
    if actual != expected:
        if variant == "full_factorial":
            raise ValueError(
                "Study manifest must contain all four communication-authority cells"
            )
        if variant in {"room_instrument", "room_instrument_smoke"}:
            raise ValueError(
                f"Study manifest {variant} conditions do not match the "
                "three Organizational Presets"
            )
        if variant == "room_instrument_demo":
            raise ValueError(
                "Study manifest room_instrument_demo must be equal council only"
            )
        raise ValueError("Study manifest conditions do not match a predeclared pair")
    for condition in conditions:
        if _condition_payload(condition) != _CONDITION_SPECS[condition.condition_id]:
            raise ValueError(
                "Study manifest condition does not match its predeclared treatment"
            )


def _condition_payload(condition: StudyCondition) -> dict[str, object]:
    return {
        "communication": condition.communication,
        "authority": condition.authority,
        "authority_parameters": condition.authority_parameters,
        "press_passes": condition.press_passes,
    }


__all__ = ["STUDY_VARIANTS", "validate_study_conditions"]
