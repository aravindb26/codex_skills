# Crypto Training Exploit Pattern Stub: Victim automation `execute()` missing auth drains yvWETH via Yearn withdrawal path

Source:
- https://crypto.training/hacks/2026-04-YearnStETHAccumulator/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- Ethereum

Loss / impact summary:
- 429.210570004163139903 ETH (exact internal transfer / PoC profit)

Tags:
- access-control/missing-modifier, logic/missing-check, dependency/approval

Dedupe:
- id: `2026-04-YearnStETHAccumulator`
- fingerprint: `fb8a6aeeaf428ab908a248e85a20c43714788ea6f2a94366cbb8e36521343425`

Core exploit idea:
- 1. Victim EOA holds ~384.667 yvWETH and grants max allowance to a personal automation at 0x143A…181A. 2. Automation exposes execute((uint8,bytes)[]) (selector 0x49650044…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
