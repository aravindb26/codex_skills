# Discovery Init

> **Language rule**: All discovery documents (any `.md` file written to `.discovery/`) are always in English — regardless of the conversation language.

**You are reading this file before generating your first response. Good. Now follow the steps below exactly — one step at a time, one question per response.**

Create the `.discovery/` directory tree and `STATE.md`. This step runs before any phase begins, regardless of entry profile. Do not begin Phase 0 or Phase 1 before STATE.md exists.

## Scope of this phase

Init covers: working name, session framing, directory structure, and STATE.md creation. Nothing else.

If the developer raises topics belonging to a future phase (competitive analysis, economics, risks) — register as `QUEUED [Phase N]: ...` in STATE.md and redirect back.

---

## Steps

Do not ask multiple questions at once. Work through these steps sequentially, waiting for the developer's answer before advancing to the next.

---

### Step 1 — Acknowledge and extract the working name

Based on the developer's first message, classify their profile:

- **Profile A** — Concrete idea: developer described a specific protocol concept.
- **Profile B** — Vague direction: developer named a space or segment but no specific idea.
- **Profile C** — Open exploration: developer wants to build in DeFi but has no stated direction.

Do not ask the developer which profile they are — classify from context.

**Profile A vs B disambiguation — critical rule**: A developer who names a domain, technology, space, or segment (e.g., "AI Agents and DevOps", "something for LPs", "yield farming", "lending on Solana") but expresses a desire to *explore*, *think of*, *brainstorm*, or *look for* ideas is **Profile B — not Profile A**. Profile A requires a specific concept or mechanism, not just a domain. If the developer's message contains any of the following signals — "want to think of ideas", "exploring what to build", "looking for ideas", "want to brainstorm", "haven't decided what to build", "want to see what I could build", "figuring out what to build", or equivalents in any language — classify as Profile B (or C if no domain is stated), regardless of how specific the domain sounds. A domain name is not an idea. When the profile is still ambiguous after reading the message, ask the developer directly: *"Do you have a specific concept in mind, or would you like to explore what to build within [space] first?"*

**Send one message** that: (1) reflects back your reading of their starting point in 1–2 sentences, and (2) asks exactly one question:

**Profile A:**
*"You're describing [one-sentence summary of the concept]. What's a working name for this — even a placeholder? We'll use it to anchor the session."*

If the first message already contains a clear name — skip the name question and move directly to Step 2, stating: *"Got it — working name: [name]. Let me set up the session."*

**Profile B:**
*"You want to build something in [space]. What's the most important constraint for you — the type of user you want to serve, the chain, the problem area, or something else? This shapes how we'll scan for opportunities."*

**Profile C:**
*"Open exploration — understood. Is there a type of user or a DeFi domain you find most interesting, even loosely? If truly open, say so and we'll cover the full landscape."*

If the first message doesn't contain enough signal to classify the profile, ask: *"Tell me about what you want to build — or about where you're thinking of building, if you don't have a specific idea yet."*

**Ask and stop.** Wait for the developer's answer before proceeding to Step 2.

---

### Step 2 — Confirm the session goal

Before creating any files, confirm what the developer wants from this session. One short message:

*"We'll work through [phase list] and land on a go/no-go decision. If it's a go, the output is a Protocol Brief that feeds directly into defi-spec-driven. Does that match what you're after — or do you have a narrower goal for today?"*

Phase list by profile:
- **Profile A**: Phases 1–6 (Idea Sharpening → Go/No-Go)
- **Profile B/C**: Phases 0–6 (Opportunity Discovery → Go/No-Go)

**Ask and stop.** Wait for confirmation or redirection before creating files.

If the developer wants a narrower scope (e.g., "just validate the economic model") — note it in STATE.md as a session constraint and adjust routing accordingly.

---

### Step 3 — Create directory structure and STATE.md

After Step 2 is confirmed, create the directory and STATE.md without asking for more input:

```
.discovery/
├── project/
├── opportunities/
├── problem/
├── landscape/
├── canvas/
├── economics/
├── risks/
└── decision/
```

Create `.discovery/project/STATE.md` from the template in [state-management.md](state-management.md). Set:
- `Name:` → working name from Step 1 (or "TBD" if not established)
- `Profile:` → A, B, or C
- `Phase:` → 0 (Profile B/C) or 1 (Profile A)

Log any topics raised during Steps 1–2 that belong to future phases as `QUEUED [Phase N]: [description]` entries in STATE.md.

---

### Step 4 — Transition to the first phase

Name 2–3 specific things the developer should already know before diving in — inferred assumptions, queued topics, or choices with downstream consequences visible from the first message.

Then transition:

**Profile A:** *"Session ready. Starting Phase 1 — Idea Sharpening, where we'll separate the problem from the mechanism and sharpen the problem statement before anything else."*

**Profile B:** *"Session ready. Starting Phase 0 — Opportunity Discovery (focused mode), where we'll scan [space] for protocol-shaped problems and select one to pursue."*

**Profile C:** *"Session ready. Starting Phase 0 — Opportunity Discovery (open mode), where we'll scan DeFi systematically for protocol opportunities and select one to pursue."*

---

## Done when — gate

Before advancing to Phase 0 or Phase 1, verify:

- `.discovery/project/STATE.md` exists with Name, Profile, Phase, and Phase History sections
- Working name recorded (or "TBD" with a note to revisit in Phase 1)
- Topics raised during Steps 1–2 that belong to future phases are written to STATE.md as QUEUED entries
- Profile classification and phase routing confirmed
