"""Check the public repository's reader-facing navigation."""

import re
from pathlib import Path

PROJECT = Path(__file__).parents[2]

NAVIGATION_FILES = (
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

ARCHIVE_INDEX_FILES = (
    "docs/archive/README.md",
    "docs/archive/chinatalk-pre-deadline/README.md",
)


def test_repository_has_world_and_room_entry_points() -> None:
    readme = (PROJECT / "README.md").read_text()

    assert readme.startswith("# WOPR\n")
    for relative_path in NAVIGATION_FILES:
        assert (PROJECT / relative_path).is_file()
        assert relative_path in readme


def test_navigation_maps_point_to_the_implemented_modules() -> None:
    date_map = (PROJECT / "worlds" / "date" / "README.md").read_text()
    nuclear_war_map = (PROJECT / "worlds" / "nuclear-war" / "README.md").read_text()
    room_map = (PROJECT / "situation-room" / "README.md").read_text()
    architecture = (PROJECT / "ARCHITECTURE.md").read_text()

    assert "docs/contest/EPISODE_1.md" in date_map
    assert "docs/contest/EVIDENCE_MATRIX.md" in date_map
    assert "src/nuclear_war_contest/date_world" in date_map
    assert "src/nuclear_war_env" in nuclear_war_map
    assert "src/nuclear_war_contest/situation_room" in room_map
    assert "src/nuclear_war_contest/date_world" in architecture
    assert "src/nuclear_war_env" in architecture


def test_navigation_states_the_cross_world_evidence_boundary() -> None:
    architecture = (PROJECT / "ARCHITECTURE.md").read_text().lower()

    assert "not yet run" in architecture
    assert "same-room comparison" in architecture


def test_local_links_in_navigation_files_resolve() -> None:
    for relative_path in ("README.md", *NAVIGATION_FILES, *ARCHIVE_INDEX_FILES):
        document = PROJECT / relative_path
        for link in re.findall(r"\]\(([^)]+)\)", document.read_text()):
            if link.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = link.split("#", 1)[0].split("?", 1)[0]
            assert (document.parent / target).exists(), f"{relative_path}: {link}"
