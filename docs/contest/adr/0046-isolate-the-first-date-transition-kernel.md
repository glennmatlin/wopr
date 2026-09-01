# Isolate the first DATE transition kernel

Status: proposed implementation default D62 under D60; no executable claim

The first DATE tracer will use a small pure transition kernel under `nuclear_war_contest.date_world`, separate from both the closed Nuclear War `GameState` and the Concordia Room harness. It will own only candidate-profile loading, a typed episode Core, fixed-envelope ledger entries, semantic patch operations, fail-closed validation, canonical hashes, and replay. This proves the World-state seam before model, Room, Open Action Proposal, or creative EXCON integration can obscure a state error.

## Considered options

- **Selected:** add the contest-scoped transition kernel and drive it with frozen fixtures. This keeps the first proof local to D50-D60 and leaves the complete U.S. Room unchanged.
- **Rejected:** add DATE mode switches to `nuclear_war_env`. Its `GameState`, legal actions, events, and replay encode the closed game, so reuse would couple the open crisis to card-game assumptions.
- **Rejected:** begin inside the Concordia harness. That would mix provider, memory, and institutional failures with the unproved World transition and make a green model call look like World evidence.
- **Deferred:** build a general national or multi-scenario simulator. The first contest claim needs one episode-bounded Core and one matched transition, not a universal engine.

## Consequences

The frozen matched artifact is an event or patch template. Each admitted ledger entry and State Patch instance adds its run ID, current Core version, sequence, and before-and-after hashes. Template bytes and semantic operations therefore match across runs even when open-ended earlier branches have different Core versions. The instance still satisfies D51's base-version requirement and fails closed if it is stale. No arbitrary JSON-path patching, closed legal-move catalog, model inference, or transcript parsing enters this kernel.
