# Crypto Training Exploit Pattern Stub: rsETH Safe drain — Router `multicall` treats a self-call as authorized and the enabled module delegatecalls a recipe

Source:
- https://crypto.training/hacks/2026-09-rsethsafemodule/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 2,899.999999999997756821 aEthrsETH pulled from the victim Safe (~2,900 rsETH, reported ~$…

Tags:
- access-control/auth-bypass, auth/caller-check, logic/self-call

Dedupe:
- id: `2026-09-rsethsafemodule`
- fingerprint: `912c4539421f633a84b7b324860b8a554cf333e9140708768f4930c8da15a41e`

Core exploit idea:
- A whale Safe held 53,402.655157601774360853 aEthrsETH and had enabled a custom module, 0xeA18B13d.... That module will act on the Safe when the Router calls it. The Rout…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
