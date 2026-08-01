# Crypto Training Exploit Pattern Stub: Tapioca DAO — BalancerStrategy _withdraw scales WETH as BPT

Source:
- https://crypto.training/hacks/27530-h-40-balancerstrategysol-withdraw-withdraws-insufficient-to/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `27530-h-40-balancerstrategysol-withdraw-withdraws-insufficient-to`
- fingerprint: `e871bd79a903b025152cbdf8f978b39f916daf41c27d8874a9f1b95f9afbee19`

Core exploit idea:
- 1. _withdraw converts desired WETH → BPT-like figure via getRate. 2. _vaultWithdraw encodes type-2 exact-tokens-out with that figure as minAmountsOut. 3. Vault pays only…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
