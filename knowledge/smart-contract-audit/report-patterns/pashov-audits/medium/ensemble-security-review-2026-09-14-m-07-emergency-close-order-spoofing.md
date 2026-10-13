# Pashov Audit Pattern: Favorable order-book quotes can make emergency close orders non-marketable

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Ensemble Security Review` (team PDF, M-07)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Ensemble-security-review_2026-09-14.pdf>
- Dedupe decision: Distinct from ordinary spot-price manipulation; the issue is one-sided emergency-price clamping combined with asynchronous IOC execution.

## Core Idea

Emergency close accepts a favorable best bid or offer without bounding it to a trusted mark, so an attacker can show removable liquidity during the read and leave the submitted IOC unfilled.

## Broken Invariant

Emergency orders must remain executable under the trusted reference price even when observed order-book liquidity disappears before asynchronous processing.

## Where To Look

- Emergency liquidation pricing from BBO or thin order books
- One-sided price clamps that accept all apparently favorable prices
- Async order submission without fill or residual-position confirmation

## Attack Path

Present a favorable quote, let the vault construct a reduce-only order, remove the quote before processing, and keep the vault's position open while recovery assumes the close succeeded.

## False-Positive Checks

- Confirm the order is actually asynchronous and not atomically matched
- Verify the attacker can alter the quote before execution
- Trace retries, residual position checks, and withdrawal gating

## PoC Shape

Use a controllable order-book mock or fork to show the quote passes validation, disappears before execution, and leaves nonzero exposure after the close attempt.

## Triage Note

The impact is strongest when an emergency state blocks users while the unclosed position can still lose value.
