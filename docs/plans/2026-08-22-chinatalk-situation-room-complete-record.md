# Complete record: ChinaTalk Situation Room pivot

Created: 2026-08-22

Status: archival working record for transfer to the main conversation

Related concise handoff:
`/private/tmp/wopr-situation-room-pivot-handoff-2026-08-22.md`

Main Codex thread:

- Title: `Plan ChinaTalk contest week`
- Thread ID: `01a02276-c7b2-7f80-9287-e444d862b88b`

## Preservation statement

This document preserves every accessible decision, correction, source,
distinction, scenario path, architecture choice, and unresolved question from
the side conversation about the ChinaTalk submission. It is intended to prevent
the design work from remaining trapped in conversational context.

This is not a verbatim transcript. The side conversation is an ephemeral thread,
and the app reported both `no rollout found` and `ephemeral threads do not
support thread/turns/list` when asked to export it. Some earlier assistant turns
were also compacted out of the visible history. Exact user language is quoted
where it remains available. Other passages are marked as reconstructed
chronology or consolidated design state. No missing wording should be treated as
evidence that an unrecorded design choice was made.

The concise handoff remains useful for fast operational pickup. This complete
record is the fuller provenance source. If they appear to conflict, the most
specific confirmed decision in this record should be surfaced to the owner
rather than silently resolved.

## Mutation and repository audit

- Working directory observed during the side conversation:
  `~/.codex/worktrees/903e/wopr`
- Branch observed: `glenn/chinatalk-contest-repair`
- Commit observed: `04dd10e3932e`
- Worktree observed as clean.
- No repository files, source files, Git state, permissions, or configuration
  were changed in the side conversation.
- The only written artifacts were temporary handoff records under
  `/private/tmp`.

## Reading conventions

- **Confirmed** means the owner explicitly selected or affirmed it.
- **Provisional** means it is the current working design but still needs a
  direct owner decision or source-derived specification.
- **Historical** means it describes the already executed Nuclear War study or
  an option explored and later rejected.
- **Open** means implementation should not quietly decide it.
- **Inference** means a conclusion derived from the sources or code rather than
  a claim made directly by a source.

## Executive synthesis

The contest submission should be about a machine-operated Situation Room as a
reusable evaluation task. A crisis World produces incomplete and
role-differentiated information. Machines occupy seats with actor-appropriate
mandates and personas, deliberate under an explicit communication regime, and
produce a policy package. A release rule determines what advice becomes an
authorized decision. A constrained interpreter maps that policy into supported
formal actions, requests clarification when necessary, and fails closed on
unresolved ambiguity. A hard-mechanics World applies consequences and returns
the next state. The complete trace supports replay and comparison.

The current Nuclear War implementation is the engineering origin and the first
demonstrated World. It showed that machines can occupy structured advisory
seats, deliberate under full press, vote, release actions through different
authority rules, and generate replay-linked consequences. It did not establish
that the Nuclear War card game is a realistic Situation Room task, that the
architecture already transfers across Worlds, or that one organizational form
produces better crisis outcomes.

The selected contest-facing World is therefore a new DATE-backed
Himaldesh-Olvana arena. It represents three heterogeneous Rooms: the actual
United States as a friendly external actor, fictional Himaldesh, and fictional
Olvana. The arena begins with conventional high-altitude border crises. Nuclear
coercion, warning, or limited-use branches are mechanically reachable, but they
are not forced into every opening. The arena contains a registry of authored
Crisis Setups rather than one privileged vignette. Evaluation runs use matched
setup-seed pairs; demo or free-play runs may sample from the frozen registry.

## Owner intent in preserved language

The following remarks are retained because they define the design boundary more
precisely than a later paraphrase could.

- The goal is to take the Situation Room and extract it so a narrative can
  explain why and how it is simulated. "nuclear war is just the starting
  example."
- The existing game mismatch was stated as: "the task of being a room in THIS
  game doesnt feel right for the situation room setup" and "the physics of
  cards etc feel weird yes not aligned with the world."
- Satirical tone was not itself disqualifying: "humor can be fun so thats not
  an issue per se."
- Scope was not initially the main concern: "i would be okay with one solid
  scenario."
- The desired adjudication may combine both families: "a game that uses hard
  mechanics and or open-ended judges. its possible to do both."
- Disagreement is potentially evidence rather than failure: "I dont think
  disagreement is a bad thing it might be a good feature."
- The Room has several explicit objectives, while roles may have different
  interests, goals, focus areas, or personas.
- The Instrument should model "multiple different rooms and their different
  personas and such."
- The design must be based in DATE because it should use "settings and methods
  familiar to the american national security state."
- Scenario fidelity controls Room design: "We should be adopting the Room
  structure and personas that fit DATE."
- The owner considered Indo-Pacific island crises "done-to-death" and thought a
  generic gray-zone crisis might not be ideal.
