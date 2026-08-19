# Crypto Training Exploit Pattern Stub: Oku OracleLess: `procureTokens` pulls from the order recipient, letting an attacker steal a victim's approved tokens

Source:
- https://crypto.training/hacks/44378-h-8-insecure-calls-to-safetransferfrom-leads-to-users-tokens/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-check, defi/direct-drain, token/transferfrom-source

Dedupe:
- id: `44378-h-8-insecure-calls-to-safetransferfrom-leads-to-users-tokens`
- fingerprint: `e69ad2f73d9ac9e5667f1944e1c4e6989d5c0ce6775c483fb7841fa06a7ce3f1`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
