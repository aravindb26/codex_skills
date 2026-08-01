# Crypto Training Exploit Pattern Stub: Reentrant `mintMultiple` callback — untrusted external call

Source:
- https://crypto.training/hacks/18201-reentrancy-and-untrusted-contract-call-in-mintmultiple-diffi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2021

Chain:
- Ethereum

Loss / impact summary:
- Reentrant asset callback can mutate vault accounting before mint completion

Tags:
- reentrancy/single-function, dependency/unsafe-external-call

Dedupe:
- id: `18201-reentrancy-and-untrusted-contract-call-in-mintmultiple-diffi`
- fingerprint: `531c117b89da0622093b2d72c2a48c86bc76f2fc89354b4b5b571ce4ed389a5c`

Core exploit idea:
- mintMultiple computes state and then calls every caller-supplied asset. A malicious token's transferFrom callback re-enters mint, proving that the no-guard ordering expo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
