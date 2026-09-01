# Cut the experiment and package the evidence boundary

Status: Accepted

## Context

The U.S. Room, its two-cycle workflow, its open-output contracts, the
fail-closed proposal interpreter, and deterministic rehearsal machinery were
implemented and tested offline. The live DATE evaluation was not completed.
Continuing to treat a successful provider run as a submission gate would spend
the remaining deadline on execution controls while leaving the actual contest
entry incoherent and risk presenting implementation evidence as behavioral
evidence.

The contest contribution is the institutional Room model and the evaluation
design. DATE remains the primary open World. Nuclear War remains the future
closed-form comparison World for the same Room.

## Decision

Stop live provider execution, retries, model comparison, M7, and the same-Room
Nuclear War run for this submission. Preserve their code, receipts, and failed
attempt history as deferred engineering work, but do not make them the public
narrative.

Package every public claim in one of four classes:

- **Implemented** means the repository contains working machinery covered by
  local tests or deterministic replay.
- **Executed evidence** means a retained run or rehearsal supports the exact
  stated observation.
- **Specified but not evaluated** means the design is concrete but has no
  completed behavioral comparison.
- **Future work** names extensions outside the submitted evidence.

The application and microsite must center the U.S. Situation Room, Episode 1,
the open proposal-to-consequence path, the offline scaffold, and the proposed
comparison. They must say plainly that no live DATE behavioral result exists.
Only cheap local publication checks may run before submission.

## Alternatives retained

- Finishing the live DATE evaluation before packaging was rejected for this
  deadline because it made an incomplete provider run block a coherent entry.
- Cutting DATE and reverting to the completed Nuclear War Sounding was rejected
  because the institutional Room in an open crisis World is the contribution.
- Presenting retry controls, packet hashes, or failed provider attempts as the
  main story was rejected because they support provenance rather than the
  research question.
- Claiming preliminary DATE behavior from scripted rehearsals or partial live
  responses was rejected because neither is a completed evaluation.

## Consequences

The release can be complete without a successful live DATE run, but it cannot
claim model performance, policy quality, institutional effects, or World
outcomes that were not evaluated. The authoritative evidence matrix now
controls public wording. The retained live-run machinery can support later
experiments without reopening the submission narrative.
