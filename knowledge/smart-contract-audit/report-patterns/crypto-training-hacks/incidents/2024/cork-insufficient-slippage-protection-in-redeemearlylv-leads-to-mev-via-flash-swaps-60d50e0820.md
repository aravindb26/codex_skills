# Crypto Training Exploit Pattern Stub: Cork — Insufficient slippage protection in `redeemEarlyLv` leads to MEV via flash swaps

Source:
- https://crypto.training/hacks/53126-insufficient-slippage-protection-in-redeemearlylv-leads-to-m/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `53126-insufficient-slippage-protection-in-redeemearlylv-leads-to-m`
- fingerprint: `60d50e08207ed72869efe4c1a5429fe76d6ece54112c471d36bd20dfa4d469c3`

Core exploit idea:
- 1. redeemEarlyLv takes amountOutMin and checks it only against RA from the AMM. 2. CT / DS / PA received have no floors. 3. Attacker skews the RA/CT pool (e.g. flash-sty…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
