# Crypto Training Exploit Pattern Stub: ParaSpace — [H-05] Attacker can manipulate low-TVL Uniswap V3 pool to borrow

Source:
- https://crypto.training/hacks/15978-h-05-attacker-can-manipulate-low-tvl-uniswap-v3-pool-to-borr/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `15978-h-05-attacker-can-manipulate-low-tvl-uniswap-v3-pool-to-borr`
- fingerprint: `08f9fc98db31cad938faed9a20cf529742ac9fd67501924a790707c26f612f18`

Core exploit idea:
- 1. Any UniV3 position whose tokens are listed can be collateral. 2. Value = token amounts in the position × external oracle prices (no pool TVL check). 3. Attacker owns…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
