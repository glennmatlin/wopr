# Low-Cost Serverless Model Findings

## Current Understanding

The official serverless catalog is the source of record for this survey. It lists per-token serverless inference with no provisioning or minimum cost, plus dynamic per-model rate limits. The live `/v1/models` endpoint returned a broader provider inventory, so I used it only to confirm candidate IDs and metadata.

For WOPR and Concordia, the main requirement is not only low price. The model must handle long prompts and reliably return parseable decisions. Native Concordia prompts already exceeded an 8k-context model during local smoke testing, so 8k models should not be used for native Concordia calibration.

## Shortlist

`openai/gpt-oss-20b` remains the first provisional low-cost calibration lane to measure. It has 128k context, documented function calling, documented structured outputs, and the lowest listed input/output price among long-context chat models with those capability flags: $0.05 input and $0.20 output per 1M tokens.

`Qwen/Qwen3.5-9B` remains the second provisional calibration lane to measure. It is not cheaper than `openai/gpt-oss-20b`, but it has 262k context, documented function calling, documented structured outputs, and is also listed as a vision model. It is appropriate when prompt length or model-family diversity matters.

`LiquidAI/LFM2-24B-A2B` and `google/gemma-3n-E4B-it` remain exploratory low-cost lanes to measure. Both have 32k context and lower output pricing than most alternatives. The official catalog does not list function calling or structured outputs for them, so they should be tested only with short no-press JSON-decision prompts before any longer run.

`meta-llama/Meta-Llama-3-8B-Instruct-Lite` should stay out of native Concordia calibration for now. Its 8k context was the observed cause of a native smoke failure when inherited from the local endpoint environment.

## First Calibration Smokes

`openai/gpt-oss-20b` passed the direct HTTP JSON smoke and one-turn native Concordia smoke.

`Qwen/Qwen3.5-9B` passed the direct HTTP JSON smoke and one-turn native Concordia smoke.

`LiquidAI/LFM2-24B-A2B` passed the direct HTTP JSON smoke. I have not run it through native Concordia yet.

`google/gemma-3n-E4B-it` passed the direct HTTP JSON smoke. I have not run it through native Concordia yet.

The direct JSON smoke needs a 256-token completion cap for the primary candidates. Lower caps caused empty final content with `finish_reason: length` because the response budget was spent before the final JSON answer.

These smoke results are historical checks. They are not full Stage 2 scorecard results because they do not cover all 23 chat models through the current scorecard runner with recorded per-model outcomes.

## Scorecard Status

The Task 6 catalog scorecard artifact covers all 23 chat models from `research/llm_model_calibration/data/serverless_catalog_2026-07-05.json`. Every score in `/tmp/wopr_model_scorecard_catalog/catalog_scorecard.json` is labeled `predicted`.

The scorecard CLI now has a gated `--provider together` Stage 2 path. It constructs the existing OpenAI-compatible HTTP client with the Together provider defaults and the catalog model ID. Runtime calls still require `TOGETHER_API_KEY`. The `--max-models-cost-usd` flag is required and must be positive before any live Stage 2 artifacts are written. This gate does not yet estimate or report actual spend.

The first live Together Stage 2 artifact is `/tmp/wopr_model_scorecard_stage2/stage2_calibration_results.json`. It has schema version 1 and measured results for all 23 chat models. This run is now historical because follow-up debugging found request-shape and parser false failures.

Historical measured Stage 2 counts from the first live run:

- Pass count: 3.
- Fail count: 20.
- Direct smoke pass count: 19.
- WOPR one-turn pass count: 3.
- Recorded provider-failure count: 15 `http_error` results and 5 `parse_failure` results.

The initial Stage 2 survivors were `LiquidAI/LFM2-24B-A2B`, `deepcogito/cogito-v2-1-671b`, and `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`. These are no longer the only measured operational candidates.

The run recorded 72,083 prompt tokens, 4,086 completion tokens, and 76,169 total tokens across returned provider usage. Applying the catalog prices to recorded usage gives an estimated run cost of about $0.035928. This is an estimate from returned usage and catalog rates, not a billing statement.

The highest predicted catalog scores without current risk flags are `Qwen/Qwen3.5-9B`, `google/gemma-4-31B-it`, `MiniMaxAI/MiniMax-M3`, `openai/gpt-oss-20b`, `MiniMaxAI/MiniMax-M2.7`, and `openai/gpt-oss-120b`. This is catalog-only ranking, not operational evidence.

