# Crypto Training Exploit Pattern Stub: Value DeFi vSafe WBNB Vault — Inflated-Share Mint via Manipulated Alpaca `ibBNB` Strategy Price

Source:
- https://crypto.training/hacks/2021-05-ValueDefi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2021

Chain:
- BNB Chain

Loss / impact summary:
- attacker minted 396.17 vSafeWBNB shares for a 273.81 WBNB net deposit — a ~44% over-issue…

Tags:
- oracle/price-manipulation, governance/flash-loan-attack, arithmetic/rounding

Dedupe:
- id: `2021-05-ValueDefi`
- fingerprint: `a8ef9b8d56eb3f07cfb70714ec81d6d9f9a5aa39684d62265d7f8e3e15514a9c`

Core exploit idea:
- VSafeVaultWBNB is a yield vault that mints shares to depositors in proportion to deposit / pricePerShare, where the share price is derived from the vault's total holding…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
