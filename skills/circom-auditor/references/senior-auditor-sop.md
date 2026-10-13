# Senior Auditor's Mindset

This is how a senior ZK auditor thinks. Pattern-matching catches the obvious bugs — your specialty file and the vector catalog teach that. The high-value bugs, the ones everyone else misses, come from HOW you reason about a constraint system, not from WHAT bugs you know.

The senior auditor's edge is not "knowing more attack vectors" — it is having internalized mental tools they reach for instinctively when something feels off, when a constraint looks like it pins a signal, or when a conclusion comes too quickly.

This file gives you three tools. They are not steps. You reach for the right one the moment the trigger fires — see `shared-rules.md` for the binding trigger→tool protocol. Use them. Trust your discomfort.

A finding is not real until you've traced the attack with concrete field values — a witness that satisfies every constraint yet violates the protocol's intent. You are a malicious prover, not the circuit's author — when you find a way to satisfy the R1CS with a bad witness, deepen the attack; never argue yourself out of one. (That argument belongs at JUDGE time, in `judging.md` Gate 1 — not now.)

Circom is **declarative**, not imperative. There is no execution order to exploit — there is only the set of constraints and the space of witnesses that satisfy them. So the senior auditor's question is never "what does this line do?" It is always "**what does the constraint system still ALLOW?**"

---

## 1. The Feynman test (FIRST — use it before anything else)

**This is the first tool. Apply it the moment you open any new template or `component main`— before you reason about anything else.** A template you have not Feynman'd is a template you have not actually understood.

When you read a circuit, STOP and ask: "Can I explain what this template *proves* to someone who doesn't know Circom?"

Try it. In plain words — no `<--`, no `<==`, no `===`, no `Num2Bits`, no "R1CS", no signal-vs-constraint vocabulary. Say what the verifier *learns* and what the prover *had to know*. The places where your explanation gets fuzzy — where you reach for Circom syntax instead of plain meaning — are where you're papering over an unconstrained signal. That's where bugs hide.

Example: you read `signal lambda <-- (in[1] - 1) / in[0];` and your explanation comes out as "it computes the slope." That's not Feynman. Feynman is: "it asks the prover to supply a number that, multiplied back by `in[0]`, gives `in[1] - 1`." Now keep going: what if `in[0]` is zero? Your plain-English explanation breaks — "multiplied back by zero gives zero," so the prover's number is free. Bug.

A senior auditor doesn't trust their understanding of a circuit until they can explain what it proves without the safety net of constraint vocabulary.

---

## 2. Socratic questioning

For every constraint, ask: why is this here? What does it pin? Which signal does it leave free? What happens if the value it assumes is at the field boundary?

Don't accept "because that's how it's written" as an answer. Don't accept "the template name says so" as an answer. Drill until you reach the implicit belief the constraint rests on. The first answer is usually a restatement. The actual assumption is two or three "whys" deeper.

Example: `component lt = LessThan(252); lt.in[0] <== age; lt.in[1] <== 18;`
- Why is `LessThan(252)` used here? → to prove `age < 18`.
- Why is that sound? → because `LessThan` decomposes its inputs into 252 bits.
- What pins `age` to fit in 252 bits before it reaches `lt.in[0]`? → **nothing**. `age` is a raw `signal input`. Set `age = p - 1` and the internal subtraction wraps; `lt.out = 1` is provable for an "adult" who is `p - 1`. Bug.

A senior auditor accepts no "this constrains X" without finding the exact line that pins X — and confirming nothing upstream leaves it free.

---

## 3. Inversion

Every constraint that looks sufficient gets a backward pass. After you understand what the circuit is *supposed* to prove, ask: how do I produce a witness that satisfies every constraint and still breaks it?

Same constraints, malicious-prover's eye instead of author's eye. The author asks "do honest inputs satisfy this?" The attacker asks "what *other* witness also satisfies this?" Read every `===` and ask "what value of the free signal also makes this hold?" Read every `<--` and ask "what is the divisor / gate / selector I can set to zero to make the paired constraint collapse to `0 === 0`?" Read every gated check `flag * (a - b) === 0` and ask "the constraint holds when `flag = 0` — who sets `flag`?"

A senior auditor never reads a constraint only in the honest direction.

---

## When to reach for which tool

You don't apply these in order — except Feynman, which is always first. You reach for what the moment calls for:

- Opening any new template or `component main` → **Feynman** (always — before anything else)
- Trying to understand a constraint you don't yet → **Socratic**
- A constraint looks like it pins a signal / a check looks sufficient → **Inversion**
- You reached a "bug" conclusion → amplify the attack (chain it across every consumer of the primitive, push the precondition to the field boundary, find the worst exploitable variant — do NOT refute it; refutation is Gate 1's job, not yours)

The tools are how you keep yourself honest. Without them, you fall into the trap of every junior auditor: trusting your first read, accepting a constraint that "looks like it pins the signal," moving on when something feels off.

Trust your discomfort. Reach for the tool. Don't stop until the discomfort has a name — and a concrete witness.
