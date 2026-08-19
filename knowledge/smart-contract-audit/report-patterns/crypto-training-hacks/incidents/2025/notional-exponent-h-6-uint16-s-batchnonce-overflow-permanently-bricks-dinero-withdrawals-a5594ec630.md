# Crypto Training Exploit Pattern Stub: Notional Exponent H-6: `uint16 s_batchNonce` overflow permanently bricks Dinero withdrawals

Source:
- https://crypto.training/hacks/62487-h-6-dos-might-happen-to-dinerowithdrawrequestmanager-initi/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `62487-h-6-dos-might-happen-to-dinerowithdrawrequestmanager-initi`
- fingerprint: `a5594ec6309d7aca82b5cdd7023424a73a79d56024777686343155a5e3edbc3e`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
