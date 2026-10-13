---
repo_url: https://github.com/zksecurity/zkbugs
repo_ref: main
contracts_dir: dataset/circom/iden3/circomlib/veridise_decoder_accepting_bogus_output_signal
---

# Ground Truth — circomlib Decoder Accepting Bogus Output

Source: https://github.com/zksecurity/zkbugs/tree/main/dataset/circom/iden3/circomlib/veridise_decoder_accepting_bogus_output_signal

The canonical V-D6 (`one-sided-decoder` / `Decoder` not enforcing one-hot) instance from the iden3/circomlib core library. The original template enforces `out[i] * (inp - i) === 0` (i.e. `out[i] = 0 OR inp = i`) but does NOT enforce `sum_i out[i] === 1` and does NOT enforce `out[i] ∈ {0, 1}`. The prover supplies `out = [0, 0, ..., 0]` regardless of `inp`, and a `success` output signal that should reflect "is `inp` in domain" can be set to anything.

## Findings

FINDING | id: H-1 | severity: High | template: Decoder | signal: out | bug_class: one-sided-decoder
description: `Decoder` enforces only the one-sided constraint `out[i] * (inp - i) === 0` for each index — which holds when `out[i] = 0` for every `i` regardless of `inp`. There is no booleanity constraint (`out[i] * (out[i] - 1) === 0`) and no one-hot sum constraint (`sum_i out[i] === 1`), so the prover can produce `out = [0, 0, 0, 0]` (or any field-element vector that satisfies the one-sided product) and an arbitrary `success` flag, breaking every consumer of `Decoder` for one-hot / membership selection. Fix: add both booleanity and sum-to-one constraints, or use `IsEqual(inp, i).out` per slot to derive `out[i]` from a constraint-bound source. Cross-reference: every circomlib consumer (`Multiplexer`-style templates) inherits this bug until either the consumer adds the missing constraints or the library template is fixed.
