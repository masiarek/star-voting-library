# Exercise 7 — The vanishing votes that never vanished

*A park board votes on which tree to plant. Nine ballot papers come back — two score the top pair equal, one bullet-votes Cedar, one is all zeros, one is completely blank. The runoff summary then announces: "Voters with a preference: 3 of 9." A board member stands up: "Six votes just vanished!" Your job: predict every number on that summary line before you see it — and then answer the board member.*

**You practice:** reading STAR's two-line runoff summary — the **decided-voters denominator**, **[Equal Support](../../00_start_here/GLOSSARY.md)**, and the difference between a *zero*, an *equal score*, and a *blank* (see [Two Denominators, One Winner](../../00_start_here/STAR_Voting/the_count/runoff_percentages.md)).

Work each part on paper before opening its solution. The YAML at the bottom is runnable; its `expected_winners` key is regression-tested, and the `_tabulated` mirror is the full audit report.

## The ballots

Three trees, nine ballot papers, one row per voter (`-` = left blank):

| # | Aspen | Birch | Cedar | the voter's story |
|:---:|:---:|:---:|:---:|---|
| 1 | 5 | 5 | 0 | loves both front-runners equally |
| 2 | 5 | 5 | 3 | same, with a nod to Cedar |
| 3 | 3 | 3 | 5 | Cedar first, equal on the other two |
| 4 | 5 | 2 | 0 | clear Aspen preference |
| 5 | 4 | 1 | 0 | clear Aspen preference |
| 6 | 2 | 4 | 0 | clear Birch preference |
| 7 | 0 | 0 | 5 | bullet vote for Cedar |
| 8 | 0 | 0 | 0 | turned in all zeros |
| 9 | – | – | – | completely blank |

## Your task

- **(a)** Scoring round: compute all three totals (what do `-` and `0` contribute?). Who are the finalists?
- **(b)** For each of the nine ballots, say what it does in the runoff: counts for Aspen, counts for Birch, or Equal Support.
- **(c)** Now write the summary line yourself: *"Voters with a preference: __ of __ (__ Equal Support)"* — and the percentages.
- **(d)** Ballot 7 scored both finalists zero and ballot 9 is blank. Do they land in the same buckets everywhere? Where does the count tell them apart?
- **(e)** Answer the board member, in two sentences, using only numbers from the report.

## Solutions

<details>
<summary><b>(a) Scoring round — Aspen 24, Birch 20, Cedar 13</b></summary>

Both `-` and `0` contribute zero stars to the totals (the engine prints exactly that note). Aspen 5+5+3+5+4+2 = **24**, Birch 5+5+3+2+1+4 = **20**, Cedar 3+5+5 = **13**. **Aspen and Birch advance** — ballot 7's bullet 5 counted at full weight toward Cedar's 13; it just wasn't enough to make Cedar a finalist.

</details>

<details>
<summary><b>(b) Ballot by ballot</b></summary>

Aspen-vs-Birch verdicts: ballots **4, 5 → Aspen**; ballot **6 → Birch**; ballots **1, 2, 3, 7, 8, 9 → Equal Support** (1 and 2 at 5–5, 3 at 3–3, 7 and 8 at 0–0, and the blank 9 scores no one). Note the range inside "Equal Support": loving both equally, rating both mid, supporting *neither*, and abstaining entirely all land in the same runoff bucket — because between *these two finalists* they express exactly the same thing: no preference.

</details>

<details>
<summary><b>(c) The summary line</b></summary>

```text
Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Aspen         -- 2 -- First place
   Birch         -- 1
   Equal Support -- 6
 Aspen wins.
   Voters with a preference: 3 of 9 (6 Equal Support).
   Aspen 2 (67%) vs Birch 1 (33%); majority = 2.
```

**3 of 9, with 6 Equal Support** — and the line self-reconciles: 3 + 6 = 9. If you wrote "3 of 8 (5 Equal Support)", you tracked the *cast* ballots — a perfectly good instinct, and exactly the trap: on this line the engine counts every **tabulated** ballot, blank included, and reports the cast-vs-abstained split separately (the tabulation header prints *"Note: 1 of 9 ballots is marked as an abstention"*). Percentages use the decided voters only: Aspen 2 of 3 = 67%.

</details>

<details>
<summary><b>(d) Zero vs blank — same bucket here, different everywhere else</b></summary>

In *this* runoff they coincide (both Equal Support), but the count still tells them apart. Ballot 7 is a **cast vote**: its Cedar 5 counted in the scoring round, and had Cedar been a finalist, ballot 7 would have had a preference to give. Ballot 9 is a **true abstention**: it contributed nothing anywhere and is flagged by the abstention note — it exists so turnout-style questions ([quorum](../../00_start_here/topics/quorum.md)) can be answered honestly. Zero is an opinion; blank is the absence of one. (Canonical tiny demo: [the abstentions example](../../01_STAR/_main/_main_pages/abstentions.md).)

</details>

<details>
<summary><b>(e) Answering "six votes vanished!"</b></summary>

"All nine papers were counted — every score they contain is in the totals that chose the finalists (Cedar's 13 includes the bullet vote). Six of them scored Aspen and Birch *equally*, so in an Aspen-vs-Birch runoff they have no preference to express — the report says so on its face: 3 of 9 with a preference, 6 Equal Support, 3 + 6 = 9." Nothing vanished; the deeper treatment of why an equal-scores ballot is a *counted voice*, not a discount, is [Aren't equal-score votes discounted?](../../00_start_here/STAR_Voting/reference/are_equal_score_votes_discounted.md)

</details>

## Reading this fairly

No paradox here at all — this drill exists because the *reporting* is where real elections win or lose trust, and "votes vanished" is the most common misreading of any runoff summary. The two-denominator design (count everything in the scoring round; state the decided-voter split with Equal Support named inline) is precisely the answer to it.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex07_vanishing_votes.yaml
```

Source: [ex07_vanishing_votes.yaml](ex07_vanishing_votes.yaml). Full audit report: [mirror](exercises_tabulated/ex07_vanishing_votes_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast); the concept homes are [Two Denominators, One Winner](../../00_start_here/STAR_Voting/the_count/runoff_percentages.md) and the [equal-score votes FAQ](../../00_start_here/STAR_Voting/reference/are_equal_score_votes_discounted.md).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex07_vanishing_votes.md
