# Crypto Training Exploit Pattern Stub: Tapioca DAO — mintBBLendXChainSGL compose data.user not bound — force-lend victim

Source:
- https://crypto.training/hacks/32312-h-01-magnetarmintxchainmodulesolmintbblendxchainsgl-can-be-u/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `32312-h-01-magnetarmintxchainmodulesolmintbblendxchainsgl-can-be-u`
- fingerprint: `b1f116804044879c97b885d589c0efb00a5fe4d1014f1d69eb11ed78b52586f4`

Core exploit idea:
- mintBBLendXChainSGL compose data.user not bound — force-lend victim. Harm demonstrated: Whitelisted USDO compose forces lend of victim tokens into Magnetar.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
