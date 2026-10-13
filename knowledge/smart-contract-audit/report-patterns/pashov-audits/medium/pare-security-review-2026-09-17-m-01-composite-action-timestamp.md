# Pashov Audit Pattern: A non-collapsed composite action inherits only the last timestamp

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Pare Security Review` (team PDF, M-01)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Pare-security-review_2026-09-17.pdf>
- Dedupe decision: Distinct from collapsed-action timestamp reuse; this branch records a multi-action jump as non-collapsed and stamps it with the last action.

## Core Idea

When multiple multiplier actions occur between observations, the accountant records one composite as non-collapsed and attributes all value to the last action's effective time.

## Broken Invariant

Settlement and maturity accounting must preserve the effective time of every value-changing action, even when observations batch several actions together.

## Where To Look

- Oracles or accountants that infer action history from endpoint values
- Composite updates classified as ordinary single actions
- Maturity checkpoints and yield/principal attribution after delayed sync

## Attack Path

Let two actions occur before `sync()`, place the final timestamp after maturity, and show that settlement excludes the earlier action from yield attribution or shifts it to the wrong holder class.

## False-Positive Checks

- Prove multiple actions can occur without an intermediate observation
- Confirm the classifier does not force guardian review for the composite
- Trace the exact maturity checkpoint written to downstream vaults

## PoC Shape

Apply two updates around a maturity boundary with one sync and compare per-leg accounting against a control with two syncs.

## Triage Note

Keep separate from any path where a collapsed record reuses the first timestamp; the state and fix differ.
