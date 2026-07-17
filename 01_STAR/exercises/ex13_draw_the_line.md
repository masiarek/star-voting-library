# Exercise 13 — Where do you draw the line?

*Nine voters hold perfectly clear opinions about Ash, Beck, and Cora — you can read them off their 0–5 scores below. Now hand those same nine people an **Approval ballot**: "mark everyone you approve of." Each voter must compress a five-point opinion into a yes/no. Run the election three times, with the whole room drawing its approval line at 3+, at 4+, and at favorites-only. Predict all three winners before you start — and then decide which of them is "the real one."*

**You practice:** the Approval ballot's hidden free parameter — the **threshold** — and why [Approval](../../04_Approval/README.md) has *no canonical sincere ballot*: the same honest opinions legally produce many honest ballots, and the election can turn on which one the room's psychology converges to.

Work each part on paper before opening its solution. All four YAMLs are runnable; the STAR file's answer key is regression-tested, and the `_tabulated` mirrors are the full audit reports.

## The opinions

Nine voters, scores 0–5 (rows are candidates, columns are voter blocs):

| | ×3 voters | ×2 voters | ×4 voters |
|---|:---:|:---:|:---:|
| **Ash** | 5 | 0 | 3 |
| **Beck** | 4 | 5 | 0 |
| **Cora** | 0 | 3 | 5 |

## Your task

- **(a)** Warm-up on the full scores: who wins plain **Score voting**, and who wins **STAR**? (They disagree — say why in one sentence.)
- **(b)** **Approve 3 and up** (the generous reading): convert every ballot, count approvals, name the winner.
- **(c)** **Approve 4 and up** (the stricter reading): same drill. Who wins now, and *why did the previous winner collapse*?
- **(d)** **Favorites only** (approve just your 5s): who wins — and what other method did this election just become?
- **(e)** Three thresholds, three winners — plus your two answers from (a). Write the moral: what exactly does the Approval ballot ask a voter to do, and who ends up holding the free parameter?

## Solutions

<details>
<summary><b>(a) Score says Ash; STAR says Cora</b></summary>

Totals: Ash 3×5 + 4×3 = **27**, Cora 2×3 + 4×5 = **26**, Beck 3×4 + 2×5 = **22**. Score voting: **Ash** by a point. STAR advances Ash and Cora — and the runoff asks a different question:

```text
Automatic Runoff Round
   Cora          -- 6 -- First place
   Ash           -- 3
 Cora wins.
   Cora 6 (67%) vs Ash 3 (33%); majority = 5.
```

**Cora**, two-to-one: Ash's 27 leans on four lukewarm 3s from Cora's own camp, and in a head-to-head those voters come home. (The engine prints its `[Runoff Reversal]` block — [exercise 8](ex08_build_a_reversal.md)'s breadth-vs-depth recipe in the wild. And a fun fact from the mirror: pairwise, Ash beats Beck, Beck beats Cora, and Cora beats Ash — a Condorcet cycle, so even the head-to-head standard shrugs at this electorate.)

</details>

<details>
<summary><b>(b) Approve 3+ — Ash, with 7 of 9</b></summary>

```text
   Ash  -- 7 (78%) -- Elected
   Cora -- 6 (67%)
   Beck -- 5 (56%)

[Approval Distribution]
   18 approvals across 9 ballots — average 2.0 of 3 (range 2–2).
```

Every voter approves exactly two candidates, and every tolerance counts: Ash collects his own camp *plus* all four "he's a 3" nods from Cora's camp. **Ash wins the generous room.**

</details>

<details>
<summary><b>(c) Approve 4+ — Beck, as the tolerances vanish</b></summary>

```text
   Beck -- 5 (56%) -- Elected
   Cora -- 4 (44%)
   Ash  -- 3 (33%)

[Approval Distribution]
   12 approvals across 9 ballots — average 1.3 of 3.
```

Raise the bar one point and six approvals evaporate — all of them tolerances (Ash's four 3s, Cora's two 3s). Ash crashes from first to last; the survivor is **Beck**, whose support was quietly *high-graded*: three 4s and two 5s all clear the stricter line. The average-approvals line is the psychology made visible: the room went from approving 2.0 candidates each to 1.3.

</details>

<details>
<summary><b>(d) Favorites only — Cora, and it's Choose-One in a costume</b></summary>

```text
   Cora -- 4 (44%) -- Elected
   Ash  -- 3 (33%)
   Beck -- 2 (22%)
```

Approve only your 5 and the "Approval election" is just **Choose-One plurality** — first-choice counts, 4-3-2. **Cora wins the stingy room.** (This is the devolution the Approval literature worries about in close races: when approving a second candidate feels like helping your favorite's rival, thresholds slide toward bullet voting — the same instinct [exercise 6](ex06_bullet_backfire.md) put on trial in STAR.)

</details>

<details>
<summary><b>(e) The moral — the ballot outsources its precision to the voter</b></summary>

One set of honest opinions produced **five defensible winners across five readings**: Ash (Score), Cora (STAR), Ash (approve-3+), Beck (approve-4+), Cora (favorites-only). Nothing was insincere anywhere — the Approval ballot simply asks each voter to *pre-aggregate* their own opinion into a yes/no, so the threshold is a free parameter the method never pins down. That is Approval's honest trade: maximal simplicity, bought by pushing the hard decision onto the voter — and it is why any "how often do STAR and Approval agree?" number depends on an assumed cutoff model ([the worked divergence study](../../method_comparisons/star_vs_approval_divergence.md); threshold strategy itself: [strategic voting](../../00_start_here/topics/strategic_voting.md)). A score ballot keeps the resolution and lets the *count* do the compressing; an approval ballot is a score ballot each voter compressed in their head.

</details>

## Reading this fairly

Engineered so the thresholds separate cleanly, and openly a *stress* case — in lopsided electorates all three lines elect the same person, and Approval's real-world record (Fargo, St. Louis) is genuinely good. The point is not "Approval is broken"; it is that the threshold is a real, outcome-bearing degree of freedom the ballot cannot see — a fact fair-minded Approval advocates state themselves. Symmetry per [the four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md): part (a) shows Score and STAR disagreeing on the very same opinions, so no method walks out of this exercise smug.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex13_opinions.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex13_approve3.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex13_approve4.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex13_bullet.yaml
```

Sources: [opinions (STAR)](ex13_opinions.yaml) · [approve 3+](ex13_approve3.yaml) · [approve 4+](ex13_approve4.yaml) · [favorites only](ex13_bullet.yaml). Full audit reports in [exercises_tabulated](exercises_tabulated/ex13_opinions_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast); the imposing-approvals-on-scores move follows Sullivan's *An Introduction to the Math of Voting Methods* (2022), ch. 5, which builds approval ballots from score ballots the same way. Concept homes: [Approval Voting](../../04_Approval/README.md) and [the STAR-vs-Approval divergence study](../../method_comparisons/star_vs_approval_divergence.md).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex13_draw_the_line.md
