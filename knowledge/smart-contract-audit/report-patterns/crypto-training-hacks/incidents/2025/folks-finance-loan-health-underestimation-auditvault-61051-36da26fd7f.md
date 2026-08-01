# Crypto Training Exploit Pattern Stub: Folks Finance loan-health underestimation — AuditVault 61051

Source:
- https://crypto.training/hacks/61051-folks-unlimited-loan-health/

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
- logic/liquidation-logic, arithmetic/precision-loss

Dedupe:
- id: `61051-folks-unlimited-loan-health`
- fingerprint: `36da26fd7fcc3c728636024eadf995a72ccb17599b19ba2effe972ff877d768d`

Core exploit idea:
- The health calculation overstates collateral capacity and permits an outsized loan for a minimal deposit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
