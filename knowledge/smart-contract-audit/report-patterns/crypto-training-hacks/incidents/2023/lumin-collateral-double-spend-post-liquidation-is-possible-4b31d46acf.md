# Crypto Training Exploit Pattern Stub: Lumin — Collateral double-spend post liquidation is possible

Source:
- https://crypto.training/hacks/27233-c-01-collateral-double-spend-post-liquidation-is-possible-pa/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/accounting-desync, loss-of-funds/bad-debt, access-control/missing-check

Dedupe:
- id: `27233-c-01-collateral-double-spend-post-liquidation-is-possible-pa`
- fingerprint: `4b31d46acf31fea9190ab31763358befdc80fcbdb4a7596862f81fd0e1d948e9`

Core exploit idea:
- 1. AssetManager tracks each user's collateral in a UserDeposit{depositAmount, lockedAmount} struct. Withdrawals are gated on the free balance: depositAmount - lockedAmou…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
