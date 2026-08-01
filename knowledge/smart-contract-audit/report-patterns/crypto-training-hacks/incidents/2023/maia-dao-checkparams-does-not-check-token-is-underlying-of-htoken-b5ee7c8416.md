# Crypto Training Exploit Pattern Stub: Maia DAO — checkParams does not check token is underlying of hToken

Source:
- https://crypto.training/hacks/26043-h-09-rootbridgeagent-checkparamslibcheckparams-does-not-chec/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `26043-h-09-rootbridgeagent-checkparamslibcheckparams-does-not-chec`
- fingerprint: `b5ee7c8416888a3c022450d564a55b4be3e15fee8f813308e3def6b9dd03f069`

Core exploit idea:
- 1. checkParams requires underlying exists and hToken is local, not that they pair.\n2. Attacker deposits USDC with hToken=hEther.\n3. Root mints 10 global hEther for 10…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
