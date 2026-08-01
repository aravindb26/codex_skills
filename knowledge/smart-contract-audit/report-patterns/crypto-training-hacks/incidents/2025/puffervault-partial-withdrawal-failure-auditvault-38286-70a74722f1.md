# Crypto Training Exploit Pattern Stub: PufferVault partial withdrawal failure — AuditVault 38286

Source:
- https://crypto.training/hacks/38286-puffer-partial-withdrawal-failure/

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
- logic/incorrect-state-transition, dos/frozen-funds

Dedupe:
- id: `38286-puffer-partial-withdrawal-failure`
- fingerprint: `70a74722f18426b89048a6ec8859f181865748b3d88b85b992fa5b522722502d`

Core exploit idea:
- A partial failure returns early and silently leaves later withdrawal requests unhandled.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
