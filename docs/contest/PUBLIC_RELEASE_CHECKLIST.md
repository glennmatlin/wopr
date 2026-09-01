# Public release checklist

_Deadline packaging checklist for the ChinaTalk Situation Room submission. It covers the evidence-faithful public packet and static site only; live execution, provider access, and M7 work are outside this checklist._

---

## 📋 Evidence matrix

- [x] Include [EVIDENCE_MATRIX.md](EVIDENCE_MATRIX.md) and reconcile every row with the current evidence class, status label, artifact path, and claim boundary; keep the older readiness matrix in private history.
- [x] Make the matrix identify DATE as the primary realism-oriented open crisis World and Nuclear War as the proposed closed-form secondary comparison; do not present historical Nuclear War receipts as DATE evidence.
- [x] Keep design, offline mechanical evidence, historical engineering evidence, and any absent evidence visibly separate. A candidate file, fixture, or receipt must not be described as a completed episode or behavioral result without its own evidence.

## 📍 Episode 1

- [x] Include [EPISODE_1.md](EPISODE_1.md), the [first-episode default profile](spec/13-first-episode-default-profile.md), and the exact development profile required by the offline example, with their provisional, authored, and inference labels intact. A candidate profile may support reproducibility only when the release keeps its candidate status visible.
- [x] Owner clears or replaces the candidate source registers, Charters, and
  source-review material listed under **Owner rights gate**. The current
  curated export retains the exact candidates required by the offline
  rehearsal and design record under the owner decision recorded below.
- [x] State that Himaldesh and Olvana are the fictional crisis actors, that the U.S. Room is the focal institution, and that the synthetic geography, force packages, clocks, probes, and projections are not official DATE facts.

## 📝 Application

- [x] Include [APPLICATION_DRAFT.md](APPLICATION_DRAFT.md) and align its title, abstract, World roles, evidence claims, limitations, and local artifact links with this checklist and the evidence matrix.
- [x] Remove or qualify any claim that would imply a completed DATE episode, a same-Room Nuclear War result, official DATE fidelity, or a public release that has not occurred.

## 📐 Protocol

- [x] Include [PROTOCOL.md](PROTOCOL.md) and align its World description with the DATE-primary, open-crisis design and the proposed closed-form Nuclear War comparison.
- [x] Preserve the open-proposal, typed-state, deterministic-validation boundary for DATE and the finite legal-move, engine-owned-consequence boundary for Nuclear War.
- [x] Keep the cross-World claim boundary explicit: shared institutional definitions may be discussed where applicable, but World outcomes are not ranked as commensurate results.

## 🌐 Site

- [x] Export [`site/index.html`](site/index.html), [`site/styles.css`](site/styles.css), and [`site/og.svg`](site/og.svg) only after the page copy matches the application, protocol, register, and evidence matrix.
- [x] Replace local-checkout links, private notes, placeholder metadata, and private `noindex, nofollow` settings with the owner-approved public values before deployment.
- [x] Keep the page's evidence labels and limitations visible; do not turn an offline example or historical receipt into a DATE run or model result.

## 🧪 Offline example

- [x] Include one small offline DATE example with its exact development profile and [`DATE_TRACER_RECEIPT.json`](DATE_TRACER_RECEIPT.json); keep the profile's candidate status and non-evidence boundary visible.
- [x] Label the example as mechanical, no-model evidence. State that it does not establish a completed DATE episode, model behavior, realism, policy quality, or a comparison result.
- [x] If [`US_TWO_CYCLE_RECEIPT.json`](US_TWO_CYCLE_RECEIPT.json) is shown, retain its `development_fixture_non_evidence` boundary and identify it as a no-model development fixture.

## 📤 Public export allowlist

First materialize a dedicated curated export root, such as `<curated-export-root>`, from an exact file manifest. The export root, not the private checkout, is the publication input and the only tree scanned for public release.

The checked-in manifest records the owner-cleared publication set. Its
successful materialization and scan prove the selected bytes and release
checks, not any new behavioral result.

Export only the following classes of material after the checks below pass:

- Final, evidence-reconciled versions of [GAMES_REGISTER.md](GAMES_REGISTER.md), [EVIDENCE_MATRIX.md](EVIDENCE_MATRIX.md), [APPLICATION_DRAFT.md](APPLICATION_DRAFT.md), and [PROTOCOL.md](PROTOCOL.md), with links limited to the curated export.
- [EPISODE_1.md](EPISODE_1.md), the approved Episode 1 specification and final profile, and source cards and Charters that the owner has cleared for public distribution.
- The selected offline example and only the receipts required to explain and reproduce its stated mechanical boundary.
- Public-safe source files required to reproduce the claims actually made; the private checkout is not automatically an export allowlist.
- The three static site files listed above, plus source URLs and attribution that have passed the rights review.

Never materialize these paths or file classes in the curated export:

