"""Contract tests for the separate three-model screening packet."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nuclear_war_agents import HTTPClientConfig
from nuclear_war_contest.screening_manifest import (
    load_screening_manifest,
    load_screening_manifest_file,
)
from nuclear_war_env.llm_model_scorecard_catalog import load_catalog_rows

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCREENING_MANIFEST = PROJECT_ROOT / "docs/contest/MODEL_SCREENING.candidate.json"
SCREENING_CATALOG = (
    PROJECT_ROOT
    / "research/llm_model_calibration/data/contest_screening_catalog_2026-08-16.json"
)
FINAL_CANDIDATE = PROJECT_ROOT / "docs/contest/MODEL_MANIFEST.candidate.json"
CATALOG_SHA256 = "1bba59c3f20df3ed41d82f042f228457148e412ce2cd51b4453fca4fa5b24856"
BUDGET_SHA256 = "99058cfef2f47a2878c8e3cf13ee633664bcdc32f20313d3e505529263dc449d"
FINAL_CANDIDATE_SHA256 = (
    "5bf960368ad93ccedff46aa422cde5c2ad4b36cb74a71767f7d66b75614a4bb9"
)

EXPECTED_MODELS = (
    "openai/gpt-oss-20b",
    "deepseek-ai/DeepSeek-V4-Flash-0731",
    "Qwen/Qwen3.5-9B",
)


def test_screening_packet_is_separate_from_final_candidate() -> None:
    manifest = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    final_candidate = json.loads(FINAL_CANDIDATE.read_text(encoding="utf-8"))
    loaded = load_screening_manifest_file(SCREENING_MANIFEST)

    assert manifest["selection_status"] == "screening_only"
    assert manifest["full_design_model_selection"] == "deferred_after_screen"
    assert [item["provider_model"] for item in manifest["models"]] == list(
        EXPECTED_MODELS
    )
    assert [item["client"]["model"] for item in final_candidate["models"]] == [
        "openai/gpt-oss-120b",
        "Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
    ]
    assert loaded.final_candidate_sha256 == FINAL_CANDIDATE_SHA256
    assert loaded.catalog_sha256 == CATALOG_SHA256
    assert loaded.budget_sha256 == BUDGET_SHA256
    assert len(loaded.models) == 3


def test_screening_packet_freezes_controls_and_disjoint_seeds() -> None:
    manifest = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    screening = manifest["screening"]
    loaded = load_screening_manifest_file(SCREENING_MANIFEST)

    assert manifest["screening_seeds"] == [101, 102, 103]
    assert manifest["study_seeds"] == [51, 52, 53, 54, 55]
    assert set(manifest["screening_seeds"]).isdisjoint(manifest["study_seeds"])
    assert screening == {
        "mode": "press_light",
        "players": 4,
        "max_turns": 3,
        "temperature": 0.7,
        "max_tokens": 512,
        "reasoning_enabled": False,
        "stream": True,
        "output_retries": 1,
        "transport_retry_margin": 2,
    }
    assert manifest["approval_status"] == "pending_owner"
    assert manifest["network_calls"] == 0
    assert manifest["credentials_read"] is False
    assert manifest["owner_total_cap_usd"] == 1000.0
    assert all(model.backend == "concordia_http" for model in loaded.models)
    assert loaded.provider_name == "together"
    assert all(model.client["timeout_seconds"] == 60 for model in loaded.models)
    assert all(model.client["model"] == model.provider_model for model in loaded.models)
    assert all(
        model.client["max_tokens"] == loaded.max_tokens for model in loaded.models
    )
    assert all(
        model.client["temperature"] == loaded.temperature for model in loaded.models
    )
    for model in loaded.models:
        HTTPClientConfig(**model.client)


def test_deepseek_screening_client_pins_together_catalog_contract() -> None:
    manifest = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    model = manifest["models"][1]

    assert model["provider"] == "together"
    assert model["provider_model"] == "deepseek-ai/DeepSeek-V4-Flash-0731"
    assert model["client"]["base_url"] == "https://api.together.ai/v1"
    assert model["client"]["api_key_env"] == "TOGETHER_API_KEY"
    assert model["client"]["reasoning_enabled"] is False


def test_screening_loader_rejects_unpinned_client_settings() -> None:
    payload = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    del payload["models"][0]["backend"]

    with pytest.raises(ValueError, match="model fields"):
        load_screening_manifest(payload, base_dir=SCREENING_MANIFEST.parent)


def test_screening_loader_rejects_catalog_hash_drift() -> None:
    payload = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    payload["catalog_sha256"] = "0" * 64

    with pytest.raises(ValueError, match="catalog hash"):
        load_screening_manifest(payload, base_dir=SCREENING_MANIFEST.parent)


def test_screening_loader_rejects_coherent_control_drift() -> None:
    payload = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    payload["screening"]["temperature"] = 0.0
    for model in payload["models"]:
        model["client"]["temperature"] = 0.0

    with pytest.raises(ValueError, match="gameplay controls"):
        load_screening_manifest(payload, base_dir=SCREENING_MANIFEST.parent)

    payload = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    payload["screening_seeds"][0] = 104
    with pytest.raises(ValueError, match="seed assignments"):
        load_screening_manifest(payload, base_dir=SCREENING_MANIFEST.parent)


def test_screening_loader_rejects_cap_drift() -> None:
    payload = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    payload["owner_total_cap_usd"] = 1001.0

    with pytest.raises(ValueError, match="authorization fields"):
        load_screening_manifest(payload, base_dir=SCREENING_MANIFEST.parent)


def test_screening_catalog_matches_manifest_models_and_rates() -> None:
    manifest = json.loads(SCREENING_MANIFEST.read_text(encoding="utf-8"))
    rows = load_catalog_rows(SCREENING_CATALOG)
    expected = {
        item["provider_model"]: (
            item["input_usd_per_million"],
            item["output_usd_per_million"],
        )
        for item in manifest["models"]
    }

    assert [row.model_id for row in rows] == list(EXPECTED_MODELS)
    assert {row.model_id: (row.input_price, row.output_price) for row in rows} == {
        model_id: (rates[0], rates[1]) for model_id, rates in expected.items()
    }
