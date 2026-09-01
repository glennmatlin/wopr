# Situation Room contest Packet

This Packet presents an evidence-honest evaluation design centered on a
machine-operated U.S. Situation Room. The first episode places that Room in an
open-ended Himaldesh-Olvana nuclear crisis built with DATE concepts. A later
comparison will place the same Room in the closed Nuclear War game.

## Read the entry

1. [`EVIDENCE_MATRIX.md`](EVIDENCE_MATRIX.md) separates what is implemented,
   executed, specified, and still unverified.
2. [`EPISODE_1.md`](EPISODE_1.md) explains the crisis, Room, information path,
   two cycles, proposal contract, interpreter, and World consequences.
3. [`PROTOCOL.md`](PROTOCOL.md) defines the evaluation and its claim boundary.
4. [`APPLICATION_DRAFT.md`](APPLICATION_DRAFT.md) contains the final form copy
   and publication fields.
5. [`site/index.html`](site/index.html) is the static microsite source.

The private working repository retains the consolidated specification,
decision crosswalk, appendices, and full ADR history. The curated release keeps
the deadline pivot in
[`ADR 0075`](adr/0075-cut-the-experiment-and-package-the-evidence-boundary.md)
and the Episode 1 decisions linked from the episode packet without making the
engineering chronology the public entry point.

## Run the offline Room rehearsal

From `nuclear_war/`, install the development environment and run the checked-in
two-cycle fixture through all 114 scripted Room calls:

```bash
uv sync --extra concordia
REVISION="$(git rev-parse HEAD)"
uv run python scripts/run_public_room_rehearsal.py \
  docs/contest/US_TWO_CYCLE_FIXTURE.development.json \
  "$REVISION" \
  /tmp/us-room-rehearsal.json
```

Dependency installation may require network access the first time. The
rehearsal command itself performs no provider or network call. It validates selective
information delivery, attributable portfolio and group products, two Room
cycles, open-proposal materialization, deterministic World admission, and
exact replay. Its output is implementation evidence, not model behavior or a
completed DATE evaluation.

The curated launcher exposes the two model-protocol types required by the
frozen Room modules without changing their byte-bound imports or adding the
closed Nuclear War engine to the export.

## Materialize the curated public release

After committing the intended release bytes, materialize only the allowlisted
files from that exact commit into a new directory outside the checkout:

```bash
REVISION="$(git rev-parse HEAD)"
uv run python scripts/materialize_public_export.py \
  --source-root . \
  --manifest docs/contest/PUBLIC_EXPORT_MANIFEST.json \
  --destination /tmp/wopr-contest-public \
  --source-revision "$REVISION"
```

The exporter reads Git blobs from the named commit, not mutable working-tree
files. Its receipt binds the commit, tree, manifest, file modes, blob objects,
and content hashes. The destination must not already exist.

The checked-in manifest records the owner's MIT-license and source-rights
decision. Each publication still uses a new exact-commit export, receipt, secret
scan, link check, and offline rehearsal before the public repository is updated.

## Publication boundary

The repository checkout remains a private working repository. The curated
contest release excludes credentials, `.env` files, private output trees,
provider stages, raw provider material, and historical rules or source PDFs.
See
[`PUBLIC_RELEASE_CHECKLIST.md`](PUBLIC_RELEASE_CHECKLIST.md) and
[`SOURCE_RIGHTS_INVENTORY.md`](SOURCE_RIGHTS_INVENTORY.md) before publishing.
