# Crypto Training Exploit Pattern Stub: DAOstack Genesis Alpha — permissionless `newOrganization` mints reputation and drains the avatar

Source:
- https://crypto.training/hacks/2026-09-daostack/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 4.025 ETH, the avatar's entire treasury. Attacker balance log goes from 0 to 4.0255770215…

Tags:
- access-control/missing-auth, governance/proposal-manipulation, logic/missing-validation

Dedupe:
- id: `2026-09-daostack`
- fingerprint: `021ca29611fc818bb115986532e9abeed9b589684e3c9c287cfa113cc30c6428`

Core exploit idea:
- Genesis Alpha is a DAOstack DAO. Its avatar (0x7b11…6DB0) holds the ETH treasury. Its Reputation token (0x6256…5BF9) is the voting weight. Both are owned by one shared U…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
