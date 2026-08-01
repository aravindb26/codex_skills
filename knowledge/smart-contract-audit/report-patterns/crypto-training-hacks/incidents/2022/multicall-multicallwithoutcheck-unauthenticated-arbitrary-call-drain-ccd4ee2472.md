# Crypto Training Exploit Pattern Stub: Multicall `multicallWithoutCheck()` — Unauthenticated Arbitrary-Call Drain

Source:
- https://crypto.training/hacks/2022-10-MulticallWithoutCheck/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2022

Chain:
- Polygon

Loss / impact summary:
- 619.748460 USDT drained from the Multicall contract (Polygon PoS USDT, 6 decimals)

Tags:
- access-control/missing-auth, dependency/unsafe-external-call

Dedupe:
- id: `2022-10-MulticallWithoutCheck`
- fingerprint: `ccd4ee24728714cb417661ec57db78c5b1a848d1a24467b198feb2ed78e7358d`

Core exploit idea:
- The Multicall contract exposes a public, unauthenticated batching entry point, multicallWithoutCheck(Call[] calls) (contracts_Multicall.sol:34-39), that loops over calle…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
