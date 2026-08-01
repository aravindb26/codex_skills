# Crypto Training Exploit Pattern Stub: Karak — [H-02] An operator can create a `NativeVault` that is silently unslashable

Source:
- https://crypto.training/hacks/41066-h-02-the-operator-can-create-a-nativevault-that-can-be-silen/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-validation, logic/missing-check, dos/permanent

Dedupe:
- id: `41066-h-02-the-operator-can-create-a-nativevault-that-can-be-silen`
- fingerprint: `75a176550a253994679753fcb67b0785e9f078f02597e2acc90a6c1f2ef6009d`

Core exploit idea:
- 1. In Karak, an operator deploys a NativeVault via Core.deployVaults(), passing extraData = (manager, slashStore, nodeImplementation). 2. NativeVault.initialize() stores…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
