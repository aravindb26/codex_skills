# Pashov Audit Pattern: Collapsed actions reuse the first timestamp across all legs

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Pare Security Review` (team PDF, M-04)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Pare-security-review_2026-09-17.pdf>
- Dedupe decision: Distinct from non-collapsed composites stamped with the last action; here a collapsed resolution writes every leg at the first observation time.

## Core Idea

A collapsed multiplier record preserves only the first timestamp, so later decomposed dividend actions are backdated before a vault maturity.

## Broken Invariant

Post-maturity value changes must not be included in a pre-maturity principal/yield checkpoint.

## Where To Look

- Collapsed or batched oracle updates with one shared timestamp
- Decomposition into multiple dividend/split legs
- Maturity-dependent index snapshots and settlement calculations

## Attack Path

Leave an early update pending, apply a later dividend after maturity, resolve the collapsed record, and show the later dividend is credited to the pre-maturity index.

## False-Positive Checks

- Verify the later action is actually included in the collapsed record
- Check whether per-leg timestamps are stored or reconstructed
- Compare the settlement checkpoint with a control that syncs each action separately

## PoC Shape

Use timestamps before and after maturity, resolve one collapsed record, and assert that the post-maturity leg does not alter the pre-maturity index.

## Triage Note

The strongest impact is misallocation between PT and YT or blocked settlement, not merely an inaccurate timestamp field.
