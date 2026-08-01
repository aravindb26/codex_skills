# Crypto Training Exploit Pattern Stub: Recall — [H-05] Incorrect supply fund transferral in leave()

Source:
- https://crypto.training/hacks/65092-h-05-incorrect-supply-fund-transferral-in-function-leave-can/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65092-h-05-incorrect-supply-fund-transferral-in-function-leave-can`
- fingerprint: `d078185e7cf006c0cd7c672a6718c2f17903e37a9d44e3c1318f39b702c91c1f`

Core exploit idea:
- leave() pays genesisBalance as ETH collateral instead of supply ERC20 — drains other validators

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
