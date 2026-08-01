# Crypto Training Exploit Pattern Stub: Decent — Anyone can update the Router address in `DcntEth`

Source:
- https://crypto.training/hacks/30559-h-01-anyone-can-update-the-address-of-the-router-in-the-dcnt/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-caller-check

Dedupe:
- id: `30559-h-01-anyone-can-update-the-address-of-the-router-in-the-dcnt`
- fingerprint: `d8ae64b56e4ebab274e570544023ad472c7814f309a9176075dfb3cfe5d5148d`

Core exploit idea:
- 1. DcntEth gates mint/burn with onlyRouter, but setRouter is public and unrestricted. 2. Anyone can point router at themselves, mint arbitrary DcntEth, and call DecentEt…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
