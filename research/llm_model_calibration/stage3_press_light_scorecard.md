# Stage 3 Press-Light Scorecard

I ran this scorecard to compare every official serverless chat model lane under the same bounded
press-light setup.

Artifact paths:

- Aggregate: `/tmp/wopr_stage3_presslight_robustness/press_light_aggregate.json`
- Run artifacts: `/tmp/wopr_stage3_presslight_robustness/runs`
- Configs: `/tmp/wopr_stage3_presslight_robustness/configs`

Controls:

- 23 model lanes, 3 seeds each, 69 attempted runs.
- Seeds 101, 102, and 103.
- Four `concordia_http` seats.
- `max_turns=3`, `temperature=0.7`, `max_tokens=512`, `stream=true`,
  `reasoning_enabled=false`.
- GPT-OSS lanes also used `reasoning_effort=low`.

Metric boundary:

- Run status, press count, spoken count, decline count, invalid actions, retries, token use, and
  catalog-priced cost are measured from artifacts.
- Role-play fit is a qualitative coding from sampled press messages, not a blinded evaluation.

## Aggregate Result

- Attempted runs: 69.
- Completed runs: 51.
- Failed runs: 18.
- Decision traces in completed runs: 1,729.
- Press messages in completed runs: 363.
- Spoken messages: 306.
- Declined messages: 57.
- Invalid action count in completed runs: 0.
- Retry count in completed runs: 0.
- Recorded tokens: 5,465,636 prompt, 300,488 completion, 5,766,124 total.
- Catalog-priced estimate from recorded usage: `$4.29009455`.

## Working Tiers

Tier A, primary low-cost working lanes:

- `openai/gpt-oss-20b`: 3/3 passed, all observed press messages spoken, lowest 3/3 cost.
- `Qwen/Qwen2.5-7B-Instruct-Turbo`: 3/3 passed, all press messages spoken, low cost.
- `meta-llama/Meta-Llama-3-8B-Instruct-Lite`: 3/3 passed with the short cap; keep context risk noted.
- `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`: 3/3 passed, all press messages spoken.
- `Qwen/Qwen3.5-9B`: 3/3 passed, strong low-cost comparison, two declines.

Tier B, role-play comparison lanes:

- `moonshotai/Kimi-K2.7-Code` and `moonshotai/Kimi-K2.6`: 3/3 passed, high spoken rate, more
  characterful sampled messages.
- `zai-org/GLM-5.2` and `zai-org/GLM-5.1`: 3/3 passed, all spoken, sampled messages were more
  state-aware than the cheaper generic lanes.
- `deepseek-ai/DeepSeek-V4-Pro`: 3/3 passed, good sampled role-play, higher cost.
- `deepcogito/cogito-v2-1-671b`: 3/3 passed and now recovered for press-light comparison.
- `google/gemma-4-31B-it`: 3/3 passed, more stylized messages, several declines.
- `meta-llama/Llama-3.3-70B-Instruct-Turbo`: 3/3 passed, all spoken, higher cost.
- `openai/gpt-oss-120b`: 3/3 passed with `reasoning_effort=low`, but GPT-OSS 20B is cheaper.

Tier C, usable baselines or narrow roles:

- `MiniMaxAI/MiniMax-M3`: 3/3 passed with clean decisions, but all press opportunities declined.
- `nvidia/nemotron-3-ultra-550b-a55b`: 3/3 passed, but declined most press opportunities.

Tier D, partial working lanes:

- `google/gemma-3n-E4B-it`: 2/3 passed, all press opportunities spoken in successful runs.
- `LiquidAI/LFM2-24B-A2B`: 1/3 passed, very low recorded cost, failures came from press output
  shape.

Tier E, not ready for press-light runs:

- `MiniMaxAI/MiniMax-M2.7`: 0/3, empty or partial content.
- `Qwen/Qwen3.7-Max`, `Qwen/Qwen3.6-Plus`, and `Qwen/Qwen3.7-Plus`: 0/3, timed out under the
  bounded runner.
- `pearl-ai/gemma-4-31b-it`: 0/3, missing or partial content.

## Model Results

