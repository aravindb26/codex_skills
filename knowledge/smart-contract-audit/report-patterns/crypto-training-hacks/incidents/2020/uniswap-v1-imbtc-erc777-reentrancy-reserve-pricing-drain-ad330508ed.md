# Crypto Training Exploit Pattern Stub: Uniswap V1 × imBTC (ERC777) — Reentrancy Reserve-Pricing Drain

Source:
- https://crypto.training/hacks/2020-04-uniswap-erc777/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2020

Chain:
- Ethereum

Loss / impact summary:
- +0.0837168576630010 ETH profit from 1 ETH of working capital — the live April-2020 campai…

Tags:
- unknown

Dedupe:
- id: `2020-04-uniswap-erc777`
- fingerprint: `ad330508ed1076a6ad1fe80e49031ed1ce8103c6df9aaf90e7ed070b23c49e98`

Core exploit idea:
- The Uniswap V1 exchange prices a token→ETH sell by reading the pool's current token balance (self.token.balanceOf(self)) as the input reserve, paying out ETH, and only a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
