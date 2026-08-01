# Crypto Training Exploit Pattern Stub: Burve — Incorrect handling of ERC4626 vaults with fees

Source:
- https://crypto.training/hacks/56950-h-1-incorrect-handling-of-erc4626-vaults-with-fees-sherlock/

Imported:
- 2026-08-01

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
- id: `56950-h-1-incorrect-handling-of-erc4626-vaults-with-fees-sherlock`
- fingerprint: `8d57a4cf605c4d93c1017c7daa4efc750f68598d852994464ea5eaacb9309176`

Core exploit idea:
- 1. Pool deposits user tokens into an ERC4626 that takes a 1% deposit fee. 2. Protocol still credits full value despite fewer shares minted. 3. User withdraws full credit…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