- The owner wanted to avoid replaying Ukraine-Russia and said: "I would like to
  have India and Pakistan nuclear conflict LOL but DATE isnt built for that."
- On discovering the DATE-native pairing: "himaldesh olvana makes a perfect
  choice here!!"
- The owner wants repeated use: "I'd be willing and interested in setting up a
  system that allowed me to run it with multiple different setups or events to
  keep it random."
- The owner corrected false convergence: "Again, why fix to one option? Aren't
  we trying to demonstrate a fully fleshed out setup and arena? We can run
  things more than once right?"
- The owner explicitly requested: "document EVERYTHING we've produced in this
  thread" and then emphasized: "i want to avoid losing stuff!!"

## Chronological conversation ledger

This ledger preserves the sequence at the level recoverable from the visible
thread. It is a reconstruction, not a transcript.

### 1. Recover the earlier literature review

The owner asked whether earlier documentation contained examples of real,
open-ended, published, academic games and remembered one with a Situation
Room-style setup. The recovered comparator set included Human vs. Machine,
Biziouras, the 2026 Situation Room Game, Snow Globe, and SIGNAL. The prior repo
logbook also contained older academic citation work.

The central distinction that emerged was that Human vs. Machine pits humans and
machines against the same crisis task, while Biziouras provides a closer model
of differentiated officials advising through a national-security bureaucracy.
The 2026 Situation Room Game supplies a concrete setup pattern with dossiers,
private briefs, injects, and a chair.

### 2. Reframe the contribution

The owner said the purpose was not simply to submit a Nuclear War-playing
system. The interesting object is the machine-operated Situation Room. Nuclear
War could remain the starting example, but the submission narrative needed to
extract the Room as the evaluated task.

Two claims were affirmed and must remain separate:

1. **Demonstrated:** Machines can occupy structured advisory seats, deliberate
   under full press, vote, release actions through different authority rules,
   and generate replay-linked consequences in Nuclear War.
2. **Boundary:** Nuclear War is the first demonstrated World, not the entire
   contribution.

### 3. Decide whether to continue in a main conversation

The owner asked whether this work should be promoted to a main chat and whether
a handoff would be safer. A temporary handoff was chosen first because more
design conversation was still needed. Direct promotion was investigated, but
the ephemeral side thread could not be forked or exported. The practical
solution was to send the handoff to the existing main thread titled `Plan
ChinaTalk contest week` and navigate there.

The owner continued the side conversation, so this complete record was later
requested as an additional preservation layer.

### 4. Test whether Nuclear War fits the new framing

The owner identified four concerns:

1. Acting as a Room inside the present card game does not feel like a Situation
   Room task.
2. Card physics are not aligned with the crisis World being represented.
3. Humor is acceptable and may be useful, so tone alone is not the main defect.
4. One convincing scenario could be sufficient, so breadth was initially less
   important than task fidelity.

This moved the design away from defending the current game at all costs. The
decision became: preserve Nuclear War as evidence and engineering provenance,
while testing whether a more fitting World should carry the contest-facing
demonstration.

### 5. Choose the adjudication shape

The desired task may use hard mechanics and open-ended judgment together. The
stable hybrid design became:

1. Rooms deliberate and write an open-ended policy package.
2. A constrained interpreter decomposes the package into supported formal
   actions.
3. The interpreter exposes ambiguities and asks for confirmation or revision.
4. Unresolved ambiguity fails closed.
5. Hard World mechanics apply consequences.
6. Replay retains the original policy, proposed mapping, clarification exchange,
   confirmed actions, and resulting state.

The open-ended component therefore interprets Room policy. It does not freely
invent World outcomes or MSEL events.

### 6. Define disagreement and role differentiation

The owner rejected the idea that disagreement is inherently a defect. A Room
must solve several explicit actor-level objectives, and seats may protect
different institutional mandates, attend to different risks, receive different
information, or express distinct professional personas.

The design separated three concepts:

- A **role mandate** states what a seat is professionally obliged to protect,
  notice, or provide.
- A **persona** states doctrine, risk tolerance, analytic style, and
  communication behavior.
- **Authority** states how a seat's advice can bind, block, delay, or inform the
  Room's released decision.

Artificial private victory conditions were not selected. Differentiated
mandates can generate substantive disagreement without turning crisis policy
into a hidden-score social game.

### 7. Require multiple actor-specific Rooms

The owner wanted multiple Rooms and multiple personas. The assistant initially
approached this as a choice among symmetric experimental organizations. The
owner corrected that assumption: the Room structure must fit the DATE actor and
the scenario.

The resulting concept is a **Room Charter** for each represented actor. A
Charter defines seats, mandates, information entitlements, communication
permissions, chairing, and release authority. The United States, Himaldesh, and
Olvana should not be forced into the same organization merely to make a neat
factorial design.

