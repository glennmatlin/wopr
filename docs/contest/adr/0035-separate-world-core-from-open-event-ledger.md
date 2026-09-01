# Separate the World Core from the open event ledger

Status: accepted decision D50; refined by D51; resolves OPEN-WORLD-009

The DATE World pairs a minimal typed World Core with an append-only World Event Ledger. The Core contains only state that deterministic mechanics must query or change. The Ledger uses a fixed causal and provenance envelope while permitting open-ended descriptions of exogenous events, observations, and admitted consequences.

Every EXCON consequence remains a proposal until deterministic admission. Admission always creates a ledger entry. A proposal must also contain a typed, preconditioned State Patch when it would change a Core fact, permission, quantity, clock, terminal condition, or other value used by validation or declared measurement. Ledger-only content may inform Rooms and later adjudication, but it cannot override the Core, satisfy a Core predicate, or become a quantitative result through post-hoc parsing.

## Considered options

- Store all state in one open document or graph that EXCON may patch.
- Require every possible consequence and observation to use a predeclared typed schema.

The first option preserves surface freedom but makes arbitrary semantic writes difficult to validate or match across runs. The second gives strong shape validation but closes the consequence space around the schemas anticipated by the authors. The selected split fixes provenance and mechanically consequential state while leaving consequence content open.

## Consequences

D50 refines D49's shorthand that EXCON outputs a State Patch: EXCON outputs a retained consequence proposal, and only a Core-changing proposal requires a State Patch. Accepted patches and their ledger entries are atomic and preserve the prior Core version; rejected proposals and patches remain replay artifacts but do not enter World truth.

The existing Nuclear War engine supplies typed-state and validated-event patterns, not this DATE representation. D51 selects an episode-bounded invariant-and-affordance Core and semantic patch families; the exact serialization, concrete first-episode state, and validator implementation remain OPEN and require a tracer.
