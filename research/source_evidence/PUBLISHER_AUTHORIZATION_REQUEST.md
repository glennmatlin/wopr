# Publisher Authorization Request

This packet supports publisher-authorized source acquisition. It is not source evidence, and it
does not create live manifests, draft records, registry changes, or permission by itself.

## Current Public Source Leads

- Mr. B Games product page for Nuclear Destruction:
  `https://www.mrbgames.com/products/pre-order-nuclear-destruction-card-game`
- Mr. B Games public Nuclear Destruction downloads:
  - Updated rules PDF:
    `https://cdn.shopify.com/s/files/1/0040/1240/8885/files/NucDesRulesUpdated040226.pdf?v=1775165495`
  - Game log PDF:
    `https://cdn.shopify.com/s/files/1/0040/1240/8885/files/NuclearDestructionLog.pdf?v=1775165495`
  - Anti-missile chart PDF:
    `https://cdn.shopify.com/s/files/1/0040/1240/8885/files/Nuclear_DestructionAntiMissileChart.pdf?v=1775165495`
- Mr. B Games contact form:
  `https://www.mrbgames.com/pages/contact-us`

Use these as contact and source leads only. `PUBLIC_SOURCE_LEADS.md` records the public download
boundary. Verify the current contact path before sending a request.

## Request Scope

Ask for permission or publisher-authorized source material for:

- derived card-effect summaries for active Nuclear War cards;
- deck composition counts for base and expansion cards;
- edition boundary notes such as spinner or dice randomizer, hand size, population deck model, and
  whether expansion cards are included;
- expansion deck composition counts for Nuclear Escalation, Nuclear Proliferation, and related
  Nuclear War family materials;
- permission to record public-safe derived metadata in this repository.

Do not ask for permission to publish exact card text, scans, art, or private correspondence in this
repository unless the publisher explicitly grants that permission and the project owner separately
approves a public-data policy change.

## Request Template

```text
Hello,

I am building a deterministic rules engine for the Nuclear War card-game family. The current
repository keeps source evidence public-safe: it records derived metadata such as card identity,
card type, deck counts, edition boundaries, and summarized effect behavior. It does not publish
card scans, art, or exact card text.

Would you be willing to authorize the use of publisher-provided materials, or provide a public-safe
card/deck reference, for verifying:

- active Nuclear War card identities, counts, and derived effect summaries;
- expansion deck composition counts;
- edition boundaries such as spinner/dice randomizer, hand size, and population deck model?

If authorization is granted, I will keep any private files or correspondence outside the public
repository and will record only public-safe derived evidence records unless you explicitly approve a
broader public use.

Thank you.
```

## Response Handling

- Store private replies, attachments, screenshots, and exact text outside the public repository.
- Do not put exact card text, official card text, art, scans, or private email text in git.
- If authorization is granted, draft records can use
  `evidence_kind: "publisher_authorized_source"`.
- Use source references that identify the authorized source without exposing private files or
  private correspondence.
- Run `nuclear-war validate-source-evidence` on draft paths before promotion.
- Promote records into `card_effect_evidence.jsonl` or `expansion_deck_composition.jsonl` only
  after second-pass verification.
- Make registry card-effect or expansion count changes in a separate rules-change branch after live
  manifests validate.

## Non-Evidence Boundary

This file is only an acquisition aid. It does not satisfy `card_effect_transcription`,
`expansion_deck_composition`, `expansion_rules_verification`, or edition blockers.
