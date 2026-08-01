# Crypto Training Exploit Pattern Stub: Canto (veRWA) — unguarded `checkpoint_lender`/`checkpoint_market` let anyone grief a lender's reward to 0

Source:
- https://crypto.training/hacks/26975-h-07-lack-of-access-control-in-lendingledgersolcheckpoint-le/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-modifier, dos/griefing, logic/incomplete-guard

Dedupe:
- id: `26975-h-07-lack-of-access-control-in-lendingledgersolcheckpoint-le`
- fingerprint: `a898dde1375d1b43bee4e020d6ebb2d7763d9137e32f89d058ca3c3dbaba5518`

Core exploit idea:
- 1. A lender deposits cNote into a whitelisted lending market. sync_ledger records the deposit and tracks the epoch it was last updated at. 2. checkpoint_lender(market, l…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
