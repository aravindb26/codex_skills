# Crypto Training Exploit Pattern Stub: maxRedeem permits leverage above the configured buffer — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/28949-h-2-vault-leverage-can-be-increased-to-any-value-up-to-min-m/

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
- logic/incorrect-state-transition, logic/price-calculation

Dedupe:
- id: `28949-h-2-vault-leverage-can-be-increased-to-any-value-up-to-min-m`
- fingerprint: `f4eb159739ff10194137091e9246db72c8c5a80ae0884e40591ca83529e8d7c4`

Core exploit idea:
- A bug report has been identified in the Vault leverage calculations. The bug is caused by incorrect maxRedeem calculations with closable and LEVERAGE_BUFFER. This was fo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