### 8. Adopt DATE as the World basis

The owner explicitly required the arena to be based in the U.S. Army's Decisive
Action Training Environment. The reason was not visual flavor. DATE supplies a
training-world vocabulary and scenario-development method recognizable to the
American national-security community.

Research established that DATE is an operational environment, not a complete
scenario. It provides fictional countries informed by real-world conditions,
PMESII-PT descriptions, military forces, relationships, equipment, and threat
context. Exercise designers still select objectives, write a Road to War,
define STARTEX conditions, and author an MSEL.

This changed the implementation target from "reskin the card game" to "build a
DATE-derived World and scenario registry behind the reusable Room machinery."

### 9. Explore candidate theaters

Several paths were considered:

- An Indo-Pacific island crisis was deprioritized because the owner considered
  that space overused.
- A gray-zone attribution crisis was deprioritized because it risked giving an
  open-ended judge too much control over the decisive fact pattern.
- A DATE Eurasian allied-defense or nuclear-coercion crisis was explored.
- Gorgas, Pirtuni, Atropia, and Donovia were considered.
- Pirtuni felt too close to another Ukraine-coded scenario.
- Gorgas supplied useful occupied-territory and Western-alignment facts, but
  much of the nuclear danger would still sit primarily in a U.S.-Donovia
  confrontation and retain Russia-Georgia-Ukraine associations.
- Atropia was too neutral for the desired partner relationship.

The owner wanted a regional partner with meaningful U.S. ties but no automatic
mutual-defense guarantee. They also raised the attractive real-world structure
of an India-Pakistan nuclear crisis, while observing that DATE did not appear to
contain a clean fictional Pakistan analogue.

### 10. Select Himaldesh-Olvana

Research found that DATE contains a stronger native pair:

- Himaldesh is nuclear-armed, has a Strategic Command, and declares no first
  use.
- Olvana has a nuclear deterrent and a public no-first-use posture, while DATE
  leaves useful ambiguity around limited employment.
- The countries already have border tension and incursion dynamics.
- The United States has a special bilateral military relationship with
  Himaldesh without a mutual-defense guarantee.
- The theater is a high-altitude continental border, not another island
  blockade or Taiwan analogue.

The owner selected Himaldesh-Olvana. The represented Rooms became:

1. The actual United States national-security Room, modeled only from public
   roles and methods.
2. A Himaldesh Room derived from DATE actor institutions and public analogues
   where needed.
3. An Olvana Room derived on the same basis.

The actual United States can appear as a friendly external actor under DATE's
conventions. The design must not name current officeholders, imply access to
classified procedures, or imply Army endorsement.

### 11. Decide how nuclear escalation enters

The arena should begin with conventional border crises. Nuclear coercion,
warning, signaling, misinterpretation, or limited-use branches should be
reachable through the state and event mechanics. They should not be forced into
the opening merely because the original game was Nuclear War.

This preserves nuclear-risk relevance while making crisis management, alliance
ambiguity, signaling, intelligence uncertainty, and escalation control genuine
Room work from the first turn.

### 12. Correct false convergence around one scenario

The assistant repeatedly used a grill format that asked the owner to choose one
option at each branch. This was useful for identifying invariants but became
misleading when the product itself was supposed to support multiple setups.

The owner corrected the method. A fully developed arena can and should run more
than one opening, actor intent, event path, or seed. The correct design rule is:

- Ask for a single choice only when the World requires one invariant.
- Map an entire variable dimension when multiplicity is part of the arena.
- Do not quietly turn an illustrative scenario into the definition of the
  system.

The result was a reusable Himaldesh-Olvana World plus a registry of Crisis
Setups, actor-specific Room Charters, and a common execution and replay
contract.

### 13. Preserve the work before implementation

The owner asked to record all conversation, resources, choices, and corrections
before more design or implementation. The concise operational handoff was
written first. This complete record was then created because the ephemeral
side-chat state could not be exported and the owner wanted stronger protection
against context loss.

## Literature and comparator register

### Human vs. Machine

- Citation target: Lamparth et al., *Human vs. Machine*.
- Link: https://arxiv.org/abs/2403.03407
- Relevance: Human and machine conditions face the same crisis-decision task.
  The machine condition includes simulated team dialogue.
- Use in the submission: It supports pitting machine systems against a common
  decision task rather than treating model text quality as the object of study.
- Limitation for our design: It does not by itself provide the differentiated,
  actor-specific institutional Room and hard World mechanics we want.

### Biziouras

- Citation target: Nikolaos Biziouras, *Bureaucratic Politics and Decision
  Making Under Uncertainty in a National Security Crisis*.
- DOI: https://doi.org/10.1080/15512169.2013.770987
- Relevance: A peer-reviewed Taiwan crisis exercise places differentiated
  officials in a Situation Room-style process. Officials advise a President,
  and their advice is converted into policy through an organizational rule.
