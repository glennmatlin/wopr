# 15. U.S. Charter machine contract

Status: RATIFIED D67; Milestone 1 PASSED

## Scope

`SR-USM-001` Milestone 1 MUST produce `US_SOURCE_REGISTER.candidate.json` and `US_CHARTER.candidate.json` under `docs/contest/`, with the latter serializing `US_PUBLIC_2026Q3`. It MUST NOT call a model, run a Room, freeze the Crisis Setup, implement Open Action Proposals or EXCON, alter the DATE Core, or claim official procedural fidelity.

`SR-USM-002` The source and Charter candidates MUST live in the contest context and use strict canonical JSON identity. Unknown fields, duplicate keys or IDs, unresolved references, invalid scalar types, current-officeholder fields, and unsupported source-status values fail closed.

`SR-USM-003` Candidate status binds exact bytes for review and tests but does not itself ratify or freeze the Charter. Ratification is one batch owner gate after source refresh, validation, and a rendered review surface. A separate canonical receipt MUST bind the accepted candidate commit and exact source and Charter hashes so acceptance does not mutate the reviewed bytes.

`SR-USM-004` Milestone 1 parsing, identity, validation, compilation, and review rendering SHOULD live under `nuclear_war_contest.situation_room`. Provider clients, live seat execution, general episode orchestration, and World integration belong to later milestones.

## Source-register contract

`SR-USM-010` Every Source Card MUST bind a stable source ID, issuing institution, public title, canonical URL, publication or effective date when available, retrieval date, source type, bounded claim excerpt or paraphrase, applicable office or process IDs, and status `fact`, `inference_support`, or `context_only`.

`SR-USM-011` A source record MUST distinguish what the official material says from the machine-design inference drawn from it. One source MAY support multiple facts; one inference MAY cite multiple sources. Absence of a source MUST remain an explicit gap rather than be repaired by office-title analogy.

`SR-USM-012` The refresh MUST cover the public NSC and HSC membership and process basis, stable statutory offices, voting or advisory status where public, department and adviser mandate boundaries, CJCS command exclusion, dated public posture used in personas, and any issue-specific invitee included in the first episode.

`SR-USM-013` The register MUST NOT copy classified material, name current officeholders, imply endorsement, turn DATE role labels into U.S. facts, or describe a WOPR routing inference as official procedure.

## Charter envelope

`SR-USM-020` The candidate Charter MUST bind schema version, Charter ID and version, candidate status, source-snapshot identity, actor ID, objective IDs, Institution Registry, group registry, information classes, disclosure permissions, activation predicates, decision routes, Required Confirmation rules, product schemas, and evidence labels.

`SR-USM-021` Every Seat record MUST declare one stable seat ID, public office class, first-slice disposition, voting or advisory status, mandate, supported contributions, prohibited actions, information entitlements, group memberships, activation predicates, decision-route roles, persona-posture references, and supporting fact or inference IDs.

`SR-USM-022` Every Group record MUST declare one stable group ID, purpose, ordered eligible membership, active-member rule, input entitlements, dependencies, shared-seat barriers, activation predicate, product schema, collection order, and failure effect.

`SR-USM-023` Every Decision Route MUST declare its action class or applicability predicate, owning authority, eligible forum, consensus or referral rule, presidential-attention rule, consultations, Required Confirmations, final decision record, and failure effect. Office title alone cannot imply delegation.

`SR-USM-024` Information classes and permissions MUST keep Common Crisis Picture, seat-private synthetic facts, cell products, senior products, retrieved underlying facts, disclosures, and World ground truth distinct. A union prompt or undeclared delivery fails closed.

## First-episode institutional coverage

`SR-USM-030` The candidate MUST serialize the complete public roster classes in module 04, not a target number of agents. Activation follows typed predicates; the conventional-crisis baseline count remains a derived, provisional consequence.

`SR-USM-031` The candidate MUST serialize Watch, seven specialist and synthesis groups, PC, NSC or HSC routing, Executive Secretary, and the triggered U.S. Theater Commander role without turning deterministic services into judgment-bearing seats.

`SR-USM-032` The selected ridge episode MUST be able to activate the intelligence, diplomatic, economic, defense, nuclear-risk, legal-authority, senior-integration, and theater-operational contributions its Policy Package and weather path require. An absent required mandate is a Charter gap, not permission to invent a generic adviser.

`SR-USM-033` Cross-group seats MUST retain one identity and memory. The machine graph MUST expose serialization barriers for shared seats and MAY mark only disjoint nodes eligible for concurrency.

## Candidate validation

`SR-USM-040` A strict loader MUST reject unknown envelopes, duplicate identities, missing required fields, unresolved source, objective, seat, group, entitlement, product, activation, route, or confirmation references, invalid enum values, current officeholder fields, and cycles in the first-slice dependency graph.

`SR-USM-041` A compiler MUST derive, without model judgment, the allowed seat registry, group graph, first-episode activation candidates, shared-seat barriers, delivery entitlements, and decision-route lookup. Derived views MUST NOT create undeclared Charter truth.

`SR-USM-042` Canonical identity MUST follow module 14's strict JSON rules. Human-readable renderings MAY change whitespace only and MUST show every fact, inference, gap, source, seat, group, permission, trigger, route, and confirmation included in the candidate hash.

## Required no-model checks

`SR-USM-050` Focused tests MUST prove strict source and Charter loading, exact identity, global ID uniqueness, complete reference resolution, stable canonical hashing, and deterministic compilation.

`SR-USM-051` Fixture tests MUST prove one active seat can join multiple groups without cloning; one private fact reaches only entitled seats; one shared seat creates a dependency barrier; one disjoint pair remains concurrency-eligible; one adviser cannot count toward policy consensus; and one missing authority or confirmation produces no supported decision route.

`SR-USM-052` Failure tests MUST retain the rejected candidate and stable reason codes `invalid_envelope`, `duplicate_id`, `unknown_reference`, `unbound_fact`, `unbound_inference`, `forbidden_officeholder_field`, `entitlement_leak`, `activation_error`, `dependency_cycle`, `inferred_delegation`, `invalid_adviser_status`, and `incomplete_route`.

## Milestone gate

`SR-USM-060` Milestone 1 passes only when official-source refresh is complete for every first-episode claim, all gaps are explicit, both candidate artifacts have deterministic hashes, focused tests pass, the rendered review surface matches the serialized content, and the owner ratifies or revises the bundle once.

Passing this gate establishes a ratified source-bound Charter contract for the first-episode implementation. It does not establish Room feasibility, model behavior, institutional authenticity, Counterpart Room execution, DATE execution, or comparative performance. Milestone 2 begins only from the ratified Charter identity.

## D66 candidate receipt

The source register candidate hashes to `73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f`; the bound Charter candidate hashes to `fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2`. Forty-five focused tests pass for loading, rejection, identity, compilation, candidate coverage, and lossless review. D67 subsequently closes the batch owner gate without changing either candidate identity.

## D67 ratification receipt

[`US_CHARTER_RATIFICATION.json`](../US_CHARTER_RATIFICATION.json) records status `ratified`, decision `D67`, candidate commit `623612166aa65bb0c2f14a79ea6993cd02221f8d`, the exact source and Charter identities above, and the Milestone 1 scope. Its canonical SHA-256 is `0b831d55ba60dd458e44b0e63d714a82eaf05b508a32694f96181caba0b5ad13`. The receipt proves owner acceptance of those exact artifacts only. It records no Room execution, model behavior, official or classified fidelity, effect-level authority path, Counterpart Room, or DATE episode evidence.
