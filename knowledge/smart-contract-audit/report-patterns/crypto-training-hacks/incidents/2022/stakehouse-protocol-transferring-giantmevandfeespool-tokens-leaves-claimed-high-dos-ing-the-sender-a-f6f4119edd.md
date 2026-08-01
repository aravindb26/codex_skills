# Crypto Training Exploit Pattern Stub: Stakehouse Protocol — transferring GiantMevAndFeesPool tokens leaves claimed[] high, DoS-ing the sender and orphaning future rewards

Source:
- https://crypto.training/hacks/43034-h-12-sender-transferring-giantmevandfeespool-tokens-can-afte/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, logic/dos-resistance

Dedupe:
- id: `43034-h-12-sender-transferring-giantmevandfeespool-tokens-can-afte`
- fingerprint: `f6f4119eddcb0d86a20dc2973d613a43dba58cf9e8f7569ee1c4531327d245a0`

Core exploit idea:
- 1. claimed[user][token] records how much a user has already been paid for their LP. 2. On GiantLP transfer, rewards are settled for the sender, balances move, then after…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
