# 04_Approval — Approval Voting

The simplest equal-vote method: mark **1 (approve)** or **0** for each
candidate; the most-approved candidate wins. No rankings, no scores — a normal
ballot with "vote for one" crossed out. Approval is Score voting at 1-bit
resolution: enormous gain in expressiveness over choose-one, for near-zero
ballot complexity.

Cases live in [`_main/`](_main), starting with
[`approval_101_c3_b5.yaml`](_main/approval_101_c3_b5.yaml). Multi-winner (bloc)
Approval has its own folder: [multi-winner Approval](multiwinner/)
— the same ballot, top-`N` approved win, and a worked majority-sweep example.

Approval also appears throughout the comparison sets — that's where its
character shows best:

- [`../method_comparisons/black_curtain/`](../method_comparisons/black_curtain) —
  the same five voters counted by Approval vs STAR vs RCV-IRV vs Score
  (Approval flips the winner in election 1)
- [`../method_comparisons/BV_Library/`](../method_comparisons/BV_Library) —
  a real BetterVoting approval election
- Concept docs: [`../00_start_here/Approval_Voting/`](../00_start_here/Approval_Voting) — the [method overview](../00_start_here/Approval_Voting/approval_voting.md), its [honest limits](../00_start_here/Approval_Voting/approval_honest_limits.md), and [multi-winner Approval](../00_start_here/Approval_Voting/approval_multiwinner.md)

House rule: Approval ballots accept only `0`/`1` (blank / markers = not
approved); the engine errors on 0–5 scores under `voting_method: Approval`.

**Conversation scripts:** the Larry ↔ Adam series (STAR + RCV-IRV) is indexed in
[`conversation_scripts.md`](../00_start_here/conversation_scripts.md).

# file: README.md
