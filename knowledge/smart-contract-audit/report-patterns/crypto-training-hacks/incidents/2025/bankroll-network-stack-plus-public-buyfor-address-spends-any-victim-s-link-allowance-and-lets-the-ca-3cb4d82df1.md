# Crypto Training Exploit Pattern Stub: Bankroll Network Stack Plus — public `buyFor(address,...)` spends any victim's LINK allowance and lets the caller skim the dividend pool it just inflated

Source:
- https://crypto.training/hacks/2025-06-BankrollStackPlus/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Ethereum

Loss / impact summary:
- ~12,234.48 USD (933.93 LINK net to the attacker) [output.txt:1565,1977]

Tags:
- access-control/missing-auth, logic/incorrect-state-transition, defi/fee-manipulation

Dedupe:
- id: `2025-06-BankrollStackPlus`
- fingerprint: `3cb4d82df15d787b7acfa6a90fbb0f4fa28e5648a9daecae99a3fc1a0c5c918d`

Core exploit idea:
- BankrollNetworkStackPlus is an old-school "dividend drip" farming contract (a POWH/Bankroll-network descendant) priced 1:1 in LINK. Every buy pays a 10% entry fee, a 10%…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
