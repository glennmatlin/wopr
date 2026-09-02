"""Static QA for the owner-review contest microsite."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

SITE = Path("docs/contest/site")
INDEX = SITE / "index.html"
STYLES = SITE / "styles.css"


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


def _relative_luminance(color: str) -> float:
    channels = (int(color[index : index + 2], 16) / 255 for index in (1, 3, 5))
    linear = tuple(
        value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
        for value in channels
    )
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def _contrast_ratio(foreground: str, background: str) -> float:
    lighter, darker = sorted(
        (_relative_luminance(foreground), _relative_luminance(background)),
        reverse=True,
    )
    return (lighter + 0.05) / (darker + 0.05)


def test_contest_microsite_has_truthful_accessible_structure() -> None:
    text, parser = _page()

    assert parser.h1_count == 1
    assert 'class="skip-link"' in text
    assert 'id="main"' in text
    assert 'type="application/ld+json"' in text
    assert "Put the Room between model choice and World consequence." in text
    assert "This page reports no live DATE run." in text
    assert "It is not model behavior or a live DATE run." in text
    assert "NEXT EMPIRICAL STAGE" in text
    assert 'href="../EVIDENCE_MATRIX.md"' in text
    assert 'content="index, follow"' in text
    assert '<link rel="canonical" href="https://glennmatlin.doctor/wopr/" />' in text
    assert 'content="https://glennmatlin.doctor/wopr/"' in text
    assert 'href="https://github.com/glennmatlin/wopr"' in text
    assert 'href="../M6_CURRENT_STATUS.md"' not in text
    assert "Sounding complete; coverage incomplete" not in text
    assert 'href="#"' not in text


def test_contest_microsite_small_text_palette_meets_wcag_aa() -> None:
    styles = STYLES.read_text(encoding="utf-8")
    colors = dict(re.findall(r"--([\w-]+):\s*(#[0-9a-f]{6});", styles))

    assert _contrast_ratio(colors["amber"], colors["paper"]) >= 4.5
    assert _contrast_ratio(colors["amber"], colors["white"]) >= 4.5


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
