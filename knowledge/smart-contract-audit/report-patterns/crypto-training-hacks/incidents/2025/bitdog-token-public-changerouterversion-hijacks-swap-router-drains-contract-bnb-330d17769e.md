# Crypto Training Exploit Pattern Stub: BITDOG token — public `changeRouterVersion` hijacks swap router & drains contract BNB

Source:
- https://crypto.training/hacks/2025-04-bitdog/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- BNB Chain

Loss / impact summary:
- 2.101368297037048768 BNB (~2.10 BNB)

Tags:
- access-control/missing-modifier, access-control/missing-owner-check, oracle/price-manipulation

Dedupe:
- id: `2025-04-bitdog`
- fingerprint: `330d17769e51b376fbbd8e32bf49e5887645e284e0492631e62c02b2a0c93d76`

Core exploit idea:
- BITDOG is a fee-on-transfer BEP-20 that holds its collected swap fees in BNB inside the token contract itself. When any transfer pushes the contract's own token balance…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
