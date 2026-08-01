# Crypto Training Exploit Pattern Stub: Unverified Base airdrop-claim contract drained via constructor-time claim spam — per-claimant eligibility keyed on `msg.sender` with no nonce/code/allow-list guard

Source:
- https://crypto.training/hacks/2025-05-unverified_91a1/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Base

Loss / impact summary:
- 0.208333333333333384 ETH (≈ 551.22 USD at the time) — full victim balance drained

Tags:
- access-control/broken-logic, logic/missing-check, dos/griefing

Dedupe:
- id: `2025-05-unverified_91a1`
- fingerprint: `ba5f20266f41d4ea586bfb421a08e81bf6a5f5f454371633fa361ab71712721b`

Core exploit idea:
- The victim at 0x91a1…193D is an unverified Base contract exposing a public claim() that sends the caller a fixed per-claim chunk of ETH and records that the caller has c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
