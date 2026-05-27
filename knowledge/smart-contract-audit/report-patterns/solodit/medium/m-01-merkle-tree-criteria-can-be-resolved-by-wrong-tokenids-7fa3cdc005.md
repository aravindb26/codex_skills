# Solodit Pattern Stub: [M-01] Merkle Tree criteria can be resolved by wrong tokenIDs

Source:
- https://solodit.cyfrin.io/issues/m-01-merkle-tree-criteria-can-be-resolved-by-wrong-tokenids-code4rena-opensea-opensea-seaport-contest-git
- https://code4rena.com/reports/2022-05-opensea-seaport

Imported:
- 2026-05-23

Status:
- distilled

Severity:
- MEDIUM

Protocol:
- OpenSea Seaport

Source platform / firm:
- Code4rena

Tags:
- seaport, criteria, merkle-proof, nft-token-id

Dedupe:
- id: `2623`
- fingerprint: `7fa3cdc005f9a40a8005b630d3434d59a5966fe605f076dc8fe937edae0336b0`

Core idea:
- In old Seaport criteria resolution, the supplied token id was used directly as the initial Merkle proof value. This allowed an intermediate node hash to be submitted as a token id with an empty or short proof, so a fulfiller could provide a token id that was not an intended leaf of the maker's criteria set.

Broken invariant:
- Criteria fulfillment must prove membership of the concrete token id as a leaf, not allow proof-internal nodes to masquerade as token ids.

Where to look in code:
- Merkle proof verification for criteria-based ERC721/ERC1155 items.
- Whether the concrete identifier is hashed as a leaf before proof folding.
- Whether wildcard criteria roots are treated separately from nonzero criteria roots.

Attack path:
1. Maker signs criteria for token ids such as 1 or 2.
2. Attacker obtains/mints an NFT whose token id equals an intermediate Merkle node/root.
3. Attacker submits that intermediate value as the identifier with a proof that verifies under the vulnerable algorithm.
4. Maker receives a token id not actually included as a leaf in the intended criteria set.

False-positive checks:
- Check that the leaf is hashed first, e.g. `computedHash = keccak256(abi.encodePacked(identifier))`.
- Check nonzero criteria roots require a valid proof.
- Check collection-wide wildcard roots reject non-empty proofs and are explicitly intended.

PoC shape:
- Criteria order accepting `{1,2}` where attacker fulfills with token id equal to `hash(1,2)` using empty proof.

Triage notes:
- Usually medium because it depends on token ids being arbitrary enough to mint/procure the intermediate hash. For current Seaport versions, the leaf-hashing fix should kill the exact root cause.
