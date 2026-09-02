"""End-to-end check for the committed contest export."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from nuclear_war_contest.public_scan import audit_public_packet

PROJECT = Path(__file__).parents[2]
SCRIPT = PROJECT / "scripts" / "materialize_public_export.py"
sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location("public_export_release", SCRIPT)
assert SPEC and SPEC.loader
public_export = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(public_export)


def test_committed_export_runs_the_scripted_room_without_closed_engine(
    tmp_path: Path,
) -> None:
    revision = _git("rev-parse", "HEAD")
    destination = tmp_path / "export"
    public_export.materialize_export(
        PROJECT,
        PROJECT / "docs" / "contest" / "PUBLIC_EXPORT_MANIFEST.json",
        destination,
        revision,
    )

    assert (destination / "LICENSE").read_text().startswith("MIT License\n")
    _assert_release_metadata(destination)
    _assert_repository_navigation(destination)
    scan = audit_public_packet(destination)
    assert scan["ok"] is True, scan
    assert not (destination / "src" / "nuclear_war_env").exists()
    runner = destination / "scripts" / "run_public_room_rehearsal.py"
    assert runner.is_file()
    output = tmp_path / "rehearsal.json"
    subprocess.run(
        [
            sys.executable,
            "-c",
            _isolated_program(destination, runner, revision, output),
        ],
        check=True,
        cwd=destination,
    )
    receipt = json.loads(output.read_text())
    assert receipt["status"] == "passed"
    assert receipt["evidence_status"] == "scripted_rehearsal_non_evidence"
    assert receipt["call_counts"]["total"] == 114
    assert receipt["replay_matched"] is True


def _assert_release_metadata(destination: Path) -> None:
    contest = destination / "docs" / "contest"
    application = (contest / "APPLICATION_DRAFT.md").read_text()
    checklist = (contest / "PUBLIC_RELEASE_CHECKLIST.md").read_text()
    site = (contest / "site" / "index.html").read_text()
    manifest = json.loads((contest / "PUBLIC_EXPORT_MANIFEST.json").read_text())
    rights_register = (contest / "SOURCE_RIGHTS_REGISTER.md").read_text()
    evidence_spec = (contest / "spec" / "08-sources-and-evidence.md").read_text()

    for text in (application, checklist, site):
        assert "https://glennmatlin.doctor/wopr/" in text
        assert "https://github.com/glennmatlin/wopr" in text
    assert "Yes, part time" in application
    assert "www.linkedin.com/in/" not in application
    assert 'content="index, follow"' in site
    assert manifest["publication_status"] == "owner_cleared_for_publication"
    assert "LICENSE" in manifest["include_globs"]
    assert "docs/contest/SOURCE_RIGHTS_REGISTER.md" in manifest["include_globs"]
    assert "SRC_DATE_OLV_MILITARY" in rights_register
    assert "SRC_ROAD_TO_WAR" in rights_register
    assert "Version or date metadata" in rights_register
    assert "Faithful paraphrase" in rights_register
    assert "[RESOLVED 2026-09-01]" in evidence_spec
    assert "That rights review is OPEN" not in evidence_spec
    assert not (destination / "outputs").exists()


def _assert_repository_navigation(destination: Path) -> None:
    readme = (destination / "README.md").read_text()
    navigation_files = (
        "HISTORY.md",
        "ARCHITECTURE.md",
        "worlds/README.md",
        "worlds/date/README.md",
        "worlds/nuclear-war/README.md",
        "situation-room/README.md",
        "docs/README.md",
        "src/README.md",
        "tests/README.md",
    )
    export_only_indexes = (
        "docs/archive/README.md",
        "docs/archive/chinatalk-pre-deadline/README.md",
        "tests/integration/test_contest_microsite.py",
        "tests/integration/test_public_export_release.py",
        "tests/integration/test_repository_navigation.py",
    )

    assert readme.startswith("# WOPR\n")
    for relative_path in navigation_files:
        assert (destination / relative_path).is_file()
        assert relative_path in readme
    for relative_path in export_only_indexes:
        assert (destination / relative_path).is_file()

    architecture = (destination / "ARCHITECTURE.md").read_text().lower()
    assert "same-room comparison" in architecture
    assert "not yet run" in architecture


def _isolated_program(
    destination: Path, runner: Path, revision: str, output: Path
) -> str:
    private_source = str(PROJECT / "src")
    export_source = str(destination / "src")
    fixture = str(
        destination / "docs" / "contest" / "US_TWO_CYCLE_FIXTURE.development.json"
    )
    argv = [str(runner), fixture, revision, str(output)]
    return (
        "import runpy, sys; "
        f"sys.path = [p for p in sys.path if p != {private_source!r}]; "
        f"sys.path.insert(0, {export_source!r}); "
        f"sys.argv = {argv!r}; "
        f"runpy.run_path({str(runner)!r}, run_name='__main__')"
    )


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(PROJECT), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
