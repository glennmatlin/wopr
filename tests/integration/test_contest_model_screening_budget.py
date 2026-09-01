"""Budget arithmetic tests for the offline model-screening packet."""

from __future__ import annotations

import hashlib
import json
import shutil
from decimal import Decimal
from pathlib import Path

import pytest

from nuclear_war_contest.screening_manifest import load_screening_manifest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCREENING_MANIFEST = PROJECT_ROOT / "docs/contest/MODEL_SCREENING.candidate.json"
SCREENING_BUDGET = PROJECT_ROOT / "docs/contest/M3_SCREENING_BUDGET.json"


def test_screening_budget_is_conservative_and_not_authorized() -> None:
    budget = json.loads(SCREENING_BUDGET.read_text(encoding="utf-8"))
    manifest = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))

    assert budget["status"] == "planning_only"
    assert budget["authorization_status"] == "pending_owner"
    assert budget["network_calls"] == 0
    assert budget["credentials_read"] is False
    assert budget["request_bound"] == {
        "models": 3,
        "seeds_per_model": 3,
        "calls_per_game": 624,
        "retry_multiplier": 6,
        "provider_request_attempts": 33696,
        "input_tokens": 276037632,
        "output_tokens": 17252352,
    }
    request_bound = budget["request_bound"]
    assumptions = budget["assumptions"]
    retry_multiplier = (1 + assumptions["output_retries"]) * (
        1 + assumptions["transport_retry_margin"]
    )
    expected_attempts = (
        len(manifest["models"])
        * assumptions["seeds_per_model"]
        * assumptions["calls_per_game"]
        * retry_multiplier
    )
    assert request_bound["models"] == len(manifest["models"])
    assert request_bound["seeds_per_model"] == len(manifest["screening_seeds"])
    assert request_bound["retry_multiplier"] == retry_multiplier
    assert request_bound["provider_request_attempts"] == expected_attempts
    assert (
        request_bound["input_tokens"]
        == expected_attempts * assumptions["input_tokens_per_request"]
    )
    assert (
        request_bound["output_tokens"]
        == expected_attempts * assumptions["output_tokens_per_request"]
    )
    total = Decimal("0")
    model_bounds = {
        item["provider_model"]: Decimal(str(item["cost_usd"]))
        for item in budget["model_bounds"]
    }
    per_model_attempts = request_bound["provider_request_attempts"] // len(
        manifest["models"]
    )
    for model in manifest["models"]:
        input_cost = (
            Decimal(per_model_attempts * assumptions["input_tokens_per_request"])
            * Decimal(str(model["input_usd_per_million"]))
            / Decimal(1_000_000)
        )
        output_cost = (
            Decimal(per_model_attempts * assumptions["output_tokens_per_request"])
            * Decimal(str(model["output_usd_per_million"]))
            / Decimal(1_000_000)
        )
        expected = (input_cost + output_cost).quantize(Decimal("0.000001"))
        total += expected
        assert model_bounds[model["provider_model"]] == expected
    assert Decimal(str(budget["upper_bound_usd"])) == total
    assert budget["owner_total_cap_usd"] == 1000.0


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("upper_bound_usd", 1001.0, "upper bound"),
        ("upper_bound_usd", True, "upper bound"),
        ("upper_bound_usd", -1.0, "upper bound"),
        ("upper_bound_usd", float("nan"), "upper bound"),
        ("paid_work_authorized", True, "object"),
        ("schema_version", 2, "schema_version"),
    ],
)
def test_screening_loader_rejects_budget_shape_or_bound_drift(
    tmp_path: Path, field: str, value: object, message: str
) -> None:
    manifest = json.loads(
        (PROJECT_ROOT / "docs/contest/MODEL_SCREENING.candidate.json").read_text()
    )
    budget = json.loads((SCREENING_BUDGET).read_text())
    budget[field] = value
    budget_path = tmp_path / "budget.json"
    budget_path.write_text(json.dumps(budget), encoding="utf-8")
    catalog = PROJECT_ROOT / manifest["catalog_path"].replace("../../", "")
    candidate = PROJECT_ROOT / "docs/contest/MODEL_MANIFEST.candidate.json"
    catalog_path = tmp_path / "catalog.json"
    candidate_path = tmp_path / "candidate.json"
    shutil.copyfile(catalog, catalog_path)
    shutil.copyfile(candidate, candidate_path)
    manifest["budget_path"] = budget_path.name
    manifest["budget_sha256"] = _sha256(budget_path)
    manifest["catalog_path"] = catalog_path.name
    manifest["catalog_sha256"] = _sha256(catalog_path)
    manifest["final_candidate_path"] = candidate_path.name
    manifest["final_candidate_sha256"] = _sha256(candidate_path)

    with pytest.raises(ValueError, match=message):
        load_screening_manifest(manifest, base_dir=tmp_path)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
