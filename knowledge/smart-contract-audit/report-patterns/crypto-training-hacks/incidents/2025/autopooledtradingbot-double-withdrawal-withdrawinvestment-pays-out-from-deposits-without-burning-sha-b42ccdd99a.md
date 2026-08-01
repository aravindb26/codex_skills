# Crypto Training Exploit Pattern Stub: AutoPooledTradingBot double-withdrawal — withdrawInvestment pays out from deposits without burning shares, so emergencyWithdrawAll pays the same position twice

Source:
- https://crypto.training/hacks/2025-08-AutoPooledTradingBot/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Ethereum

Loss / impact summary:
- 0.15198 ETH on-chain (PoC reproduces 0.152158266800401203 ETH net profit after flash-swap…

Tags:
- logic/incorrect-state-transition, logic/state-update, logic/missing-validation

Dedupe:
- id: `2025-08-AutoPooledTradingBot`
- fingerprint: `b42ccdd99af82f812f2a02ff87c6bc0fa0a48034d7e002eedaa86539d631224c`

Core exploit idea:
- AutoPooledTradingBot is an ETH "auto-trading pool" that issues share tokens on deposit() and lets users exit through one of two paths: withdrawInvestment() (an "earnings…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
