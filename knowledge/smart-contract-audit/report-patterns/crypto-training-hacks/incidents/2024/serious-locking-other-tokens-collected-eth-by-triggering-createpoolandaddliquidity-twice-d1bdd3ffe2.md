# Crypto Training Exploit Pattern Stub: Serious — locking other tokens' collected ETH by triggering `createPoolAndAddLiquidity` twice

Source:
- https://crypto.training/hacks/36317-c-01-locking-collected-eth-by-triggering-createpoolandaddliq/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-state-guard, accounting/shared-pot-drain, dos/fund-lock

Dedupe:
- id: `36317-c-01-locking-collected-eth-by-triggering-createpoolandaddliq`
- fingerprint: `d1bdd3ffe25dc62afb8411bd057ecdc822257caa14bc65baf494a62b10706e18`

Core exploit idea:
- 1. Every token's buyers pay ETH into the SAME SeriousMarketProtocol contract balance while their token is being funded. 2. Once a token is fully funded, anyone can call…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
