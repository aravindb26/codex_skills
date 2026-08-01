# Crypto Training Exploit Pattern Stub: SHELL MEV-Bot Drain — Permissionless Arbitrage Function with Attacker-Chosen Recipient

Source:
- https://crypto.training/hacks/2024-01-Shell_MEV_0xa898/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- BNB Chain

Loss / impact summary:
- ~$1,000 (≈ 1,250 BUSD of the victims' stablecoin balances; SlowMist lists ~$1K). Two MEV-…

Tags:
- access-control/missing-auth, access-control/missing-modifier

Dedupe:
- id: `2024-01-Shell_MEV_0xa898`
- fingerprint: `29058cc81c5ed0b5fb6eb4972f9292bc8a7c245aec44c0c38c7d57a689522d80`

Core exploit idea:
- Two BSC MEV/arbitrage bots ("Robot1", "Robot2") expose a permissionless function with selector 0x5f90d725. The bot owners had pre-approved the bots to spend their BUSD a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
