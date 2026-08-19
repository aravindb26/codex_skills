# Crypto Training Exploit Pattern Stub: YieldFi CCIP: missing source validation lets an untrusted chain drive privileged mint/unlock

Source:
- https://crypto.training/hacks/55536-missing-source-validation-in-ccip-message-handling-cyfrin-no/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55536-missing-source-validation-in-ccip-message-handling-cyfrin-no`
- fingerprint: `c367dc35f8c6fe5b32d48746b535c960b0e60dbaf9112eeaf5c40089e2793823`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
