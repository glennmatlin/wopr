# 14. First DATE machine contract

Status: PROVISIONAL IMPLEMENTATION CONTRACT D62-D63 under D60; D64 transition, D69 bridge, and D70 two-cycle composition passed at their bounded no-model scopes

## Scope

`SR-MACHINE-001` The first implementation slice MUST prove D50-D60's World transition only. It MUST NOT call a model, construct a Room, adjudicate an Open Action Proposal, simulate either counterpart government, claim creative EXCON, or alter the U.S. Charter.

`SR-MACHINE-002` The slice SHOULD live under `nuclear_war_contest.date_world` as a pure contest-scoped kernel. It MUST NOT import or extend the closed game's `GameState`, `EngineEvent`, legal-action, replay, or three-member C2 schemas. Generic hash and JSON-I/O behavior MAY be reused when the DATE artifact contract remains independently validated.

`SR-MACHINE-003` Every transition MUST be a pure all-or-nothing operation over an input Core. Rejection returns the unchanged Core plus a retained validator receipt. Acceptance returns a new Core, one admitted ledger entry, and the receipt; no caller-visible mutation may occur before every check passes.

## Candidate profile

`SR-MACHINE-010` [`DATE_PROFILE.candidate.json`](../DATE_PROFILE.candidate.json) is the exact `0.1.1` candidate serialization of module 13 at canonical hash `64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477`. Its `candidate` status means its hash is a checkpoint identity, not a frozen Setup or run identity. Source binding, Charter ratification, and a versioned freeze receipt remain required.

The profile envelope fixes `schema_version`, profile and Setup identity, Seed, episode clock, Road to War, initial Core, partner request, escalation ladder, terminal policy, declared audience and evidence IDs, authored event templates, patch templates, risk-probe IDs, and Outcome Projection IDs. Unknown top-level fields fail closed rather than silently changing identity.

## Core contract

`SR-MACHINE-011` `date-core.v0.2` uses these closed semantic domains:

| Domain | First-slice content |
|---|---|
| identity | Core schema and monotonically increasing `core_version` |
| actors and geography | U.S., Himaldesh, Olvana; Kestrel Ridge, Talus Node, South Pass |
| activities and packages | U.S. crisis assessment and three fictional Force Packages |
| affordances | separate U.S. observation and Himaldeshi support windows |
| truth and authority | hidden Olvanan intent and active Himaldeshi authorization state |
| commitments and clocks | typed active records and the three episode deadlines |
| escalation and terminal | current escalation and terminal states |
| projections | the eight declared candidate World-outcome fields |

An identifier reference MUST resolve within the candidate profile. An absent domain fact remains unknown or outside the model. Open ledger content cannot add a Core field or entity.

`SR-MACHINE-012` [PROVISIONAL D63] Outcome Projections MUST be read-only semantic selectors over location control, authorization, commitment, escalation, affordance, or terminal state. `project_outcomes` MUST resolve every declared selector from the supplied Core without mutation, a Core-version change, an implicit patch operation, or ledger-text parsing. Unknown selectors, targets, or duplicate projection IDs fail closed during profile loading.

## Event and patch instances

`SR-MACHINE-020` A frozen event template binds its ID, kind, episode hour, causal parents, source, affected entities, audience, evidence, assumptions, uncertainty, open content, and optional patch-template ID. An admitted ledger entry copies those fields and adds `run_id`, `entry_index`, `core_version_before`, `core_version_after`, and its validator-receipt ID.

`SR-MACHINE-021` A frozen patch template binds its ID, effective hour, causal parents, ordered operations, expected values, and replacement values. A State Patch instance copies the template and adds `run_id`, `patch_instance_id`, `base_core_version`, `base_core_hash`, and template hash. This split keeps template and operation bytes matched while binding each run to its actual current Core.

`SR-MACHINE-022` The first operation catalog contains only:

- `set_force_package_readiness(force_package_id, expected, value)` for tracer branch fixtures; and
- `set_affordance_state(affordance_id, expected, value)` for the atomic paired weather change.

Adding another operation changes the schema and Room-World Contract. Neither operation accepts an arbitrary field or JSON path.

