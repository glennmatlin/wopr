"""Check the public repository's current-versus-history boundary."""

import re
from pathlib import Path

PROJECT = Path(__file__).parents[2]
ARCHIVE = PROJECT / "docs" / "archive" / "chinatalk-pre-deadline"

PRE_DEADLINE_FILES = (
    "COMPOSITION_SMOKE.md",
    "CURRENT_DESIGN.md",
    "CURRENT_STATUS.md",
    "M2_DRY_RUN.md",
    "M3_MODEL_DECISION_PACKET.md",
    "M3_MODEL_PREFLIGHT.md",
    "M3_PROMOTION.md",
    "M3_SCREENING.md",
)


def test_pre_deadline_status_package_is_archived() -> None:
    for name in PRE_DEADLINE_FILES:
        assert not (PROJECT / "docs" / "contest" / name).exists()
        assert (ARCHIVE / name).is_file()


def test_current_and_historical_entry_points_are_distinct() -> None:
    history = (PROJECT / "HISTORY.md").read_text()
    handoff = (PROJECT / "docs" / "AGENT_HANDOFF.md").read_text()

    assert "docs/contest/README.md" in history
    assert "docs/archive/chinatalk-pre-deadline/README.md" in history
    assert "CURRENT_DESIGN.md" not in "\n".join(handoff.splitlines()[:20])
    assert "contest/README.md" in "\n".join(handoff.splitlines()[:30])


def test_archive_markdown_links_resolve() -> None:
    documents = [PROJECT / "HISTORY.md", PROJECT / "docs" / "archive" / "README.md"]
    documents.extend(ARCHIVE.glob("*.md"))
    for document in documents:
        for link in re.findall(r"\]\(([^)]+)\)", document.read_text()):
            if link.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = link.split("#", 1)[0].split("?", 1)[0]
            assert (document.parent / target).exists(), f"{document}: {link}"
