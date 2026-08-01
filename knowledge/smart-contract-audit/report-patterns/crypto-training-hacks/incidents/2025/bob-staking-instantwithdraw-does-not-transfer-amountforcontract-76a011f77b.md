# Crypto Training Exploit Pattern Stub: BOB Staking — instantWithdraw does not transfer amountForContract

Source:
- https://crypto.training/hacks/63717-c-01-instantwithdraw-does-not-transfer-amountforcontract-lo/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/frozen-funds

Dedupe:
- id: `63717-c-01-instantwithdraw-does-not-transfer-amountforcontract-lo`
- fingerprint: `76a011f77b05735c8498911abd1b252dfb018297140076456c8e7158f40cf659`

Core exploit idea:
- 1. Delegated stake lives in a DelegationSurrogate. 2. instantWithdraw pulls only _amountForUser from the surrogate. 3. _amountForContract (penalty) is never transferred…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
