# Three-Preset live composition smoke

> **HISTORICAL RECEIPT.** This smoke belongs to the earlier Nuclear War-only
> Instrument. It does not test the complete U.S. Room or DATE. See
> [CURRENT_STATUS.md](CURRENT_STATUS.md).

Status: corrected three-Preset smoke passed 2026-08-21 on executor
`fd48b11e49675c3a8a82319e13f07c7900a5ddba`. Not a Sounding result.

DeepSeek V4 Flash ran seed 51 for two turns in all three Presets. Every attempt
was Tier A with 93 validated traces, zero fallback, zero validation errors, and
zero transport retries. Receipt hashes are recorded in
[CORRECTED_RUN_RECEIPT.json](../../contest/CORRECTED_RUN_RECEIPT.json).

An earlier corrected GPT-OSS smoke produced two Tier-A cells and one terminal
equal-council failure. Those receipts remained in the private working output
tree; the predeclared smoke contract allowed one model from the approved pair,
so the complete DeepSeek smoke closed the composition gate.

## Superseded August 18 smoke

Status: passed 2026-08-18. Not a Sounding result.

One live Room (`player_0`) under full press, three first-legal opponents, seed
51, two turns, `openai/gpt-oss-20b`. Request cap 35 per Preset.

| Preset | Requests | Fallback | C2 traces | Press |
| --- | ---: | ---: | ---: | ---: |
| Presidential staff | 31 | 0 | 30 | 4 |
| Equal council | 31 | 0 | 30 | 4 |
| Chair-weighted council | 31 | 0 | 30 | 4 |

Chair-weighted council passed, so the three-Preset Instrument stays. Artifacts:
`/tmp/wopr-composition-smoke/`. Traces did not store `provider_usage`, so there
is no catalog-rate recost for this smoke.
