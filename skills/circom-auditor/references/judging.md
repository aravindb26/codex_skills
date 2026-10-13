# Finding Validation

Every finding passes four sequential gates. Fail any gate → **rejected** or **demoted** to lead. Later gates are not evaluated for failed findings.

The threat model is one of:

1. **Soundness break**: a malicious prover can craft a witness/inputs that satisfy the R1CS but violate the protocol's intended semantics, AND a verifier accepts the resulting proof.
2. **Completeness break**: an honest prover with valid inputs cannot produce a satisfying witness (circuit bricks legitimate use).
3. **Privacy / zero-knowledge leak**: the verifier (or proof bytes) reveals a meaningful function of private inputs that the protocol claims to hide.

You are not defending the circuit. The job of these gates is to verify the attacker's claimed witness actually satisfies the constraint system end-to-end — a finding fails ONLY when a specific constraint on the witness path provably pins the value the attacker needs free. "I can imagine an honest prover wouldn't do this" is not a refutation; "this exact `===` forces the signal, here is the line" is.

## Gate 1 — Attack execution

Trace the attacker's claimed witness from the inputs they control to the accepted bad proof. Read every constraint, range check, tag, and guard that sits on that path. A finding is refuted only if you trace EVERY constraint on the path and one of them provably pins the value the attack needs free — not because the bad witness "seems unlikely."

- Concrete refutation: a specific line on the witness path pins the value — explicit `===`, `<==`, `Num2Bits_strict`, `IsZero(b).out === 0`, `BigLessThan(...).out === 1`, an upstream tag template that enforces the invariant, or a downstream consumer that re-checks the value. Quote the exact line and trace how it blocks the claimed step → **REJECTED** (or **DEMOTE** if a related code smell remains).
- Speculative refutation ("the prover wouldn't do that", "in practice the input is small", "the witness generator only emits canonical values", "no honest prover would pick `p - k`") → **clears**, continue. Witness generators do not constrain the prover; only the R1CS does.

## Gate 2 — Reachability

Prove the bad witness/input space exists in normal usage.

- Structurally impossible (every valid call-site supplies bounded values that an upstream constraint already enforces) → **REJECTED**.
- Achievable through any of:
  - any malicious prover supplying the witness directly,
  - honest input near the field boundary (`p - k` for small `k`, sentinel values, zero, max),
  - boundary or edge cases the protocol implicitly assumes away,
  → **clears**, continue.

## Gate 3 — Trigger

Prove an unprivileged prover can produce the bad witness and submit a proof.

- Only the trusted setup or a designated prover can trigger → **DEMOTE**.
- Any prover with access to valid public inputs can trigger → **clears**, continue.

**Trusted-party-action findings — demote unless an unprivileged amplifier is named.** This applies ONLY to harm that requires the trusted setup or a designated prover acting against documented intent, NOT to ordinary malicious-prover witnesses (those are the default threat model and clear above). If the harm needs the trusted party to misbehave, **DEMOTE** unless the finding names a concrete path by which an *unprivileged* prover reaches the same harm:

- **toxic-waste leak** — the setup's secret leaks (or is assumed honest but unverified), after which any prover forges proofs.
- **designated-prover gap via public entry** — a constraint the designated prover "shouldn't" violate is reachable through a public input or entry-point template that any prover can drive.
- **setup-assumed invariant, prover-checkable** — the setup assumes a tag/range/canonicalization invariant that the circuit never enforces, so any prover can supply a witness that violates it.

No unprivileged amplifier → **DEMOTE** (lead, not finding). Amplifier named → judge it on that unprivileged path.

## Gate 4 — Impact

Prove material harm.

- **Soundness break with external impact**: verifier accepts something it shouldn't (double-spend, signature forgery, unauthorized membership, range-proof bypass, replay, cross-context proof reuse): **CONFIRMED**.
- **Completeness break that bricks honest provers permanently** (bad witness derivation, divergent constraint vs. witness logic, infinite loop in witness generator): **CONFIRMED**.
- **Privacy leak** that reveals a meaningful function of private inputs (lower bound, range, per-row equality, intent linkage): **CONFIRMED**.

## Confidence

Start at **100**, deduct:

- partial witness path (steps not fully traced) **-20**
- bounded non-compounding impact (small leak, single-shot, self-contained) **-15**
- requires specific (but achievable) field-boundary state **-10**
- completeness-only impact (no soundness or privacy break) **-10**

Confidence ≥ 80 gets description + fix. Below 80 gets description only.

## Safe patterns (do not flag)

- `Num2Bits_strict()` / `Bits2Num_strict()` — the built-in alias check rejects `in ≥ p`.
- `<==` (not `<--`) for any quadratic relation — emits a constraint that pins the signal.
- The canonical inverse pattern: `out <-- 1/x; out * x === 1` paired with `IsZero(x).out === 0` upstream.
- `s * (s - 1) === 0` immediately before any `Mux1` / `MultiMux*` selector input.
- `BigLessThan(n, k)(r, modulus).out === 1` after `BigMod` / `BigMul` outputs.
- `IsEqual(a, b).out === 0` before any `(b - a)`-based EC constraint (e.g. `EllipticCurveAddUnequal`).
- Tag templates whose body explicitly enforces the named invariant (e.g. `Uint8Tag` body contains `Num2Bits(8)(in)`).
- `Poseidon(.., intentHash)` binding for nullifier-burning / spend proofs (binds proof to spender's intent).
- `EllipticCurveAdd` (the dispatch wrapper) when inputs may be equal (vs. `EllipticCurveAddUnequal` which asserts inequality).
- `safe*` / `*_strict` / `Force*EqualIfEnabled` family of templates whose name signals the runtime check.

## Lead promotion

Before finalizing leads, promote where warranted:

- **Cross-template echo.** Same root cause confirmed as FINDING in one template → promote in every template using the same primitive (e.g. every consumer of buggy circomlib `MontgomeryAdd`, `Decoder`, `BinSum` propagates the same bug).
- **Multi-agent convergence.** 2+ agents flagged the same area, lead was demoted (not rejected) → promote to FINDING at confidence 75.
- **Partial-path completion.** Only weakness is incomplete witness construction but the path is clearly reachable and unguarded → promote to FINDING at confidence 75, description only.
- **Composite chain.** Two leads chain into a worse impact than either alone (e.g. missing range-check + selector-mux collapse → always-disabled enforcement) → promote both to FINDING at confidence = min(A, B), with `Chain: [A] + [B]` annotation.

## Leads

High-signal trails for manual investigation. No confidence score, no fix — title, code smells, and what remains unverified.

## Do Not Report

- Style: snake_case vs camelCase, file layout, missing comments.
- Compile-time `assert(...)` used in its legitimate role (parameter sanity checks the user understands won't survive into R1CS).
- Generic "this could be optimized" / "circuit size could be smaller" — not a finding.
- Centralization / admin-by-design without a concrete circuit-level exploit path.