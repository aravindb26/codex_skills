# Crypto Training Exploit Pattern Stub: Mass — low-level call to an empty account falsely succeeds

Source:
- https://crypto.training/hacks/29664-low-level-call-missing-existence-check/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dependency/unsafe-external-call, input-validation/missing, logic/wrong-condition

Dedupe:
- id: `29664-low-level-call-missing-existence-check`
- fingerprint: `d40a43e0dc1bb8b9e6cbf7a0a415b182c596e4491a91a95c7baaa93b6f673c36`

Core exploit idea:
- The helper accepts delegatecall success from an account with no code. EVM semantics return true for an empty destination, so the caller observes success without executin…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
