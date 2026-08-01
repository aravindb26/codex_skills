# Crypto Training Exploit Pattern Stub: 540 seconds is used instead of 540 days — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/43733-h-2-fluidlocker-getunlockingpercentage-uses-540-instead-of-5/

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
- arithmetic/underflow, input-validation/boundary

Dedupe:
- id: `43733-h-2-fluidlocker-getunlockingpercentage-uses-540-instead-of-5`
- fingerprint: `75ee9e173b8be83943fb018f6e04cb8aeaa5eb81eeeb4c817eb25a5f2bc8e9b1`

Core exploit idea:
- The report discusses a bug found in the Superfluid locking contract, where the function _getUnlockingPercentage() incorrectly uses the number 540 instead of 540 days, le…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
