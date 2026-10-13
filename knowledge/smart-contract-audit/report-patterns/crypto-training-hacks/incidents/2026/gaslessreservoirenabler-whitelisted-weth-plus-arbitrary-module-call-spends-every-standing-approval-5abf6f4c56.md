# Crypto Training Exploit Pattern Stub: GaslessReservoirEnabler — whitelisted WETH plus arbitrary `module.call` spends every standing approval

Source:
- https://crypto.training/hacks/2026-09-gaslessreservoirenabler/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Polygon

Loss / impact summary:
- This tx: 8.7199 WETH from 466 victims (~$23.8K at the fork-block price; the ~$23K alert).…

Tags:
- access-control/missing-auth, dependency/unsafe-external-call, input-validation/missing

Dedupe:
- id: `2026-09-gaslessreservoirenabler`
- fingerprint: `5abf6f4c568cfa04c45cabda98a0e80fb120e91f004793442359c040eddd360c`

Core exploit idea:
- GaslessReservoirEnabler is a Polygon meta-transaction helper. The intended path is EIP-712: a user signs, a relayer calls executeMetaTransaction, and _msgSender() is the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
