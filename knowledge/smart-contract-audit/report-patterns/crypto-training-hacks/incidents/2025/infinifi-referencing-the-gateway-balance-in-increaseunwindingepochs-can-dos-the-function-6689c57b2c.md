# Crypto Training Exploit Pattern Stub: InfiniFi — Referencing the gateway balance in `increaseUnwindingEpochs` can DoS the function

Source:
- https://crypto.training/hacks/55052-referencing-the-gateway-balance-in-lockingcontrollerincrease/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55052-referencing-the-gateway-balance-in-lockingcontrollerincrease`
- fingerprint: `6689c57b2ccd35968a7f1cc2c18f5af46ede9d270202843f70f83e186c976d9a`

Core exploit idea:
- 1. LockedPositionTokens are transferable until used to vote. 2. Bob transfers his position tokens to the gateway. 3. Alice deposits her own shares and approves only her…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
