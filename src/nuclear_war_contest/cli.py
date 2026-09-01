"""CLI entry point for the non-billable contest study dry run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .live_preflight import run_candidate_preflight
from .live_preflight_promotion import (
    build_live_preflight_promotion_approval,
    promote_live_preflight_receipt,
)
from .manifest import load_study_manifest
from .preflight import build_preflight_receipt, load_candidate_manifest
from .public_scan import audit_public_packet
from .runner import run_matched_study
from .screening_cli import run_screening_command


def add_contest_parser(subparsers: argparse._SubParsersAction) -> None:
    preflight = subparsers.add_parser("contest-preflight")
    preflight.add_argument("--manifest", required=True)
    preflight.add_argument("--out", required=True)
    live_preflight = subparsers.add_parser("contest-live-preflight")
    live_preflight.add_argument("--manifest", required=True)
    live_preflight.add_argument("--out", required=True)
    live_preflight.add_argument("--allow-network", action="store_true")
    live_preflight.add_argument("--approval", required=True)
    live_preflight.add_argument("--executor-revision", required=True)
    promotion = subparsers.add_parser("contest-build-promotion-approval")
    promotion.add_argument("--approval", required=True)
    promotion.add_argument("--receipt", required=True)
    promotion.add_argument("--out", required=True)
    promote = subparsers.add_parser("contest-promote-preflight")
    promote.add_argument("--manifest", required=True)
    promote.add_argument("--receipt", required=True)
    promote.add_argument("--approval", required=True)
    promote.add_argument("--out", required=True)
    dry_run = subparsers.add_parser("contest-dry-run")
    dry_run.add_argument("--manifest", required=True)
    dry_run.add_argument("--out-dir", required=True)
    dry_run.add_argument("--max-workers", type=int, default=1)
    run_study = subparsers.add_parser("contest-run-study")
    run_study.add_argument("--manifest", required=True)
    run_study.add_argument("--out-dir", required=True)
    run_study.add_argument("--max-workers", type=int, default=1)
    screening = subparsers.add_parser("contest-model-screening")
    screening.add_argument("--manifest", required=True)
    screening.add_argument("--approval", required=True)
    screening.add_argument("--out-dir", required=True)
    screening.add_argument("--allow-network", action="store_true")
    screening.add_argument("--executor-revision", required=True)
    public_scan = subparsers.add_parser("contest-public-scan")
    public_scan.add_argument("--root", required=True)


def run_contest_command(args: argparse.Namespace) -> int | None:
    if args.command == "contest-preflight":
        manifest_path = Path(args.manifest)
        manifest = load_candidate_manifest(
            _read_json(manifest_path), base_dir=manifest_path.resolve().parent
        )
        receipt = build_preflight_receipt(manifest)
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8"
        )
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return 0
    if args.command == "contest-live-preflight":
        manifest_path = Path(args.manifest)
        manifest = load_candidate_manifest(
            _read_json(manifest_path), base_dir=manifest_path.resolve().parent
        )
        receipt = run_candidate_preflight(
            manifest,
            authorization=(
                _read_object(Path(args.approval))
                if getattr(args, "approval", None)
                else None
            ),
            executor_revision=getattr(args, "executor_revision", None),
            allow_network=bool(args.allow_network),
        )
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8"
        )
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return 0 if receipt["status"] == "passed" else 1
    if args.command == "contest-build-promotion-approval":
        approval = _read_object(Path(args.approval))
        receipt = _read_object(Path(args.receipt))
        promotion = build_live_preflight_promotion_approval(approval, receipt)
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(promotion, indent=2, sort_keys=True), encoding="utf-8"
        )
        print(json.dumps(promotion, indent=2, sort_keys=True))
        return 0
    if args.command == "contest-promote-preflight":
        manifest_path = Path(args.manifest)
        manifest = load_candidate_manifest(
            _read_json(manifest_path), base_dir=manifest_path.resolve().parent
        )
        receipt = _read_object(Path(args.receipt))
        approval = _read_object(Path(args.approval))
        promoted = promote_live_preflight_receipt(manifest, receipt, approval)
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(promoted, indent=2, sort_keys=True), encoding="utf-8"
        )
        print(json.dumps(promoted, indent=2, sort_keys=True))
        return 0
    if args.command not in {"contest-dry-run", "contest-run-study"}:
        if args.command == "contest-model-screening":
            return run_screening_command(args)
        if args.command == "contest-public-scan":
            report = audit_public_packet(Path(args.root))
            print(json.dumps(report, indent=2, sort_keys=True))
            return 0 if report["ok"] else 1
        return None
    payload = _read_json(Path(args.manifest))
    manifest = load_study_manifest(payload)
    if args.command == "contest-dry-run" and any(
        model.backend != "concordia_first_legal" for model in manifest.models
    ):
        raise ValueError("contest-dry-run accepts only concordia_first_legal models")
    summary = run_matched_study(
        manifest,
        Path(args.out_dir),
        max_workers=getattr(args, "max_workers", 1),
    )
    print(json.dumps(summary["analysis"], indent=2, sort_keys=True))
    return 0


def _read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Could not read study manifest: {path}") from exc


def _read_object(path: Path) -> dict[str, Any]:
    payload = _read_json(path)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return payload


__all__ = ["add_contest_parser", "run_contest_command"]
