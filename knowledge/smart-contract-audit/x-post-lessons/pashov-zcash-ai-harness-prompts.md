# Pashov Zcash Post - AI Harnesses Need Expert-Directed Prompts

Source context: User-provided X post from Pashov about the Zcash critical vulnerability capable of minting counterfeit ZEC.

## Core Lesson

A strong AI model and an automated audit harness can still miss critical bugs when the prompt is too broad. In the cited Zcash case, prior automated audits of the Orchard circuit using the same auditor agents did not find the bug. The model found it only when directed at a specific gadget and a specific failure mode: variable-base scalar multiplication constraints that could lead to inflation or double spending.

## Audit Rule

For serious audits, convert broad hunting into targeted invariant questions:

- Identify the exact invariant or security property.
- Identify the exact module, function, gadget, or state transition enforcing it.
- Name the specific bug class being tested.
- Try to disprove the hypothesis against code and specs.
- Use PoC evidence before treating the result as submit-worthy.

## Practical Prompt Shape

```text
Audit [specific module/function/path] for [specific bug class].
Focus on whether [specific invariant/security property] can break under [program scope and attacker model].
Use docs, prior audits, known issues, skills, and knowledge-base patterns.
Try to disprove first, then strengthen any surviving candidate.
Accept only code-backed and PoC-backed conclusions.
```

## False Confidence Warning

A broad prompt like "audit the protocol for inflation or double-spend bugs" may still miss deep issues. Treat broad AI passes as orientation only. High-risk surfaces need repeated, targeted, expert-guided passes.
