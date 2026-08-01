# Crypto Training Exploit Pattern Stub: MISO / SushiSwap Dutch Auction — `batch()` `delegatecall` Reuses `msg.value`

Source:
- https://crypto.training/hacks/2021-09-Sushimiso/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2021

Chain:
- Ethereum

Loss / impact summary:
- 400 ETH drained from the live DutchAuction at fork block 13,038,771 (100 ETH committed →…

Tags:
- logic/incorrect-order-of-operations, dependency/unsafe-external-call

Dedupe:
- id: `2021-09-Sushimiso`
- fingerprint: `f120410e3c74cb097d4e8040058f7e9235ec24503cb4eefbef6539ed651aac49`

Core exploit idea:
- DutchAuction inherits BoringBatchable, which exposes a public, payable batch(bytes[] calls, bool revertOnFail) that executes each supplied calldata via address(this).del…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
