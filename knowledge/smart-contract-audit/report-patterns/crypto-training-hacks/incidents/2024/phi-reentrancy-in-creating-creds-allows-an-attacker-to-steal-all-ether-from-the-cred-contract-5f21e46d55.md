# Crypto Training Exploit Pattern Stub: Phi — Reentrancy in creating Creds allows an attacker to steal all Ether from the Cred contract

Source:
- https://crypto.training/hacks/43397-h-06-reentrancy-in-creating-creds-allows-an-attacker-to-stea/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- reentrancy/single-function

Dedupe:
- id: `43397-h-06-reentrancy-in-creating-creds-allows-an-attacker-to-stea`
- fingerprint: `5f21e46d55b46363fd9d4074f24fc0a2fb8c837e9036a25fee655587610d0bc7`

Core exploit idea:
- 1. createCred writes creds[credIdCounter], then buyShareCred (auto-buy 1 share). 2. buyShareCred refunds excess ETH via an external call before credIdCounter is incremen…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
