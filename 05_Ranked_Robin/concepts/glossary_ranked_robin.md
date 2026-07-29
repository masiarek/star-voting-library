# Glossary — Ranked Robin & the Condorcet family

Method-specific terms for **Ranked Robin** (RCV-RR) and the broader Condorcet family. Shared, cross-method vocabulary lives in the [main glossary](../../07_Concepts/GLOSSARY.md).

- **Ranked Robin (RCV-RR)** — a Condorcet tabulation of a ranked ballot: compare every pair head-to-head, elect the most head-to-head wins (Copeland-style; ties broken by total margin). No center squeeze — do **not** lump it with IRV. → [Ranked Robin (RCV-RR / Copeland)](ranked_robin.md)
- **Ranked (ordinal) ballot** — the ballot Ranked Robin reads: order over degree of support, shared with RCV-IRV and STV (the term is defined once in the [main glossary](../../07_Concepts/GLOSSARY.md)). Unlike IRV's strict ballot, Ranked Robin naturally allows **equal ranks** (weak ranks) — see [Strict vs. Weak Ranks — Not All Ranked Ballots Are the Same](../../07_Concepts/scores_and_ranks/strict_vs_weak_ranks.md) and scored vs ranked [Scores vs. Ranks — Don't Confuse Ranks and Ratings](../../07_Concepts/scores_and_ranks/scores_vs_ranks.md).
- **Condorcet method** — any ranked method that *always* elects the candidate who beats every other head-to-head (the Condorcet winner) when one exists. A **family**: Ranked Robin, Ranked Pairs, Schulze, Minimax, Copeland.
- **Condorcet cycle** — a rock-paper-scissors situation (A beats B beats C beats A) with no Condorcet winner; each Condorcet method resolves it differently. → [Cycle Resolution — why Minimax, Ranked Pairs, and Schulze exist](cycle_resolution.md)
- **Copeland** — Ranked Robin's tabulation. Two conventions are both in use: **wins − losses**, and **wins + ½·ties** (what the engine prints, and what BetterVoting and `pref_voting` score). They are affine transforms of each other, so they always give the **same ranking** — but neither equals the raw *win count*, which ignores draws and can disagree with both. → worked case [a draw is worth half a win](../copeland_score/)
- **Ranked Pairs (Tideman)** — lock in the strongest pairwise victories first, skipping any that would create a cycle.
- **Schulze (beatpath)** — decides via the strongest "beatpaths" between candidates.
- **Minimax (Simpson–Kramer)** — elect the candidate whose *worst* pairwise loss is smallest.
- **Borda** — a positional ranked method (points by rank); ranked but **not** Condorcet-compliant. *Contrast with Ranked Robin, which is often mistaken for it:* Borda scores rank **numbers**; Ranked Robin uses only each ballot's **order** to decide pairwise winners — see [a blank is ranked last](rr_blank_means_last.md).
- **Blank / unranked (ranked last)** — a candidate you leave off a ranked ballot is placed **below every candidate you did rank** (not a specific tier like "5th" or "6th" — the numeric label is irrelevant to the count). Multiple blanks are **tied** with one another ([Equal Support](../../07_Concepts/GLOSSARY.md)). → [a blank is ranked last](rr_blank_means_last.md)
- **Bucklin (Grand Junction)** — a ranked, median-style method; ranked but **not** Condorcet. (Spelled *Bucklin*, not "Buckling".) <!-- terminology-ok: teaches the correct spelling -->


*The shared criterion terms — **Condorcet winner / loser / efficiency / compliance**, **monotonicity**, **summability** — are defined in the [main glossary](../../07_Concepts/GLOSSARY.md#properties-criteria) (they apply across methods).*

# file: glossary_ranked_robin.md
