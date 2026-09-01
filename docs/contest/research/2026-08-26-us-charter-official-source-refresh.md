# U.S. Charter official-source refresh

Status: Milestone 1 evidence note for the candidate `US_PUBLIC_2026Q3` Charter

Snapshot date: 2026-08-26

## Scope and method

I refreshed only public official U.S. sources needed to define the first-episode U.S. Room. I used current public law for stable office boundaries, NSPM-1 for the dated public NSC and HSC organization, agency mission pages for portfolio bounds, and dated public strategy for bounded persona posture. I did not use reporting, memoirs, current-officeholder biographies, classified material, or claims about actual crisis practice.

The source register records a fact about what a public source says separately from the inference used in the simulation. A public office title does not create delegation, a synthetic information entitlement is not an official distribution rule, and a DATE role label is not a U.S. government fact.

A batched reachability check returned HTTP 200 for 19 of the 20 canonical URLs. The official defense-media PDF returned HTTP 403 to the command-line client but opened through the official web reader, where its text was inspected. I treat that result as a client-specific access limitation, not as proof that the document is unavailable.

## Official source inventory

| Source ID | Public official source | Bounded use |
|---|---|---|
| `SRC_NSPM1_2025` | [NSPM-1](https://www.whitehouse.gov/presidential-actions/2025/01/organization-of-the-national-security-council-and-subcommittees/) | NSC and HSC function, public membership and attendance classes, Executive Secretary, PC consensus, separate presidential-attention poll, and referral. |
| `SRC_USC_50_3021` | [50 U.S.C. 3021](https://uscode.house.gov/view.xhtml?req=%28title%3A50+section%3A3021+edition%3Aprelim%29) | Statutory NSC mission and membership basis. |
| `SRC_USC_22_2651A` | [22 U.S.C. 2651a](https://uscode.house.gov/view.xhtml?req=%28title%3A22+section%3A2651a+edition%3Aprelim%29) | State office boundary. |
| `SRC_TREASURY_ROLE` | [Treasury role](https://home.treasury.gov/about/general-information/role-of-the-treasury) | Economic, financial, sanctions, markets, and financial-integrity portfolio. |
| `SRC_USC_31_321` | [31 U.S.C. 321](https://uscode.house.gov/view.xhtml?req=%28title%3A31+section%3A321+edition%3Aprelim%29) | Statutory Treasury office and general-authority boundary. |
| `SRC_USC_10_113` | [10 U.S.C. 113](https://uscode.house.gov/view.xhtml?req=%28title%3A10+section%3A113+edition%3Aprelim%29) | Statutory Secretary of Defense office and department relationship. |
| `SRC_ENERGY_MISSION` | [Energy mission](https://www.energy.gov/mission) | Energy and national-security portfolio boundary. |
| `SRC_NNSA_MISSION` | [NNSA mission](https://www.energy.gov/nnsa/about-nnsa) | Stockpile, nonproliferation, and nuclear or radiological response responsibilities. |
| `SRC_USC_28_503` | [28 U.S.C. 503](https://uscode.house.gov/view.xhtml?req=%28title%3A28+section%3A503+edition%3Aprelim%29) | Attorney General office boundary. |
| `SRC_DOJ_NSD_MISSION` | [Justice National Security Division](https://www.justice.gov/nsd/about-national-security-division-nsd) | Public national-security legal and law-enforcement portfolio. |
| `SRC_INTERIOR_MISSION` | [Interior mission](https://www.doi.gov/about) | Land, resource, trust, and community portfolio boundary. |
| `SRC_USC_6_112` | [6 U.S.C. 112](https://uscode.house.gov/view.xhtml?req=%28title%3A6+section%3A112+edition%3Aprelim%29) | Homeland Security office and department relationship. |
| `SRC_USC_42_300HH3` | [42 U.S.C. 300hh-3](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title42-section300hh-3) | Pandemic and biological-threat office mandate. |
| `SRC_USC_50_3024` | [50 U.S.C. 3024](https://uscode.house.gov/view.xhtml?edition=prelim&hl=false&req=granuleid%3AUSC-prelim-title50-section3024) | Objective all-source intelligence, competitive analysis, gaps, and disagreement. |
| `SRC_USC_50_3036` | [50 U.S.C. 3036](https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&jumpTo=true&num=0&req=%28title%3A50+section%3A3036+edition%3Aprelim%29+OR+%28granuleid%3AUSC-prelim-title50-section3036%29) | CIA foreign-intelligence functions and domestic law-enforcement exclusion. |
| `SRC_USC_10_151` | [10 U.S.C. 151](https://uscode.house.gov/view.xhtml?req=%28title%3A10+section%3A151+edition%3Aprelim%29) | CJCS principal military-adviser role and range of military advice. |
| `SRC_USC_10_163` | [10 U.S.C. 163](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title10-section163) | CJCS communications and oversight role with no military command. |
| `SRC_USC_10_164` | [10 U.S.C. 164](https://uscode.house.gov/view.xhtml?req=title%3A10+section%3A164+edition%3Aprelim) | Combatant-commander operational responsibilities, kept distinct from CJCS advice. |
| `SRC_NDS_2026` | [2026 National Defense Strategy](https://media.defense.gov/2026/Jan/23/2003864773/-1/-1/0/2026-NATIONAL-DEFENSE-STRATEGY.PDF) | Dated homeland, Indo-Pacific access, partner, deterrence, and strategic-stability posture. |
| `SRC_NSS_2025` | [2025 National Security Strategy](https://www.whitehouse.gov/wp-content/uploads/2025/12/2025-National-Security-Strategy.pdf) | Dated national-interest, economic, regional, partner, deterrence, and stability posture. |

## Facts carried into the Charter

The public roster is complete at the office-class level. The candidate retains the President, Vice President, State, Treasury, Defense, Energy, Pandemic Preparedness, Attorney General, Interior, Chief of Staff, National Security Advisor, Homeland Security, Homeland Security Advisor, DNI, CJCS, CIA Director, White House Counsel, Policy Assistant, and Counselor classes. It separately records the Executive Secretary as a deterministic service.

NSPM-1 supports the voting-member versus non-voting-adviser distinction used by the candidate. DNI, CJCS, and CIA remain non-voting advisers. White House Counsel, the Policy Assistant, and the Counselor remain non-voting invitee classes where applicable. The candidate does not turn the chair into a weighted voter.

Public law supports the portfolio bounds for State, Defense, Energy, Justice, Interior, Homeland Security, Pandemic Preparedness, DNI, CIA, CJCS, and a functional combatant-command contribution. The CJCS advisory seat cannot command. A functional Theater Commander can supply operational advice but does not inherit U.S. policy authority.

## Declared design inferences

The five U.S. objectives are an unweighted exercise vector, not an official ranking. The same applies to the first-episode activation values, the seven specialist and synthesis groups, persistent office memories across groups, the synthetic private briefs, selective disclosures, the raw-weather route, the integrated Policy Package, and the Required Confirmation schema.

The Watch and Executive Secretary are deterministic because transport and recordkeeping should not add model judgment. Deputy and staff roles stay represented inside their principal office products in this first slice. Making any represented role an independent seat would change the Charter identity.

The first candidate routes final policy direction to the President-chaired NSC. It does not encode a PC or department effect-level action route because the snapshot contains no crisis-specific delegation instrument. The PC produces an integrated recommendation and preserves each principal's policy position and separate presidential-attention position.

The ridge episode activates the functional Theater Commander because its authored weather path affects synthetic observation, access, logistics, support, readiness, and force protection. This is a functional exercise role and is not mapped to a real combatant command.

## Explicit gaps and conflicts

- The exact component-level authority, consultation, capability, and confirmation map belongs to the later Open Action Proposal milestone and blocks any effect-level route now.
- The public snapshot contains no selected additional portfolio mandate for the Policy Assistant or Counselor, so both remain unavailable rather than becoming generic advisers.
- Public sources cannot establish classified distribution, deliberation, or crisis procedure. The candidate makes no classified-fidelity claim.
- The fictional arena is not bound to a real command, installation, platform, or operational plan.
- The dated defense strategy uses an administration-specific department label that diverges from the current statutory office name. The Charter retains `Secretary of Defense` from 10 U.S.C. 113 and keeps the strategy wording only as dated posture context.

## Candidate identities and claim boundary

- Source register candidate SHA-256: `73dbda61ad01472abeadb5bd8aae2aead8a84b5596bbd00c5afbccba21d5051f`.
- U.S. Charter candidate SHA-256: `fe3837ad22a898218c3c298d1facf91e1ddd09b1a2d58dfc9a48b9d3c4bf83d2`.
- Both artifacts remain `candidate`. These hashes bind the review bytes but do not ratify the Charter.
- This refresh supports source-bound Charter review only. It does not establish Room feasibility, model behavior, actual U.S. procedure, DATE execution, or comparative performance.
