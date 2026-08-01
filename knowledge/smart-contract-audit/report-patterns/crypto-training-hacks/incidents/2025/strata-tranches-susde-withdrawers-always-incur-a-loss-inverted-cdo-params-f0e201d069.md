# Crypto Training Exploit Pattern Stub: Strata Tranches — sUSDe withdrawers always incur a loss (inverted CDO params)

Source:
- https://crypto.training/hacks/63222-withdrawers-of-susde-always-incur-a-loss-because-parameters/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63222-withdrawers-of-susde-always-incur-a-loss-because-parameters`
- fingerprint: `f0e201d06953d3725fb52ef67be76f8d27d5a4a182e8b0fa6d582c394489cc61`

Core exploit idea:
- 1. Withdraw of 100 sUSDe (worth 150 USDe at 1.5 rate) burns 150 JRT shares. 2. Tranche passes (baseAssets, tokenAssets) but CDO expects (tokenAmount, baseAssets). 3. Str…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
