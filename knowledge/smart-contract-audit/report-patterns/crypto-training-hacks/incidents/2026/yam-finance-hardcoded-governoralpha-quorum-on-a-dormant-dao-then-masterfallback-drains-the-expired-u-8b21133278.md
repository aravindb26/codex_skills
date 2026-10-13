# Crypto Training Exploit Pattern Stub: Yam Finance — hardcoded GovernorAlpha quorum on a dormant DAO, then `masterFallback` drains the expired UMA farms

Source:
- https://crypto.training/hacks/2026-09-yamfinance/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 48.085375043290366770 WETH and 763.101265318097645247 UMA to the attacker. MAR 23.4991194…

Tags:
- governance/quorum-manipulation, governance/admin-takeover, access-control/live-admin-power-on-dormant-protocol, logic/arbitrary-external-call

Dedupe:
- id: `2026-09-yamfinance`
- fingerprint: `8b2113327857c9b7df996637aaca3fed5fa86bf0a53b45cb4604c319622fc81e`

Core exploit idea:
- 1. Yam's GovernorAlpha is the Compound fork: state() marks a proposal Succeeded when forVotes > againstVotes and forVotes >= quorumVotes(). There is no extra "for" thres…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
