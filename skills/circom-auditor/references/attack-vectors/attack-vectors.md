# Circom Attack Vectors — Index

A curated library of 48 soundness, completeness, and privacy vectors for Circom circuits. Each vector is grounded in at least one real audit finding from the zkbugs dataset or a published audit report. Per-vector format: **D** description / **FP** false-positive guard / **Source** real-bug citation.

The vectors are organized by **code shape** (the kind of Circom construct you grep for), not by abstract bug class. To keep each scanning agent's context focused, the catalog is split across **six slice files** — a vector-scan agent reads only its slice, never the whole catalog.

## Categories

- **A. Signal flow** — `<--` vs `<==` / `===` mismatches, unassigned outputs, decompositions without recomposition.
- **B. Range checks** — comparators, packers, bit-decompositions whose operands aren't bounded.
- **C. Arithmetic / field** — division-by-zero, EC degeneracies, modular reduction not enforced.
- **D. Selector / mux** — conditional gate collapse, mux selectors not boolean, assert-vs-constraint.
- **E. Accumulator** — wrong init seeds, wrong-side keying.
- **G. Regex / encoding** — sentinel-byte abuse, regex overlap, base64 mismatch.
- **H. Protocol binding** — replay, unbound public input, sentinel leaf, low-entropy nullifier.
- **L. Language-level footguns** — Circom-language pitfalls that don't show up in real audits often but bite developers at write-time.

## Slice manifest

| Slice file | Categories | Vectors | Count |
| ---------- | ---------- | ------- | ----- |
| `attack-vectors/signal-field.md`           | A + C | V-A1–A5, V-C1, V-C3–C6 | 10 |
| `attack-vectors/range.md`                   | B     | V-B1–B7                | 7  |
| `attack-vectors/selector-accumulator.md`    | D + E | V-D1–D7, V-E1–E2        | 9  |
| `attack-vectors/binding-1.md`               | H     | V-H1–H8                | 8  |
| `attack-vectors/binding-2.md`               | H     | V-H9–H16               | 8  |
| `attack-vectors/regex-language.md`          | G + L | V-G1, V-L1–L5          | 6  |

Total: 48 vectors. Categories: A:5, B:7, C:5, D:7, E:2, G:1, H:16, L:5. (V-C2 retired — folded into V-A3; its id is not reused.)

## Cross-cutting auditor mantras

- **Every `<--` is a constraint hole until proven otherwise.**
- **Every `LessThan(N)` operand must come from a `Num2Bits(M ≤ N)` chain.**
- **Every `Num2Bits(254)` over BN254 needs `_strict` or an alias check.**
- **Every divisor in `<-- a/b` needs `IsZero(b).out === 0` upstream.**
- **Every `Mux*` selector needs `s * (s - 1) === 0` upstream.**
- **Every public input must appear in at least one `===` / `<==` constraint.**
- **`assert(...)` is not a constraint — it's a compile-time check the verifier never sees.**

Each slice file repeats the mantras relevant to its categories, so an agent reading only its slice has the discipline it needs.
