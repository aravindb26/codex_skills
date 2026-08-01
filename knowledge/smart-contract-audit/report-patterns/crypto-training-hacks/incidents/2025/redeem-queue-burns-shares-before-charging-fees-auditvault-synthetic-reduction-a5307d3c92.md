# Crypto Training Exploit Pattern Stub: Redeem queue burns shares before charging fees — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/62111-h-6-redeems-through-redeemqueue-avoid-paying-management-and/

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
- logic/fee-calculation, logic/state-update

Dedupe:
- id: `62111-h-6-redeems-through-redeemqueue-avoid-paying-management-and`
- fingerprint: `a5307d3c92af561e5fd55b12238cf2284832d8fca95e6a8d03c15b97bbed0bea`

Core exploit idea:
- This bug report discusses an issue found by a group of users regarding the redeem function in the RedeemQueue contract. When a user redeems their shares, the shares are…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
