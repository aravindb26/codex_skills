# Crypto Training Exploit Pattern Stub: Notional V1 escrow — unbacked fCash mint overflows uint128 ladders and settles as cash

Source:
- https://crypto.training/hacks/2026-09-notionalfinance/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- $1.727M — 69,257.372677950923155658 DAI + 1,658,524.864122 USDC (exact) output.txt

Tags:
- arithmetic/overflow, logic/missing-validation, input-validation/missing

Dedupe:
- id: `2026-09-notionalfinance`
- fingerprint: `5b3c98e61f1d86827b8a8324e3c1feaa2a586c635f24986842bd82dc4a069d5f`

Core exploit idea:
- Notional V1 books an ERC-1155 fCash transfer as a minted pair: a CASH_PAYER (debt / short, assetType 2) on from and a CASH_RECEIVER (claim / long, assetType 3) on to — e…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
