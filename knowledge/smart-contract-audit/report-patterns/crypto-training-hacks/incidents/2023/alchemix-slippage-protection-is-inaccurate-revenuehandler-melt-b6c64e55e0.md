# Crypto Training Exploit Pattern Stub: Alchemix — slippage protection is inaccurate (`RevenueHandler._melt`)

Source:
- https://crypto.training/hacks/38184-slippage-protection-is-inaccurate-immunefi-alchemix-git/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/naive-slippage-check, mev/sandwich-attack, economic/price-manipulation

Dedupe:
- id: `38184-slippage-protection-is-inaccurate-immunefi-alchemix-git`
- fingerprint: `b6c64e55e0a4e864e6ed12cd02ad49a26bfaeafae05534f6c14ab02c827cef02`

Core exploit idea:
- 1. RevenueHandler._melt(revenueToken) swaps revenueTokenBalance of a revenue token (e.g. WETH) for its paired alAsset (e.g. alETH) through a pool adapter. 2. It passes r…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
