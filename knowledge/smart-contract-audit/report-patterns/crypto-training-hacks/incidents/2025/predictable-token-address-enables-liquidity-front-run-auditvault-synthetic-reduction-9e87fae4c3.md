# Crypto Training Exploit Pattern Stub: Predictable token address enables liquidity front-run — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/57870-h-03-predictable-token-deployment-address-enables-liquidity/

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
- access-control/broken-logic, defi/sandwich-attack

Dedupe:
- id: `57870-h-03-predictable-token-deployment-address-enables-liquidity`
- fingerprint: `9e87fae4c315d4b266040266ab1bde609b0ce5129a773aebacb3be07e0a647e4`

Core exploit idea:
- This report describes a high-risk bug that allows an attacker to manipulate the deployment of a contract called DaosToken within the DaosLive contract. This predictabili…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
