# Crypto Training Exploit Pattern Stub: Hybra Finance — Assets deposited before calculating shares to mint

Source:
- https://crypto.training/hacks/63707-h-01-assets-deposited-before-calculating-shares-amount-to-mi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-order

Dedupe:
- id: `63707-h-01-assets-deposited-before-calculating-shares-amount-to-mi`
- fingerprint: `37fe0ff34bf3161e5542b2b3ee879532873912cff03b432b73fee64f6c821d6a`

Core exploit idea:
- 1. deposit first moves HYBR into the voting escrow (increasing totalAssets). 2. Then shares = calculateShares(amount) uses the post-deposit total. 3. At 1:1 with 100 alr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
