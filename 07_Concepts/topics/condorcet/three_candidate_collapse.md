# At three candidates, the famous Condorcet methods collapse into one

*The voting-theory literature lists **dozens** of Condorcet methods — Minimax, Ranked Pairs, Schulze, Kemeny, Dodgson, Young, Copeland, Nanson, leximin, and more — and newcomers reasonably panic at the zoo. Here's the calming fact, proved cleanly by [Brandt, Dong & Peters (2024)](three_candidate_maximin.md): **with exactly three candidates, most of the famous ones are literally the same rule.** They can only disagree when there are four or more candidates. So for a three-way race, "which Condorcet method?" barely matters — and where the survivors *do* differ is small and nameable.*

→ Reads on from: [the maximin result](three_candidate_maximin.md) · [cycle resolution](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md) (where they finally diverge, at 4 candidates) · [the ranked-ballot method zoo](../ranked_ballot_methods_zoo.md) · [Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md).

---

## The collapse

Every Condorcet method agrees whenever a [Condorcet winner](README.md) exists — that's not news. The interesting question is what they do in a **cycle** (no head-to-head winner). The paper's Fig. 2 maps the entire refinement hierarchy for three candidates, and the headline is that a whole cluster of celebrated methods **coincide exactly**:

> **Maximin = Ranked Pairs = Schulze (beat-path) = Kemeny = Dodgson = Young** — one and the same social choice function on three candidates.

Three more sit just below or beside them, and these are the ones actually worth distinguishing at three candidates:

- **Copeland** (our [Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md)) — a **separate branch**. It counts pairwise *wins*, so in a symmetric three-cycle it **ties all three** and needs a tiebreak. It is *not* a refinement of maximin, which matters: it doesn't inherit maximin's [no-show immunity](three_candidate_maximin.md).
- **Nanson** — a maximin refinement, and a *strong* Condorcet extension (it also picks "almost-Condorcet-winners" that maximin's tie-break would drop).
- **leximin** — the *most decisive* refinement (fewest tied outcomes of any rule studied — the paper's Fig. 4), which is why it's the natural rule to complete maximin.

So the "dozens of methods" reduce, for a three-way race, to a **handful that matter**: the maximin family (one rule, however you brand it), Copeland/Ranked Robin (ties cycles), and the two refinements (Nanson, leximin) that break maximin's ties.

## See the collapse — and where it breaks

The claim is checkable in this library with cases already runnable:

**Three candidates, symmetric cycle → everyone ties.** The [North district (6 voters) in the reinforcement case](../../../method_comparisons/reinforcement_paradox/README.md) is a perfect rock-paper-scissors cycle. Ranked Robin's Copeland count ties Ada, Ben, and Cara 1–1; maximin, Ranked Pairs, and Schulze also return all three (a symmetric cycle has no "least-bad loss" to separate them). No method distinguishes them — exactly the collapse.

**Three candidates, tilted cycle → the maximin family separates from Copeland.** The paper's Fig. 1 profile (5 voters: 2×Ada>Ben>Cara, 1×Ben>Cara>Ada, 2×Cara>Ada>Ben) has margins Ada→Ben by 3, Ben→Cara and Cara→Ada by 1 each. **Copeland/Ranked Robin** ties all three at 1–1 (then LH breaks to Ada by largest margin); **maximin** instead reads the margins and returns {Ada, Cara} — the two whose worst loss is only 1. Same three candidates, and already the "wins" rule and the "margins" rule part ways — a three-candidate reminder that Copeland is *not* in the maximin family. **Runnable, with the minimality proved:** [The minimal tilted cycle — five voters, and already the methods disagree](../../../method_comparisons/minimal_tilted_cycle/README.md) shows why 5 voters and margins 3–1–1 are the *only* option (3 voters force symmetry, 4 admit no cycle at all), and runs every rule the tools can count on it — including Kemeny–Young and Dodgson, which land on {Ada, Cara} with the rest of the collapsed family.

**Four candidates → the maximin family itself finally splits.** This is the boundary. In the [21-voter and 40-voter profiles on the cycle-resolution page](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md), Minimax, Ranked Pairs, Schulze, and Split Cycle — identical at three candidates — return **different winners**. The collapse is a three-candidate phenomenon; add a fourth and the zoo is real again.

## Why this is the practical takeaway

For a **single-winner public election with a realistic three-way top tier**, the anxious "but *which* Condorcet method?" debate is mostly moot: pick maximin, Ranked Pairs, or Schulze and you have picked the same rule. The genuine design choices that remain are narrow and clear:

1. **Copeland/Ranked Robin vs. the maximin family** — "most wins" (simple, ties cycles) vs. "least-bad loss" (breaks cycles, no-show-immune). This repo's engine ships Copeland; the difference only surfaces in a cycle.
2. **Which tie-break for maximin** — leximin (most decisive) or Nanson (rescues near-winners).

Everything else in the method zoo is a four-plus-candidate concern. Full hierarchy, the twelve cycle-shapes, and the axiomatic characterizations: [Brandt, Dong & Peters, "Condorcet-Consistent Choice Among Three Candidates"](https://arxiv.org/abs/2411.19857) (2024), summarized [here](three_candidate_maximin.md).

---

*Source: Felix Brandt, Chris Dong & Dominik Peters, "Condorcet-Consistent Choice Among Three Candidates" (arXiv:2411.19857, 2024), Fig. 2 (the three-candidate refinement Hasse diagram) and Table 1 (all twelve no-Condorcet-winner margin graphs with each rule's output). Runnable anchors are this library's own elections; the maximin/Ranked-Pairs/Schulze cross-checks use `pref_voting` (see [cross-checking with pref_voting](../../tabulation_engines/cross_checking_with_pref_voting.md)). Glossary: [`Condorcet`](../../GLOSSARY.md).*
