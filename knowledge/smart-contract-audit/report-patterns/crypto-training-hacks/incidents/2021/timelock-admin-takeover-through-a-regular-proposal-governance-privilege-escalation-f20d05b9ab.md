# Crypto Training Exploit Pattern Stub: Timelock.admin takeover through a regular proposal — governance privilege escalation

Source:
- https://crypto.training/hacks/18200-proposals-could-allow-timelockadmin-takeover-trailofbits-ori/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2021

Chain:
- Ethereum

Loss / impact summary:
- Governance administration can be seized by a proposal author

Tags:
- governance/proposal-manipulation, access-control/missing-owner-check

Dedupe:
- id: `18200-proposals-could-allow-timelockadmin-takeover-trailofbits-ori`
- fingerprint: `f20d05b9ab18989c0925e534cf1693cdf11d1ed1d191c3e5d7791178edca403b`

Core exploit idea:
- The audited Governor path lets an ordinary proposal call the Timelock's privileged setPendingAdmin. The reduction records an attacker-controlled pending administrator wh…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
