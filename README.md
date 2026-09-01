# WOPR

A machine-operated national-security Situation Room that you can run, inspect,
and replay, evaluated across two deliberately different Worlds.

> Same Room, two Worlds: one open crisis, one closed game, every decision
> traceable.

## The question

Most evaluations of models in strategic settings score an outcome: who won, how
escalatory the final move was, whether the model picked the analyst-approved
option. That collapses an institution into a single response. The thing a real
Situation Room produces is not a move, it is an attributable decision that
survived a process, and the interesting failures live in the process.

So the evaluation unit here is one persistent, complete U.S. Room, not one
model call and not a three-member vote. A versioned Room Charter fixes the
eligible seats, mandates, prohibited actions, information entitlements,
activation rules, product dependencies, decision routes, and required
confirmations. The first U.S. Charter defines 20 eligible seats, 14 of them
active in the first DATE episode. Seat identity and memory persist across
groups and crisis cycles, so a seat that hedged in cycle one is the same seat
that has to live with the consequence in cycle two.

The umbrella question is whether that same Room stays coherent when the World
underneath it changes completely:

> Can the same machine-operated U.S. Situation Room produce coherent,
> attributable, adaptive decisions in both an open-ended DATE crisis and the
> deliberately closed Nuclear War game?

## Two Worlds

| Property | DATE | Nuclear War |
| --- | --- | --- |
| Role | Primary crisis lane | Secondary entertainment contrast |
| Action interface | Natural-language Open Action Proposals | Finite legal moves |
| Consequences | State-bounded generative EXCON plus deterministic admission | Deterministic game engine |
| Main pressure | Open policy formation, uncertainty, synthesis, adaptation | Closed action ontology, hidden information, engine-owned effects |
| Claim boundary | Authenticity-oriented, not fully realistic | Deliberately unrealistic |

The pairing is a cross-World stress test of one institution, not a shared
leaderboard. Nuclear War is a published card game about mutual annihilation
with a spinner in it. That is the point: it is a closed, hostile, fully
adjudicated World where the Room cannot talk its way out of a bad rule, and it
is cheap to run thousands of times. DATE is the open lane where the Room writes
policy in natural language and a bounded generative controller has to decide
what the world does about it.

Nuclear War is one instance of a class, not the class itself. The register of
other game-like environments the project tracks is in
[`docs/contest/GAMES_REGISTER.md`](docs/contest/GAMES_REGISTER.md).

## What actually runs today

I am strict about this separation, because a design document is not a result.

**Verified, in this repository:**

- A deterministic Nuclear War rules engine with replay validation: same seed
  and same actions reconstruct the same run, byte for byte.
- PettingZoo AEC (table play) and Parallel (postal no-press) environments.
- A decision-point contract that hands control to an agent at each choice,
  with random, heuristic, LLM, and Concordia-backed agents behind one interface.
- A Concordia harness, native and HTTP, with a four-rung press ladder from
  no-press to full press, and faction command-and-control for collective
  decisions.
- The U.S. Room vertical slice and the counterpart Rooms, executed
  deterministically with receipt validation and charter dependency graphs.
- 2084 passing tests covering rules fidelity, hidden information, replay
  determinism, PettingZoo API compliance, and the Room contracts.

**Designed and specified, not yet run live:**

- A receipt-valid live DATE episode.
- The same-Room cross-World comparison the umbrella question asks about.

There is no live DATE comparison result in this repository, and nothing here
should be read as one. The evidence boundary as of the last status pass is in
[`docs/contest/CURRENT_STATUS.md`](docs/contest/CURRENT_STATUS.md).

## Quickstart

