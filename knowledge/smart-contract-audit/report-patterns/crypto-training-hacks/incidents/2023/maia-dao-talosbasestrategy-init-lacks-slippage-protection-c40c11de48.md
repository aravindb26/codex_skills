# Crypto Training Exploit Pattern Stub: Maia DAO — TalosBaseStrategy#init() lacks slippage protection

Source:
- https://crypto.training/hacks/26044-h-10-talosbasestrategyinit-lacks-slippage-protection-code4re/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `26044-h-10-talosbasestrategyinit-lacks-slippage-protection-code4re`
- fingerprint: `c40c11de48d417399c7a5f0c0e95ba1f05d993bbf1b8ca4cb2465ddc1bdc232d`

Core exploit idea:
- 1. deposit() has checkDeviation; init() does not.\n2. amount0Min/amount1Min hardcoded to 0.\n3. Price manipulation drains 99% of init deposit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
