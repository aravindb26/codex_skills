# Nuclei Suggest Reference For Codex

Source: <https://github.com/forefy/.context/tree/c8ff161fccdeef9a0416df6230636eb2dfde4a8b/skills/hunter-utils/nuclei-suggest>

This is a filtered, reference-only Web2/AppSec skill. It is not an active default Codex skill and
must not be routed into Solidity, Vyper, Solana, Cosmos, Move, or other Web3 audits.

Use it only for an authorized Web2 target when Nuclei template selection is relevant. It requires
scope confirmation, distinguishes passive from intrusive templates, honors `.nuclei-ignore`, and
requires commit-pinned template links plus captured evidence. A skipped template is unrun, not
clean. The install commands in the reference are offers for the operator, not automatic steps.

Review the original `SKILL.md` and both references before using it. Nuclei remains a lead generator;
validate every result against the program scope, actual request/response evidence, exploitability,
and impact.