- Use in the submission: This is the closest conceptual precedent for treating
  the Room, not a single response, as the unit of machine performance.
- Design lesson: Seat mandates and institutional aggregation matter because
  policy is produced by a structured organization under uncertainty.

### The Situation Room Game

- Citation target: Broxmeyer, *The Situation Room Game*.
- Link: https://activelearningps.com/category/simulations-and-games/
- Relevance: A 2026 teaching simulation uses role dossiers, private briefings,
  policy options, live injects, and a chair.
- Use in the submission: It provides a concrete setup pattern for how a Room
  receives differentiated evidence and experiences a staged crisis.
- Evidentiary caution: Treat this as a published teaching-game comparator, not
  as the same kind of peer-reviewed empirical result as the journal articles.

### Snow Globe

- Citation target: Hogan and Brennen, *Open-Ended Wargames with Large Language
  Models*.
- Link: https://arxiv.org/abs/2404.11446
- Relevance: Open-ended qualitative wargame stages may be operated by humans,
  machines, or both.
- Use in the submission: It supports mixed open-ended game operation and the
  possibility of machine participants beyond fixed-choice play.
- Design difference: Our interpreter should be constrained and auditable, and
  World consequences should remain mechanically governed.

### SIGNAL

- Citation target: Reddie and Goldblum, *Evidence of the unthinkable*.
- DOI: https://doi.org/10.1177/00223433221094734
- Relevance: SIGNAL is a published experimental nuclear wargame with
  mechanically governed consequences.
- Use in the submission: It is a comparator for hard adjudication and measured
  play in a nuclear-risk setting.
- Design difference: Our core evaluated object is a differentiated Room rather
  than an undifferentiated player making game actions.

### Existing repository citation work

- Historical source:
  `~/.codex/worktrees/903e/wopr/LOGBOOK.md:10229`
- Purpose: Earlier academic citation research should be reconciled with this
  register rather than duplicated or silently replaced.

## DATE source register and findings

These links were consulted during the side conversation. They should be
rechecked before public citation, and redistribution terms should be verified
before copying DATE text or assets into a public artifact.

### DATE foundation

- DATE World portal: https://odin.t2com.army.mil/DATEWORLD
- DATE how-to:
  https://odin.t2com.army.mil/How-To/DATE/Decisive_Action_Training_Environment_%28DATE%29
- Army overview:
  https://www.army.mil/article/242997/decisive_action_training_environment_world_the_armys_authoritative_training_environment
- DATE Europe: https://odin.t2com.army.mil/DATE/Europe
- DATE Indo-Pacific region:
  https://odin.t2com.army.mil/DATE/1054bcd2b9fb3254eb220ccc1cda75ac
- DATE Events and MSEL context:
  https://oe.t2com.army.mil/date-decisive-action-training-environment/
- TRADOC G-2 DATE Events List:
  https://oe.t2com.army.mil/2025/02/11/tradoc-g2-develops-date-events-list/
- Exercise design: https://odin.t2com.army.mil/TC/TC_7-101_Exercise_Design
- NTC MSEL detail:
  https://home.army.mil/irwin/download_file/view/a6a83d16-6ad2-4fae-9ae0-25f72e21f59d/684
- Road to War source:
  https://oe.t2com.army.mil/site-content/OEE/Scenario%20Development/TC7_101.pdf

### DATE findings used in the design

- DATE means Decisive Action Training Environment.
- DATE is an Army training operational environment, not a complete scenario or
  a claim that every exercise must simulate every country attribute.
- It uses real-world-informed fictional countries.
- Its country and regional material is organized through PMESII-PT: political,
  military, economic, social, information, infrastructure, physical
  environment, and time.
- It provides force structures, equipment, threat context, relationships, and
  scalable conditions.
- Training objectives determine which conditions an exercise designer models.
- A scenario still needs a Road to War, a STARTEX state, objectives, events,
  dissemination rules, and consequences.
- Real-world countries may be represented as friendly or neutral actors, but
  DATE avoids using them as adversaries in unclassified scenarios.
- **Inference:** The actual United States can therefore be a friendly external
  actor in this arena, while Himaldesh and Olvana carry the adversarial crisis.
- Public U.S. roles and recognizable methods may be modeled. The design must not
  claim classified fidelity or institutional endorsement.

### Selected actor pages

- Himaldesh military:
  https://odin.t2com.army.mil/DATE/2522b29e0fefb26f4164330c2311eb46
- Olvana military:
  https://odin.t2com.army.mil/DATE/5b0c52ae77b5b0e1750dc286a4be93
- Olvana political:
  https://odin.t2com.army.mil/DATE/00e3553e63ca9e3ca7cd562f9364f9d2

### Other actor pages consulted during scenario search

- Bagansait nuclear posture:
  https://odin.t2com.army.mil/DATE/5fc15ff55d0b75e0bf5732af8b955985
