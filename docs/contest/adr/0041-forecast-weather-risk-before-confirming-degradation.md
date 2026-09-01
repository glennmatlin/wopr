# Forecast weather risk before confirming degradation

Status: accepted decision D56, refined by D57-D60; partially resolves OPEN-WORLD-002

The first Setup gives the U.S. Room a credible but uncertain Cycle 1 forecast that high-altitude access may deteriorate, then confirms the actual degradation at the matched Cycle 2 barrier. The forecast supports contingency planning without making the later observation redundant; the confirmation tests adaptation without appearing as an unrelated surprise.

## Considered options

- Provide an uncertain forecast before confirming deterioration.
- Provide no warning before a surprise confirmation.
- Provide a precise STARTEX forecast whose realization is expected.

No warning produces a clean shock but does not test whether weak evidence survives the institution before becoming fact. A precise forecast tests planned execution but weakens the second cycle's new-information challenge. The selected sequence observes both anticipation and revision while keeping the policy choice open.

## Consequences

The forecast is a matched, Setup-authored, ledger-only observation of a possible future constraint. It MUST state uncertainty and a bounded risk interval, MUST NOT change access state, and MUST leave materially different weather outcomes epistemically live for the Room. The later event is the matched exogenous fact: it applies the frozen weather or access State Patch and produces a linked confirmation observation that materially narrows the uncertainty.

Both stages and their identities, content, timing, entitlement, delivery, and causal link are frozen across matched runs. Confirmation MUST NOT depend on whether either Room prepared for it. Room actions may change downstream exposure or response options but cannot prevent or rewrite the authored weather event.

ADR 0042 fixes the U.S. institutional route: specialist cells receive the raw Cycle 1 forecast, senior forums receive attributable products and evidence links, and the linked Cycle 2 confirmation becomes common to every active U.S. seat. ADR 0043 and D59 fix paired dependency classes and mixed ownership. Module 13 supplies D60's reversible confidence language, warning interval, severity, report, and patch-value defaults. Surprise-only and precise-forecast paths remain separately authorable Setup identities. No existing harness code implements this two-stage DATE information path, so D56-D60 remain design rather than execution evidence.
