# Crypto Training Exploit Pattern Stub: EigenLayer — Beacon chain withdrawals at lastWithdrawalTimestamp are lost

Source:
- https://crypto.training/hacks/40684-beacon-chain-withdrawals-that-occur-at-lastwithdrawaltimesta/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `40684-beacon-chain-withdrawals-that-occur-at-lastwithdrawaltimesta`
- fingerprint: `6ea15ee1913c131b1f00812d080ce4e1ed4c9b74f3b5eb3acf57a2a124d1aced`

Core exploit idea:
- 1. activateRestaking sets mostRecentWithdrawalTimestamp = block.timestamp and sweeps pod ETH. 2. Beacon-chain withdrawals for that timestamp execute after user txs (EIP-…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