I debugged the 20 failures instead of treating them as model evidence. The root causes were: reasoning models spending the output budget in `message.reasoning`, Qwen Plus and Max models requiring streaming, fenced or prefaced JSON, invalid JSON around nested action IDs, and provider error details hidden by the client error message.

The corrected full-catalog run is `/tmp/wopr_model_scorecard_stage2_fixed_4096/stage2_calibration_results.json`. It used `--stream --disable-reasoning --max-tokens 4096` after adding streaming support, reasoning-disable controls, provider error messages, and parser recovery for legal action IDs.

Corrected measured Stage 2 counts:

- Pass count: 20.
- Fail count: 3.
- Direct smoke pass count: 23.
- WOPR one-turn pass count: 20.
- Recorded provider-failure count: 3 `http_error` results and 0 `parse_failure` results.
- Returned usage: 222,122 prompt tokens, 25,939 completion tokens, and 248,061 total tokens.
- Estimated catalog-priced cost: about $0.20721057. This is not a billing statement.

Remaining failure notes:

- `MiniMaxAI/MiniMax-M2.7` still emits empty `message.content` after spending 4096 tokens in reasoning. Do not promote it until I have a prompt-shortening or model-specific reasoning-control task.
- `openai/gpt-oss-20b` failed in the global 4096 corrected run but passed an isolated diagnostic with `reasoning_effort=low`; use that control for future GPT-OSS checks.
- `meta-llama/Meta-Llama-3-8B-Instruct-Lite` failed only because prompt tokens plus 4096 output tokens exceeded its 8193-token limit. It passed the 1024-token corrected run. Keep 8k-context models on smaller caps and out of native Concordia prompts.

Stage 3 role-play and Concordia candidates should now be selected from the corrected Stage 2 evidence, not the stale 3-survivor list.

## Stage 3 Short Runs

I ran short native Concordia no-press checks for the three Stage 2 survivors.

`LiquidAI/LFM2-24B-A2B` failed strict Concordia action parsing. The failure snapshot is `/tmp/wopr_stage3_concordia_liquid/concordia/failure_snapshot.json`. The visible responses contained role-play text and JSON, but not a strict top-level JSON object accepted by the current parser.

`deepcogito/cogito-v2-1-671b` completed `/tmp/wopr_stage3_concordia_cogito` with 47 traces, 0 invalid actions, 0 retries, and termination at the 4-turn cap. It eliminated `player_2` before the cap. It then failed the short press-light check at `/tmp/wopr_stage3_press_cogito` because the response again included role-play analysis before the JSON action object.

`Qwen/Qwen3-235B-A22B-Instruct-2507-tput` completed `/tmp/wopr_stage3_concordia_qwen235` with 46 traces, 0 invalid actions, 0 retries, and termination at the 4-turn cap. It eliminated `player_1` and `player_3` before the cap. It also completed the short press-light check at `/tmp/wopr_stage3_press_qwen235` with 22 decision traces, 3 public press messages, 0 invalid actions, and 0 retries.

The Qwen press-light messages were parseable and role-specific in the current run. Examples: the cautious commander said, "We maintain readiness without provocation. Stability favors the patient." The risk-accepting commander said, "The weak prepare. The strong act. I am not here to wait—I am here to decide." The deterrence-focused commander said, "Strength lies not in haste, but in the certainty of response."

Observed catalog-priced cost estimate across the Stage 2 run plus these Stage 3 short checks is about $1.079220, based on returned provider usage and catalog rates. This is not a billing statement.

## Stage 3 Bounded Candidate Runs

I then selected candidates from the corrected Stage 2 run and ran bounded Stage 3 checks under `/tmp/wopr_stage3_bounded`.

No-press native Concordia setup:

- Six candidate lanes were attempted: `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`, `Qwen/Qwen3.5-9B`, `google/gemma-4-31B-it`, `openai/gpt-oss-120b`, `MiniMaxAI/MiniMax-M3`, and `openai/gpt-oss-20b` with `reasoning_effort=low`.
- Seed 91 was run for all six lanes.
- Seeds 92 and 93 were run only for the seed-91 completers.
- Configs used four native HTTP Concordia seats, `max_turns=8`, `temperature=0.0`, `max_tokens=1024`, `stream=true`, and `reasoning_enabled=false`.
- Aggregate artifact: `/tmp/wopr_stage3_bounded/no_press_aggregate.json`.

No-press results:

