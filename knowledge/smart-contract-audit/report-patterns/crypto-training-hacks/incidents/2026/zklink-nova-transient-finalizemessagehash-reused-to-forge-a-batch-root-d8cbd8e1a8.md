# Crypto Training Exploit Pattern Stub: zkLink Nova — Transient finalizeMessageHash Reused to Forge a Batch Root

Source:
- https://crypto.training/hacks/2026-10-zklinknovabridge/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Ethereum

Loss / impact summary:
- Reported about $783K across two exploit transactions. This PoC is the first transaction o…

Tags:
- bridge/replay, bridge/missing-validation, logic/incorrect-state-transition

Dedupe:
- id: `2026-10-zklinknovabridge`
- fingerprint: `d8cbd8e1a8aae8173bd112b4b157e355293edaacf810bb10215fcc284db45c9b`

Core exploit idea:
- zkLink Nova finalizes L2-to-L1 withdrawals by Merkle-proving them against l2LogsRootHashes for a batch. Only a gateway-authenticated message may call syncBatchRoot. The…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
