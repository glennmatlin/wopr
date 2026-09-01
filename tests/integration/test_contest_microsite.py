"""Static QA for the owner-review contest microsite."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

SITE = Path("docs/contest/site")
INDEX = SITE / "index.html"


class _LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h1":
            self.h1_count += 1
        self.hrefs.extend(value for name, value in attrs if name == "href" and value)


def _page() -> tuple[str, _LinkParser]:
    text = INDEX.read_text(encoding="utf-8")
    parser = _LinkParser()
    parser.feed(text)
    return text, parser


def test_contest_microsite_has_truthful_accessible_structure() -> None:
    text, parser = _page()

    assert parser.h1_count == 1
    assert 'class="skip-link"' in text
    assert 'id="main"' in text
    assert 'type="application/ld+json"' in text
    assert "Sounding complete; coverage incomplete" in text
    assert "Six Tier-C cells and the failed Demo limit downstream comparisons." in text
    assert "access-controlled" in text
    assert 'href="#"' not in text


def test_contest_microsite_local_artifact_links_resolve() -> None:
    _, parser = _page()

    for href in parser.hrefs:
        if href.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = (SITE / href.split("#", 1)[0]).resolve()
        assert target.exists(), href


def test_contest_markdown_relative_links_resolve() -> None:
    root = SITE.parent
    for path in root.glob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if target:
                assert (path.parent / target).resolve().exists(), (path, target)
