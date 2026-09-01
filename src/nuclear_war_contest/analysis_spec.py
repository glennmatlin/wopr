"""Frozen measure and contrast definitions for contest analysis."""

ANALYSIS_SCHEMA_VERSION = 1
PRIMARY_MEASURES = (
    "ordinary_escalation.count",
    "ordinary_escalation.total_yield",
    "ordinary_escalation.first_turn",
    "ordinary_escalation.targets",
    "forced_retaliation.targeted_count",
    "forced_retaliation.executed_count",
    "forced_retaliation.total_yield",
    "forced_retaliation.targets",
    "population_loss",
    "eliminations",
    "winner",
    "surviving_factions",
    "turns",
    "censored",
    "authority.deliberation_count",
    "authority.disagreement_count",
    "authority.threshold_failure_count",
    "authority.executive_match_count",
    "authority.executive_override_count",
)
NUMERIC_MEASURES = {
    path
    for path in PRIMARY_MEASURES
    if path
    not in {
        "ordinary_escalation.first_turn",
        "ordinary_escalation.targets",
        "forced_retaliation.targets",
        "winner",
        "surviving_factions",
        "censored",
    }
}
PRIMARY_CONTRASTS = (
    ("full_press_minus_no_press", "sole_authority", "communication"),
    ("council_minus_sole_authority", "no_press", "authority"),
)
EXPLORATORY_CONTRASTS = PRIMARY_CONTRASTS + (
    ("full_press_minus_no_press", "council", "communication"),
    ("council_minus_sole_authority", "full_press", "authority"),
)
ROOM_INSTRUMENT_CONDITION_IDS = {
    "full_press_presidential_staff",
    "full_press_equal_council",
    "full_press_chair_weighted_council",
}
ROOM_INSTRUMENT_PRIMARY_CONTRASTS = (
    (
        "equal_council_minus_staff",
        "full_press_presidential_staff",
        "full_press_equal_council",
    ),
    (
        "chair_weighted_minus_staff",
        "full_press_presidential_staff",
        "full_press_chair_weighted_council",
    ),
)


__all__ = [
    "ANALYSIS_SCHEMA_VERSION",
    "EXPLORATORY_CONTRASTS",
    "NUMERIC_MEASURES",
    "PRIMARY_CONTRASTS",
    "PRIMARY_MEASURES",
    "ROOM_INSTRUMENT_CONDITION_IDS",
    "ROOM_INSTRUMENT_PRIMARY_CONTRASTS",
]