- Eurasia:
  https://odin.t2com.army.mil/DATE/53cceeeeb9ae5c0c9a70f218360aa3d1
- Ariana nuclear posture:
  https://odin.t2com.army.mil/DATE/a8c4c89487d3a67481712f6d561315f2
- Pirtuni:
  https://odin.t2com.army.mil/DATE/1faf9edd310516b9129ec11d638597f1
- Donovia relationships:
  https://odin.t2com.army.mil/DATE/e38c799cc6970b1f96fa644a61b1de66
- Atropia:
  https://odin.t2com.army.mil/DATE/93451c916d46ba40c09f6f3d6978d59b

### Scenario-search conclusions

- Himaldesh is the DATE actor closest to the desired India-like nuclear state.
- No equally clean DATE-native Pakistan analogue was found.
- Bagansait is Myanmar-like and explicitly non-nuclear, so it does not support
  the intended dyadic nuclear structure.
- Building a custom fictional Pakistan analogue would require substantial
  country specification and would weaken the submission's claim to use DATE's
  own setting within the available week.
- Using actual India and Pakistan as the adversarial pair would depart from
  DATE's usual unclassified convention for real countries.
- Himaldesh-Olvana supplies a native nuclear dyad, a disputed high-altitude
  border, and a useful U.S.-Himaldesh relationship without an automatic treaty
  obligation.

## The contest narrative

### The problem

Current model evaluations usually ask an isolated system for a recommendation
or place one model in one role. Real crisis decisions are organizational. A
national-security Room distributes information and mandates across seats,
permits or suppresses communication, aggregates disagreement, and releases a
decision through an authority structure. Those procedural choices can change
what the organization does even when the underlying models and evidence remain
the same.

### The evaluated object

The evaluated object is a machine-operated Situation Room. Models are seated in
named institutional roles. They receive common and private observations,
deliberate under a declared communication regime, and produce advice or a policy
package. A release rule converts internal work into authorized external action.
The World then produces consequences and the next information state.

### Why this is a game

It has an evolving state, bounded legal actions, asymmetric information,
strategic interaction among several actors, uncertainty, temporal pressure,
causal consequences, and terminal conditions. It also admits open-ended policy
language at the Room boundary. The hybrid interpreter keeps that language from
becoming an unbounded game-master judgment.

### Why the Situation Room abstraction matters

It allows the same model population to be evaluated under different seating,
communication, and authority arrangements. It also allows different machine
systems to operate the same actor-specific Room against the same setup and
seed. The replay can then attribute a released action to the evidence, role
mandates, deliberation, interpretation, and authority rule that produced it.

### Why Nuclear War remains in the story

Nuclear War is honest engineering provenance and an initial demonstration of
the Room machinery. It is useful because it already exercised multi-seat
deliberation, full press, voting, release rules, and replay-linked actions. It is
not the selected realism claim. The card game's abstractions and satirical
physics do not naturally represent the national-security task the contest
submission now wants to evaluate.

### Why Himaldesh-Olvana is the new World

It allows a conventional crisis to generate real Room work before nuclear use:
border facts are uncertain, alliance commitments are limited, military posture
can be read as signal or preparation, several objectives must be managed at
once, and three governments have distinct information and authority systems.
Nuclear escalation remains possible because both regional actors have DATE
nuclear postures, but the game need not manufacture an immediate launch choice.

## Confirmed design decisions

### Evaluation unit

The machine-operated Room is the reusable evaluation unit. An isolated answer,
one model role, one card-game action, or one scenario outcome is not the whole
unit.

### Represented actors

The arena represents three actor-specific Rooms:

1. The United States.
2. Himaldesh.
3. Olvana.

No symmetry assumption applies. Each Room structure must follow the represented
actor and selected scenario.

### World and scenario relationship

The Himaldesh-Olvana World contains stable actor, geography, capability,
doctrine, relationship, action, and consequence rules. A Crisis Setup chooses a
particular Road to War, opening incident, intent, STARTEX state, private briefs,
constraints, and event graph. A seed varies bounded uncertainty and friction
inside that setup.

### Multiple setups

The arena contains a frozen registry of authored Crisis Setups. One trajectory
may be used to explain the submission, but it does not become the only supported
opening or intent.

### Matched evaluation

Evaluation mode runs competing systems on the same setup and seed. This keeps
the crisis facts and stochastic friction matched. Demo or free-play mode may
sample from the registry, but the sampled setup and seed remain recorded.

### Hybrid interpretation and hard mechanics

Rooms may express policy in open-ended language. A constrained interpreter maps
the policy to the formal action vocabulary, states uncertainty, and asks for
clarification. Unresolved ambiguity fails closed. The deterministic or seeded
World mechanics, not an unconstrained judge, apply consequences.

### Outcome representation

