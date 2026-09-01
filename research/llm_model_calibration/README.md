# LLM Model Calibration Study

This directory is the review entry point for the current LLM model calibration branch.

## Study Boundary

I evaluated serverless chat model lanes for WOPR and Concordia experiment readiness. The grades
below are operational grades for this project, not general model-quality grades. They combine
completion, press participation, parser stability, cost, and sampled role-play fit.

Role-play fit is qualitative coding from sampled press traces. It is not a blinded evaluator score.
Cost values use recorded provider usage and catalog prices. They are not billing statements.

## Artifact Map

- Catalog source: `data/serverless_catalog_2026-07-05.json`
- Findings narrative: `findings.md`
- Run log: `research-log.md`
- Machine-readable state: `research-state.yaml`
- Stage 3 scorecard: `stage3_press_light_scorecard.md`
- Local visual walkthrough: `playground/stage3_results_playground.html`
- Stage 3 aggregate: `/tmp/wopr_stage3_presslight_robustness/press_light_aggregate.json`
- Stage 3 run artifacts: `/tmp/wopr_stage3_presslight_robustness/runs`

## Final Result

The final Stage 3 press-light run attempted 69 runs across 23 model lanes, with 3 seeds per lane.
It completed 51 runs and failed 18. Completed runs recorded 1,729 decision traces, 363 press
opportunities, 306 spoken messages, 57 declines, 0 invalid actions, and 0 retries. Recorded usage
was 5,766,124 tokens. The catalog-priced estimate was `$4.29009455`.

The repaired parser and provider paths are sufficient for moving into the next experiment phase.
The remaining blocked lanes need separate timeout, empty-content, or malformed-output recovery work.

## Operational Grades

| Grade | Models | Use |
|---|---|---|
| A | `openai/gpt-oss-20b`, `Qwen/Qwen2.5-7B-Instruct-Turbo`, `Qwen/Qwen3.5-9B`, `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`, `meta-llama/Meta-Llama-3-8B-Instruct-Lite` | Near-term LLM game lanes. |
| A- | `moonshotai/Kimi-K2.7-Code`, `moonshotai/Kimi-K2.6`, `zai-org/GLM-5.1`, `zai-org/GLM-5.2`, `deepcogito/cogito-v2-1-671b` | Role-play and behavior comparison lanes. |
| B+ | `deepseek-ai/DeepSeek-V4-Pro`, `google/gemma-4-31B-it`, `meta-llama/Llama-3.3-70B-Instruct-Turbo`, `openai/gpt-oss-120b` | Higher-cost comparison lanes. |
| B | `MiniMaxAI/MiniMax-M3`, `nvidia/nemotron-3-ultra-550b-a55b` | Baselines or narrow roles. |
| C | `google/gemma-3n-E4B-it`, `LiquidAI/LFM2-24B-A2B` | Partial lanes. Keep represented, but do not use as defaults. |
| Hold | `MiniMaxAI/MiniMax-M2.7`, `Qwen/Qwen3.7-Max`, `Qwen/Qwen3.6-Plus`, `Qwen/Qwen3.7-Plus`, `pearl-ai/gemma-4-31b-it` | Not ready for press-light. |

## Recommended Next Experiment Set

Use `openai/gpt-oss-20b` with `reasoning_effort=low` as the default low-cost lane.

Use these alternates to preserve diversity:

- `Qwen/Qwen3.5-9B`
- `Qwen/Qwen2.5-7B-Instruct-Turbo`
- `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`

Use these comparison lanes when role-play behavior matters more than cost:

- Kimi lanes
- GLM lanes
- Cogito
- DeepSeek
- Gemma 4
- larger Llama and GPT-OSS lanes

Use these baselines deliberately:

- `MiniMaxAI/MiniMax-M3` for silent legality checks.
- `nvidia/nemotron-3-ultra-550b-a55b` for decline-heavy press behavior.

## PR Review Notes

This branch now contains the provider controls, parser repairs, calibration state, final scorecard,
and local visual walkthrough needed to review the LLM study work. The next branch can begin actual
LLM game experiments using the recommended model set above.