Requires Python 3.13 and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/glennmatlin/wopr.git
cd wopr
uv sync --extra dev
```

Check that the rules engine agrees with its own source ledger, then play a
deterministic game and read it back:

```bash
uv run nuclear-war validate-rules
uv run nuclear-war simulate --mode table --players 3 --seed 1 --agent heuristic --out run.json
uv run nuclear-war summarize run.json
uv run nuclear-war replay run.json
```

Run a batch, which is the unit most experiments use:

```bash
uv run nuclear-war experiment --mode table --players 3 --seed-start 1 --runs 100 --agent heuristic --out batch.json
```

Run the test suite:

```bash
WOPR_REQUIRE_CONCORDIA=1 uv run --extra dev python -m pytest -o addopts="" -q
```

`WOPR_REQUIRE_CONCORDIA=1` turns a missing or broken `gdm-concordia` install
into a hard failure instead of a silent module-level skip, so the native
Concordia path cannot quietly stop being covered.

`nuclear-war --help` lists the full command surface, including the contest
runner, model screening, preflight, and the public-release scanner.

## Repository map

| Path | What is in it |
| --- | --- |
| `src/nuclear_war_env/` | Deterministic rules engine, decision contract, PettingZoo environments, CLI |
| `src/nuclear_war_agents/` | Random, heuristic, interactive, and LLM agents behind one interface |
| `src/nuclear_war_concordia/` | Concordia harness, press ladder, faction C2, native and HTTP model paths |
| `src/nuclear_war_contest/` | Situation Room runner, manifests, receipts, screening, preflight |
| `tests/` | 2084 tests: rules, hidden information, replay, API compliance, Room contracts |
| `rules/` | Machine-readable rule and card metadata |
| `research/` | Source provenance bundle the engine validates against |
| `docs/contest/` | The Situation Room design: 47 ADRs, 20 specification documents, charters, receipts |
| `docs/specs/` | Engine and harness design documents |
| `docs/examples/` | Runnable configuration examples for every harness path |
| `visualizer/` | React replay debugger for engine runs and decision traces |

## The design trail

The strongest thing in this repository is not the engine, it is the record of
how the design got here. Every consequential choice is an ADR with the
alternatives that lost and the reason:
[`docs/contest/adr/`](docs/contest/adr/), 47 of them, from
[0001 one packet Nuclear War world](docs/contest/adr/0001-one-packet-nuclear-war-world.md)
through the DATE pivot at
[0010](docs/contest/adr/0010-pivot-to-date-situation-room-arena.md)
to
[0047 build the U.S. vertical slice before counterpart Rooms](docs/contest/adr/0047-build-the-us-vertical-slice-before-counterpart-rooms.md).

Start here:

1. [Current design](docs/contest/CURRENT_DESIGN.md), the Room, the two World
   contracts, and the evaluation boundary.
2. [Glossary](docs/contest/CONTEXT.md), which defines Room, World, Charter,
   Seat, Setup, and the rest of the vocabulary precisely.
3. [Situation Room specification](docs/contest/SITUATION_ROOM_SPEC.md).
4. [Decision crosswalk](docs/contest/DECISION_CROSSWALK.md), which maps every
   recorded choice into the live glossary, ADRs, and specification.
5. [Engine and harness design documents](docs/specs/) for the internals, and
   [`docs/AGENT_HANDOFF.md`](docs/AGENT_HANDOFF.md) for the build chronology.

## Paper

The deterministic engine, the decision-point contract, the Concordia harness,
the press ladder, and faction C2 are described in "No One Wins in Nuclear War"
([arXiv:2608.01868](https://arxiv.org/abs/2608.01868)), accepted to the Social
Simulation workshop at COLM 2026. The paper covers the instrument. The
two-World Situation Room program in `docs/contest/` is newer than the paper and
is not described in it.

## License and rights

The code is MIT licensed. *Nuclear War* is a published card game owned by its
publisher; this project implements a rules engine and ships derived effect
summaries with recorded provenance, never rulebook scans or exact card text.
The DATE crisis material is fictional. See [NOTICE.md](NOTICE.md) for the full
rights statement and [`docs/source_research_policy.md`](docs/source_research_policy.md)
for the sourcing rules.
