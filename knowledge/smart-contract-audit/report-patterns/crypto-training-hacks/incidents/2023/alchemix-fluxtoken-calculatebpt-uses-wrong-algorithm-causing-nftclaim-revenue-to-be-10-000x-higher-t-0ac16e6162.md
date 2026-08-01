# Crypto Training Exploit Pattern Stub: Alchemix — `FluxToken.calculateBPT` uses wrong algorithm causing `nftClaim` revenue to be 10,000x higher than expected

Source:
- https://crypto.training/hacks/38191-fluxtokencalculatebpt-uses-wrong-algorithm-causing-fluxtoken/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `38191-fluxtokencalculatebpt-uses-wrong-algorithm-causing-fluxtoken`
- fingerprint: `0ac16e61620c494875dc7115273543f8518b96a760ae77835087236388f94573`

Core exploit idea:
- 1. FluxToken.bptMultiplier = 40 is documented as representing 0.4% (40 out of 10,000 bps). 2. calculateBPT(_amount) returns _amount * bptMultiplier without ever dividing…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
