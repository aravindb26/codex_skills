# Crypto Training Exploit Pattern Stub: Liquid Ron — totalAssets wrong when operatorFeeAmount > 0

Source:
- https://crypto.training/hacks/50051-h-01-the-calculation-of-totalassets-could-be-wrong-if-operat/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `50051-h-01-the-calculation-of-totalassets-could-be-wrong-if-operat`
- fingerprint: `d22a04d92a3bd3f6cf44cf553ad8cba45a86c64eecefb492a8444d94beb8d310`

Core exploit idea:
- 1. Operator fee sits in the vault balance and is tracked in operatorFeeAmount. 2. totalAssets() still counts that fee toward share pricing. 3. New depositor mints fewer…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
