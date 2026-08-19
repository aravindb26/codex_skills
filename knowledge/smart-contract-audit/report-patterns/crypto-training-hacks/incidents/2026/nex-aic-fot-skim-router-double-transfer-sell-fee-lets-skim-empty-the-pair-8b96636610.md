# Crypto Training Exploit Pattern Stub: NEX/AIC FoT Skim — Router Double-Transfer + Sell Fee Lets skim() Empty the Pair

Source:
- https://crypto.training/hacks/2026-08-nexaicfotskim/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~32.36 BNB (~$19.1K) (32361267289208020008 wei) — exact match to the live attack tx

Tags:
- logic/incorrect-state-transition, defi/fee-manipulation, logic/missing-check

Dedupe:
- id: `2026-08-nexaicfotskim`
- fingerprint: `8b966366104cfed1cc22774a9d43ae5af20ff4878008e0ad6b3cf217b52d22d7`

Core exploit idea:
- 1. NEX is a fee-on-transfer token with a 6% dao sell fee when the recipient is an AMM pair, and a special branch that is meant to skip fees when either side of the trans…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
