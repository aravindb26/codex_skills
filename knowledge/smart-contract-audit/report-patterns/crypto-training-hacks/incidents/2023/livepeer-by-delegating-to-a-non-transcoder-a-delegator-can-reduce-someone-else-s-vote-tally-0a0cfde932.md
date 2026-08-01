# Crypto Training Exploit Pattern Stub: Livepeer — By delegating to a non-transcoder, a delegator can reduce someone else's vote tally

Source:
- https://crypto.training/hacks/27048-h-02-by-delegating-to-a-non-transcoder-a-delegator-can-reduc/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `27048-h-02-by-delegating-to-a-non-transcoder-a-delegator-can-reduc`
- fingerprint: `0a0cfde9328bee9c634d21b256be5a38411758ca23e23c691bef2185639efcfa`

Core exploit idea:
- 1. Non-transcoder Alice votes For with 100; Carol For 5000 → For=5100.\n2. Bob delegates 1000 to Alice, votes Against.\n3. Override subtracts 1000 from For without Alice…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
