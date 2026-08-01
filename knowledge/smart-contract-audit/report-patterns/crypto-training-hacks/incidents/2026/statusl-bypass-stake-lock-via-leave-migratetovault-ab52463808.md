# Crypto Training Exploit Pattern Stub: Statusl — bypass stake lock via leave + migrateToVault

Source:
- https://crypto.training/hacks/65328-user-can-bypass-lock-and-withdraw-stake-anytime-cyfrin-none/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65328-user-can-bypass-lock-and-withdraw-stake-anytime-cyfrin-none`
- fingerprint: `ab52463808e680e6aed10c39c7810d284b0c6d720bccbb0cfaf98b65245ce353`

Core exploit idea:
- 1. Stake with a multi-year lock for max multiplier. 2. leave() zeros stakedBalance but does not permanently ban the vault as a migrate target. 3. An empty vault migrates…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
