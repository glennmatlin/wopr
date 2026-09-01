# Serverless Model Survey for WOPR Calibration

## What I Checked

I reviewed the official serverless model catalog, recommended-model guide, rate-limit guide, and OpenAI-compatible endpoint guide on 2026-07-05. I also queried `/v1/models` with the local API key and printed only sanitized metadata.

The live endpoint returned 271 records. That endpoint appears to be a broader provider model inventory, not only the serverless catalog. I therefore use the official serverless docs as the source of record for availability and pricing.

## Main Finding

`openai/gpt-oss-20b` is the best first calibration target for WOPR and Concordia. It has 128k context, documented function calling, documented structured outputs, and a listed price of $0.05 input and $0.20 output per 1M tokens. It is also the model pattern already used by the current no-press Concordia endpoint example.

`Qwen/Qwen3.5-9B` is the best Qwen candidate. It has 262k context and the same documented function and structured-output capability flags, but it costs more than `openai/gpt-oss-20b` on input and output. It is useful as a second lane because the larger context may reduce prompt-length risk.

## Low-Cost Exploratory Models

`LiquidAI/LFM2-24B-A2B` is the cheapest listed chat model at $0.03 input and $0.12 output per 1M tokens. It has 32k context and no documented structured-output flag in the serverless table.

`google/gemma-3n-E4B-it` is listed at $0.06 input and $0.12 output per 1M tokens. It also has 32k context and no documented structured-output flag in the serverless table.

These two should be tested only with short WOPR-native no-press JSON prompts before considering longer calibration.

## Bounded Smoke Results

`openai/gpt-oss-20b` passed direct HTTP and one-turn native Concordia smokes.

`Qwen/Qwen3.5-9B` passed direct HTTP and one-turn native Concordia smokes.

`LiquidAI/LFM2-24B-A2B` passed the direct HTTP JSON smoke.

`google/gemma-3n-E4B-it` passed the direct HTTP JSON smoke.

The direct smoke needed a 256-token completion cap. Smaller caps caused empty final content on the primary candidates because completion tokens were spent before the final JSON answer.

## Avoid for Native Concordia Now

`meta-llama/Meta-Llama-3-8B-Instruct-Lite` is listed at $0.14 input and $0.14 output per 1M tokens, but its 8k context is too small for observed native Concordia prompts. I would not use it for native Concordia calibration.

## Coverage Notes

The official serverless docs list 23 chat rows, 29 image rows, 5 vision rows, 37 video rows, 9 audio rows, and 1 embedding row. They list no serverless rerank models and no serverless moderation models.

## Next Calibration Step

Run bounded, single-request smokes in this order:

1. Add a calibration runner that records provider usage, latency, parse status, and selected legal action.
2. Run it for `openai/gpt-oss-20b` and `Qwen/Qwen3.5-9B`.
3. Extend it to short WOPR-native prompts for `LiquidAI/LFM2-24B-A2B` and `google/gemma-3n-E4B-it`.

Stop before overnight batches unless the calibration artifacts validate.
