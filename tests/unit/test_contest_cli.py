"""Fail-closed contest CLI tests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pytest

from nuclear_war_contest.cli import run_contest_command
from nuclear_war_env.cli_parser import build_parser


def test_contest_dry_run_parser_accepts_max_workers() -> None:
    args = build_parser().parse_args(
        [
            "contest-dry-run",
            "--manifest",
            "manifest.json",
            "--out-dir",
            "out",
            "--max-workers",
            "3",
        ]
    )

    assert args.max_workers == 3


def test_contest_dry_run_passes_max_workers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    observed: dict[str, int] = {}

    def fake_run_matched_study(*args: object, **kwargs: object) -> dict[str, object]:
        del args
        observed["max_workers"] = int(kwargs["max_workers"])
        return {"analysis": {}}

    monkeypatch.setattr(
        "nuclear_war_contest.cli.run_matched_study", fake_run_matched_study
    )
    code = run_contest_command(
        argparse.Namespace(
            command="contest-dry-run",
            manifest=str(source),
            out_dir=str(tmp_path / "output"),
            max_workers=3,
        )
    )

    assert code == 0
    assert observed == {"max_workers": 3}


def test_contest_run_study_passes_max_workers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    observed: dict[str, int] = {}

    def fake_run_matched_study(*args: object, **kwargs: object) -> dict[str, object]:
        del args
        observed["max_workers"] = int(kwargs["max_workers"])
        return {"analysis": {}}

    monkeypatch.setattr(
        "nuclear_war_contest.cli.run_matched_study", fake_run_matched_study
    )
    args = build_parser().parse_args(
        [
            "contest-run-study",
            "--manifest",
            str(source),
            "--out-dir",
            str(tmp_path / "output"),
            "--max-workers",
            "2",
        ]
    )

    code = run_contest_command(args)

    assert code == 0
    assert observed == {"max_workers": 2}


def test_contest_dry_run_rejects_live_backend_before_output(tmp_path: Path) -> None:
    source = (
        Path(__file__).parents[2] / "docs" / "contest" / "STUDY_MANIFEST.dry_run.json"
    )
    payload = json.loads(source.read_text(encoding="utf-8"))
    payload["models"][0]["backend"] = "concordia_http"
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(payload), encoding="utf-8")
    output = tmp_path / "output"

    with pytest.raises(ValueError, match="only concordia_first_legal"):
        run_contest_command(
            argparse.Namespace(
                command="contest-dry-run",
                manifest=str(manifest),
                out_dir=str(output),
            )
        )

    assert not output.exists()


def test_contest_preflight_writes_pending_owner_receipt(tmp_path: Path) -> None:
    source = (
        Path(__file__).parents[2] / "docs" / "contest" / "MODEL_MANIFEST.candidate.json"
    )
    output = tmp_path / "preflight.json"

    code = run_contest_command(
        argparse.Namespace(
            command="contest-preflight",
            manifest=str(source),
            out=str(output),
        )
    )

    assert code == 0
    receipt = json.loads(output.read_text(encoding="utf-8"))
    assert receipt["status"] == "pending_owner"
    assert receipt["network_calls"] == 0


def test_live_contest_preflight_requires_explicit_network_flag(
    tmp_path: Path,
) -> None:
    source = (
        Path(__file__).parents[2] / "docs" / "contest" / "MODEL_MANIFEST.candidate.json"
    )
    output = tmp_path / "live-preflight.json"

    with pytest.raises(ValueError, match="allow_network"):
        run_contest_command(
            argparse.Namespace(
                command="contest-live-preflight",
                manifest=str(source),
                out=str(output),
                allow_network=False,
            )
        )

    assert not output.exists()


def test_contest_public_scan_reports_a_clean_packet(
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = Path(__file__).parents[2] / "docs" / "contest"

    code = run_contest_command(
        argparse.Namespace(command="contest-public-scan", root=str(root))
    )

    assert code == 0
    assert json.loads(capsys.readouterr().out)["ok"] is True