Outcomes should be represented as a vector of relevant crisis dimensions rather
than collapsed immediately into one opaque score. The exact dimensions and any
aggregation remain open.

### Disagreement

Role disagreement is allowed and may be informative. The design should reveal
how the Room resolves conflicting professional mandates. It should not assume
that consensus is always desirable or that dissent is a mechanical failure.

### Traceability

Every run binds the World version, setup, seed, Room Charters, seating, model
configuration, interpreter, executor release, observations, deliberation,
proposed policy mapping, clarification, confirmed actions, and consequences.

## Provisional domain model

The names `Crisis Setup` and `Room Charter` are provisional until the contest
glossary and ADRs are formally revised.

### World

The World owns stable crisis physics and legal possibility:

- actors and geography;
- baseline political and military relationships;
- institutions and strategic authorities relevant to action legality;
- capabilities and readiness ranges;
- declared doctrines and deliberately represented ambiguities;
- the formal action vocabulary;
- state variables and transition rules;
- consequence production;
- terminal and abort conditions.

### Room Charter

A Room Charter defines one actor's decision organization:

- chair or decision authority;
- seats and professional mandates;
- persona parameters grounded in office or doctrine;
- common and private information entitlements;
- who may communicate with whom and when;
- agenda and deliberation rules;
- dissent representation;
- release authority, veto, concurrence, or advisory rules;
- what external policy product the Room must produce.

### Crisis Setup

A Crisis Setup fixes the authored crisis identity:

- setup ID and content hash;
- evaluation objective;
- Road to War;
- STARTEX state;
- opening incident;
- actual actor intent;
- public common picture;
- Room-private briefs;
- starting postures;
- political constraints;
- MSEL event graph;
- supported follow-on branches.

An accidental incursion and a deliberate resolve probe are different setups,
even if the visible opening report is identical. Strategic intent is not a
random seed variable.

### World Seed

A World Seed may vary bounded mechanical uncertainty such as:

- detection;
- timing and delay;
- weather;
- readiness;
- sensor confidence;
- communications or operational friction.

A seed must not silently change doctrine, political objective, strategic
intent, or whether an incident was accidental or planned.

### Seating

Seating assigns particular model instances or system configurations to the
chairs defined by a Room Charter. It is distinct from the Charter itself.

### Interpreter

The interpreter accepts a released open-ended policy package and proposes a
mapping to supported formal actions. It may expose ambiguity and ask a bounded
clarification question. It may not invent new legal actions, hidden state,
consequences, or MSEL events.

### Release rule

The release rule determines how internal Room outputs become actor-authorized
policy. It may encode executive choice, concurrence, vote, veto, advice, or
another actor-appropriate procedure. It is not identical to communication or
seat persona.

### Run identity

A replayable run should bind at least:

- World version;
- Crisis Setup ID and hash;
- World Seed;
- Room Charter hashes;
- Seating and model configuration;
- interpreter version;
- executor release;
- initial state and private observations;
- every inject and dissemination target;
- deliberation artifacts;
- released policy;
- proposed and confirmed formal actions;
- resulting state and measures.

## DATE-to-arena mapping

| DATE or exercise concept | Arena responsibility | Why it matters |
|---|---|---|
| PMESII-PT | World condition model | It selects the political, military, economic, social, information, infrastructure, physical, and temporal facts relevant to the training objective. |
| Road to War | Crisis Setup prehistory | It explains how the World reached STARTEX without spending early turns on exposition. |
| STARTEX | Initial formal state | It fixes the crisis state from which matched runs begin. |
| MSEL | Authored event graph | It defines events, triggers, recipients, dissemination, purpose, consequences, and follow-ons. |
| EXCON | World executor | It applies rules and injects without becoming a participating Room. |
| Training audience | Machine-operated Rooms | The Rooms receive information, deliberate, and act. |
| Training objectives | Evaluation task and measures | They determine which PMESII-PT conditions and outcomes need to be modeled. |
| After-action review | Replay and trace | It connects observations, deliberation, authority, actions, and consequences. |

The arena should not attempt to simulate every field in a DATE country book.
Training objectives determine the minimum sufficient state.

## Candidate Crisis Setup families

These are a registry seed, not a final catalog. Their names are provisional.

### `ridge_seizure.local_exploitation`

A local commander or unit exploits a tactical opportunity without a broader
strategic decision to create a major crisis. The Rooms must infer whether the
incident is containable while responding to facts on the ground.

### `ridge_seizure.limited_fait_accompli`

An actor deliberately attempts a bounded territorial change and expects the
other side to avoid escalation. The Rooms must balance reversal, signaling,
force protection, and escalation risk.

### `ridge_seizure.resolve_probe`

The territorial move is primarily a political test of resolve and partnership.
The same physical opening can carry a different strategic objective, so this is
a separate setup rather than a different random seed.

### `aircraft_shootdown.mistaken_identification`

