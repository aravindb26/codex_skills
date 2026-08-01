# Crypto Training Exploit Pattern Stub: Rubicon — Some offers can't be cancelled

Source:
- https://crypto.training/hacks/48949-h-10-some-offers-cant-be-cancelled-code4rena-rubicon-rubicon/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `48949-h-10-some-offers-cant-be-cancelled-code4rena-rubicon-rubicon`
- fingerprint: `c4100d28a26b68f2e58b833ec2398e035ade8839ac07c3c37b0d512ba3aef4d9`

Core exploit idea:
- 1. SimpleMarket.offer(pay, payGem, buy, buyGem, owner, recipient) creates an offer without inserting it into the sorted _rank list or the unsorted _near list. 2. Rubicon…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
