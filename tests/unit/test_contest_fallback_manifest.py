"""Predeclared paired-study manifest contracts."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest

from nuclear_war_contest.manifest import load_study_manifest
from nuclear_war_contest.preflight import load_candidate_manifest
from nuclear_war_contest.preflight_study_binding import validate_study_binding
from nuclear_war_contest.runner import run_matched_study


def _payload() -> dict[str, object]:
    path = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    ("variant", "condition_ids"),
    [
        (
            "communication_sole_authority",
            ["no_press_sole_authority", "full_press_sole_authority"],
        ),
        ("authority_no_press", ["no_press_sole_authority", "no_press_council"]),
    ],
)
def test_predeclared_fallback_manifest_loads(
    variant: str, condition_ids: list[str]
) -> None:
    payload = _payload()
    payload["study_variant"] = variant
    payload["conditions"] = [
        condition
        for condition in payload["conditions"]  # type: ignore[union-attr]
        if condition["condition_id"] in condition_ids  # type: ignore[index]
    ]

    manifest = load_study_manifest(payload)

    assert manifest.study_variant == variant
    assert [condition.condition_id for condition in manifest.conditions] == (
        condition_ids
    )
    assert len(manifest.cells) == 4


def test_fallback_manifest_rejects_unapproved_condition_pair() -> None:
    payload = _payload()
    payload["study_variant"] = "communication_sole_authority"
    payload["conditions"] = deepcopy(payload["conditions"][:2])  # type: ignore[index]
    payload["conditions"][1]["condition_id"] = "no_press_council"  # type: ignore[index]

    with pytest.raises(ValueError, match="predeclared"):
        load_study_manifest(payload)


@pytest.mark.parametrize(
    ("condition_id", "field"),
    [
        ("no_press_sole_authority", "deference"),
        ("no_press_council", "threshold"),
        ("full_press_sole_authority", "press_passes"),
    ],
)
def test_fallback_manifest_rejects_treatment_parameter_drift(
    condition_id: str, field: str
) -> None:
    payload = _payload()
    payload["study_variant"] = "full_factorial"
    condition = next(
        item
        for item in payload["conditions"]  # type: ignore[union-attr]
        if item["condition_id"] == condition_id  # type: ignore[index]
    )
    if field == "press_passes":
        condition[field] = 2  # type: ignore[index]
    else:
        condition["authority_parameters"][field] = 0.5  # type: ignore[index]

    with pytest.raises(ValueError, match="predeclared treatment"):
        load_study_manifest(payload)


@pytest.mark.parametrize(
    "filename",
    [
        "STUDY_MANIFEST.communication_sole_authority.candidate.json",
        "STUDY_MANIFEST.authority_no_press.candidate.json",
    ],
)
def test_checked_in_fallback_manifests_bind_the_candidate_design(
    filename: str,
) -> None:
    path = Path(__file__).parents[2] / "docs" / "contest" / filename
    manifest = load_study_manifest(json.loads(path.read_text(encoding="utf-8")))
    candidate_path = path.parent / "MODEL_MANIFEST.candidate.json"
    candidate = load_candidate_manifest(
        json.loads(candidate_path.read_text(encoding="utf-8")),
        base_dir=candidate_path.parent,
    )
    validate_study_binding(manifest, candidate)

    assert manifest.study_variant in {
        "communication_sole_authority",
        "authority_no_press",
    }
    assert manifest.preflight_approval_status == "pending_owner"
    assert len(manifest.cells) == 20


@pytest.mark.parametrize(
    "variant",
    ["communication_sole_authority", "authority_no_press"],
)
def test_offline_fallback_runner_reports_only_the_predeclared_pair(
    tmp_path: Path, variant: str
) -> None:
    payload = _payload()
    payload["study_variant"] = variant
    condition_ids = (
        {"no_press_sole_authority", "full_press_sole_authority"}
        if variant == "communication_sole_authority"
        else {"no_press_sole_authority", "no_press_council"}
    )
    payload["conditions"] = [
        condition
        for condition in payload["conditions"]  # type: ignore[union-attr]
        if condition["condition_id"] in condition_ids  # type: ignore[index]
    ]
    manifest = load_study_manifest(payload)

    summary = run_matched_study(manifest, tmp_path)

    assert len(summary["attempts"]) == 4
    assert len(summary["analysis"]["primary"]["pairs"]) == 2
    assert len(summary["analysis"]["exploratory"]["pairs"]) == 2
    assert all(
        pair["contrast"] != "factorial_interaction"
        for pair in summary["analysis"]["exploratory"]["pairs"]
    )
