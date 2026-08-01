# Crypto Training Exploit Pattern Stub: Kinetiq — Exchange rate implementation not used in token operations

Source:
- https://crypto.training/hacks/58615-h-07-exchange-rate-implementation-not-used-in-token-operatio/

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
- id: `58615-h-07-exchange-rate-implementation-not-used-in-token-operatio`
- fingerprint: `c363aa3d073077d2c96852e2fcccdc5ba6ae686c724f6ce2903e8e863d110ae6`

Core exploit idea:
- 1. getExchangeRatio / kHYPEToHYPE / HYPEToKHYPE implement NAV-based rates. 2. stake() still does kHYPE.mint(msg.sender, msg.value) (1:1). 3. Withdraw pays 1 HYPE per kHY…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
