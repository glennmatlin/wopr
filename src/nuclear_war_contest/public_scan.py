"""Read-only checks for the local contest packet before publication."""

from __future__ import annotations

import re
from collections.abc import Iterable
from html.parser import HTMLParser
from pathlib import Path

_SECRET_PATTERNS = (
    re.compile(r"\bsk-[A-Za-z0-9][A-Za-z0-9_-]{19,}\b"),
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._-]{20,}\b"),
    re.compile(
        r'(?i)["\'](?:api[_-]?key|access[_-]?token|password)["\']\s*:'
        r'\s*["\'][^"\']{16,}["\']'
    ),
)
_PRIVATE_PATH_PATTERNS = (
    re.compile(r"(?<![A-Za-z0-9_])/(?:private/(?:tmp|var)|Users|home)/"),
    re.compile(r"(?i)\b[A-Z]:\\Users\\"),
)
_EXCLUDED_PARTS = frozenset({"private", "licensed_source", "source_material"})


class _HTMLLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            self.links.extend(
                value for name, value in attrs if name == "href" and value
            )


def audit_public_packet(root: Path) -> dict[str, object]:
    """Return deterministic, non-network findings for a candidate public packet."""
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"Public packet root is not a directory: {root}")
    findings: list[str] = []
    warnings: list[str] = []
    links_checked = 0
    files = sorted(path for path in root.rglob("*") if path.is_file())
    for path in files:
        relative = path.relative_to(root)
        if _excluded(relative):
            findings.append(f"excluded path: {relative}")
        text = path.read_text(encoding="utf-8", errors="replace")
        findings.extend(_secret_findings(relative, text))
        findings.extend(_private_path_findings(relative, text))
        links = _links(path, text)
        links_checked += len(links)
        link_findings, link_warnings = _link_findings(root, path, links)
        findings.extend(link_findings)
        warnings.extend(link_warnings)
    return {
        "root": str(root),
        "files_scanned": len(files),
        "local_links_checked": links_checked,
        "findings": findings,
        "warnings": sorted(set(warnings)),
        "ok": not findings,
    }


def _excluded(path: Path) -> bool:
    return any(
        part in _EXCLUDED_PARTS or part.startswith(".env") for part in path.parts
    )


def _secret_findings(path: Path, text: str) -> list[str]:
    return [
        f"credential-like value: {path}:{line_number}"
        for line_number, line in enumerate(text.splitlines(), 1)
        if any(pattern.search(line) for pattern in _SECRET_PATTERNS)
    ]


def _private_path_findings(path: Path, text: str) -> list[str]:
    return [
        f"private absolute path: {path}:{line_number}"
        for line_number, line in enumerate(text.splitlines(), 1)
        if any(pattern.search(line) for pattern in _PRIVATE_PATH_PATTERNS)
    ]


def _links(path: Path, text: str) -> list[str]:
    if path.suffix.lower() in {".html", ".htm"}:
        parser = _HTMLLinks()
        parser.feed(text)
        return parser.links
    return re.findall(r"\]\(([^)]+)\)", text)


def _link_findings(
    root: Path, path: Path, links: Iterable[str]
) -> tuple[list[str], list[str]]:
    findings: list[str] = []
    warnings: list[str] = []
    for link in links:
        if link.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = link.split("#", 1)[0].split("?", 1)[0]
        resolved = (path.parent / target).resolve()
        if target and not resolved.exists():
            findings.append(f"broken local link: {path}:{link}")
        elif target and not resolved.is_relative_to(root):
            warnings.append(f"local checkout link: {path}:{link}")
    return findings, warnings


__all__ = ["audit_public_packet"]
