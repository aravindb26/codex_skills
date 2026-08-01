# Crypto Training Exploit Pattern Stub: Biconomy Composability — [C-01] Missing DelegateCall check

Source:
- https://crypto.training/hacks/63148-c-01-missing-delegatecall-check-pashov-audit-group-none-bico/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-guard

Dedupe:
- id: `63148-c-01-missing-delegatecall-check-pashov-audit-group-none-bico`
- fingerprint: `80571875c54ee1a68153d41aec6530bf10399b3f4a860058a552325d4f662335`

Core exploit idea:
- 1. executeComposableDelegateCall is meant only via smart-account CALLTYPE_DELEGATECALL. 2. There is no check that address(this) differs from the module’s immutable deplo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
