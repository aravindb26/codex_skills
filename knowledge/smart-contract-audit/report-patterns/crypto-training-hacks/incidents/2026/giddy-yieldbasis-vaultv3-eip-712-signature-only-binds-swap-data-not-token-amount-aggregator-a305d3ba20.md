# Crypto Training Exploit Pattern Stub: Giddy YieldBasis VaultV3 — EIP-712 signature only binds swap `data`, not token/amount/aggregator

Source:
- https://crypto.training/hacks/2026-04-giddyvaultv3_compound_auth/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- Ethereum

Loss / impact summary:
- ~$1.3M (in three YieldBasis gauge receipt tokens: ~3.53 g(yb-tBTC), ~6.94 g(yb-cbBTC), ~6…

Tags:
- auth/signature-validation, access-control/broken-logic, logic/missing-validation

Dedupe:
- id: `2026-04-giddyvaultv3_compound_auth`
- fingerprint: `a305d3ba209c04d237fb41a42f6142b9042be22f631d905bc8c68e40c7630096`

Core exploit idea:
- Giddy's YieldBasis vaults (a tBTC, a cbBTC, and a WBTC vault, all sharing the GiddyVaultV3 implementation) compound their strategy rewards through a signed VaultAuth mes…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
