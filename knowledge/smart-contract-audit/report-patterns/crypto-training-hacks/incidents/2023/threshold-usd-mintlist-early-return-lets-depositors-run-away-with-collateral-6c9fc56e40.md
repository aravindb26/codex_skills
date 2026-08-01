# Crypto Training Exploit Pattern Stub: Threshold USD — mintList early-return lets depositors run away with collateral

Source:
- https://crypto.training/hacks/54691-requirevalidadjustmentincurrentmode-bypass-when-not-in-mintl/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `54691-requirevalidadjustmentincurrentmode-bypass-when-not-in-mintl`
- fingerprint: `6c9fc56e40d10c008bd53cea5ece8e48319e7c9cc35bb45c846fb0aa80403432`

Core exploit idea:
- 1. When BorrowerOperations is removed from thUSD.mintList, adjustment guards early-return. 2. ICR / recovery-mode checks never run for withdrawColl. 3. Alice withdraws n…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
