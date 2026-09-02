# M3 live preflight promotion handoff

Status: operator instructions only. These commands do not contact a provider,
authorize spend, publish artifacts, or submit the contest form.

The live preflight produces a passing receipt that is still `pending_owner`.
After reviewing that receipt, obtain a second approval by binding the exact
receipt hash. Keep both approval files redacted and outside the repository.

Build the receipt-bound promotion approval:

```bash
cd nuclear_war
uv run nuclear-war contest-build-promotion-approval \
  --approval /path/to/owner-approval.json \
  --receipt /tmp/wopr-live-preflight.json \
  --out /tmp/wopr-promotion-approval.json
```

The command copies the first approval fields and adds a hash of the completed
live receipt. It does not mark the receipt approved by itself.

After the second approval is reviewed, bind it into an approved preflight
receipt:

```bash
cd nuclear_war
uv run nuclear-war contest-promote-preflight \
  --manifest /path/to/new-candidate-manifest.json \
  --receipt /tmp/wopr-live-preflight.json \
  --approval /tmp/wopr-promotion-approval.json \
  --out /tmp/wopr-approved-preflight.json
```

The output is a validated, candidate-bound receipt with an approved live
preflight sidecar. The study manifest must then be materialized from this
receipt under the same source revision, model settings, prompt hashes, seeds,
retry policy, and request budget. Do not edit the checked-in candidate packet
in place; retain it as the pre-approval record.

Before study execution, validate the materialized manifest with the runner and
confirm that the approved receipt path and SHA-256 are recorded. A pending or
unbound packet must fail before an output directory is created.
