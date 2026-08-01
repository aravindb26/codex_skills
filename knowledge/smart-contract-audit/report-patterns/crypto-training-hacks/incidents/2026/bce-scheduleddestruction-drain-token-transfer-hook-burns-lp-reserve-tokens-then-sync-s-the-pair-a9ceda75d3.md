# Crypto Training Exploit Pattern Stub: BCE `scheduledDestruction` drain — token transfer hook burns LP reserve tokens then `sync()`s the pair

Source:
- https://crypto.training/hacks/2026-03-bce/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~800,000 USDT (BCE/USDT pair drained to 259,506 wei of USDT; attacker realizes ~680,000 U…

Tags:
- logic/state-update, defi/fee-manipulation, logic/incorrect-order-of-operations

Dedupe:
- id: `2026-03-bce`
- fingerprint: `a9ceda75d372e7a3c0fd5cf92d3fe92c1e8b27c1ac6e57cf534a204512168f08`

Core exploit idea:
- BCE is an ERC-20 with a deflationary "scheduled destruction" mechanism: every sell into the BCE/USDT PancakeSwap pair adds value per 10 / 100 BCE to a global scheduledDe…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
