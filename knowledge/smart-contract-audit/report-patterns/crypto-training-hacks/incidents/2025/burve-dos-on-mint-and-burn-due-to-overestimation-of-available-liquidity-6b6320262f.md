# Crypto Training Exploit Pattern Stub: Burve — DoS on `mint()` and `burn()` due to overestimation of available liquidity

Source:
- https://crypto.training/hacks/57722-h-01-dos-on-mint-and-burn-due-to-overestimation-of-available/

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
- id: `57722-h-01-dos-on-mint-and-burn-due-to-overestimation-of-available`
- fingerprint: `6b6320262f2af0c8ea81d38560275dd9869e70a37c02463a015f2091bd339ad4`

Core exploit idea:
- 1. Every mint/burn runs compoundV3Ranges → collectAndCalcCompound. 2. With 2 equal ranges and 1 wei residual, nominal liq is computed as 14. 3. Real mintable liquidity i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
