# Crypto Training Exploit Pattern Stub: AAVE ParaSwap Repay Adapter — Lingering Allowance + Arbitrary-Call Collateral Drain

Source:
- https://crypto.training/hacks/2024-08-AAVE_Repay_Adapter/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Ethereum

Loss / impact summary:
- ~$56,000 across all tokens left in the adapter. PoC steals only the wstETH leg: 0.4259665…

Tags:
- unknown

Dedupe:
- id: `2024-08-AAVE_Repay_Adapter`
- fingerprint: `6a2928353ac8580dbbf30e8b3b64e258a05cd3020475dccda9fc80296f6cb9e5`

Core exploit idea:
- ParaSwapRepayAdapter is a helper contract that lets an Aave user "repay debt with collateral": it pulls the user's aTokens, withdraws the underlying collateral, sells it…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
