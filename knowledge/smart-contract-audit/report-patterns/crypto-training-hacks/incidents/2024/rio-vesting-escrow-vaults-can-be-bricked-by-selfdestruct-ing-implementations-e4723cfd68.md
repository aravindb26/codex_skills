# Crypto Training Exploit Pattern Stub: Rio Vesting Escrow — vaults can be bricked by selfdestruct()ing implementations

Source:
- https://crypto.training/hacks/29688-h-1-vaults-can-be-bricked-by-selfdestructing-implementations/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/forgeable-immutable-args, logic/delegatecall-target-confusion, loss-of-funds/frozen-funds

Dedupe:
- id: `29688-h-1-vaults-can-be-bricked-by-selfdestructing-implementations`
- fingerprint: `e4723cfd689f2639e299663e24a6327d92726561bb5b268944ddf9349dfef970`

Core exploit idea:
- 1. Every Rio escrow "clone" is a thin proxy that DELEGATECALLs a single SHARED implementation contract for all of its logic. 2. That implementation reads its own factory…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
