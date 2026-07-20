# Exercise 4 — Lillehammer 1994: nine judges, two winners

*The ladies figure-skating final at the 1994 Winter Olympics came down to nine judges ranking Oksana Baiul, Nancy Kerrigan, and Chen Lu. History records a 5–4 split for Baiul's gold. Rerun those nine real ballots as a scored election and something odd happens: **Score voting and STAR disagree** — on real data, no construction needed.*

**You practice:** converting ranks to scores with an order-preserving map · Score vs STAR on the same ballots · why the runoff verdict survives the conversion but the score totals don't · a Pareto-dominance impossibility argument.

Work each part on paper before opening its solution. The YAML at the bottom is runnable; its `expected_winners` key is regression-tested, and the `_tabulated` mirror is the full audit report.

## The ballots

The judges' final ordinals (B = Baiul, K = Kerrigan, L = Chen Lu):

| | judges 1–5 | judges 6–7 | judges 8–9 |
|---|:---:|:---:|:---:|
| **1st** | B | K | K |
| **2nd** | K | B | L |
| **3rd** | L | L | B |

To score them, use the repo's standard order-preserving map for 3 candidates: **1st → 5, 2nd → 3, 3rd → 1** (the same top=5/bottom=1 linear map the repo's LeGrand and Felsenthal cases use).

## Your task

- **(a)** Write out the nine score ballots and compute the totals. Who wins **Score voting**?
- **(b)** Run **STAR** on the same ballots. Who wins the runoff, and by what count?
- **(c)** One of your two answers matches what actually happened in Lillehammer. Which?
- **(d)** The 5/3/1 map was an assumption. Try to build a *different* order-preserving score assignment (each judge's own ranking preserved) that changes the **runoff** verdict. What do you find — and can a different map change the **Score** verdict?
- **(e)** Prove that **Chen Lu cannot win under any honest scoring whatsoever** — not Score, not STAR, not Approval, not any ranked method.

## Solutions

<details>
<summary><b>(a) Score — Kerrigan, 35 to 33</b></summary>

Baiul: 5×5 + 2×3 + 2×1 = **33**. Kerrigan: 5×3 + 2×5 + 2×5 = **35**. Lu: 7×1 + 2×3 = **13**. **Kerrigan leads the scores** — five 3s from Baiul-first judges plus four 5s beat five 5s plus two 3s and two 1s. Breadth of moderate support, added up, outweighs a bare majority of maximums.

</details>

<details>
<summary><b>(b) STAR — Baiul, 5–4</b></summary>

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Kerrigan      -- 35 -- First place
   Baiul         -- 33 -- Second place
   Lu            -- 13
 Kerrigan and Baiul advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Baiul         -- 5 -- First place
   Kerrigan      -- 4
   Equal Support -- 0
 Baiul wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Baiul 5 (56%) vs Kerrigan 4 (44%); majority = 5.
```

The engine also prints its `[Runoff Reversal]` block — Kerrigan topped the scores, **Baiul wins the runoff** — plus a divergence note that a per-judge approval reading would side with Kerrigan too. The reversal is the whole exercise: the scoring round finds the finalists, then the majority decides between them.

</details>

<details>
<summary><b>(c) History sides with the runoff</b></summary>

Baiul took the gold on the real 5–4 judging split — the same five judges who prefer her here. The Olympic ordinal system of the day was majoritarian between the top pair, and STAR's automatic runoff reproduces it exactly. The Score total is the counterfactual: under add-up-the-points rules, Kerrigan wins Lillehammer.

</details>

<details>
<summary><b>(d) The map matters for Score — and can't touch the runoff</b></summary>

Try to help Baiul's total: stretch her supporters' ballots (B5, K1, L0) and compress her opponents' (K5, B4). That's still order-preserving for every judge, and now Baiul's total beats Kerrigan's — the **Score verdict flips with the map**. Now try the same trick on the **runoff**: impossible. The runoff only asks each judge *which finalist is higher*, and every order-preserving map keeps every judge's B-vs-K direction unchanged — judges 1–5 prefer Baiul under *any* honest scores, judges 6–9 prefer Kerrigan. As long as Baiul and Kerrigan are the finalists (and Lu's 13-ish total never threatens that), **STAR answers Baiul 5–4 under every consistent map.** Rank→score conversion injects an assumption; totals inherit it, pairwise comparisons don't. (The same moral as [scale granularity can flip the winner](../../00_start_here/scores_and_ranks/scale_granularity_flips_the_winner.md) — score *magnitudes* are modeling choices.)

</details>

<details>
<summary><b>(e) Chen Lu: a two-line impossibility proof</b></summary>

Look at the ordinals: **all nine judges rank Kerrigan above Lu** (judges 1–5: K 2nd vs L 3rd; judges 6–7: K 1st vs L 3rd; judges 8–9: K 1st vs L 2nd). So under any honest ballots whatsoever, Kerrigan's score ≥ Lu's on every single ballot (giving totals K ≥ L), Kerrigan beats Lu head-to-head 9–0, and any approval set containing Lu contains Kerrigan. Lu is **Pareto-dominated**: no method that respects unanimous preference can elect her. The only way Chen Lu wins Lillehammer is if some judges honestly *change their minds* — no clever tabulation does it for them.

</details>

## Reading this fairly

The strongest footing an example can have: **it really happened** — real ballots from a real event (the [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)'s bonus criterion). The honest caveat runs the other way: the *scores* are our imposition on ranked ordinals, and part (d) is the disclosure — the Score-vs-STAR split is real, but "Kerrigan 35, Baiul 33" is an artifact of the 5/3/1 map, while "Baiul 5–4" is not.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex04_olympics_1994.yaml
```

Source: [ex04_olympics_1994.yaml](cases/ex04_olympics_1994.yaml). Full audit report: [mirror](cases/cases_tabulated/ex04_olympics_1994_tabulated.txt).

---

**Where these ballots come from.** The 1994 Winter Olympics ladies figure-skating final ordinals, as reproduced (with the cardinal-methods exercise built on them) in Brendan W. Sullivan, *An Introduction to the Math of Voting Methods* (619 Wreath Publishing, 2022), ch. 5. Real names kept — they are the historical record, so the repo's fresh-cast rule doesn't apply.

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex04_olympics_1994.md
