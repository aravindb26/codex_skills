# Crypto Training Exploit Pattern Stub: Edel xStock — ERC4626 convertToAssets Donation Inflates Collateral and Drains Reserves

Source:
- https://crypto.training/hacks/2026-07-edel-xstock/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Ethereum

Loss / impact summary:
- 204,215.57 USDC + multi-asset xStock wrappers (wSPYx/wQQQx/wMSTRx/wNVDAx/wTSLAx)

Tags:
- defi/donation-attack, oracle/price-manipulation, defi/flash-loan-attack

Dedupe:
- id: `2026-07-edel-xstock`
- fingerprint: `a122f42f976c7ee125d08b770504f6b4a8176dea4c106a5fef22a9feaad17330`

Core exploit idea:
- 1. Edel markets treat wrapped xStock tokens (e.g. wGOOGLx) as collateral. Pricing goes through an AaveOracle path that ultimately depends on the wrapper's live convertTo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
