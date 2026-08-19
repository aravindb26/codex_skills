# Crypto Training Exploit Pattern Stub: DIA Spectra — fee dropped during the interchain oracle callback (permanent DoS)

Source:
- https://crypto.training/hacks/55410-issue-with-fee-payment-during-interchain-callback-mixbytes-n/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- cross-chain/fee-accounting, dos/liveness, logic/missing-value-forward

Dedupe:
- id: `55410-issue-with-fee-payment-during-interchain-callback-mixbytes-n`
- fingerprint: `fd59dee14684b1e1b408af70397f5dfb06f0ba0aaa8b7176da140a26efb59c99`

Core exploit idea:
- OracleRequestRecipient.handle() is the destination-chain entrypoint the Hyperlane relayer calls to deliver an inbound oracle request. To answer it, handle() dispatches a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
