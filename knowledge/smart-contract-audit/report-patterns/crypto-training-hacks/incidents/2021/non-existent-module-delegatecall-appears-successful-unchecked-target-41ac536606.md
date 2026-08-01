# Crypto Training Exploit Pattern Stub: Non-existent module delegatecall appears successful — unchecked target

Source:
- https://crypto.training/hacks/16975-lack-of-contract-existence-check-on-delegatecall-may-lead-to/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2021

Chain:
- Ethereum

Loss / impact summary:
- Batches silently skip a module call and continue with stale state

Tags:
- dependency/unsafe-external-call, input-validation/missing

Dedupe:
- id: `16975-lack-of-contract-existence-check-on-delegatecall-may-lead-to`
- fingerprint: `41ac5366067c1de54f8ca1079be2cca6526a12095854a6b3149363dc86449a19`

Core exploit idea:
- delegatecall to an EOA or destroyed contract returns true. Ladle's module registry can therefore mark a no-code address as valid and report a successful module execution…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