An aircraft loss results from error, misidentification, or local breakdown. The
Rooms receive incomplete and potentially contradictory indications while
military readiness rises.

### `aircraft_shootdown.coercive_signal`

An aircraft is attacked deliberately as a signal. The visible incident may
resemble the mistaken-identification setup, but actor intent and follow-on
branches differ.

### Additional families to map

- Missile exercise or test misread as preparation.
- Nuclear force dispersal as warning, cover, or routine procedure.
- Border reinforcement that creates reciprocal mobilization pressure.
- Communications outage during a live standoff.
- Third-party or domestic political event that changes escalation constraints.

No random event deck was selected. Events should be causal, state-triggered, or
pre-authored in the MSEL graph.

## Room objectives and role design

### Actor-level objectives

Every Room should face several explicit objectives rather than one hidden
utility score. Candidate shared dimensions include:

- protect territorial and force interests;
- prevent uncontrolled escalation;
- preserve credible commitments and relationships;
- maintain domestic political legitimacy;
- retain future freedom of action;
- improve or preserve information quality;
- limit civilian and military harm;
- avoid accidental nuclear use or misinterpretation.

These are provisional. They must be specialized to each actor and tied to the
formal state before evaluation claims are made.

### Seat-level mandates

Seats should have professional mandates that cause them to notice and protect
different things. Candidate functions include political leadership, diplomacy,
defense, military operations, intelligence, nuclear or strategic forces,
communications, and economic policy. The exact office names and powers must be
derived separately for the United States, Himaldesh, and Olvana.

### Personas

Personas should encode public doctrine, institutional risk tolerance,
communication style, and analytic emphasis. They should not be decorative
character biographies or covert victory conditions.

### Information entitlements

The Room should have a common operating picture plus seat-relevant private
briefs. Private information exists because organizations distribute evidence
unevenly, not merely to manufacture intrigue.

### Authority

Each Charter must state whether seats advise, concur, veto, command, chair, or
release. The authority mechanism is part of the evaluated organization and must
be visible in replay.

## Existing WOPR evidence boundary

### What actually ran

The corrected Sounding contains 12 admissible cells and five matched pairs.
Four admitted equal-council cells contained 35 actions released against the
executive vote. This establishes that the Room procedure can alter the command
process in the Nuclear War implementation.

### What did not run successfully

The Overlay Demo failed before producing an admissible trace. It must not be
described as successful evidence.

### Claims supported

- Structured machine seats can deliberate under full press.
- Different release rules can produce different authorized actions from the
  same internal voting situation.
- Released actions can be linked to deliberation and replay artifacts.
- The existing Nuclear War implementation is sufficient to demonstrate one
  composed Room-to-World execution path.

### Claims not supported

- No demonstrated population-level effect on escalation, casualties, or
  strategic quality.
- No established superiority of one Room organization.
- No evidence that Nuclear War's card physics are realistic crisis mechanics.
- No proof that the current code is already generic across Worlds.
- No evidence yet from a runnable DATE-backed World.

## Current repository Packet and history

The active Packet sources are:

- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/CONTEXT.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/PROTOCOL.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/APPLICATION_DRAFT.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/EXECUTION_PLAN.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/GAMES_REGISTER.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/site/index.html`

Executed evidence and readiness sources include:

- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/SOUNDING.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/SOUNDING_ANALYSIS.json`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/CORRECTED_RUN_RECEIPT.json`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/M3_SCREENING.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/M3_MODEL_PREFLIGHT.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/M3_PROMOTION.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/COMPOSITION_SMOKE.md`
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/READINESS_MATRIX.md`
- Frozen manifests in the same contest directory.

Decision history is in:

- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/contest/adr/0001` through `0009`.
- `~/.codex/worktrees/903e/wopr/LOGBOOK.md` from 2026-08-11 onward.
- `~/.codex/worktrees/903e/wopr/nuclear_war/LOGBOOK.md` from mid-August onward.
- `~/.codex/worktrees/903e/wopr/nuclear_war/docs/plans/2026-08-12-contest-live-c2-full-press.md`.

The current glossary and ADRs describe the executed Nuclear War Instrument.
They are historical evidence, not automatically the approved vocabulary for the
DATE pivot. In particular, ADR 0001 and assumptions that one shared Preset can
be applied symmetrically will need explicit supersession after the new design is
approved. They must not be silently rewritten.

## Verified code reuse boundary

### Reusable seams

- The `DecisionAgent.choose(observation, options)` interaction shape in:
  `~/.codex/worktrees/903e/wopr/nuclear_war/src/nuclear_war_env/agent_protocol.py`
- Faction-level decision aggregation in:
  `~/.codex/worktrees/903e/wopr/nuclear_war/src/nuclear_war_agents/faction_agent.py`
