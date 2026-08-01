# Crypto Training Exploit Pattern Stub: Aera Contracts v3 — incorrect received-swap-amount calculation lets guardians bypass the daily loss limit

Source:
- https://crypto.training/hacks/58289-incorrect-calculation-of-the-received-swap-amount-allows-gua/

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
- logic/fee-calculation, accounting/balance-delta-double-count, loss-of-funds/partial-drain

Dedupe:
- id: `58289-incorrect-calculation-of-the-received-swap-amount-allows-gua`
- fingerprint: `98eb6d5b2d10e47cb9977c6bd6c171f0166e49ba7c008062adb2978118e583fb`

Core exploit idea:
- 1. Aera's slippage hook enforces a daily loss limit on guardian-directed swaps. To do so, its after-hook measures how much tokenOut the vault received as a balance delta…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
