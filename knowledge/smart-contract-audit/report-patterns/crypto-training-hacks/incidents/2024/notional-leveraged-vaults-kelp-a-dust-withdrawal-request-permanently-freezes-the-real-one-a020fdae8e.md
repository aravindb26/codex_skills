# Crypto Training Exploit Pattern Stub: Notional Leveraged Vaults (Kelp) — a dust withdrawal request permanently freezes the real one

Source:
- https://crypto.training/hacks/35126-h-13-kelp-finalizecooldown-cannot-claim-the-withdrawal-if-ad/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds, logic/hardcoded-index, access-control/permissionless-griefing

Dedupe:
- id: `35126-h-13-kelp-finalizecooldown-cannot-claim-the-withdrawal-if-ad`
- fingerprint: `a020fdae8efb89e5af71d7a2c1adb3d8b0f2826df44120da4029b9d7a7829b95`

Core exploit idea:
- 1. KelpCooldownHolder._finalizeCooldown() always looks at index 0 of LidoWithdraw.getWithdrawalRequests(address(this)) to decide what's finalized and what to claim. 2. L…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
