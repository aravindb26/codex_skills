# Solodit Pattern: Downstream pool incentives accrue without an adapter claim path

Source:
- https://solodit.cyfrin.io/issues/underlying-pool-incentive-rewards-are-never-claimed-mixbytes-none-barterlab-markdown

Imported:
- 2026-11-07

Severity:
- MEDIUM

Protocol / source:
- BarterLab / MixBytes

Tags:
- adapter, external incentives, reward ownership, stranded value

Dedupe:
- id: `75090`
- fingerprint: `f5edc5acf0b5af3df11141eb698d5705fa099f58e953374ead78440f286aebec`

Core mechanism:
- An adapter deposits or supplies assets into a downstream pool whose incentives accrue to the adapter or its beneficiary, but exposes no claim-and-forward path. Rewards can accumulate outside the protocol's normal accounting and remain inaccessible or uncredited.

Invariant and audit checks:
- Every reward stream earned by protocol-controlled positions has an explicit, reachable owner and claim/distribution/exit path.
- Trace incentive controller, reward recipient, adapter interfaces, migration and redemption paths, and whether claiming is permissionless, role-gated, or possible only through a downstream UI.

False-positive checks:
- Confirm the adapter actually owns or can claim the incentives and that a separate keeper, gauge, or user path does not already harvest them. Distinguish unclaimed yield from value users were promised or protocol revenue.

PoC shape:
1. Accrue a downstream reward for the adapter-held position.
2. Enumerate callable claim/forward functions and prove none can recover or account for it.
3. Measure the value stranded and identify the rightful beneficiary.

Triage notes:
- Report only if the reward is materially attributable to users/protocol and the missing path causes unrecoverable or meaningful value loss.
