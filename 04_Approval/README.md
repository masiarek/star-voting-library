# 04_Approval — Approval Voting

The simplest equal-vote method: mark **1 (approve)** or **0** for each candidate; the most-approved candidate wins. No rankings, no scores — a normal ballot with "vote for one" crossed out. Approval is Score voting at 1-bit resolution: enormous gain in expressiveness over choose-one, for near-zero ballot complexity.

**New to Approval?** The concept pages for this method live in [`01_Learn/`](01_Learn/README.md) — start with [Approval Voting](01_Learn/approval_voting.md) (the ballot and the count), then its [honest limits](01_Learn/approval_honest_limits.md). Everything below is the **runnable examples**.

Cases live in [`02_Examples/`](02_Examples), starting with [Approval 101 — most approvals wins](02_Examples/cases/cases_pages/approval_101_c3_b5.md) ([yaml](02_Examples/cases/approval_101_c3_b5.yaml)). Multi-winner (bloc) Approval has its own folder: [multi-winner Approval](02_Examples/multiwinner/) — the same ballot, top-`N` approved win, and a worked majority-sweep example.

Approval also appears throughout the comparison sets — that's where its character shows best:

- [The Black Curtain](../method_comparisons/black_curtain/) — the same five voters counted by Approval vs STAR vs RCV-IRV vs Score (Approval flips the winner in election 1)
- [The BV library](../method_comparisons/BV_Library/) — a real BetterVoting approval election
- Multi-winner theory: [multi-winner Approval](01_Learn/Multiwinner_Approval/approval_multiwinner.md) and the [ABC rules](01_Learn/Multiwinner_Approval/abc_rules_intro.md)

House rule: Approval ballots accept only `0`/`1` (blank / markers = not approved); the engine errors on 0–5 scores under `voting_method: Approval`.

**Conversation scripts:** the Larry ↔ Adam series (STAR + RCV-IRV) is indexed in [Conversation scripts — index](../07_Concepts/about_this_repo/conversation_scripts.md).

# file: README.md
