# Crypto Training Exploit Pattern Stub: FeeManager miscalculates performance fees — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/62110-h-5-incorrect-performance-fee-calculation-in-feemanager-sher/

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
- logic/fee-calculation, arithmetic/precision-loss

Dedupe:
- id: `62110-h-5-incorrect-performance-fee-calculation-in-feemanager-sher`
- fingerprint: `fdaf6f208fa0a19b77fc647fc2b4bd476f5b14da25746f732601faab24d2e8e0`

Core exploit idea:
- This bug report discusses an issue found in the performance fee calculation of the Mellow Flexible Vaults protocol. The current formula used in the FeeManager.calculateF…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
