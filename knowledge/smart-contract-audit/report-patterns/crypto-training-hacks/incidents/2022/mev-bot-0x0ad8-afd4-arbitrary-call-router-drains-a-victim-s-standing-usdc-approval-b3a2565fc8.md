# Crypto Training Exploit Pattern Stub: MEV Bot `0x0AD8…afd4` — Arbitrary-Call Router Drains a Victim's Standing USDC Approval

Source:
- https://crypto.training/hacks/2022-11-MEV_0ad8/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Ethereum

Loss / impact summary:
- 91,638.11 USDC (~$91.6K) — the victim's entire USDC balance

Tags:
- access-control/missing-auth, dependency/unsafe-external-call

Dedupe:
- id: `2022-11-MEV_0ad8`
- fingerprint: `b3a2565fc8a9a75b99be8d0a137edd3d797bfd1fb45050178ed1e4caa5e9920d`

Core exploit idea:
- The contract at 0x0AD8…afd4 is a generic "MEV bot / swap router" that exposes a function — selector 0x090f88ca — which takes a caller-supplied bytes blob and executes it…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
