# Bound the first World Core to episode affordances

Status: accepted decision D51; refined by D52; resolves OPEN-WORLD-010

The first DATE World Core is episode-bounded. It types only the entities and ownership, geography and control, ground-truth facts, status and posture, World Affordances, active authorizations and commitments, clocks and triggers, terminal conditions, and Outcome Projections needed to run and evaluate the selected ridge-seizure episode. The ledger envelope separately types observation references, audiences, and delivery time without turning Room memory into duplicate World state.

State Patches may perform only schema-declared semantic operations: create or retire a causally downstream entity of an existing kind; assert or update a typed fact, status, location, control, or projection; adjust a bounded quantity; add or remove a typed relation, access, authorization, or commitment; and schedule, cancel, or resolve a clock or trigger. Every patch binds a Core schema and base version, expected prior values or read set, causal parents, and effective time, and applies atomically.

## Considered options

- Use an ultra-thin gate Core containing only identities, authority, capability, and clocks.
- Build a broad PMESII-PT simulation Core covering national systems beyond the first episode's mechanics.

The thin option cannot deterministically represent occupation, posture, information delivery, support dependencies, adaptation, or declared outcomes. The broad option would consume the contest schedule, invite unsupported realism claims, and shift the evaluation from the U.S. Room to construction of a general world simulator. The selected Core is the smallest model that can execute the locked episode and its causal replay.

## Consequences

Stable institutional authority rules remain in Room Charters; the Core holds only active authorizations, consents, commitments, and World facts needed by the episode. Adding a semantic domain or patch operation creates a new World and Room-World Contract version. Changing initial entities, values, hidden truth, reports, or pressure changes the Crisis Setup or its version under the existing Setup rules.

Exact class names, JSON fields, and operation serialization are implementation details inside this boundary. D52 selects the abstract Force Package resolution, D59 fixes the mixed-affordance topology, and module 13 supplies D60's reversible package, geography, initial-value, report, MSEL, and terminal defaults. Those defaults remain provisional until versioned machine freeze. No D51-D60 capability exists until a tracer passes.
