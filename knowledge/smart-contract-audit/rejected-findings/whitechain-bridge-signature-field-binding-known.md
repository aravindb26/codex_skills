# Known Issue: Whitechain Bridge Signature Field Binding

Program:
- Whitechain Bridge HackenProof / official `whitechain-labs/bridge-contracts` repository

Candidate:
- `Bridge._validateECDSA` signs caller, recipient, target token, amount, gas, chain IDs, deadline, and salt, but omits `mapId` and the origin token. Two source mappings with the same target token and chain pair can therefore accept one signed request for the other source asset.

Why it looked valid:
- A local PoC reproduced source-token substitution after trusted configuration created two same-target mappings. The substituted source token was transferred into Bridge custody under the original digest.

Why it was rejected:
- known issue

Exact known-issue evidence:
- Official issue: `https://github.com/whitechain-labs/bridge-contracts/issues/2`
- Created 2026-01-10 and closed as acknowledged 2026-05-14.
- The issue body, affected function, omitted fields, same-target mapping setup, PoC shape, and destination-liquidity impact match exactly. The maintainer states the released design is one origin token per target per chain pair and plans to bind `mapId` when multi-origin support is added.

Root lesson:
- A missing signed route discriminator is only exploitable when an alternate route with the same signed fields is reachable. Check exact same-chain-pair topology and role needed to create it, then check public repository issues before treating a passing collision PoC as new.

Future filter:
- Distinguish different origin chain IDs because they are signed and prevent this exact collision.
- Treat a collision requiring trusted mapping administration as configuration risk unless the program explicitly includes that role.
- Re-check issue/prior-report sources for the exact omitted field, mutated mapping, broken invariant, attacker setup, and impact; thematic signature-replay similarity is insufficient.

Related files or reports:
- `/home/dinesh/hackenproof/whitechain-bridge-audit/candidates/signature-field-binding.md`
- `/home/dinesh/hackenproof/whitechain-bridge-audit/ether/test/audit/BridgeCapacityIndependentPoC.ts`
