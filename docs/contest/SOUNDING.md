# 18-game Room Instrument Sounding

Status: corrected execution completed 2026-08-21. 12 of 18 cells Tier A and 6
Tier C. Descriptive Sounding only; not a population estimate.

Output directory: retained in the private engineering record and excluded from
the curated release.
Executor: `fd48b11e49675c3a8a82319e13f07c7900a5ddba`.
Analysis copy: [SOUNDING_ANALYSIS.corrected.json](SOUNDING_ANALYSIS.corrected.json).
Hashes and compact counts: [CORRECTED_RUN_RECEIPT.json](CORRECTED_RUN_RECEIPT.json).

| Model | Staff 51/52/53 | Equal 51/52/53 | Chair-weighted 51/52/53 |
| --- | --- | --- | --- |
| DeepSeek V4 Flash | A A A | A A C | C C A |
| GPT-OSS 20B | C C A | A C A | A A A |

All six Tier C attempts are terminal with zero admitted traces. Four exhausted
the frozen channel cap: DeepSeek chair-weighted seed 51; GPT-OSS staff seeds 51
and 52; and GPT-OSS equal council seed 52. DeepSeek equal council seed 53 and
chair-weighted seed 52 ended with a redacted provider-or-runner error. They are
retained and were not retried.

Primary paired analysis uses 12 eligible rows and produces five matched pairs.
DeepSeek equal-council-minus-staff is paired on seeds 51 and 52. DeepSeek
chair-weighted-minus-staff is paired on seed 53. GPT-OSS has both contrasts on
seed 53 only. This missingness precludes a complete three-seed Preset
comparison, so outcome deltas remain seed-level descriptions.

Receipts store `actual_cost_usd: 0`. Cumulative reserved planning charge on the
completed cells is `$4.2771456`. That is not an invoice. Completed attempts
record four transport retries.

The Overlay Demo ran after Sounding and failed terminal before producing an
admissible trace. There is no Demo trajectory to publish.

## Corrected equal-council reading

Four equal-council attempts are Tier A. Across 324 deliberations they record
123 disagreements, 35 decisions against the executive, and 13 genuine
threshold failures. DeepSeek seeds 51 and 52 record 3 and 5 executive
overrides; GPT-OSS seeds 51 and 53 record 15 and 12. The correction therefore
changes the live command process materially, but the small, incomplete Sounding
does not support a population claim about downstream escalation or loss.

## Superseded August 18 execution

The frozen manifest encodes two-thirds as `0.6666666667`. The August 18
executor compared the computed vote share strictly against that decimal, so an
exact two-of-three share failed the threshold and defaulted to the executive.

Across the six Tier-A equal-council cells, all 205 non-unanimous deliberations
were recorded as threshold failures. The frozen votes include 61 deliberations
where both advisers selected the same action against the executive. Every
equal-council trajectory reached one of those coalitions by turn 4, so none is
a valid trajectory for the intended two-of-three Release rule. The 61 frozen
coalitions show that the defect is material; they do not predict a corrected
rerun because the World diverges after the first changed action.

Replay, trace, failure, and operational receipts remain valid evidence of what
the August 18 executor did. Its analysis remains frozen in
[SOUNDING_ANALYSIS.json](SOUNDING_ANALYSIS.json) and is not used for corrected
behavioral claims.