- Full-press and communication machinery.
- Model and study manifests.
- Attempt ledger and provenance patterns.
- Selected-action to replay linkage.
- Deliberation sidecar patterns.

### Nuclear War-specific components

- The current `Observation` model:
  `~/.codex/worktrees/903e/wopr/nuclear_war/src/nuclear_war_env/observation.py`
- The current `ActionType` and action payloads:
  `~/.codex/worktrees/903e/wopr/nuclear_war/src/nuclear_war_env/action_models.py`
- Game state and legal-action generation.
- Card and population consequences.
- Current measures.
- Replay schemas and validators tied to those domain objects.

### Implementation conclusion

The pivot is not a country pack, prompt overlay, or configuration-only change.
It is a new DATE-backed World that can reuse WOPR's Room and provenance
machinery. The implementation choice remains open between:

1. Defining a generic World protocol and implementing the new World behind it.
2. Extracting a narrower adapter around the existing decision, deliberation,
   action-release, and trace seams for this week's evidence.

The one-week schedule and honest runnable-evidence requirement should decide
between these, not a preference for architectural breadth.

## Design corrections that future agents must retain

### Do not collapse the contribution back into Nuclear War

Nuclear War is the starting demonstration and provenance. The contribution is
the Room evaluation pattern and its application to a more fitting World.

### Do not make the interpreter the game master

The interpreter maps language to formal action and exposes ambiguity. It does
not choose hidden facts, author injects, or decide consequences.

### Do not force symmetric Rooms

Each actor gets an institutionally appropriate Charter. Experimental neatness
does not override scenario fidelity.

### Do not equate disagreement with failure

Disagreement can reveal mandate conflict, information separation, or authority
dynamics. Evaluation should examine how the Room handles it.

### Do not invent private victory conditions without a reason

Seat mandates and actor-level objectives are sufficient to create meaningful
tension. A hidden personal score would distort the national-security task.

### Do not randomize strategic intent with a seed

Different intent creates a different authored setup with a different ID and
hash. Seeds vary bounded evidence and friction.

### Do not force one opening because the design conversation used a grill

The arena is a setup registry. A selected example is a demonstration path, not
the system boundary.

### Do not imply endorsement or classified fidelity

DATE is a public training environment used as a design basis. Public U.S. roles
and methods can be recognizable without claiming official validation or access
to non-public procedure.

### Do not rewrite historical ADRs silently

The existing decisions govern what actually ran. A pivot should add explicit
superseding decisions and preserve the prior evidence trail.

## Open scientific and design questions

These questions remain unresolved and should be handled in conversation before
broad implementation.

1. What exact evaluation objective and task statement is shared across all
   matched runs?
2. Which objectives belong to the World, which belong to each actor, and which
   belong to individual seat mandates?
3. What are the U.S., Himaldesh, and Olvana Room Charters?
4. Which public sources support each seat, authority, information entitlement,
   and persona?
5. Does the crisis cycle use simultaneous decisions, asynchronous turns, or a
   bounded hybrid?
6. What formal actions can a Room authorize?
7. Which state variables are sufficient for the selected training objectives?
8. What transition and consequence mechanics are hard-coded, seeded, or
   scenario-triggered?
9. What outcome vector is reported, and are any dimensions aggregated?
10. What terminal, abort, and inadmissibility conditions apply?
11. What setup dimensions belong in the full registry?
12. What minimum runnable catalog can be implemented and tested this week
    without representing it as the arena's limit?
13. Should this week's implementation extract a generic World protocol or use a
    narrower adapter?
14. Which glossary terms and ADRs must be superseded?
15. Which public DATE material can be quoted, adapted, or redistributed in the
    application and microsite?
16. Can the new World produce enough verified runnable evidence before the
    contest deadline, or must the application distinguish implemented evidence
    from the proposed DATE extension?

## Exact next design pass

The next substantive pass should remain design work rather than immediate code
mutation:

1. Research and derive provisional Room Charters for the actual United States,
   Himaldesh, and Olvana from public official sources.
2. Identify shared actor-level objectives and seat-specific professional
   mandates without inventing private victory conditions.
3. Define each seat's information entitlement, communication permissions, and
   release authority.
4. Define the crisis decision cycle and timing.
5. Define the minimum formal action vocabulary and state variables required by
   the training objectives.
6. Map the complete setup dimensions and then select a minimum runnable suite as
   a demonstration, not a limitation.
7. Choose the generic-protocol or narrow-adapter implementation path based on
   the remaining week and required evidence.
8. Write explicit superseding ADRs and Packet language only after those choices
   are approved.

## Transfer state

The concise handoff was already sent to the existing main thread titled `Plan
ChinaTalk contest week`. This complete record should also be sent there. The
main thread should treat this file as the archival context and the concise
handoff as its quick-start summary.

No implementation is authorized merely by this archive. Its purpose is to
preserve the conversation and let the main thread continue the design with the
owner from the same state.
