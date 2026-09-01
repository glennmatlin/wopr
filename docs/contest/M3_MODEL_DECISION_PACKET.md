# M3 model decision packet

Status: model pair locked after the 2026-08-16 screening. This file records the
predeclared decision rule, the resulting pair, and the remaining approval gates.
It is not a provider approval and does not authorize further paid calls.

## Locked decision

The screen produced six validated Tier-A cells and three terminal Tier-C Qwen
cells. Under the frozen operational rule, the retained pair is:

- `deepseek-ai/DeepSeek-V4-Flash-0731` (`DeepSeek`, Together, $0.14/$0.28 per
  million input/output tokens).
- `openai/gpt-oss-20b` (`GPT-OSS`, Together, $0.05/$0.20 per million
  input/output tokens).

The selected pair is captured in
[`MODEL_MANIFEST.deepseek_flash_gpt_oss_20b.candidate.json`](MODEL_MANIFEST.deepseek_flash_gpt_oss_20b.candidate.json)
and its zero-network receipt is
[`MODEL_PREFLIGHT_RECEIPT.deepseek_flash_gpt_oss_20b.json`](MODEL_PREFLIGHT_RECEIPT.deepseek_flash_gpt_oss_20b.json).
The checked-in `MODEL_MANIFEST.candidate.json` remains the historical baseline.
The live preflight and study are still owner-gated.

The replacement rule is fixed: a candidate may be replaced only before study
execution, and replacement creates a new manifest hash, preflight receipt, and
approval packet. Study behavior cannot trigger a model substitution.

## Predeclared screening decision rule

The screen is evaluated for operational validity, not for favorable strategic
behavior. Before opening the receipts, freeze the following rule:

1. A model is eligible only if all three screening seeds have validated replay,
   ordinary traces, C2 and press sidecars, and no Tier C failure, fallback, or
   provider error. Output reprompts and transport retries do not automatically
   disqualify a model, but they remain part of the operational record.
2. If more than two models are eligible, rank them lexicographically by total
   Tier B output-reprompt count, total recoverable transport retries, total
   provider attempts, and actual cost. Lower is preferred on every field; a
   provider identifier is the final deterministic tie-break. Behavioral
   measures, message content, winners, and escalation outcomes are never
   selection criteria.
3. Retain the two highest-ranked eligible families for the default study. If
   fewer than two are eligible, stop before study execution and record the
   failed screen rather than substituting an unscreened model. Retaining all
   three requires an explicit protocol amendment, a refreshed cost bound under
   the $1,000 ceiling, and a new approved manifest.

This rule is a screening control, not a claim that lower retry or cost totals
make one model strategically better. The full study remains a descriptive
comparison of the retained families under the preregistered institutional
contrasts.

## Required evidence for each selected family

- Exact provider model identifier and provider name.
- Catalog or endpoint URL, rate-check timestamp, and input/output rates.
- Base URL, credential-environment name, timeout, streaming setting, temperature,
  output limit, reasoning control, and retry policy.
- Existing bounded calibration evidence, if available, linked to its local
  artifact rather than summarized as a behavioral claim.
- Confirmation that the three preflight seeds remain disjoint from study seeds
  51-55.

## Owner budget constraint

The total API ceiling is **$1,000**, including live preflight, composition
smoke, pilot, retries, and any full study. The checked-in `$5,000` value belongs
to a historical candidate packet and is not an authorization. A new candidate
manifest must fit the hard ceiling while retaining a reserve for validation.

## Concrete options under the cap

