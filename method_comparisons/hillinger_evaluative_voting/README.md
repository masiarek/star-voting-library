# Hillinger's evaluative voting — the paper, made runnable

**Level: 301 · deep dive**

Claude Hillinger's **"Voting and the Cardinal Aggregation of Judgments"** (Munich Discussion Paper 2004-9, [DOI](https://doi.org/10.5282/ubm/epub.353)) argues that voting is the aggregation of *judgments* rather than of *preferences*, that judgments must be **measured** before they can be aggregated, and that the classic voting paradoxes are artifacts of ballots that restrict what a voter may say. His proposal is **evaluative voting** (EV): score every candidate on a uniform, unrestricted scale; the largest sum wins.

This folder runs his own worked example. The theory lives on the concept page → **[Cardinal utility](../../07_Concepts/topics/cardinal_utility.md)**.

## The cases

| Case | What it shows | Source |
|---|---|---|
| [Table 4 — three methods, three winners](cases/cases_pages/hillinger_t4_ev3.md) | his "mirror pathology" of IRV: the most popular candidate eliminated in round one | [`hillinger_t4_ev3.yaml`](cases/hillinger_t4_ev3.yaml) |
| [The same election, rescaled](cases/cases_pages/hillinger_t4_affine.md) | what "cardinal" guarantees: totals move under `u′ = 2u + 1`, the winner does not | [`hillinger_t4_affine.yaml`](cases/hillinger_t4_affine.yaml) |
| [Table 3 — one approval result, two opposite Borda winners](cases/cases_pages/hillinger_t3_arbitrariness.md) | his §10 answer to Saari–Van Newenhizen: a coarse score under-determines the ranking exactly as a ranking under-determines the score | [`hillinger_t3_arbitrariness.yaml`](cases/hillinger_t3_arbitrariness.yaml) |

### Table 1 is already in the library — do not mint it again

Hillinger's **Table 1** ("Most Disliked Candidate Wins Under PV") is 3 voters `a > b > c`, 2 `b > c > a`, 2 `c > b > a`: **a** wins the plurality count 3–2–2 while **4 of the 7 rank a last**. That profile is *identical* to **Felsenthal's Example 1**, which this repo already runs and already has live on BetterVoting as **[BV2144 (`mxfmhm`)](../felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md)** — same seven ballots, cast as Ana / Bo / Cal, where it demonstrates four plurality paradoxes at once (Condorcet winner ignored, Condorcet loser elected, [absolute loser](../../07_Concepts/voting_paradoxes/absolute_loser_paradox.md) elected, and the spoiler/SCC effect).

Two authors, two decades apart, reached for the same seven ballots because it is the smallest profile that makes the point. Cite it as Hillinger Table 1 *or* Felsenthal Example 1 — but there is one election, and it already exists. The definitional question Hillinger raises alongside that table — what *is* a majority or minority candidate, given that almost nobody wins an arithmetic majority in a real field — is answered at [Majority & minority candidates](../../07_Concepts/topics/majority_criterion/majority_and_minority_candidates.md).

## Table 4 — the mirror pathology

Hillinger's §12 point: plurality's famous defect is that an **unpopular** candidate may win; IRV's mirror defect is that the **most popular** candidate may be eliminated in the very first round. Thirty voters, three candidates:

| Voters | Order | EV-3 marks (Ana, Bruno, Chloe) |
|:--:|---|:--:|
| 9 | Ana > Bruno > Chloe | 2, 1, 0 |
| 10 | Bruno > Ana > Chloe | 1, 2, 0 |
| 11 | Chloe > Ana > Bruno | 1, 0, 2 |

Ana holds the **fewest first choices** (9) and is the one candidate **nobody ranks last**. She is the Condorcet winner — she beats Bruno 20–10 and Chloe 19–11 — and she wins the cardinal count with 39 to Bruno's 29 and Chloe's 22, reproducing Hillinger's table exactly.

**What the engine adds to the paper.** Hillinger reports only the STV failure. Run the same thirty ballots through everything and they split three ways:

| Method | Winner |
|---|---|
| Plurality | **Chloe** — most first choices (11), ranked last by 19 |
| RCV-IRV | **Bruno** — Ana eliminated first, her ballots transfer |
| STAR · Score · Ranked Robin | **Ana** — highest sum, and the Condorcet winner |

One electorate, one set of opinions, three different winners.

> **A note on the scale.** The marks are Hillinger's EV-3 ballot `(−1, 0, +1)` shifted onto this repo's 0–5 scale as `(0, 1, 2)`. He states in §5 that the choice of origin does not affect the outcome; the [rescaled twin](cases/cases_pages/hillinger_t4_affine.md) checks that claim rather than taking his word for it.

> **A typo, caught by running it.** The paper gives the Ana–Bruno pairwise as `ab(20/11)`, which sums to 31 of 30 voters. It is **20–10** (the `ac(19/11)` beside it is correct). Harmless to his argument — but it is what a runnable companion is for.

<!-- report:hillinger_t4_ev3 -->
```text
[Divergence from STAR]
  STAR                   = Ana
  Choose-One (Plurality) = Chloe   (differs from STAR)
  RCV-IRV                = Bruno   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/hillinger_t4_ev3_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 30 ballots.
Count × Ana,Bruno,Chloe
   11 ×   1,    0,    2
   10 ×   1,    2,    0
    9 ×   2,    1,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 39 -- First place
   Bruno         -- 29 -- Second place
   Chloe         -- 22
 Ana and Bruno advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ana           -- 20 -- First place
   Bruno         -- 10
   Equal Support --  0
 Ana wins.
   Runoff math:
     30  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     30  voters with a preference  (majority = 16)
           Ana 20 (67%)  ·  Bruno 10 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ana
```
<!-- /report -->

## Related

- [Cardinal utility](../../07_Concepts/topics/cardinal_utility.md) — the concept page this folder supports: what makes a scale cardinal, Sen's measurability/comparability axes, the vNM trap, Harsanyi's theorem, and a claim-check of Hillinger
- [Is Approval's outcome arbitrary?](../../04_Approval/01_Learn/approval_indeterminacy.md) — the teaching page for §10 and Table 3: the Saari–Van Newenhizen criticism, why the Brams–Fishburn–Merrill defense fell short, and what the argument does to STAR
- [Center squeeze](../center_squeeze/) — the same failure shape as a dedicated topic
- [Condorcet efficiency](../../07_Concepts/topics/condorcet/) — how often the head-to-head winner actually wins
- [Range / Score voting](../../06_Other/Range/concepts/range_voting.md) — EV without a runoff, which is what Hillinger actually proposes
- [Scores vs. ranks](../../07_Concepts/scores_and_ranks/scores_vs_ranks.md) — the ballot-level distinction, without the theory
