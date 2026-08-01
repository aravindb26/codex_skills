# Crypto Training Exploit Pattern Stub: Royco ERC4626i — Missing permissions check in withdraw and redeem

Source:
- https://crypto.training/hacks/46674-missing-permissions-check-in-withdraw-and-redeem-functions-i/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-modifier

Dedupe:
- id: `46674-missing-permissions-check-in-withdraw-and-redeem-functions-i`
- fingerprint: `f12fee1882cc67143c0e1ee40621fa6ca9ab05b8dd7a073be68c60e35cb89056`

Core exploit idea:
- 1. ERC-4626 redeem(shares, receiver, owner) must require msg.sender == owner or sufficient allowance. 2. Royco's ERC4626i omits that check entirely. 3. An attacker calls…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
