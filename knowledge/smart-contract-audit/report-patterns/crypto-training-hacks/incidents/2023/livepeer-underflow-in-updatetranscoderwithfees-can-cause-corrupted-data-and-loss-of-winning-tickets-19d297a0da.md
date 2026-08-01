# Crypto Training Exploit Pattern Stub: Livepeer — Underflow in updateTranscoderWithFees can cause corrupted data and loss of winning tickets

Source:
- https://crypto.training/hacks/27047-h-01-underflow-in-updatetranscoderwithfees-can-cause-corrupt/

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
- unknown

Dedupe:
- id: `27047-h-01-underflow-in-updatetranscoderwithfees-can-cause-corrupt`
- fingerprint: `19d297a0da1ce3dac0fcefaa2cc1c19f26c975b877c49ce1c35320efa869ec50`

Core exploit idea:
- 1. treasuryRewardCutRate stored as PreciseMathUtils % (1e27).\n2. updateTranscoderWithFees uses MathUtils.percOf (1e6).\n3. 10% cut (1e26) → treasuryRewards >> rewards →…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