| Model | Completed | Traces | Invalid | Retries | Turns | Est. cost |
|---|---:|---:|---:|---:|---:|---:|
| `MiniMaxAI/MiniMax-M3` | 3/3 | 193 | 0 | 0 | 23 | $1.2376 |
| `Qwen/Qwen3.5-9B` | 3/3 | 196 | 2 | 2 | 18 | $0.6259 |
| `openai/gpt-oss-20b` with `reasoning_effort=low` | 3/3 | 225 | 2 | 2 | 24 | $0.2133 |
| `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` | 2/3 | 133 | 1 | 1 | 16 | $0.5100 |
| `openai/gpt-oss-120b` | 0/1 | 0 | 0 | 0 | 0 | $0.0016 |
| `google/gemma-4-31B-it` | 0/1 | 0 | 0 | 0 | 0 | $0.0026 |

The no-press failures were specific:

- `google/gemma-4-31B-it` returned fenced JSON containing a legal action id, but the current strict Concordia parser rejected it.
- `openai/gpt-oss-120b` appeared to select `modify_deterrent` during a `place` decision, but follow-up debugging showed the visible completion was stale data attached to a later missing-content provider error.
- `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` completed two seeds, then seed 93 appeared to fail by selecting `modify_deterrent` during a `place` decision. Follow-up debugging showed the visible completion was stale data attached to a later 429 provider error.

Press-light setup:

- I ran one press-light seed for the three strongest no-press lanes: MiniMax M3, Qwen 3.5 9B, and GPT-OSS 20B low-reasoning.
- Configs used four `concordia_http` seats, seed 101, `max_turns=3`, `temperature=0.7`, `max_tokens=512`, `stream=true`, and `reasoning_enabled=false`.
- Aggregate artifact: `/tmp/wopr_stage3_bounded/press_light_aggregate.json`.

Press-light results:

| Model | Status | Traces | Invalid | Retries | Press messages | Spoken / declined | Est. cost |
|---|---:|---:|---:|---:|---:|---:|---:|
| `MiniMaxAI/MiniMax-M3` | pass | 35 | 0 | 0 | 8 | 0 / 8 | $0.0382 |
| `Qwen/Qwen3.5-9B` | pass | 35 | 3 | 3 | 8 | 7 / 1 | $0.0255 |
| `openai/gpt-oss-20b` with `reasoning_effort=low` | pass | 36 | 0 | 0 | 8 | 8 / 0 | $0.0059 |

Observed press-light behavior:

- MiniMax M3 was legally clean but declined every press opportunity. It is a strong no-press legality baseline, not the best role-play lane from this press-light seed.
- Qwen 3.5 9B produced richer public statements and differentiated roles, but required three retry-recovered invalid actions.
- GPT-OSS 20B produced concise role-aligned public statements, completed with no invalid actions or retries, and had the lowest observed press-light cost in this pass.

Observed catalog-priced cost estimate for the bounded Stage 3 pass is about $2.66067695: about $2.59107752 for no-press and about $0.06959943 for press-light. This is not a billing statement.

Current report interpretation:

- Use `openai/gpt-oss-20b` with `reasoning_effort=low` as the current low-cost press-light lead.
- Use `MiniMaxAI/MiniMax-M3` as the clean no-press legality baseline.
- Use `Qwen/Qwen3.5-9B` as the richer role-play comparison, with retry risk noted.
- Treat Gemma 4 31B, GPT-OSS 120B with `reasoning_effort=low`, and Qwen 235B as repaired comparison lanes, not the primary low-cost recommendation.

## Stage 3 Repair Checks

I then repaired the strict parsing and provider-error handling issues that blocked additional candidates. The repair artifacts are under `/tmp/wopr_stage3_repair`.

Implemented fixes:

- Concordia action parsing now reuses the WOPR-native fenced/prose/legal-action recovery path.
- Native Concordia HTTP clears stale `last_completion` before each decision, so provider errors cannot surface an old completion.
- The HTTP client retries empty successful completion payloads and waits briefly before retrying 429 responses.
- Press parsing now recovers fenced JSON press messages and fenced JSON declines.

No-press repair rechecks:

| Model | Seed | Status | Traces | Invalid | Retries | Result |
|---|---:|---:|---:|---:|---:|---|
| `google/gemma-4-31B-it` | 91 | pass | 52 | 0 | 0 | Recovered the fenced-JSON action failure. |
| `openai/gpt-oss-120b` | 91 | pass | 63 | 1 | 1 | Completed after one truncated-JSON retry. |
| `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` | 93 | pass | 78 | 1 | 1 | Completed after one retry-recovered illegal enqueue. |

Press-light repair rechecks:

| Model | Seed | Status | Traces | Invalid | Retries | Press | Spoken / declined |
|---|---:|---:|---:|---:|---:|---:|---:|
| `google/gemma-4-31B-it` | 101 | pass | 35 | 0 | 0 | 8 | 6 / 2 |
| `openai/gpt-oss-120b` | 101 | fail | - | - | - | - | Empty message content when `reasoning_effort` was unset. |
| `openai/gpt-oss-120b` with `reasoning_effort=low` | 101 | pass | 35 | 0 | 0 | 8 | 7 / 1 |
| `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` | 101 | pass | 35 | 0 | 0 | 8 | 8 / 0 |

The repaired results expand the comparison set, but they do not change the low-cost lead. GPT-OSS 20B with `reasoning_effort=low` remains the first report recommendation because it is cheaper and already passed the bounded press-light run cleanly.

## Stage 3 Press-Light Robustness Scorecard

I then ran the full official chat catalog through a three-seed press-light robustness batch under
`/tmp/wopr_stage3_presslight_robustness`. The aggregate artifact is
`/tmp/wopr_stage3_presslight_robustness/press_light_aggregate.json`, and the checked-in scorecard
is `research/llm_model_calibration/stage3_press_light_scorecard.md`.

The run attempted 69 runs across 23 model lanes. It completed 51 runs and failed 18. Completed runs
recorded 1,729 decision traces, 363 press opportunities, 306 spoken messages, 57 declines, 0
invalid actions, and 0 retries. Recorded provider usage totaled 5,766,124 tokens. Applying the
catalog prices to recorded usage gives an estimated cost of `$4.29009455`; this is not a billing
statement.

Current working interpretation:

- `openai/gpt-oss-20b` with `reasoning_effort=low` remains the primary low-cost press-light lane:
  3/3 passed, all observed press opportunities spoken, and lowest 3/3 cost.
- `Qwen/Qwen2.5-7B-Instruct-Turbo`, `Qwen/Qwen3.5-9B`, and
  `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` are useful low-cost or diversity lanes.
- Kimi, GLM, Cogito, DeepSeek, Gemma 4, and Llama lanes are useful comparison lanes when sampled
  role-play behavior matters more than cost.
- `MiniMaxAI/MiniMax-M3` remains useful as a silent legality baseline, not as a press-light
  role-play lane.
- `google/gemma-3n-E4B-it` and `LiquidAI/LFM2-24B-A2B` are partial lanes, not defaults.
- MiniMax M2.7, Qwen Plus/Max lanes, and Pearl Gemma should stay on hold for press-light until a
  separate timeout or empty-content recovery task exists.

## Serverless Coverage

The official serverless catalog includes chat, image, vision, video, audio, and embedding models. It currently lists no serverless rerank models and no serverless moderation models. Rerank is documented as dedicated-only. Moderation is documented as unavailable through the serverless catalog.

## Next Calibration Plan

1. Use the Stage 3 scorecard to select models for the next LLM game runs.
2. Keep separate claims for catalog fit, Stage 2 WOPR one-turn behavior, no-press native Concordia
   behavior, and press-light behavior.
3. Treat role-play quality as a sampled qualitative code until a formal evaluator exists.

Current next action: use `research/llm_model_calibration/stage3_press_light_scorecard.md` and
`/tmp/wopr_stage3_presslight_robustness/press_light_aggregate.json` as the Stage 3 press-light
scorecard for candidate selection.

## Branch Finalization

The LLM model calibration study package is now collated for PR review. Use
`research/llm_model_calibration/README.md` as the entry point. It points to the catalog source,
findings narrative, run log, machine-readable state, Stage 3 scorecard, local visual walkthrough,
and raw Stage 3 aggregate.

The final operational grades are:

- A: GPT-OSS 20B, Qwen 2.5 7B, Qwen 3.5 9B, Qwen 235B throughput, and Llama 3 8B Lite.
- A-: Kimi, GLM, and Cogito comparison lanes.
- B+: DeepSeek, Gemma 4, Llama 3.3 70B, and GPT-OSS 120B comparison lanes.
- B: MiniMax M3 and Nemotron as narrow baseline lanes.
- C: Gemma 3N and Liquid as partial lanes.
- Hold: MiniMax M2.7, Qwen Plus/Max timeout lanes, and Pearl Gemma.

The next branch can begin LLM game experiments. The default lane remains GPT-OSS 20B with
`reasoning_effort=low`. Qwen 3.5 9B, Qwen 2.5 7B, and Qwen 235B throughput preserve low-cost or
model-family diversity. Kimi, GLM, Cogito, DeepSeek, Gemma 4, and Llama lanes are comparison lanes
for role-play behavior.
