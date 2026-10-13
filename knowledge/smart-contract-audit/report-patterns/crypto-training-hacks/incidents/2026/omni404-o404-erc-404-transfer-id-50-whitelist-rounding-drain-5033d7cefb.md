# Crypto Training Exploit Pattern Stub: OMNI404 (O404) — ERC-404 `transfer(id≤50)` + whitelist rounding drain

Source:
- https://crypto.training/hacks/2026-09-omni404erc404rounding/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- ~2.4–3.02 WETH. Main tx +2.427 WETH; three drain() follow-ups in the same block. Teaching…

Tags:
- input-validation/wrong-type, arithmetic/rounding, logic/incorrect-state-transition, defi/fee-manipulation

Dedupe:
- id: `2026-09-omni404erc404rounding`
- fingerprint: `5033d7cefbf66b210fc37ab1640a15e1675af55c2a7adbcdfbd972bfad9d6c45`

Core exploit idea:
- O404 is an ERC-404: one contract, ERC-20 balances in 1e18 units and up to 50 ERC-721 ids. transfer(to, valueOrId) guesses intent from the magnitude of the second argumen…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
