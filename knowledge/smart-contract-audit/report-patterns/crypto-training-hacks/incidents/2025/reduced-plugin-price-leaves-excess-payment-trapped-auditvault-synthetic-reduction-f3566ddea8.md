# Crypto Training Exploit Pattern Stub: Reduced plugin price leaves excess payment trapped — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/53453-h-01-excess-payment-when-plugin-owner-reduces-price-shieldif/

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
- logic/fee-calculation, input-validation/missing

Dedupe:
- id: `53453-h-01-excess-payment-when-plugin-owner-reduces-price-shieldif`
- fingerprint: `f3566ddea8a1fa6d8de6cb2b0ac0fc66152fa5fd67361fe056768d00dd08147d`

Core exploit idea:
- The report discusses a bug in the Multicall contract where the click() function does not properly check the msg.value sent by users. This can lead to a vulnerability whe…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
