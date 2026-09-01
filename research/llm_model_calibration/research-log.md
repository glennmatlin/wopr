# LLM Model Calibration Research Log

## 2026-07-05 03:06

Context: I started the low-cost serverless model survey for WOPR LLM and Concordia calibration.

Action: I checked the official serverless catalog, recommended-model guide, rate-limit guide, and OpenAI-compatible endpoint guide. I also queried the live `/v1/models` endpoint with the existing local key and printed only sanitized metadata.

Result: The official catalog lists chat, image, vision, video, audio, embedding, rerank, and moderation categories. The live endpoint returned 271 broader model records and confirmed candidate model IDs, but it is not the source of record for the serverless subset. The current calibration shortlist is `openai/gpt-oss-20b`, `Qwen/Qwen3.5-9B`, `LiquidAI/LFM2-24B-A2B`, and `google/gemma-3n-E4B-it`.

## 2026-07-05 03:20

Context: I needed a bounded first calibration pass using existing project validation instead of ad hoc scripts.

Action: Ran the existing direct HTTP smoke and native Concordia one-turn smoke for `openai/gpt-oss-20b` and `Qwen/Qwen3.5-9B`. The direct smoke exposed that 32 and 128 completion-token caps can be too low because these models may spend completion budget on reasoning text before final content. I updated the direct live smoke cap to 256. Then I ran direct-only smokes for `LiquidAI/LFM2-24B-A2B` and `google/gemma-3n-E4B-it`.

Result: `openai/gpt-oss-20b` and `Qwen/Qwen3.5-9B` passed direct HTTP plus one-turn native Concordia smokes. `LiquidAI/LFM2-24B-A2B` and `google/gemma-3n-E4B-it` passed direct HTTP smokes only.

## 2026-07-05 14:58

Context: I needed to record the Task 6 scorecard state after the catalog stage artifact was written, while avoiding live provider calls unless credentials and an explicit cost cap were present.

Action: Validated `/tmp/wopr_model_scorecard_catalog/catalog_scorecard.json`, `/tmp/wopr_model_scorecard_catalog/stage2_calibration_results.json`, and `/tmp/wopr_model_scorecard_catalog/scorecard_summary.md` with read-only checks. The catalog scorecard contains 23 chat-model scores, all labeled `predicted`. The Stage 2 result artifact has schema version 1 and zero results. I also checked presence only for `TOGETHER_API_KEY`, `WOPR_MODEL_SCORECARD_MAX_COST_USD`, and `WOPR_MAX_MODELS_COST_USD`.

Result: Bounded live Stage 2 was not run in this session. The provider key and both explicit cost-cap variables were absent, so there are no measured Stage 2 pass/fail counts yet and no provider failures recorded by a live run. The current artifacts support catalog-only ranking for all 23 chat models. The coverage requirement that each catalog chat model has a measured result or recorded provider failure remains gated until a credentialed, cost-capped Stage 2 run is executed.

## 2026-07-05 16:33

Context: I needed to run actual Together Stage 2 calibration after the scorecard CLI gained the gated provider path.

Action: Ran `nuclear-war llm-model-scorecard --stage stage2 --provider together --catalog research/llm_model_calibration/data/serverless_catalog_2026-07-05.json --out /tmp/wopr_model_scorecard_stage2 --max-models-cost-usd 5 --max-tokens 256` with `TOGETHER_API_KEY` sourced from `.env.secret` and network escalation. The first sandboxed run failed DNS resolution for all models and was not treated as model evidence. The escalated run wrote measured artifacts.

Result: The escalated Stage 2 run tested 23 chat models. Three passed: `LiquidAI/LFM2-24B-A2B`, `deepcogito/cogito-v2-1-671b`, and `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`. Twenty failed: 15 `http_error` and 5 `parse_failure`. Returned usage totaled 72,083 prompt tokens, 4,086 completion tokens, and 76,169 total tokens. Applying catalog rates to returned usage gives an estimated cost of $0.035928.

## 2026-07-05 16:55

Context: I needed to start Stage 3 candidate checks for the Stage 2 survivors.

Action: Ran short native Concordia no-press checks for `LiquidAI/LFM2-24B-A2B`, `deepcogito/cogito-v2-1-671b`, and `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`. Then ran short press-light checks for Cogito and Qwen because they were the no-press completions.

Result: Liquid failed strict no-press Concordia parsing after producing role-play text plus JSON. Cogito completed no-press with 47 traces, 0 invalid actions, and 0 retries, then failed press-light strict parsing after role-play analysis plus JSON. Qwen completed no-press with 46 traces, 0 invalid actions, and 0 retries, and completed press-light with 22 decision traces, 3 public press messages, 0 invalid actions, and 0 retries. Qwen is the current working Stage 3 candidate.

## 2026-07-05 18:03

Context: I needed to debug the 20 failed Stage 2 results instead of treating them as final model evidence.

Action: Ran exact-seed diagnostics with captured response shapes and no credentials in output. Added tests and fixes for Together streaming, reasoning-disable controls, provider error-message reporting, fenced or partial JSON parsing, and verbatim legal action-id recovery. Ran corrected full-catalog Stage 2 with `--stream --disable-reasoning --max-tokens 4096` into `/tmp/wopr_model_scorecard_stage2_fixed_4096`.

