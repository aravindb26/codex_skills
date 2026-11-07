# Crypto Training Exploit Pattern Stub: Argent relay modules — a public owner signature is replayed, and the recovery deadline can be wrapped into the past

Source:
- https://crypto.training/hacks/2026-10-argent/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Ethereum

Loss / impact summary:
- unknown

Tags:
- auth/signature-replay

Dedupe:
- id: `2026-10-argent`
- fingerprint: `3d9dc3aa5081e9656252a8576c978e72b2709560019ae67abd90cb87f8eb36b2`

Core exploit idea:
- Two Argent-style wallets are drained, in the test's account of the incident, by relaying signatures that have been public since 2020 and 2021. The execution module's exe…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
