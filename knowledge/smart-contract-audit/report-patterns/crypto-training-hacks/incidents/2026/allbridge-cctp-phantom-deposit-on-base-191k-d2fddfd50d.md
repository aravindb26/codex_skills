# Crypto Training Exploit Pattern Stub: Allbridge CCTP — Phantom Deposit on Base (~$191K)

Source:
- https://crypto.training/hacks/2026-08-allbridgecctpphantomdeposit/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Base

Loss / impact summary:
- ~$191,156 USDC (router emptied). Attacker net ~189,751.55 USDC after 10 bp fee + Aave pre…

Tags:
- bridge/message-validation, bridge/false-deposit, defi/flash-loan

Dedupe:
- id: `2026-08-allbridgecctpphantomdeposit`
- fingerprint: `d2fddfd50de801a59165d9a8b4f064ce8dbee7d09082c2e736a72a0f2229614a`

Core exploit idea:
- Allbridge’s new CCTP router on Base treated a Circle-attested generic MessageTransmitterV2.sendMessage as a real USDC deposit. The attacker authored a burn-shaped body d…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
