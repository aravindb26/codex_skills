# Crypto Training Exploit Pattern Stub: Payable delegatecall loop reuses `msg.value` — value-accounting hazard

Source:
- https://crypto.training/hacks/16976-use-of-delegatecall-in-a-payable-function-inside-a-loop-trai/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2021

Chain:
- Ethereum

Loss / impact summary:
- Future value-sensitive logic can count one payment multiple times

Tags:
- dependency/unsafe-external-call, logic/state-update

Dedupe:
- id: `16976-use-of-delegatecall-in-a-payable-function-inside-a-loop-trai`
- fingerprint: `33dbb8295cebf98a6ce83b8d8ad93d499ebd9dca0d1e075d600efc8832d3bebc`

Core exploit idea:
- Every delegatecall in a payable batch inherits the original msg.value. The reduction calls a hypothetical value-sensitive credit() twice and records two ether of credit…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
