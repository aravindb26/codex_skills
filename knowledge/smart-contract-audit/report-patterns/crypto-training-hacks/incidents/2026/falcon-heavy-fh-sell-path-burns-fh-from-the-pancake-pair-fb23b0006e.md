# Crypto Training Exploit Pattern Stub: Falcon Heavy (FH) — Sell Path Burns FH From the Pancake Pair

Source:
- https://crypto.training/hacks/2026-08-falconheavy/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~19,999 USDT (~$20K) — exact PoC match 19999018106552928530404 wei (~19,999.018 USDT)

Tags:
- defi/fee-manipulation, logic/incorrect-state-transition, defi/pair-reserve-desync

Dedupe:
- id: `2026-08-falconheavy`
- fingerprint: `fb23b0006e2726a594fb2fe7fd1b7451c5e895e5fa6bfa5c7374fb39d4b39866`

Core exploit idea:
- 1. FH is a fee-on-transfer / “deflationary” BSC token paired with USDT on PancakeSwap V2.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
