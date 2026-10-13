# Pashov Audit Pattern: A ratio oracle caps one leg but not the other

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Pare Security Review` (team PDF, M-03)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Pare-security-review_2026-10-01.pdf>
- Dedupe decision: Distinct asymmetric-boundary pattern; the code protects one side of a correlated ratio while leaving the inverse side open.

## Core Idea

An oracle caps a stablecoin or PT ratio in one direction but does not cap the correlated inverse leg, so a temporary premium or discount can create a liquidation price inconsistent with the intended bound.

## Broken Invariant

All economically equivalent directions of a bounded ratio must respect the same conservative price limits.

## Where To Look

- Ratio calculations with one-sided `min`/`max` clamps
- Stablecoin premium/discount handling and inverse price branches
- Liquidation or collateral valuation using the uncapped leg

## Attack Path

Move the correlated asset to the unbounded side of the ratio, let the oracle calculate the inverse leg without the matching cap, and trigger an incorrect liquidation or borrowing limit.

## False-Positive Checks

- Evaluate both token orderings and both premium directions
- Confirm the bound is reachable through a supported market or feed
- Trace whether downstream code applies an equivalent second cap

## PoC Shape

Run the oracle against mirrored price inputs and assert that the intended symmetric bound holds in both directions.

## Triage Note

Do not report a mathematical asymmetry without showing a material collateral or solvency consequence.
