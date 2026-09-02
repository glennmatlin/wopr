# WOPR architecture

WOPR separates the decision institution from the World that resolves its
actions. This keeps the Room's seats, information boundaries, working groups,
and policy products stable while the action grammar and consequence machinery
can change by World.

## Runtime map

```text
Situation Room
  source registers -> Charter -> seats and portfolios -> two Room cycles
  -> Open Action Proposal -> proposal bridge

DATE World
  proposal bridge -> fail-closed interpreter -> World validator
  -> Core and ledger -> EXCON/MSEL consequences -> exact replay

Nuclear War World
  bounded game action -> deterministic rules engine -> event log -> replay
```

## Module ownership

| Concern | Current implementation |
| --- | --- |
| Shared institutional Room | `src/nuclear_war_contest/situation_room` |
| Open DATE World | `src/nuclear_war_contest/date_world` |
| Closed Nuclear War World | `src/nuclear_war_env` |
| Decision and model adapters | `src/nuclear_war_agents`, `src/nuclear_war_concordia` |
| Contest release and validation | `src/nuclear_war_contest`, `scripts/` |

The directories under [`worlds/`](worlds/README.md) and
[`situation-room/`](situation-room/README.md) are reader maps. They do not
duplicate or wrap the source packages. Physical package moves are deferred so
the deadline reorganization does not break imports, receipts, or replay paths.

## Interface boundaries

1. A Room Charter defines seats, mandates, information entitlements, groups,
   routing, and record duties. A Crisis Setup does not redefine those
   institutional boundaries.
2. Seats produce attributable, open-ended advice. The Room produces a policy
   package without granting itself authority or changing World state.
3. The proposal bridge preserves original language, ordered effects,
   clarifications, rejected components, and authority/capability records.
4. The World validator is the only component that admits a consequence or
   applies a typed state patch. Unsupported fields fail closed.
5. A World owns its state, action grammar, consequences, terminal conditions,
   and replay. The Room does not secretly resolve them.

## Evidence boundary

The offline DATE kernel, Room controllers, proposal bridge, validation, and
replay seams are implemented and have retained development receipts. Creative
live EXCON behavior, a complete live DATE Room, and the same-Room comparison
between DATE and Nuclear War are not yet run. The
[evidence matrix](docs/contest/EVIDENCE_MATRIX.md) governs every public claim.

## Intended dependency direction

The shared Room may depend on small adapter protocols, but it must not import a
World's private state transition logic. Each World consumes a Room disposition
through an explicit boundary and returns observations or consequences through
its own contract. This is the post-deadline target for any physical namespace
cleanup; the current package names remain the verified implementation.
