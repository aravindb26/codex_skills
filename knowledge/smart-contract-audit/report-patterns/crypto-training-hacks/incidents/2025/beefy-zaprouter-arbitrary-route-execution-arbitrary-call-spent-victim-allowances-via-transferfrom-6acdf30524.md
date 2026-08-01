# Crypto Training Exploit Pattern Stub: Beefy ZapRouter arbitrary route execution — arbitrary `call()` spent victim allowances via `transferFrom`

Source:
- https://crypto.training/hacks/2025-08-BeefyZapRouter/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Arbitrum

Loss / impact summary:
- ~6,584.95 USD (2,782.482 vault-A mooTokens + 2,779.111 vault-B mooTokens stolen from two…

Tags:
- access-control/missing-validation, logic/missing-check, dependency/unsafe-external-call

Dedupe:
- id: `2025-08-BeefyZapRouter`
- fingerprint: `6acdf30524b3c2652dd3838ee9742d0a39b1c471525614379461b20859ee439f`

Core exploit idea:
- Beefy's BeefyZapRouter is a generic "zap" router: a user deposits input tokens, the router runs an arbitrary caller-supplied list of Steps (each a low-level target.call(…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
