# Crypto Training Exploit Pattern Stub: sAVAX Rebalancer arbitrary-call drains victim credit delegation — permissionless `target`/`data` execution from a delegated Aave borrower

Source:
- https://crypto.training/hacks/2026-04-AaveRebalancerCreditDelegation/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- Avalanche

Loss / impact summary:
- 6,999.99 WAVAX (~7,000 AVAX) [output.txt:1565]

Tags:
- access-control/missing-auth, logic/missing-validation, dependency/unsafe-external-call

Dedupe:
- id: `2026-04-AaveRebalancerCreditDelegation`
- fingerprint: `b1e80a051deda67bce2c966704da2a9cf9e8758a9eaaaa9ec3cb324b65dabb7d`

Core exploit idea:
- The "sAVAX Rebalancer" (0x7A7b…a8C9) is a contract that helps users grow their leveraged Aave V3 sAVAX position. To do so it borrows WAVAX from Aave on behalf of the use…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
