# Crypto Training Exploit Pattern Stub: Notional Exponent H-9: hardcoded `use_eth = true` on Curve V2 exit locks WETH-vault funds

Source:
- https://crypto.training/hacks/62490-h-9-hardcoded-useeth-true-in-remove-liquidity-one-coin-or-/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `62490-h-9-hardcoded-useeth-true-in-remove-liquidity-one-coin-or-`
- fingerprint: `3d03df81217991817c244b134845f4ca665cc8c842c3e07d5803f818b776aa88`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
