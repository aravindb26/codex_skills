# Crypto Training Exploit Pattern Stub: Burve — First deposit front-running attack

Source:
- https://crypto.training/hacks/57723-h-02-first-deposit-front-running-attack-pashov-audit-group-n/

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
- id: `57723-h-02-first-deposit-front-running-attack-pashov-audit-group-n`
- fingerprint: `7e737e9e1c4a654f4a3ad68a3609dbf1073d81742fdc770e1766831c72f09c5f`

Core exploit idea:
- 1. Alice mints 1 wei liquidity → 1 share (no dead shares). 2. Alice donates 1e18 of liquidity tokens, inflating totalNominalLiq. 3. Charlie mints 2e18 → shares = 2e18 *…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
