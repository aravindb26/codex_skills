# Crypto Training Exploit Pattern Stub: Ammplify malicious pool address — AuditVault 63179

Source:
- https://crypto.training/hacks/63179-ammplify-malicious-pool/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- input-validation/missing, access-control/missing-auth

Dedupe:
- id: `63179-ammplify-malicious-pool`
- fingerprint: `559e6178e6a99b6f7957f17810932e38345b0b0c5c949ee7f652ae5ac12586c4`

Core exploit idea:
- newMaker accepts an attacker-controlled pool and transfers protocol token accounting to it.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
