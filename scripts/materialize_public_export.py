"""Materialize an explicit, Git-tracked contest export."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
from pathlib import Path

from public_export_git import GitBlob, committed_tree, read_blob

RECEIPT_NAME = "PUBLIC_EXPORT_RECEIPT.json"
_HARD_FORBIDDEN_GLOBS = (
    "outputs/**", "**/outputs/**", "LOGBOOK.md", "**/LOGBOOK.md",
    "rules/**", "**/rules/**", "research/imports/**", "**/research/imports/**",
    ".env", ".env.*", "**/.env", "**/.env.*",
    "*AUTHORIZATION*", "**/*AUTHORIZATION*", "*PREFLIGHT*", "**/*PREFLIGHT*",
    "*PROMOTION*", "**/*PROMOTION*", "*LIVE*PACKET*", "**/*LIVE*PACKET*",
    "D95_*", "**/D95_*", "D101_*", "**/D101_*", "**/M6_CURRENT_STATUS.md",
    "*.jsonl", "**/*.jsonl", "private/**", "**/private/**", "stage/**",
    "stages/**", "**/stage/**", "**/stages/**", "**/*private*stage*",
)
ExportError = ValueError

def materialize_export(
    source_root: Path | str,
    manifest_path: Path | str,
    destination: Path | str,
    source_revision: str,
) -> Path:
    """Copy committed matches and return a deterministic file-hash receipt."""
    root = Path(source_root).expanduser().resolve()
    if not root.is_dir():
        raise ExportError(f"source root is not a directory: {root}")
    manifest = _relative_path(root, manifest_path)
    target = Path(destination).expanduser()
    if target.exists() or target.is_symlink():
        raise ExportError("destination must not exist")
    target = target.resolve()
    if target.exists() or not target.parent.is_dir():
        raise ExportError("destination must be nonexistent with an existing parent")
    if target.is_relative_to(root):
        raise ExportError("destination must be outside source root")
    tree_hash, tree = committed_tree(root, source_revision)
    manifest_blob = tree.get(manifest.as_posix())
    if manifest_blob is None:
        raise ExportError("manifest is absent from the source revision")
    manifest_bytes = read_blob(root, manifest_blob)
    include, forbidden = _load_manifest(manifest_bytes)
    selected = _select(tree, include, forbidden)
    target.mkdir()
    entries = []
    for relative, blob in selected:
        data = read_blob(root, blob)
        output = target / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as stream:
            stream.write(data)
        output.chmod(0o755 if blob.mode == "100755" else 0o644)
        entries.append({"path": relative.as_posix(), "bytes": len(data),
                        "sha256": hashlib.sha256(data).hexdigest(),
                        "git_blob": blob.object_id, "git_mode": blob.mode})
    receipt = {
        "schema_version": "contest-public-export-receipt.v1",
        "source_revision": source_revision,
        "source_tree": tree_hash,
        "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "file_count": len(entries),
        "files": entries,
    }
    receipt_path = target / RECEIPT_NAME
    with receipt_path.open("x", encoding="utf-8") as stream:
        json.dump(receipt, stream, indent=2, sort_keys=True)
        stream.write("\n")
    return receipt_path


def _relative_path(root: Path, value: Path | str) -> Path:
    path = Path(value).expanduser()
    absolute = path.absolute() if path.is_absolute() else (root / path).absolute()
    try:
        return absolute.relative_to(root)
    except ValueError as exc:
        raise ExportError("manifest must be inside source root") from exc


def _load_manifest(raw: bytes) -> tuple[tuple[str, ...], tuple[str, ...]]:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ExportError("manifest is not valid JSON") from exc
    if not isinstance(payload, dict):
        raise ExportError("manifest must be a JSON object")
    if payload.get("schema_version") != "contest-public-export.v1":
        raise ExportError("manifest schema_version is unsupported")
    if payload.get("path_basis") != "source_root_relative":
        raise ExportError("manifest path_basis must be source_root_relative")
    return _patterns(payload, "include_globs", True), _patterns(
        payload, "forbidden_globs", False
    )


def _patterns(payload: dict[str, object], name: str, required: bool) -> tuple[str, ...]:
    value = payload.get(name)
    if not isinstance(value, list) or (required and not value):
        raise ExportError(f"manifest {name} must be a non-empty list")
    if any(not isinstance(item, str) for item in value):
        raise ExportError(f"manifest {name} must contain strings")
    return tuple(value)


def _select(
    tree: dict[str, GitBlob], include: tuple[str, ...], forbidden: tuple[str, ...]
) -> tuple[tuple[Path, GitBlob], ...]:
    selected: set[str] = set()
    for pattern in include:
        matches = [path for path in tree if fnmatch.fnmatchcase(path, pattern)]
        if not matches:
            raise ExportError(f"include glob matched no tracked files: {pattern}")
        for path in matches:
            if _forbidden(path, forbidden):
                raise ExportError(f"forbidden export match: {path}")
        selected.update(matches)
    return tuple((Path(path), tree[path]) for path in sorted(selected))


def _forbidden(path: str, manifest_globs: tuple[str, ...]) -> bool:
    patterns = _HARD_FORBIDDEN_GLOBS + manifest_globs
    return any(
        fnmatch.fnmatchcase(path.upper(), pattern.upper()) for pattern in patterns
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source-root", "manifest", "destination", "source-revision"):
        parser.add_argument(f"--{name}", required=True)
    args = parser.parse_args(argv)
    try:
        receipt = materialize_export(
            args.source_root, args.manifest, args.destination, args.source_revision
        )
    except (ExportError, OSError) as exc:
        parser.error(str(exc))
    print(receipt)


if __name__ == "__main__":
    raise SystemExit(main())
