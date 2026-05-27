# Solodit Pattern Stub: [M-01] Incorrect Encoding of Order Hashes

Source:
- https://solodit.cyfrin.io/issues/m-01-incorrect-encoding-of-order-hashes-code4rena-opensea-opensea-seaport-12-contest-git

Imported:
- 2026-05-23

Status:
- distilled

Severity:
- MEDIUM

Protocol:
- OpenSea Seaport 1.2

Source platform / firm:
- Code4rena

Tags:
- seaport, order-hashes, zone-callback, contract-offerer, calldata-encoding, memory-copy

Dedupe:
- id: `6631`
- fingerprint: `28a29e19d713f89b598bb2fc51f329a9b8d9d8bfe6e3fd1f9c225852c69edf20`

Core idea:
- Old Seaport 1.2 `_encodeOrderHashes` copied from `srcLength.next().offset(headAndTailSize)` instead of from `srcLength.next()`. That advanced the source pointer past the array data, so zone `validateOrder` and contract-offerer `ratifyOrder` calldata could receive corrupted `orderHashes`.

Broken invariant:
- Callback calldata should encode the actual fulfilled order hash set. Zones and contract offerers that rely on `orderHashes` should not receive memory from unallocated or unrelated regions.

Where to look in code:
- `ConsiderationEncoder._encodeOrderHashes`
- Zone `validateOrder` encoding
- Contract offerer `ratifyOrder` encoding
- Memory pointer copy helpers

Attack path:
1. Construct restricted or contract-order fulfillment where downstream zone/offerer checks `orderHashes`.
2. Seaport encodes callback calldata.
3. Bad source pointer copies memory after the order hash array.
4. Zone/offerer receives incorrect order hash context and may make a wrong authorization or ratification decision.

False-positive checks:
- Current code should copy from `srcLength.next()` to `dstLength.next()` for `length * 32` bytes.
- Confirm tests cover zone calldata fidelity and contract offerer ratification calldata.
- If the only impact is external zone/offerer reliance, check whether the bug is already public/fixed and whether the target program treats public known issues as out of scope.

PoC shape:
- Zone or contract-offer test that records `keccak256(abi.encodeCall(...))` for expected callback calldata and reverts if received `orderHashes` differs.

Triage notes:
- Public known issue from Code4rena Seaport 1.2. The fix removed the extra `.offset(headAndTailSize)` from the source pointer. For current Seaport 1.6, treat this as duplicate-prone unless a new distinct encoding path corrupts `orderHashes`.
