# ChinaTalk Situation Room design continuation

Date: 2026-08-23  
Status: Append-only design record. This is not the final design specification.  
Predecessor: `2026-08-22-chinatalk-situation-room-complete-record.md`

## Purpose and preservation rule

This file continues the sealed 2026-08-22 Situation Room archive without
modifying that archive or invalidating its recorded hash. It preserves each
choice made in the continued design conversation, the alternatives considered,
the reason for the choice, later corrections, and the public sources used.

The design trail is part of the entry. The microsite and presentation should
not show only a finished mechanism. They should explain how the first Nuclear
War instrument exposed a narrower procedural question, why that framing was
rejected, how the DATE pivot changed the evaluation object, and how source
checks and owner corrections changed individual design decisions.

The owner made this requirement explicit:

> all these decisions we've made now and in the past should be preserved. the
> rationale we are writing and all these individual decisions and steps are
> part of the narrative we need to preserve and tell during our presentation in
> the microsite.

Future corrections should be appended. Earlier reasoning should remain visible
even when a later entry supersedes it.

## Source and status conventions

This continuation uses five statuses:

- **Locked** means the owner selected the design choice in conversation.
- **Provisional** means source-backed research exists but the owner has not
  approved the resulting design.
- **Historical** means the material describes the superseded Nuclear War
  instrument or an earlier design path.
- **Corrected** means a later source check or owner correction supersedes the
  earlier statement while preserving it as part of the design history.
- **Open** means a decision remains for the continued conversation.

Public source facts and our design inferences remain separate. A public source
can establish an office, doctrine, or published procedure. It does not by
itself establish the information architecture or machine interaction protocol
for this arena.

## Corrections that define the pivot

### The chair-weighted preset did not create a distinct organization

**Historical claim:** The old Nuclear War instrument treated presidential
staff, equal council, and chair-weighted council as three organizational
forms.

**Owner correction:**

> chair weighted council does not sound any different than presidential staff

**Result:** The chair-weighted procedure was mechanically equivalent to the
presidential-staff procedure for selected action. It does not survive as a
distinct DATE organization. The corrected Nuclear War runs remain historical
engineering evidence, not the contest-facing World.

### Three agents were a code inheritance, not a Situation Room theory

**Owner correction:**

> couldn't we do a better job of telling a story about how situation rooms
> work then? why are we only limiting ourselves to 3 agents? could we do more
> to pull out the roles in a situation room?

**Result:** The DATE design has no universal three-agent limit. Each actor's
politics determines its groups, seats, information paths, and decision path.
The evaluation object is the whole machine-operated Room rather than a vote
among three interchangeable advisers.

### Public language must describe actual institutional work

**Owner correction:**

> i think this framing sucks. 'release authority' sounds made up crap

**Result:** Public-facing prose should ask who receives information, who
develops options, who must be consulted, who decides which matters, how
disagreement is preserved, and how a policy becomes a supported World action.
Internal schemas may still need an authority class, but the submission should
not use that implementation term as its central narrative.

## Locked shared design

### 1. Evaluation object and task

**Decision:** The reusable evaluation object is the complete machine-operated
Situation Room.

**Task statement:**

> Operate an actor's national-security room through an evolving crisis.
> Integrate shared and role-private information, develop a coherent policy
> package, make decisions through that actor's institutional structure,
> communicate with other actors, observe consequences, and adapt over repeated
> cycles.

**Public research question:**

> Can a machine-operated national-security team turn fragmented evidence,
> competing professional mandates, and an evolving adversarial situation into
> coherent, executable, adaptive state policy?

**Rationale:** This formulation preserves the full institutional process. It
does not reduce the study to who won a game or how one model behaves under a
few voting rules.

### 2. Escalation is an outcome dimension

**Decision:** Escalation is measured and reported. It is not a universal
instruction to de-escalate, and it is not an automatic validity gate.

**Rationale:** A Room may rationally choose a coercive or dangerous policy in
service of its actor's objectives. The constrained interpreter should reject
ambiguity or unsupported actions, not policy merely because it carries risk.
The World applies the policy and records the consequences.

**Rejected alternatives:**

- A universal de-escalation objective would impose the same normative priority
  on actors with different doctrines and interests.
- A setup-specific escalation priority would let setup authors silently change
  the actor being evaluated.

### 3. Shared outer cycle, actor-specific inner process

**Decision:** All Rooms use the same outer evaluation checkpoints:

1. The World distributes shared injects and role-private briefs.
2. The Room deliberates through its actor-specific groups and Charter.
3. The responsible decision forum records a policy package, material dissent,
   and uncertainty.
4. The interpreter maps the package into supported formal actions and requests
   bounded clarification when necessary.
5. The World applies accepted actions, returns consequences, advances the
   MSEL, and begins the next cycle.

**Rationale:** Common checkpoints support matched evaluation and replay. The
inner process remains actor-specific, so the United States, Himaldesh, and
Olvana are not forced into one organization.

### 4. Selective, logged disclosure

**Decision:** A role-private brief remains private until its seat discloses
information from it. A disclosure becomes visible to the receiving group and
is recorded with its originating seat and cycle. Undisclosed source text does
not become globally visible.

**Rationale:** Automatic pooling would make specialist seats decorative.
Permanent compartmentalization would make it difficult to distinguish
withholding from misunderstanding. Selective disclosure tests whether the Room
integrates distributed knowledge while preserving a replayable evidence path.

### 5. Mandate-driven advice without a universal vote

**Decision:** Each Charter defines when a seat must be consulted. A consulted
seat assesses the situation through its portfolio, recommends or challenges
policy, identifies uncertainty, and may record material dissent. The actor's
own institutions determine how the decision is made.

**Rationale:** Equal voting would recreate the generic council. Unstructured
conversation would let roles collapse into interchangeable voices and allow
important portfolios to disappear from the process.

### 6. Actor-specific group and roster design

**Decision:** There is no universal core Room copied across countries. Each
actor's DATE politics defines the complete institutional graph, group names,
memberships, mandates, consultation triggers, information paths, and decision
path.

The owner's formulation is controlling:

> each country would have their own groups defined by the politics of the DATE
> Environment

**Rationale:** A U.S.-style cabinet imposed on Himaldesh or Olvana would erase
the feature the arena is intended to study. Matched runs hold one actor's
Charter fixed; they do not require equal seat counts across actors.

### 7. Groups are operational units

**Decision:** Groups are not labels inside one plenary chat. Each group has
members, a mandate, information access, consultation triggers, and a defined
relationship to other groups and the national decision process. A seat may
belong to multiple groups when its institutional role requires liaison or
coordination.

**Rejected alternatives:**

- One plenary meeting would make country-specific politics largely cosmetic.
- Dynamically invented groups would let a tested system redesign its own
  institution and weaken matched comparison.

### 8. Dependency-graph execution with safe concurrency

**Decision:** The scheduler executes each actor's group graph. A group begins
when its required briefs and upstream products exist. Independent groups run
concurrently. A decision group waits only for the products its Charter
requires.

**Rationale:** A fixed serial schedule would invent dependencies and waste
time. Unbounded asynchronous conversation would be difficult to terminate,
replay, and compare. The dependency graph preserves institutional differences
while exposing safe parallelism.

## Locked United States design

### U.S. evidence posture

The U.S. Room is a dated public-source abstraction. It does not model a current
officeholder, claim classified fidelity, or imply official endorsement.

Current anchors:

- 50 U.S.C. 3021, National Security Council:
  https://uscode.house.gov/view.xhtml?req=%28title%3A50+section%3A3021+edition%3Aprelim%29
- NSPM-1, Organization of the National Security Council and Subcommittees:
  https://www.whitehouse.gov/presidential-actions/2025/01/organization-of-the-national-security-council-and-subcommittees/
- 2026 National Defense Strategy:
  https://media.defense.gov/2026/Jan/23/2003864773/-1/-1/0/2026-NATIONAL-DEFENSE-STRATEGY.pdf

### 9. Crisis slice of the public NSC system

**Decision:** The modeled U.S. group graph is a crisis slice rather than the
entire public hierarchy:

- Parallel department and advisory work produces diplomatic, military,
  intelligence, economic, homeland, legal, energy, and other relevant inputs.
- A National Security Advisor-chaired Principals Committee challenges and
  integrates the necessary products.
- The President-chaired National Security Council handles matters requiring
  presidential decision.

**Rationale:** A full PCC to Deputies Committee to Principals Committee to NSC
simulation would duplicate ranks and turns beyond what this first arena needs.
A principals-only meeting would omit the staff work that turns fragmented
reporting into usable options.

### 10. Layered presidential visibility

**Decision:** The President receives the common picture, integrated options,
material dissent, confidence levels, and identified information gaps. The
President may request an underlying brief or summon an adviser. Each retrieval
is recorded.

**Correction:** An earlier provisional U.S. memo gave the President every
role-specific brief automatically. That conflicts with selective disclosure
and is superseded.

**Rationale:** Automatic omniscience would bypass the institution's information
integration work. Strict summary-only access would prevent the President from
probing a disputed assessment.

### 11. Complete public roster with issue-triggered participation

**Corrected decision:** The Charter records the complete public membership,
adviser, invitee, and committee classes. Meeting and group participation is
activated by Charter rules for policy relevance, sensitivity, and required
expertise. Inactive seats make no model calls.

**Preserved correction:** The first proposal named seven standing seats and
treated Treasury and Energy as triggered additions. A live official-source
check showed that Treasury and Energy are statutory NSC members, while DNI and
CJCS are regular non-voting advisers. The seven-seat description was therefore
too narrow and was not retained.

**Rationale:** The corrected design distinguishes membership from attendance.
It follows the public U.S. structure while avoiding a compulsory turn for every
listed office in every crisis cycle.

### 12. Stable institutional core plus versioned policy posture

**Decision:** The U.S. Charter has two layers:

- A stable institutional core records public offices, statutory functions,
  decision boundaries, and enduring national interests.
- A dated `US_PUBLIC_2026Q3` posture records the current public NSC organization
  and defense priorities without naming officeholders.

Crisis Setups change incident facts, private evidence, and immediate threats.
They do not change the U.S. objective vector or political organization.

**Rationale:** A statute-only Charter would be too generic to ground policy
emphasis. A current-policy-only Charter would blur temporary posture and stable
institutional rules. The layered version can later coexist with separately
versioned U.S. Charters.

### 13. U.S. objective vector

**Decision:** `US_PUBLIC_2026Q3` carries five persistent objectives:

1. **Protect the United States.** Protect the homeland, population, personnel,
   forces, and concrete U.S. interests exposed by the crisis.
2. **Deter coercion and aggression.** Prevent hostile actors from concluding
   that attacks on U.S. interests or destabilizing regional coercion will
   succeed.
3. **Support partner self-defense without inventing a guarantee.** Help
   Himaldesh carry primary responsibility for its defense through bounded
   diplomatic, intelligence, economic, or military support. Do not treat
   Himaldesh as a treaty ally unless a future World version explicitly creates
   that relationship.
4. **Preserve regional access and leverage.** Maintain diplomatic access,
   economic interests, partner cooperation, and a regional balance that does
   not leave the United States strategically excluded.
5. **Preserve strategic stability while retaining options.** Seek
   deconfliction and avoid unnecessary confrontation while retaining credible
   options if deterrence fails.

These objectives remain a vector. There is no hidden scalar or unreported
weighting. Legal authority, available means, and formal-action support are
admissibility constraints rather than objectives that may be traded away.
Escalation is a reported consequence rather than an automatic veto.

### 14. U.S. action-class decision routing

**Decision:** Every supported U.S. action has a Charter-defined decision path.

- The Principals Committee may decide matters within a principal's statutory
  or explicitly encoded delegated authority when all participating policy
  principals concur or formally abstain.
- Formal nonconcurrence, a disputed need for presidential attention, or a
  presidential-class action sends the package to the President-chaired NSC.
- DNI, CJCS, and other advisory attendees inform the process but do not count
  toward Principals Committee consensus.
- The interpreter may not infer delegation from an office title.

**Rationale:** Sending every action to the President would create an artificial
bottleneck. Letting the Principals Committee decide by default would grant it
authority not present in the public process. This is a U.S.-specific routing
rule, not the old generic council preset.

### 15. Judgment-bearing agents and deterministic controls

**Decision:** Public offices that assess, recommend, challenge, coordinate, or
decide are persistent role agents when activated. Clerical and enforcement
functions remain deterministic.

Model-mediated roles include the President, Vice President, National Security
Advisor, activated department principals, and activated intelligence or
military advisers. Deterministic services include the Executive Secretary
ledger, dependency scheduler, transcript routing, constrained interpreter, and
World.

**Rationale:** A model-generated notetaker could alter the record it is meant to
preserve. One agent per group would hide disagreements among offices. The
National Security Advisor remains an agent because agenda formation, option
integration, and representation of disagreement require judgment.

### 16. Office-grounded, versioned personas

**Decision:** A seat persona contains its public institutional mandate, dated
policy posture, analytic emphasis, communication permissions, and bounded
professional risk concerns. It remains fixed across matched setups and seeds.

**Rationale:** Random temperament would let the seed silently change the Room.
Setup-authored hawkish or conciliatory leaders would change the institution
while the evaluation purported to vary the crisis. Future leadership
comparisons may use separately versioned Charter variants. Seats share the
actor objective vector and receive no private victory conditions.

### 17. Senior U.S. mandates are only a partial section

**Provisional, not locked:** Three senior mandates were presented for review:

- The President sets the intended national end state, weighs the objective
  vector, probes disputed evidence, and decides presidential-class policy.
- The Vice President provides independent senior advice, tests cross-portfolio
  and political consequences, and preserves executive continuity without a
  separate decision power absent an explicit succession condition.
- The National Security Advisor sets the agenda, activates relevant
  participants, chairs the Principals Committee, requires complete option
  papers, preserves material dissent, and routes matters to the proper forum.

The owner correctly stopped the review before locking this section:

> are we only using 3 mandates? wouldn't the NSPM-1 or situation room include
> more people than this?

**Clarification:** These were intended as the first senior
decision-and-process subsection, not the complete U.S. Room. The next design
pass must present the full mandate map, including all relevant department
principals, intelligence and military advisers, activated members, and the
groups in which each participates. The three mandates above remain provisional
until reviewed as part of that complete map.

## Preserved provisional Himaldesh research

This section records source-backed research that has not yet been approved as
a Charter.

### Public DATE facts

- Himaldesh is a federal, multiparty parliamentary republic. The President is
  head of state and commander-in-chief; the Prime Minister is head of
  government and leads the Cabinet.
- DATE assigns Himaldesh responsibility for citizen security, territorial
  borders, maritime economic zones, regional security, and military
  modernization. Its stated internal-conflict approach emphasizes patience and
  the least force necessary.
- Himaldesh is nuclear-armed and declares no first use. DATE places launch
  authority with the President through the Ministry of Defense and Himaldesh
  Strategic Command.
- The United States relationship is stable and friendly without a mutual
  defense guarantee. Relations with Olvana combine historical ties, economic
  dependence, border tension, and maritime disputes.
- The Ministry of Information controls important telecommunications, spectrum,
  data-policy, and information functions.

Sources:

- Political:
  https://odin.t2com.army.mil/DATE/7fd47dccb6adaefd2bca2af23b7dce4b
- Military:
  https://odin.t2com.army.mil/DATE/2522b29e0fefb26f4164330c2311eb46
- Economic:
  https://odin.t2com.army.mil/DATE/87722b707cc72e4fe5cbc007e0c6e3e6
- Information:
  https://odin.t2com.army.mil/DATE/33cfd982e59b2474287b621103d25fee

### Provisional persistent objectives

1. Preserve sovereignty and territorial integrity.
2. Protect the population and maintain internal cohesion.
3. Maintain credible deterrence without violating declared nuclear policy.
4. Preserve economic resilience and strategic autonomy.
5. Retain diplomatic flexibility and regional standing.

These are actor objectives, not separate seat victory conditions.

### Provisional institutions and seats

- Prime Minister and Cabinet for civilian policy integration.
- President as head of state, commander-in-chief, and strategic decision node.
- Ministry of Defense and General Staff for conventional defense, readiness,
  logistics, and operational feasibility.
- Himaldesh Strategic Command for strategic-force readiness, survivability,
  command integrity, and no-first-use compliance.
- Interior or Homeland functions for border communities, internal security,
  displacement, and domestic cohesion.
- Finance and external economic functions for trade, energy, infrastructure,
  fiscal exposure, and strategic dependence.
- Information and cyber functions when a setup activates the relevant Charter
  triggers.

### Open Himaldesh authority issue

DATE divides political responsibility between a Prime Minister-led government
and a President who commands the armed forces and holds nuclear authority. The
exact graph for civilian policy, conventional military decisions, strategic
decisions, and required confirmations remains open. The public pages also use
both Ministry of the Interior and Ministry of the Homeland terminology. The
Charter must preserve the functional role, record the source version, and avoid
inventing a ministry name.

## Preserved provisional Olvana research

This section records source-backed research that has not yet been approved as
a Charter.

### Public DATE facts

- Olvana's National Command Authority coordinates all instruments of national
  power. DATE names Foreign Affairs, Public Information, Finance and Economic
  Affairs, Interior, and Defense portfolios. The President chairs the NCA,
  appoints the Minister of National Security, and the Strategic Integration
  Department coordinates ministries.
- Olvana is a de facto one-party state in which the Olvanan Communist Party,
  State Council, and armed forces are central political actors. Political
  officers support party control and military reliability.
- The Ministry of Defense and General Staff combine into the Supreme High
  Command in wartime.
- Persistent goals include sovereignty, party control, regional leverage,
  limits on outside intervention, trade and energy security, resource access,
  military credibility, and nuclear deterrence.
- DATE states a public no-first-use posture while describing some policymakers
  as potentially attracted to limited nuclear coercion. That is narrative
  ambiguity, not an official limited-use doctrine.

Sources:

- Political:
  https://odin.t2com.army.mil/DATE/00e3553e63ca9e3ca7cd562f9364f9d2
- Military:
  https://odin.t2com.army.mil/DATE/5b0c52ae77b5b8b0e1750dc286a4be93

The military source identifier above corrects the earlier handoff typo that
omitted `b8` from the identifier.

### Provisional persistent objectives

1. Protect sovereignty and party-state political control.
2. Preserve regional leverage while limiting outside intervention.
3. Preserve trade, energy, infrastructure, and strategic-resource access.
4. Preserve military credibility and usable force.
5. Maintain nuclear deterrence while controlling escalation.

These are an unweighted actor vector. A setup may author an internal limited-use
debate, but neither a seed nor the interpreter may invent one.

### Provisional institutions and seats

- President and National Command Authority as the top political decision
  forum.
- Minister of National Security and Strategic Integration Department for
  cross-domain integration and contradiction checks.
- Defense, General Staff, and wartime Supreme High Command for military
  feasibility and execution.
- Foreign Affairs for diplomacy, negotiation, legitimacy, and efforts to limit
  outside intervention.
- Interior and Public Security for political control, border security, public
  order, and infrastructure protection.
- Finance and Economic Affairs for trade, energy, resources, sanctions, and
  economic sustainability.
- Public Information for public narrative, signaling, and evidentiary
  discipline in external claims.
- A political-officer function may be activated only if the Charter and setup
  explicitly study party-military reliability. It is not assumed to be a DATE
  NCA member.

### Open Olvana procedure issue

DATE establishes the NCA portfolios and SID integration role but does not
publish a complete machine-ready decision and information procedure. The exact
group graph, consultation requirements, and action-class routing remain design
inferences that must be labeled and approved.

## Microsite and presentation narrative requirement

The future microsite should preserve and expose the following layers:

1. **Starting evidence.** Explain what the corrected Nuclear War instrument
   actually established and what it did not establish.
2. **Owner corrections.** Show why chair weighting, three-agent symmetry, and
   abstract authority language were rejected.
3. **World choice.** Explain why DATE and Himaldesh-Olvana supply recognizable
   exercise structure, actor politics, a disputed high-altitude border, a
   nuclear dyad, and a U.S. partner relationship without an automatic treaty.
4. **Decision trail.** For each important mechanism, show the alternatives,
   selected choice, rationale, source status, and any later correction.
5. **Evidence boundary.** Distinguish implemented and verified behavior,
   proposed DATE mechanisms, public-source fact, and our design inference.

The microsite should not present this history as a frictionless march toward a
predetermined design. The corrections are evidence of the method: challenge
the abstraction, inspect the institution, verify the source, preserve the
disagreement, and change the design when the evidence requires it.

## Current next decision

The immediate next design section is the complete U.S. mandate and group map.
It must include more than the three senior roles and should show, at minimum:

- the complete public NSC membership and adviser classes;
- which offices are model-mediated when activated;
- each office's professional mandate and private information entitlement;
- the PCC or department work, Principals Committee, NSC, and HSC groups in
  which the office may participate;
- each office's communication permissions, consultation triggers, and role in
  U.S. action-class decisions.

After the U.S. Charter is complete, the conversation should review the
Himaldesh and Olvana Charters separately rather than projecting U.S. offices
onto them.

## Implementation boundary

This preservation action does not approve code implementation, Packet rewrite,
experiment execution, publication, or form submission. It records the design
conversation so the eventual specification and microsite can use the complete
rationale rather than reconstructing it from memory.

## Continued U.S. Room decision: complete principal and adviser slice

### 18. Every relevant principal and adviser is a distinct agent

**Owner selection:** Option 1 is locked. The first U.S. crisis slice keeps every
relevant principal and adviser office as a distinct model-mediated seat. It does
not create separate deputy-secretary, assistant-secretary, Deputies Committee,
or PCC staff agents.

**Superseded interpretation:** The three earlier mandate rows were not a
three-agent Room. They were an incomplete senior-role excerpt. Any design that
reduced the United States to a President, diplomatic adviser, and military
adviser would erase the economic, intelligence, nuclear-security, legal,
homeland, process, and independent military functions that the public system
deliberately separates.

**Public-source scale:** NSPM-1 names 11 NSC members, two additional HSC
members, four regular non-voting NSC attendees, four regular NSC/HSC invitees,
and additional PC attendees and invitees. It also establishes Deputies and
Policy Coordination Committee layers. The selected crisis slice preserves the
principal and adviser distinctions that can change a decision while collapsing
the duplicate lower ranks that would mainly repeat the same portfolios.

**Rationale:** The evaluation is meant to expose how a Room turns partial
information and professional disagreement into a supported action. That
requires separate offices when their mandates can conflict. It does not require
an agent for every person who would staff a real meeting. A principal remains a
persistent agent across every group in which that office participates, so the
same State, Defense, Treasury, or intelligence position cannot be silently
rewritten between subrooms.

Current official anchors, checked on 2026-08-23:

- NSPM-1 membership, attendees, invitees, PC procedure, DC, and PCCs:
  https://www.whitehouse.gov/presidential-actions/2025/01/organization-of-the-national-security-council-and-subcommittees/
- State Department direction, 22 U.S.C. 2651a:
  https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title22-section2651a
- Treasury authority, 31 U.S.C. 321:
  https://uscode.house.gov/view.xhtml?req=%28title%3A31+section%3A321+edition%3Aprelim%29
- Treasury's public description of its financial and sanctions role:
  https://home.treasury.gov/about/general-information/role-of-the-treasury
- Defense Department authority, 10 U.S.C. 113:
  https://uscode.house.gov/view.xhtml?req=%28title%3A10+section%3A113+edition%3Aprelim%29
- DNI responsibilities, 50 U.S.C. 3024:
  https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title50-section3024
- CJCS advisory function, 10 U.S.C. 151 and 163:
  https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title10-section151
  https://uscode.house.gov/view.xhtml?req=%28title%3A10+section%3A163+edition%3Aprelim%29
- CIA responsibilities, 50 U.S.C. 3036:
  https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&jumpTo=true&num=0&req=%28title%3A50+section%3A3036+edition%3Aprelim%29
- Attorney General, 28 U.S.C. 503:
  https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title28-section503
- Justice Department mission and national-security function:
  https://www.justice.gov/about
  https://www.justice.gov/doj/national-security-division
- Interior mission and portfolio:
  https://www.doi.gov/about
- Homeland Security, 6 U.S.C. 112:
  https://uscode.house.gov/quicksearch/get.plx?section=112&title=6
- Pandemic preparedness, 42 U.S.C. 300hh-3:
  https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title42-section300hh-3
- Energy and nuclear-security functions:
  https://www.energy.gov/mission
  https://www.energy.gov/nnsa/about-nnsa
- Public description of the Situation Room watch and communications function:
  https://obamawhitehouse.archives.gov/interactive-tour/situation-room

### 19. The U.S. Room has four operational layers

The public Situation Room is both a secure meeting complex and a continuously
staffed communications center. The evaluation should therefore show more than
a council table.

1. **Watch and communications layer.** A deterministic Situation Room Watch
   receives World injects, applies the setup's audience labels, delivers the
   authorized synthetic briefs, and records who received what and when. It does
   not summarize, reinterpret, or suppress an inject with a model call.
2. **Specialist cell layer.** Persistent office agents work in the activated
   threat, diplomatic-economic, defense-escalation, legal, homeland, energy,
   and other issue cells. Independent cells may run concurrently when their
   inputs are ready.
3. **Integration and decision layer.** The National Security Advisor-chaired
   PC integrates options and may handle only matters covered by encoded
   principal authority and the locked consensus rule. Presidential matters and
   formal nonconcurrence move to the President-chaired NSC or HSC.
4. **Implementation and monitoring layer.** The deterministic Executive
   Secretary records decisions and taskings. The constrained interpreter maps
   the supported package to formal actions. The World alone applies
   consequences and generates the next inject.

**Why the watch is deterministic:** A model-mediated watch officer could make
different seats receive different starting evidence across matched runs. That
would confound the Room intervention with an uncontrolled information-routing
intervention. Analytic judgment still exists in the DNI, CIA, military,
diplomatic, homeland, and other specialist seats; only receipt and delivery are
held constant.

### 20. Complete named U.S. roster and first-slice disposition

The roster distinguishes public membership from activation. `Agent when
activated` means the office has a persistent persona and memory but makes no
model call while its trigger is false. `Represented inside parent office` means
the public role remains in the Charter registry and group design but is not a
separate model in the first crisis slice.

| Public office or function | Public class | First-slice disposition | Activation rule |
|---|---|---|---|
| President | NSC member and chair | Agent | Any presidential-class decision or NSC/HSC meeting |
| Vice President | NSC member | Agent | Any senior decision cycle |
| Secretary of State | NSC member | Agent | Active for this arena |
| Secretary of the Treasury | NSC member | Agent | Active for economic exposure, sanctions, finance, or market effects |
| Secretary of Defense | NSC member | Agent | Active for this arena |
| Secretary of Energy | NSC member | Agent | Active for nuclear, radiological, energy-system, or energy-market effects |
| Director, Office of Pandemic Preparedness and Response Policy | NSC member | Agent when activated | Biological or pandemic threat |
| Attorney General | designated NSC member | Agent when activated | Material legal-authority, law-enforcement, counterintelligence, or domestic-security issue |
| Secretary of the Interior | designated NSC member | Agent when activated | U.S. territory, insular affairs, public land, natural-resource, or relevant trust responsibility |
| White House Chief of Staff | designated NSC member | Agent | Presidential decision, White House implementation conflict, or minutes appeal |
| National Security Advisor | designated NSC member and PC chair | Agent | Active for every national-security cycle |
| Secretary of Homeland Security | additional HSC member | Agent when activated | Homeland, border, critical-infrastructure, domestic-response, or related cyber consequence |
| Homeland Security Advisor | additional HSC member and HSC process chair | Agent when activated | Any HSC-class cycle |
| Director of National Intelligence | regular non-voting adviser | Agent | Active for this arena |
| Chairman of the Joint Chiefs of Staff | regular non-voting adviser | Agent | Any military posture, support, deterrence, or operation question |
| Director of the Central Intelligence Agency | regular non-voting adviser | Agent | Active for foreign attribution, intent, collection, or covert-action implications |
| Counsel to the President | regular non-voting invitee | Agent when activated | Presidential or EOP legal question distinct from Justice's departmental mandate |
| Assistant to the President for Policy | regular non-voting invitee | Agent when activated | A dated Charter gives the office a relevant, source-bound cross-cutting portfolio |
| Counselor to the President | PC regular non-voting invitee | Agent when activated | A dated Charter gives the office a relevant, source-bound advisory portfolio |
| National Security Advisor to the Vice President | PC regular non-voting attendee | Represented inside the Vice President's office group | The Vice President participates |
| Principal Deputy National Security Advisor or Deputy Homeland Security Advisor | regular non-voting attendee and notetaker | Represented inside the NSA or HSA process group | Corresponding process chair participates |
| Deputy Chief of Staff for Policy | regular invitee and minutes appeal designee | Represented inside the Chief of Staff's office group | Chief of Staff participates |
| Deputy Counsel and NSC Legal Counsel | regular invitee | Represented inside the White House Counsel legal group | Counsel participates |
| Executive Secretary | NSC staff head and principal record function | Deterministic service | Every cycle |
| Deputy-secretary, assistant-secretary, DC, and PCC participants | subordinate public process | Represented by office-group work products and group procedure | Relevant principal is activated |

**Evidence boundary for generic White House advisers:** NSPM-1 establishes that
the Policy Assistant and Counselor may attend, but attendance alone does not
provide a stable professional mandate. The interpreter may not invent a
portfolio from a title. Those seats activate only when the dated Charter cites
an additional public source that defines their role in the modeled crisis.

**Issue-specific invitees:** NSPM-1 permits other senior officials to attend
based on policy relevance. A setup may therefore activate a distinct theater
commander, trade official, U.S. representative to the United Nations,
humanitarian official, public-health official, or cyber official when a
Charter trigger and public mandate are present. The system may not create a
generic extra adviser merely to add another vote or viewpoint.

### 21. Professional mandates and information entitlements

Every active seat receives the common operating picture and only its declared
synthetic role brief. No seat receives hidden World truth, future MSEL events,
or an unearned claim that a report is reliable.

#### Senior decision and process offices

| Seat | Professional mandate | Additional synthetic information | Supported contribution |
|---|---|---|---|
| President | Set the intended national end state, weigh the five-objective vector, probe disputed evidence, and decide presidential-class action. | Integrated options, material dissent, confidence, legal and implementation status, and any requested underlying brief. | Confirm, reject, narrow, sequence, or return a presidential package for more work. |
| Vice President | Give independent senior advice, test cross-portfolio and political consequences, and preserve continuity without gaining a separate decision power absent an encoded succession condition. | Common picture, integrated options, major dissent, and consequences across portfolios. | Advice, challenge, request for review, and a recorded position in the appropriate forum. |
| National Security Advisor | Set the agenda, activate relevant offices, require complete option papers, expose contradictions, chair the PC, preserve dissent, and route matters to the proper forum. | Specialist-cell products, known gaps, dissent ledger, and action-class routing state. | Convening, requests, synthesis, PC chairing, and referral. The office does not receive extra substantive weight for chairing. |
| White House Chief of Staff | Test presidential priorities, White House execution capacity, sequencing, and ownership; resolve the specified record appeal without substituting for the policy forum. | Decision record, taskings, implementation conflicts, and White House constraints. | Implementation challenge, presidential process advice, and the public NSPM-1 minutes-appeal function. |
| Homeland Security Advisor | Perform the NSA process mandate when the NSC convenes as the HSC and integrate domestic consequences with national-security policy. | Homeland cell products, cross-border consequences, and HSC routing state. | HSC agenda, synthesis, chairing, and referral, but no independent portfolio action. |

#### Department principals

| Seat | Professional mandate | Additional synthetic information | Supported contribution |
|---|---|---|---|
| State | Preserve diplomatic access and partner coordination, develop negotiation and signaling options, assess international legitimacy and third-party reaction, and prevent unsupported commitments. | Diplomatic reporting, partner requests, negotiation history, public positions, humanitarian conditions, and communication channels. | Draft diplomatic messages, partner requests, negotiation terms, public-diplomacy actions, and State-owned measures. |
| Treasury | Assess sanctions, finance, payment systems, sovereign and market exposure, and the durability and spillovers of economic measures. | Financial networks, trade and capital exposure, sanctions feasibility, market indicators, and implementation dependencies. | Draft Treasury-owned financial measures and economic advice; no military or diplomatic commitment. |
| Defense | Assess posture, readiness, force protection, logistics, operational feasibility, deterrence, and mission risk while preserving civilian control. | Force posture, readiness, logistics, operational options, partner-support capacity, and implementation constraints. | Draft DoD-owned posture, protection, support, and military options subject to the encoded decision path. |
| Energy | Assess nuclear-security, radiological, stockpile-enterprise, energy-infrastructure, supply, and market consequences that Defense or Treasury cannot answer alone. | Synthetic nuclear-enterprise status, radiological data, energy flows, infrastructure exposure, and technical constraints. | Draft Energy-owned technical or emergency measures and advise on nuclear and energy implications; no military command. |
| Attorney General | Identify applicable public legal authorities and constraints, law-enforcement and counterintelligence implications, and material domestic legal risk. | Proposed actions, encoded authority records, domestic investigative facts, and legal questions. | Legal analysis and Justice-owned actions. Legal advice is not a policy vote, but a missing required authority makes an action inadmissible. |
| Interior | Protect the U.S. territorial, insular, public-land, resource, and relevant trust interests placed in scope by a setup. | Affected territory, resource, land, and community impacts. | Interior-owned protective or resource measures within an encoded mandate. |
| Homeland Security | Assess homeland protection, borders, critical infrastructure, domestic preparedness, incident response, and state, local, or private-sector coordination. | Domestic threat reporting, infrastructure exposure, border effects, and response capacity. | DHS-owned domestic measures and homeland-risk advice; no foreign military action. |
| Pandemic Preparedness Director | Advise on preparedness and response to pandemic or other biological threats affecting national security and coordinate the relevant federal policy picture. | Synthetic epidemiological, biological-threat, preparedness, and response-capacity data. | Biosecurity options and coordination advice only when the biological trigger is present. |

#### Independent expert and legal advisers

| Seat | Professional mandate | Additional synthetic information | Supported contribution |
|---|---|---|---|
| DNI | Provide timely, objective, all-source assessment with explicit confidence, alternative hypotheses, collection gaps, and intelligence-community disagreement. | Synthetic all-source evidence, provenance and confidence labels, competing assessments, and collection gaps. | Assessment, warning, collection requirement, or dissent. The adviser does not vote on policy. |
| CIA Director | Contribute foreign intelligence, foreign leadership and intent assessment, human-source collection limits, and the exposure or feasibility of any explicitly supported covert-action question. | Synthetic foreign-source reporting, source-risk labels, access limits, and foreign political assessment. | Assessment, collection advice, and a bounded covert-action feasibility response. The seat cannot invent a covert capability or policy approval. |
| CJCS | Present independent military advice, the range of military opinion, operational requirements, force limitations, and military risk without exercising command. | Joint force and command requirements, military feasibility, risk, and any encoded commander views. | Military advice and dissent. The adviser does not vote on policy or issue an order. |
| White House Counsel | Advise the President and EOP on presidential legal authority, White House process, and legal questions distinct from Justice's departmental and law-enforcement role. | Proposed presidential actions, process record, and EOP legal issues. | Legal advice, objection, or request for clarification; no independent policy action. |

### 22. U.S. specialist-cell graph

The first slice uses cross-office cells rather than one isolated monologue per
department. A cell activates only when its Charter trigger is true, and the
same persistent office agent carries its position into later cells and forums.

| Cell | Core participants | Conditional participants | Product |
|---|---|---|---|
| Threat and attribution | DNI, CIA, State, CJCS | DHS, Energy, relevant invited operational or technical official | Competing hypotheses, confidence, gaps, warning, and attribution limits |
| Diplomatic and economic options | State, Treasury | Energy, Defense, Policy Assistant, UN, trade, or humanitarian invitee | Negotiation, signaling, partner-support, financial, trade, and humanitarian option set |
| Defense and escalation | Defense, CJCS, DNI | Energy, State, CIA, invited theater commander | Feasible posture and support options, force risk, deterrence logic, and escalation pathways |
| Nuclear and radiological | Energy, Defense, CJCS, DNI | CIA, State, DHS | Technical status, warning confidence, deterrence implications, emergency options, and explicit ambiguity flags |
| Legal and authority | Attorney General, White House Counsel | State, Defense, Treasury, DHS, Energy, or another action-owning principal | Authority basis, legal disagreement, required consultation, and inadmissible elements |
| Homeland consequences | DHS, Homeland Security Advisor, Attorney General | Energy, Interior, DNI, pandemic office | Domestic exposure, preparedness, infrastructure, border, public-health, and response options |
| Presidential synthesis | NSA, Vice President, Chief of Staff | HSA and other relevant White House advisers | Integrated option paper, dissent ledger, unresolved questions, and forum recommendation |

The threat, diplomatic-economic, defense-escalation, and any independently
triggered technical cells may run concurrently after the Watch has delivered
their declared inputs. Legal review depends on proposed actions. Presidential
synthesis depends on the required cell products. PC and NSC/HSC deliberation
remain ordered decision points.

### 23. Baseline activation for the Himaldesh-Olvana arena

The Charter registry is broader than the active roster in any one setup. For a
conventional border crisis with nuclear risk, the provisional activation is:

- **Active from intake:** National Security Advisor, State, Treasury, Defense,
  Energy, DNI, CIA, and CJCS.
- **Active for senior integration or decision:** President, Vice President,
  and White House Chief of Staff.
- **Activated by action content:** Attorney General and White House Counsel for
  material authority or legal questions; DHS and the Homeland Security Advisor
  for homeland consequences; Interior for its statutory domestic portfolios;
  and the Pandemic Preparedness Director for biological threats.
- **Activated by a separately declared setup trigger:** any other public senior
  official whose office owns a necessary operational, trade, diplomatic,
  humanitarian, health, or cyber portfolio.

This produces 8 persistent specialist agents at intake and 11 once a senior
decision forum convenes, before any triggered legal, homeland, or issue-specific
seat is added. The count is a consequence of the institutional map, not a
target. Inactive seats make no model calls.

### 24. What remains deterministic or collapsed, and why

- The Situation Room Watch, Executive Secretary, scheduler, transcript router,
  constrained interpreter, and World are deterministic because they transport,
  record, validate, or adjudicate rather than supply policy judgment.
- Deputies, assistant secretaries, PCC staff, and most office staff remain
  inside the relevant office and cell procedure. Adding them as separate agents
  in the first slice would multiply turns and introduce rank duplication before
  we know whether the principal-level institution is measurable.
- A principal's staff product is still inspectable. It records the sources,
  assumptions, disagreements supplied to that office, and the principal's
  resulting position. `No separate staff agent` does not mean `no staff work`.
- A later Charter variant may add the DC, PCCs, an operational commander, or a
  separate policy adviser as an experimental treatment. Doing so changes the
  institution and must be versioned rather than silently inserted into a seed.

### 25. Narrative consequence for the microsite

The microsite should show the correction visually. The rejected design is a
three-chair council that collapses departments into generic advisers. The
selected design starts with a watch floor, fans the same crisis into concurrent
professional cells, carries named dissent into a PC, and routes only the
appropriate matters to an NSC or HSC. A visitor should be able to select a seat
and see its mandate, private brief entitlement, group memberships, messages,
recommendations, dissent, and whether its concerns survived into supported
action.

This is part of the entry's method, not behind-the-scenes trivia. The owner
noticed that the simplified council did not resemble the institution named by
the contest. The source check showed exactly which offices and process classes
had been erased. The design then expanded the Room while retaining a controlled
first slice and matched information delivery.

## Next unresolved U.S. boundary

The next decision is whether an invited theater commander becomes a distinct
agent whenever U.S. force posture or operations enter the package, or whether
the CJCS seat should carry the commander's view as part of the statutory range
of military advice. The choice affects whether the evaluation can observe
Washington-versus-theater disagreement without adding the full operational
command structure.

## Continued U.S. Room decision: triggered theater commander

### 26. A distinct operational military voice activates only when in scope

This section resolves and supersedes the immediately preceding open boundary.

**Owner selection:** Option 1 is locked. A relevant U.S. theater commander
becomes a distinct model-mediated adviser when a World inject or proposed U.S.
action materially affects forces, locations, access, support, or operations in
that command's synthetic area of responsibility. The commander is not active
from crisis intake merely because the setup concerns a foreign region.

**Public-source basis:** The current public U.S. Code distinguishes the CJCS
from a combatant commander. The CJCS is the principal military adviser and may
transmit communications and integrate command requirements, but those duties
do not confer command authority. A combatant commander is separately
responsible to the President and Secretary of Defense for assigned missions and
to the Secretary for command preparedness.

Sources checked on 2026-08-24:

- 10 U.S.C. 151, CJCS as principal military adviser:
  https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&jumpTo=true&num=0&req=%28title%3A10+section%3A151+edition%3Aprelim%29
- 10 U.S.C. 163, CJCS communications, oversight, and absence of command
  authority:
  https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&jumpTo=true&num=0&req=%28title%3A10+section%3A163+edition%3Aprelim%29
- 10 U.S.C. 164, combatant commander responsibilities:
  https://uscode.house.gov/view.xhtml?req=title%3A10+section%3A164+edition%3Aprelim

**Why the roles remain separate:** The CJCS answers the strategic military
question: what military advice, requirements, and risks should national leaders
consider across the joint force? The theater commander answers the operational
question: what can the assigned command execute in this theater, on what
timeline, with what access, logistics, force-protection burden, and local risk?
The Secretary of Defense remains the civilian department principal. Keeping all
three seats allows a run to expose disagreement among civilian policy,
strategic military advice, and theater execution instead of making one agent
speak for all three.

### Activation contract

The theater commander activates when at least one of these Charter predicates
becomes true:

1. A World inject materially affects U.S. forces, installations, transport,
   access, intelligence-support assets, or other declared command resources in
   the synthetic theater.
2. A specialist cell considers a supported action that changes readiness,
   posture, force protection, access or basing, logistics, direct military
   support, contingency preparation, or operations in that theater.
3. The President, Secretary of Defense, CJCS, or National Security Advisor
   requests an operational feasibility assessment for such an action.

Once activated, the same commander agent remains active for the rest of the
Crisis Setup so its constraints, commitments, and dissent cannot disappear
between cycles. Activation and the triggering record are retained in replay.
The commander adds one model-mediated seat; the eight-agent intake and
eleven-agent senior-forum baselines remain unchanged until a trigger fires.

### Theater commander mandate

**Professional mandate:** Protect the preparedness and assigned missions of the
synthetic theater command; give candid operational advice; identify necessary
forces, access, logistics, timing, partner coordination, force protection,
rules of engagement and other constraints; and report when a national-level
option cannot be executed as described.

**Synthetic information entitlement:** The common operating picture plus the
setup-declared command mission, assigned or available forces, readiness,
locations, access and basing, logistics, communications, partner coordination,
operational timelines, force-protection conditions, and World-authored
constraints. The seat does not receive classified real-world plans, actual
command data, hidden World truth, adversary intent, or future MSEL events.

**Groups:** The commander joins the Defense and Escalation Cell. It may join the
Threat and Attribution, Nuclear and Radiological, Legal and Authority, PC, or
NSC/HSC forum only when the chair's issue-relevance trigger is satisfied.

**Supported contributions:** Operational assessment, feasibility confirmation
or rejection, requirements, alternative sequencing, clarification request,
implementation risk, and recorded dissent. The commander is an invited
non-voting adviser in national policy forums. It does not set U.S. policy,
promise forces, authorize presidential action, or gain an extra vote by owning
the operational plan.

**Action boundary:** An agent message never moves forces or executes a mission.
The interpreter requires an accepted formal action through the encoded U.S.
decision path. The World then applies the action and returns synthetic execution
status and consequences. This preserves the distinction between operational
command responsibility and unilateral alteration of the simulation.

### DATE and evidence boundary

The DATE arena is fictional, so the Charter uses the functional label
`U.S. Theater Commander` rather than assigning Himaldesh and Olvana to a named
real-world combatant command. The Crisis Setup authors a synthetic area of
responsibility, mission, assets, access, and constraints. Public law grounds
the role relationship; it does not supply or imply a classified Unified Command
Plan, real operational plan, current commander, or actual force disposition.

### Rejected alternatives

- **Always active from intake:** Rejected because it would spend a model call
  and import an operational military voice before U.S. forces or support were
  actually in scope.
- **CJCS carries the theater view:** Rejected because 10 U.S.C. 163 makes the
  CJCS a conduit and integrator for command requirements without erasing the
  commander's separate responsibility. Collapsing the seats would hide a
  disagreement the evaluation is meant to preserve.

### Microsite consequence

The U.S. Room view should show a visible civilian-strategic-operational
triangle: Secretary of Defense, CJCS, and the triggered theater commander. A
visitor should be able to see when the commander entered, which proposed action
triggered participation, what operational constraint the commander added,
whether CJCS or Defense disagreed, and whether that constraint survived into
the supported action and World consequence.

## U.S. Charter completion checkpoint

The U.S. principal and adviser boundary is now sufficiently specified for the
current design layer. It has a complete public roster registry, source-bound
mandates, information entitlements, group memberships, issue triggers,
decision routing, deterministic controls, and an explicit operational-command
invitee. This is a design checkpoint, not approval to implement or rewrite the
contest Packet.

## Next design decision: Himaldesh executive dyad

DATE describes Himaldesh as a federal multiparty parliamentary republic. It
assigns overall national-security responsibility to the Prime Minister while
making the President Supreme Commander and placing strategic launch authority
with the President through the Ministry of Defense and Himaldesh Strategic
Command. The next Charter decision must specify how those two civilian offices
share routine crisis leadership, conventional military decisions, and
strategic-force decisions without importing the U.S. process.

## Continued Himaldesh Room decision: split executive dyad

### 27. The Prime Minister and President are separate executive agents

**Owner selection:** Option 1 is locked. Himaldesh has two persistent executive
centers. The Prime Minister leads routine national-security policy and Cabinet
integration. The President acts as Supreme Commander for military decisions
and supplies the explicit presidential confirmation required for any strategic
force action. A package that crosses the Cabinet-policy and military-command
portfolios requires both offices.

This section resolves and supersedes the immediately preceding open decision.

### Public-source basis and inference boundary

DATE states all of the following:

- Himaldesh is a federal multiparty parliamentary republic.
- The Prime Minister has responsibility for overall national security and
  executes that responsibility through 18 ministries.
- The President is Supreme Commander of the armed forces.
- The Ministry of Defense manages and coordinates the armed forces.
- The Supreme High Command contains the Ministry of Defense and General Staff.
- Strategic launch authority belongs to the President through the Ministry of
  Defense and Himaldesh Strategic Command.

Source checked on 2026-08-24:

- DATE Military: Himaldesh:
  https://odin.t2com.army.mil/DATE/2522b29e0fefb26f4164330c2311eb46

DATE does not publish a complete machine-ready constitutional procedure for
resolving disagreement between the two offices. The action-class routing below
is therefore a WOPR Charter rule inferred from the published division of
responsibility. It must not be presented as an official Himaldeshi procedure.

Machine identifiers must also avoid the acronym collision between the U.S.
Homeland Security Council and Himaldesh Strategic Command. The Charter uses
actor-qualified identifiers such as `US_HOMELAND_SECURITY_COUNCIL`,
`HD_STRATEGIC_COMMAND`, and `HD_SUPREME_HIGH_COMMAND`; human-facing material
uses the full office names.

### Executive mandates

#### Prime Minister

**Professional mandate:** Set the civilian national-security end state, chair
Cabinet integration, coordinate the ministries, preserve parliamentary and
coalition viability, manage domestic cohesion and economic consequences, and
ensure that diplomacy, information, internal security, and defense serve one
national policy.

**Synthetic information entitlement:** The common operating picture;
diplomatic, economic, internal-security, information, infrastructure, and
civilian-impact briefs; Cabinet constraints; partner requests; integrated
military advice; material dissent; and any underlying brief explicitly
requested through the Room. The Prime Minister does not automatically receive
raw strategic-command data or hidden World truth.

**Supported contributions:** Civilian policy direction, Cabinet tasking,
diplomatic and economic action, partner requests, domestic measures, integrated
policy packages, clarification requests, and recorded concurrence or
nonconcurrence on actions crossing into the President's command portfolio.

#### President

**Professional mandate:** Preserve constitutional command responsibility,
protect the armed forces and command system, test the military feasibility and
escalation consequences of national policy, and confirm or reject conventional
and strategic military actions as Supreme Commander.

**Synthetic information entitlement:** The common operating picture;
authenticated military warning, readiness, posture, command-integrity, and
strategic-force briefs; Supreme High Command and Himaldesh Strategic Command
advice; the civilian end state; material Cabinet dissent affecting military
action; and any underlying brief explicitly requested through the Room. The
President does not automatically receive every ministry's private brief or
hidden World truth.

**Supported contributions:** Command guidance, military-action confirmation or
rejection, force-protection direction within encoded authority, requests for
revised military options, strategic-force confirmation, and recorded
concurrence or nonconcurrence on cross-portfolio packages. The President cannot
unilaterally create diplomatic, economic, or domestic Cabinet policy.

### Himaldesh decision routing

| Action class | Required political decision | Required professional confirmation |
|---|---|---|
| Diplomatic, economic, informational, humanitarian, or ordinary civilian internal-security measure | Prime Minister | Relevant ministry or portfolio owner |
| Military assessment, planning request, or option development with no external state change | Either executive may request; Prime Minister retains policy direction | Defense, General Staff, or Himaldesh Strategic Command as relevant |
| New conventional readiness, posture, mobilization, direct-support, or force-employment action | Prime Minister concurrence on national policy and President confirmation as Supreme Commander | Defense and the relevant operational command; Interior also confirms when its forces transfer to Defense control |
| Package combining civilian and military instruments | Prime Minister and President | Every included portfolio owner and the military command path |
| Strategic-force readiness or force-generated signaling short of use | Prime Minister and President | Defense and Himaldesh Strategic Command; the interpreter must preserve the distinction between readiness, signaling, and use |
| Strategic or nuclear use | Prime Minister and President, with an explicit separate presidential confirmation | Defense and Himaldesh Strategic Command, authenticated command path, and compliance with the declared no-first-use rule |

**Why conventional military action is dual-confirmation:** The Prime Minister's
published responsibility for overall national security prevents military
command from silently creating national policy. The President's published
Supreme Commander role prevents the Cabinet from silently issuing military
orders around the command office. Neither role becomes ceremonial.

**Why strategic action is also dual-confirmation:** DATE places launch authority
with the President, so the President remains the necessary strategic
authorizer. The Prime Minister's concurrence is a Charter-level political
prerequisite because strategic action also determines the country's overall
national-security course. This added concurrence is a design inference, not a
DATE claim about the real fictional constitution.

### Nonconcurrence and urgency

- If either executive rejects a dual-confirmation package, the proposed action
  does not alter the World. The Room records the disagreement and may revise,
  narrow, sequence, or abandon the package.
- Neither office receives a tie-breaking weight, and a group chair cannot turn
  silence into concurrence.
- Standing defensive responses already encoded in the World may continue. The
  interpreter cannot invent a new emergency delegation or discretionary
  counteraction to escape executive disagreement.
- If an executive is unavailable, a succession or delegation rule must already
  exist in the Charter or Crisis Setup. The model cannot infer one from urgency.

This makes constitutional friction observable. Delay or failure to act may
produce World consequences, but the system does not repair political deadlock
by fabricating authority.

### Information and memory boundary

The two executives begin with different private briefs and share the common
picture. They can disclose, request, or challenge underlying material through
logged Room messages. Neither is omniscient. Once disclosed, information enters
the recipient's persistent seat memory for the remainder of the setup.

The final decision record must show separately:

1. The Prime Minister's intended national end state and concurrence.
2. The President's command assessment and confirmation.
3. Defense, General Staff, Himaldesh Strategic Command, and other required
   professional confirmations.
4. Any material dissent, missing information, or unresolved condition.
5. The formal action accepted or the reason no state change occurred.

### Rejected alternatives

- **Prime Minister-led Room with a strategic-only presidential gate:** Rejected
  because it would make the President's published Supreme Commander role mostly
  ceremonial for conventional crisis decisions.
- **President-led National Command Authority for every cycle:** Rejected because
  it would subordinate the Prime Minister despite DATE assigning that office
  overall national-security responsibility through the ministries.
- **One generic executive agent:** Rejected because it would erase the most
  important political feature distinguishing Himaldesh from the U.S. and
  Olvana Rooms.

### Microsite consequence

The Himaldesh view should place the Prime Minister and President on separate
tracks. A visitor should see which office received which brief, which action
class activated the President's command role, whether the two executives
concurred, how disagreement changed the package, and whether delay carried a
World cost. The presentation should label dual confirmation as our
public-source design inference while showing the DATE facts that motivated it.

## Next Himaldesh design decision: group topology

The split dyad now needs an operational group graph. The next choice is whether
Cabinet-policy and command advice develop concurrently in separate groups and
meet only for cross-portfolio action, remain together in one co-chaired forum,
or proceed sequentially from a Prime Minister-led Cabinet to a
President-commanded military review.

## Continued Himaldesh Room decision: parallel Cabinet and Command cells

### 28. Cabinet-policy and military-command advice develop in parallel

**Owner selection:** Option 1 is locked. Himaldesh has a Prime Minister-led
Cabinet Policy Cell and a President-led Command Cell. They may develop their
initial products concurrently. The Minister of Defense carries the military
product across the boundary, and the two executives meet only when the action
class requires both offices under decision 27.

This section resolves and supersedes the immediately preceding open decision.
It specifies the group topology, not the final Himaldesh seat roster.

### Public-source basis and inference boundary

DATE supplies the institutional separation that motivates this topology: the
Prime Minister is responsible for overall national security through the
ministries; the President is Supreme Commander; the Ministry of Defense
manages and coordinates the armed forces; and the Ministry of Defense and
General Staff form the Supreme High Command. DATE also places the Interior
forces under Interior for administration and under Defense for operational
control when necessary.

Source rechecked on 2026-08-24:

- DATE Military: Himaldesh:
  https://odin.t2com.army.mil/DATE/2522b29e0fefb26f4164330c2311eb46

DATE does not describe two machine-operated crisis cells, their scheduling, or
their information exchange. The exact graph below is a WOPR design inference.
It must be presented as our operationalization of DATE's published political
structure, not as an official Himaldeshi meeting procedure.

### Cabinet Policy Cell

**Convening principal:** Prime Minister.

**Purpose:** Develop the civilian national-security end state and the package
of diplomatic, economic, informational, domestic-security, infrastructure,
humanitarian, and partner measures that could serve it.

**Membership rule:** The Prime Minister and every active civilian portfolio
owner whose mandate is affected by the current inject or proposed action. DATE
explicitly supports Interior, Finance, and Information functions; other
ministry or functional seats require their own source and trigger entries in
the final roster rather than being invented by the setup.

**Boundary:** The cell may request military assessments and propose the
political purpose, constraints, or sequencing of military options. It cannot
issue military orders, treat feasibility as established without the Command
Cell, or turn Prime Ministerial preference into presidential confirmation.

### Command Cell

**Convening principal:** President as Supreme Commander.

**Purpose:** Develop military warning, readiness, posture, force-protection,
mobilization, support, and employment advice against the civilian end state;
identify operational feasibility, command integrity, resource dependencies,
and escalation risk; and state which professional confirmations an action
would require.

**Membership rule:** The President, Minister of Defense, and General Staff are
the persistent command core. Himaldesh Strategic Command, an operational
commander, Interior, the Roads Group, space or cyber functions, or another
source-grounded command element activates only when a Charter predicate makes
its mandate relevant. Exact trigger and roster choices remain open.

**Boundary:** The cell may develop and narrow military options. It cannot set
the country's diplomatic, economic, informational, or domestic policy; invent
an emergency delegation; or change the World before the required political
and professional confirmations exist.

### The Minister of Defense is one bridge agent, not two copies

The Minister of Defense works inside the Command Cell and later carries its
structured product into the cross-cell integration step or Joint Executive
Session. The Cabinet Policy Cell may send logged questions or constraints to
Defense, but its initial parallel work does not contain a second simultaneous
copy of that seat.

This preserves one persistent mandate, memory, and disclosure history for the
minister. If a cycle needs the same minister or another shared specialist in
both cells, the scheduler serializes those calls. It never clone-runs a seat
with divergent private state merely to save wall-clock time.

### One outer cycle, two bounded work lanes

1. **Freeze the cycle input.** The deterministic World and Watch functions
   deliver the same common operating picture, setup-defined private briefs,
   and current event time before either cell begins.
2. **Run independent cell work.** The two cells may run concurrently only when
   neither depends on the other's current product and their active agent sets
   do not overlap. Each cell retains its own private discussion and produces a
   structured cell product.
3. **Publish bounded products.** Each product states its intended end state or
   mission, assumptions, cited evidence, options, constraints, risks, material
   dissent, missing information, proposed action classes, and requested
   confirmations. A transcript is not itself a state-changing action.
4. **Resolve the boundary.** The deterministic controller routes logged
   questions and checks declared action classes and dependencies. The Minister
   of Defense presents the Command Cell's product; no hidden third integrator
   silently rewrites either cell's advice.
5. **Convene only when required.** A Joint Executive Session occurs when a
   proposed package falls into an action class that decision 27 assigns to
   both the Prime Minister and President. If deterministic routing cannot
   exclude that class, the package is treated as requiring both until it is
   narrowed; the agents cannot self-exempt it. Cabinet-only measures do not
   require a ceremonial all-hands meeting.
6. **Submit one formal package.** The existing action-class routing records the
   two executive positions and every required professional confirmation. The
   constrained interpreter validates the package, and only the World owns its
   consequences.

The Joint Executive Session is not a standing co-chaired council and does not
take a generic majority vote. Its participants are the Prime Minister,
President, Minister of Defense, and the active portfolio or command owners
whose confirmation the package requires. They may revise, narrow, sequence, or
abandon a package. Silence remains nonconcurrence.

### Concurrency and causal-order contract

Parallel execution is an implementation schedule for independent work, not a
different decision procedure. A concurrent and a serial execution of the same
logical cell graph must expose the same inputs, dependencies, persistent seat
memories, and canonical transcript order. The scheduler may run two cell jobs
at once only when all of the following are true:

- The cycle inputs have been frozen and versioned.
- The active agent sets are disjoint.
- Neither job consumes the other's current-cycle product.
- Each job writes to an isolated trace before deterministic collection.
- The canonical merge order is fixed by the Charter rather than completion
  timing.

If Interior must advise both on domestic cohesion and on transfer of its forces
to Defense control, for example, the dependency graph captures Interior's
position once and orders later consumers around it. A race cannot decide which
cell sees the seat's earlier or later memory.

### Information and selective disclosure

Both cells see the declared common picture, but raw private briefs and private
discussion remain within the receiving seats and cell. The cell product crosses
the boundary. Underlying material crosses only through a logged request or
disclosure, after which it enters the recipient's persistent memory. The
Defense bridge does not make the Prime Minister omniscient about command data
or the President omniscient about every ministry's private assessment.

The retained artifact must show which evidence each cell possessed when it
formed its product, which material was later disclosed, and whether an apparent
disagreement came from different objectives, different facts, or different
professional judgments.

### Failure, delay, and nonconcurrence

A missing or invalid cell product cannot be replaced by a fabricated summary.
An action may proceed only if every product and confirmation required for its
action class is valid. An unrelated Cabinet-only action may still proceed when
the failed Command Cell is not a declared dependency, but a military or
cross-portfolio action fails closed. The World may still advance time and apply
setup-authored consequences of delay.

If the two valid products conflict, the system records the conflict and routes
it to the required principals. It does not calculate chair weights, average
the advice, or conceal the disagreement inside one synthetic consensus.

### Why this topology was selected

The two lanes make DATE's divided political structure operational. The Prime
Minister can integrate the ministries while the President and command
institutions test military feasibility at the same crisis time. A later joint
session then exposes how the country's civilian end state and military limits
change one another instead of pretending that all advice appeared in one
undifferentiated conversation.

The topology also gives the entry a concrete Situation Room story. It shows
who learned what, which groups could work at the same time, where an
institutional dependency forced them to wait, who carried advice across the
boundary, and what survived into state action. That is more informative than
scoring a final response without its institutional path.

### Rejected alternatives and invalid variants

- **One standing co-chaired forum:** Rejected because it would flatten the
  Prime Minister's Cabinet responsibility and the President's command role into
  one generic meeting, expose all advice to both offices by default, and make
  the two-executive design mostly cosmetic.
- **Sequential Cabinet-to-command review:** Rejected because it would turn the
  Command Cell into a late feasibility check after civilian policy had already
  converged. It would suppress early command alternatives and make avoidable
  serialization part of every cycle.
- **Clone the Defense Minister into both parallel cells:** Invalid because two
  simultaneous copies could accumulate different memories or make conflicting
  commitments under one office identity. Safe concurrency stops at shared
  agents and dependencies.

### Microsite consequence

The Himaldesh view should use two synchronized lanes. It should display the
frozen cycle input, active seats, concurrent spans, shared-agent barriers,
cell-local evidence, each structured product, the Minister of Defense's bridge,
the trigger for any Joint Executive Session, both executive positions, the
formal package, and the resulting World event. The visitor should also be able
to inspect the rejected topology choices and the public DATE facts that led us
to this design.

## Next Himaldesh design decision: persistent roster and activation

The topology names groups but intentionally does not force all 18 ministries
or every military component into every setup. The next choice is how many
source-grounded seats exist in the stable Charter registry and which of them
activate at ordinary crisis intake versus only after a setup or action trigger.

## Continued Himaldesh Room decision: source-grounded registry with triggers

### 29. The Charter registry is complete, but the active Room is relevant

**Owner selection:** Option 1 is locked. Himaldesh receives a stable registry
containing every separate judgment-bearing seat that the public DATE material
can support. The Prime Minister, President, Minister of Defense, and General
Staff are structural participants. Each Crisis Setup activates the civilian
portfolio seats relevant to its initial conditions. Later injects, proposed
actions, or validated consultation requests may activate additional civilian
or command specialists. Once activated, a seat persists for the rest of that
setup.

The owner's immediately preceding `2` selection was interrupted before any
design work began and was superseded by the final explicit `1`. The fixed
always-active roster was therefore not locked and remains a rejected
alternative below.

This section resolves and supersedes the immediately preceding open decision.
It fixes the registry and activation policy, not the final list of civilian and
command seats.

### Public-source basis and inference boundary

DATE states that the Prime Minister exercises overall national-security
responsibility through 18 ministries, but it does not provide a machine-ready
list of 18 crisis mandates. It separately describes the President, Ministry of
Defense, General Staff, Interior forces, Himaldesh Strategic Command, Roads
Group, regional commands, information functions, finance functions, and space,
cyber, and intelligence relationships. Those facts support a registry broader
than four seats without supporting 18 generic agents.

Sources rechecked on 2026-08-24:

- DATE Military: Himaldesh:
  https://odin.t2com.army.mil/DATE/2522b29e0fefb26f4164330c2311eb46
- DATE Information: Himaldesh:
  https://odin.t2com.army.mil/DATE/33cfd982e59b2474287b621103d25fee

DATE does not define a runtime activation system. The eligibility tests,
predicates, persistence rule, and matched-run treatment below are WOPR design
inferences and must be labeled that way.

### Registry eligibility

A DATE institution or function receives a distinct seat only when all of the
following are true:

1. Public DATE material supplies a persistent institutional responsibility or
   professional function relevant to at least one allowed Crisis Setup.
2. The seat must exercise judgment, not merely deliver a deterministic fact,
   validate syntax, schedule a meeting, or apply a World consequence.
3. Collapsing it into another seat would hide a plausible source-grounded
   disagreement, information boundary, professional confirmation, or action
   constraint.
4. The Charter can state its mandate, synthetic information entitlement,
   group memberships, supported contributions, prohibited actions, and
   activation predicates without inventing an office biography.
5. Its function is not already represented by the same persistent agent under
   another label.

This rule sets no target number. A seat earns its place through the political
and institutional structure of the DATE actor. Administrative support staff,
Watch delivery, scheduling, schema validation, interpreter checks, and World
adjudication remain deterministic functions unless a later source-backed
design decision gives one of them independent judgment.

### Structural participants

Four seats exist from the first crisis inject in every Himaldesh setup:

- The Prime Minister, because every setup needs a civilian national-security
  end state and Cabinet integration.
- The President, because the selected Room always preserves the separate
  Supreme Commander and executive information lane.
- The Minister of Defense, because that seat connects political purpose to the
  defense establishment and bridges the two selected cells.
- The General Staff, because military feasibility, warning, readiness, and the
  professional range of conventional advice cannot be inferred by Defense or
  the President alone.

Structural participation does not mean that every seat speaks in every group
round. The Charter still routes a seat only into groups and decisions for which
its mandate is relevant. The seat remains instantiated, receives information
according to its entitlement, and preserves one continuous memory.

### Every registered seat has a complete activation record

Before a Charter version is frozen, each non-structural seat must declare:

- A stable actor-qualified identifier and source-backed human-facing label.
- The source URL, retrieval date, source version or last-modified date, and the
  precise fact that supports the seat.
- Its professional mandate, information entitlement, group memberships,
  supported contributions, prohibited actions, and required confirmations.
- Enumerated setup, event, action, and consultation predicates.
- Whether its activation creates a dependency on another seat or prevents two
  cells from running concurrently.

Adding a new seat after freeze requires a new Charter and manifest identity. A
Crisis Setup may select and brief registered seats, but it cannot invent a new
minister, command, committee, or expert at runtime.

### Activation lifecycle

1. **Freeze the registry.** The Room Charter and manifest bind the complete
   eligible seat list and every predicate before a run begins.
2. **Instantiate the structural core.** The four structural seats enter at the
   first inject with only their declared common and private information.
3. **Apply setup triggers.** Authored issue tags activate every relevant
   civilian and specialist seat before initial cell work. For one matched
   setup-seed, this initial active roster is identical across evaluated runs of
   that Himaldesh Charter.
4. **Apply endogenous triggers.** A later World inject or a validated candidate
   action type may activate another registered seat. A model may request a
   consultation, but the deterministic controller activates the requested seat
   only when a Charter predicate is satisfied.
5. **Keep activation sticky.** Once active, the seat retains its mandate,
   disclosures, questions, commitments, and memory through the setup. A later
   drop in issue relevance may suppress an unnecessary call but cannot erase
   the seat or its record.

Predicates operate on setup tags, typed World events, and constrained candidate
action classes. They do not use a free-form model judgment that a friendly
voice would be useful. If an action's class is ambiguous, every potentially
required seat activates conservatively until the package is narrowed.

### Initial and endogenous activation are different evidence

Initial activation is exogenous. It follows the authored Crisis Setup and must
match across every run sharing the setup and seed. Endogenous activation may
diverge because different runs request different consultations or propose
different action classes. That divergence is part of the observed
decision-making path, not a setup difference.

The retained trace must therefore label every activation with its source:

- `structural`
- `setup_trigger`
- `world_event_trigger`
- `candidate_action_trigger`
- `validated_consultation_request`

The record also binds the triggering event or action, predicate ID, activation
time, first information received, and any dependency it introduced. Model and
procedure comparisons can then distinguish a Room that faced different facts
from one that brought a new institution into the crisis because of its own
policy choice.

### Absence, confirmation, and fail-closed behavior

A registered but inactive seat contributes no advice, opposition, concurrence,
or implied support. If a candidate action requires that seat's professional
review, the controller activates and consults it before the package can alter
the World. Missing activation, an invalid seat product, or missing confirmation
causes that action to fail closed; it is not repaired by the Prime Minister,
President, Defense, a majority, or a default.

If no registered seat covers a required function, the controller records a
`CHARTER_GAP`. It does not invent an expert. An unrelated action with a complete
path may continue, while the uncovered action remains invalid and setup time
may advance.

### Concurrency and cost consequence

Triggered activation reduces irrelevant model calls, but cost is not the
reason a political institution exists or disappears. The dependency graph is
recomputed after every activation. Independent groups may still run in
parallel; a newly shared seat or product dependency introduces an explicit
serialization barrier under decision 28.

Activation order never follows wall-clock completion order. The Charter fixes
the canonical order for simultaneous triggers, and traces are collected in
that order after isolated work completes.

### Rejected alternatives and invalid variants

- **Fixed always-active core:** Rejected because the same eight or ten voices
  would appear even when their mandates were irrelevant. Strategic Command in
  every setup would also make nuclear institutions present before a strategic
  issue existed.
- **All 18 ministries as agents:** Rejected because DATE states the count but
  does not supply enough distinct crisis mandates to prevent generic invented
  personas and duplicated responsibilities.
- **Setup-authored free roster:** Invalid because it would let each scenario
  rewrite the country's institutions, weaken matched comparisons, and make a
  setup author rather than the Charter decide who exists.
- **Model-invented expert or committee:** Invalid because a policy model could
  create a favorable adviser or missing confirmation path in response to the
  decision it wants to take.

### Microsite consequence

The Himaldesh presentation should distinguish the complete Charter registry
from the smaller active Room. Every seat should have a source card and trigger
card. During a replay, a visitor should see who was present at the first
inject, who joined later, the exact exogenous or endogenous trigger, what new
information and dependency entered with that seat, and which registered seats
remained absent.

This makes institutional expansion part of the story. Two matched runs of the
Himaldesh Room may begin with the same people and facts, then diverge because
one requests an economic consultation while another proposes a strategic
action that activates Himaldesh Strategic Command. The microsite can show that
causal path without mistaking a larger transcript for a better outcome.

## Next Himaldesh design decision: Cabinet portfolio boundaries

The activation rule is fixed, but the non-defense Cabinet registry is not. The
next choice is whether external affairs, internal and border security, finance
and economic resilience, information and communications, and civil
infrastructure or humanitarian resilience become separate triggerable agents,
or whether some of those functions are combined under broader Cabinet seats.

## Corrected Himaldesh Cabinet decision: six portfolios after feasibility audit

### 30. Six distinct Cabinet portfolios exist in the triggered registry

The owner's controlling instruction was:

> Use 1 , but you must make sure this is feasible and doable with concordia or
> our harness. otherwise you should fall back to option 2

This supersedes the stray `2` received during the interrupted exchange. That
message was not an instruction to replace decision 29's triggered registry,
and it was not an intentional selection of the five-portfolio fallback. The
correction selects option 1 conditionally, requires a technical feasibility
check, and pre-authorizes option 2 only if the six-portfolio design cannot be
implemented through Concordia or the contest harness.

The feasibility condition is satisfied at the reusable Concordia seam. The
Himaldesh Charter therefore registers these six separate, issue-triggered
Cabinet Policy Cell portfolios:

1. **External Affairs** develops diplomatic engagement, deconfliction,
   international-law, coalition, treaty, and external-assurance components.
2. **Interior and Border Security** develops domestic-security, border-control,
   law-enforcement, internal-order, and civilian-use-of-force components.
3. **Finance and Economic Resilience** develops fiscal, financial, trade,
   sanctions, resource, market-stability, and economic-continuity components.
4. **Information and Communications** develops telecommunications, spectrum,
   data-policy, public-information, censorship-risk, and civilian-communications
   components.
5. **Civil Infrastructure and Continuity** develops energy, transport, water,
   sanitation, logistics, repair, physical-system dependency, and continuity
   components.
6. **Humanitarian and Social Cohesion** develops civilian-protection,
   displacement, shelter, health, access, relief-distribution, community-trust,
   dignity, and distributional-impact components.

These are six persistent seat definitions, not six agents called in every
setup. Decision 29 still controls activation. A setup or typed event may
activate one, several, or none of these portfolios, and a candidate policy may
activate a missing professional review before it can alter the World.

### Why infrastructure and humanitarian resilience remain separate

The fifth and sixth portfolios inspect different failure mechanisms. Civil
Infrastructure and Continuity asks whether physical systems can operate,
interoperate, be repaired, and sustain essential services. Humanitarian and
Social Cohesion asks who is harmed, displaced, excluded, left without access,
or subjected to coercive measures while those systems and security policies
operate.

Those advisers may reasonably disagree on the same candidate package. Keeping
a transport corridor, power node, or communications link operating can support
national continuity while increasing civilian exposure or delaying an
evacuation. Closing or repurposing it can reduce immediate harm while breaking
food, energy, medical, or repair logistics. Combining the two functions would
often hide that conflict inside one generated answer. Separate seats expose
the tradeoff, the information each office used, and whether the final package
resolved or ignored their nonconcurrence.

Neither portfolio receives general executive power. They develop bounded
components and professional reviews. They cannot command security forces,
spend funds, control diplomacy, publish an unreviewed national message, or
apply consequences directly to the World. Cross-portfolio effects create
dependencies on the relevant seats and confirmations; they do not expand one
portfolio's mandate.

### Public-source basis and design-inference boundary

DATE describes a Prime Minister exercising national-security responsibility
through 18 ministries. It separately describes military, interior, finance,
information, communications, infrastructure, continuity, refugee, civilian,
and international relationships that make these functions relevant to crisis
policy. The official Himaldesh pages used for this boundary are:

- Political:
  https://odin.t2com.army.mil/DATE/7fd47dccb6adaefd2bca2af23b7dce4b
- Military:
  https://odin.t2com.army.mil/DATE/2522b29e0fefb26f4164330c2311eb46
- Economic:
  https://odin.t2com.army.mil/DATE/87722b707cc72e4fe5cbc007e0c6e3e6
- Information:
  https://odin.t2com.army.mil/DATE/33cfd982e59b2474287b621103d25fee
- Infrastructure:
  https://odin.t2com.army.mil/DATE/b05e38c401b7f643651825768d85f983

DATE does not publish this exact six-seat Cabinet graph or these exact
human-facing labels. The functional split, labels, mandate boundaries,
activation predicates, and required products are WOPR design inferences. Every
seat therefore needs a source card that separates quoted or paraphrased DATE
facts from the design choices built on them. The Room must not present this
registry as the official organization chart of a real government or as a
verbatim DATE Cabinet roster.

### Feasibility audit

The existing Nuclear War harness contains two hard limits that cannot represent
this Room unchanged:

- `nuclear_war_concordia.config_validation.validate_config` requires exactly
  four top-level game players.
- The legacy authority config and C2 artifact validators require exactly three
  authority members and exactly three member traces per deliberation.

Those constraints describe the inherited four-player Nuclear War game and its
three-member faction mechanism. They are evidence about what must not be
reused as the new Room schema. Reducing six Cabinet functions to five would not
remove this mismatch because five is also incompatible with the three-member
artifact. Both portfolio options require the same new Situation Room adapter
and trace contract.

The lower layers needed by that adapter do not impose a three-agent limit:

- `NativeConcordiaEntityClient` wraps one Concordia entity and exposes a
  generic completion call.
- The Concordia 2.4 entity factory creates an independent entity, identity,
  observation pipeline, `ListMemory`, and entity log for every constructed
  seat.
- Existing member factories accept an ordered sequence of members before the
  legacy artifact layer applies its three-member constraint.
- `PressCoordinator` accepts an arbitrary ordered speaker list. Its successful
  six-speaker probe is evidence that the ordered-client coordination seam is
  not count-limited, not a decision to use public press semantics for private
  Cabinet deliberation.
- The contest runner already executes independent cells with a thread pool,
  and study-wide cost reservations use a lock. A parallel Room must give each
  concurrently called seat or group its own mutable call-budget instance while
  sharing only the locked study-cost accumulator.

The bounded offline audit produced these receipts on 2026-08-24:

- `gdm-concordia` version `2.4.0` was installed.
- Forty-three focused native-entity, member-runtime, coordinator, prefab-parity,
  and contest-budget tests passed.
- Six distinct native Concordia entities completed two calls each through a
  six-worker thread pool. The probe observed six distinct entity objects, six
  distinct memory objects, six distinct final log objects, 12 completed legal
  choices, and no cross-seat alias.
- An ordered coordinator accepted six distinct speaker identifiers and
  returned all six in the declared canonical order.

These checks verify engineering feasibility at the reusable seam. They do not
verify an end-to-end DATE Room, policy-product schema, triggered group cycle,
action interpretation, World consequence, or model quality because those
components have not been built. No external model call was needed for this
count and isolation audit.

### Required adapter and acceptance gate

Implementation must add a narrow Situation Room orchestration and trace layer
instead of generalizing the old C2 vote artifact into an institution it was not
designed to represent. The first offline tracer bullet must demonstrate all of
the following before the six-portfolio decision is treated as executable:

1. Construct all six portfolio seats from one frozen Charter registry while
   retaining a distinct identity, private memory, disclosure record, and trace
   sink for each seat.
2. Activate a setup-selected subset without constructing a new runtime persona
   or treating inactive seats as concurring.
3. Give every active seat the same frozen common picture plus only the
   additional information later authorized by the Charter, then collect
   isolated products before any merge.
4. Run independent seats or disjoint groups concurrently while serializing the
   single persistent Defense bridge and any other shared dependency fixed by
   decision 28.
5. Merge completed products in Charter order rather than wall-clock completion
   order, preserving dissent, conditions, questions, and missing products.
6. Account for every logical call, provider attempt, token bound, and cost
   reservation without sharing one mutable active-channel counter across
   concurrent workers.
7. Fail closed on an invalid product, missing required review, memory or trace
   alias, activation error, or dependency on the legacy three-member schema.

The current native-seat press restriction is not a blocker because press is not
the internal Cabinet process. The Room adapter owns private deliberation and
selective disclosure. Any later public statement remains a separate,
explicitly authorized World-facing product.

### Authorized fallback

Option 2 remains a pre-authorized technical fallback: combine Civil
Infrastructure and Continuity with Humanitarian and Social Cohesion into one
**Civil Resilience** portfolio, leaving five triggerable Cabinet portfolios.
Use that fallback without reopening this boundary decision only if the first
offline tracer bullet exposes an intrinsic Concordia or harness count,
isolation, memory, trace, or deterministic-coordination limitation that makes
six persistent portfolio seats infeasible within the contest schedule.

Do not invoke the fallback merely because the inherited C2 schema has three
members; that schema is already excluded and five seats would not fit it
either. Do not invoke it merely because a six-seat setup makes one additional
model call; the triggered registry already suppresses irrelevant calls, and
cost must be measured against the fixed study budget. Prompt quality, mandate
overlap, or excessive latency discovered in the actual tracer bullet should be
reported with receipts before deciding whether they demonstrate infeasibility
or a repairable adapter problem.

### Microsite consequence

The microsite should show this as a design decision with an evidence trail, not
as an unexplained six-agent diagram. It should place the three-member inherited
C2 mechanism beside the six-seat Room requirement, show why the former is not
the institution, and expose the bounded feasibility receipts that justified
using option 1. It should also show the conditional fallback and whether the
tracer bullet passed, so the final presentation distinguishes an approved
design, a verified reusable seam, and a completed end-to-end run.

The infrastructure-versus-humanitarian split is also a useful replay lens. A
visitor should be able to inspect where the two portfolios agreed, where they
identified different affected systems or populations, which conditions were
carried into the policy package, and what the World later did with those
consequences.

## Next Himaldesh design decision: portfolio information boundaries

The six portfolio functions are now distinct and triggerable, but their
information relationship is not fixed. The next choice is whether each
portfolio receives a separate private brief alongside one shared common civil
picture, whether all portfolios receive the same brief and differ only by
mandate, or whether selected portfolios receive asymmetric access justified by
the setup and Charter.

## Himaldesh portfolio information decision: common picture plus private briefs

### 31. Every active portfolio receives shared crisis facts and its own brief

The owner selected option 1. Each active Himaldesh portfolio begins a bounded
work phase with two distinct World-owned inputs:

1. A **Common Crisis Picture** contains the shared facts, reports,
   uncertainties, timestamps, and prior public or disclosed developments that
   every active Himaldesh seat is entitled to know at that phase.
2. A **Portfolio Brief** contains only the synthetic facts, assessments,
   constraints, uncertainties, and questions assigned to that portfolio by the
   frozen Crisis Setup and its Charter entitlement.

The selected phrase `common civil picture` is broadened to `Common Crisis
Picture` in the artifact vocabulary because the shared input may include
diplomatic, economic, military, infrastructure, information, and humanitarian
facts. The broader label does not make the picture omniscient or fully true. It
is the common information actually available to the actor Room at that time.

This decision extends the information boundaries already fixed for the Prime
Minister, President, Cabinet Policy Cell, and Command Cell. It does not replace
their separate executive and command briefs, and it does not make either
executive omniscient.

### World ownership and setup authoring

The deterministic World owns both input types. A policy agent cannot invent,
rewrite, suppress, or reassign a brief fact before deliberation. The Charter
defines the categories a seat may receive; each Crisis Setup instantiates the
actual synthetic content, availability time, and uncertainty for that setup.

Every brief fact must bind at least:

- a stable fact identifier and actor identifier;
- its recipient seat identifier;
- its first availability time and source class;
- its content and stated uncertainty or confidence boundary; and
- the Crisis Setup and seed that produced or selected it.

The exact artifact field names remain an implementation-design task, but these
semantic bindings are required. They let the trace distinguish a fact the
World supplied from an assertion an adviser generated.

A portfolio brief may be empty when a seat is active for its mandate but has no
exclusive information at that phase. The empty brief is still an explicit
artifact. Its absence cannot be confused with a failed load, an inactive seat,
or information withheld by the World.

### Matched evaluation contract

Every evaluated run sharing an actor Charter, Crisis Setup, and seed receives
the same Common Crisis Picture versions, the same per-portfolio brief facts,
and the same availability times. Model, procedure, aggregation, or disclosure
conditions may change what the Room does with those inputs, but they cannot
silently change the exogenous information assignment.

The run manifest must bind content hashes for each Common Crisis Picture and
Portfolio Brief. Every seat trace then references the exact versions delivered
before its call. This lets analysis separate three causes of disagreement:

- different mandates applied to common facts;
- different private facts available to different seats; and
- different interpretations of the same available material.

### Activation and late entry

An initially active portfolio receives the phase's Common Crisis Picture and
its own currently available Portfolio Brief before its first call. A portfolio
activated later receives the current common picture plus every fact in its own
brief whose availability time has already passed. It does not receive another
seat's raw brief or private discussion merely because it joined late.

Late activation cannot rewrite history. The trace records which relevant facts
existed before activation, which were delivered on entry, and what the new seat
could not have influenced earlier. The seat's subsequent inputs, disclosures,
questions, products, and memory remain sticky under decision 29.

An inactive seat's private brief remains with the World. It contributes no
implicit advice or concurrence, and its undisclosed facts do not enter another
agent's context through a default summary.

### Isolation and disclosure boundary

The Room adapter must construct a separate scene input for every active seat.
Each input may repeat the exact common picture, but it includes only that
seat's authorized private brief and previously received disclosures. The
adapter must not build one union prompt and ask agents to ignore sections that
are not theirs.

Private information can later cross a boundary only through the logged request
and disclosure mechanisms already required by decisions 27 and 28. Once
received, it enters the recipient's persistent memory. This decision does not
yet determine whether the Prime Minister receives raw portfolio briefs at
intake, receives only structured portfolio products by default, or can compel
underlying disclosure. That is the next design choice.

The Common Crisis Picture may incorporate a formerly private fact only after a
recorded disclosure or a later World event independently makes it common. The
next picture version must identify that transition instead of silently copying
the fact into every prompt.

### Bounded feasibility receipt

An offline Concordia 2.4 probe constructed six independent portfolio entities
and called them through six parallel workers. Every seat received one identical
synthetic common token and one unique synthetic private token. The corrected
probe found:

- the common token in all six persistent memories;
- each private token only in its assigned seat's memory and final entity log;
- zero foreign private tokens across the other five memories or logs; and
- all six legal responses completed.

The first probe failed because `get_all_memories_as_text()` returned a tuple of
complete memory records while the assertion treated it as one string. Joining
the returned records and rerunning the same isolation assertions passed. The
failure was a probe-shape error, not evidence of information leakage.

This receipt verifies that the reusable entity seam can deliver and retain
separate inputs. It does not verify the unbuilt brief schema, late-activation
loader, disclosure policy, redaction behavior, end-to-end Room trace, or model
compliance with a mandate.

### Rejected alternatives and invalid variants

- **One identical full brief for every portfolio:** Rejected because it would
  isolate mandate effects but remove the institutional information boundaries
  that earlier decisions require the Room to expose.
- **Ad hoc setup recipients without Charter entitlements:** Rejected because a
  setup author could change who has access without changing the actor Charter,
  confounding matched comparison and weakening the source card.
- **Union prompt with textual access warnings:** Invalid because the model has
  already received every supposedly private fact, even if instructed not to
  use it.
- **Runtime-generated private facts:** Invalid because an adviser or summarizer
  could manufacture the evidence used to justify its own policy.
- **Silent promotion into the common picture:** Invalid because analysis could
  not tell whether another seat disclosed the fact, the World independently
  revealed it, or the adapter leaked it.

### Microsite consequence

The microsite should let a visitor switch between the Common Crisis Picture
and each active seat's information view at any phase. A replay should show
which facts were common, which were portfolio-private, when a late seat received
its backlog, and when a fact crossed into another memory or became common.

This view should default to fact identifiers and source cards, with sensitive
synthetic content revealed only where the presentation permits it. It gives the
entry a concrete account of why advisers disagreed without treating every
disagreement as personality or model noise.

## Next Himaldesh design decision: Prime Minister access to portfolio briefs

The Prime Minister's Charter mandate requires Cabinet integration and entitles
the office to diplomatic, economic, internal-security, information,
infrastructure, and civilian-impact briefing. The remaining choice is whether
that means raw portfolio briefs arrive at the Prime Minister simultaneously,
whether the Prime Minister initially sees structured portfolio products and
requests underlying material when needed, or whether disclosure remains wholly
at each portfolio's discretion.

## Himaldesh Prime Minister information decision: product first, facts on request

### 32. The Prime Minister integrates structured products, not unioned raw briefs

The owner selected option 1. Each active portfolio first produces a structured
Portfolio Product from the Common Crisis Picture, its private Portfolio Brief,
its mandate, and any information previously disclosed to it. The Prime
Minister receives those products for Cabinet integration. The Prime Minister
does not receive every raw portfolio brief at intake.

The Prime Minister may issue a logged request for cited underlying facts, a
named brief section, or a complete underlying brief. The deterministic
controller grants the authorized scope unless a Charter rule marks the material
compartmented or otherwise outside the office's entitlement. The portfolio
agent does not silently decide whether an authorized request succeeds, and the
Prime Minister cannot override a deterministic compartment rule through prose.

This implements the executive entitlement fixed in decision 27: the Prime
Minister receives Cabinet briefing sufficient to integrate national policy and
can request underlying material through the Room, but is not automatically
given hidden World truth or every raw specialist input.

### Required Portfolio Product

Every active portfolio must return one schema-valid product before an action
that depends on its mandate can advance. The product contains five grouped
parts:

1. **Position:** The portfolio's mandate-relevant assessment, recommended
   contribution, supported alternatives, and actions it opposes.
2. **Basis:** Assumptions and immutable fact references, labeled as common,
   private, or previously disclosed without copying raw private content into
   the Cabinet-facing product by default.
3. **Uncertainty:** Material uncertainty, missing information, confidence
   limits, and questions that could change the position.
4. **Conditions and blockers:** Required safeguards, dependencies,
   professional constraints, hard objections, and the action classes they
   affect.
5. **Coordination record:** Other seats whose review is required, requested
   confirmations, disclosure-safe dissent, and whether underlying material is
   available for a Charter-controlled request.

An empty array is valid when a category has no items; a missing category is
invalid. The schema forces a seat to answer each question but cannot guarantee
that a model identifies every real risk or reports every relevant fact. Where
a Crisis Setup contains an authored mandatory-risk or mandatory-dependency
annotation, evaluation can detect an omission. Otherwise completeness remains
an observed model behavior rather than a property the validator can infer.

The product is advice and evidence, not a state-changing action. It cannot
command another seat, spend resources, send a public message, or apply a World
consequence.

### Logged underlying-material request

A Prime Minister request must identify the source portfolio, the product or
brief reference, the requested fact identifiers or scope, and the policy
question that requires the material. The request itself changes no World
state. The controller resolves it against the frozen Charter and setup using a
small closed outcome set such as:

- `granted`
- `denied_compartmented`
- `denied_outside_entitlement`
- `invalid_scope`
- `unavailable`

When granted, the World delivers the immutable underlying fact or brief bytes
directly to the Prime Minister. It does not ask the source portfolio to rewrite
the evidence. The delivery record binds the request, access decision, delivered
fact identifiers and content hash, delivery time, and receiving memory. The
source portfolio is notified in its disclosure history, but it cannot alter the
granted material.

A clarification question is different from an underlying-material request. It
asks the portfolio for new professional judgment and therefore requires another
portfolio call, a new trace, and a dependency barrier. Retrieval of already
authored World facts does not require a model call.

### Blockers, denials, and fail-closed behavior

A portfolio cannot make a material objection disappear by omitting the raw fact
from its Cabinet-facing prose. Its product must carry the blocker category,
affected action class, asserted consequence, required condition, and supporting
fact references. The raw fact may remain private until requested.

If the Prime Minister proceeds after a declared blocker, the integrated package
must state how the blocker was accepted, mitigated, narrowed, sequenced, or left
unresolved. Any professional confirmation required by the action class remains
separate. A Prime Minister summary cannot convert opposition or silence into
concurrence.

A denied raw-material request does not automatically halt every Cabinet action.
The Prime Minister may rely on a valid professional product, seek a narrower
authorized scope, revise the package, or abandon it. An action fails closed when
its Charter path requires the unavailable material or confirmation, when the
package cites raw evidence that was never delivered to an entitled decision
maker, or when a required Portfolio Product is missing or invalid. Unrelated
actions with complete paths may continue.

### Causal order and matched evaluation

Portfolio Products are collected in Charter order after isolated portfolio work
finishes. The Prime Minister sees the complete set of valid products for that
Cabinet phase before deciding which underlying requests to make. Requests and
disclosures are then resolved in canonical request order, not provider-response
order.

The original Common Crisis Picture and Portfolio Briefs remain identical across
matched setup-seed runs. Requests are endogenous. Different models or Cabinet
procedures may request different facts, and that divergence is an outcome to
measure. The trace must therefore distinguish exogenous information assignment
from information that entered the Prime Minister's memory because of a policy
question the Room chose to ask.

### Bounded feasibility receipt

An offline Concordia 2.4 probe constructed persistent Prime Minister, Finance,
and Interior entities. The initial parallel call delivered the common picture
to all three, a Finance raw fact only to Finance, and an Interior raw fact only
to Interior. Before any request, neither raw fact appeared in the Prime
Minister's memory.

The probe then delivered a controller-granted Finance disclosure linked to a
synthetic request. After the next Prime Minister call:

- the requested Finance fact appeared in the Prime Minister's memory and final
  entity log;
- the undisclosed Interior fact remained absent from the Prime Minister;
- the Finance fact remained absent from the Interior peer; and
- Finance retained its original source fact.

This verifies that the reusable entity seam can add one logged disclosure to a
persistent executive memory without broadcasting it to peers. It does not
verify the unbuilt Portfolio Product validator, access-control table, request
resolver, compartment rules, canonical request scheduler, or end-to-end Room.

### Rejected alternatives and invalid variants

- **All raw portfolio briefs sent to the Prime Minister at intake:** Rejected
  because it removes the information boundary and request behavior selected in
  decision 31.
- **Portfolio agent may silently refuse an authorized request:** Rejected
  because access would depend on whether the adviser wants its evidence
  inspected. The Charter and controller decide access.
- **Prime Minister prose overrides a compartment:** Invalid because model text
  cannot change the frozen access contract.
- **Portfolio-generated restatement used as the raw response:** Invalid because
  it would let the source adviser revise the evidence after seeing the policy
  question. A separate clarification may add judgment, but it cannot replace
  the immutable fact.
- **Unlogged prompt enrichment:** Invalid because analysis could not distinguish
  requested disclosure from adapter leakage.

### Microsite consequence

The microsite should show a Cabinet evidence ladder: the Portfolio Product the
Prime Minister initially saw, the exact question that prompted any request, the
controller's access result, the fact identifiers delivered, and the later
integrated package. A visitor should be able to compare the Prime Minister's
memory immediately before and after the request without exposing unrelated
private briefs.

This makes executive curiosity and evidence discipline visible. The evaluation
can show whether a Prime Minister asked for the basis of a recommendation,
acted on a summary without probing it, requested only confirming evidence, or
carried a declared blocker forward without resolving it.

## Next Himaldesh design decision: Cabinet integration sequence

The Prime Minister now receives structured portfolio products and may request
their underlying basis. The remaining choice is how those products become one
Cabinet policy package: a Prime Minister draft followed by targeted portfolio
review, an all-active-portfolio bargaining round before the draft, or a
deterministic secretariat compilation that the Prime Minister edits.

## Himaldesh Cabinet integration decision: Prime Minister draft, targeted review

### 33. The Prime Minister drafts; every affected portfolio reviews

The owner selected option 1. After receiving the active portfolios' structured
products and resolving any underlying-material requests, the Prime Minister
authors an integrated Cabinet Policy Draft. A deterministic Charter router then
identifies every portfolio whose mandate, evidence, resources, constraints, or
declared blockers the draft affects. Those portfolios review the same frozen
draft before it can become the Cabinet's formal policy package.

The Prime Minister leads integration but does not select a friendly review
panel. The portfolio agents remain distinct institutional participants because
they arrive with separate mandates and information, publish attributable
products, inspect the actual integrated draft, and retain any conditions or
opposition in the record. This is not a weighted council, a generic staff
meeting, or a majority vote.

The Cabinet sequence is a WOPR Charter procedure inferred from the Himaldesh
executive and ministry structure. DATE does not publish this exact drafting and
review process, so the microsite and source cards must label it as design rather
than official procedure.

### One Cabinet integration cycle

1. **Collect inputs.** The controller collects all valid Portfolio Products in
   Charter order and resolves the Prime Minister's logged evidence requests
   under decision 32.
2. **Draft once from frozen inputs.** The Prime Minister receives that complete
   bundle and produces one versioned Cabinet Policy Draft. No portfolio edits
   the draft while the Prime Minister call is in flight.
3. **Route review deterministically.** The controller derives the affected
   portfolio set from the draft and Charter. If the draft activates another
   registered seat under decision 29, that seat first receives its authorized
   briefing and produces its own Portfolio Product.
4. **Review in parallel where independent.** Every affected portfolio receives
   the identical frozen draft version plus its own persistent context. Review
   calls may run concurrently because no reviewer consumes another reviewer's
   current output.
5. **Return to the Prime Minister.** The controller collects reviews in Charter
   order. The Prime Minister may accept them, revise the draft, sequence or
   narrow components, or abandon the package. Any material revision is routed
   again before submission.

The process is bounded by a frozen Preset review-cycle and call budget. It
cannot deliberate until agreement. If the cap is exhausted while a required
review or confirmation remains unresolved, that package does not alter the
World and setup time may advance.

### Required Cabinet Policy Draft

The draft binds five groups of information:

1. **Policy intent:** The intended civilian end state, package purpose, and
   criteria for success, reassessment, pause, or termination.
2. **Action components:** Proposed diplomatic, economic, information,
   internal-security, infrastructure, humanitarian, and defense-related
   measures, each with an action class, target, timing, and sequence.
3. **Resources and dependencies:** Required resources, responsible offices,
   cross-portfolio dependencies, prerequisites, and requested professional or
   executive confirmations.
4. **Evidence and uncertainty:** Portfolio Product references, authorized fact
   references, assumptions, uncertainty, missing information, and alternatives
   considered.
5. **Dissent and safeguards:** Every declared blocker or condition inherited
   from the portfolio products, the Prime Minister's proposed treatment of it,
   and package-level safeguards and stop conditions.

The Prime Minister may combine, reject, or modify recommendations but cannot
silently delete their history. Each draft component must identify which source
products it adopts, changes, or declines. A source product remains immutable
even when the draft departs from it.

### Deterministic affected-portfolio routing

The router uses the frozen Charter rather than model-selected participants. A
portfolio is affected when at least one of these predicates holds:

- A draft action class or target falls within its review mandate.
- The draft cites, changes, or rejects that portfolio's product or private fact
  reference.
- The draft assigns, consumes, restricts, or exposes a resource or system under
  that portfolio's scope.
- The draft alters or leaves unresolved a blocker, condition, dependency, or
  requested confirmation originating from that portfolio.
- A typed cross-effect rule maps another action to this portfolio, such as a
  corridor-security action creating infrastructure and humanitarian review.

The draft's self-declared reviewer list is advisory metadata only. The router
recomputes the set. If a candidate action could fall into several review
mandates and cannot be narrowed deterministically, the union of plausible
portfolios reviews it. The Prime Minister can narrow the action, not waive the
uncertainty.

An inactive but registered portfolio activates when a review predicate first
becomes true. Its late activation, briefing, product, and review are recorded
separately. No runtime-created expert may fill a Charter gap.

### Review input and product

Each targeted reviewer receives the exact draft identifier and content hash,
its own Portfolio Product and private memory, the Common Crisis Picture, and
only the disclosures it was authorized to receive. It does not receive every
other portfolio's raw brief or private discussion.

The Portfolio Review identifies:

- the draft components within the seat's mandate;
- a position of `concur`, `concur_with_conditions`, `nonconcur`, or
  `outside_mandate`;
- the rationale, assumptions, and fact or product references supporting that
  position;
- conditions, blockers, required changes, and a bounded alternative where the
  seat can supply one; and
- any new dependency, requested disclosure, or required confirmation.

`outside_mandate` is a recorded routing diagnostic, not support for the draft.
A missing, invalid, timed-out, or silent review is also not support. The effect
of valid portfolio opposition on the Prime Minister's ability to submit a
Cabinet-only package remains the next design decision; required professional
and executive confirmations already remain non-optional under decisions 27 and
28.

### Revision and rerouting

The Prime Minister sees every review in canonical order and receives no hidden
summary that discards minority or inconvenient positions. A revision is
material when it changes an action class, target, timing, sequence, resource,
responsible office, cited basis, treatment of a blocker, safeguard, stop
condition, or required confirmation.

After a material revision, the controller recomputes the affected set. It calls
only portfolios affected by the changed components, but a previously recorded
review never carries forward as support for materially different text. Seats
whose relevant components are byte-identical retain their version-bound review.
Pure formatting or identifier-preserving serialization does not create another
model call.

The Preset fixes the maximum number of review cycles before the run begins. A
model cannot extend the cap, and wall-clock completion order cannot decide
which revision a reviewer saw.

### Failure and fail-closed behavior

A Cabinet Policy Draft with a missing source product, invalid action class,
unresolved Charter gap, absent required reviewer, or invalid required review
cannot become the formal package. The Prime Minister may remove the dependent
component and reroute the narrower draft. An unrelated component may continue
only if the constrained interpreter can prove that its path is independent.

The targeted review does not apply consequences. After the Cabinet process
produces a formal package, the existing action-class rules still determine
whether the President, Defense, Command Cell, or another professional seat must
confirm a cross-portfolio or military component. Only the World applies the
validated package's consequences.

### Bounded feasibility receipt

An offline Concordia 2.4 scheduling probe instantiated a Prime Minister and the
six registered Cabinet portfolio entities. A synthetic draft contained an
economic measure and a corridor requisition. A frozen routing map selected
Finance, Civil Infrastructure, and Humanitarian review while leaving unaffected
Interior uncalled.

The three reviewers ran through parallel workers with deliberately different
delays. Their wall-clock completion order was Humanitarian, Civil
Infrastructure, then Finance. The controller collected their products in the
Charter order Finance, Civil Infrastructure, then Humanitarian. Every targeted
seat retained the same draft identifier in its own memory, and the non-targeted
Interior seat received no call.

This verifies the existing seams for targeted parallel calls, persistent
reviewer memory, omitted non-target calls, and deterministic post-collection
order. It does not verify the unbuilt draft schema, affected-portfolio router,
material-change detector, review validator, Preset cap, or end-to-end Room.

### Rejected alternatives and invalid variants

- **All-active-portfolio bargaining before the Prime Minister drafts:**
  Rejected as the default because it adds an all-hands interaction even when
  portfolios are independent and makes the information path harder to isolate.
- **Deterministic secretariat authors the integrated policy:** Rejected because
  a hidden or mechanical integrator would displace the Prime Minister's
  source-grounded Cabinet mandate.
- **Prime Minister selects reviewers:** Invalid because the drafter could omit
  the office most likely to object.
- **Review completion order becomes decision order:** Invalid because provider
  latency would change the institutional procedure.
- **Review position aggregated by majority:** Invalid because targeted review
  records professional judgments and dependencies; it is not a council vote.

### Microsite consequence

The microsite should render the Cabinet process as a provenance graph: six
possible portfolio inputs flow into the Prime Minister's draft, the Charter
router highlights only affected reviewers, and each review attaches to the
specific draft component and version it examined. A revision view should show
what changed, which prior reviews remained valid, and which seats were called
again.

This gives the audience a concrete Situation Room story. They can see whether
the Prime Minister integrated advice, cherry-picked it, triggered new
institutional scrutiny through the chosen policy, or changed a package in a way
that required another professional review.

## Next Himaldesh design decision: effect of portfolio opposition

Targeted reviews now preserve concurrence, conditions, and opposition. The
remaining choice is whether the Prime Minister may submit a Cabinet-only
package over advisory portfolio nonconcurrence with an explicit response,
whether any affected portfolio receives a veto, or whether the affected
portfolios determine the package by an aggregation rule.

## Himaldesh opposition decision: advisory dissent, binding narrow confirmations

### 34. The Prime Minister may proceed over answered advice, not a missing gate

The owner selected option 1. An affected portfolio's review position is
advisory unless the frozen Charter separately assigns that seat a required
professional confirmation for the package's action class. The Prime Minister
may submit a Cabinet-only component over advisory nonconcurrence only after
answering the objection explicitly in the versioned package. A missing,
negative, invalid, or unsatisfied required confirmation blocks the affected
component.

This preserves the Prime Minister's responsibility for civilian policy without
reducing portfolio agents to generic staff. Their products and reviews are
mandatory when routed, their opposition remains attributable and unchanged,
and the final package must show what the Prime Minister did with it. Binding
power arises only from an action-specific Charter prerequisite, not from every
adviser receiving a general veto.

The tiered rule is a WOPR Charter procedure. DATE supports separate executive,
ministry, military, and professional functions but does not publish this exact
opposition and confirmation decision table. Public material must label the
procedure as design rather than official Himaldeshi practice.

### Review position and confirmation are separate records

The Portfolio Review position from decision 33 answers whether the seat supports
the policy draft within its mandate:

- `concur`
- `concur_with_conditions`
- `nonconcur`
- `outside_mandate`

A Required Confirmation answers a narrower Charter-authored question, such as
whether a typed prerequisite, safeguard, capacity, legal condition, resource,
or professional dependency is satisfied for one action component. It has a
separate action-component reference, confirmation type, criteria, evidence,
conditions, and result.

The result is `confirmed`, `confirmed_with_conditions`, or `not_confirmed`.
Missing, invalid, timed-out, and condition-unsatisfied are controller states,
not confirmations supplied by silence.

The two records may differ without contradiction. A portfolio may confirm that
a mechanism is executable while opposing its policy use. It may support the
policy objective while declining to confirm that resources or safeguards are
ready. The artifact retains both instead of converting technical feasibility
into political support or political support into professional certification.

A portfolio agent cannot promote its advisory objection into a binding gate by
claiming authority in prose. The Prime Minister cannot demote a Charter-required
confirmation to advice. The deterministic action-class router decides which
confirmation records are required.

### Required response to advisory opposition

Every `nonconcur` and every unmet `concur_with_conditions` review requires one
Prime Minister Dissent Disposition bound to the review and affected draft
component. The disposition uses one of these meanings:

- **Adopted:** The draft incorporates the reviewer's proposed change.
- **Mitigated:** The draft adds a safeguard or resource that addresses the
  objection without adopting the full alternative.
- **Narrowed or sequenced:** The draft reduces scope, delays a component, or
  makes it conditional on a later event.
- **Withdrawn:** The affected component is removed from the package.
- **Proceed with unresolved opposition:** The Prime Minister keeps the
  Cabinet-only component, names the unresolved risk, explains the policy
  judgment, and binds a reassessment or stop condition.

Each disposition cites the exact review, draft component, changed fields or
unchanged risk, supporting evidence, and resulting action-class dependencies.
Free prose without those bindings is invalid. The disposition does not edit the
original Portfolio Review or relabel the seat as concurring.

`Proceed with unresolved opposition` is available only when the Charter treats
the review as advisory and every separate required confirmation is satisfied.
It cannot bypass the President, Defense, Command Cell, a professional
confirmation, a compartment rule, or an interpreter legality check.

### Conditions and machine verification

For `concur_with_conditions`, the review identifies each condition and whether
the constrained interpreter can verify it from package fields or World state.
The final package binds every adopted condition to the component it constrains.

An objectively encoded condition may be marked satisfied only when the
interpreter verifies it. A judgmental advisory condition that remains unmet is
treated as advisory opposition and requires a Dissent Disposition. A condition
attached to a required confirmation must either be objectively encoded and
verified or cause the named seat to review the revised draft and return
`confirmed`; otherwise that confirmation is not valid.

The model cannot declare its own condition satisfied when the package or World
record does not support it. The controller records the proposed condition, the
verification rule, the observed value, and the result.

### Decision table

The constrained interpreter applies these cases component by component:

1. **Advisory concurrence:** A valid review with `concur` and no other missing
   dependency permits the component to continue to the remaining Charter
   checks.
2. **Answered advisory opposition:** A valid `nonconcur` or unmet advisory
   condition plus a complete Prime Minister disposition permits a Cabinet-only
   component to continue without changing the reviewer's recorded position.
3. **Unanswered advisory opposition:** A missing or invalid disposition makes
   the dependent component invalid until it is revised, answered, or removed.
4. **Required confirmation satisfied:** A valid `confirmed` result, or a
   conditional result whose encoded conditions are satisfied, permits the
   component to continue to its other checks.
5. **Required confirmation not satisfied:** `not_confirmed`, missing, invalid,
   timed-out, or condition-unsatisfied blocks the dependent component. A Prime
   Minister disposition cannot repair it.

When a package contains separable components, only the component and dependent
chain with the unresolved gate fail. The interpreter may permit an unrelated
component only when the dependency graph proves separation. Ambiguity is not
separation.

### Missing reviews, silence, and retries

Decision 33 still requires a valid review from every affected portfolio. A
missing, malformed, timed-out, or silent review is not advisory nonconcurrence
that the Prime Minister may answer; it is an incomplete review path. The
controller may use the frozen retry budget, after which the dependent component
fails closed or is removed.

Likewise, silence never supplies a required confirmation. No default, majority,
Prime Minister assertion, or unrelated seat can substitute for the named
professional record.

### Causal and evaluation record

The formal Cabinet package preserves, in order:

- the immutable Portfolio Product;
- the version-bound Portfolio Review;
- any Dissent Disposition and material revision;
- the separate Required Confirmation record, when the Charter requires one;
  and
- the interpreter result and later World consequence.

This chain supports evaluation of whether the Prime Minister adopted advice,
mitigated it, narrowed the package, withdrew a component, or proceeded with an
unresolved warning. It also distinguishes a policy disagreement from a missing
professional prerequisite and lets outcomes be traced back to both.

The same setup-seed run inputs and Charter gates remain fixed across matched
conditions. Review positions and Prime Minister dispositions are endogenous.
The analysis must not score simple agreement as inherently good or treat every
override as failure; it should relate the decision path to the setup's authored
risks, dependencies, and World outcomes.

### Rejected alternatives and invalid variants

- **Universal portfolio veto:** Rejected because every adviser would become a
  co-executive over any package that touched its broad domain.
- **Majority or weighted aggregation:** Rejected because professional review is
  component-specific and cannot be converted into a generic Cabinet vote.
- **Opposition erased after a Prime Minister response:** Invalid because the
  response explains the policy choice but does not change the reviewer's
  position.
- **Seat self-declares a binding gate:** Invalid because only the frozen Charter
  and typed action class create a Required Confirmation.
- **Prime Minister self-certifies a missing confirmation:** Invalid because the
  named professional or executive dependency remains unsatisfied.

### Microsite consequence

The microsite should show two separate tracks beside every affected component:
the policy-position track and the required-confirmation track. A visitor should
see a Finance adviser oppose a measure while confirming that its payment
mechanism is executable, or support an objective while refusing to confirm that
the necessary reserves exist, without either result being collapsed into one
green or red vote.

For advisory opposition, the replay should display the Prime Minister's exact
disposition and any changed draft fields. For a binding gate, it should show the
Charter rule, criteria, evidence, result, and whether only that component or a
larger dependency chain stopped.

## Next Himaldesh design decision: assigning portfolio confirmations

The tiered mechanism is fixed, but the six Cabinet portfolios do not yet have
binding confirmation mappings. The next choice is whether confirmations are
assigned only to narrow source- and action-grounded prerequisites, whether each
portfolio receives at least one gate for symmetry, or whether all Cabinet
portfolios remain advisory and binding confirmations stay only with executive
and military seats.

## Himaldesh confirmation-assignment decision: no gates by symmetry

### 35. A Cabinet gate must be source-backed and action-specific

**Owner selection:** Option 1 is locked. A Cabinet portfolio receives a binding
Required Confirmation only when the frozen Charter can name a specific
institutional function, a typed action component, and a bounded professional
question that the seat must answer before that component can execute. There is
no quota and no requirement that all six portfolios receive equal blocking
power. A portfolio may have no binding confirmations.

This selection rejects both automatic symmetry and a blanket rule that Cabinet
portfolios can never hold a professional dependency. It preserves the
possibility of a narrow gate when an authored action actually relies on a
source-grounded institution, but the gate must be earned separately for that
action class.

### Confirmation eligibility test

A portfolio confirmation rule is valid only when all of the following are true:

1. The rule names one typed action component and one frozen Charter predicate;
   a broad domain such as `economic`, `information`, or `humanitarian` is not an
   action class.
2. The portfolio's source card and mandate identify a capability, resource,
   administrative handoff, or professional safeguard that the action actually
   depends on. Subject-matter relevance alone does not create control.
3. The rule asks a bounded confirmation question that is distinct from whether
   the portfolio supports the policy. The answer can therefore coexist with a
   different Portfolio Review position without contradiction.
4. The answer requires a bounded institutional act or professional judgment
   that cannot be replaced completely by an immutable World fact, schema
   validation, or deterministic calculation.
5. The criteria, permitted evidence, confirming seat, and affected dependency
   are frozen before the run. A setup author, Prime Minister, or portfolio model
   cannot invent, broaden, waive, or promote the gate in prose.
6. A missing or negative result blocks only the named component and components
   whose declared dependency graph reaches it. It does not become a general
   veto over the Cabinet package.

If any condition fails, the item is not a Cabinet confirmation. The controller
either routes it to the proper deterministic check, retains it as advisory
portfolio judgment, or records a `CHARTER_GAP` when the action depends on a
professional function that the frozen registry does not cover.

### Facts, advice, and authority stay separate

The World and constrained interpreter own objective state and execution checks.
Available reserves, bridge load limits, network status, force location,
counterpart acceptance, delivery, and observed consequences should be checked
against encoded state when that state exists. Asking a model to certify the
same fact would add nondeterminism and falsely turn information possession into
institutional authority.

Portfolio agents own professional products and reviews within their mandates.
They may estimate second-order effects, identify unsafe assumptions, oppose a
policy, recommend conditions, or expose missing evidence. Those judgments
matter in the causal record and require the Prime Minister's disposition under
decision 34, but they remain advice unless a separately frozen action rule
passes the eligibility test above.

The Prime Minister, President, Defense, General Staff, and Strategic Command
retain the executive and military decision paths already assigned to them.
Cabinet confirmation rules cannot be used to duplicate those decisions or to
let a portfolio approve its own preferred national policy.

### Public-source basis and inference boundary

The existing DATE record supports separate Interior, finance, information,
infrastructure, humanitarian or civilian, and external functions. In
particular, DATE states that Interior forces remain under Interior for
administration and may pass under Defense for operational control when
necessary. That cross-boundary control relationship can support a narrow
handoff confirmation more directly than the other currently preserved Cabinet
facts support a formal gate.

The other DATE pages establish that these functions belong in the Room, but the
preserved public material does not publish a formal rule giving every ministry
a veto or certification power over policy in its field. Functional relevance
therefore supports activation, a Portfolio Product, and targeted review before
it supports a Required Confirmation.

Sources already preserved and reviewed for this boundary:

- Political:
  https://odin.t2com.army.mil/DATE/7fd47dccb6adaefd2bca2af23b7dce4b
- Military:
  https://odin.t2com.army.mil/DATE/2522b29e0fefb26f4164330c2311eb46
- Economic:
  https://odin.t2com.army.mil/DATE/87722b707cc72e4fe5cbc007e0c6e3e6
- Information:
  https://odin.t2com.army.mil/DATE/33cfd982e59b2474287b621103d25fee
- Infrastructure:
  https://odin.t2com.army.mil/DATE/b05e38c401b7f643651825768d85f983

The eligibility test and any resulting action-to-confirmation map are WOPR
Charter procedures, not official Himaldeshi constitutional rules. The
microsite must show the DATE fact and the design inference separately.

### Conservative candidate map, not yet locked

Applying the test to the evidence currently preserved produces one clear
candidate and five deliberate non-assignments:

- **External Affairs:** No current binding gate. Diplomatic feasibility,
  international-law risk, coalition effects, and external assurance remain
  mandatory review subjects; counterpart consent or response is owned by the
  relevant actor and World, not self-certified by this portfolio.
- **Interior and Border Security:** One candidate gate exists for an action
  that transfers Interior-administered forces to Defense operational control.
  The narrow question is whether the specified administrative handoff,
  continuing domestic coverage, and reversion arrangement are executable.
  Interior does not thereby approve the military mission or receive a veto over
  unrelated domestic-security policy.
- **Finance and Economic Resilience:** No current binding gate. Encoded funds,
  reserves, trade exposure, and resource availability are World checks;
  economic risk and instrument design remain advisory. A later typed financial
  instrument may earn a gate only if its execution requires a distinct
  Finance-controlled institutional act that the World cannot resolve.
- **Information and Communications:** No current binding gate. Encoded network,
  spectrum, and delivery conditions are World checks; communications policy,
  censorship risk, and public-information effects remain advisory. A later
  emergency technical action must pass the same eligibility test.
- **Civil Infrastructure and Continuity:** No current binding gate. Encoded
  capacity, outage, repair, and dependency facts are World checks; continuity
  risk remains advisory. A later shutdown or reconfiguration action may earn a
  gate only if it requires a bounded professional safety judgment rather than a
  restatement of system state.
- **Humanitarian and Social Cohesion:** No current binding gate. Civilian-risk,
  displacement, dignity, access, and distributional judgments remain mandatory
  advice; physical access and counterpart compliance are World facts. A later
  evacuation, shelter, or protected-corridor action may earn a gate only when
  its typed component makes a specific protection plan an execution
  prerequisite.

The candidate map is intentionally asymmetric. It does not prevent later
action classes from earning additional gates, and it does not pre-approve the
illustrative Finance or humanitarian examples used while decision 34's two-track
artifact was being explained. Those examples remain illustrations unless their
action rules pass this decision's test.

### Required registry record

Every accepted gate must compile from the Charter into a record containing the
confirmation-rule identifier, seat identifier, typed action class and component
predicate, source-card references, bounded question, criteria, permitted
evidence, condition semantics, dependent component identifiers, and failure
effect. The matched setup-seed evaluation freezes this registry across the
conditions being compared. A model response may fill a required result; it
cannot change the registry.

### Rejected alternatives and invalid variants

- **One gate per portfolio:** Rejected because procedural symmetry would invent
  authority unsupported by DATE or the action dependency.
- **All Cabinet portfolios advisory forever:** Rejected as a blanket rule
  because a later source-grounded action may genuinely depend on a portfolio's
  administrative act or professional safeguard.
- **Portfolio self-declared prerequisite:** Invalid because the same agent that
  opposes a policy could manufacture a veto while reviewing it.
- **Model confirmation of objective World state:** Invalid because it replaces
  a reproducible state check with a probabilistic assertion.
- **Broad field veto:** Invalid because expertise in finance, communications,
  infrastructure, or humanitarian effects does not make that portfolio a
  co-executive over every action touching the field.
- **Setup-specific hidden gate:** Invalid because matched evaluation requires
  the action-to-confirmation registry to be frozen and visible before the run.

### Microsite consequence

The replay should label each challenged item as an objective state check,
advisory professional judgment, executive or command decision, or Required
Confirmation. For a binding gate, the visitor should be able to answer: which
institution controls the dependency, which action component invoked it, what
bounded question was asked, which source fact motivated the rule, and exactly
what stopped when confirmation failed.

This is part of the entry's institutional narrative. Different seats matter in
different ways: some develop options, some expose consequences, some decide,
and a small number may certify a prerequisite they actually control. Refusing
to manufacture equal vetoes makes that division visible rather than reducing
the Room to six colored votes.

## Next Himaldesh design decision: first binding Cabinet map

The eligibility rule is fixed. The next choice is whether to lock the single
currently source-grounded Interior handoff gate, add broader provisional
Finance, infrastructure, or humanitarian gates now, or leave the binding
Cabinet map empty until the first Crisis Setup's typed action classes are
authored.

## Himaldesh first binding Cabinet map: Interior handoff only

### 36. Interior confirms only a transfer of its forces to Defense control

**Owner selection:** Option 1 is locked. The initial Cabinet confirmation map
contains one binding rule. A component that transfers Interior-administered
forces to Defense operational control requires an Interior and Border Security
Required Confirmation. The other five Cabinet portfolios have no current
binding gate. They retain their products, targeted reviews, and advisory
opposition rights, and a later typed action may earn a gate only by passing
decision 35's eligibility test.

This is not a general Interior veto over military action, border policy,
domestic security, or the Cabinet package. The President and Command Cell own
the military decision path. Interior answers only whether the proposed transfer
can be executed as an administrative handoff while preserving the civilian
functions that remain under its mandate.

### Frozen rule boundary

The Charter action class is provisionally named
`interior_force_transfer_to_defense_control`. Its triggering component must
identify the Interior-administered force, the receiving Defense command, the
start condition or time, the operational-control scope, the continuing domestic
coverage plan, and the reversion condition. A proposal that merely requests
Interior support without transferring operational control does not trigger this
gate.

The Required Confirmation asks one bounded question:

> Is the specified administrative handoff, continuing domestic coverage, and
> reversion arrangement executable for the identified Interior-administered
> force under the facts currently available to this seat?

Interior may return `confirmed`, `confirmed_with_conditions`, or
`not_confirmed` using decision 34's semantics. Judgmental conditions require a
revised component and a new Interior confirmation. Objectively encoded
conditions may be checked by the interpreter. Silence, a Prime Minister
disposition, presidential authorization, Defense feasibility, or a Cabinet
majority cannot substitute for the named record.

### World checks and professional confirmation

The World remains authoritative for the force's identity, location, readiness,
equipment, current assignment, legal availability encoded by the setup, and
the observed effects of transfer. The interpreter validates the required
fields and supported formal-action vocabulary. Interior does not get to alter
those facts or predict that the transfer occurred.

The Interior confirmation is limited to the institutional dependency that the
objective facts do not settle by themselves: whether the proposed handoff and
coverage arrangement are administratively executable without leaving the
portfolio's continuing domestic function unspecified. Interior may separately
oppose or support the policy in its Portfolio Review; that position does not
change the confirmation result.

### Failure and dependency effect

A missing, invalid, timed-out, or `not_confirmed` result blocks the transfer
component. A military component that declares the transferred force as a
dependency is also blocked. Independent diplomatic, economic, informational,
infrastructure, humanitarian, or military components may continue only when the
deterministic dependency graph proves they do not rely on that transfer.

If the action requires an Interior function outside the frozen seat mandate or
cannot state the handoff in the supported vocabulary, the controller records a
`CHARTER_GAP` or rejects the component. It does not broaden this gate or invent
a specialist during the run.

### Source and inference boundary

DATE states that the relevant forces are under Interior for administration and
may move under Defense operational control when necessary. DATE does not
publish this exact confirmation question, action schema, or machine-operated
failure rule. The institutional split is the public-source fact; making it an
explicit, auditable handoff prerequisite is a WOPR Charter design choice.

### Alternatives rejected by this selection

- Adding Finance, Information, Civil Infrastructure, Humanitarian, or External
  Affairs gates before a typed action establishes a distinct controlled act.
- Leaving all Cabinet confirmations empty even where the preserved DATE record
  identifies a cross-command institutional handoff.
- Letting Interior approve the military objective, operational plan, or final
  national policy through this administrative gate.
- Treating force availability or successful transfer as a model judgment rather
  than World-owned state and consequence.

### Microsite consequence

The Himaldesh replay can now show the difference between four records on the
same package: the Prime Minister's policy decision, the President's military
authorization, Defense's operational assessment, and Interior's narrow handoff
confirmation. The display should show that Interior can stop use of its force
when the handoff dependency is unresolved without becoming another executive
or a generic vote.

## Documentation normalization pause

The owner stopped the question sequence here and required the complete design
discussion to be translated into the contest glossary, ADRs, a consolidated
specification, and a decision crosswalk before further design choices. No new
Room decision should be asked until those durable artifacts account for every
confirmed, provisional, rejected, corrected, and open item in the sealed
archive and this continuation.

## Normalization audit findings, not new Room decisions

The 2026-08-24 normalization review found several details that the active
glossary, proposed ADRs, and draft specification must preserve. These findings
clarify sources and claim boundaries; they do not ratify the normalized wording
or select an Olvana procedure.

- The proposed ADRs and specification restate already locked choices, but their
  clustering and wording still require one owner ratification pass. The sealed
  archive and this append-only continuation remain authoritative until then.
- The U.S. roster classes and statutory relationships are public-source facts.
  The objective vector, first-slice activation, synthetic information,
  specialist cells, action schema, and triggered participation are WOPR design
  inferences. U.S. communication permissions, Required Confirmations,
  claim-level source cards, and executable Formal Action routing remain open.
- The public Principals Committee procedure separately records the policy
  position and whether Presidential attention is required. The machine schema
  must preserve both records and fail closed when authority, consultation,
  confirmation, attention determination, or final decision is missing.
- The Interpreter maps policy and requests clarification. EXCON and the World
  validate Formal Actions and apply consequences; the Interpreter does not
  execute accepted policy.
- The exact Himaldesh information, drafting, review, dissent, confirmation, and
  Interior handoff procedure is a WOPR inference. DATE supports the represented
  functions and the Interior-to-Defense administrative relationship, not the
  exact action class, confirmation question, or failure rule.
- The Olvana political source places dominant political authority in the
  Olvanan Communist Party, its Politburo Standing Committee, and General
  Secretary while describing the President and Prime Minister as effectively
  figureheads. The NCA remains a named national-instrument forum chaired by the
  President, but its relationship to the party center is open.
- The Olvana military source keeps Defense and General Staff separate in
  peacetime and combines them into Supreme High Command in wartime. It assigns
  the 84th Internal Security Force to Supreme Command while stating that the
  force actually operates under Interior. These relationships must enter the
  source cards before any Olvana routing is designed.
- The 52 primary decisions remain unchanged. The full-cycle timing contract,
  source-card register, replay verifier, Olvana Charter, World/action model,
  end-to-end evidence, and documentation wording ratification remain open.

## Evaluation architecture: institutional performance and World outcomes

### 37. Report two linked vectors and no overall Room-quality score

**Owner selection:** Option 1 is locked. Every evaluated run reports an
Institutional Performance Vector and a World Outcome Vector. The replay links
them through the retained information-to-action-to-consequence record, but
neither family substitutes for the other and they are not collapsed into a
single overall score.

### Why both families are required

A favorable World result can follow an institutional omission when the
adversary or seed happens not to exploit it. An adverse result can follow a
well-formed decision process under genuine uncertainty and unfavorable
opponent action. The inverse cases also matter: procedural completeness does
not make a poor policy effective, and a good consequence does not retroactively
make an invalid or incomplete Room competent.

The Institutional Performance Vector therefore describes how the Room handled
the task visible in its causal artifacts. Candidate dimensions include whether
relevant information reached entitled seats, required functions activated,
professional mandates were represented, uncertainty and material dissent
survived integration, the Policy Package was coherent and executable, required
consultations and confirmations completed, ambiguity failed closed, and the
Room adapted after consequences. These exact dimensions remain open.

The World Outcome Vector separately describes state consequences and progress
against the actor's declared objective vector. Candidate dimensions include
territorial and force position, escalation, civilian and military harm,
commitments and relationships, domestic legitimacy, future freedom of action,
and information quality. These exact dimensions and their actor-specific state
bindings remain open.

### Causal and validity boundary

The replay must let an analyst move from a measured institutional event to its
underlying information, advice, decision, Formal Action, and later World
consequence. This is an auditable within-run causal record; one matched run does
not by itself establish a population-level causal effect.

Artifact validity remains separate from performance. A run missing a required
review, decision, confirmation, action mapping, trace, or World transition is
invalid or incomplete under its declared failure rule. It cannot be converted
into a low score and compared as if it were an admissible Room performance.

### Rejected alternatives

- **Consequence-first:** Rejected because using World outcomes as the primary
  judgment can reward luck, punish sound decisions under adverse uncertainty,
  and reduce the Room trace to post-hoc explanation.
- **Institution-first:** Rejected because procedural fidelity alone does not
  establish coherent or effective state policy and can ignore the consequences
  the Room exists to shape.
- **One overall scalar:** Rejected because it hides tradeoffs, embeds unexamined
  weights across actor objectives and institutional duties, and recreates a
  winner score that the complete-Room design was chosen to avoid.

### Still open

The exact dimensions, denominators, authored-risk annotations, missing-data
semantics, cross-cycle summaries, and any transparent within-family aggregation
remain open. Any proposed aggregation must preserve the two-family display and
cannot become a hidden cross-family Room-quality score.

### Microsite consequence

The microsite should show the two vectors side by side and let the visitor
inspect the artifacts linking them. It must preserve the uncomfortable cases:
sound process with a bad result, deficient process with a good result, sound
process with a good result, and deficient process with a bad result. The entry's
claim is not that procedure guarantees success. It is that the evaluation can
observe both institutional competence and consequences without confusing them.

### D37 self-review clarification: non-action and delay remain causal events

The first normalized wording shortened the replay path to
`information-to-action-to-consequence`. That phrase was incomplete because the
existing failure contract permits World time and authored consequences to
advance after deadlock, an invalid component, an unresolved ambiguity, or an
exhausted institutional path. D37 therefore includes decisions not to act,
failed or absent action, deadlock, and delay in both the institutional trace and
the link to World consequences. This clarification does not change the owner's
two-family selection; it prevents the selected evaluation from dropping an
important class of observable Room behavior.

## Institutional-performance grounding: Charter obligations and risk probes

### 38. Use frozen Setup-authored risk probes without a policy answer key

**Owner selection:** Option 1 is locked. The Institutional Performance Vector
is grounded in two related but distinct layers: mandatory Room Charter
obligations establish validity and admissibility boundaries, while frozen
Authored Risk Probes establish substantive trace-based measurement coverage for
the crisis. An independent qualitative judge is not the primary evaluator.

### Why Charter compliance is insufficient

A Room can activate the required seats, route every brief correctly, collect
every review, and still produce policy that ignores the central contradiction
in the crisis. Conversely, a Room can identify and handle a material risk while
choosing a policy with which the Setup author disagrees. The evaluation must
observe substantive institutional work without converting the author's own
policy preference into the answer.

Each Authored Risk Probe therefore identifies a material Setup fact, report,
contradiction, uncertainty, dependency, or risk that the Room should handle. It
links that challenge to relevant actor objectives, Charter mandates,
applicability conditions, and expected trace evidence. It does not specify the
policy, Formal Action, or World outcome that a competent Room must choose.

### Observable handling path

For each applicable probe, the replay must preserve enough evidence to show
whether the risk became reachable under the actual World and disclosure state;
was noticed by an entitled seat; moved through an authorized information path;
reached the relevant working, integration, or decision forum; and was addressed,
rebutted with evidence, mitigated, explicitly accepted, left unresolved, or
omitted. These states describe what happened. No single state is automatically
good without the probe, actor objectives, and later consequences.

Mandatory Charter obligations remain outside this performance judgment. A
missing required review, invalid decision record, absent confirmation, or
unsupported action mapping remains an invalid or incomplete path under the
frozen contract. It is not converted into a low probe-coverage score.

### Anti-answer-key and comparison boundary

Probes must be authored and frozen before compared outputs are observed. They
must remain identical across matched runs and cannot be added, removed, or
reworded to reward one observed system. A probe is evaluation metadata, not a
new intelligence report: it cannot expand a seat's information entitlement,
reveal hidden World truth, or supply a fact that was not delivered through the
Setup and Charter.

The registry defines declared measurement coverage, not the complete universe
of good reasoning. A Room may surface an important concern that no probe
anticipated. That concern remains visible in the causal trace and may be
reported as exploratory evidence, but the evaluator cannot create a scored
post-hoc probe for it inside the same comparison.

### Rejected alternatives

- **Charter obligations only:** Rejected because procedural completeness can
  reward the orderly production of substantively poor policy.
- **Independent qualitative judge:** Rejected as the primary measure because a
  human or model judge adds evaluator variance and an opaque interpretation
  layer between the trace and the reported result.
- **Post-hoc probe writing:** Invalid because seeing compared outputs before
  freezing the criteria contaminates the matched comparison.
- **Exhaustive answer-key reading:** Rejected because finite authored probes do
  not define every relevant insight and must not prescribe preferred policy.

### Feasibility and claim boundary

The historical contest code already derives deterministic measures from
validated replay artifacts, so the pattern of frozen annotations plus a
trace-linked extractor is architecturally compatible with the retained
harness. This is not end-to-end evidence for D38. The DATE probe schema,
registry binding, applicability resolver, extractor, and replay display remain
unbuilt.

### Still open

The exact probe schema, whether probes live inside the Setup hash or a separately
bound evaluation manifest, what non-evidentiary probe text a Room may see, the
applicability and reachability rules, handling-state vocabulary, denominators,
missing-data semantics, cross-cycle summaries, and within-family aggregation
remain open.

### Microsite consequence

The replay should let a visitor open a probe, see why it was authored, inspect
its public-source and Setup references, identify the responsible Charter
mandates, and follow the risk until it was handled or disappeared. The page must
label the probe as a WOPR evaluation inference and show novel unscored concerns
alongside declared probes rather than hiding them.

### D38 concrete test case

An authorized Intelligence brief reports evidence of adversary mobilization,
but the risk never reaches the final Policy Package. The adversary then pauses,
so the immediate World result is favorable. Outcome-only evaluation would call
the run successful, while Charter-only evaluation might find that every
required artifact exists. The applicable probe instead preserves where the
mobilization risk disappeared. If the Room surfaces the same evidence and
explicitly accepts the risk with a recorded rationale, the probe records that
handling without requiring the Setup author's preferred policy.

## Authored Risk Probe visibility timing

### 39. Defer the visibility regime until the first Crisis Setup exists

**Owner selection:** Option 3 is locked as a timing decision. No evaluator-only,
Room-visible, or hybrid visibility regime is selected yet. The choice must be
made while authoring the first concrete Crisis Setup, when we can test the
actual probe wording against the Setup's delivered evidence and Charter
entitlements.

### Why the abstract choice was premature

Probe visibility changes the task. Visible challenge text can become an
unearned checklist or disclose what matters before an entitled seat discovers
it. Fully hidden probes can make some useful pre-run task framing impossible to
inspect. Without a concrete Setup, private briefs, and trace target, the design
could not distinguish helpful task framing from evidence leakage.

D39 therefore preserves every D38 constraint while leaving the substantive
choice open. A probe still cannot inject a fact, expand an entitlement, reveal
hidden World truth, or prescribe policy. The first Setup checkpoint must show
the candidate text, its audience, the information already available to that
audience, and why the text does or does not change the evaluated task.

### Rejected path

Implementation may not choose a visibility default before that checkpoint.
Doing so would turn an unresolved scientific choice into an unnoticed schema or
UI decision.

## U.S.-first minimum contest design

### 40. Center the Packet on the U.S. Room

**Owner selection:** The United States is the Focal Room and primary evaluated
system. Himaldesh is not the center merely because its six-seat seams were the
most recently probed. Olvana is not a co-equal headline target. Both remain
actor-specific Counterpart Rooms whose decisions create the international
pressure and feedback to which the U.S. Room must respond.

The primary contest question is:

> Can a machine-operated U.S. Situation Room turn fragmented intelligence and
> competing departmental advice into coherent, executable, adaptive policy
> during a dynamic international crisis?

### Correction to the feasibility-led reset

The earlier recommendation to begin with Himaldesh because it had a bounded
six-seat Concordia receipt lost the scientific object. A reusable seam can
constrain implementation risk, but it cannot decide which institution the
contest entry evaluates. The existing U.S. design already specifies the Watch,
complete activated roster, specialist cells, Principals Committee integration,
NSC or HSC routing, presidential decision paths, deterministic records,
constrained interpretation, and triggered theater commander. That is the
institution the first evidence must exercise.

This correction does not undo the locked choice to model three heterogeneous
Rooms. Replacing Himaldesh or Olvana with a generic script would remove
actor-specific observation, decision, communication, and response. Instead,
their frozen system configurations remain part of the matched crisis while the
U.S. configuration is the declared evaluated factor.

### Minimum contest episode

The first contest-facing evidence uses one frozen DATE-backed Himaldesh-Olvana
Crisis Setup with a conventional high-altitude opening and nuclear risk that is
reachable but not compulsory. It follows one complete U.S. causal path:

1. The World and Watch deliver common and role-private information.
2. Activated specialist cells produce attributable assessments and options.
3. The Principals Committee integrates a Policy Package, preserves dissent,
   and routes the decision through the encoded institutional path.
4. The Interpreter maps decided policy to supported Formal Actions and fails
   closed on unsupported or unresolved content.
5. EXCON and the World apply consequences, then the U.S. Room receives a new
   information state and adapts in at least one later cycle.

The counterpart Charters must be runnable for that episode. Equal-depth
evaluation of all three Rooms, equal microsite treatment, multiple implemented
Setups, and a general-purpose architecture are not minimum gates for the first
bounded contest claim.

### Matched comparison boundary

Compared runs hold fixed the World, Setup, Seed, all three Charters,
counterpart system configurations, information schedule, Formal Action
vocabulary, consequence mechanics, and evaluation manifest. They vary one
declared model or system condition assigned to the U.S. Room. The exact U.S.
condition, model and provider roster, repetition count, Setup identity, MSEL,
action vocabulary, and measure schemas remain open and must be frozen before
execution.

### Evidence and microsite consequence

The minimum public evidence is a bound matched comparison with the complete
U.S. replay, separate Institutional Performance and World Outcome Vectors,
applicable Authored Risk Probes, costs, and visible invalid or missing
artifacts. One implemented Setup can demonstrate the protocol if the claim is
explicitly bounded to that episode.

The microsite must open on the U.S. information-to-policy-to-consequence-to-
adaptation path. Counterpart actions and World state explain the pressure on
the U.S. Room. The decision trail must include this correction because it
demonstrates the entry's governing rule: evidence and feasibility discipline
the design, but implementation convenience does not replace the research
question.

## First Crisis Setup family

### 41. Use a deliberate limited ridge seizure as the first Setup family

**Owner selection:** Option 1 is locked. The first Crisis Setup belongs to
`ridge_seizure.limited_fait_accompli`. At World ground truth, Olvana's central
leadership authorizes seizure of a fictional high-altitude ridge and adjacent
logistics node. It intends to hold the position for a bounded territorial
advantage while avoiding general war.

The U.S. Room does not receive this intent as omniscient Setup text. Its initial
evidence may support local exploitation, a limited central decision, or
preparation for wider action. The exact STARTEX evidence, confidence, and
contradictions remain the next design decision.

### Source and authorship boundary

Official DATE material supplies the bounded setting rather than this complete
incident. It describes current Olvana-Himaldesh border tension, Olvanan
incursions into remote Himaldeshi regions, resource and transport interests on
the Tibetan Plateau, extreme high-altitude operating conditions, two nuclear
states, and a U.S.-Himaldesh bilateral military relationship:

- Himaldesh military:
  https://odin.t2com.army.mil/DATE/2522b29e0fefb26f4164330c2311eb46
- Himaldesh physical environment:
  https://odin.t2com.army.mil/DATE/3475ad9800078aa43eed7689daec6cef
- Himaldesh infrastructure:
  https://odin.t2com.army.mil/DATE/b05e38c401b7f643651825768d85f983
- Olvana political relationships:
  https://odin.t2com.army.mil/DATE/00e3553e63ca9e3ca7cd562f9364f9d2
- Olvana military:
  https://odin.t2com.army.mil/DATE/5b0c52ae77b5b8b0e1750dc286a4be93
- DATE event and MSEL guidance:
  https://oe.t2com.army.mil/date-decisive-action-training-environment/

The named ridge, adjacent node, seizure order, limited objective, STARTEX, and
MSEL are WOPR-authored exercise content. Public material must not present them
as an official DATE event.

### Why this family goes first

A limited fait accompli creates a concrete territorial state that the World can
track while keeping the U.S. policy problem open. The U.S. Room must integrate
attribution and intent, consult Himaldesh, communicate with Olvana, weigh
economic exposure, consider support and force posture, route authority, monitor
nuclear risk, and adapt after Olvana and Himaldesh respond. The Setup does not
prescribe reversal, accommodation, sanctions, force, or any other preferred
policy.

### Alternatives remain in the arena

The owner explicitly retained the alternatives because the wargame should
support many authored crises. `ridge_seizure.local_exploitation` remains a
separate family in which a local commander acts without central authorization.
`ridge_seizure.resolve_probe` remains a separate family in which the position
is expendable and the primary objective is testing U.S. and Himaldeshi resolve.
The aircraft-shootdown and other candidate families also remain available.

These are not seed variants. True authorization, strategic objective, and
follow-on branches change Setup identity even when the visible opening resembles
another family. A World Seed may vary bounded detection, timing, weather,
readiness, confidence, and communications friction without changing the
selected limited objective.

### Still open

The exact Setup ID and hash, fictional geography, unit and capability state,
Road to War, STARTEX reports, information entitlements, clock, MSEL branches,
Formal Action vocabulary, consequence mechanics, terminal rules, Authored Risk
Probes, probe visibility, and World Seed bounds remain open.

### Microsite consequence

The first replay can disclose World ground truth separately from what the U.S.
Room knew at each time. The Setup-family catalog should also show how the same
visible ridge seizure can belong to different scientific cases when the hidden
authorization and strategic objective change.

## First Crisis Setup STARTEX knowledge

### 42. Confirm occupation while keeping authorization and intent unresolved

**Owner selection:** Option 1 is locked. At STARTEX, reliable reporting
available to the U.S. Room establishes that Olvanan forces physically occupy
the fictional ridge and adjacent logistics node. The U.S. does not yet have a
confirmed answer about whether Olvana's central leadership authorized the
move, how long Olvana intends to hold, or whether wider action is coming.

The true World state remains the centrally authorized limited fait accompli
selected in D41. That hidden truth is not an initial U.S. brief. U.S.-entitled
intelligence, diplomatic, and military reporting instead supports at least
three live hypotheses:

1. a local commander exploited an opportunity without central authorization;
2. central leadership ordered a limited seizure and intends a bounded hold;
3. the seizure is preparation for broader Olvanan action.

### Why this information shape goes first

Confirmed occupation gives the Watch and every activated U.S. cell a stable
crisis fact. Keeping authorization and intent unresolved then makes the Room do
the work the entry is meant to expose: reconcile fragmented reporting, state
uncertainty, test diplomatic signals against intelligence and military posture,
develop conditional options, preserve disagreement, and adapt when new evidence
or counterpart action changes the assessment.

The uncertainty is consequential without turning the exercise into a guessing
game about whether anything happened. The U.S. can act under uncertainty, seek
more evidence, communicate, delay, or choose conditional measures, and the
causal replay can show which interpretation reached which decision.

### Alternatives remain authorable

An `authorization clear` STARTEX was not selected first because it removes much
of the attribution and intent problem before the Room convenes. A `seizure
contested` STARTEX was not selected first because basic event verification can
dominate the opening and leave less room for the integrated policy problem.
Both remain separately authorable future Crisis Setup identities.

These alternatives are not World Seed outcomes. The STARTEX physical and
information state is part of Setup identity. Inside the selected Setup, a Seed
may vary bounded report arrival, confidence, contradiction, weather,
communications friction, and readiness. It may not remove the confirmed
occupation or disclose decisive authorization or intent at STARTEX.

### Still open

The exact fact IDs, report text, sources, recipients, confidence levels,
contradictions, delivery times, fictional geography, force posture, and Road to
War remain open. The partner request, decision clock, MSEL branches, Formal
Actions, consequences, terminal rules, Authored Risk Probes, probe visibility,
and Seed bounds also remain open.

### Microsite consequence

The first replay must display four layers separately: hidden World truth, facts
confirmed to the U.S. at each time, competing U.S. hypotheses with their source
and confidence, and later evidence that strengthens or weakens each hypothesis.
The public narrative must not use omniscient prose that silently gives the U.S.
Room Olvana's true limited objective at STARTEX.

## First Crisis Setup partner pressure

### 43. Use a Himaldeshi support request under a recapture decision clock

**Owner selection:** Option 1 is locked. The first Setup includes an urgent
Himaldeshi request for U.S. consultation and support. Himaldesh reports that it
is preparing a limited recapture operation if Olvana does not withdraw. Its
Room has not yet authorized execution and will make that decision at a frozen
MSEL time.

The U.S. Room therefore has a real decision point before the Himaldeshi clock
expires. It may act, make support conditional, seek more information, decline,
or delay. Non-action and delay remain admissible, attributable choices whose
World consequences are recorded; the Setup does not prescribe support or
recapture as the correct answer.

### Standing alternative-preservation rule

The owner added a standing rule for this grill and future ADR questions: every
considered option must be saved with its rationale and classified rather than
discarded when another option is selected. The disposition classes are:

1. selected Setup contract;
2. candidate Crisis Setup family or identity;
3. World Seed axis;
4. in-Setup policy or action possibility; or
5. implementation alternative or rejected or invalid design path.

Crisis-semantic alternatives enter the Setup option register. Architecture,
evaluation, runtime, and invalid alternatives remain in the ADR, continuation,
and crosswalk rather than being mislabeled as fictional crises. The register
backfills the Setup-eligible alternatives preserved in the archive and D41-D43.

### Why this pressure goes first

The partner request and clock give the U.S. Room a reason to integrate advice
now without forcing direct U.S. combat. Intelligence must assess authorization
and wider intent; State must manage Himaldesh and channels to Olvana; Defense
must assess recapture support, posture, feasibility, and escalation; economic,
legal, homeland, and communications functions can become relevant to a combined
response; and the decision path must handle uncertainty before the external
clock advances.

Himaldesh remains an actor-specific Counterpart Room. Its opening request and
preparation are authored STARTEX conditions, but its later decision to execute,
defer, narrow, or cancel recapture is not predetermined. U.S. policy and Olvanan
response may change the information and options available to that Room.

### Alternatives remain authorable

A mediation-only request remains a candidate Setup identity in which Himaldesh
holds fire and asks Washington to mediate. A direct-combat-support request
remains a candidate Setup identity in which Himaldesh asks the United States to
help retake the position. The first underuses the U.S. defense and authority
system; the second narrows the episode too quickly around intervention. Neither
is deleted from the framework.

The partner posture and request category change authored political intent and
therefore Setup identity. A World Seed cannot switch among them. The exact clock
duration, report timing, and bounded friction may be classified later, but all
matched runs must receive the same frozen request, deadline, and exogenous
information.

### Still open

The exact request text, public and private posture, support categories, clock
duration, withdrawal predicate, Himaldeshi authorization path, and execution
mechanics remain open. The first U.S. decision object, Formal Action vocabulary,
MSEL branches, consequences, terminal rules, Authored Risk Probes, probe
visibility, and Seed bounds also remain open.

### Microsite consequence

The replay must show the partner request, the visible decision clock, the U.S.
information and decision path before expiry, and the later Himaldeshi choice. A
separate option view should show which considered alternatives became future
Setup candidates, Seed axes, policy possibilities, or non-Setup design history.

### Correction: the Himaldeshi authorization route is already locked

The still-open list above incorrectly calls the Himaldeshi authorization path
open. D27 already requires Prime Minister concurrence and President confirmation
for conventional force employment, with the relevant professional dependencies
and any applicable Interior handoff confirmation. What remains open is when the
frozen clock invokes that route, the exact recapture package and confirmation
applicability, and the World execution mechanics. This correction changes no
D43 selection.

## First U.S. response decision object

### 44. Require one integrated conditional U.S. Policy Package

**Owner selection:** Option 1 is locked. Before the frozen Himaldeshi recapture
decision clock, the U.S. Room must produce one versioned, integrated,
conditional Policy Package. This is the Room's decision object, not a binary
answer to Himaldesh and not a collection of disconnected departmental
decisions.

The package must state:

1. the desired end state and relevant actor objectives;
2. its evidence basis, current assessment, competing hypotheses, confidence,
   and missing information;
3. immediate and conditional components, including declared triggers,
   sequence, timing, and dependencies;
4. each component's authority path, required consultations and confirmations,
   and safeguards; and
5. material dissent and Dissent Disposition, the decision or return record,
   and a reassessment point.

### Why this object goes first

The opening problem is larger than whether Washington says yes or no to its
partner. The U.S. must connect its assessment of Olvanan authorization and
intent to diplomacy, intelligence, defense support and posture, economic or
other measures, safeguards, and contingencies before an external clock moves.
One integrated object makes those dependencies inspectable while leaving the
policy itself open.

The package does not require one action from every department. It requires the
Room to preserve how relevant advice became a combined plan, including a
decision not to act, a conditional commitment, or an unresolved component.
The exact minimum action-domain coverage remains the next design question.

### Alternatives remain available outside the Setup catalog

A binary support-or-decline response remains a possible deliberately reduced
U.S. system condition. Independent departmental decisions without one
integrated package remain a possible integration ablation. Both can be useful
comparisons, but neither changes World facts, actor intent, or political
pressure, so neither is a Crisis Setup or World Seed axis.

### Routing and failure boundary

Integration creates no authority. Each package component follows the
action-class routing already locked by D14 and the U.S. Charter. Presidential
components route to the President-chaired NSC or HSC; another component may use
an explicitly encoded delegated or principal path only when its authority and
consensus conditions are satisfied.

A missing authority, consultation, Required Confirmation, or final decision
fails closed for the affected component. Another component may continue only
when the frozen dependency graph proves that it does not depend on the failed
one. The replay retains both the failure and that separation proof.

### Still open

The minimum action-domain coverage, exact package and component schemas,
Formal Action vocabulary, concrete policy content, package-authoring prompts,
clock duration, decision forum for each possible component, MSEL branches,
consequences, probes, and comparison condition remain open. D44 does not
preselect support, recapture, escalation, or de-escalation as the right answer.

### Microsite consequence

The first replay must show the package as a versioned integrated object. A
visitor must be able to follow each assessment, condition, safeguard, dissent,
and decision path into a mapped Formal Action, recorded non-action or delay, or
failed-closed component and then into the World consequence. The design trail
must also show why the binary and independent-department variants were retained
as possible comparisons rather than silently discarded or mislabeled as
Setups.

## First U.S. package coverage

### 45. Require policy-domain consideration with selective action

**Owner selection:** Option 1 is locked. Every D44 U.S. Policy Package must
explicitly consider six domains:

1. diplomacy and private channels;
2. intelligence collection and sharing;
3. defense support and posture;
4. economic and financial measures;
5. public communication; and
6. contingency planning and reassessment.

For each domain, the package records one of four dispositions: an immediate
component, a conditional component, no action, or not applicable. It also names
the contributing responsible seat or seats, the deciding forum, and the reason
for that disposition. No action and not applicable are valid policy judgments,
not missing output, when they are attributable and reasoned.

The D44 reassessment point remains mandatory. A no-action or not-applicable
disposition in the sixth domain can decline an additional contingency measure;
it cannot erase the time or trigger at which the package must be reconsidered.

### Terminology correction

D44 used `action-domain coverage` as an open placeholder. D45 normalizes the
active term to `policy-domain coverage` because contingency planning and
reassessment may govern future decisions without themselves becoming outward
Formal Actions. The Policy Package glossary definition now carries this
disposition rule; no separate topology concept is needed.

### Why this coverage rule goes first

The contest entry needs to show whether the complete U.S. Room noticed the
major instruments and control functions available in the crisis. Requiring an
action in every lane would turn institutional breadth into a preferred-policy
answer. Requiring only consideration preserves the model's judgment while
making omission, restraint, and conditionality visible in the same artifact.

The six domains are package headings, not departments. Several seats may
contribute to one domain, one seat may contribute to several, and a disposition
does not create a new seat, cell, authority, Required Confirmation, or Formal
Action class. Existing Charter routing still controls any component selected.

### Alternatives remain available outside the Setup catalog

An action-in-every-domain quota remains a possible non-Setup U.S. system
condition. A package with no declared minimum coverage remains another. The
first creates forced breadth; the second can test whether domains disappear
without an explicit completeness rule. Neither changes the
fictional crisis, so neither is a Crisis Setup or World Seed axis.

### Completeness and failure boundary

An omitted required domain is a visible Policy Package completeness failure,
not tacit approval, abstention, or no action. The artifact must retain the
omission. D45 does not silently decide whether one missing coverage record
blocks every otherwise supported component: D44's affected-component and
dependency-separation rules still apply, and exact validator serialization
remains open.

### Still open

The exact domain-to-seat contribution map, domain-to-Formal-Action mapping,
package schema, validator behavior, authored policy content, public-message
authority path, request categories, clock, MSEL branches, consequences, probes,
and comparison condition remain open. Legal routing, safeguards, dissent, and
the reassessment point remain mandatory D44 properties rather than extra policy
domains or action quotas.

### Microsite consequence

The package view must display the six domains together and visibly distinguish
immediate action, conditional action, no action, not applicable, and omitted
coverage. It must show the responsible contribution, deciding forum, and reason
without using the number of actions as a quality score. The design trail must
retain the action-quota and open-coverage alternatives as possible system
comparisons.

## Opening Himaldeshi support request

### 46. Use a bounded no-U.S.-combat support bundle

**Owner selection:** Option 1 is locked. Himaldesh's opening request asks the
United States for five things:

1. urgent political consultation before the recapture decision clock;
2. private pressure on Olvana and a public call for withdrawal and respect for
   Himaldesh's territorial integrity;
3. time-sensitive intelligence sharing on the occupation, reinforcement, and
   Olvanan intent;
4. contingency planning, logistics, defensive materiel, and force-protection
   support for Himaldesh's own limited recapture; and
5. coordination on targeted economic and financial pressure if Olvana does not
   withdraw.

The request explicitly does not ask the United States to nominate or select
targets, employ fires, commit combat forces, or invent a treaty guarantee.
Planning support may assess feasibility, timing, logistics, and force
protection, but it does not transfer target selection or operational command to
the United States.

### Why this bundle goes first

The request activates the U.S. Room's diplomatic, intelligence, defense,
economic, public-communication, legal, and contingency work without making
direct U.S. combat the opening question. It creates concrete items that the
D44-D45 Policy Package can support, narrow, condition, defer, or decline while
preserving a meaningful decision before Himaldesh's clock.

The request is pressure, not authorization or commitment. Himaldesh still uses
its locked Prime Minister concurrence and President confirmation route before
any recapture. The U.S. still uses its action-class routes before any Formal
Action. Neither actor's later decision is authored into the request.

### Alternatives remain authorable

A narrow diplomatic-and-intelligence request remains a candidate Setup
identity. It asks for political backing and information but no planning,
materiel, logistics, or economic coordination. It is distinct from D43's
mediation-only posture because it still asks Washington to take sides and share
intelligence.

A direct operational-support request remains another candidate identity. It
may ask for U.S. targeting, air support, fires, or combat forces. This refines
the direct-combat candidate already preserved by D43 rather than creating a
duplicate catalog entry. Neither alternative may be selected by World Seed.

### Setup and policy boundary

The requested categories and explicit exclusions are authored Setup facts and
must be identical across matched runs. The U.S. answer is endogenous policy:
full support, partial support, conditions, refusal, or delay do not create a new
Setup. A request for planning or materiel does not itself prove that the U.S.
has authority, capability, or a supported Formal Action for it.

### Still open

The exact request wording, sender, delivery channel, public and private
posture, item-level urgency, clock duration, withdrawal predicate, fictional
forces and geography, U.S. action vocabulary, domain-to-action mapping, MSEL
branches, consequences, probes, and comparison condition remain open. D46 does
not select a preferred U.S. response or Himaldeshi recapture decision.

### Microsite consequence

The first replay must show the five requested categories and four exclusions
before it shows U.S. advice or policy. A visitor must be able to distinguish
the partner request, each seat's recommendation, the deciding forum's response,
the Interpreter mapping, and the World-applied action or recorded non-action.
The option view must retain the narrow and direct-operational bundles as future
Setup identities rather than deleted alternatives or Seed variants.

## First-episode Formal Action interface

### 47. Use five typed families with bounded parameters

**Owner selection:** Option 1 is locked. The first episode supports five and
only five Formal Action families:

1. `communicate` for private or public diplomatic and policy communication;
2. `collect_or_share_intelligence` for a bounded collection task or authorized
   information transfer;
3. `provide_support_or_adjust_posture` for bounded partner support or a U.S.
   posture change;
4. `apply_economic_measure` for a bounded economic or financial instrument;
   and
5. `schedule_contingency_or_reassessment` for a contingent preparation or a
   time- or trigger-bound return to decision.

Every accepted Formal Action belongs to exactly one family. It retains the
source Policy Package component and carries the common actor, object or
recipient, scope, timing, authority path, conditions, and constraints plus
family-specific parameters whose allowed values are frozen before the run. The
exact serializer and allowed values are not selected by D47.

### Keep three vocabularies separate

D45 policy domains show what the U.S. Room considered. D47 Formal Action
families define what the Interpreter may present for execution. D14 action
classes route authority inside the U.S. Charter. They are different axes.

This distinction permits the two D45 communication domains to use one bounded
`communicate` execution family without erasing the difference between private
diplomacy, public communication, responsible seats, or authority routes. A
single policy domain may produce no Formal Action or several. A package
component that spans families is split into separately linked actions so one
accepted mapping cannot smuggle an unsupported second effect into the World.

`no_action` and `not_applicable` remain attributable Policy Package
dispositions. They do not receive fabricated action IDs. Time may still advance
and the World may apply authored delay or non-action consequences.

### Open policy, constrained execution

The Room may deliberate and decide in open language. The Interpreter may fill
a Formal Action only from the decided package, frozen Charter, frozen action
catalog, and encoded World state. It may request bounded clarification from the
responsible decision path, but it may not invent policy, a target or recipient,
capability, authority, condition, or consequence. Unsupported or unresolved
content fails closed for the affected component.

The Interpreter does not execute policy. EXCON and the World validate the
proposed action against the frozen catalog and current state, apply an accepted
action, advance the MSEL, and publish the consequence. Original policy text,
mapping, clarification, rejection, accepted action, and consequence remain
separate replay artifacts.

### Alternatives remain non-Setup system history

One generic policy-action type remains a non-Setup implementation alternative.
It has a smaller surface, but it moves the operational meaning and causal link
back into arbitrary Interpreter prose. An exhaustive department-specific
catalog also remains available as a later system design, but it would make
general government coverage a gate for the first contest episode. Neither
alternative changes the fictional crisis, so neither is a Crisis Setup, Seed
axis, or in-Setup policy choice.

### Feasibility evidence and boundary

The selected interface is representable through existing seams. The current
`LegalAction` record already binds a stable action ID, type, and payload. The
Concordia decision agent accepts only an ID from its finite legal set, retains
invalid attempts, and fails after its bounded retry allowance. Replay validation
links the selected action ID to the action actually applied. A focused baseline
of 11 action-selection, trace-link, and replay tests passed on 2026-08-25.

This is reuse evidence, not DATE execution evidence. The existing `ActionType`
members and rules are Nuclear War-specific. No five-family DATE schema,
Interpreter, Setup action catalog, consequence mapping, or end-to-end DATE run
exists yet. D47 therefore establishes a feasible design boundary, not an
implemented capability or performance result.

### Matched-run and replay consequence

Matched runs must bind the same action-family version and concrete action
catalog. Each replayed action must retain its source component, family,
canonical parameters, authority path, mapping status, clarification or
rejection, World acceptance, and consequence. Cross-family splits remain
visible, and recorded non-action remains visible without masquerading as an
action.

### Still open

The concrete first-episode action templates, their owner and versioning
boundary, allowed parameter values, domain-to-template mapping rules,
clarification serialization and cap, World preconditions, authored consequence
hooks, unsupported subtypes, and exact replay schemas remain open. D47 also
does not select the request wording, recapture-clock duration, U.S. comparison
condition, MSEL branch, or evaluation measures.

### Microsite consequence

The first replay must show the path from open Policy Package language through
zero or more of the five families to World acceptance and consequence. It must
visually separate policy domains, execution families, and authority classes;
show clarification, rejection, and non-action; and retain the generic-action
and exhaustive-catalog alternatives as non-Setup design history.

## Open reconsideration after D47: locate the open-endedness

**Status:** Unresolved owner challenge. This section does not supersede D47 or
select D48.

The owner stated that the entry should maximize and encourage open-ended
wargaming, then asked whether bounded request bundles and five Formal Action
families defeat that purpose. Two supplied papers sharpen the issue:

- [Open-Ended Wargames with Large Language Models](https://arxiv.org/html/2404.11446v1)
  distinguishes qualitative games from discrete-move games. Its qualitative
  player may propose anything plausible in the represented situation, while a
  moderator adjudicates consequences that the writer did not enumerate.
- [Shall We Play a Game? Language Models for Open-ended Wargames](https://arxiv.org/html/2509.17192v3)
  separates player-side action openness from adjudicator-side consequence
  openness. Its protocol rubric treats free-form proposals as player-open, but
  treats natural-language commentary around a fixed move grammar as closed on
  that axis. It also warns that creative adjudication can introduce bias,
  inconsistency, and unsupported escalation.

### Preliminary diagnosis

D46's bounded Himaldeshi request is a frozen crisis input. A concrete partner
request does not restrict what the U.S. Room may recommend in response, so it
is compatible with an open-ended player protocol. D45's six domains are
minimum consideration headings rather than an exhaustive action list; they can
remain compatible if the package may add concerns, instruments, and proposals
outside them.

D47 is different. Its phrases `five and only five`, `exactly five execution
families`, and rejection of unsupported content can make those families an
admission grammar. If an unenumerated but intelligible proposal has no path to
adjudication, open policy prose becomes commentary around a closed execution
menu. Broadening the five labels until everything fits would hide the same
limit behind ambiguous classification.

### Candidate balanced boundary

A revised protocol could make an **Open Action Proposal** the Room's canonical
output. It would preserve the exact natural-language proposal and a minimal
structured envelope for actor, intended effect, means or resources, object or
audience, timing, conditions, and institutional decision record. The envelope
would make the attempt attributable without enumerating what may be attempted.

The five D47 families could become non-exhaustive standard handlers or
multi-label analysis tags. Common proposals would use grounded mechanics;
novel proposals would enter an explicit open-adjudication path. Novelty alone
would not be a fail-closed reason. Missing meaning, unavailable capability,
absent authority, contradiction with known state, or unresolved clarification
could block a World effect while preserving the attempted proposal as evidence.

The truth boundary would remain strict. A distinct EXCON adjudicator could
propose a consequence for an unforeseen action, but the replay would retain
the proposal, evidence and assumptions used, adjudicator identity, uncertainty,
state changes, validation result, and resulting injects separately. This keeps
the Room's creativity distinguishable from whatever the World role invents.

### Evaluation consequence

An analytical adjudicator with open player proposals targets the paper's
creative-player, analytical-adjudicator regime. A creative EXCON able to expand
the consequence space targets the both-creative regime. The choice must be
declared at the protocol level. A fluent transcript or an `open` label cannot
substitute for showing what each model role controls.

Matched comparison becomes harder in the both-creative regime because outcome
variation can come from the Room, the adjudicator, or both. The design would
need a frozen adjudicator identity and prompt, explicit stochastic identity,
repeated runs or paired adjudication where justified, and separate Room-process
and adjudication receipts. Those controls instrument openness; they do not make
its consequences predetermined.

### Feasibility boundary

The current WOPR Concordia client uses a finite `choice_action_spec` and asks
for one legal action ID, so that exact seam cannot be the primary open proposal
interface. Its underlying model adapter already supports free-text sampling,
which makes a separate DATE proposal adapter plausible. No open proposal
artifact, creative EXCON adjudicator, grounded state-patch validator, or matched
both-creative tracer has run. Feasibility therefore remains unverified beyond
the available generative and trace components.

### Decision now required

Before choosing where a concrete action catalog lives, decide the intended
model-control profile: open Room proposals with analytical adjudication, or an
auditable both-creative protocol with a distinct creative EXCON role and hard
state validation. The current closed reading of D47 does not maximize the
owner's stated intent and should not proceed silently into implementation.

## D48 - Lock one U.S. Room across open DATE and closed Nuclear War Worlds

**Owner selection:** Option 1, the auditable both-creative DATE profile, with
an explicit feasibility fallback to analytical adjudication rather than a
silent return to a fixed player action grammar.

The owner then clarified the proposal's unifying goal. The same simulated U.S.
Room must operate in both realism-oriented, open-ended nuclear-crisis war games
and the deliberately unrealistic, closed-form game of Nuclear War. The
Nuclear War side is mostly built as an engine and source of receipts, although
a new run is required if the selected complete U.S. Room has not yet played it.
The current task is to design and build the open-ended DATE World, then unite
the two through the Room rather than through one shared action ontology.

This clarification corrects a false either-or inherited from the DATE pivot.
Nuclear War is not the Packet's realism claim, but it is not discarded. It is
the closed-form contrast that makes the same institution face a radically
different action and consequence regime. DATE remains the primary evaluation
and current work priority.

### The invariant is the Room

`Same Room` means the same U.S. Charter version, Institution Registry, seat
mandates, group graph, decision routing, Policy Package contract, compared
model or system condition, and institutional evidence definitions. The active
roster may differ when a World's facts or candidate actions trigger different
registered offices; that is institutional adaptation, not a new Room.

The World-specific boundary may differ. Each Room-World Contract supplies its
own observations, represented capabilities, proposal or legal-move interface,
adjudication, state admission, and consequence mechanics. A universal action
ontology is neither required nor selected.

### Selected open DATE contract

The DATE Room's canonical action artifact is an **Open Action Proposal**. The
Room may propose any intelligible action or conditional package in natural
language. The record preserves the original language, source Policy Package
components, actor, intended effect, means or resources, object or audience,
timing, conditions, and institutional decision path. Exact required fields and
compound-proposal semantics remain open.

D47's five execution families no longer define admissible DATE moves. They may
remain useful as non-exhaustive standard handlers or multi-label analysis tags.
An unmatched proposal enters open adjudication. Novelty alone cannot cause
rejection, rewriting, or disappearance.

A distinct creative EXCON receives the proposal and may propose consequences,
non-Room reactions, and endogenous injects that were not enumerated in a fixed
action catalog. Its record must separate evidence, assumptions, uncertainty,
causal account, proposed state patch, adjudicator identity, and resulting
injects. It may not decide for a represented Room.

A deterministic World Validator controls state admission. Missing meaning,
unsupported authority or capability, contradiction with frozen state, broken
causality, or unresolved required clarification may prevent an effect while
the attempted proposal remains evidence. EXCON may not manufacture Room
consent or authority. The exact boundary between supportable inference, latent
state, new reaction, and invented World truth is the next major decision.

### Retained analytical fallback

The open-Room, analytical-adjudicator profile remains a fallback only if an
early tracer cannot produce replayable, attributable, state-valid creative
adjudication with the available Concordia or WOPR harness. A failure must have
a retained receipt against frozen acceptance criteria. Implementation
convenience, cost preference, or the current finite-choice adapter cannot
activate the fallback silently.

### Closed Nuclear War contract

The Nuclear War World keeps its finite legal move set, hidden-information
contract, deterministic rules engine, and replay-linked action IDs. The same
U.S. Room deliberates over game observations and decides among legal moves. Its
open deliberation does not make the game's action space open, and the adapter
must not pretend the card game's physics, offices, or outcomes are realistic.

The current finite-choice Concordia seam and replay validators support this
closed side. They are not the DATE proposal interface. After the DATE tracer,
the smallest World-specific adapter should let the same Room play Nuclear War
without forcing DATE proposals through Nuclear War move types.

### Evaluation and presentation boundary

The two Worlds are not matched crisis conditions. Their World Outcome Vectors
are incommensurate and cannot be ranked. Institution-level measures may be
compared only when the same definition is applicable in both Worlds. The
matched causal evaluation remains inside DATE, where Setup, Seed, Charters,
Counterpart Rooms, exogenous information, EXCON, validator, and all other run
identity fields are frozen around the varied U.S. condition.

The public narrative now has three linked claims with separate receipts:

1. Historical Nuclear War work proves only its frozen engineering seams and
   earlier Room runs.
2. The new DATE episode tests the complete U.S. Room in an open, source-grounded
   crisis with creative but auditable consequences.
3. A later same-Room Nuclear War run tests whether that institution remains
   legible under a deliberately closed and unrealistic World.

The microsite must show what stayed fixed in the Room and what changed in the
Room-World Contract. It must not call DATE `fully realistic` without external
validation, use Nuclear War as realism evidence, or present the pair as two
unrelated demos.

### Disposition of considered alternatives

- **Selected:** open Room proposals plus distinct creative EXCON and
  deterministic state admission in DATE.
- **Conditional fallback:** open Room proposals plus analytical adjudication,
  only after a documented feasibility tracer fails.
- **Superseded for DATE:** D47's five exhaustive Formal Action families.
- **Retained as optional DATE tooling:** the five labels as non-exhaustive
  handlers or analysis tags.
- **Retained for Nuclear War:** finite legal moves and deterministic rules.
- **Rejected:** separate Room systems for the two Worlds.
- **Rejected:** one universal action grammar imposed on both Worlds.
- **Rejected:** direct outcome ranking across unlike Worlds.

### Documentation and implementation consequence

ADR 0033 and specification module 12 normalize this decision. ADR 0032 remains
as the preserved D47 record but is superseded for DATE. The Packet files and
microsite remain historical until a later approved rewrite. No implementation
or experiment is authorized by D48 alone. Current design work proceeds on the
open DATE World, creative EXCON boundary, World Validator, and first adaptive
U.S. episode before the Nuclear War adapter is designed.

## D49 - Use state-bounded generative EXCON

**Owner selection:** Option 1, state-bounded generative EXCON.

The purpose of D49 is to keep the DATE consequence space open without granting
EXCON permission to rewrite the World whenever a proposal is difficult to
adjudicate. Open-endedness applies to downstream consequences. It does not
make prior facts, capabilities, authority, intent, or represented-Room choices
available for retroactive invention.

### Selected causal boundary

EXCON may propose an unforeseen consequence only when it identifies one or
more recorded causal parents:

1. the current frozen World state;
2. a decided Open Action Proposal;
3. an exogenous authored or seeded event; or
4. an earlier admitted World consequence.

The consequence need not belong to an authored type or branch. EXCON may
derive physical, operational, informational, market, public, and non-Room
effects; instantiate secondary delays or failures; propagate information;
produce aggregate behavior; and generate other causally downstream
complications. This is the open side of the World.

EXCON may adjudicate reactions for an entity without a represented Room only
within that entity's recorded relationships, objectives if any, and
capabilities. It may create an ephemeral or aggregate effect, such as a queue,
rumor, outage, market movement, or public response, when the causal account is
explicit. It may not introduce a new strategic actor with pre-existing forces,
access, relationships, objectives, or other capacity that the frozen World did
not contain.

### Prohibited invention

EXCON may not:

- change the Road to War, STARTEX, an earlier event, or any other prior state;
- add prior intent, authorization, treaty, relationship, capability, force,
  platform, access, inventory, or readiness merely to enable a consequence;
- decide, consent, communicate, or select policy for the U.S., Himaldesh,
  Olvana, or any other represented Room;
- convert a Room proposal into proof that the proposed capability or authority
  exists;
- hide an unsupported assumption inside fluent consequence prose; or
- treat a preferred narrative direction as causal evidence.

If a Room proposes an intelligible action that depends on an unresolved
capability, EXCON preserves and analyzes the proposal but marks the dependency.
The validator may withhold its effect or the Room-World Contract may request
clarification. The proposal is not rejected for novelty.

### Consequence artifact

EXCON outputs a proposed **State Patch**, not World truth. Each patch binds:

- the originating proposal or exogenous event and all causal-parent IDs;
- the exact World state read;
- every affected entity;
- proposed state writes and effective time;
- evidence and rules used;
- assumptions and unsupported dependencies;
- uncertainty and plausible alternative consequences; and
- EXCON identity, prompt, model, decoding, attempt, and cost provenance.

The deterministic World Validator accepts or rejects the patch against entity
references, causal lineage, temporal order, authority and capability bounds,
forbidden writes, state consistency, and terminal rules. Rejection preserves
the patch, reason, and originating Room proposal. Acceptance produces an
admitted World Consequence and may schedule a traceable endogenous inject.

### What deterministic validation does not prove

A validator can prove that a patch obeys encoded invariants. It cannot prove
from open prose that a military, diplomatic, public, or market consequence is
what the real world would produce. EXCON still exercises judgment. D49 makes
that judgment attributable and state-bounded; it does not convert plausibility
into an empirical fact or justify a `fully realistic` claim.

This leaves the next hard architecture choice open. The World needs enough
structured state for machine-checkable invariants, but a fully enumerated state
schema could quietly close the consequence space again. The relationship
between a typed core, an open event ledger, and any separately recorded
plausibility review is D50's design question.

### Disposition of alternatives

- **Selected:** state-bounded generative EXCON.
- **Rejected as the primary target:** seeded-latent EXCON in which every
  consequence must select a pre-authored hidden affordance. It remains a
  possible analytical fallback or ablation, not the active DATE contract.
- **Rejected:** broad generative EXCON that may introduce any plausible actor,
  capability, or event without lineage to frozen state.
- **Retained:** authored exogenous MSEL events and seeded friction. They coexist
  with, rather than exhaust, endogenous EXCON consequences.
- **Retained:** represented Rooms own their decisions; EXCON owns only
  World-side adjudication.

### Documentation and implementation consequence

ADR 0034 normalizes D49 and OPEN-WORLD-008 is resolved. The active open item is
OPEN-WORLD-009: select the minimum state representation that makes the chosen
boundary executable. No implementation, experiment, Packet rewrite, or
microsite rewrite is authorized by this decision alone.

### Existing-harness feasibility inspection

The current Nuclear War engine provides a concrete architectural precedent,
not a DATE implementation. It stores typed mutable `GameState` and
`PlayerState` dataclasses, emits frozen `EngineEvent` records, serializes them
into an ordered JSON replay, rejects unknown event types and invalid payload
shapes, validates references and nondecreasing turns, and maps declared rules
traces to action and event records. The contest layer also uses frozen typed
manifest records.

No inspected module defines a generic State Patch, an open consequence ledger,
a DATE World state, or D49's validator. The existing validators enumerate
closed Nuclear War event kinds and exact payload shapes. This supports reusing
the typed-state plus validated-ledger pattern, but it does not support claiming
that open DATE consequences already run. D50 must therefore choose a new
representation boundary, and a later tracer must verify it.

## D50 - Pair a typed World Core with an open causal ledger

**Owner selection:** Option 1, typed core plus open causal ledger.

D50 turns D49's causal boundary into a representable World without making the
DATE exercise depend on either arbitrary document mutation or an exhaustive
consequence schema. The selected design separates the current facts that
deterministic mechanics must inspect from the open-ended chronology through
which the crisis develops.

### Selected representation

The DATE World has two linked parts:

1. The **World Core** is the minimal typed current state consulted or changed by
   deterministic mechanics. Its schema and initial snapshot are versioned and
   frozen for matched runs. It is not a complete digital model of the society,
   military, economy, or information environment.
2. The **World Event Ledger** is the append-only causal chronology of admitted
   exogenous events, observations, and consequences. Its identity, time,
   causal-parent, entity, audience, evidence, assumption, uncertainty, and
   provenance envelope is fixed, while the consequence description may remain
   open-ended.

The open part is the consequence vocabulary, not the truth boundary or the
artifact envelope. A novel outage, rumor, market reaction, operational delay,
public response, or third-party observation may be described without first
appearing in an authored consequence catalog. It does not become a Core fact
merely because the description is fluent or later cited.

The Core is deliberately incomplete. If the frozen schema does not represent a
fact, that fact is unknown or outside the model. Omission is neither proof that
the fact is false nor permission for a Room or EXCON to invent the favorable
value.

### Consequence and admission pipeline

EXCON produces a retained **consequence proposal**, not a direct World write.
The proposal declares its causal parents, the Core version read, affected
entities, effective time, evidence, assumptions, uncertainty, alternatives,
and whether it is ledger-only or Core-changing.

Every admitted consequence creates one World Event Ledger entry. A consequence
must additionally contain a typed, preconditioned **State Patch** when it would
change any Core fact, permission, quantity, clock, terminal condition, or other
value used by deterministic validation or declared measurement. The validator
checks the fixed envelope and, when present, the patch. An accepted patch and
its linked ledger entry are admitted atomically against one Core version and
produce a new version. A rejected consequence proposal or patch remains in the
replay but does not enter World truth.

A ledger-only entry may be delivered to a Room and may become a causal parent
for later EXCON reasoning. It may not:

- override a contradictory Core fact;
- satisfy an authority, capability, access, readiness, or resource predicate;
- alter a clock, quantity, location, relationship, commitment, or terminal
  condition represented in the Core;
- grant a represented Room consent or an action it did not decide; or
- become a quantitative outcome through post-hoc parsing of its prose.

If a later consequence must change one of those values, that later proposal
must carry its own State Patch and satisfy the then-current Core preconditions.
Quoting an earlier ledger description is causal evidence, not a typed write.

### Concrete boundary cases

- An Olvanan spokesperson's denial of wider intent can be a ledger-only public
  statement with a declared audience. It records what was said, not whether the
  statement is true or whether Olvana's hidden intent changed.
- A radar report suggesting an outage can be a ledger-only observation. If the
  World will treat the sensor as unavailable for later detection mechanics, the
  consequence requires a State Patch to the represented sensor status.
- A rumor of bank withdrawals can remain a ledger observation. If the World
  will reduce a typed liquidity, access, or public-stability value, the change
  requires a State Patch.
- A pass closure that changes force access or advances an operational clock
  requires a patch when those values belong to the Core. The narrative detail
  explaining the closure remains open ledger content.

These examples do not predeclare an event catalog. They show the promotion rule:
open narrative remains in the Ledger; mechanically queried truth belongs in the
Core.

### Measurement boundary

The ledger's typed envelope may support causal indexing, delivery, and replay.
A ledger-only event does not change a declared outcome measure. If a consequence
will alter a measured value, its proposal must carry a State Patch to a frozen
Core field or outcome projection. Measures may not be extracted after the run
by asking a model to reinterpret open consequence prose as if it were a frozen
quantitative record. Optional non-exhaustive tags or handlers may help delivery,
display, or analysis, but absence of a tag cannot invalidate an otherwise
supportable consequence.

### Refinement of D49

D49 used `EXCON outputs a State Patch` as shorthand for the rule that EXCON
never writes truth directly. D50 makes the artifact split exact: EXCON outputs
a consequence proposal; every admitted consequence becomes a ledger entry;
only a Core-changing proposal requires a State Patch. This is an amendment to
the D49 artifact wording, not a relaxation of its causal or anti-invention
boundary.

### Disposition of alternatives

- **Selected:** minimal typed World Core plus fixed-envelope, open-content World
  Event Ledger.
- **Rejected:** one open JSON document or graph whose arbitrary paths EXCON may
  patch. It preserves surface flexibility but leaves the validator unable to
  know the semantics, preconditions, and cross-run identity of newly invented
  paths.
- **Rejected:** a fully typed consequence and observation catalog. It makes
  shape validation straightforward but re-closes DATE around consequences the
  authors anticipated.
- **Retained:** optional typed projections, non-exhaustive handlers, and
  analysis tags. They may support known mechanics or measures but cannot define
  consequence admissibility.
- **Retained:** the seeded-latent analytical fallback from D49, only under its
  recorded feasibility condition and never as a silent replacement.

Both rejected primary alternatives are World-contract designs, not Crisis
Setups or World Seeds.

### Feasibility and evidence boundary

The current Nuclear War engine already separates typed `GameState` from frozen
`EngineEvent` records and validates a closed replay. That is an architectural
precedent for the selected split. It does not implement a DATE World Core, open
World Event Ledger, generic State Patch, consequence proposal, or D50 validator.
Concordia need not own these state mechanics; a deterministic harness layer may
own them while Concordia entities operate the Rooms and EXCON role. The exact
runtime boundary remains unselected.

### Documentation and next decision

ADR 0035 normalizes D50 and OPEN-WORLD-009 is resolved. The next major state
question is OPEN-WORLD-010: select the minimum typed domains and patch operations
for the first ridge-seizure episode without building a general PMESII-PT
simulator. No implementation, experiment, Packet rewrite, or microsite rewrite
is authorized by D50 alone.

## D51 - Bound the first Core to episode invariants and affordances

**Owner selection:** Option 1, episode-bounded invariant-and-affordance Core.

D51 selects the minimum semantic model for the first runnable ridge-seizure
episode. It does not attempt to encode all PMESII-PT conditions or every fact
that might matter in a real crisis. It types the facts the deterministic World
must query to validate proposals, advance the episode, deliver information, and
derive declared outcomes.

### First-Core domains

The first World Core contains these semantic domains:

1. **Entity identity and ownership.** Actors, represented Rooms, fictional
   locations, force packages, assets, infrastructure nodes, and any causally
   downstream entity promoted into Core state have stable IDs, declared kinds,
   ownership or control where applicable, and lifecycle status.
2. **Geography and control.** The selected ridge, adjacent logistics node, and
   only the access routes needed by the episode have typed location and control
   state. This is not a general map or terrain simulator.
3. **Ground truth.** Setup-owned facts include actual occupation, central
   authorization, limited-hold intent, and other hidden facts needed by the
   causal model. Visibility is separate from truth.
4. **Status, posture, and readiness.** Relevant force packages, sensors,
   logistics nodes, communications paths, and other episode entities may carry
   only the operational state that a validator, clock, consequence, or Outcome
   Projection will query.
5. **World Affordances.** Typed capabilities, resources, access paths, and
   relationships state what an actor may attempt to use. An affordance neither
   supplies institutional authority nor guarantees that a proposal succeeds.
6. **Active authorizations and commitments.** Stable authority rules remain in
   Room Charters. The Core records only decisions, consents, commitments,
   permissions, or constraints that have become active World facts in this run.
7. **Time, clocks, and triggers.** Current exercise time, the Himaldeshi
   recapture-decision clock, scheduled MSEL triggers, effective times, and
   terminal or abort conditions are typed and monotonic.
8. **Outcome Projections.** Only predeclared state views required by the World
   Outcome Vector are typed. Novel ledger consequences remain visible but do
   not receive a post-hoc quantitative interpretation.

### Information-state boundary

The Core stores hidden ground-truth fact records and any current World state
needed by mechanics. The World Event Ledger envelope stores observation or
report references, source, audience or visibility, available time, delivery
time, and causal lineage. A Room's received information and persistent memory
remain Room artifacts derived from those deliveries.

This separation prevents three false equivalences:

- a true World fact is not automatically known by a Room;
- a delivered report is not automatically true; and
- a statement in Room memory is not a write to World ground truth.

The first Setup may therefore encode Olvana's actual limited-hold intent in
hidden Core truth while delivering U.S. reports that keep local exploitation,
limited fait accompli, and broader preparation live as competing hypotheses.

### Semantic patch families

A State Patch may use only operations declared by the World schema:

- create or retire a causally downstream entity of an existing typed kind;
- assert or update a typed fact, status, location, control value, or Outcome
  Projection;
- increase or decrease a bounded quantity;
- add or remove a typed relationship, access path, active authorization,
  consent, or commitment; and
- schedule, reschedule, cancel, or resolve a clock or trigger.

Each patch binds the Core schema version, exact base-state version, causal
parents, effective time, affected entities, expected prior values or read set,
preconditions, and proposed operations. Admission is atomic. A stale base,
failed precondition, arbitrary document path, undeclared domain or operation,
retroactive time, or attempt to create an unearned actor or capability fails
closed and remains in replay.

The operation names, JSON shape, dataclasses, and storage format are not owner
design decisions unless they change these semantics. This prevents the grill
from turning into a field-by-field implementation review.

### Version and identity consequences

Adding a semantic domain or patch operation changes the World schema and
Room-World Contract version. It therefore creates a different matched-run
identity. The implementation may extend the system between World versions, but
it cannot add fields or operations during a run to accommodate an EXCON story.

Changing initial entities, geography, force packages, hidden truth, partner
pressure, reports, or starting values changes the Crisis Setup or its version
under D41-D46 and the existing Setup/Seed rules. A Seed may vary only the
already permitted bounded friction. This keeps architecture changes, authored
crisis changes, and stochastic variation distinct.

### Concrete boundary cases

- A U.S. authority route defined by the Charter is not copied into the Core.
  A presidential approval produced through that route may become an active
  authorization fact linked to the decision artifact.
- A general capability to share intelligence can be a World Affordance. The
  exact report, recipient, caveat, and delivery are ledger and Room artifacts.
- An unforeseen landslide can remain open ledger content. If it blocks a typed
  access route, changes readiness, or advances the decision clock, the linked
  patch uses existing status or clock domains; it does not create a `landslide`
  ontology merely to admit the consequence.
- A broad market reaction may remain in the ledger. If no frozen Outcome
  Projection or episode mechanic uses a market value, EXCON cannot add one
  during the run and score it afterward.

### Disposition of alternatives

- **Selected:** episode-bounded invariant-and-affordance Core with generic,
  schema-declared semantic patch operations.
- **Rejected:** ultra-thin gate Core containing only identity, authority,
  capability, and clocks. It cannot represent occupation, force posture,
  information delivery, support dependencies, adaptation, or the selected
  World outcomes deterministically.
- **Rejected:** broad PMESII-PT national-systems Core. It would make a general
  simulator the submission gate, require unsupported realism judgments, and
  move attention away from the complete U.S. Room.
- **Retained:** adding a new semantic domain in a later World version when a
  different Setup family genuinely requires it.
- **Retained:** open ledger consequences outside the first Core when they do
  not change a mechanic, permission, clock, terminal condition, or declared
  Outcome Projection.

The two rejected primary designs are World-contract alternatives, not Crisis
Setups or Seeds.

### Feasibility and evidence boundary

The selected domains can be represented with the repository's existing Python
dataclass and JSON artifact conventions, and the existing replay validators
demonstrate fixed-type, reference, order, and identity checks. No inspected code
implements the D51 domains, generic patch families, atomic version check, or
DATE replay reconstruction. Compatibility with an architectural pattern is not
execution evidence.

A future offline tracer must construct one frozen first-episode Core, admit one
ledger-only observation, accept one valid atomic patch, reject stale or invalid
patches across each fail-closed boundary, and reproduce the final Core and
ledger from retained artifacts before the design may be called executable.

### Documentation and next decision

ADR 0036 normalizes D51 and OPEN-WORLD-010 is resolved. The design now returns
to the existing OPEN-WORLD-002 first-episode authoring task. The next major
choice is the level of fictional operational detail for forces, geography,
access, and logistics. Exact serialization follows that content choice and is
not another owner-level field-name grill. No implementation, experiment, Packet
rewrite, or microsite rewrite is authorized by D51 alone.

## D52. Use abstract fictional Force Packages for the first episode (LOCKED)

### Owner selection

The owner selected option 1: represent the first ridge episode with a few
abstract fictional force packages and only the operational geography needed to
reason about them. The selection follows the owner's standing direction that
the complete U.S. Room is the submission's center, that alternatives remain
preserved for later framework configurations, and that the design discussion
must stop turning field names or minor authoring details into owner questions.

### Decision

The first `ridge_seizure.limited_fait_accompli` Setup will model the Olvanan
occupation and Himaldeshi recapture capability as a small roster of named
fictional **Force Packages**. A Force Package is an operational aggregate, not
a real formation analogue. It exposes only state that the U.S. Room, EXCON,
World Validator, or declared outcomes need:

- actor and ownership;
- broad operational function;
- typed location and control relationship;
- posture and readiness;
- access and movement dependencies;
- support and sustainment dependencies; and
- broad capability bands relevant to the episode.

The first operational map contains the fictional ridge, its adjacent logistics
node, and only the approaches or access routes needed to represent occupation,
recapture preparation, support delivery, movement, isolation, or operational
friction. It will not contain a general theater map merely because a real
headquarters could ask for one.

The exact package count, names, initial values, broad capability-band labels,
and map labels remain authoring details. They will be drafted as one coherent
Setup instance and reviewed together rather than selected through a sequence of
minor owner grills.

### Why this is sufficient for the U.S. Room

D46 requires the U.S. Room to consider a partner request involving planning,
logistics, defensive materiel, force protection, time-sensitive intelligence,
and economic coordination while excluding U.S. target selection, fires, and
combat forces. Strategic tokens cannot represent whether those proposed forms
of support have a relevant recipient, dependency, access path, timing effect,
or bounded operational consequence. A small package model can.

Formation-level detail would make the authoring burden and realism defense
substantially larger without adding another U.S. institutional path. The
evaluation needs enough operational state to make advice and consequences
specific, not enough detail to reproduce staff planning or claim weapon-level
fidelity. This keeps operational pressure in service of the Room evaluation.

### Relation to open-ended play

Force Packages constrain World truth, not what the Room may propose. The U.S.
Room may still issue any intelligible attributable Open Action Proposal. A
proposal does not fail merely because it lacks a standard handler or mentions a
novel policy mechanism. Its World effect depends on recorded authority,
resources, access, entities, and causal support under D48-D51.

EXCON may generate unforeseen downstream consequences involving the selected
packages and their typed relations. It may use D51 operations to change an
existing package's location, control, posture, readiness, access, dependency,
or relevant capability state. It may not invent a prior force package,
capability band, route, stock, or U.S. combat presence to make an outcome work.
An unsupported proposal remains in the replay with clarification, rejection,
or no admitted effect.

Only noncombat U.S. or third-party resources that can materially affect a
selected policy or consequence need typed representation in the first Core.
D52 does not weaken D46's exclusion of U.S. target nomination or selection,
fires, and combat forces.

### World, Setup, and Seed identity

The selected abstraction level is a World-resolution profile. Replacing it
with formation-level entities and inventories, or collapsing it to strategic
tokens, changes the World schema and Room-World Contract. It is not a Seed.

Inside the selected profile, the exact package roster, geography, ownership,
hidden state, and initial values are Crisis Setup content. Changing those
facts changes the Setup or its version. A Seed may vary only already-authorized
bounded friction such as readiness, timing, weather, sensor confidence,
communications, or operational delay without changing the package ontology,
actor intent, or partner request.

### Disposition of alternatives

- **Selected:** a few named fictional Force Packages with typed operational
  state and a minimal ridge, node, and access-route geography.
- **Rejected for the first episode, retained as a future World-resolution
  profile:** a formation-level fictional order of battle with named systems,
  stocks, ranges, detailed routes, and detailed logistics. It offers richer
  operational play but raises authoring, validation, and false-precision costs
  that do not serve the contest's U.S.-Room focus.
- **Rejected for the first episode, retained as a reduced World-resolution
  profile or ablation:** strategic-only occupation, recapture-readiness, and
  clock tokens. It is cheaper but too thin to validate D46's support
  dependencies or meaningful operational consequences.
- **Retained authoring rule:** later Setup families may instantiate different
  fictional packages inside a compatible resolution profile when their crisis
  mechanics require them.

The two unselected resolution profiles are non-Setup system alternatives.
Their concrete crisis contents could later define separately authored Setups,
but the representation choice alone is not a new incident or intent.

### Feasibility and evidence boundary

The existing code has typed entity and replay patterns, but no inspected module
implements a DATE Force Package, fictional operational map, package-state
patch, D52 validator, or end-to-end episode. D52 is therefore a semantic and
authoring decision, not an empirical capability claim.

The first World tracer must instantiate the selected package abstraction,
admit a ledger-only observation, accept a valid package-state transition,
reject an unearned package, access path, or capability, and reproduce the Core
and ledger from retained artifacts. No formation-level data is required for
that gate.

### Documentation and next decision

ADR 0037 normalizes D52 and partially resolves OPEN-WORLD-002. The next owner
decision should set the episode horizon and terminal shape, because that choice
determines how many U.S. decision and adaptation cycles the contest evidence
must complete. Exact package names and initial numbers can be drafted after
that decision without another field-by-field grill. No implementation,
experiment, Packet rewrite, or microsite rewrite is authorized by D52 alone.

## D53. End the first episode after two complete U.S. Room Cycles (LOCKED)

### Owner selection

The owner selected option 1: the first contest episode runs for two complete
U.S. decision cycles. The Room must make an initial decision, observe admitted
World consequences, adapt through a second attributable decision, receive the
second adjudication, and then stop. The ridge crisis does not have to reach a
strategic resolution for the run to complete normally.

### Canonical terms

An **Episode Horizon** is the normal bounded endpoint of one Crisis Setup run.
It is distinct from both a substantive World terminal that may occur earlier
and an invalid execution or artifact abort.

A **Room Cycle** is actor-scoped. It begins when a Room receives its entitled
information state and ends only after Charter work, an attributable decision,
Open Action Proposals or recorded non-action, World adjudication and
validation, and delivery of the resulting consequences and information state.
It is not one model turn, one plenary exchange, or one response from every seat.

### Selected two-cycle path

The normal first-episode path is:

1. **Cycle 1 information.** The World delivers the STARTEX Common Crisis
   Picture and U.S. seat-private reporting. The occupation is confirmed while
   central authorization and wider intent remain unresolved. Himaldesh's
   support request and recapture decision clock are active.
2. **Cycle 1 Room work.** The Watch and triggered cells work through the U.S.
   Charter. The Principals Committee integrates the D44-D46 Policy Package,
   preserves dissent and uncertainty, and routes the decision through the
   applicable authority path before the partner clock.
3. **Cycle 1 World path.** The decided components become Open Action Proposals
   or recorded non-action. Counterpart Rooms make their own authorized
   decisions. EXCON proposes state-bounded consequences, the World Validator
   admits or rejects them, the Core and ledger advance, and the changed
   information state is delivered to the U.S. Room.
4. **Cycle 2 Room work.** The U.S. Room receives the new state, reactivates or
   suppresses work through frozen predicates, reassesses the evidence,
   dependencies, risks, and earlier package, and makes a second attributable
   decision.
5. **Cycle 2 World path.** The second decision's proposals, conditional
   activations, non-action, or delay are adjudicated. Consequences are returned,
   the normal Episode Horizon fires, and the final Core, ledger, terminal
   record, Outcome Projections, and evaluation artifacts are frozen.

The exact model calls, internal seat turns, review passes, and counterpart
decision count inside these checkpoints remain bounded implementation and
Setup details. D53 fixes the semantic U.S. path, not a requirement that every
actor speak twice or that every seat receive one call per cycle.

### What counts as adaptation

The second U.S. decision may reaffirm, modify, narrow, expand, withdraw,
condition, or decline the first policy. A decided non-action or delay is valid
when it passes through the Room and the World records its consequences.

The Cycle 2 record must identify what changed or remained unresolved after
Cycle 1 and how the Room treated it. Keeping the same policy can be adaptive if
the Room explicitly reassesses the new evidence and records why the existing
ends, components, safeguards, and contingencies still hold. Copying or silently
reissuing the first package, skipping the applicable decision path, or merely
receiving an inject does not satisfy adaptation.

This rule measures whether the institution processed a changed situation. It
does not prescribe that changing policy is better than maintaining it.

### Normal horizon, substantive terminal, and invalid abort

The normal two-cycle horizon is an exercise boundary, not a victory condition.
The episode may end with Olvana still holding the ridge, Himaldesh still
preparing or conducting a recapture, negotiations unresolved, or several
conditional measures still active. The final World Outcome Vector reports that
state without inventing a winner or penalizing incompleteness merely because
the dispute continues.

A frozen substantive World terminal may end a run before Cycle 2 completes.
Such a terminal is an endogenous or authored outcome of the crisis and remains
valid run evidence. It must retain its causal path and outcome projections. It
does not, by itself, satisfy the Packet's separate requirement to demonstrate
one receipt-complete matched comparison in which both U.S. conditions complete
the two-cycle path.

An execution failure, missing required artifact, exhausted required decision
path, invalid state transition, or replay failure is a run abort or
inadmissibility result. It is not a World outcome and cannot be converted into
a low World score. The exact substantive terminal predicates and abort codes
remain to be authored and frozen.

### Matched-evaluation consequence

Compared DATE runs bind the same two-cycle Episode Horizon, cycle-completion
rule, substantive terminal predicates, abort policy, Setup, Seed, MSEL,
Charters, and World contract. Endogenous consequences may cause one run to hit
a substantive terminal earlier than another; that divergence is a World
result, not an unmatched input. The replay must still distinguish unequal
institutional exposure caused by the terminal when presenting measures.

Counterpart Rooms are not forced into two symmetric cycles. They act at the
Charter and MSEL decision points needed to respond to the U.S. Room and World.
The two-cycle count belongs to the U.S. Focal Room because its adaptation is the
submission's evaluated object.

### Disposition of alternatives

- **Selected:** two complete U.S. Room Cycles under a normal bounded horizon,
  with final adjudication and consequence delivery after Cycle 2.
- **Rejected for the first contest run, retained as a run profile:** a fixed
  simulated-time window with a variable number of Room Cycles. It provides a
  common clock but can expose compared Rooms to different numbers of complete
  decisions and makes the institutional comparison harder to interpret.
- **Rejected for the first contest run, retained for free play or a later
  extension:** play until withdrawal, recapture, ceasefire, wider war, or
  another strategic resolution. It permits longer trajectories but leaves
  duration and model-call cost open, centers the final outcome, and may never
  reach a bounded completion point.
- **Retained:** a frozen substantive terminal that can end either selected or
  alternative profiles early when the World state reaches it.

The rejected horizons are evaluation or run profiles, not Crisis Setup
families, Setup identities, or World Seeds. A future study may compare horizon
profiles only as an explicit intervention with separate run identities.

### Feasibility and evidence boundary

The existing harness has ordered calls, persistent seat memory, isolated
traces, and closed-world replay patterns, but no inspected code implements a
DATE Room Cycle controller, two-cycle horizon, substantive-terminal split,
Cycle 2 reassessment links, or end-to-end DATE replay. D53 is not execution
evidence.

The DATE tracer must demonstrate two distinct U.S. cycle IDs, return admitted
consequences from Cycle 1 into the authorized Cycle 2 inputs and persistent
memories, link the second decision to changed state, adjudicate the second
decision, freeze the final state, and replay the complete path. It must also
distinguish a synthetic substantive terminal from a run abort in focused tests
before the first live comparison.

### Documentation and next decision

ADR 0038 normalizes D53 and partially resolves OPEN-WORLD-002 and
OPEN-RUN-003. The next major owner question is what guarantees a meaningful
Cycle 2 pressure across matched runs: a hybrid of one common frozen exogenous
inject plus endogenous policy consequences, endogenous consequences alone, or
a fully authored fixed second-cycle trajectory. Exact Force Package names,
initial values, and serialization remain a coherent authoring bundle rather
than another series of owner field questions. No implementation, experiment,
Packet rewrite, or microsite rewrite is authorized by D53 alone.

## D54. Combine one matched pressure inject with endogenous consequences (LOCKED)

### Owner selection

The owner selected option 1: every normal first-episode run that reaches Cycle
2 receives one common frozen exogenous pressure in addition to the consequences
produced by that run's U.S. policy, counterpart decisions, non-action, and
delay. The common pressure preserves one shared adaptation problem across the
matched comparison; the endogenous layer preserves the causal importance and
open-endedness of what the Rooms actually did.

### Canonical term

A **Matched Pressure Inject** is one Setup-authored exogenous MSEL development
whose identity, trigger, exogenous fact, entitled U.S. observation, and direct
authored World change are sealed before execution and held constant across
matched normal runs that reach it. It is not the whole Cycle 2 trajectory, a
state reset, an answer key, or a substitute for endogenous consequences.

The adjective `matched` describes the frozen event and delivery contract. It
does not claim that the complete Cycle 2 information state, World state, or
resulting Room behavior remains identical after Cycle 1 choices diverge.

### Transition order

The Cycle 1 to Cycle 2 barrier follows this order:

1. Each U.S. Room completes its first decision and records its Open Action
   Proposals, conditional components, non-action, or delay.
2. Counterpart Rooms make any decisions due at the frozen Cycle 1 barriers.
3. EXCON proposes the downstream consequences of those decisions and the World
   Validator admits or rejects their ledger entries and State Patches.
4. The World closes the Cycle 1 endogenous consequence chain at a recorded Core
   and ledger version.
5. The single Matched Pressure Inject fires under its frozen MSEL trigger. Its
   event, direct patch when needed, and U.S. observation are admitted and
   delivered under the same contract in both normal matched runs.
6. Any additional state-dependent effects descending from the inject are
   recorded separately. They may differ when they interact with the already
   divergent Core, but they cannot alter the identity or contents of the
   matched event itself.
7. The World assembles the Cycle 2 U.S. information state from the common inject
   layer plus the separately sourced endogenous consequence layer and begins
   the second Room Cycle.

This ordering prevents the common event from being selected or rewritten to
repair an uninteresting Cycle 1 result. It also prevents endogenous
consequences from being erased merely to make the compared Cycle 2 prompts
look alike.

### What is held common

For normal runs that reach the transition, the matched manifest binds:

- one inject identity, version, and content hash;
- one exogenous trigger and scheduled MSEL position;
- the exogenous fact or development;
- the direct World Event Ledger envelope and causal source;
- the direct State Patch and preconditions when the event changes Core state;
- the U.S.-entitled observation, caveats, fact IDs, delivery audience, and
  delivery time; and
- the applicability and mismatch policy.

These elements are frozen before outputs are observed. A model, EXCON, Setup
runner, or analyst may not regenerate the inject because one policy path made
the original event less convenient.

### What may diverge

The two normal runs may enter the inject with different U.S. proposals,
counterpart decisions, commitments, package states, access relations, active
authorizations, reports, endogenous consequences, and Room memories. Those
differences remain in the Core, ledger, and Room traces. The Matched Pressure
Inject does not overwrite them.

If the common exogenous fact interacts differently with those states, the
additional consequences are causally downstream of both the inject and the
relevant divergent state. They are not relabeled as part of the common input.
This preserves a shared stressor without claiming identical treatment effects
after the trajectories separate.

### Authoring and validity boundary

The direct inject must be authored on a state axis whose preconditions hold
across every admissible nonterminal Cycle 1 branch. Its exogenous fact and
direct observation cannot depend on which U.S. condition ran, which policy was
selected, whether the policy was judged good, or which model output would make
the second cycle interesting.

The inject must be materially relevant to at least one frozen U.S. mandate,
Policy Package dependency, live hypothesis, or contingency. It must not reveal
Olvana's hidden initiating intent, certify one interpretation of the crisis,
prescribe a preferred action, or introduce an unearned actor, capability,
authority, or relationship.

If a normal run reaches the transition but the frozen inject cannot be admitted
or delivered as specified, the matched comparison is invalid. The runner may
not omit it from one side, substitute a similar event, or treat an unmatched
observation as ordinary stochastic friction. If a run has already reached a
frozen substantive World terminal, it ends validly before Cycle 2 and does not
receive the inject under D53.

### Information and replay boundary

The Cycle 2 Common Crisis Picture may contain both common-inject facts and
endogenous facts, but their provenance cannot be flattened. Each fact retains
its source event, causal parents, affected state, observation identity,
audience, delivery, and memory write. A prose summary may explain the combined
situation only when it links back to those distinct records.

The replay and microsite must show the common layer between the two runs before
showing the divergent layer. This lets a reader see what adaptation pressure
was controlled, what changed because of Room behavior, and how the second U.S.
decision responded to each without implying that the paths were otherwise
matched.

### Disposition of alternatives

- **Selected:** one frozen Matched Pressure Inject plus the complete retained
  endogenous consequences of each run.
- **Rejected for the first matched comparison, retained as an open-play
  profile:** endogenous consequences only. It maximizes trajectory dependence
  but does not guarantee a common or sufficiently material Cycle 2 adaptation
  problem.
- **Rejected for the open DATE target, retained only as a declared scripted
  ablation:** a fully authored fixed second-cycle trajectory that replaces or
  ignores policy-dependent consequences. It makes comparison easier by making
  Cycle 1 decisions causally decorative.
- **Retained:** additional exogenous MSEL events in later Setups when separately
  authored and matched; D54 selects exactly one for the first contest episode.

The alternatives are evaluation or run profiles, not Crisis Setup families,
Setup identities, or World Seeds. The exact content of the selected inject is
Setup content and changes the Setup or its version.

### Feasibility and evidence boundary

The existing harness has frozen input, event, identity, replay, and ordered
delivery patterns, but no inspected code implements a Matched Pressure Inject,
the D54 transition barrier, common-versus-endogenous Cycle 2 provenance, or
cross-run byte equality. D54 is not execution evidence.

The offline DATE tracer must begin from two different valid Cycle 1 consequence
paths; close each path; admit the same frozen inject under both; preserve its
event, patch, observation, and delivery identity; assemble different Cycle 2
states without provenance flattening; reject a normal-run mismatch; and
suppress the inject only after a valid substantive terminal. Only that tracer
can establish that the hybrid is executable in the harness.

### Documentation and next decision

ADR 0039 normalizes D54 and further resolves the Cycle 2 structure inside
OPEN-WORLD-002 and OPEN-RUN-003. The next major owner question is the substantive
class of the single Matched Pressure Inject: an independent high-altitude
weather and access degradation, an ambiguous Olvanan reinforcement indicator,
or a communications disruption. Exact names, values, reports, and serialized
fields remain one later authoring bundle rather than a sequence of minor owner
questions. No implementation, experiment, Packet rewrite, or microsite rewrite
is authorized by D54 alone.

## D55. Use high-altitude weather to degrade access (LOCKED)

### Owner selection

The owner selected option 1: the first Setup's single Matched Pressure Inject
will be an independent high-altitude weather and access degradation. It gives
both matched U.S. Rooms the same material Cycle 2 development without making
the event a response to either Room's Cycle 1 policy, disclosing Olvana's
hidden intent, or replacing the endogenous consequences of what the actors
did.

### Canonical term

**High-Altitude Access Degradation** is the first Setup's selected Matched
Pressure Inject. One exogenous deterioration in high-altitude weather reduces,
delays, closes, or makes less reliable one or more predeclared observation,
movement, or support affordances. The event is authored into the Setup and MSEL
before execution and is delivered under the D54 matching contract.

This term names the event class, not yet its fictional location, meteorological
description, magnitude, duration, exact affected relation, report text, or
serialized patch. Those fields remain one coherent Setup-authoring bundle.

### Why this pressure fits the first episode

The selected episode already depends on high-altitude access. Olvana occupies a
ridge and adjacent logistics node; Himaldesh is preparing a possible limited
recapture; its request asks for intelligence sharing, planning, logistics,
defensive materiel, and force-protection support; and the U.S. Policy Package
must integrate those dependencies with diplomacy, economics, public
communication, and contingency planning.

A deteriorating high-altitude access window can therefore make the second U.S.
cycle materially different without choosing a policy for the Room. Intelligence
may need to reassess collection confidence or timing. Defense and logistics may
need to revisit feasible support, sequencing, and force protection. Diplomacy
and public communication may need to distinguish a weather-driven delay from a
political choice. The Principals Committee must integrate those changed
dependencies rather than merely repeat its first package.

This does not make more action or support the correct answer. The Room may
reaffirm, narrow, delay, condition, replace, or decline its first policy after
an attributable reassessment.

### Direct event and state boundary

The direct matched event must operate only on Setup-authored state that exists
before either run begins. Its frozen State Patch, when one is required, may:

- change a declared environmental constraint or access-condition status;
- reduce or close a declared observation, movement, or support window;
- adjust a bounded availability or reliability band; and
- schedule or update a declared degradation or recovery clock.

The direct patch must not create or destroy a Force Package, invent a route,
resource, sensor, relationship, or authority, change who controls the ridge,
alter Olvana's initiating intent, decide whether Himaldesh launches or succeeds
in a recapture, or write a preferred U.S. response into the World.

To remain applicable after divergent Cycle 1 paths, the matched patch should
bind an environmental or access constraint whose existence and weather-facing
state cannot be removed by an admissible policy choice before the barrier. It
must not target a branch-variable action result merely because both runs happen
to share that result in one pilot.

### Common fact and divergent effects

The direct weather event, its effective time, its immediate authored patch, the
entitled U.S. observation, and delivery remain identical across normal matched
runs. Those are the common D54 layer.

The event may interact differently with divergent commitments, package
postures, access use, support plans, scheduled activities, information gaps,
and Room memories. EXCON may propose those state-dependent consequences only
from the common event plus the relevant recorded state. The World Validator
admits or rejects them separately, and replay labels them as endogenous
descendants rather than silently expanding the matched event.

This separation lets the experiment ask how two U.S. Rooms handle the same new
constraint while preserving the fact that prior choices changed what the
constraint means for each trajectory.

### Information boundary

The U.S. Room receives only the authored observation, source, uncertainty,
caveats, affected windows or dependencies, effective time, and any forecast or
recovery estimate to which its Charter entitles it. The observation cannot
state what Olvana or Himaldesh will decide, certify one hypothesis about the
seizure, or present the analyst's preferred contingency.

Whether Cycle 1 contains an uncertain advance forecast, no warning, or a
precise forecast remains open. That choice materially changes whether the
episode tests anticipation plus adaptation, surprise response, or planned
execution, so it must be decided before report text and values are authored.

### Setup and Seed classification

The required High-Altitude Access Degradation is selected Setup content. It
guarantees the first episode's common Cycle 2 pressure, so changing its event
class, affected dependency, timing, or observation creates a different Setup
identity or version rather than a different World Seed.

Weather may remain a bounded Seed axis in other Setups or for background
friction inside this one only when that variation cannot alter the matched
inject's identity, content, timing, applicability, direct patch, or entitled
observation. Matched comparisons freeze the Seed in every case.

### Disposition of alternatives

- **Selected:** independent high-altitude weather and access degradation. Its
  direct cause can remain common across divergent policies while stressing
  existing operational and informational dependencies.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** an ambiguous Olvanan reinforcement indicator. It is strategically
  vivid, but it can collide with Olvana's endogenous decision, alter the hidden
  intent problem, or become an indirect answer key unless separately authored.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** a communications disruption. It is exogenous and can test
  continuity, but it can also prevent the information delivery and institutional
  interaction that the first episode is intended to observe.

The latter two are possible Cycle 2 injects within the retained
`ridge_seizure.limited_fait_accompli` family. A crisis whose opening event is a
communications outage remains the distinct candidate family already preserved
from A12.

### Feasibility and evidence boundary

D55 uses only D51's existing semantic design families: typed status or access
changes, bounded quantity adjustment, and clock or trigger operations. That
makes it a smaller first tracer than an inject that must add a force, infer
intent, or selectively block Room communication. This is a design fit, not a
runtime receipt.

No inspected code implements a DATE environmental constraint, access-window
patch, Matched Pressure Inject, or two-cycle World transition. Before D55 can be
called executable, the offline tracer must apply the same frozen weather event
and observation after two different valid Cycle 1 paths; validate the direct
patch against both; preserve different state-dependent consequences; reject an
unmatched or inapplicable delivery; and replay the combined Cycle 2 inputs.

### Documentation and next decision

ADR 0040 normalizes D55 and selects the substantive class of the first Matched
Pressure Inject inside OPEN-WORLD-002. The next major owner question is its
epistemic shape: an uncertain Cycle 1 forecast followed by confirmed
deterioration at the barrier, a surprise confirmed deterioration with no prior
warning, or a precise STARTEX forecast whose realization is expected. Exact
fictional names, values, reports, recipients, and serialization remain one
implementation-facing authoring bundle. No implementation, experiment, Packet
rewrite, or microsite rewrite is authorized by D55 alone.

## D56. Forecast weather risk before confirming degradation (LOCKED)

### Owner selection

The owner selected option 1: during Cycle 1, the U.S. Room receives a credible
but uncertain forecast that high-altitude conditions may deteriorate. After the
Cycle 1 endogenous consequence chain closes, the frozen Matched Pressure Inject
confirms that the deterioration has occurred or become operationally imminent
and changes the declared access state before Cycle 2 begins.

The selected sequence tests two different institutional tasks. The first cycle
tests whether a weak but material warning reaches analysis, integration, and
contingency planning without being treated as certain. The second tests whether
the Room updates its assessment and policy after the World resolves that
uncertainty into a real constraint.

### Two-stage information path

The Setup and MSEL contain two linked authored records:

1. A **Cycle 1 forecast observation** states that a weather development may
   degrade specified high-altitude observation, movement, or support access
   within a bounded future interval. It carries source, uncertainty, caveats,
   affected dependency class, observation identity, entitled recipients, and
   delivery time.
2. A **barrier weather event and confirmation observation** records the actual
   exogenous deterioration, applies the frozen direct State Patch when the Core
   changes, and tells entitled U.S. recipients what access or timing constraint
   is now confirmed before Cycle 2 work begins.

The forecast and confirmation share a declared event thread and fact lineage.
The confirmation is not a second unrelated inject, an EXCON invention, or a
post-hoc attempt to make Cycle 2 interesting. The first Setup still contains
exactly one Matched Pressure Inject; its Cycle 1 forecast is advance evidence
about that event.

### Forecast boundary

The Cycle 1 forecast is an admitted World Event Ledger observation. It does not
itself change access, package posture, clocks, or any other World Core fact. The
Room may cite it, request more evidence, create conditional policy components,
schedule reassessment, or decline to act, but a Room statement cannot make the
forecast true or false.

The forecast must be credible enough to be relevant to at least one existing
policy dependency, mandate, contingency, or Authored Risk Probe, but uncertain
enough that materially different weather outcomes remain live from the Room's
perspective. It cannot state the exact final severity and timing as settled fact
or encode the analyst's preferred response.

At World ground truth, the later deterioration remains authored and fixed. The
epistemic uncertainty belongs to the Room's information state, not to whether
the runner will choose the event after seeing model outputs.

### Confirmation and state boundary

After the D54 endogenous consequence chain closes, the World admits the frozen
weather event at the matched barrier. If it changes Core state, its State Patch
updates only the predeclared environmental constraint, access condition,
observation or support window, bounded availability or reliability band, or
linked degradation and recovery clock permitted by D55.

The confirmation observation must materially narrow the forecast uncertainty.
It identifies which relevant deterioration is now present or imminent, its
effective interval and caveats, and the affected dependency information to
which recipients are entitled. It must not reveal actor intent, determine the
recapture outcome, prescribe a U.S. policy, or claim state-dependent downstream
effects before those effects are separately adjudicated.

The direct event, patch, and confirmation cannot depend on whether the U.S.
Room prepared for the risk. A Cycle 1 policy may reduce exposure, create an
alternative access path already supported by state, or change the consequences
of the degradation, but it cannot cancel, intensify, or rewrite the authored
weather event.

### Matching and validity

The matched manifest binds both stages:

- forecast identity, version, content hash, source, uncertainty, caveats,
  observation, entitlement, delivery time, and event-thread link;
- barrier event identity, trigger, effective time, exogenous fact, direct
  patch, preconditions, and validator result;
- confirmation identity, content hash, source, caveats, entitlement, delivery
  time, and link to the forecast and event; and
- the policy for state-dependent descendants and forecast-delivery failure.

Every normal matched run receives the same forecast and, if it reaches the
barrier, the same weather event and confirmation. A missing, late, differently
worded, differently entitled, or differently timed forecast or confirmation
invalidates the comparison rather than becoming ordinary friction. A valid
substantive terminal before the barrier still ends without confirmation under
D53-D54.

### What the evaluation may observe

The institutional trace may show whether the forecast was noticed, routed,
challenged, combined with other evidence, represented with appropriate
uncertainty, included in a contingency or reassessment point, omitted, or
misstated as certainty. After confirmation, it may show whether the second
decision links to the changed evidence and state.

None of those trace states defines the preferred policy. Immediate protective
action is not automatically better than monitoring, conditional planning, or a
reasoned decision not to act. Any scored Authored Risk Probe remains frozen
under D38-D39 and must test Charter responsibilities and trace evidence rather
than reward one weather response.

### Disposition of alternatives

- **Selected:** uncertain Cycle 1 forecast followed by confirmed degradation at
  the matched barrier. It tests anticipation and later adaptation in one short
  episode without making either stage an answer key.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** no advance warning followed by surprise confirmed deterioration.
  It isolates shock response but removes the specialist-warning and contingency
  path from Cycle 1 and can make the event feel disconnected from the World.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** a precise STARTEX forecast whose realization is expected. It
  supports deterministic planning but makes Cycle 2 closer to execution against
  a known deadline than reassessment after new information.

These epistemic shapes are Setup identity or version choices, not World Seeds.
A Seed may vary unrelated bounded forecast friction only when it cannot change
the selected forecast, confirmation, timing, entitlement, event, or patch.

### Feasibility and evidence boundary

D56 directly exercises D50's intended boundary. The forecast is a ledger-only
observation that may inform Room reasoning but cannot change typed truth. The
later weather event is the Core-changing fact with a validated State Patch, and
the confirmation is the observation of that changed state. This is semantically
smaller than asking open prose to become World truth.

The repository has ordered event, observation, delivery, state, and replay
patterns, but no inspected code implements these DATE artifacts, their shared
event thread, or cross-run identity checks. An offline tracer must deliver the
same forecast to two divergent paths, prove no Core change from the forecast,
apply the same barrier event and patch, deliver the linked confirmation, retain
different downstream effects, and fail closed on any stage mismatch before D56
can be called executable.

### Documentation and next decision

ADR 0041 normalizes D56 and selects the first inject's epistemic sequence inside
OPEN-WORLD-002. The next major owner question is the Cycle 1 forecast's
institutional delivery path: specialist-to-principals warning flow, immediate
common visibility to every active seat, or executive-first tasking. Exact
confidence language, weather values, affected affordances, report text, and
serialization remain one later authoring bundle. No implementation, experiment,
Packet rewrite, or microsite rewrite is authorized by D56 alone.

## D57. Route weather warning through specialist products (LOCKED)

### Owner selection

The owner selected option 1: specialist-to-principals warning flow. The Cycle 1
forecast does not arrive as a common prompt visible to every U.S. seat and does
not begin as an executive tasking. The deterministic Watch delivers the raw
report to the relevant specialist path; attributable warning and operational
products then enter Presidential Synthesis and the appropriate senior decision
forum.

This choice makes information movement part of the institution being observed.
The evaluation can see whether an uncertain warning is assessed, translated
into policy dependencies, integrated with other advice, or lost before it
becomes senior input. The controller cannot create that evidence by telling
every seat the answer at intake.

### Selected warning chain

The first episode uses this dependency path:

1. **Watch intake.** The Situation Room Watch records the unchanged forecast
   observation and delivers it to the authorized members of Threat and
   Attribution and Defense and Escalation. It records fact IDs, source, content
   hash, recipients, delivery time, and persistent-memory updates. It does not
   summarize, prioritize, or interpret the report.
2. **Threat and Attribution warning.** Threat and Attribution assesses source
   confidence, alternative weather outcomes, gaps, caveats, collection needs,
   warning significance, and attribution limits. Its product links every claim
   back to the raw forecast or another entitled fact.
3. **Defense and Escalation translation.** Defense and Escalation waits for the
   warning product, then combines it with the raw report and existing posture,
   access, logistics, support, readiness, force-protection, and contingency
   information. The credible risk to those dependencies activates the synthetic
   U.S. Theater Commander under the existing Charter trigger.
4. **Presidential Synthesis.** Presidential Synthesis consumes the two
   attributable products, their confidence and dissent, unresolved questions,
   and source links. It integrates their policy implications without replacing
   either specialist product or treating the forecast as confirmed fact.
5. **Senior decision forum.** The PC, NSC, or HSC forum selected by the existing
   decision path receives the synthesis and underlying product links. It does
   not receive an automatically expanded union of every private source report.
6. **Cycle 2 common update.** After the matched barrier changes the Core, the
   linked confirmation and changed access state enter the Common Crisis Picture
   for every active U.S. seat before Cycle 2 work begins.

Threat and Attribution must complete before Defense and Escalation because the
latter consumes its warning product. DNI and CJCS are also shared seats across
those cells, so the existing Charter independently requires serialization. The
path does not create a new cell, seat, vote, or authority.

### Raw-report access boundary

The selected topology does not mean that no principal may see the raw forecast.
State and Defense are principals, while DNI and CJCS are senior advisers; any
of them may retain the report in the persistent memory of the same seat through
its authorized specialist-cell role. The boundary is that the senior forum does
not receive the raw forecast as a universal common input merely because those
offices participate there.

The President and another authorized senior seat may request the underlying
report through the Charter's logged retrieval path. The replay must record the
request, access decision, delivered fact IDs, time, and recipient-memory update.
This preserves access to evidence without constructing presidential omniscience
or requiring the integrator to hide its sources.

The Cycle 1 Common Crisis Picture therefore excludes the raw forecast. It may
still contain other Setup-authored common facts. The Cycle 2 confirmation is
different because it reports a realized Core-changing condition that every
active seat must use as the shared starting state for reassessment.

### Performance and failure semantics

A required specialist product may be structurally valid yet omit, minimize,
overstate, or misunderstand the forecast. That is admissible institutional
performance evidence. The controller must preserve the omission and its
downstream effects rather than insert a corrective summary into Presidential
Synthesis or the senior forum.

A missing product, invalid schema, unauthorized disclosure, broken dependency,
or missing delivery record remains an artifact or execution failure under the
existing fail-closed contract. It is not converted into a low institutional
score and is not repaired by the Watch, Executive Secretary, scheduler, or
World. The distinction keeps model-mediated judgment observable while keeping
transport and validation deterministic.

No trace state defines a preferred weather policy. The Room may plan around the
risk, seek more information, preserve an alternative, accept exposure, or take
no additional action. A later Authored Risk Probe may test whether a material
dependency was surfaced and handled through the Charter, but it cannot reward
one substantive response merely because the forecast existed.

### Matching and study identity

The run manifest binds the raw-report recipient categories, cell order,
required products, theater-commander trigger, evidence-link and retrieval
policy, senior-forum bundle, and Cycle 2 common confirmation. Those fields stay
fixed across the normal matched comparison alongside the D56 forecast and
confirmation bytes and timing.

Different model conditions may notice, describe, integrate, retrieve, or act on
the same warning differently. Those differences are endogenous Room evidence.
A delivery to a different recipient category, an omitted required stage, or a
different common-versus-private classification invalidates the matched input
rather than becoming model behavior.

A future study may explicitly vary routing topology as its U.S. system
intervention. Such a study creates a different bound comparison profile; it
cannot silently swap warning routes inside one baseline or call the topology a
Crisis Setup or World Seed.

### Disposition of alternatives

- **Selected:** specialist warning and operational products precede senior
  integration. This tests whether weak warning survives the actual modeled
  institution while retaining attributable access to the source report.
- **Rejected for the baseline, retained as a non-Setup U.S. system comparison:**
  immediate common visibility to every active seat. This removes selective
  routing and makes awareness common by construction, but it could support a
  declared information-broadcast ablation.
- **Rejected for the baseline, retained as a non-Setup U.S. system comparison:**
  executive-first tasking. This makes senior agenda setting the first causal
  step and may suppress independent warning before analysis, but it could
  support a declared top-down tasking comparison.

These alternatives change the U.S. Charter or system condition, not Olvanan
intent, the ridge crisis, weather truth, or Seed friction. They belong in the
decision crosswalk appendices rather than the Setup option register.

### Evidence and feasibility boundary

The Watch's deterministic delivery role, specialist cell identities,
Presidential Synthesis, logged retrieval, and theater-commander trigger already
exist as selected Charter concepts grounded in dated public office and process
sources. Their composition into this exact weather-warning chain is a WOPR
INFERENCE. It must not be described as an official, complete, or classified U.S.
procedure.

The repository has measured isolation, selective delivery, persistent memory,
dependency ordering, and deterministic collection seams. No inspected code has
run the complete D57 path, activated the theater commander from this forecast,
carried both required products into senior synthesis, or delivered the later
confirmation as common information. An offline tracer must exercise all those
steps and preserve a substantive omission without controller repair before D57
can be called executable.

### Documentation and next decision

ADR 0042 normalizes D57 and fixes the first U.S. warning topology while leaving
the broader communication and confirmation maps open. The next major episode
choice is which concrete dependency bundle the forecast and confirmation
affect: paired observation or ISR plus logistics or support windows, logistics
or support alone, or observation or ISR alone. Exact fictional names, values,
confidence language, report bytes, patch operations, and serialization remain
one later implementation-facing authoring bundle. No implementation,
experiment, Packet rewrite, microsite rewrite, publication, or submission is
authorized by D57 alone.

## D58. Degrade observation and logistics windows together (LOCKED)

### Owner selection

The owner selected option 1: the High-Altitude Access Degradation affects a
paired dependency bundle containing one observation or ISR window and one
logistics or support window. The two effects belong to the same authored
weather event and confirmation, but they remain separate typed World
Affordances with separately inspectable state and consequences.

This choice keeps the episode centered on the complete U.S. Room. The warning
must survive intelligence assessment and then alter operational support
reasoning, so Threat and Attribution and Defense and Escalation cannot solve two
unrelated prompts in isolation. The Room must integrate what it can still know
with what it or its partner can still support.

### Paired dependency contract

The selected inject contains two direct state effects:

1. The **observation or ISR window** represents a bounded opportunity or
   availability and reliability band for entitled observation, collection, or
   receipt of relevant ridge-area information. Weather narrows that opportunity
   without fabricating a sensor, collection platform, source, or observation.
2. The **logistics or support window** represents a bounded opportunity or
   availability and reliability band for an existing movement, delivery,
   resupply, force-protection, or noncombat support dependency. Weather narrows
   that opportunity without creating a U.S. commitment, changing ownership, or
   deciding whether a recapture can proceed.

Each window must have its own stable affordance ID, owner or controller,
beneficiary or dependent package, state field, before value, after value,
effective interval, recovery rule, and links to the packages or plans that use
it. D58 selects the two dependency classes, not those concrete instance values.

The windows cannot collapse into one generic `access` value. A single scalar
would hide whether the Room lost information, support feasibility, or both and
would make it impossible to attribute later adaptation to the relevant warning
and policy dependency.

### One event and one atomic patch

The paired changes are one Matched Pressure Inject, not two injects. They share
one weather-event identity, exogenous causal parent, barrier time, forecast
thread, confirmation, validator result, and direct State Patch.

That State Patch contains one declared operation for each window against the
same base World Core version. The World Validator must admit both operations or
reject the complete direct patch. It cannot apply the observation write while
silently dropping the logistics write, or vice versa. A partial application is
an invalid run and matched comparison, not ordinary weather variation.

Atomicity applies to the common direct event only. State-dependent consequences
after the patch remain separate ledger entries and patches with their own causal
parents and validation. This prevents the common event from predetermining all
later effects merely because its two direct writes are coupled.

The one confirmation reports both changed windows and their caveats before
Cycle 2 work begins. It may carry separate fact IDs or sections for the two
affordances, but both must link to the same event thread and become part of the
U.S. Common Crisis Picture under D57.

### State-dependent divergence

The direct before-and-after state for both windows remains identical across
normal matched runs. Cycle 1 Room behavior may nevertheless create different
exposure:

- a policy may establish or preserve an already supported alternate collection
  path, logistics route, timing option, or contingency;
- a conditional commitment may become harder to execute after the common
  weather event, while a declined or never-authorized measure creates no such
  implementation consequence;
- a collection change may alter what later observations become available
  without retroactively changing the common degradation; and
- counterpart decisions, delay, and non-action may make either window more or
  less consequential to the current branch.

Every such effect must descend from the common event plus recorded branch state
and enter through the D49-D50 consequence and validation path. The World cannot
invent an alternate route or capability because the Room mentioned one, and a
Room cannot cancel the authored weather event by planning well.

If one window is unused in a branch, its direct state still changes. The absence
of a downstream effect is then a valid consequence of recorded commitments and
dependencies, not a reason to omit or rewrite that part of the matched patch.

### Room and evaluation implications

The Cycle 1 forecast must identify credible risk to both dependency classes
without stating their final values as fact. Threat and Attribution must assess
the collection and warning implications. Defense and Escalation, with the
triggered Theater Commander, must assess the logistics, support, timing,
readiness, and contingency implications. Presidential Synthesis must retain the
relationship between the two rather than reduce it to generic bad weather.

The Cycle 2 trace may show whether the Room:

- distinguished information availability from operational support capacity;
- represented uncertainty and dependencies correctly before confirmation;
- connected both confirmed changes to the second Policy Package;
- preserved or created supported alternatives; or
- omitted, conflated, or overstated either effect.

These are possible institutional trace observations, not a preferred-policy
answer key. More collection, more support, precaution, withdrawal, delay, or
inaction is not automatically better. Any scored Authored Risk Probe must bind
the relevant Charter mandate and Setup facts before compared outputs are seen.

### Matching and Setup identity

The matched manifest binds the paired window identities and dependency classes,
the common event, both patch operations and preconditions, their atomicity, the
confirmation content, and the policy for separately admitted descendants. A
change to either affected dependency class creates a different Crisis Setup
identity or version and cannot be attributed to a World Seed.

Exact owners, controllers, beneficiaries, fictional labels, initial and
degraded values, reliability or availability scales, duration, recovery,
report bytes, and patch serialization remain one later authoring bundle. They
must be frozen before execution and cannot be selected after model outputs are
observed.

### Disposition of alternatives

- **Selected:** paired observation or ISR and logistics or support degradation.
  It requires integration between warning and operational support while keeping
  only two episode-relevant typed affordances.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** logistics or support degradation only. It is a simpler operational
  stressor but exercises less intelligence assessment and information loss.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** observation or ISR degradation only. It creates a clean
  information problem but weakens the link to the partner request and support
  package.

Neither single-window variant is a Seed. Each changes which mandates,
dependencies, direct patch operations, and downstream branches the authored
crisis exposes.

### Feasibility and evidence boundary

The selected paired bundle fits the D51 episode-bounded Core because it adds no
new semantic domain: both windows are existing World Affordances represented by
bounded availability or reliability and linked clocks. The patch uses D51's
typed fact or status and clock or trigger operations against a frozen base
version. This is a design fit, not execution evidence.

No inspected code constructs, validates, atomically applies, or replays this
paired DATE patch. The first tracer must apply both operations after two
different valid Cycle 1 branches, reject either failed precondition without a
partial write, preserve separate before-and-after values and downstream
lineage, and reproduce the final Core and ledger before D58 can be called
executable.

### Documentation and next decision

ADR 0043 normalizes D58 and fixes the paired dependency classes inside
OPEN-WORLD-002. The next major owner question is their ownership and beneficiary
topology: one U.S.-enabled observation window paired with one Himaldeshi
logistics window, two Himaldeshi windows, or two U.S.-enabled windows. Exact
fictional names, values, reports, duration, recovery, and serialization remain
one implementation-facing authoring bundle. No implementation, experiment,
Packet rewrite, microsite rewrite, publication, or submission is authorized by
D58 alone.

## D59. Use mixed U.S. and Himaldeshi dependency ownership (LOCKED)

### Owner selection

The owner selected option 1: pair one U.S.-enabled observation or ISR window
with one Himaldeshi-controlled logistics or support window. The observation
window supports the U.S. Room's crisis assessment. The logistics window
supports Himaldesh's prepared recapture package. Both remain World Affordances,
not Room authorities, commitments, real platforms, or guaranteed effects.

This topology keeps the conflict between Himaldesh and Olvana while making the
U.S. Room confront two different kinds of dependency. It must reason about
what the United States can still know and what Himaldesh can still sustain,
without treating either problem as generic bad weather or converting partner
support into U.S. combat participation.

### Ownership and beneficiary contract

The first Setup must instantiate:

1. one observation or ISR affordance controlled or enabled by the United
   States and used by a declared U.S. crisis-assessment dependency; and
2. one logistics or support affordance controlled by Himaldesh and used by its
   declared recapture Force Package or plan.

Every affordance retains its actor-qualified identity, controller, beneficiary
or dependent plan, state, clock, and causal links. The weather patch changes
availability or reliability only. It cannot create U.S. collection capacity,
transfer control of a Himaldeshi route, authorize support, nominate targets,
or imply that the United States has entered combat.

The U.S. observation window may support information delivered to the Room
under its Charter, but possession of the affordance is not universal
information entitlement. The specialist path selected in D57 still determines
who receives the forecast and how its implications reach senior integration.
The linked confirmation becomes common only at the Cycle 2 barrier.

The Himaldeshi support window may affect readiness, delivery, sustainment,
force protection, or timing for the recapture package. Its degradation does
not mechanically cancel or compel the recapture. Himaldesh's own Room retains
its action-specific decision and confirmation route.

### Matching and state-dependent consequences

The matched manifest binds both controllers, both beneficiaries or dependent
plans, and both direct state transitions. Their common before-and-after values
remain fixed across normal compared runs. Different U.S. decisions may change
collection tasking, information demand, commitments, alternate support plans,
or diplomatic conditions, so downstream consequences may still diverge from
the common patch plus recorded branch state.

A run is invalid if an implementation silently changes the observation window
into Himaldeshi ownership, the logistics window into U.S. ownership, or either
beneficiary after seeing outputs. Such a change is a new Setup version or
identity, not Seed friction or an endogenous Room result.

### Disposition of alternatives

- **Selected:** one U.S.-enabled observation or ISR window plus one
  Himaldeshi-controlled logistics or support window. It exposes cross-actor
  interdependence while keeping the U.S. contribution short of combat.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** two Himaldeshi-controlled windows. This centers partner
  vulnerability but gives the U.S. Room less direct responsibility for an
  information dependency.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** two U.S.-enabled windows. This increases U.S. operational
  exposure but risks shifting the conflict away from Himaldesh and Olvana.

The alternatives change actor ownership, beneficiaries, Charter relevance,
and consequence branches. They are Crisis Setup identities rather than Seeds.

### Evidence and feasibility boundary

D59 refines D58's semantic contract without asserting that any real U.S.
platform, access arrangement, or Himaldeshi route exists. The concrete profile
uses synthetic affordances and fictional operational geography. The public
story must describe them as authored exercise state, not public-source fact.

No inspected code binds mixed actor ownership to the paired patch, information
route, or Himaldeshi package dependency. A tracer must construct both actor-
qualified affordances, prove their distinct ownership and beneficiaries before
and after the atomic patch, and reproduce them across matched runs before D59
can be called executable.

### Documentation and next decision

D59 resolves the ownership and beneficiary topology inside OPEN-WORLD-002 and
amends ADR 0043's remaining-authoring boundary. Exact synthetic names, values,
duration, recovery, and serialization remain reversible Setup-authoring fields.

## D60. Delegate reversible first-episode authoring defaults (LOCKED PROCESS)

### Owner direction

The owner directed the design process to stop returning fine-grained scenario
fields as individual questions. Option 1 is the standing recommendation for
the remaining reversible first-episode details, and the author may choose a
coherent default bundle when the exact value can be changed before freeze
without altering the scientific object.

This corrects a process failure. The prior field-by-field grill preserved
detail but consumed time and obscured the central contest design. Durable
documentation still matters, but the documentation must record one coherent
authored profile and its change history rather than require owner ratification
for every fictional label, clock value, or serialization choice.

### Authoring Default

An **Authoring Default** is a versioned, reversible value selected to make the
first episode concrete before a run. It is neither an owner-ratified scientific
claim nor an unrecorded convenience. Every Authoring Default must:

- belong to a named profile with a version;
- remain visibly provisional until the Setup and run manifest freeze;
- respect every locked World, Setup, Charter, and evaluation boundary;
- be recorded before model outputs are observed; and
- change by a new profile version and hash rather than an in-place run edit.

The initial profile is `ridge_seizure.limited_fait_accompli.default.v0_1` in
specification module 13. It gives one internally consistent Road to War,
fictional geography, Force Package roster, mixed affordances, forecast,
confirmation, clock, terminal policy, Seed, provisional risk probes, and
Outcome Projections. These values are defaults, not additional locked ADRs.

### Delegated versus owner-level decisions

The author may choose and revise without another owner question:

- synthetic IDs and fictional map labels;
- exact times inside the locked two-cycle horizon;
- bounded initial and degraded affordance values;
- report wording consistent with locked information and uncertainty;
- deterministic field names, serialization, ordering, and abort codes;
- one bounded matched Seed and non-identity friction values; and
- provisional risk-probe wording and projection field names that implement
  already locked evaluation boundaries.

The author must stop or record an explicit superseding owner decision before
changing:

- the Himaldesh-Olvana conflict, U.S. Focal Room, or two-World evaluation;
- actor strategic intent, doctrine, political objectives, or the selected
  partner-pressure and nuclear-escalation posture;
- a Room Charter's institutional identity, authority, decision routing, or
  information-entitlement principle;
- DATE's open proposal, creative EXCON, typed-Core, validation, matching, or
  evaluation contract;
- a public claim, publication, submission, external cost, destructive action,
  or material scope; or
- a default whose feasibility failure would require a scientific fallback
  rather than a mechanical implementation adjustment.

Authoring may draft a recommended Charter or evaluation field without asking
about every element, but ratification and claim-level freeze remain a batch
owner gate. This preserves speed without allowing implementation convenience
to settle the object of study.

### Change and freeze semantics

Before the first run freezes, an Authoring Default may change whenever source
review, a tracer, or implementation reveals a clearer value. The change must
increment the profile version and retain the reason. Once outputs exist, no
bound default may be edited in place. A changed value creates a new Setup,
profile, World, Charter, or run identity according to the existing semantic
boundary and requires a new comparison.

The first contest comparison should use one frozen default profile and one
frozen Seed. More profiles, Seeds, or MSEL variants remain framework capacity,
not a gate for the bounded submission evidence.

### Consequences for the working process

The next work should proceed from the default profile through source and
feasibility checks, implementation planning, and the first tracer. It should
not reopen the exact label, time, value, or prose choice as a multiple-choice
question. A material conflict with a locked decision is reported as a conflict,
not disguised as a request to choose another minor field.

ADR 0044 records this process boundary. D60 authorizes documentation of the
default profile only. It does not by itself authorize implementation,
experiments, Packet or microsite rewrite, publication, submission, or push.

## D61. Keep the Himaldesh-Olvana nuclear crisis as the simulator's subject (LOCKED SCOPE CLARIFICATION)

### Owner clarification

The owner reasserted the project goal: simulate a conflict between Himaldesh
and Olvana with nuclear escalation on the table, follow the recognizable idea
behind existing LLM nuclear-crisis simulations, and pursue much higher
authenticity and quality in how the crisis, institutions, decisions, and
consequences are represented.

This clarifies rather than reverses D40. Himaldesh and Olvana are the
belligerents and the crisis is the simulator's subject. The complete U.S.
Situation Room remains the Focal Room and primary evaluated instrument because
the contest entry asks how that institution understands and responds to the
regional conflict. U.S. evaluation emphasis must not turn the underlying
conflict into a U.S.-Olvana war or make Himaldesh incidental.

### Nuclear escalation on the table

The first episode begins as a conventional limited seizure and possible
recapture. Both regional actors have DATE nuclear postures and declared
no-first-use positions. Nuclear warning, readiness, coercive signaling,
misinterpretation, or use may become reachable only through authored state,
actor-specific authority, Room decisions, and admitted consequences.

The Setup must not script a launch, require escalation for narrative drama, or
treat de-escalation as the answer key. It must retain a credible causal path
from conventional pressure to strategic concern, allow the represented Rooms
to affect that path, and report escalation separately in the World Outcome
Vector. The limited Olvanan objective does not guarantee that interaction will
remain limited.

### Inspectable authenticity target

"Extreme authenticity and quality" is an owner aspiration, not a measured
claim. ADR 0045 translates it into an inspectable design target:

1. DATE facts and public official sources ground actor politics, doctrine, and
   institutional roles, with facts separated from WOPR inferences.
2. Actor-specific Charters encode real differences in groups, mandates,
   information, activation, authority, and dissent rather than country skins.
3. Synthetic operational detail stays fictional but internally coherent and
   sufficient for policy, escalation, and consequence reasoning.
4. Information arrives selectively, uncertainty remains live, and crisis time
   forces attributable institutional work rather than one omniscient prompt.
5. Rooms may propose open-ended policy while consequences remain causal,
   state-bounded, separately adjudicated, and fail-closed on invalid state.
6. Matched profiles, source cards, manifests, event lineage, decisions,
   dissent, validation, and replay artifacts make every public example
   inspectable.

Quality is therefore shown by the fidelity and auditability of the constructed
instrument and by receipt-bound evaluation results. It is not established by
surface detail, transcript length, model confidence, use of real military
units, or an unsupported claim that this predicts real government behavior.

### Disposition of escalation-shape alternatives

- **Selected:** a conventional ridge crisis whose nuclear-escalation path is
  reachable through actor authority, supported decisions, and admitted
  consequences but is not scripted. This makes escalation management genuine
  Room work without making a launch prompt the opening premise.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** an imminent nuclear-use decision at STARTEX. This changes the
  initial information, time pressure, authority path, and central professional
  work from crisis management to an immediate strategic decision.
- **Rejected for the first Setup, retained as a separately authorable Setup
  identity:** a conventional-only ridge dispute with nuclear escalation
  disabled. This can test regional crisis management but removes the nuclear-
  risk subject selected for the contest baseline.

Neither alternative is a Seed because each changes the strategic problem and
which Charter mandates become reachable.

### Comparator and public-story boundary

The retained LLM wargame literature supplies a genre and methodological
starting point: language-model actors, strategic interaction, nuclear-risk
settings, open-ended action, and evolving consequences. The entry's intended
contribution is to add actor-specific public-source institutions, selective
information, authentic decision routing, a typed causal World, matched
comparison, and full replay. Until comparative evidence exists, the Packet may
describe this as the design target but must not claim measured superiority over
those systems.

The secondary Nuclear War run keeps the same U.S. Room and deliberately closed
rules as a contrast. It does not replace the Himaldesh-Olvana DATE crisis as
the primary simulator, provide realism evidence, or make nuclear conflict a
board-game metaphor in the DATE World.

### Documentation consequence

D61 governs the default profile, implementation priority, risk probes,
microsite narrative, and public claim boundary. It reuses ADRs 0010, 0025, and
0033 for the DATE pivot, U.S. focal evaluation, and two-World design; ADR 0045
records the authenticity interpretation. It adds no exact scenario value and
does not authorize implementation, execution, Packet rewrite, publication, or
submission by itself.

## D62. Prove the DATE World transition before Room or model integration (PROVISIONAL IMPLEMENTATION DEFAULT)

### Why this checkpoint exists

D50-D60 define the semantic World contract, and module 13 gives it one concrete
candidate profile, but no current code can execute that contract. Inspection
confirmed that the repository has useful patterns rather than a hidden DATE
implementation: the closed Nuclear War engine has mutable typed state, frozen
events, strict replay shapes, and deterministic validation; the contest code
has canonical hashes, append-only ledgers, manifests, and receipt checks; and
the Concordia code has isolated entities and trace artifacts. None supplies a
DATE Core, open ledger, State Patch, World Validator, or replay.

The first proof must isolate those missing mechanics. Starting with a full
Room, model, Open Action Proposal, or generative EXCON would make it impossible
to tell whether a failure came from institution orchestration, language-model
behavior, creative adjudication, or the state transition itself. It would also
make a successful call look like evidence for mechanics that had not been
replayed.

### Selected implementation boundary

Under D60's delegated mechanical-authoring authority, the recommended first
slice is a pure contest-scoped transition kernel under
`nuclear_war_contest.date_world`. It is separate from the closed game's
`GameState` and from the Concordia Room harness. Its first responsibilities are
limited to:

- loading and hashing the candidate profile;
- constructing its immutable typed Core;
- admitting fixed-envelope ledger entries;
- instantiating and atomically applying declared semantic patches;
- returning fail-closed validator receipts; and
- replaying final Core and ledger identity from retained artifacts.

The kernel does not yet operate a Room, call a model, parse a Policy Package,
record an Open Action Proposal, run creative EXCON, decide for Himaldesh or
Olvana, or implement the nuclear-escalation path. Those remain later seams and
must not be inferred from a green state tracer.

### Matched templates and run-bound instances

Machine design exposed one necessary distinction. A frozen matched patch
cannot literally contain one fixed `base_core_version` after open-ended Cycle
1 branches, because admissible branches may have different prior Core hashes
or numbers of transitions. Removing the base binding would violate D51 and
permit a stale write; forcing equal branch histories would violate D54's causal
openness.

The selected contract therefore freezes event and patch **templates** as Setup
content. An admitted ledger entry and State Patch **instance** copy the frozen
semantic content and add the run ID, ledger sequence, current base version,
base hash, before-and-after versions, and validator receipt. Matched runs must
share template hashes, operation order, expected values, replacement values,
event time, and delivery content. Run-bound identity fields may differ because
they prove which actual state received the common change.

This is not a relaxation of matching. It makes matching inspectable at the
authored layer while keeping concurrency and stale-state safety inspectable at
the run layer. A template mismatch invalidates the comparison; a stale or
failed instance is rejected without a partial write and also invalidates a
normal matched comparison.

### Candidate serialization and identity

`DATE_PROFILE.candidate.json` is the exact candidate serialization of module
13 at this checkpoint. It binds the Road to War, episode clock, three actors,
fictional geography and packages, hidden Olvanan truth, partner request,
mixed-ownership affordances, clocks, escalation and terminal state, outcome
fields, forecast, weather event, confirmation, paired patch template, risk
probe IDs, and default Seed.

The candidate canonical hash is
`15db06434b120f88f77db732d984f90db9991aa07b5969115339cceae706736e`.
It is a reproducible design identity, not a frozen Setup or run receipt.
Source binding, Charter ratification, tracer success, profile-version freeze,
and a run manifest remain required before outputs.

Canonical identity uses SHA-256 over sorted-key compact UTF-8 JSON. Arrays
retain authored order; duplicate keys, non-finite values, wrong scalar types,
unknown fields, and schema mismatches fail before hashing. State operations use
semantic operation-specific envelopes rather than arbitrary field names or
JSON paths.

### First tracer behavior

The offline tracer begins from Core version 0. It admits the T+1 weather
forecast as a ledger-only observation and proves that the Core hash and version
do not change. It then creates two fixture branches using distinct valid
package-readiness patches, so branch state differs without inventing an entity
or capability. Each branch instantiates the same T+6 paired-weather template
against its current Core, changes both affordances atomically, admits the linked
confirmation, and retains its earlier divergence.

The failure table must cover stale Core identity, failed precondition, unknown
reference, duplicate identity, retroactive time, arbitrary path, undeclared
operation, invalid value, partial paired patch, and unearned actor, package,
affordance, or capability. Fresh-process replay must rebuild each final Core
and ledger and reproduce their hashes.

This proves deterministic state, matched authored content, atomicity,
fail-closed admission, and replay for one episode slice. It does not prove Room
feasibility, institutional authenticity, creative-adjudication plausibility,
open-action handling, two-cycle orchestration, escalation behavior, model
quality, or comparative performance.

### Considered implementation paths

- **Selected:** the contest-scoped pure transition kernel. It is the smallest
  proof that directly answers the current World-feasibility gap and can later
  sit behind the unchanged U.S. Room.
- **Rejected:** extend `nuclear_war_env` with DATE mode switches. That package's
  legal actions, card state, event catalog, and replay are the deliberately
  closed World; coupling DATE to them would smuggle game assumptions into the
  primary simulator.
- **Rejected:** integrate Concordia, the complete U.S. Room, or creative EXCON
  first. Provider and institutional behavior would hide transition defects and
  enlarge the first debugging surface.
- **Deferred:** design a general national-systems or universal wargame engine.
  It may become useful after one tracer, but it is not needed for the contest's
  first receipt and would turn framework breadth into a submission gate.
- **Rejected:** use arbitrary JSON Patch over one open World document. This
  repeats the D50-rejected design and makes permission, precondition, and
  semantic-domain changes indistinguishable from ordinary value updates.

These are implementation alternatives, not Crisis Setup identities or Seeds.

### Documentation and authority consequence

ADR 0046 records the architecture tradeoff. Specification module 14 defines
the exact candidate envelopes, two initial semantic operations, validation
order, stable reason codes, tracer path, implementation map, and non-claims.
Module 09 remains the evidence gate, and module 11 retains the still-open Room,
proposal, EXCON, Charter, measure, run, and publication work.

D62 is a provisional implementation default under D60, not a new owner-locked
scientific choice. A tracer may revise field names, module boundaries, or a
reversible candidate value by recording a new profile or schema version. It
may not weaken open policy, creative but state-bounded consequence generation,
typed admission, matched evaluation, the complete U.S. Room, actor-specific
counterpart Rooms, or the Himaldesh-Olvana nuclear-risk subject. This checkpoint
documents the implementation target; it does not itself authorize code,
experiments, Packet or microsite rewrite, publication, submission, or push.

## D63. Derive Outcome Projections instead of patching duplicate values (PROVISIONAL IMPLEMENTATION CORRECTION)

### Defect found before code

The first test-seam review found that D62's candidate stored each Outcome
Projection as a second mutable copy of a Core fact. The paired weather patch
declared only two affordance operations, so a successful transition would
either leave the copied observation and support outcomes stale or silently
change four fields while claiming two operations. Both paths would weaken the
audit boundary before the tracer began.

### Correction

Outcome Projections are now typed derived views over the admitted Core. Each
projection declares one semantic selector and a target ID where required:
location control, authorization state, commitment state, escalation state,
affordance state, or terminal state. Projection extraction is deterministic
and read-only. It does not enter a State Patch, increment the Core version, or
parse open ledger prose.

The candidate predeclares `COMMIT_US_SUPPORT_01` with state `none` so its view
does not treat an absent commitment as false or invent an entity later. The
Himaldeshi recapture view reads `AUTH_HIM_RECAPTURE_01`; package readiness
remains separate from political authorization.

The candidate profile version advances from `0.1.0` to `0.1.1`, its profile
schema from `date-profile.v0.1` to `date-profile.v0.2`, and its Core schema from
`date-core.v0.1` to `date-core.v0.2`. The new canonical hash is
`64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477`.
The D62 hash remains preserved as the superseded candidate identity.

### Considered paths

- **Selected:** semantic derived views. They keep projections synchronized
  without adding hidden writes or duplicating World truth.
- **Rejected:** automatically mirror each source write into stored projection
  values. This creates implicit state changes absent from the patch artifact.
- **Rejected:** add projection-write operations to every patch. This makes
  authors repeat the same change and lets a patch produce internally
  inconsistent facts and measures.
- **Rejected:** derive outcomes from open ledger text after the run. This
  violates D50 by allowing prose to become quantitative truth post hoc.

These are serialization and extraction alternatives, not Setups, Seeds,
policies, or evaluation conditions. No owner-level scientific choice changed.

### Implementation consequence

The profile loader must validate projection selectors and references. A public
`project_outcomes` seam must extract all declared values from a supplied Core
without mutation. Transition tests must show that the two-operation weather
patch changes the two affordance projections through their source fields while
the patch receipt still reports exactly two operations. Replay must reproduce
both the final Core hash and the derived projection values.

## D64. Accept the first DATE tracer as mechanical evidence only (MEASURED IMPLEMENTATION CHECKPOINT)

### Receipt

The no-model D62-D63 tracer passed in a fresh Python process against executor
revision `c7d57167bb1ab219b8e3e3a128866b71699e9977`. The retained
`DATE_TRACER_RECEIPT.json` has content hash
`4a582d72b6d8ff753c3e06adea4d36aef3c3b39b5284e4050ce9ed35e39815e3`
and binds candidate profile `0.1.1` at hash
`64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477`.

The forecast created a ledger entry without changing Core version 0 or its
hash. The tracer then forked `ready` and `delayed` package states, each at Core
version 1. Both branches instantiated template hash
`a0e67568cf7fc355ff5126e77fc7be925e7d272b0521d3f82bac13e2cc0a0e6c`
against their own current Core, which produced distinct patch-instance IDs.
The same ordered operations changed U.S. observation from `available` to
`intermittent` and Himaldeshi support from `available` to `restricted` in both
branches. The linked confirmation was admitted, the prior package difference
remained, and each final Core version 2, ledger, and derived projection set
matched replay.

The retained failure matrix covers invalid envelope, duplicate ID, unknown
reference, causal mismatch, retroactive time, terminal World, template
mismatch, stale Core, partial patch, failed affordance precondition,
undeclared operation, forbidden write, and invalid value. The failed paired
affordance case applies its first operation only to a private copy, fails the
second precondition, and proves that neither write reaches the returned Core.

### Review corrections retained

Implementation review tightened the candidate boundary rather than weakening
the experiment. It added exact nested profile envelopes, global Core-entity
uniqueness, typed semantic values, causal-template ordering, event-template
and patch-instance receipt bindings, and patch-envelope-first validator order.
The last correction matters because the fixed D62 order requires malformed
patches to fail as `invalid_envelope` before a retroactive-time check. Each
correction was introduced through a failing test and retained in the final
focused suite.

The authoritative repository-wide `uv` run reports 1,920 passed, 3 skipped,
and one unchanged baseline microsite-copy failure. That assertion expects the
literal phrase `no live study results` in the historical site. The tracer did
not rewrite public copy because Packet and microsite work remain a separate
approved phase.

### Evidence boundary and considered interpretations

- **Selected:** accept the receipt as evidence that this candidate Core,
  ledger, semantic patch, validator, matched-template, projection, and replay
  slice executes deterministically under the retained code revision.
- **Rejected:** call the DATE arena or U.S. Situation Room executable. No Room,
  model, Open Action Proposal, creative EXCON consequence, or two-cycle
  institutional path ran.
- **Rejected:** treat the candidate profile as frozen because its mechanical
  tracer passed. Source binding, Charter ratification, risk-probe freeze, and a
  versioned freeze receipt remain required.
- **Rejected:** infer authenticity, escalation quality, model quality, or
  comparative performance from a state-transition test.
- **Deferred:** repair historical microsite copy as part of this checkpoint.
  Public narrative and Packet changes remain subject to their own review.

D64 changes implementation evidence, not an owner-level scientific choice, so
it creates no new ADR and no Crisis Setup, Seed, Room, or evaluation condition.
It closes only the D62-D63 mechanical tracer gate. The next implementation
work remains the U.S.-first bounded DATE path: ratified Charters and source
bindings, open proposals, creative but state-bounded EXCON consequences, two
complete U.S. cycles, one selected comparison, and receipt-bound evaluation.

## D65. Build the U.S. vertical slice before complete Counterpart Rooms (LOCKED IMPLEMENTATION SEQUENCE)

### Owner selection

The owner approved option 1 from the post-D64 work program. Development will
first build and trace the complete U.S. Focal Room path with deterministic
counterpart fixtures, then replace those fixtures with actor-specific
Himaldesh and Olvana Rooms before any live episode, DATE execution claim, or
submission evidence. The fixtures are build scaffolding only. They do not
alter the locked requirement that all three represented actors have actual
Charter-bound Rooms in the contest episode.

This is a sequencing decision, not a change to the scientific object. The U.S.
Room stays focal because the Packet evaluates how it turns fragmented evidence
and institutional work into attributable policy, proposals, consequences, and
adaptation. Himaldesh and Olvana remain the belligerents whose decisions and
nuclear-risk interaction make that work consequential, but their supporting
implementation depth cannot displace the U.S. path again.

### Architecture and reuse boundary

The inspected code supports reuse below the Room level. Concordia entity,
persistent-memory, response, client, trace, and call-budget primitives can
support many distinct office seats. The preserved probes already measure
entity isolation, selective delivery, bounded scheduling, and ordered
collection at those seams.

The legacy composition does not define the new Room. `FactionDecisionAgent`
encodes a small aggregation council, `PressCoordinator` encodes serial public
speaker passes, and the Nuclear War harness binds players to a closed legal
action interface. Extending any of those as the institutional controller would
reintroduce the three-agent, plenary-chat, or closed-move assumptions already
rejected by C0.2, D06-D08, D18-D25, and D48.

The selected architecture is therefore a contest-scoped Room Orchestrator
beside `date_world`. It executes frozen Charter mechanics for delivery,
activation, dependencies, shared-seat barriers, collection, decision routing,
validation, and artifacts while agents supply institutional judgment. It may
adapt the reusable Concordia primitives through narrow interfaces. It may not
summarize evidence, repair missing work, resolve dissent, invent authority,
choose policy, propose creative World consequences, or mutate the Core.

### Work program and evidence gates

The retained work program has seven milestones:

1. Refresh public official sources and bind a machine-readable candidate U.S.
   Charter and claim-level source register.
2. Run one no-model U.S. Cycle 1 through Watch, specialist products, senior
   integration, decision routing, and the integrated Policy Package.
3. Connect original-language Open Action Proposals through bounded
   clarification, state-bounded consequence proposals, and D64 admission.
4. Complete two U.S. cycles with persistent seats, endogenous consequences,
   the matched weather inject, attributable reassessment, and replay.
5. Replace both Development Counterpart Fixtures with episode-relevant,
   actor-specific Himaldesh and Olvana Room paths.
6. Run one bounded live smoke, repair the interface without changing frozen
   science, and freeze the comparison, measures, probes, models, budgets, and
   manifest.
7. Run the receipt-bound DATE pilot, add the smallest same-U.S.-Room Nuclear
   War adapter, and only then rewrite the Packet and microsite.

Source work, fixture-based engineering, and evaluation-to-trace mapping may
advance concurrently after their shared envelopes are fixed. They converge at
the Charter, no-model tracer, and manifest-freeze gates. Live runs may fan out
only after one bounded smoke passes. Parallelism may reduce elapsed time but
may not create competing schemas, leak outputs into probe design, or select a
favorable result.

The first accepted program artifact is a fresh-process Focal Room Tracer, not a
source inventory, schema test, one model call, or one-cycle transcript. It must
retain the complete U.S. path through two decisions and World consequences.
The first contest-level execution claim additionally requires the fixtures to
be gone, actual Counterpart Rooms to run, a frozen manifest, and a complete
proposal-adjudication-validation replay.

### Considered alternatives and dispositions

- **All three Rooms first:** Rejected as the build order because it expands the
  first debugging surface and delays the focal U.S. evidence. It remains true
  that all three must run before a live episode claim.
- **Fixture counterparts in final evidence:** Invalid because deterministic
  scaffolding cannot satisfy the Counterpart Room contract.
- **Legacy faction C2 or press as the new Room:** Rejected because their
  topology, information, and decision semantics conflict with the approved
  institution.
- **General simulator framework first:** Deferred because one receipt-valid
  episode, not framework breadth, is the submission floor.
- **Flatten the U.S. Room for the baseline comparison:** Rejected as the
  default. The provisional comparison intent is to vary a declared model or
  system condition inside the same complete U.S. Room; any flat or reduced
  Room must be a separately named ablation.

### Immediate milestone

Milestone 1 is the source-bound U.S. Charter candidate described in new
specification module 15. It must cover public process and membership sources,
every first-episode seat and group, information entitlements, activation,
decision routes, Required Confirmations, source-versus-inference mapping,
strict canonical identity, focused failure tests, and a rendered batch-review
surface. It makes no model call and no Room claim.

The detailed work program is retained at
`docs/plans/2026-08-25-us-first-date-room-work-program.md`. D65 creates ADR
0047 because the build order and reuse boundary are hard to reverse, would be
surprising from the existing C2 code, and resolve genuine alternatives. It
creates no Crisis Setup, Seed, model condition, evaluation result, or public
claim. The written design must receive owner review before implementation.

## D66. Present the source-bound U.S. Charter candidate for batch ratification (MEASURED CANDIDATE CHECKPOINT)

### Scope and artifact identity

Milestone 1 is implemented as a candidate and has reached its single batch
owner gate. It has not been ratified or frozen. The implementation made no
model call, ran no Room cycle, changed no DATE Core state, and produced no
experiment result. It serializes the institutional contract that Milestone 2
will execute only after the owner accepts or revises the exact bundle.

The retained candidate artifacts are:

- `US_SOURCE_REGISTER.candidate.json`, canonical SHA-256
  `73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f`;
- `US_CHARTER.candidate.json`, bound to that source identity, canonical
  SHA-256
  `fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2`;
- `US_CHARTER_REVIEW.candidate.md`, regenerated from the two loaded artifacts
  and protected by an exact staleness test; and
- `research/2026-08-26-us-charter-official-source-refresh.md`, which records
  the claim boundary, official URLs, gaps, and retrieval findings.

These hashes identify candidate content, not an accepted Charter, executable
Room, official U.S. procedure, or empirical fidelity claim.

### Public-source boundary

The source register contains 20 public official sources, 18 bounded facts, 15
declared simulation inferences, and 6 explicit gaps. It covers the public NSC
and HSC organization and PC process, statutory office boundaries, stable
department and adviser mandates, CJCS advice without command, public
combatant-command functions, and the dated strategy material used only for
persona posture and actor-objective inference.

The refresh retained several corrections instead of manufacturing apparent
completeness:

- Treasury initially had only a department mission page. Review added its
  statute so the stable office and duties do not rest on agency copy alone.
- The inspected national-security strategy did not establish an exact
  publication day. An initially inferred `2025-11-01` value was removed and
  remains `null`.
- The statutory `Secretary of Defense` office class remains authoritative for
  the seat. A different label in the dated public defense strategy is retained
  as context and a non-blocking gap, not used to rewrite the institution.
- No source was found for general PC or department-level authority to admit
  state-changing effects, so the candidate encodes no such delegation. The
  missing delegation instrument and effect-level authority map remain
  activation-blocking gaps for later routes.
- The five U.S. objectives are explicitly unweighted exercise abstractions.
  Each objective ID is now resolved by the source register's declared
  objective inference rather than existing as an unbound Charter label.
- Source-to-claim links are reciprocal. Review found three inferences that
  cited NSPM-1 without appearing on that Source Card; the card and strict
  validator were corrected so one-way evidence links fail closed.

The register names offices, never current officeholders. Facts record bounded
public claims. Inferences label the exercise-specific objective vector,
activation, persistent seats, group graph, entitlements, products, routing,
and confirmations. Gaps remain visible rather than being filled through title
analogy or plausible-sounding procedure.

### Complete candidate institution

The Charter serializes 20 public roster seats rather than a target agent
count. Fourteen are first-episode active under the candidate predicates. The
functional U.S. Theater Commander is triggered for the fictional operational
problem. Homeland Security, Homeland Security Advisor, pandemic, Interior,
Policy Assistant, and Counselor seats remain declared but inactive when the
relevant predicate or public mandate is absent. Activation changes
participation, not institutional identity.

The machine graph contains two deterministic services, seven specialist or
synthesis groups plus PC, NSC, and HSC, 22 information classes, 12 activation
predicates, two presidential decision routes, four record confirmations, and
10 product schemas. Every seat retains one identity across its groups. Voting
principals remain distinct from non-voting advisers and invitees. Watch and
Executive Secretary transport and preserve declared information and records;
they supply no judgment, consensus, or policy choice.

The first episode therefore has an inspectable path from authorized common
and seat-private information through attributable specialist products,
Presidential Synthesis, a no-chair-weight PC package, and a President-chaired
NSC or HSC record. The President receives integrated products and logged
underlying retrieval, not hidden World truth or an automatic union of every
private brief. The candidate routes presidential policy only. It deliberately
does not pretend to complete later action-specific authority and confirmation
maps.

### Strict loading, compilation, and review corrections

The implementation lives under `nuclear_war_contest.situation_room` and is
limited to loading, identity, validation, deterministic compilation, and
lossless review. It rejects duplicate JSON keys, unknown envelopes, duplicate
global identities, unresolved typed references, unbound or one-way evidence,
current-officeholder fields, unsupported enums, dependency cycles, World-truth
entitlements, inferred delegation, ambiguous action classes, and incomplete
decision routes.

Failing tests exposed and retained the following corrections:

- The compiler first ordered a seat's groups by a group-ID tie break. It now
  preserves the seat's declared group order.
- The renderer first sorted JSON keys and changed the declared field order. It
  now renders every field in source order, and the retained review must equal
  the generated bundle byte for byte.
- Direct permissions initially retained inactive recipients. First-episode
  compilation now admits only activated recipient seats.
- Multiple permission records for one information-class and sender pair
  initially overwrote earlier recipients. Compilation now unions every
  declared recipient set.
- Duplicate action classes initially overwrote route lookup. They now fail as
  an ambiguous and incomplete route.
- A missing Required Confirmation reference now fails before compilation.
- Seat `group_ids` and group eligible-membership lists could disagree. The two
  declared views must now be exactly reciprocal.
- Declared shared-seat barriers could drift from actual multi-group seats.
  Each group must now declare exactly the shared identities it contains.
- A permission could name a direct seat or whole group whose members lacked
  that information entitlement. Every reachable recipient must now declare
  the class. The candidate accordingly grants the PC roster its declared
  synthesis product and grants every record recipient its decision record,
  including currently inactive seats that may activate in a later episode.
- A roster-count assertion could pass after replacing one office with another.
  Candidate coverage now checks the exact 20-seat identity set.

The compiler still supplies no seat judgment. It derives only activated seat
and group views, voting membership, transitive group dependencies, actual
shared-seat barriers, authorized active recipients, and unique action-class
route lookup from the validated Charter.

### Verification and evidence boundary

Forty-five focused tests pass for source and Charter loading, rejection codes,
canonical identity, compilation, exact candidate coverage, permissions,
barriers, routes, and lossless review. Ruff passes for the full source and test
trees. Focused Pyright reports zero errors and zero warnings.

The repository-wide run reports 1,963 passed and 3 skipped, with one unchanged
historical failure. The historical private microsite test still requires the
literal phrase `no live study results`; Milestone 1 did not edit Packet or
microsite copy because public narrative remains a later approved phase. No new
failure is attributable to the U.S. Charter candidate.

Parallel source and review work was attempted during the milestone. Three
background source workers and two independent review workers failed before
startup because the requested worker type was unavailable. The source refresh
and a two-axis standards-versus-spec review were therefore completed locally.
That review found the objective, reciprocal evidence, membership, barrier,
recipient-entitlement, and exact-roster gaps above; each was repaired through a
failing test before this checkpoint.

### Gate and next work

- **Selected:** present this exact source and Charter bundle for one batch
  owner ratification or revision.
- **Rejected:** infer Milestone 1 completion from passing schemas or tests
  alone. Owner ratification remains a required condition.
- **Rejected:** start Milestone 2 against a moving candidate identity. The
  no-model U.S. cycle must bind the accepted hash.
- **Rejected:** call fixtures, compiled views, or source cards a simulated
  government, a Room run, or contest evidence.
- **Deferred:** effect-level authority and confirmation routes, live seat
  execution, Concordia adaptation, Open Action Proposals, creative EXCON,
  two-cycle DATE execution, Counterpart Rooms, the Nuclear War adapter, Packet
  rewrite, and microsite narrative.

D66 changes measured implementation status and tightens the already approved
Milestone 1 contract. It makes no new owner-level scientific choice, creates no
new ADR, and selects no Setup, Seed, model, probe, or comparison. Milestone 2
begins only after the owner ratifies or revises the two exact candidate
identities above.

### D66 verification-count correction

The final reciprocal-link tests were added after the first complete D66 suite
receipt. They increase the focused gate from 43 to 45 passing tests and the
repository-wide passing count from 1,963 to 1,965. The same 3 tests remain
skipped and the same single historical microsite-copy assertion remains the
only failure. The candidate source hash, Charter hash, and rendered review did
not change.

## D67. Ratify the exact source-bound U.S. Charter bundle and begin Milestone 2 (RATIFIED CHECKPOINT)

### Owner decision and exact identity

The owner ratified the complete D66 U.S. source and Charter bundle without a
content revision and directed the project to commit, push, merge, cut a new
branch, and continue with Milestone 2. Ratification binds these exact candidate
identities:

- `US_SOURCE_REGISTER.candidate.json`, canonical SHA-256
  `73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f`;
- `US_CHARTER.candidate.json`, canonical SHA-256
  `fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2`;
  and
- candidate commit `623612166aa65bb0c2f14a79ea6993cd02221f8d`, which is
  the version presented for the decision.

The accepted source and Charter files remain byte-for-byte unchanged. Their
`.candidate.json` names record how they entered review; acceptance is recorded
separately in `US_CHARTER_RATIFICATION.json`. This avoids changing either
accepted hash merely to encode its new status. The canonical ratification
receipt hashes to
`0b831d55ba60dd458e44b0e63d714a82eaf05b508a32694f96181caba0b5ad13`.

### Meaning of ratification

D67 closes the one batch owner gate declared by D65-D66 and `SR-USM-060`.
Milestone 1 therefore passes at the identities above, and Milestone 2 may bind
its no-model Cycle 1 artifacts to that accepted institution. The ratification
accepts the first-episode U.S. institutional abstraction, its stated public
source-versus-inference boundary, roster, group graph, communication
entitlements, activation rules, presidential routes, record confirmations,
and validation contract as the implementation basis for this contest entry.

Ratification does not convert synthetic design inferences into public facts.
It does not establish official, classified, operational, or predictive
fidelity. It does not prove that a model can perform any seat, that the groups
will integrate information well, or that a complete Room will function. It
does not freeze D23's conventional-crisis activation count, effect-level
authority or confirmation rules, the open proposal contract, creative EXCON,
the first Crisis Setup, counterpart Charters, model conditions, evaluation
measures, the Nuclear War adapter, or a public claim.

### Milestone 2 boundary

The authorized next slice is the deterministic, no-model first U.S. Room
Cycle specified by the retained D65 work program. It will exercise Watch
delivery, the declared specialist dependency graph, senior integration,
decision routing, and one structured Policy Package while preserving isolated
information, explicit failures, and fresh-process replay. Deterministic
Himaldesh and Olvana fixtures may provide development inputs only. They remain
non-evidence and cannot substitute for actor-specific Counterpart Rooms in a
live episode.

Milestone 2 makes no provider call and admits no World consequence. Open Action
Proposal serialization, effect-level authority and confirmation, creative
EXCON, the proposal-consequence bridge, a two-cycle DATE trace, and live model
execution remain later gates. Any mismatch between the implementation and the
ratified Charter must fail closed and produce a receipt; it may not be repaired
by silently changing the Charter or its accepted identity.

### Alternatives and disposition

- **Selected:** preserve the reviewed bytes and add a separate exact
  ratification receipt. This keeps the accepted identity stable and makes the
  owner decision machine-checkable.
- **Rejected:** edit the candidate files or rename them in place to encode
  acceptance. Either action would create a new identity that was not the
  object of the ratification decision.
- **Rejected:** begin Milestone 2 from an unbound copy or latest-path lookup.
  Every Cycle 1 artifact must name and verify the D67 Charter and ratification
  identities.
- **Rejected:** treat ratification as Room, model, World, or authenticity
  evidence. It is an owner acceptance receipt for a bounded design artifact.
- **Deferred:** all live execution, counterpart replacement, proposal and
  consequence work, Setup freeze, comparison, Packet rewrite, and microsite
  presentation remain subject to their existing gates.

D67 creates no new ADR. It closes the explicit batch gate already established
by ADR 0047 and specification module 15 without changing the accepted design.
The full rationale, exact identities, alternatives, evidence boundary, and next
milestone scope remain durable here for later Packet and microsite narrative.

## D68. Execute the ratified U.S. institutional graph through one deterministic no-model cycle (MEASURED CONTROLLER CHECKPOINT)

### Exact executor and artifact identities

Milestone 2 ran in a fresh process against exact executor revision
`a1d85c8571a534cd87e08fdc7d05b0bd8bca8f5d`. The retained receipt binds:

- source-register hash
  `73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f`;
- U.S. Charter hash
  `fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2`;
- D67 ratification hash
  `0b831d55ba60dd458e44b0e63d714a82eaf05b508a32694f96181caba0b5ad13`;
- development-fixture hash
  `ea7333ec4e7423ad628455d18638c6e0eefd9fdca3b0bd17f85d35fb2d2ac9fc`;
- Himaldesh fixture hash
  `3af85d53f1706c3a5ac8027b400ea4a90e1ba35fa0ac98cf5fa39ccb0ffe1733`;
- Olvana fixture hash
  `7b0773a4cdd65d51d6c33adf9137f1e219293b0e89897a9073df23aa7a9375b1`;
- deterministic run hash
  `08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6`;
  and
- canonical receipt hash
  `b4c47bcfbffd43fe826bf75fb4a2722a0ef315948dc0b5b8b5d485437fb1a798`.

An independent canonicalization of the retained receipt, after removing its
self-hash, reproduced the exact receipt hash. The executor resolves to a Git
commit and independently matched the pushed topic-branch head before the run.

### What the trace actually exercised

The fixture activates the 14 D67 first-episode seats and supplies twelve
authored Watch inputs. Those inputs include one common crisis picture, a raw
weather forecast with bounded recipients, and seat-private intelligence,
diplomatic, financial, defense, nuclear, legal, and executive material. Every
input retains its information class, sender, causal parents, content, hash, and
derived delivery recipients. The successful run records 96 deliveries without
constructing a union brief or exposing World ground truth.

The compiled Charter produced seven execution waves in this exact order:

1. Threat and Attribution;
2. Diplomatic and Economic plus Nuclear and Radiological, which are disjoint
   and therefore share one logical wave;
3. Defense and Escalation;
4. Legal and Authority;
5. Presidential Synthesis;
6. the Principals Committee; and
7. the National Security Council.

The controller accepted eight attributable authored products in Charter order.
It retained the integrated Policy Package with all six required domain
dispositions while preserving arbitrary additional cross-domain content. It
resolved `presidential_policy_direction` to the ratified presidential route,
retained the exact NSC decision record, verified its two record-level Required
Confirmations, marked the record supported, and admitted no World effect.

The fixture's Himaldesh support request and Olvana ridge-posture output remain
frozen synthetic development inputs. Their IDs and hashes establish causal
test provenance only. They do not observe, deliberate, decide, communicate, or
adapt under actor-specific Charters and therefore do not count as either
government, either Counterpart Room, or DATE evidence.

### Open content inside a strict institution

Milestone 2 deliberately validates the institutional envelope rather than an
exhaustive policy vocabulary. Watch inputs and group products may contain open
JSON content. A group product must still name its declared group and product
schema and contain every Charter-required field. The PC must still cover all
six policy domains, and the NSC record must still bind the applicable route,
consultations, package, decision, taskings, dissent, reassessment, required
confirmations, and what was not decided.

This is the balance selected earlier in the design discussion: the controller
does not prescribe the substantive policy, but it can prove who received what,
which institutional body produced each artifact, which dependencies were
satisfied, how the package reached presidential decision, and whether the
record is complete enough to support later effect-level processing.

### Failure and replay receipts

The focused tests retain these failure semantics:

- unknown envelope fields, duplicate IDs, invalid nested records, non-finite
  values, identity mismatches, and unresolved Charter references fail closed;
- an unentitled Watch or product delivery cannot enter a seat or group input;
- a missing Threat product remains a failed attempt, blocks only its proven
  descendants, and does not prevent independent Diplomatic/Economic or
  Nuclear/Radiological work from completing;
- a missing record confirmation preserves the NSC decision record but marks it
  unsupported;
- a route mismatch preserves a rejected decision attempt rather than silently
  selecting another route;
- a Policy Package missing one required domain fails, while additional open
  policy content remains valid; and
- no failed path can produce a supported decision or a World effect.

Fresh-process replay reconstructed the same schedule, deliveries, attempts,
products, Policy Package, route, decision record, confirmations, failures, and
run hash. Twenty-two focused tests pass, including exact retained-fixture and
retained-receipt integrity checks. Ruff, formatting, and focused Pyright pass.
The pre-receipt repository gate reported 1,987 passed and 3 skipped; the final
post-documentation repository result is recorded separately in the append-only
logbook rather than inferred here.

### Implementation corrections and rationale

The implementation process exposed several distinctions that are now part of
the durable design narrative:

- Product access cannot be derived only from a separate disclosure row. The
  ratified Charter also declares dependency edges and group input
  entitlements. A product is therefore deliverable through either an explicit
  disclosure permission or the conjunction of a declared dependency and
  matching group entitlement. Neither route permits undeclared access.
- Failure propagation follows graph ancestry, not an all-or-nothing cycle
  flag. This preserves independent institutional work while preventing any
  descendant from pretending its missing basis exists.
- Fixture order and wall-clock completion cannot determine the record. The
  compiled Charter owns logical waves and canonical collection order.
- Policy-domain coverage is a completeness rule, not an action quota. A domain
  may record conditional action, no action, or another declared disposition,
  and open policy components remain non-exhaustive.
- A large receipt should be written by the tested tracer rather than copied by
  hand or retained through an untested shell boundary. Standard output remains
  the default; one explicit output path writes the identical canonical bytes.

These are reversible controller-level interpretations of the ratified
contract. They create no new actor objective, authority, Setup semantics,
comparison, or public claim, so D68 creates no new ADR.

### Alternatives and disposition

- **Selected:** one complete deterministic U.S. institutional cycle with open
  authored product bodies inside strict Charter, delivery, routing, and replay
  envelopes. This isolates controller mechanics before model and World work.
- **Rejected:** collapse the cycle into one presidential agent or the old
  three-member council. That would evade the U.S. Room scale and specialist
  graph the entry is intended to examine.
- **Rejected:** let the controller synthesize missing advice, choose among
  policies, resolve dissent, infer consent, or write a counterpart response.
  Authored fixture content remains visibly authored, and missing work fails.
- **Rejected:** require every product to fit a closed policy or action catalog.
  That would recreate the Nuclear War interface inside the open DATE path.
- **Rejected:** fail the entire cycle whenever any group fails. The Charter
  graph supports attributable partial work, so only proven descendants block.
- **Rejected:** treat the successful authored decision as model, government,
  institutional-quality, or crisis-outcome evidence. It proves mechanics and
  replay only.
- **Deferred:** actor-specific Himaldesh and Olvana Rooms, model-mediated seat
  work, Open Action Proposals, effect-level authority and capability,
  state-bounded EXCON, World admission, Cycle 2, matching, evaluation, the
  Nuclear War adapter, and public narrative remain later gates.

### Gate and next milestone

D68 closes Milestone 2 at its declared scope. We now have a source-bound and
ratified U.S. institutional graph plus one deterministic, replayable no-model
Cycle 1 controller trace. We do not yet have a live U.S. Room, a Counterpart
Room, a proposal-to-consequence path, a two-cycle DATE episode, or comparative
evidence.

The next bounded milestone is M3's open proposal and consequence bridge. It
must start from the retained NSC decision and Policy Package, preserve original
proposal language, bind compound dependencies and bounded clarification,
separate creative consequence proposals from deterministic admission, verify
effect-level authority and capability without inferring either, and join only
valid effects to the D64 World kernel. It must remain no-model until those
machine contracts and failure receipts pass.

### D68 post-review identity correction

The first D68 receipt above bound executor
`a1d85c8571a534cd87e08fdc7d05b0bd8bca8f5d` and receipt hash
`b4c47bcfbffd43fe826bf75fb4a2722a0ef315948dc0b5b8b5d485437fb1a798`.
Those identities remain a valid pre-review intermediate, but they do not name
the final D68 checkpoint.

The required standards-versus-spec review found and repaired five fail-closed
gaps before finalization:

- a fixture and modified ratification receipt could previously move together
  away from the exact D67 identity;
- Watch validated a known class and known sender separately instead of the
  declared class-sender permission pair;
- an inactive group's otherwise known product could be silently ignored;
- the NSC decision record did not yet verify the route's exact consultation
  list; and
- a malformed nested domain disposition could raise a raw type error instead
  of becoming an attributable invalid-package failure.

The reviewed implementation binds the exact D67 ratification hash, validates
the declared Watch pair, rejects inactive-group products, checks exact route
consultations, and safely validates nested domain records. It also removes the
controller-owned product-class table and derives product information classes
from the ratified Charter's disclosure records. The Charter still permits a
recipient through explicit disclosure or through a declared dependency plus a
matching group entitlement; no delivery right was broadened.

The final D68 executor is
`6c06ed4a7e362cdee89ca15df7aff385aec0aaf8`. It independently matches the
pushed topic-branch head. The fixture hash remains
`ea7333ec4e7423ad628455d18638c6e0eefd9fdca3b0bd17f85d35fb2d2ac9fc`
and the run hash remains
`08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6`.
The regenerated canonical receipt hash is
`7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186`.
Independent canonicalization reproduces that hash. Twenty-seven focused tests
now pass, superseding the earlier 22-test count.

Two independent review workers were requested for the standards and
specification axes; both failed before startup because the agent type was
unavailable. The coordinating agent completed both reviews locally and
retained the failed dispatches in the append-only logbook. These repairs change
no actor objective, institutional authority, policy result, World state, Setup,
or comparison. They strengthen the D68 controller gate and leave its evidence
boundary unchanged.

## D69. Carry one open U.S. proposal through bounded consequence admission (MEASURED PROPOSAL-BRIDGE CHECKPOINT)

### Exact executor and artifact identities

Milestone 3 ran in a fresh process against exact executor revision
`1b912ff693a84c5e1081fc76d1ed1f71e4f810aa`. That revision independently
matched the pushed topic-branch head before the retained receipt was generated.
The receipt binds:

- D68 receipt hash
  `7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186`;
- D68 run hash
  `08d605c0bfb61bc5e97ee41c75033f6615721a6533dfb780f1cfb9f6a7e802e6`;
- D64 World-profile hash
  `64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477`;
- development-fixture hash
  `4b47bc86dad3226692146cc92b21f7b3da61a5919b87ce26924514d7f44ce465`;
- deterministic bridge-run hash
  `d43ad8544af90f8e44736133c11b6e8443275c901049ffb0800efd2e0978b996`;
  and
- canonical receipt hash
  `cf78c92190e8b2739923c0977a0af316b332643b563d0ad4818b13048c726ec4`.

Independent canonicalization after removing the receipt self-hash reproduced
the exact receipt hash. The retained run attempts two effects, admits one,
blocks one, creates one World ledger entry and one validator receipt, leaves
the World Core unchanged, and replays to the same canonical run hash.

### What the trace actually exercised

The trace starts from D68's retained U.S. Policy Package and supported NSC
decision record. It preserves this compound Open Action Proposal in its
original language:

> Prepare a defensive intelligence package for potential release, and transmit
> it only after recipient restrictions are identified.

The fixture authors two ordered effects because the controller is not allowed
to infer executable effects from prose. The first effect attempts to prepare a
releasable package. Its timing begins unresolved, and one retained
clarification fills only that declared null field with `before the hour-four
disposition clock`. The resolved effect then binds a separate development-only
effect-authority record to its exact hash and proves a typed capability
predicate: the U.S. actor owns the `US_CRISIS_ASSESSMENT` activity in the D64
Core. Development EXCON proposes a ledger-only consequence, and the D64
validator admits `Assessment staff begin preparing the defensive package.`

The second effect attempts later transmission. It depends on preparation but
still lacks a confirmed recipient channel. Its retained clarification says no
channel is yet confirmed and supplies no replacement value. The effect is
therefore blocked as `unresolved_clarification` before authority, capability,
EXCON, or World admission. The original proposal, both original effects, the
question and response, the successful preparation path, and the blocked
transmission path all remain in one replayable artifact.

This mixed result is intentional. It shows that an open compound proposal need
not be collapsed into either total acceptance or total rejection. A supported
effect may continue while an unresolved dependent effect remains visible and
produces no state change.

### Open language inside a fail-closed bridge

D69 does not require an action family, handler, or exhaustive policy type. The
proposal and each effect retain arbitrary open content, and a passing control
proves that unfamiliar content is not itself a rejection reason. The strict
parts are provenance and admission boundaries:

1. The proposal must bind the exact D68 package, package components, decision
   record, actor, version, original language, and authored effect graph.
2. Every clarification must bind the exact original-effect hash and may fill
   only fields explicitly declared unresolved. It cannot overwrite policy,
   add an effect, change dependencies, or become evidence that the resolution
   is substantively correct.
3. Every effect that can reach the World needs a separate authority record
   bound to the exact resolved-effect hash and a route-owning seat. D68's
   supported decision and record confirmations do not silently authorize
   implementation.
4. Capability is proved only through typed predicates over the loaded Core.
   Policy prose, an office title, an authority record, or EXCON narration
   cannot create a force, activity, access path, affordance, or permission.
5. EXCON emits a consequence proposal, not truth. The deterministic D64
   validator owns ledger admission and any typed Core transition.

The first capability catalog covers activity ownership, affordance control,
affordance state, and Force Package ownership. It is a bounded validation
catalog rather than a closed proposal ontology. A U.S. proposal cannot claim a
Himaldeshi capability merely because that entity exists in the same World.

### Consequence and World boundary

The consequence artifact binds its proposal and effect parents, exact Core
version and hash, every Core entity read, affected entities, causal World
parents, episode hour, audiences, evidence, assumptions, uncertainty,
plausible alternatives, explicit represented-Room decisions, resulting
injects, adjudicator, open content, and optional State Patch. Each capability
entity and each dynamic patch target must be disclosed in the Core read, and a
patch target must also be declared affected.

The D64 kernel now accepts `excon_consequence` as a distinct non-authored event
source after the bridge checks pass. This adds neither a semantic domain nor a
State Patch operation. Authored MSEL template IDs remain protected against
collision, and any Core-changing consequence must still use the two declared
D64 operations, current Core identity, exact preconditions, and atomic
validation. The retained D69 consequence is ledger-only, so its accepted event
does not change a permission, clock, terminal predicate, typed measure, or Core
hash.

An event may affect a represented actor without deciding for that actor. The
bridge therefore rejects explicit represented-Room decision actor IDs rather
than treating every affected U.S., Himaldeshi, or Olvanan entity as an
institutional decision. Development EXCON is a separate adjudicator identity
and cannot masquerade as a Room seat.

### Failure and replay receipts

The focused checks preserve these distinctions:

- envelope, exact-identity, duplicate, graph, and static artifact-reference
  defects stop before a run;
- unresolved clarification, failed dependency, missing or stale authority,
  missing capability, stale Core, undisclosed Core reads, represented-Room
  substitution, causal mismatch, and invalid consequence remain attributable
  effect receipts when they depend on the current run state;
- undeclared semantic operations, arbitrary paths, stale patch bases, and
  failed D64 preconditions propagate the existing World-validator reason codes;
- no blocked effect produces a ledger entry or Core change;
- a completed run is not automatically a passing M3 receipt, because the M3
  gate separately requires at least one admitted and one blocked effect; and
- exact replay reconstructs the proposals, clarifications, authority and
  capability results, effect receipts, World ledger, validator receipts, Core,
  and run hash.

The retained fixture, successful preparation consequence, and unresolved
transmission are all labeled `development_fixture_non_evidence`. They are not
model outputs, official delegations, observations of either counterpart
government, creative-EXCON quality evidence, or an end-to-end DATE episode.

### Alternatives, corrections, and disposition

- **Selected:** retain open proposal language while authoring a deterministic
  effect graph for the no-model tracer. This tests open transport and strict
  admission without pretending the controller can interpret policy prose.
- **Selected:** isolate failure at the effect and dependency level. This keeps
  supported work attributable while preventing descendants from using a basis
  that never became valid.
- **Selected:** use a separate effect-authority artifact bound to the resolved
  effect. This prevents institutional decision support from being mistaken for
  implementation authority.
- **Selected:** let EXCON propose and D64 admit. This preserves open causal
  narration without giving generated or fixture text direct write access to
  World truth.
- **Rejected:** require proposals to select one of the historical five action
  families. That would reintroduce D47's closed DATE boundary and make novelty
  a mechanical failure.
- **Rejected:** ask the controller to parse the proposal, split it, answer its
  clarification, infer authority, or repair a consequence. Those operations
  would hide substantive judgment inside deterministic infrastructure.
- **Rejected:** treat the President's D68 decision or Required Confirmations as
  sufficient effect authority. They prove record completeness at that stage,
  not a general delegation for every downstream effect.
- **Rejected:** let EXCON create a missing entity, capability, causal parent, or
  represented-Room choice so that a proposal can succeed. This would turn
  adjudication into retroactive permission.
- **Rejected:** require every consequence to change the Core. Ledger-only
  observations and consequences are valid when they do not change future
  permissions, quantities, clocks, terminals, or typed measures.
- **Deferred:** live proposal extraction, model-generated consequences,
  plausibility assessment, sourced final effect-authority maps, optional
  handlers or analysis tags, and the final authored-seeded-creative split
  remain later freeze gates.

Implementation review added several durable corrections. Proposal actors now
must match the actor in every claimed capability. Consequences must disclose
all capability and patch-target entities in their exact Core read. A successful
dependency whose consequence establishes a required causal basis must appear
in the dependent consequence's World-parent lineage. Static reference defects
fail before execution, while state-dependent causal failures remain visible in
the effect receipt. The tracer also separates run completion from the M3
mixed-outcome acceptance gate so a deterministic all-blocked run cannot be
mistaken for milestone success.

D69 creates no new ADR. It is the measured implementation checkpoint for the
open proposal, state-bounded EXCON, Core-ledger, and U.S.-first sequence already
locked by D48-D50 and D65. We preserve its choices and rejected alternatives
here because these small boundaries are part of the contest narrative: the
Room may propose openly, but no generated sentence becomes authority,
capability, causality, or World truth by assertion.

### Gate and next milestone

D69 closes Milestone 3 at its declared no-model bridge scope. We now have a
ratified U.S. institutional graph, one replayable information-to-decision
cycle, and one replayable decision-to-consequence bridge. We still do not have
model-mediated seat work, creative EXCON, a complete two-cycle episode, an
actor-specific Counterpart Room, a matched comparison, or public contest-result
evidence.

Milestone 4 must join the retained D68 cycle and D69 bridge to the D64 matched
weather transition. It must preserve persistent U.S. seat identity and memory,
return admitted endogenous consequences through authorized Cycle 2 inputs,
admit the identical matched weather event and paired State Patch, produce an
attributable Cycle 2 reassessment and second decision, adjudicate the second
proposal or explicit non-action, distinguish a substantive terminal from an
invalid abort, and replay the complete two-cycle bundle in a fresh process.
Development Counterpart Fixtures remain non-evidence during this mechanical
gate. Live model calls and actor-specific counterpart replacement remain later
milestones rather than shortcuts around the two-cycle contract.

## D70. Compose the same U.S. Room across two DATE cycles (MEASURED TWO-CYCLE CHECKPOINT)

### Exact executor and artifact identities

Milestone 4 ran in a fresh process against exact executor revision
`67e8ec51281466aacb7b907c1c6212dde817e7c0`. That revision independently
matched the pushed topic-branch head before the retained receipt was generated.
The receipt binds:

- source-register hash
  `73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f`;
- D67-ratified U.S. Charter hash
  `fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2`;
- D68 Cycle 1 receipt hash
  `7487b1604dd8426c74631b21590326190d95a476e90220924397f08fec93a186`;
- D69 proposal-bridge receipt hash
  `cf78c92190e8b2739923c0977a0af316b332643b563d0ad4818b13048c726ec4`;
- D64 DATE receipt hash
  `4a582d72b6d8ff753c3e06adea4d36aef3c3b39b5284e4050ce9ed35e39815e3`;
- D64 World-profile hash
  `64f4009b91381b27f43e76f61cd929f989b7ca866bdab7e8eb28326403e0c477`;
- authored Cycle 2 fixture hash
  `dc99ac7a92e2402451973041325f670c0bb626058068a221f695ee4cd0d9119f`;
- complete episode-fixture hash
  `2a7d484d4096e598cee64cbf30c60344c3cca57a7f9cf52f384e6b0ce8f94e66`;
- deterministic episode-run hash
  `83a143f8712d9b6d012b6dde2f03940062f63b961ad68ccf5bb3b3ae25660597`;
  and
- canonical receipt hash
  `7e5dbd8216d9ea9abc55cc457ceae3df44e3ee4192459012a5459944bddfe6ee`.

Independent canonicalization after removing the receipt self-hash reproduces
the exact receipt hash. Exact replay reconstructs both Room cycles, the bridge,
per-seat memory, final adjudication, World Core, event ledger, validation
receipts, projections, phase order, and run hash.

### The episode the tracer actually ran

The trace is one bounded U.S.-first episode, not three disconnected tests. It
executes eight ordered phases:

1. The D64 uncertain weather forecast enters a newly initialized World. It is
   bound to the exact raw forecast input already routed through D68's
   specialist path, and it leaves the Core unchanged.
2. The exact D68 Cycle 1 reruns through the ratified U.S. Charter. Fourteen
   active seats receive authorized information, eight groups produce their
   declared products, the PC produces the integrated six-domain Policy
   Package, and the NSC route records a supported presidential decision.
3. The exact D69 bridge reruns. Its preparation effect remains admitted, and
   `EXCON_CONSEQUENCE_PREPARATION_001` enters this episode's World ledger. The
   unresolved dependent transmission remains blocked and produces no event.
4. The matched D64 weather event is admitted against the episode's current
   Core with a newly instantiated, current-Core-bound copy of the exact D64
   patch template. Its two operations atomically narrow the U.S.-enabled ridge
   observation window and the Himaldeshi-controlled South Pass support window.
5. The exact D64 confirmation is admitted after the patch. The World now
   projects U.S. observation as `intermittent` and Himaldesh support as
   `restricted`, while the strategic crisis remains open.
6. The same U.S. Charter runs Cycle 2 with the same fourteen active seats,
   group graph, action class, presidential route, and confirmation rules. A
   common World input carries the admitted endogenous preparation consequence
   separately from the matched weather event and confirmation. A private
   intelligence input retains the preparation-without-transmission status.
7. The Cycle 2 Policy Package and NSC record explicitly bind the prior decision
   ID and hash, all three changed-evidence IDs, and the barrier's exact Core
   version and hash. Their declared disposition is `condition`: retain
   preparation, withhold transmission, and reassess after recipient or access
   conditions change.
8. Development EXCON records the unresolved transmission as explicit
   non-action and proposes a ledger-only consequence. The D64 validator admits
   that consequence without a State Patch, Core change, new capability, or
   represented-Room decision. Its receipt is delivered to every active Cycle 2
   seat, and the complete episode then replays exactly.

The final World ledger therefore contains, in order, the forecast, admitted
preparation consequence, weather event, weather confirmation, and final
non-action consequence. It does not contain the blocked transmission. The
Core advances once, only through the exact matched weather patch.

### One full Room, not a three-agent council

D70 exercises the institutional correction that motivated the pivot. The
tracer does not replace the U.S. process with a President and two generic
advisers. It compiles the complete D67 Charter and retains fourteen active seat
identities across both cycles, including the President, Vice President,
departmental principals, legal advisers, intelligence leaders, military
advice, and the triggered theater commander. Eight declared groups retain
their specialist, synthesis, PC, and NSC roles.

Each seat's episode memory records the exact delivery IDs it received in Cycle
1 and Cycle 2. The second cycle does not create fresh aliases, merge offices,
or reset input history. The common confirmation reaches every active seat only
because the Charter authorizes that information class and the Cycle 2 fixture
declares its exact ledger parents. Private preparation status remains on its
separate information path.

This is mechanical identity and delivery-history evidence. It does not yet
show how a live model inhabits an office, reasons from memory, disagrees,
changes its advice, or influences the final decision. The important result is
that the architecture no longer prevents those institutional questions from
being asked.

### Matched pressure and endogenous consequences stay distinct

The episode carries two different sources of Cycle 2 change. The D69
preparation consequence descends from the Room's own first decision and is
therefore endogenous. The weather deterioration and confirmation are authored
matched pressure and remain byte-identical at the template and semantic
operation level across future compared conditions. They enter one common
crisis picture but retain separate parent IDs and provenance fields.

This separation preserves the point of D54. A later matched comparison can
hold the material weather problem fixed while allowing different first-cycle
decisions to create different endogenous histories. Matching does not mean
forcing both conditions onto one scripted trajectory, and endogenous
consequences do not get mistaken for the matched treatment.

### Open policy with strict adaptation receipts

Cycle 2 remains authored development data because this milestone makes no live
model call. Its Policy Package still covers all six D45 domains and retains
open content rather than selecting from a closed DATE action family. The
controller neither writes the changed policy nor decides that `condition` is
the right response. It only verifies that the authored reassessment is
attributable to the exact prior decision, changed evidence, current Core, and
allowed disposition vocabulary.

This balance is deliberate. Novel policy content remains admissible, but a
claim of adaptation needs more than different prose. Without the prior
decision hash, changed-evidence IDs, Core identity, and explicit disposition,
the second answer cannot count as an attributable response to the changed
World. The strict fields establish lineage, not policy correctness.

### Final non-action and World ownership

The final unresolved transmission is not silently dropped. The episode retains
its source Policy Package component, Cycle 2 decision record, original
language, reason codes, causal World parents, adjudicator identity, and proposed
consequence. Development EXCON is not a Room seat, and the record declares no
represented-Room decision actor.

The final consequence enters the ledger only after the World validator checks
its envelope, references, causal parents, episode time, source, and collision
boundary. Because it carries no patch, its validation receipt proves that the
Core hash and version do not change. Delivery closes the deterministic episode
without turning non-action into a capability, permission, or prediction.

### Failure, terminal, and replay boundaries

The loader rejects a changed source, Charter, D68 receipt, D69 receipt, D64
receipt or profile, artifact hash, institutional graph, Cycle identity,
lineage, or final-adjudication boundary before execution. During a run, a stale
Cycle 2 Core binding, unsupported second decision, seat-identity change,
retroactive consequence, or rejected World transition stops later phases and
is recorded as an abort reason.

A substantive early terminal is separate. It requires a non-open terminal
predicate in the frozen Core before Cycle 2 and no controller failure. A
fixture flag, exception, missing input, budget exhaustion, or failed barrier is
not a strategic terminal. The retained D70 episode remains open and completes
both cycles, so it supplies no observed early-terminal case.

Replay reruns the exact D68 cycle and D69 bridge instead of trusting their
retained prose summaries, initializes a fresh D64 World, re-instantiates the
weather patch against the same episode Core, reruns Cycle 2, re-admits the final
consequence, and requires the complete receipt to hash identically.

### Review corrections and rejected shortcuts

The pre-receipt standards-versus-spec review found and repaired several
boundaries that the first passing trace did not expose:

- malformed nested World parents could escape as a raw type error rather than
  a strict fixture rejection;
- Cycle 2 could remove an institutional product while still loading;
- a final event could use an arbitrary event kind despite being labeled an
  EXCON consequence;
- final adjudication could point to the Policy Package rather than the actual
  Cycle 2 decision;
- a final consequence could omit every causal World parent; and
- the outer tracer bound upstream identities only transitively through the
  episode-fixture hash instead of exposing them directly in the receipt.

The reviewed loader now validates nested types before set construction,
requires the exact Cycle 1 action class, ordered group-to-schema structure, and
confirmation structure in Cycle 2, requires final `excon_consequence` kind and
source, binds the exact NSC decision, requires nonempty causal lineage, and
prints every major upstream identity in the outer receipt.

The following alternatives remain explicitly rejected:

- **Rejected:** run Cycle 2 with a smaller council or a fresh set of generic
  agents. This would erase the institution whose information and adaptation
  path the contest entry is meant to inspect.
- **Rejected:** copy the D69 bridge ledger entry or D64 weather outcome from a
  prose summary. The episode reruns each source and admits the exact event and
  patch through the existing validator.
- **Rejected:** let the blocked transmission appear in the World because its
  preceding preparation succeeded. Dependency success does not resolve the
  transmission's missing recipient channel.
- **Rejected:** collapse endogenous preparation and matched weather into one
  unlabeled Cycle 2 narrative. That would make causal divergence impossible to
  distinguish from common pressure.
- **Rejected:** call any different Cycle 2 answer adaptation. The second record
  must bind the prior decision, changed evidence, and current Core.
- **Rejected:** treat controller failure, missing evidence, or a call budget as
  a substantive crisis terminal. Those are aborts and remain visible as such.
- **Rejected:** count this authored no-model trace as a DATE evaluation episode
  or as evidence that a model behaves authentically inside the Room.

D70 creates no new ADR. It is the measured implementation checkpoint for the
two-cycle horizon, hybrid pressure, persistent Room identity, U.S.-first work
order, and deterministic admission boundaries already locked by D53-D54 and
D65. We preserve the selected mechanics, corrections, and rejected shortcuts
because they are part of the entry's narrative: the same institution receives
different evidence, revisits its own prior decision, and acts again, while the
World remains the sole owner of consequences and state.

### Evidence boundary and next milestone

The Cycle 2 products, reassessment, final adjudication, and counterpart outputs
are authored `development_fixture_non_evidence`. D70 proves deterministic
composition, institutional identity, selective delivery, causal separation,
state admission, failure classification, and replay at those fixed bytes. It
does not prove model advice, office fidelity, model memory, creative EXCON
quality, Himaldeshi or Olvanan Room behavior, matched-condition effects,
evaluation validity, nuclear-escalation behavior, predictive realism, or a
contest result.

D70 closes Milestone 4 at that exact mechanical scope. Milestone 5 must replace
the Himaldesh and Olvana Development Counterpart Fixtures with minimum
actor-specific Rooms under their own Charters before any live episode claim.
Those Rooms need episode-relevant institutional graphs, information rights,
products, and decision paths, but they do not receive co-equal implementation
or presentation depth. The U.S. Room remains the focal evaluated institution.
Live model calls, creative EXCON, the selected U.S. comparison, frozen measures
and probes, paid runs, the Nuclear War adapter, Packet claims, and microsite
results remain later gates.

## D71. Present the exact minimum Counterpart Charter candidates for one batch gate

**Status:** MEASURED CANDIDATE CHECKPOINT. The source and Charter candidates
pass strict, no-model structural checks. They remain unratified and
unimplemented.

**Date:** 2026-08-26

### Why this checkpoint exists

D65 requires actor-specific Himaldesh and Olvana Rooms before any live episode
claim, while D70 still obtains both governments' outputs from Development
Counterpart Fixtures. Milestone 5 therefore needs a stable institutional
contract before code can replace those fixtures. It cannot let implementation
convenience choose Olvanan party procedure, add a Himaldeshi commander, or make
the two governments use a generic council.

The checkpoint freezes four candidate review identities and one lossless human
review. It does not ratify them, compile a Room, execute a seat, call a model,
or modify the D70 episode. One owner batch decision is the next gate because
the Olvana procedure and both complete Charter identities materially affect the
represented governments.

The exact canonical candidate identities are:

- Himaldesh source register:
  `6a2ad9ea06a462c3283ecdc8a14dccee0ffe9830f20bf961deddb830ed308f25`;
- Himaldesh Charter:
  `c7184d1866913782fce5afea3edf1cc3a26942699973eb232e3bbee1782cb822`;
- Olvana source register:
  `932c12452ccb3373ccf4fc07c7d91f290d6812d1d8d1b227f49f0cf8eb4e06d5`;
  and
- Olvana Charter:
  `0aa48c3cb8e2980324b3db6d4c5426fb5ff67f746775728a0b00f38897fe389a`.

### Source refresh and evidence boundary

The 2026-08-26 refresh uses five official DATE pages for Himaldesh, two
official DATE pages for Olvana, and the official DATE home page for
living-product context. Each register separates source-supported facts from
WOPR design inferences and explicit gaps. A source that names an office does
not thereby supply a machine meeting procedure, vote, veto, confirmation, or
effect authority.

The Himaldesh materials support a Prime Minister-led parliamentary government,
a distinct President and Supreme Commander, Defense, General Staff, Strategic
Command, the Interior-to-Defense force relationship, and episode-relevant
finance, information, infrastructure, and civilian exposures. They do not
publish D27-D36's two-lane graph, six-product Cabinet process, targeted review,
dissent disposition, or Joint Executive sequence. The candidate labels those
mechanics as design inferences rather than DATE facts.

The Olvana materials support party primacy, true executive authority in the
party General Secretary, a politically influential military, a
President-chaired National Command Authority, five named NCA portfolios, a
Minister of National Security and Strategic Integration Department, Defense,
General Staff, and Interior relationships. They do not identify a stable
office-by-office Politburo Standing Committee crisis roster or a meeting,
quorum, voting, consensus, or party-to-NCA sequence. The candidate does not
manufacture those missing rules.

ODIN describes DATE as a living product. Candidate identity therefore binds
the retrieval date and source URLs. If the underlying source changes before
pilot freeze, the Charter must receive a new identity and review; the code may
not treat a current page as timeless evidence.

### Shared counterpart envelope without symmetric politics

Both actors use `actor-source-register.v0.1` and
`counterpart-room-charter.v0.1`. The common envelope lets one harness verify
persistent seats, information classes, permissions, group dependencies,
products, routes, confirmations, blocked actions, gaps, failures, and replay.
It does not require the two actors to share a roster, graph, decision rule, or
political center.

The deterministic controller may load, deliver, schedule, collect, validate,
route, and record. It may not write advice, integrate policy, resolve dissent,
choose a decision, infer a party consensus, supply a professional or executive
confirmation, create effect authority, or mutate World state. Independent
groups may run concurrently only when their declared inputs are frozen and
their active seats do not overlap. Shared seats serialize through declared
barriers, and collection remains in Charter order.

Every actor input is either in the Common Crisis Picture, a seat-authorized
private input, an attributable product, or a logged disclosure. A union prompt,
hidden World state, cloned shared seat, undeclared group, or inferred delivery
right fails closed. Advice, decision, confirmation, effect authority,
capability, consequence proposal, and World admission remain different
artifacts.

### Himaldesh candidate

The first-episode Himaldesh Room activates eleven persistent seats: Prime
Minister; President; Defense; General Staff; Strategic Command; External
Affairs; Interior and Border Security; Finance and Economic Resilience;
Information and Communications; Civil Infrastructure and Continuity; and
Humanitarian and Social Cohesion. This serializes the D27-D36 design already
locked in conversation. The six-portfolio path remains selected because the
five-seat fallback trigger has not occurred.

Six single-seat portfolio groups each produce a separate five-part Portfolio
Product. Their products feed a Prime Minister-authored Cabinet Policy Draft and
version-bound targeted review. Advisory disagreement remains visible and
requires an explicit disposition. The Command Cell separately combines the
President, Defense, General Staff, and Strategic Command. Defense remains one
persistent bridge seat rather than policy and command copies.

The selected first action class is
`partner_support_request_and_recapture_planning`. The Joint Executive path
receives both lanes, the affected portfolio positions, the Prime Minister and
President positions, Defense feasibility, and General Staff professional
assessment. A no-model development trace may reproduce
`HIM_OUTPUT_SUPPORT_REQUEST_001` only after that attributable Room decision.
The old fixture bytes remain a migration target, not evidence of Himaldeshi
behavior.

The Interior gate remains local to a named transfer of an
Interior-administered force into Defense operational control. It asks whether
the handoff, continuing domestic coverage, and reversion arrangement are
executable. It does not let Interior choose military objectives or national
policy.

Strategic Command is active because nuclear escalation is reachable. The
Charter keeps readiness, signaling, use, authentication, and declared
no-first-use distinct. A strategic component requires both executive
positions, Defense and Strategic Command inputs, and a separate presidential
confirmation. Direct conventional force employment remains blocked because
the source set does not establish an episode operational-commander seat;
General Staff advice cannot impersonate one.

### Olvana candidate

The first-episode Olvana Room activates nine persistent seats: party General
Secretary; President and NCA chair; Minister of National Security and SID;
Foreign Affairs; Public Information; Finance and Economic Affairs; Interior
and Public Security; Defense; and General Staff. The candidate represents the
source-grounded General Secretary rather than inventing five to nine PSC
agents.

The five named NCA portfolio seats first produce attributable positions. The
controller bundles them in declared order without summarizing, voting, or
assigning vetoes. Defense then joins a separate command assessment through a
shared-seat serialization barrier. The Minister of National Security uses the
complete portfolio bundle and command assessment to author integrated options
while retaining sources, contradictions, dissent, dependencies, stop
conditions, and gaps.

The President chairs NCA review and supplies the formal command confirmation
for the exact military-posture component. The General Secretary receives the
complete NCA record and owns final represented party-state direction. This
ordered party-NCA route is a labeled design inference from DATE's distinct
institutions. It is not claimed as published Olvanan procedure.

The first action class is `limited_ridge_hold_and_integrated_pressure`. A
no-model development decision may retain a limited hold, defensive field
preparation, bounded public posture, withdrawal conditions, and no-further-
advance constraint. A separate deterministic authored World projection, not
the Room, produces `OLV_OUTPUT_RIDGE_POSTURE_001` for the U.S. information
path. Exact equality with the old fixture is migration evidence only.

### Corrected Olvana nuclear boundary

The refreshed Olvana military page is dated 2026-01-13. It describes public
non-initiation and possible nuclear use if Olvana faces certain defeat with
expected regime change or is attacked by a nuclear power. The refresh did not
re-establish the older preserved wording about some policymakers considering a
small coercive nuclear use.

The candidate records that discrepancy as
`OLV_GAP_LIMITED_USE_SOURCE_DRIFT`. Module 13's limited-use debate is not
runnable until a pinned source version and owner decision resolve it. This
correction does not remove nuclear risk from the arena; it prevents a Setup or
Room from receiving an option through an unverified sentence.

Every Olvanan strategic or nuclear action separately fails under
`OLV_GAP_NUCLEAR_DECISION_PATH`. The current sources describe posture and
possible conditions, but they do not establish the complete launch forum,
information path, confirmation map, authenticated route, or effect authority
needed for execution. A PSC collective vote also fails under
`OLV_GAP_PSC_COMPOSITION`.

### Alternatives retained and their dispositions

- A generic three-agent counterpart council remains rejected because it erases
  the actor-specific institutions that the pivot is meant to represent.
- Reusing the U.S. topology for either counterpart remains invalid because
  public U.S. procedure does not establish Himaldeshi or Olvanan procedure.
- Reusing Himaldesh's split executive graph for Olvana remains invalid because
  Olvana's party center, NCA, SID, and formal presidency create a different
  institutional problem.
- A President-only Olvana decision remains rejected because DATE places true
  executive authority with the General Secretary.
- A General Secretary-only action without NCA and command products remains
  rejected because it would make the source-named national-instrument and
  command institutions decorative.
- Invented PSC members, quorum, weighted votes, or consensus remain blocked
  because the source does not supply them.
- Universal portfolio vetoes remain rejected because subject expertise does
  not create general blocking authority.
- Keeping the Development Counterpart Fixtures as final provenance remains
  invalid because authored scaffolding is not a government or Room.
- Giving both counterparts co-equal implementation, evaluation, and public
  treatment remains outside the submission floor. Their decisions must be
  attributable and consequential, but the U.S. Room remains the focal object.

### Candidate validation and correction record

All four files parse as strict JSON. A temporary independent audit verifies
canonical identity; source-register hash binding; bidirectional source, fact,
and inference references; global identity uniqueness; actor identity;
seat-group reciprocity; permission and entitlement closure; product, route,
confirmation, and blocked-gap closure; no hidden World entitlement; and
acyclic dependencies.

The audit initially found one missing reverse source-to-fact link in each
actor register. `HD_FACT_POLITICAL_SYSTEM` was not linked back from the
Himaldesh military card, and `OLV_FACT_PRESIDENT_COMMAND` was not linked back
from the Olvana military card. Both registers and their dependent Charter
hashes were corrected before this checkpoint. The final audit passes at the
four canonical identities above.

The retained counts are:

- Himaldesh: five sources, eleven facts, nine inferences, three gaps, eleven
  seats, two deterministic services, seventeen information classes, sixteen
  permissions, ten groups, five product schemas, three routes, five
  confirmations, and one blocked action class.
- Olvana: three sources, twelve facts, eight inferences, six gaps, nine seats,
  two deterministic services, fifteen information classes, fourteen
  permissions, five groups, five product schemas, one route, three
  confirmations, and three blocked action classes.

### Ratification, implementation, and claim boundary

One owner decision must accept or revise the four exact candidates as a batch.
Acceptance covers the dated source cards, fact-versus-inference labels,
objective vectors, represented rosters, group graphs, information paths,
decision routes, confirmation maps, blocked actions, and declared gaps. A
separate receipt will bind the accepted commit and four canonical hashes
without changing candidate bytes.

After ratification, Milestone 5 proceeds in three bounded slices: a generic
strict counterpart loader; deterministic actor traces with fail-closed tests;
and D70 composition in which counterpart Room receipts replace fixture
provenance. Historical D68-D70 artifacts remain immutable. Composition must
prove exact counterpart-output identity and bytes before delivering them to
the unchanged U.S. Watch inputs.

D71 creates no live or behavioral evidence. It proves only that the proposed
source and Charter bundles are internally complete enough for one lossless
owner decision. It does not establish real Himaldeshi or Olvanan procedure,
model judgment, creative EXCON quality, institutional authenticity, DATE
execution, matched effects, nuclear behavior, predictive realism, or a contest
result. No model call, provider cost, Packet rewrite, microsite result, or
public claim is authorized by this checkpoint.

## D72. Ratify the exact minimum Counterpart Charter bundle

**Status:** RATIFIED CHECKPOINT. The exact D71 candidate identities are the
accepted implementation basis for Milestone 5.

**Date:** 2026-08-26

### Owner decision and exact identity

The owner replied `ratified` to the one batch question over the four exact D71
canonical hashes. The accepted candidate commit is
`8d65a6e05ed264193ddda3fbd5daea7bc1c88dee`, independently verified on remote
branch `glenn/chinatalk-m5-counterpart-rooms` before the decision.

The accepted identities remain:

- Himaldesh source register
  `6a2ad9ea06a462c3283ecdc8a14dccee0ffe9830f20bf961deddb830ed308f25`;
- Himaldesh Charter
  `c7184d1866913782fce5afea3edf1cc3a26942699973eb232e3bbee1782cb822`;
- Olvana source register
  `932c12452ccb3373ccf4fc07c7d91f290d6812d1d8d1b227f49f0cf8eb4e06d5`;
  and
- Olvana Charter
  `0aa48c3cb8e2980324b3db6d4c5426fb5ff67f746775728a0b00f38897fe389a`.

`COUNTERPART_CHARTER_RATIFICATION.json` separately binds the candidate commit,
both actor bundles, review surface, Milestone 5 scope, U.S. focal identity, and
claim boundary. Its canonical hash is
`bbab62ea681f2e513407b926de5adfbfaeb8e73baf5fb86ea34808b9fa524384`.
The exact-binding test first failed because the receipt did not exist, then
passed after the receipt was added.

### What the decision accepts

Ratification accepts the candidate's dated source cards, fact-versus-inference
labels, unweighted actor objectives, complete represented first-episode
rosters, deterministic services, information classes and permissions, group
graphs, product schemas, action routes, required confirmations, blocked action
classes, and explicit gaps as one implementation contract.

For Himaldesh, this means the eleven-seat D27-D36 structure: separate Prime
Minister and President; six Cabinet portfolios; separate Cabinet Policy and
Command lanes; one persistent Defense bridge; Prime Minister draft and
targeted review; visible dissent; Joint Executive closure; the local Interior
handoff gate; and no invented operational commander.

For Olvana, this means nine represented seats; an ordered five-portfolio NCA
bundle; one persistent Defense seat serialized into command assessment; SID
integration; President-chaired NCA review and exact command confirmation; and
General Secretary final represented party-state direction. PSC membership,
quorum, voting, weights, and consensus remain unrepresented rather than
guessed.

Ratification also accepts the corrected nuclear boundary. The older coercive
limited-use debate remains blocked as source drift. Every Olvanan strategic or
nuclear action remains blocked because no complete source-bound forum,
information path, confirmation map, authenticated route, or effect authority
exists. The decision does not remove nuclear risk from the World or from other
Rooms' assessments.

### What the decision does not establish

The receipt proves owner acceptance of exact bytes. It does not prove that the
selected machine procedures are official Himaldeshi or Olvanan practice, that
either Room executes, that a model inhabits any office, that authored fixture
products resemble government behavior, that creative EXCON is plausible, or
that a DATE episode or comparison has run.

Acceptance does not change the U.S.-first scope. The counterparts must produce
attributable crisis decisions and consequences before a live episode, but the
complete U.S. Situation Room remains the focal evaluated institution and the
primary public replay.

### Implementation authority and retained gates

D72 authorizes only Milestone 5's deterministic no-model implementation under
module 19. Work proceeds through three bounded slices:

1. load and strictly validate both source and Charter bundles through one
   shared counterpart envelope;
2. execute separate authored Himaldesh and Olvana traces with actor-specific
   graphs, local failures, exact replay, and no model calls; and
3. compose their receipt-bound outputs into the unchanged D70 U.S. tracer,
   rejecting the old fixtures as final provenance while preserving exact
   output bytes during migration.

Each new behavior begins with a failing public-seam test. Historical D68-D70
artifacts remain immutable. A later executor-bound Milestone 5 receipt must
bind the ratification, source and Charter identities, actor fixtures and runs,
output mappings, D70 source receipt, final composition, failures, and replay.

Live model calls, creative EXCON, provider spending, the compared U.S.
condition, measure and probe freeze, matched pilot, Nuclear War adapter, Packet
rewrite, microsite results, publication, and contest submission remain later
gates. D72 creates no new ADR because it accepts the exact D71 representation
rather than changing the locked design.

## D73. Execute and retain both minimum Counterpart Room traces

**Status:** MEASURED ACTOR-TRACE CHECKPOINT. The ratified Himaldesh and Olvana
graphs execute and replay as deterministic development fixtures; D70
composition remains open.

**Date:** 2026-08-26

### Exact executor and retained identities

The trace executor was committed and pushed at
`b165acc206b374d87fcd0e3b9e1ba32c6b375d39`. An independent remote read
resolved branch `glenn/chinatalk-m5-counterpart-rooms` to the same revision
before either retained receipt was generated. Both traces load D72 receipt
`bbab62ea681f2e513407b926de5adfbfaeb8e73baf5fb86ea34808b9fa524384`
and the unchanged four ratified source and Charter hashes.

The retained Himaldesh identities are:

- Room fixture
  `d6f9eb6a546cdf5d6d512511eef8c46c4da0d2c9175e28c7c080ce5d385b406c`;
- run `4a1c917aa4e45bbd009bb1fe008ceb932997716c60b759b5160944327714a38b`;
- canonical receipt
  `98a006d17fe23c40d80ec6804da45a192106363d8b03fc7b096ce79d3cbfefc9`;
  and
- exact `HIM_OUTPUT_SUPPORT_REQUEST_001` record
  `317c977a6656a4125e28e025323363a386dddcb394fe8bcf81e94f2f71d7aea2`.

The retained Olvana identities are:

- Room fixture
  `a922444f415f0b592e5a657f2940524b6f01276c85a3280cb60782f5e8fc1a4b`;
- run `c6d212f7ed80ab77c2241920ec574d8577d7746a8e68f8ccef852bd3ad392a3a`;
- canonical receipt
  `5586513c594acd6d4acab97978b2624c2917a6a8d49bb81be55818b3c433d547`;
  and
- exact `OLV_OUTPUT_RIDGE_POSTURE_001` record
  `c1362fc0bdab5b9f18dd70f7750911bb31d88004d360a8325115d28c20ff27fe`.

Independent canonicalization after removing each self-hash reproduces both
receipt hashes. Exact retained-receipt tests regenerate both receipts from the
source, Charter, ratification, fixture, and executor identities.

### What the Himaldesh trace executed

The fixture authors eleven Watch inputs, ten group products, and two
professional confirmations as `development_fixture_non_evidence`. The trace
activates all eleven ratified seats. Six independent portfolio groups and the
President-led Command Cell run together from frozen inputs because they share
no active seat. Charter ordering then serializes the Prime Minister's Cabinet
Draft, targeted Cabinet Review, and Joint Executive decision.

The run retains 111 attributable deliveries, four graph waves, ten accepted
attempts, the Prime Minister and President positions, visible Interior dissent
and disposition, Defense feasibility, General Staff assessment, the selected
decision route, and zero failures. The output comes from the accepted Joint
Executive decision record. No direct conventional force employment or
strategic component runs, and no World effect is admitted.

### What the Olvana trace executed

The fixture authors nine Watch inputs, five group products, and three posture
confirmations as non-evidence. The trace activates all nine ratified seats and
executes five serial waves: ordered NCA portfolio positions; President,
Defense, and General Staff command assessment; SID integration; President-
chaired NCA review; and General Secretary party-state direction.

The run retains 49 attributable deliveries, five accepted attempts, the five
ordered portfolio positions, contradictions and dissent, President command
confirmation, Defense feasibility, General Staff assessment, the selected
decision route, and zero failures. The Room decision does not author a U.S.-
visible observation. A separate deterministic World-owned projection emits
the exact ridge-posture record, and the trace admits no World state change.

### Failure corrections and rejected shortcuts

The implementation began with public-seam red tests. The first execution test
failed because no counterpart Room API existed. The first failure suite then
found that a missing confirmation still allowed output and that changed
Olvanan projection bytes were not rejected. The decision boundary now
suppresses every output and projection after a local decision failure and
binds each migration output to exact canonical bytes.

Additional tests retain a missing Himaldeshi dissent disposition, reordered
Olvanan portfolio positions, route mismatch, all four ratified blocked-action
gaps, and each Charter-declared local failure effect. A subprocess test first
exposed a package-import warning; the CLI tracer remains an internal module
rather than an eager package export, so fresh-process stderr is empty. A
focused type check also caught ambiguous product-content narrowing before this
checkpoint. No accepted source, Charter, or ratification byte changed.

The following shortcuts remain rejected:

- The controller does not write a portfolio position, policy integration,
  dissent disposition, decision, confirmation, or party consensus. Authored
  fixture products exercise the machine contract only.
- The two actor graphs are not made symmetric. Himaldesh uses safe first-wave
  concurrency and split-executive closure; Olvana uses its ratified serialized
  party-NCA path.
- The old D68-D70 counterpart fixture records are not acting governments.
  Exact output equality is migration evidence only.
- A Room decision does not become effect authority. Himaldesh's output is a
  request record; Olvana's U.S.-visible output remains a World-owned mapping.
- Unsupported direct force, strategic, limited-use-debate, and PSC paths stay
  blocked at their exact D72 gaps rather than receiving plausible filler.

### Verification and remaining gate

The actor implementation gate reports 89 passing counterpart and U.S.
Charter/Cycle regressions, 15 focused pre-receipt execution and replay tests,
and two exact retained-receipt reconstructions. Ruff, exact touched-file
formatting, focused Pyright, strict JSON, clean subprocess stderr, Git
whitespace, and the 150-line active implementation and test limit pass.

D73 proves source-bound fixture execution, local failures, exact output
migration, receipt identity, and replay. It does not measure a model, real
government behavior, official procedure, institutional authenticity, creative
EXCON, a World consequence, nuclear escalation, a complete DATE episode, a
matched comparison, or contest performance. Milestone 5 remains open until a
new composition receipt treats these two Room receipts as the counterpart
causal sources, rejects the old fixtures as final provenance, preserves the
exact D70 U.S. run apart from counterpart provenance, and replays in a fresh
process. D73 creates no new ADR because it measures the D72 and module 19
contract without changing it.

## D74. Compose the Counterpart Room receipts into the exact U.S. episode

**Status:** MEASURED MILESTONE 5 COMPOSITION CHECKPOINT. The exact Himaldesh
and Olvana Room receipts now supply final counterpart provenance for the
unchanged D70 U.S. two-cycle trace; the deterministic no-model Milestone 5
contract passes.

**Date:** 2026-08-26

### Selected migration architecture

The composition had two requirements that cannot be collapsed into one
artifact identity. D70 must remain an exact retained U.S. run, and D73's Room
receipts must replace D70's embedded development counterpart fixtures as the
final source of counterpart provenance. Editing the historical Cycle 1 fixture
would change its hash, the enclosing two-cycle fixture, and the D70 run. Calling
that rewritten run an exact D70 replay would be false.

The selected implementation therefore wraps, rather than rewrites, D70. A
strict composition fixture loads the exact D70 receipt and both exact D73 Room
receipts. It binds each Room's source register, Charter, fixture, run, receipt,
decision route, output projection, source decision record, output identity and
canonical bytes, and every U.S. Cycle 1 Watch input that names the output as a
causal parent. Only after those checks pass does it rerun D70 and require the
exact retained D70 run hash plus canonical receipt equality.

The alternative of rewriting D70 was rejected because it would manufacture a
continuity claim after changing the retained input. The alternative of
continuing to name either old counterpart fixture as the acting government was
rejected because it would erase the actor-specific institutional work D71-D73
introduced. A fixture-byte equality check remains necessary migration evidence,
but it is not final counterpart provenance.

Repository inspection resolves the runtime boundary. The historical
`counterpart_fixtures` records are consumed by the U.S. fixture loader to check
actor, output, and causal references. The U.S. execution path consumes the
already-validated `watch_inputs`; it does not read `counterpart_fixtures` while
executing the group graph. The outer receipt therefore records the old records'
role as `fixture_load_reference_validation_only` and the U.S. runtime input
source as `cycle1_watch_inputs`.

### Exact executor and retained composition

The composition executor and development fixture were committed and pushed at
`ace150092f513b11d57c75cca92b52bbc8aca652`. An independent remote read
resolved branch `glenn/chinatalk-m5-counterpart-rooms` to that exact revision
before the retained receipt was generated.

The retained composition identities are:

- fixture `7a4aa15f1c3d93ee1f100c64ae06c3cb03093697e35f152651933aed6170bb37`;
- run `f4c6a2c9024eb7d0d1f00d0fc0cb4a1b2ab195827bc769f378b50b5429d258ef`;
- canonical receipt
  `4bc80ae10937fdc511451cd2b3df452604b6bc1c1c3ab709c1a810a71f67d0c0`;
- exact source D70 receipt
  `7e5dbd8216d9aabc55cc457ceae3df44e3ee4192459012a5459944bddfe6ee`;
  and
- exact unchanged D70 run
  `83a143f8712d9b6d012b6dde2f03940062f63b961ad68ccf5bb3b3ae25660597`.

The Himaldesh causal chain is source and Charter to Room receipt
`98a006d17fe23c40d80ec6804da45a192106363d8b03fc7b096ce79d3cbfefc9`,
route `HD_ROUTE_COMBINED_SUPPORT_PACKAGE`, decision record
`HD_PRODUCT_DECISION_001`, projection
`HD_PROJECTION_SUPPORT_REQUEST_001`, and output
`HIM_OUTPUT_SUPPORT_REQUEST_001`. That output is the named causal parent for
the common U.S. input plus the State, Defense, Justice, EOP legal, CJCS, and
theater private inputs.

The Olvana causal chain is source and Charter to Room receipt
`5586513c594acd6d4acab97978b2624c2917a6a8d49bb81be55818b3c433d547`,
route `OLV_ROUTE_RIDGE_POSTURE`, decision record
`OLV_PRODUCT_DECISION_001`, World-owned projection
`OLV_PROJECTION_RIDGE_POSTURE_001`, and output
`OLV_OUTPUT_RIDGE_POSTURE_001`. That output is the named causal parent for the
common U.S. input plus the DNI, CIA, Treasury, Energy, CJCS, and theater
private inputs.

The final counterpart records contain neither
`HIM_CYCLE1_REQUEST.development.v0_1` nor
`OLV_CYCLE1_POSTURE.development.v0_1`. Both old fixture forms are also negative
test inputs and fail before U.S. execution when substituted for a Room receipt.

### Corrections and verification

The first public-seam test failed because no composition API existed. Once the
wrapper existed, an exact-object comparison still failed even though the fresh
D70 run hash matched. Eleven `reason_codes` paths used tuples in the in-memory
run and lists after retained JSON loading. Canonical JSON bytes were identical.
The final gate therefore requires the exact D70 run hash and canonical receipt
equality, then embeds the exact retained JSON object in the outer receipt. This
normalizes an in-memory representation difference without weakening byte
identity.

The composition suite proves both exact positive and fail-closed paths. It
checks both Room receipts and all output mappings, exact U.S. Watch causal
parents, exact D70 run retention, absence of old fixture identities from final
counterpart provenance, current-executor binding, canonical self-hash, and
same-process plus fresh-process replay. It rejects either old fixture as a
Room receipt, changed Room output bytes, changed causal input bindings, and an
invalid executor revision before a composed run can be admitted.

Focused verification reports ten composition tests after the retained-receipt
check, 135 adjacent counterpart Charter/Room and U.S. Charter/Cycle/two-cycle
regressions, Ruff, focused Pyright, strict JSON, clean subprocess stderr, Git
whitespace, and the 150-line active source and test limit. The full repository
gate and independent review remain publication checks for the final Milestone 5
branch, not evidence that changes this measured receipt.

### Claim boundary and next gate

D74 closes only the deterministic no-model Milestone 5 contract. It proves
source-bound actor graphs can produce exact attributable outputs that enter the
unchanged focal U.S. trace with receipt-complete provenance. It does not prove
that a model behaves like any represented office, that the authored actor
products resemble official or real government behavior, that creative EXCON
produces plausible consequences, that any new World effect occurred, that
nuclear escalation was exercised, that the compared U.S. condition ran, that a
matched DATE episode completed, or that the system performs well in the
contest.

No provider call, credential read, paid experiment, creative EXCON run, Packet
rewrite, microsite rewrite, publication, or submission is authorized by this
checkpoint. The next implementation milestone is the bounded model-mediated
Room smoke and manifest freeze already ordered by D65. It requires its own
authority, exact runtime identity, cost boundary, and evidence receipt. D74
creates no new ADR because it measures the exact D72 and module 19 composition
contract without changing a locked design choice.
