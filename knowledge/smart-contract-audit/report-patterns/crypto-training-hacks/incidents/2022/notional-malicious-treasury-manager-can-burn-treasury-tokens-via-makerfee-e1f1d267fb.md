# Crypto Training Exploit Pattern Stub: Notional — malicious treasury manager can burn treasury tokens via makerFee

Source:
- https://crypto.training/hacks/24657-h-03-a-malicious-treasury-manager-can-burn-treasury-tokens-b/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `24657-h-03-a-malicious-treasury-manager-can-burn-treasury-tokens-b`
- fingerprint: `e1f1d267fbbf2d6ec456f2aec1701bb53962f005b6739cfad178001b182940bc`

Core exploit idea:
- 1. Treasury manager signs 0x orders to sell harvested COMP for WETH. 2. _validateOrder never requires makerFee == 0 and takerFee == 0. 3. Malicious manager sets makerFee…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
