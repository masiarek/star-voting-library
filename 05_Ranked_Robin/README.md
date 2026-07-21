# 05_Ranked_Robin — Ranked Robin (RCV-RR / Copeland)

Equal Vote's method for **ranked** ballots: compare every pair of candidates head-to-head; the candidate who wins the most matchups wins (a round robin, like a sports league). It reads the *whole* ballot — no eliminations, no center squeeze — and elects the Condorcet winner whenever one exists.

| Where | What |
|---|---|
| [The worked intro — RR elects the consensus IRV eliminates](_main/) | the worked intro: RR elects the consensus candidate IRV eliminates |
| [Condorcet vs. Ranked Robin — worked examples](condorcet_vs_ranked_robin/) | a clean Condorcet winner, a genuine cycle (rock/paper/scissors) and how RR resolves it, and a real 0-wins record |
| [RR vs. IRV vs. plurality — same ballots](rr_vs_irv_plurality/) | one ranked ballot set, three winners — the Tennessee center-squeeze (BV-backed, triple-checked: LH / BetterVoting / pref_voting) |
| [Tiebreaks — dead heat → lot](rr_tiebreaks/) | the Equal Support column, the ½-Copeland credit, and the full ladder to lot order — and where the LH & BetterVoting tiebreaks [diverge](../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) |
| [**Burial — RR's signature wart, worked**](burial/) | the sincere/buried pair (BV2208/BV2209): fifteen voters rank the Condorcet winner last, manufacture a cycle, and win the record tie — triple-checked, deterministic on both engines |
| [STAR vs RR — 30 divergence samples](star_vs_rr_divergence/) | an auto-generated dump of 30 elections where STAR and RR elect different winners, spread across candidate field (3/5/7/10), electorate size, and grouped-vs-random structure — each YAML states its own cause (cycle vs dark horse), with RCV-IRV / Approval / Plurality on the same ballots (they scatter — no clean alignment). Empirical companion to the [simulation](../06_Other/simulations/README.md#star-vs-ranked-robin-divergence-simulation) |

Same ballot, different count: RCV-IRV (elimination rounds) lives in [other methods](../06_Other/) and inside the comparison sets. Concept docs: [Ranked Robin](../00_start_here/RCV_Ranked_Robin/ranked_robin.md).

**Conversation scripts:** the Larry ↔ Adam series (STAR + RCV-IRV) is indexed in [Conversation scripts — index](../00_start_here/about_this_repo/conversation_scripts.md).

# file: README.md
