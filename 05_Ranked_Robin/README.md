# 05_Ranked_Robin — Ranked Robin (RCV-RR / Copeland)

Equal Vote's method for **ranked** ballots: compare every pair of candidates
head-to-head; the candidate who wins the most matchups wins (a round robin,
like a sports league). It reads the *whole* ballot — no eliminations, no
center squeeze — and elects the Condorcet winner whenever one exists.

| Where | What |
|---|---|
| [`_main/`](_main/README.md) | the worked intro: RR elects the consensus candidate IRV eliminates |
| [`condorcet_vs_ranked_robin/`](condorcet_vs_ranked_robin/README.md) | a clean Condorcet winner, a genuine cycle (rock/paper/scissors) and how RR resolves it, and a real 0-wins record |

Same ballot, different count: RCV-IRV (elimination rounds) lives in
[other methods](../06_Other/README.md) and inside the comparison sets.
Concept docs: [Ranked Robin](../00_start_here/RCV_Ranked_Robin/ranked_robin.md).

**Conversation scripts:** the Larry ↔ Adam series (STAR + RCV-IRV) is indexed in
[`conversation_scripts.md`](../00_start_here/conversation_scripts.md).

# file: README.md
