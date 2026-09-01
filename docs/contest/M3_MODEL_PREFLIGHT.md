# M3 model preflight packet

Status: corrected six-cell live preflight passed and was promoted on 2026-08-21
for executor `fd48b11e49675c3a8a82319e13f07c7900a5ddba`. Its compact receipt is
[CORRECTED_RUN_RECEIPT.json](CORRECTED_RUN_RECEIPT.json). The historical executor is
`09421afee7a0c763127d0ec5e460f7d94a596bdc`. Historical live receipt file:
[MODEL_PREFLIGHT_RECEIPT.live.json](MODEL_PREFLIGHT_RECEIPT.live.json),
SHA-256 `7dd927a53d97ffcce85d3562ef35446003f7f8f9beefe13f559a84ab948552a6`.
The selected pair is recorded in
[`MODEL_MANIFEST.deepseek_flash_gpt_oss_20b.candidate.json`](MODEL_MANIFEST.deepseek_flash_gpt_oss_20b.candidate.json)
with the offline planning receipt
[`MODEL_PREFLIGHT_RECEIPT.deepseek_flash_gpt_oss_20b.json`](MODEL_PREFLIGHT_RECEIPT.deepseek_flash_gpt_oss_20b.json).

The owner has set a hard total API ceiling of $1,000, including screening,
preflight,
composition smoke, pilot, retries, and study execution. The checked-in
historical candidate and receipt still contain a $5,000 planning value and
must not be used for live calls; the pair-specific packet below is the current
offline candidate under the hard ceiling.

## What is frozen in the candidate packet

The owner-facing model replacement fields and historical approval sequence are
in [M3_MODEL_DECISION_PACKET.md](M3_MODEL_DECISION_PACKET.md). The corrected
runtime approval was consumed for the executor-bound run and remains outside
the public packet because it names the private receipt path.

The pair-specific candidate names two direct-API models selected by the
screening rule:

- `deepseek-ai/DeepSeek-V4-Flash-0731`, recorded as the DeepSeek family.
- `openai/gpt-oss-20b`, recorded as the GPT-OSS family.

The screening receipts are retained outside the repository under
`/private/tmp/wopr-contest-screening-20260816`; they establish operational
admissibility for these two lanes, not strategic behavior in the contest study.
Current endpoint availability, pricing, prompt usage, and preflight behavior
still require the owner-approved live preflight.

The candidate settings are the same across both models where the provider
supports the field: Together's HTTPS endpoint, a fixed model identifier, a
60-second timeout, temperature `0.0`, `max_tokens=512`, streaming enabled, and
reasoning disabled. Together's reasoning documentation lists both model IDs and
documents `reasoning={"enabled": false}` for Qwen hybrid models; the HTTP client
therefore emits that control rather than relying on an undocumented prompt
convention. GPT-OSS additionally records `reasoning_effort=low`, the control used
by the existing calibration. The model is pinned in the manifest; `model_env` is
intentionally absent so an unrecorded environment override cannot change the
tested model.

The screening packet and pair-specific candidate pin Together's HTTPS endpoint,
the exact model identifiers, `$0.14`/`$0.28` rates for DeepSeek V4 Flash, and
`$0.05`/`$0.20` rates for GPT-OSS 20B. Rates and endpoint behavior must still
be rechecked when creating the owner approval packet. The live preflight must
record exact responses, usage, retries, and provider-model identity; the
offline receipt is not a substitute for that evidence.

The three preflight seeds, 91-93, are disjoint from the proposed study seeds,
51-55. The preflight packet keeps the four conditions and five seeds per model
explicit, so changing the design changes the receipt rather than silently
changing the cost calculation.

## Offline request and cost envelope

The packet records the largest observed offline fixture counts, 564 C2 member
calls plus 60 full-press calls per game, in
`M3_OFFLINE_FIXTURE_MEASUREMENTS.json`. That artifact retains the producer
command, a hashed source snapshot, the three disjoint preflight seeds, and
per-seed measurements. The loader recomputes the maxima and checks both file
hashes before producing the receipt. These are reproducible planning inputs,
not model results and not a proof of a 40-round maximum.

The candidate also records a fail-closed operational cap of 2,048 C2 calls and
160 press calls per game. The press cap follows four players, 40 rounds, and
one pass. The C2 cap is deliberately a large operational ceiling because the
engine exposes several decision phases per player-turn. M4 must enforce these
caps and classify an over-cap run as Tier C; the pending-owner packet does not
claim that the engine's state machine can never exceed them.

The provider retry layers permit one decision retry and up to two additional
transport attempts for each decision attempt, giving a multiplier of
`(1 + 1) * (1 + 2) = 6`. The packet records that transport cap explicitly;
the live runner must preserve the same cap before any spend is authorized.

With 40 proposed games, the operational caps above, an 8,192-input-token
planning bound per request, and a 512-token output cap, the pair-specific
generated receipt reports:

