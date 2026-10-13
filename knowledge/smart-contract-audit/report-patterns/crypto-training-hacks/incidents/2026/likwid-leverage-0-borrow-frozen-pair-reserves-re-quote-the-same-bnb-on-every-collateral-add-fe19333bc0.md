# Crypto Training Exploit Pattern Stub: Likwid `leverage == 0` borrow — frozen pair reserves re-quote the same BNB on every collateral add

Source:
- https://crypto.training/hacks/2026-09-likwid/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- 74.310377807370642618 BNB taken from LikwidVault in this transaction (reported ~74.31 BNB…

Tags:
- logic/missing-state-update, defi/price-manipulation, logic/incorrect-accounting

Dedupe:
- id: `2026-09-likwid`
- fingerprint: `fe19333bc04813e30874dbd3ab89eab0a964ac174f8a7822f4fe47ddd7afa83f`

Core exploit idea:
- Likwid margin positions can be opened in two modes. leverage > 0 is a real leveraged swap: it writes delta.pairDelta, and the vault's marginBalance moves the pool. lever…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
