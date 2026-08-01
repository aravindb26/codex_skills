# Crypto Training Exploit Pattern Stub: Lumin — Disabled lender's loan configuration can be used by a borrower

Source:
- https://crypto.training/hacks/27234-h-01-disabled-lenders-loan-configuration-can-be-used-by-a-bo/

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
- access-control/missing-check, logic/state-flag-ignored

Dedupe:
- id: `27234-h-01-disabled-lenders-loan-configuration-can-be-used-by-a-bo`
- fingerprint: `acd3be51cdc1bffa625e79280cb15b38e4ef777a8ea530bb2750cb2bd96001b6`

Core exploit idea:
- 1. A LoanConfig has an enabled flag, true by default, that a lender can flip to false via updateLoanConfigEnabledStatus — her only lever to stop further loans from being…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
