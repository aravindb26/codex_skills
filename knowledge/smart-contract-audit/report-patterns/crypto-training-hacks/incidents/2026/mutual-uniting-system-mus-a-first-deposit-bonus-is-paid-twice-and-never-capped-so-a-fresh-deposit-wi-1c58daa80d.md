# Crypto Training Exploit Pattern Stub: Mutual Uniting System (MUS) — a first-deposit bonus is paid twice and never capped, so a fresh deposit-withdraw returns more ETH than it put in

Source:
- https://crypto.training/hacks/2026-09-mus/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 0.400167773791578324 ETH net over-extraction for one fresh deposit-withdraw cycle — repro…

Tags:
- logic/reward-calculation, logic/missing-check, access-control/missing-auth

Dedupe:
- id: `2026-09-mus`
- fingerprint: `1c58daa80d93ff9376c438078f328869f306b49d63a2051bfaa3589a14e01593`

Core exploit idea:
- 1. MUS is a "pack"/round Ponzi-matrix contract. deposit{value: D}() and withdraw(uint256,uint256,bool) are permissionless — no owner/caller check anywhere. 2. For a fres…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
