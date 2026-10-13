---
repo_url: https://github.com/zksecurity/zkbugs
repo_ref: main
contracts_dir: dataset/circom/selfxyz/self/zksecurity_second_pre_image_attacks_on_packbytesandposeidon_may_be_used_to_register_arbitrary_passports_and_dsc_certificates
---

# Ground Truth — selfxyz/Self PackBytesAndPoseidon Second-Preimage

Source: https://github.com/zksecurity/zkbugs/tree/main/dataset/circom/selfxyz/self/zksecurity_second_pre_image_attacks_on_packbytesandposeidon_may_be_used_to_register_arbitrary_passports_and_dsc_certificates

The canonical V-B5 (`packbytes-input-byte-range-missing`) instance: `PackBytes(k)` packs an input byte array into a single field element by computing `sum_i bytes[i] * 256^i`, but does NOT enforce `bytes[i] < 256` for each index. Combined with a Poseidon hash downstream, this enables second-preimage collisions on certificate / passport commitments.

## Findings

FINDING | id: H-1 | severity: High | template: PackBytesAndPoseidon | signal: bytes[i] | bug_class: packbytes-input-byte-range-missing
description: `PackBytes` consumes its input array as raw field elements without `Num2Bits(8)` on each entry. A malicious prover supplies one byte equal to 256 (or any value with a 9th bit set), which packs to the same field element as a different byte sequence with carry propagated into the next slot. Two distinct passport / DSC byte sequences therefore hash to the same Poseidon commitment, allowing the attacker to register an arbitrary passport under a legitimate-looking certificate root. Fix: insert `Num2Bits(8)(bytes[i])` for every input byte before passing to `PackBytes`.
