# Crypto Training Exploit Pattern Stub: BitBay StableVault — withdraw on an empty position pays the caller the whole vault, uncapped by shares

Source:
- https://crypto.training/hacks/2026-10-bitbaystablevault/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Polygon

Loss / impact summary:
- 14,838.466608989135865711 DAI — the vault's entire idle balance, sent to the attacker by…

Tags:
- logic/missing-check, defi/share-accounting, defi/price-manipulation

Dedupe:
- id: `2026-10-bitbaystablevault`
- fingerprint: `3e43973944bb99a7a567d6a077170c4d5d3a218fb2b005f80d8787d0b158baa3`

Core exploit idea:
- UsdcDaiV4Vault keeps its funds as a single Uniswap v4 DAI/USDC position. withdraw(shareAmount, deadline, addDust) is supposed to burn shareAmount and return the caller t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