| Quantity | Bound |
| --- | ---: |
| Operational base calls per game | 2,208 |
| Provider request attempts | 529,920 |
| Input tokens | 4,341,104,640 |
| Output tokens | 271,319,040 |
| DeepSeek V4 Flash candidate envelope | $341.861990 |
| GPT-OSS 20B candidate envelope | $135.659520 |
| Combined catalog-rate envelope | $477.521510 |

The pair-specific candidate uses a proposed `$500` study cap, leaving room
under the owner's hard `$1,000` total ceiling for screening, preflight,
composition smoke, and retries. Both model availability and rates must be
refreshed against the provider before any live spend decision. The input-token
figure is still a planning bound until the runner records actual usage; it must
not be presented as a completed study cost.

Generate the receipt without network access:

```bash
cd nuclear_war
UV_CACHE_DIR=/tmp/wopr-uv-cache uv run --extra dev python -m nuclear_war_env.cli \
  contest-preflight \
  --manifest /path/to/new-candidate-manifest.json \
  --out /tmp/wopr-model-preflight.json
```

The receipt is `pending_owner`, records `network_calls: 0` and
`credentials_read: false`, and includes the candidate manifest hash. It cannot
authorize or execute a live run.

## First owner-approval packet

Keep this JSON outside the repository and create it only after confirming the
endpoint, credential environment, model identifiers, executor revision, and
maximum spend. It contains no credential value. The live command rejects the
packet if any field is changed, if the candidate hash differs, or if the
executor SHA is not the clean checkout.

```json
{
  "schema_version": 1,
  "candidate_manifest_hash": "<sha256 of the new candidate manifest>",
  "approved": false,
  "max_spend_usd": 0.0,
  "model_ids": ["<candidate model id 1>", "<candidate model id 2>"],
  "endpoints": ["<endpoint 1>", "<endpoint 2>"],
  "credential_envs": ["<credential env 1>", "<credential env 2>"],
  "executor_revision": "<40-character clean Git SHA>"
}
```

Set `approved` to `true` only as the owner's authorization decision. The
candidate hash, endpoint list, credential-environment list, model IDs, and
executor revision must be generated from the reviewed packet, not guessed from
the command line. Replace the fail-closed `0.0` placeholder only with an
owner-approved maximum at least as large as the candidate's calculated upper
bound; that value is still an owner spend decision.

The CLI loads `TOGETHER_API_KEY` from the repository `.env` file if that
variable is not already set. It does not load `.env.secret`.

After explicit owner approval of the endpoint, credentials path, and maximum
spend, run the candidate-bound live preflight with the separate network flag:

```bash
cd nuclear_war
uv run nuclear-war contest-live-preflight \
  --manifest /path/to/new-candidate-manifest.json \
  --out /tmp/wopr-live-preflight.json \
  --allow-network \
  --approval /path/to/owner-approval.json \
  --executor-revision <full-executor-sha>
```

This makes one bounded request per model and preflight seed, records provider
attempts, usage, latency, prompt hashes, and redacted failure types, and keeps
the receipt `pending_owner` until it is reviewed and bound into a promoted
study manifest. The approval JSON contains no secret, but binds the candidate
hash, exact endpoint and credential-environment names, maximum spend, and full
executor SHA. The completed receipt receives a second owner approval whose
hash binds the exact live evidence before it can authorize the study. The
promotion commands are documented in [M3_PROMOTION.md](M3_PROMOTION.md). The
CLI also requires that the executor SHA match a clean checkout. Omitting
either `--allow-network` or the first owner packet fails before any request,
including when a test transport is injected.

`STUDY_MANIFEST.candidate.json` is the corresponding 40-cell study handoff. It
copies the four conditions, five study seeds, two candidate model settings,
role-prompt hashes, retry policy, channel caps, token and cost bounds, and the
receipt binding. Its `pending_owner` status is intentional: the runner rejects
it before creating an output directory until the receipt is refreshed and
approved.

## Owner gates before M4

1. Confirm that both model identifiers, endpoint behavior, and prices are
   current on the intended provider.
2. Decide whether the provisional temperature-0 control is the desired study
   setting. If it changes, regenerate the candidate packet and receipt.
3. Set an explicit maximum spend at or above the refreshed bound and authorize
   the credentials path. No credential is written to the repository.
4. Run the three preflight seeds through the live direct API, retaining usage,
   retry, latency, and provider-error receipts. A failed candidate is replaced
   only before study execution and under a new manifest hash.
5. Promote the reviewed candidate into the frozen `MODEL_MANIFEST.json`; the
   runner must continue to reject `pending_owner` packets as study inputs.
   The superseded 2026-08-18 promotion wrote `MODEL_MANIFEST.json`,
   `MODEL_PREFLIGHT_RECEIPT.live.json`, and
   `STUDY_MANIFEST.room_instrument.json`. The Sounding ran under executor
   `09421afee7a0c763127d0ec5e460f7d94a596bdc`. The corrected run requires a
   new clean executor, live receipt, receipt-hash approval, and promotion.

Headless code-agent execution remains a separate backend decision. It is not
interchangeable with these direct API lanes until executable version, model selection,
hidden retries, trace retention, applicable terms, and a separate parity check are recorded.