Result: The corrected run produced 20 passes and 3 failures. Remaining failures are now classified: MiniMax M2.7 still emits reasoning only at 4096 tokens, GPT-OSS 20B needs `reasoning_effort=low`, and Llama 3 8B Lite needs a smaller output cap because the 4096 cap exceeds its 8193-token context with the current prompt. The corrected run recorded 248,061 total tokens and an estimated catalog-priced cost of $0.20721057.

## 2026-07-05 21:34

Context: I needed bounded Stage 3 evidence on the selected candidate roster before drafting the calibration report.

Action: Ran no-press native Concordia checks under `/tmp/wopr_stage3_bounded` with six candidate lanes and three-seed continuation only for seed-91 completers. Then ran one press-light seed for the three strongest no-press lanes: MiniMax M3, Qwen 3.5 9B, and GPT-OSS 20B low-reasoning.

Result: No-press completed 3/3 for MiniMax M3, Qwen 3.5 9B, and GPT-OSS 20B low-reasoning. Qwen 235B completed 2/3 and failed seed 93 by selecting an illegal `modify_deterrent` action during a `place` decision. Gemma 4 31B failed on fenced JSON containing a legal action id. GPT-OSS 120B failed by selecting `modify_deterrent` during a `place` decision. Press-light passed for all three attempted lanes. MiniMax M3 was legally clean but declined every press message; Qwen 3.5 9B produced richer public messages but needed three retries; GPT-OSS 20B produced concise role-aligned messages with no invalid actions or retries. The bounded Stage 3 catalog-priced estimate is about $2.66067695.

## 2026-07-05 22:45

Context: I needed to debug and recover the failed Stage 3 candidates before deciding whether they were unsuitable for press-light tests.

Action: Added parser and provider-error fixes for Concordia action responses, native Concordia stale completion handling, HTTP retry behavior, and fenced JSON press responses. Reran bounded no-press checks for Gemma 4 31B seed 91, GPT-OSS 120B seed 91, and Qwen 235B seed 93 under `/tmp/wopr_stage3_repair/no_press`. Then ran press-light seed 101 checks for Gemma 4 31B, GPT-OSS 120B, GPT-OSS 120B with `reasoning_effort=low`, and Qwen 235B under `/tmp/wopr_stage3_repair/press_light`.

Result: Gemma 4 31B no-press passed with 52 traces, 0 invalid actions, and 0 retries. GPT-OSS 120B no-press passed with 63 traces, 1 invalid action, and 1 retry. Qwen 235B seed 93 no-press passed with 78 traces, 1 invalid action, and 1 retry. Gemma 4 31B press-light passed with 35 action traces, 0 invalid actions, 0 retries, 8 press messages, 6 spoken, and 2 declined. GPT-OSS 120B press-light failed without `reasoning_effort=low` because the provider returned empty message content after bounded retries, but passed with `reasoning_effort=low`: 35 traces, 0 invalid actions, 0 retries, 8 press messages, 7 spoken, and 1 declined. Qwen 235B press-light passed with 35 traces, 0 invalid actions, 0 retries, 8 press messages, 8 spoken, and 0 declined. The earlier GPT-OSS 120B and Qwen 235B failure snapshots were reclassified as stale-completion artifacts attached to later provider errors, not direct evidence of current-decision illegal `modify_deterrent` choices.

## 2026-07-06 01:46

Context: I needed a catalog-wide Stage 3 press-light scorecard that kept Cogito and Liquid in the evaluated set and did not filter out expensive models before measurement.

Action: Ran 23 serverless chat model lanes through a three-seed press-light robustness batch under `/tmp/wopr_stage3_presslight_robustness`. Each run used four `concordia_http` seats, seeds 101 to 103, `max_turns=3`, `temperature=0.7`, `max_tokens=512`, `stream=true`, and `reasoning_enabled=false`. GPT-OSS lanes also used `reasoning_effort=low`. I added a temporary runner timeout after repeated provider hangs so timeout failures were recorded and the batch could continue.

Result: The batch attempted 69 runs. It completed 51 and failed 18. Completed runs recorded 1,729 decision traces, 363 press opportunities, 306 spoken messages, 57 declines, 0 invalid actions, and 0 retries. Recorded provider usage totaled 5,766,124 tokens, with a catalog-priced estimate of `$4.29009455`. The aggregate is `/tmp/wopr_stage3_presslight_robustness/press_light_aggregate.json`. The checked-in scorecard is `research/llm_model_calibration/stage3_press_light_scorecard.md`.

## 2026-07-06 13:02

Context: I needed to collate the LLM study branch so it can be reviewed as one package before opening a PR and moving on to LLM game experiments.

Action: Added `research/llm_model_calibration/README.md` as the study entry point. Updated `research-state.yaml`, `findings.md`, `AGENT_HANDOFF.md`, and the scorecard-state integration test to point to the finalized study package, including the scorecard, local playground, and raw Stage 3 aggregate.

Result: The branch now has a reviewer-facing index, final operational model grades, exact artifact paths, and a clear next-step boundary: the next branch can begin LLM game experiments using GPT-OSS 20B low-reasoning as the default lane, with Qwen, Kimi, GLM, Cogito, DeepSeek, Gemma 4, and Llama comparison lanes.
