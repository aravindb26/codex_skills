# Crypto Training Exploit Pattern Stub: Ammplify maker spot-price manipulation — AuditVault 63167

Source:
- https://crypto.training/hacks/63167-ammplify-maker-spot-price/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/spot-price, defi/fee-manipulation

Dedupe:
- id: `63167-ammplify-maker-spot-price`
- fingerprint: `853de2b176e51629570b657e46ca46cbf2b566aa476fa8661f20d476ca0201bd`

Core exploit idea:
- Maker deposits value liquidity using a manipulable Uniswap spot price.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
