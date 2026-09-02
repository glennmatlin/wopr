# M2 offline matched-study receipt

The checked-in dry-run manifest exercises all four communication and command-authority cells
with two matched engine seeds and one deterministic `concordia_first_legal` backend. It is a
pipeline fixture, not a model result and not a frozen provider manifest.

```bash
cd nuclear_war
uv run nuclear-war contest-dry-run \
  --manifest docs/contest/STUDY_MANIFEST.dry_run.json \
  --out-dir /tmp/wopr-contest-dry-run
```

The runner writes `STUDY_MANIFEST.json`, an append-only `run_ledger.jsonl`, one immutable
attempt directory per cell, validated WOPR replay and Concordia sidecars, `analysis.json`, and
`study_summary.json`. A second invocation reads terminal attempt receipts, adds no ledger lines,
and does not rerun or overwrite completed cells.

The offline gate currently covers eight cells, eight Tier A attempts, four paired seed-level
records for the two preregistered primary contrasts, and ten Tier A exploratory records that
include the two additional cellwise contrasts plus the factorial interaction. The tests also
exercise Tier B output-reprompt handling, Tier C fallback and runner failure handling, manifest
factor validation, and the no-overwrite resume path.

The dry run deliberately refuses any model backend other than `concordia_first_legal`. Live
provider execution remains a separate owner-authorized step after the model manifest, request
budget, and credential path are frozen.
