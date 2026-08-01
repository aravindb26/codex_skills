# Crypto Training Exploit Pattern Stub: Blueberry HyperVaultRouter — missing asset index check mints shares for any token

Source:
- https://crypto.training/hacks/61477-c-02-missing-asset-index-check-allows-any-token-to-mint-shar/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition

Dedupe:
- id: `61477-c-02-missing-asset-index-check-allows-any-token-to-mint-shar`
- fingerprint: `ab889391729e90d111dd12626c5bbad4f13386d051d67a469371bbb9ace28eeb`

Core exploit idea:
- 1. deposit(asset, amount) looks up assetIndexes[asset] and requires _isAssetSupported. 2. Unregistered tokens return mapping default 0, and USDC is hardcoded as index 0.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