- All of `nuclear_war/outputs/`, both `LOGBOOK.md` files (`LOGBOOK.md` and `nuclear_war/LOGBOOK.md`), `nuclear_war/rules/`, and `nuclear_war/research/imports/`.
- Provider authorization, preflight, and promotion artifacts, including files matching `*AUTHORIZATION*`, `*PREFLIGHT*`, or `*PROMOTION*`.
- All D95 and D101 artifacts, including files matching `D95_*`, `D101_*`, `D95_REPAIR_*`, or `D101_REPAIR_*`.
- Raw journals such as `*.jsonl`, provider or live-run candidate packets, and any unredacted request, response, or transport record. Authored DATE profiles and Charter candidates may be included only when needed for the offline example and clearly labeled as candidates.
- Private operational status and handoff records, including `M6_CURRENT_STATUS.md`, owner-only authorization packets, lease records, private notes, and unselected outputs.
- Credentials, `.env` files, FIFOs, unredacted request headers, local checkout paths, and excluded historical game or source files.

Materialize curated copies when an included document links to an excluded artifact; do not copy the private `docs/contest` tree or the whole repository and call that release. A clean secret or link scan does not establish source rights.

## ⚖️ License and source rights

### Owner rights gate

The curated export includes these exact candidate files because
the retained U.S. rehearsal and linked design record depend on them. Before
external publication, the owner must either clear each file or approve a
curated replacement and its updated links and receipt identities:

- `docs/contest/US_SOURCE_REGISTER.candidate.json`
- `docs/contest/US_CHARTER.candidate.json`
- `docs/contest/US_CHARTER_REVIEW.candidate.md`
- `docs/contest/HIMALDESH_SOURCE_REGISTER.candidate.json`
- `docs/contest/HIMALDESH_CHARTER.candidate.json`
- `docs/contest/OLVANA_SOURCE_REGISTER.candidate.json`
- `docs/contest/OLVANA_CHARTER.candidate.json`
- `docs/contest/COUNTERPART_CHARTER_REVIEW.candidate.md`
- `docs/contest/research/2026-08-26-us-charter-official-source-refresh.md`
- `docs/contest/research/2026-08-26-counterpart-charter-source-refresh.md`

Owner decision, recorded 2026-09-01: all ten WOPR-authored candidate artifacts
and the site assets are cleared for publication. This clearance does not claim
ownership of the linked official sources. Source URLs and attribution remain,
while downloaded source documents and historical game rules remain excluded.

- [x] Owner selected the MIT License. The curated export includes the license used by the existing public repository.
- [x] DATE source treatment is recorded in [`SOURCE_RIGHTS_REGISTER.md`](SOURCE_RIGHTS_REGISTER.md): source URLs, attributed short quotations, and WOPR-authored paraphrases may ship; downloaded source documents do not.
- [x] Historical Nuclear War rules and imported source material remain excluded under [`SOURCE_RIGHTS_INVENTORY.md`](SOURCE_RIGHTS_INVENTORY.md).
- [x] The MIT notice and source attribution treatment are included in the release files.

## 🔐 Secret, link, accessibility, and static checks

- [ ] Run `nuclear-war contest-public-scan --root <curated-export-root>` from the `nuclear_war` project and resolve credential-like findings, excluded paths, broken local links, and private-checkout warnings; do not scan private `docs/contest` or the whole repository as release evidence.
- [ ] Run the targeted publication tests, Ruff checks for changed Python, and
  deterministic offline rehearsal on the exact release revision. Full-suite
  execution is outside the deadline check and must not become a release gate.
- [ ] Run the microsite and Markdown link checks against the materialized export and verify the one-H1 structure, skip link, main landmark, structured metadata, local artifact links, and Markdown relative links.
- [ ] Inspect the rendered exported site at mobile and desktop widths for keyboard access, visible focus, heading order, link names, table readability, contrast, descriptive image text, and no clipped or hidden content.
- [ ] Confirm that the exported tree contains no credential values, private paths, unredacted headers, unresolved placeholders, or licensed material outside the owner-approved allowlist.

## 🔗 GitHub and site URLs

- [x] Public GitHub repository: <https://github.com/glennmatlin/wopr>. It returned HTTP 200 and public visibility on 2026-09-01.
- [x] Public microsite: <https://glennmatlin.doctor/wopr/>. It returned HTTP 200 from GitHub Pages on 2026-09-01.
- [x] The application and source microsite use the same final URLs in public metadata and navigation.
- [ ] Reverify both URLs after the exact release revision and indexing metadata are deployed.
- [x] Owner authorized publication, selected MIT, and cleared the WOPR-authored assets for the release.

## 👤 Owner-only form fields

The form is the [ChinaTalk Evals Contest submission form](https://docs.google.com/forms/d/e/1FAIpQLSfSVOzLSEN-ke5tf87SE4WPSi0VJSH3aCsW0Np9pFKibCMW9A/viewform). The owner supplies these values; they are not guessed, generated, or committed as secrets.

| Field | Current state |
| --- | --- |
| Name, including all contributors | Owner supplies it directly in the form; omitted from the public repository |
| Email address | Owner supplies it directly in the form; omitted from the public repository |
| LinkedIn URL | Owner supplied it for the form; omitted from the public repository |
| Two-sentence author bio | Final copy recorded in `APPLICATION_DRAFT.md` |
| Evaluation title | Final copy recorded in `APPLICATION_DRAFT.md` |
| Abstract, approximately 150 words | Final 146-word copy recorded in `APPLICATION_DRAFT.md` |
| Project microsite URL | <https://glennmatlin.doctor/wopr/> |
| GitHub repository URL | <https://github.com/glennmatlin/wopr> |
| Interest in working for ChinaTalk | Yes, part time |

- [ ] Owner reviews the completed fields, confirms the deadline submission, and submits the form.
