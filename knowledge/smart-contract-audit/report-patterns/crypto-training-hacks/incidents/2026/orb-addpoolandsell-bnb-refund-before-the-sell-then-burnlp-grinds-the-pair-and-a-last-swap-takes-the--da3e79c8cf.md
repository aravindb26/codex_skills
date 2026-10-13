# Crypto Training Exploit Pattern Stub: ORB `addPoolAndSell` — BNB refund before the sell, then `burnLP` grinds the pair and a last swap takes the WBNB

Source:
- https://crypto.training/hacks/2026-09-orb/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- 45.302221034270454423 BNB net to the attacker after repaying every flash-loan and Venus l…

Tags:
- reentrancy/cross-function, defi/reserve-manipulation, logic/incorrect-order-of-operations

Dedupe:
- id: `2026-09-orb`
- fingerprint: `da3e79c8cf18c42050b1fbd5172e0f5f3b7850721e032e6f49a722eca47a6fa5`

Core exploit idea:
- Sending BNB to ORBToken is an implicit sell. receive() max-approves the sender to ORBCore and calls addPoolAndSell{value: msg.value}(msg.sender). On the sell branch (0.0…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
