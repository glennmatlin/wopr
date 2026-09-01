# Three-model screening packet

Status: the authorized 2026-08-16 screen completed nine cells. Six cells were
Tier A and the three Qwen3.5 cells were terminal Tier C; the deterministic
selection retained DeepSeek V4 Flash and GPT-OSS 20B. This packet records the
screening controls and decision rule; the retained pair is captured separately
in the pair-specific candidate and offline preflight receipt.

## Purpose

This packet is an upstream screening run, not the frozen contest study. It
keeps three inexpensive model families in the same bounded press-light lane so
we can decide whether two or all three should enter the full institutional
sensitivity design. The checked-in final candidate manifest remains a separate
two-model historical artifact; the retained pair now has a pair-specific
candidate packet.

## Frozen screening controls

- Models: `openai/gpt-oss-20b`,
  `deepseek-ai/DeepSeek-V4-Flash-0731`, and `Qwen/Qwen3.5-9B`.
- Seeds: 101, 102, and 103 for screening; 51-55 remain reserved for the
  eventual five-seed study.
- Communication mode: `press_light`, with four seats, three turns, streaming,
  temperature 0.7, 512 output tokens, and reasoning disabled.
- Retry policy: one output retry and a transport-retry margin of two.
- The executable backend, endpoint, timeout, credential variable name, client
  settings, and role-prompt hashes are pinned in
  `MODEL_SCREENING.candidate.json`. The loader also binds the catalog and final
  two-model candidate plus the planning budget by SHA-256 before a runner can
  consume the packet, and it rejects a budget upper bound above $1,000.

Validate the packet without network access from `nuclear_war/`:

```bash
UV_CACHE_DIR=/tmp/wopr-uv-cache uv run python -c \
  'from pathlib import Path; from nuclear_war_contest import load_screening_manifest_file; load_screening_manifest_file(Path("docs/contest/MODEL_SCREENING.candidate.json"))'
```

## Approval-gated runner

The executable screen is `contest-model-screening`. It refuses a pending or
mis-bound approval before creating the output directory, and it requires both
the explicit network flag and a clean executor revision. The approval file is
redacted and contains only the screening manifest hash, exact model IDs,
endpoints, credential-environment names, an approved maximum spend, and the
executor SHA.

```bash
cd nuclear_war
uv run nuclear-war contest-model-screening \
  --manifest docs/contest/MODEL_SCREENING.candidate.json \
  --approval /path/to/screening-approval.json \
  --out-dir /path/to/screening-run \
  --allow-network \
  --executor-revision <full-executor-sha>
```

The runner creates nine resumable attempt receipts, one per model and seed,
with the ordinary replay, trace, C2, press, runtime, and budget sidecars. A
retry reuses the existing attempt directory and preserves the prior receipt;
all current receipts are revalidated before another request is dispatched.
The completed `screening_summary.json` also contains a deterministic selection
report. It marks models ineligible for failed, Tier C, fallback, provider-error,
or incomplete operational receipts, then ranks eligible models using the frozen
retention rule below.

The provider model identifiers are retained here because they are the exact
configuration keys required for reproducible screening; all three screening
models use Together and `TOGETHER_API_KEY`. The external screening approval
authorized the completed run, but this packet does not authorize a rerun or
read the credential.

The screen measures direct response validity, legal-action parsing, replay and
trace completeness, press behavior, declines, retries, and provider usage. It
does not estimate the contest's no-press/full-press contrast or authority
contrast.

## Frozen model-retention rule

The screen is judged on operational validity rather than strategic behavior.
Each model must have three validated, non-Tier-C attempts with replay, trace,
C2, and press sidecars and no fallback or provider error. Among eligible
models, the decision packet ranks total output reprompts, recoverable transport
retries, provider attempts, and actual cost in that order, with the provider ID
as a deterministic tie-break. Message content, winners, escalation, and other
behavioral measures are excluded from selection. The default study retains the
top two eligible families; retaining all three requires a protocol amendment,
an updated bound below the owner's $1,000 ceiling, and a new approval.

## Spend boundary

This packet records the owner's $1,000 total ceiling. The checked-in planning
packet records no network calls and no credential reads; the completed screen's
attempt receipts are retained in the run output and are not an approval for a
future run.

## Decision after screening

The completed screening retained DeepSeek V4 Flash and GPT-OSS 20B for the
existing `2 x 2 x 2 x 5` study. The eventual study keeps matched seeds 51-55
and the four institutional cells: no press/sole authority, full press/sole
authority, no press/council, and full press/council. The pair-specific live
preflight remains the next approval-gated evidence step.
