# Crypto Training Exploit Pattern Stub: Forte Float128 — [H-02] Sqrt silently stops the entire call frame on packed 0

Source:
- https://crypto.training/hacks/55704-h-02-sqrt-function-silently-reverts-the-entire-control-flow/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55704-h-02-sqrt-function-silently-reverts-the-entire-control-flow`
- fingerprint: `c8ed7c5ea73ae69086c782647cc7543dbd0b3a535dcc1f6f678b08f4854b36ab`

Core exploit idea:
- 1. Mathematically, sqrt(0) = 0. 2. Float128 uses assembly stop() on packed zero — equivalent to return(0,0) for the entire call frame. 3. Because sqrt is internal pure,…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
