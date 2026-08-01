# Crypto Training Exploit Pattern Stub: VII Finance — liquidations can be made to revert by an attacker

Source:
- https://crypto.training/hacks/61327-liquidations-can-be-made-to-revert-by-an-attacker-through-va/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61327-liquidations-can-be-made-to-revert-by-an-attacker-through-va`
- fingerprint: `9e737557f6e9e0fb02d5502d0c650c9b0cd7ada6b0497f8a7d5ef938c62ea1dd`

Core exploit idea:
- 1. A borrower can enableTokenIdAsCollateral for a tokenId they do not hold. 2. Liquidation seizes value via transfer, which walks all enabled tokenIds. 3. normalizedToFu…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
