# Crypto Training Exploit Pattern Stub: Lumi Finance (Sodium ERC-4337 account) — Signature-Bypass Drain

Source:
- https://crypto.training/hacks/2026-07-LumiFinance/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Arbitrum

Loss / impact summary:
- Multi-asset drain across ~50 Sodium smart accounts (≈ $264k reported). This fork replay m…

Tags:
- auth/signature-validation, access-control/broken-logic, input-validation/missing

Dedupe:
- id: `2026-07-LumiFinance`
- fingerprint: `2340d07efb4ccbc57e4d2ed8aaee4f73953a8ea92d3403c3dfe36d01e4b8b270`

Core exploit idea:
- Sodium is Lumi Finance's ERC-4337 v0.6 smart-account wallet, and its owner check is forgeable: it trusts a signer address taken from the attacker-supplied UserOperation…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
