# Crypto Training Exploit Pattern Stub: Amphor — exchange rate is calculated incorrectly when the vault is closed

Source:
- https://crypto.training/hacks/30918-h-3-exchange-rate-is-calculated-incorrectly-when-the-vault-i/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/rounding-mismatch, loss-of-funds/direct-drain, accounting/double-counted-offset

Dedupe:
- id: `30918-h-3-exchange-rate-is-calculated-incorrectly-when-the-vault-i`
- fingerprint: `8fc15faeb5961f67539e27f041107fc809144b0000a396c3912e4af12091b009`

Core exploit idea:
- 1. AsyncSynthVault.deposit()/redeem() (the standard open-vault ERC4626 path) use the FAIR conversion rate: assets.mulDiv(totalSupply()+1, totalAssets()+1) — a single +1…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
