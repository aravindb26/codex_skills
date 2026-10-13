# Crypto Training Exploit Pattern Stub: Reflexer GEB — unauthenticated `GebProxyActions.quitSystem` drains library-owned SAFEs

Source:
- https://crypto.training/hacks/2026-08-reflexergeb/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- 5.943599831844387377 ETH (~$14K) leftover ETH-A collateral output.txt

Tags:
- access-control/missing-auth, access-control/missing-owner-check, logic/missing-check

Dedupe:
- id: `2026-08-reflexergeb`
- fingerprint: `273ce7e91b81ca2bce3fef3eb74bf47267facbcdc3a14353631f1c8af6b3d097`

Core exploit idea:
- GebProxyActions is a shared, stateless "proxy actions" library. It is meant to be DELEGATECALLed through each user's DSProxy so that, from GebSafeManager's point of view…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
