# Crypto Training Exploit Pattern Stub: Base/reward token alias inflates `burnForBase` — reward-accounting theft

Source:
- https://crypto.training/hacks/16984-strategy-contracts-balance-tracking-system-could-facilitate/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2021

Chain:
- Ethereum

Loss / impact summary:
- Burners receive reward funding as if it were base principal

Tags:
- logic/reward-calculation, logic/missing-validation

Dedupe:
- id: `16984-strategy-contracts-balance-tracking-system-could-facilitate`
- fingerprint: `fcf98fe6a369329dc0ccb5d43999dce444bd4527c7b0bc23f0468a24b5fe101e`

Core exploit idea:
- burnForBase pro-rates the entire base-token balance. If rewards use the same token as base, reward funding is counted as principal and a burner receives 150 for 100 stra…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
