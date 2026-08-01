# Crypto Training Exploit Pattern Stub: PegaBall — `buyGamesFrom` self-funds ticket purchases from the contract balance instead of `msg.value` — free vendor/referrer cut drain

Source:
- https://crypto.training/hacks/2025-06-PegaBall/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Ethereum

Loss / impact summary:
- ~0.579 ETH (~1,512.85 USD) — 129 free ticket purchases draining vendor + referrer cuts [o…

Tags:
- logic/incorrect-state-transition, access-control/broken-logic, dependency/unchecked-return-value

Dedupe:
- id: `2025-06-PegaBall`
- fingerprint: `9ff8c32196bec07220e280479d7d135b72c0fb7202825fdb6d8e47b9a6d8da6c`

Core exploit idea:
- PegaBall is an on-chain PowerBall-style lottery. Tickets are bought through buyGames / buyGamesFrom, both payable. The intended model is: a buyer sends amount * gamePric…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
