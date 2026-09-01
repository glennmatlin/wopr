"""Tests for checked-in model scorecard examples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from nuclear_war_env.cli import main
from nuclear_war_env.llm_model_scorecard_catalog import load_catalog_rows

PROJECT_ROOT = Path(__file__).resolve().parents[2]
EXAMPLE_PATH = PROJECT_ROOT / "docs/examples/llm_model_scorecard_catalog_demo.json"
RESEARCH_STATE_PATH = (
    PROJECT_ROOT / "research/llm_model_calibration/research-state.yaml"
)
CATALOG_RELATIVE_PATH = (
    "research/llm_model_calibration/data/serverless_catalog_2026-07-05.json"
)


def test_scorecard_catalog_demo_writes_predicted_only_artifacts(
    tmp_path,
    capsys,
) -> None:
    demo = _load_demo()
    assert demo["command"] == "llm-model-scorecard"
    assert demo["stage"] == "catalog"
    assert demo["catalog"] == CATALOG_RELATIVE_PATH

    catalog_path = PROJECT_ROOT / str(demo["catalog"])
    rows = load_catalog_rows(catalog_path)
    assert len(rows) == 23

    out_dir = tmp_path / "scorecard"
    code = main(_demo_args(demo, out_dir))

    captured = capsys.readouterr()
    catalog = json.loads((out_dir / "catalog_scorecard.json").read_text())
    stage2 = json.loads((out_dir / "stage2_calibration_results.json").read_text())
    assert code == 0
    assert json.loads(captured.out) == _expected_paths(out_dir)
    assert len(catalog["scores"]) == 23
    assert {row["score_type"] for row in catalog["scores"]} == {"predicted"}
    assert stage2["results"] == []
    assert (out_dir / "scorecard_summary.md").is_file()


def test_research_state_names_stage3_report_artifacts_as_next_step() -> None:
    next_action = _next_action()

    assert "research/llm_model_calibration/README.md" in next_action
    assert "stage3_press_light_scorecard.md" in next_action
    assert "stage3_results_playground.html" in next_action
    assert (
        "/tmp/wopr_stage3_presslight_robustness/press_light_aggregate.json"
        in next_action
    )
    assert "reasoning_effort=low" in next_action
    assert "Qwen/Qwen3.5-9B" in next_action
    assert "Qwen/Qwen2.5-7B-Instruct-Turbo" in next_action
    assert "Qwen/Qwen3-235B-A22B-Instruct-2507-tput" in next_action


def _load_demo() -> dict[str, Any]:
    return json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))


def _next_action() -> str:
    for line in RESEARCH_STATE_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("next_action: "):
            return line.removeprefix("next_action: ")
    raise AssertionError("research-state.yaml is missing next_action")


def _demo_args(demo: dict[str, Any], out_dir: Path) -> list[str]:
    return [
        str(demo["command"]),
        "--stage",
        str(demo["stage"]),
        "--catalog",
        str(PROJECT_ROOT / str(demo["catalog"])),
        "--out",
        str(out_dir),
    ]


def _expected_paths(out_dir: Path) -> dict[str, str]:
    return {
        "catalog_scorecard": str(out_dir / "catalog_scorecard.json"),
        "scorecard_summary": str(out_dir / "scorecard_summary.md"),
        "stage2_calibration_results": str(out_dir / "stage2_calibration_results.json"),
    }
