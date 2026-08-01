# Crypto Training Exploit Pattern Stub: Unlocking percentage formula applies an 80% penalty — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/43732-h-1-fluidlocker-getunlockingpercentage-incorrectly-divides-o/

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
- arithmetic/precision-loss, logic/price-calculation

Dedupe:
- id: `43732-h-1-fluidlocker-getunlockingpercentage-incorrectly-divides-o`
- fingerprint: `9ab22e19124d3e66c6fbc2bcaed74b9b49c24eb4cb3f8b0055acb05c41e5a74c`

Core exploit idea:
- The bug report discusses an issue with the FluidLocker::_getUnlockingPercentage() function in the Superfluid locking contract. The function incorrectly divides one of th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
