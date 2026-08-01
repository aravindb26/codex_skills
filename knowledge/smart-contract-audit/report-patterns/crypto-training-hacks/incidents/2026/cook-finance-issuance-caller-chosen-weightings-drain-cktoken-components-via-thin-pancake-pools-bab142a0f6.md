# Crypto Training Exploit Pattern Stub: Cook Finance Issuance — Caller-Chosen Weightings Drain CKToken Components via Thin Pancake Pools

Source:
- https://crypto.training/hacks/2026-06-CookFinanceIssuance/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~2.82 BNB net profit to the attacker (2816924852223933205 wei), extracted from a Cook Fin…

Tags:
- oracle/price-manipulation, logic/incorrect-state-transition, defi/flash-loan-attack

Dedupe:
- id: `2026-06-CookFinanceIssuance`
- fingerprint: `bab142a0f6a967bc7bf05e1624de24755ec4e878d6d01a3060068ab66e2be4fc`

Core exploit idea:
- 1. Cook's IssuanceModuleV2.issueWithSingleToken2 (IssuanceModuleV2.sol:3124-3153) lets anyone mint a CKToken by supplying a single component token and a caller-chosen _w…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
