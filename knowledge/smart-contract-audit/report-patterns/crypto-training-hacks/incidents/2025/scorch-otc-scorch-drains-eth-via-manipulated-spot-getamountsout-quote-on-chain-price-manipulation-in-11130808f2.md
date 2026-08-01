# Crypto Training Exploit Pattern Stub: Scorch OTC `scorch()` drains ETH via manipulated spot `getAmountsOut` quote — on-chain price manipulation in a burn-for-ETH function

Source:
- https://crypto.training/hacks/2025-02-Scorch/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Ethereum

Loss / impact summary:
- ~0.14 ETH on-chain (public report); 0.337 ETH reproduced in the offline fork trace [outpu…

Tags:
- oracle/price-manipulation, oracle/spot-price, logic/price-calculation, defi/flash-loan-attack

Dedupe:
- id: `2025-02-Scorch`
- fingerprint: `11130808f2fa1776d5eb3e80eb2b037965ef3f833871370f3232b4caefa40bc7`

Core exploit idea:
- Scorch (OTC) is an ERC-20 whose contract holds an ETH treasury. Its scorch(amount) function lets any holder burn their OTC tokens and receive ETH directly from the contr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