| Model | Runs | Spoken / declined | Invalid / retry | Est. cost | Scorecard role |
|---|---:|---:|---:|---:|---|
| `openai/gpt-oss-20b` | 3/3 | 17 / 0 | 0 / 0 | `$0.01411500` | Primary low-cost lane |
| `meta-llama/Meta-Llama-3-8B-Instruct-Lite` | 3/3 | 22 / 0 | 0 / 0 | `$0.04788868` | Cheap short-context lane |
| `openai/gpt-oss-120b` | 3/3 | 19 / 5 | 0 / 0 | `$0.05381760` | Larger GPT-OSS comparison |
| `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` | 3/3 | 18 / 0 | 0 / 0 | `$0.06343160` | Large Qwen comparison |
| `Qwen/Qwen3.5-9B` | 3/3 | 20 / 2 | 0 / 0 | `$0.06615343` | Low-cost Qwen comparison |
| `Qwen/Qwen2.5-7B-Instruct-Turbo` | 3/3 | 24 / 0 | 0 / 0 | `$0.09883770` | Cheap all-spoken lane |
| `MiniMaxAI/MiniMax-M3` | 3/3 | 0 / 20 | 0 / 0 | `$0.10714590` | Silent legality baseline |
| `google/gemma-4-31B-it` | 3/3 | 15 / 5 | 0 / 0 | `$0.16610720` | Stylized comparison |
| `nvidia/nemotron-3-ultra-550b-a55b` | 3/3 | 7 / 15 | 0 / 0 | `$0.24922920` | Decline-heavy baseline |
| `meta-llama/Llama-3.3-70B-Instruct-Turbo` | 3/3 | 20 / 0 | 0 / 0 | `$0.32945432` | Larger Llama comparison |
| `moonshotai/Kimi-K2.7-Code` | 3/3 | 21 / 1 | 0 / 0 | `$0.39425595` | Role-play comparison |
| `deepcogito/cogito-v2-1-671b` | 3/3 | 18 / 4 | 0 / 0 | `$0.43290750` | Cogito comparison |
| `zai-org/GLM-5.1` | 3/3 | 20 / 0 | 0 / 0 | `$0.51477680` | State-aware comparison |
| `moonshotai/Kimi-K2.6` | 3/3 | 22 / 1 | 0 / 0 | `$0.52424940` | Role-play comparison |
| `zai-org/GLM-5.2` | 3/3 | 20 / 0 | 0 / 0 | `$0.56247520` | State-aware comparison |
| `deepseek-ai/DeepSeek-V4-Pro` | 3/3 | 19 / 4 | 0 / 0 | `$0.64104210` | Higher-cost role-play lane |
| `google/gemma-3n-E4B-it` | 2/3 | 16 / 0 | 0 / 0 | `$0.02041956` | Partial cheap lane |
| `LiquidAI/LFM2-24B-A2B` | 1/3 | 8 / 0 | 0 / 0 | `$0.00378741` | Partial low-cost lane |
| `MiniMaxAI/MiniMax-M2.7` | 0/3 | 0 / 0 | 0 / 0 | `$0.00000000` | Hold |
| `Qwen/Qwen3.7-Max` | 0/3 | 0 / 0 | 0 / 0 | `$0.00000000` | Hold, timeouts |
| `Qwen/Qwen3.6-Plus` | 0/3 | 0 / 0 | 0 / 0 | `$0.00000000` | Hold, timeouts |
| `pearl-ai/gemma-4-31b-it` | 0/3 | 0 / 0 | 0 / 0 | `$0.00000000` | Hold |
| `Qwen/Qwen3.7-Plus` | 0/3 | 0 / 0 | 0 / 0 | `$0.00000000` | Hold, timeouts |

## Next Use

For immediate LLM game work, I would use `openai/gpt-oss-20b` as the low-cost default, keep
`Qwen/Qwen3.5-9B` and `Qwen/Qwen2.5-7B-Instruct-Turbo` as low-cost alternates, and use Kimi,
GLM, Cogito, DeepSeek, Gemma 4, and Qwen 235B as comparison lanes when role-play behavior matters
more than cost. I would keep MiniMax M3 as a no-press or silent-control baseline, not as a
press-light role-play lane.
