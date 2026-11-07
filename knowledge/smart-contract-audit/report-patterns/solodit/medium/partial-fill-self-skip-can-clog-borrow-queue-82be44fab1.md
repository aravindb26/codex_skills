# Solodit Pattern: Partial-fill dust and self-skip can clog a borrow queue

Source:
- https://solodit.cyfrin.io/issues/borrow-queue-clogging-via-the-self-skip-mechanism-mixbytes-none-barterlab-markdown

Imported:
- 2026-11-07

Severity:
- MEDIUM

Protocol / source:
- BarterLab / MixBytes

Tags:
- borrow queue, partial fill, dust order, sybil griefing

Dedupe:
- id: `75088`
- fingerprint: `82be44fab15aea98778db02291369faeadbd545cbcd7d67ee5d471dca60e22b6`

Core mechanism:
- A minimum order size is enforced when creating or cancelling an order but not after a partial fill. The remaining dust order can persist at the queue head; a self-skip/requeue operation changes ordering, letting an attacker rotate or stack low-cost entries.

Invariant and audit checks:
- Partial execution must not leave unserviceable queue entries that block or unfairly reorder valid borrowers.
- Compare minimum-size validation at creation, partial-fill mutation, skip, cancel, and dequeue. Test many attacker-controlled entries and verify progress, fairness, and bounded per-call work.

False-positive checks:
- Establish the actual queue policy and whether dust can be permissionlessly removed or skipped by others. Quantify attacker capital/gas versus blocked users and verify this is not merely an intended priority rule.

PoC shape:
1. Create a valid order and partially fill it below the minimum.
2. Exercise self-skip/requeue and repeat with multiple attacker-controlled entries.
3. Show ordinary queue processing or borrower progress is materially delayed or blocked.

Triage notes:
- Sybil cost, queue caps, gas limits, and practical recovery determine severity; transient ordering changes alone are weak.