The screening packet uses the Together serverless endpoint for all three
families. The catalog was checked on 2026-08-16 at
[Together's serverless model catalog](https://docs.together.ai/docs/serverless/models),
which lists GPT-OSS 20B, DeepSeek V4 Flash 0731, and Qwen3.5 9B with the rates
below. Rates and endpoint behavior must be rechecked before live approval. The
[official DeepSeek API](https://api-docs.deepseek.com/quick_start/pricing)
is a separate fallback endpoint, not the current screening path.
The full-study bound is the existing 40-game design; the demo bound is four
conditions with one seed per condition for each family, or eight games total.

| Option | Exact pair and rates (input/output USD per million) | Full-study bound | One-seed demo bound | Evidence and tradeoff |
| --- | --- | ---: | ---: | --- |
| A, locked pair | `deepseek-ai/DeepSeek-V4-Flash-0731` (0.14/0.28) + `openai/gpt-oss-20b` (0.05/0.20) | $477.521510 | $95.504302 | Both models completed all three screening seeds as Tier A. DeepSeek Flash has no strategic claim attached to this operational screen; live preflight remains required. |
| B, rejected screen fallback | `openai/gpt-oss-20b` (0.05/0.20) + `Qwen/Qwen3.5-9B` (0.17/0.25) | Not admissible | Not admissible | GPT-OSS passed all three cells, but Qwen3.5 failed all three screening cells as terminal Tier C, so this pair is not eligible under the frozen rule. |
| C, protocol amendment | Retain all three screened families after review | Recompute | Recompute | Allowed only if the protocol is explicitly amended; it is not an unscreened fourth model option. |

The screen makes DeepSeek V4 Flash a retained operational candidate alongside
GPT-OSS 20B. It does not establish strategic superiority or substitute for the
three-seed live preflight, which is the next evidence-producing step under the
$1,000 total cap.

Option A is now locked. Qwen3.5-9B is not substituted back into the study based
on the failed screen; any replacement would require a new screening or an
explicit protocol amendment.

The local calibration evidence is bounded and historical: see the
[press-light scorecard](../../research/llm_model_calibration/stage3_press_light_scorecard.md)
and [calibration findings](../../research/llm_model_calibration/findings.md).
It proves neither current catalog availability nor behavior on the full study.
Hosted model families outside the confirmed endpoint path require a separate
backend and manifest-validation change; they are not drop-in replacements in
this decision packet.

Use this redacted owner record outside the repository:

```json
{
  "schema_version": 1,
  "candidate_manifest_revision": "new-candidate-required",
  "model_ids": ["<exact provider id 1>", "<exact provider id 2>"],
  "provider": "<provider>",
  "endpoint": "<https endpoint>",
  "catalog_urls": ["<url 1>", "<url 2>"],
  "rates_checked_at": "<YYYY-MM-DD>",
  "input_usd_per_million": [0.0, 0.0],
  "output_usd_per_million": [0.0, 0.0],
  "max_spend_usd": 0.0,
  "credential_env": "<environment variable name>",
  "executor_revision": "<40-character clean SHA>",
  "approved": false
}
```

`approved` stays `false` until the owner has reviewed the identifiers, rates,
endpoint, credential path, executor revision, and spend cap. The record must
contain no credential value.

## Frozen planning envelope

The current design has 40 games, 2,208 base calls per game, and a retry
multiplier of six, giving 529,920 maximum provider attempts. Each selected
family accounts for 264,960 attempts, an input bound of 2,170,552,320 tokens,
and an output bound of 135,659,520 tokens. The recalculated combined cost is:

```text
sum over families(
  2170.55232 * input_usd_per_million
  + 135.65952 * output_usd_per_million
)
```

The hard owner cap must cover the refreshed full-study bound plus the reserved
preflight and composition-smoke allowance; it remains a spend decision, not a
prediction of actual usage. If the cap, selected pair, or request settings
change, regenerate the candidate manifest and receipt rather than editing a
receipt by hand.

## Regeneration and execution sequence

1. Keep the selected IDs and rates in the new candidate manifest; do not
   overwrite the checked-in historical candidate.
2. The zero-network planning receipt is generated and bound to the new
   candidate hash.
3. Create the first owner approval outside the repository, then run the bounded
   live preflight with `--allow-network` and the exact clean executor SHA.
4. Review the completed receipt, create the separate receipt-hash promotion
   approval, and promote only a passing receipt into the frozen study manifest.
5. Run the provider-backed C2/full-press composition smoke before any study
   seed. A failed gate selects the two checked-in paired fallback manifests.

The authoritative procedures are [M3_MODEL_PREFLIGHT.md](M3_MODEL_PREFLIGHT.md),
[M3_PROMOTION.md](M3_PROMOTION.md), and
[EXECUTION_PLAN.md](EXECUTION_PLAN.md). This packet makes the decision fields
explicit; it does not waive any of those gates.
