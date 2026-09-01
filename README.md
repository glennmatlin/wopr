# Nuclear War

I am building a deterministic implementation of Nuclear War for repeatable
game runs and experiments. The package also contains the ChinaTalk Situation
Room entry, which uses a separate DATE-backed crisis World and treats Nuclear
War as a later closed-form comparison.

## Situation Room contest entry

The current contest contribution is an institutional U.S. Room with distinct
seats and mandates, selective information, working groups, preserved dissent,
two decision cycles, open policy proposals, a constrained interpreter, and
World-owned consequences. The realistic DATE evaluation is specified but not
completed. The repository contains the working offline scaffold and only the
evidence claimed in the
[`contest Packet`](docs/contest/README.md) and
[`evidence matrix`](docs/contest/EVIDENCE_MATRIX.md).

The historical v1 engine remains separate: language-model integration does not
change the deterministic Nuclear War rules engine or its replay contract.

## Start Here

For the contest release, begin with the linked Packet and evidence matrix. The
private engineering checkout retains its separate agent handoff and broader
engine history.

## V1 Target

- Table play through a PettingZoo AEC environment.
- Postal no-press play through a PettingZoo Parallel environment.
- Scriptable CLI commands for rule validation, simulation, replay, and summaries.
- Random and heuristic agents for baseline experiments.
- Replay-safe JSON logs with seeds, actions, events, winner, final populations, and termination reason.
- Tests that cover rules, hidden information, CLI behavior, PettingZoo compliance, and reproducibility.

## CLI

The package exposes `nuclear-war`.

```bash
nuclear-war validate-rules
nuclear-war simulate --mode table --players 3 --seed 1 --agent random --max-turns 50 --out run.json
nuclear-war simulate --mode postal --players 3 --seed 1 --agent heuristic --out run.json
nuclear-war experiment --mode table --players 3 --seed-start 1 --runs 10 --agent random --out batch.json
nuclear-war replay run.json
nuclear-war summarize run.json
```

## Development

1. Install dependencies: `uv pip install --system -e ".[dev]"`. The dev extra
   includes the `concordia` extra (`gdm-concordia`), so the native Concordia
   tests run.
2. Run tests: `pytest`. The only expected skips are the two live-endpoint
   smokes that need model env vars.
3. Run lint: `ruff check src tests`
4. Run type checks: `pyright`
5. Run guardrails: `scripts/validate-phase`

The current implementation keeps deterministic rules in `nuclear_war_env`. PettingZoo, CLI, and agents are interfaces around that engine. They do not resolve rules independently. Rule coverage is tracked in `docs/rule_fidelity_matrix.md`.

## Research Sources

Imported source bundles live under `research/imports/`. The current source
policy is documented in `docs/source_research_policy.md`.

The v1 engine uses effect summaries and confidence-tracked card metadata. It
does not publish exact card text or treat community card lists as authoritative
wording.

The 2026-06-14 research bundle is the current source import.
`nuclear-war validate-rules` loads IDs from the imported `source_index.json`
and reports unresolved source labels so the active registry stays tied to the
bundle source ledger.