`SR-MACHINE-023` [MEASURED D69] A proposal-derived event MAY use source
`excon_consequence` only after module 17's proposal, clarification, authority,
capability, Core-read, and represented-Room checks pass. It MUST NOT collide
with an authored MSEL template ID. An optional dynamic State Patch still uses
only this module's semantic operations and passes the same D64 validation,
atomicity, receipt, and replay path.

The candidate readiness values are `active`, `prepared`, `ready`, and `delayed`; the candidate affordance values are `available`, `intermittent`, and `restricted`. A transition may select only a value valid for its target field and must still satisfy the operation's expected prior value.

## Canonical identity

`SR-MACHINE-030` Artifact identity is SHA-256 over UTF-8 canonical JSON with object keys sorted, arrays preserved, no insignificant whitespace, standard finite JSON values only, and the hash field itself omitted. Readers MUST reject duplicate keys, non-finite numbers, unknown fields, wrong scalar types, booleans where integers are required, and schema-version mismatches before hashing.

Human-readable pretty JSON MAY differ in whitespace only. A loader MUST re-canonicalize the parsed value and bind the resulting hash; a filename, branch, or `latest` label is not identity.

## Validator order

`SR-MACHINE-040` The validator MUST check, in order:

1. exact envelope, schema, scalar, and unique-ID shape;
2. profile, template, Core, actor, entity, audience, and causal references;
3. non-retroactive event time and nonterminal current state;
4. template identity, current base Core version, and base Core hash;
5. declared operation, target kind, field semantics, expected prior value, and allowed replacement value;
6. the complete operation list against a private copy; and
7. next Core version and hash, ledger entry, and receipt consistency.

Any failure returns one or more stable reason codes, including `invalid_envelope`, `duplicate_id`, `unknown_reference`, `causal_mismatch`, `retroactive_time`, `terminal_world`, `template_mismatch`, `stale_core`, `failed_precondition`, `undeclared_operation`, `forbidden_write`, and `invalid_value`. One failed operation rejects the whole patch.

## Offline tracer

`SR-MACHINE-050` The first no-model tracer MUST:

1. load the candidate profile, compute its hash, and construct Core version 0;
2. admit the T+1 forecast as ledger-only and prove the Core version and hash did not change;
3. fork two fixture runs and admit one valid package-readiness patch in each, producing distinct state but the same Core version;
4. instantiate the same weather patch template against each current Core and atomically narrow both affordances;
5. admit the linked confirmation and prove identical direct template operations but retained branch differences;
6. reject stale Core, one failed affordance precondition, unknown entity, arbitrary path, undeclared operation, retroactive event, duplicate ID, partial patch, and unearned actor, package, affordance, or capability cases; and
7. rebuild both final Cores and ledgers from initial Core plus retained transitions, compare hashes, and reproduce the D63 derived projections.

The D64 tracer proves only deterministic state, matching, atomicity, fail-closed admission, and replay for this slice. D69-D70 separately prove authored proposal admission and two-cycle composition against the same kernel. None proves live Room judgment, Counterpart Room behavior, creative-EXCON plausibility, nuclear escalation behavior, model quality, or comparative performance.

`SR-MACHINE-051` [MEASURED D64] [`DATE_TRACER_RECEIPT.json`](../DATE_TRACER_RECEIPT.json) records the fresh-process tracer at executor revision `c7d57167bb1ab219b8e3e3a128866b71699e9977` and receipt hash `4a582d72b6d8ff753c3e06adea4d36aef3c3b39b5284e4050ce9ed35e39815e3`. It closes only the D62-D63 mechanical transition gate; the candidate remains unfrozen and no Room, model, Open Action Proposal, creative EXCON consequence, or end-to-end DATE episode ran.

## Smallest implementation map

The implementation should use concern-sized modules for immutable models and canonical identity, candidate-profile loading, semantic operations, validation and transition, replay, and one offline tracer entry point. Focused unit tests should mirror the failure cases above; one integration test should run the full two-branch tracer in a fresh process. No CLI, provider dependency, general event registry, database, async runtime, or microsite path is required for this proof.
