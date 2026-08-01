# Crypto Training Exploit Pattern Stub: Liquidator can increase a position while liquidating — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/28948-h-1-liquidator-can-liquidate-user-while-increasing-user-posi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/liquidation-logic, input-validation/missing

Dedupe:
- id: `28948-h-1-liquidator-can-liquidate-user-while-increasing-user-posi`
- fingerprint: `bb2e8d0ab12edacd5a1a6d3eb262014536e5a093503a9fff59963888cdad0883`

Core exploit idea:
- This bug report is about a vulnerability found in the Market contract of the Perennial Protocol. The vulnerability allows a malicious liquidator to liquidate a user whil…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
