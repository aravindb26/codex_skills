# Crypto Training Exploit Pattern Stub: Linea TokenBridge upgrade — permissionless reinitialization drains locks

Source:
- https://crypto.training/hacks/65618-after-the-upgrade-permissionless-attacker-can-fully-drain-th/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/uninitialized-proxy, access-control/missing-auth

Dedupe:
- id: `65618-after-the-upgrade-permissionless-attacker-can-fully-drain-th`
- fingerprint: `6d3d2a671d45bf6b76e834ec6425b3683a5e295219351d43ad68586e86bf1874`

Core exploit idea:
- Replacing an inherited initializer changes the storage layout. The live bridge appears uninitialized, letting an arbitrary caller become admin, install an attacker messa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
