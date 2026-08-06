# The cost of districting — when the best candidate wins no district at all

*Two chapters of one club elect a single national delegate. **Ana** is adored in Northside and unknown in Southside; **Beto** is the mirror image; **Cleo** is everybody's solid second. Count chapter by chapter and Cleo wins **neither** — so a delegate picked from the chapter winners is Ana or Beto. Count all nine members as one electorate and Cleo wins outright, and she is also the **highest-welfare** candidate in the race and the **Condorcet winner**. Nothing about the ballots changed. Only the map did.*

**Level: 301 · deep dive** The runnable companion to [distributed voting — the measured price of counting by district](../../07_Concepts/topics/distributed_voting_distortion.md), which is where the theorems live.

→ Its honest twin: [Exercise 1 — two districts, one mayor](../../01_STAR/05_Practice/ex01_two_districts.md), where districting costs **nothing** and the centralized count is the one that gives ground. Read the pair together or neither.

---

## The whole story in one table

Nine members, three candidates, scores 0–5. Every winner below is engine-verified from the three `cases/` files.

| Electorate | Ana | Beto | **Cleo** | STAR winner |
|---|:--:|:--:|:--:|:--:|
| **Northside** (5) | 23 | 0 | 19 | **Ana** |
| **Southside** (4) | 0 | 19 | 14 | **Beto** |
| **Both together** (9) | 23 | 19 | **33** | **Cleo** |

Cleo leads the combined field by ten points and wins neither half. That is not a paradox — it is arithmetic. Ana's 23 is concentrated in one chapter and Beto's 19 in the other, while Cleo's 33 is spread evenly across both. A district count reads *concentration*; a combined count reads *total*.

## The three counts

**Northside (5 members) — Ana wins.** [full report → `cases/cases_tabulated/districting_north_tabulated.txt`](cases/cases_tabulated/districting_north_tabulated.txt)

```text title="Abridged — scoring and runoff rounds only"
Scoring Round
   Ana           -- 23 -- First place
   Cleo          -- 19 -- Second place
   Beto          --  0
Automatic Runoff Round
   Ana           -- 3 -- First place
   Cleo          -- 2
```

**Southside (4 members) — Beto wins**, by the mirror image of the same shape. [full report → `cases/cases_tabulated/districting_south_tabulated.txt`](cases/cases_tabulated/districting_south_tabulated.txt)

```text title="Abridged — scoring and runoff rounds only"
Scoring Round
   Beto          -- 19 -- First place
   Cleo          -- 14 -- Second place
   Ana           --  0
Automatic Runoff Round
   Beto          -- 3 -- First place
   Cleo          -- 1
```

**Both chapters together (9 members) — Cleo wins.** [full report → `cases/cases_tabulated/districting_combined_tabulated.txt`](cases/cases_tabulated/districting_combined_tabulated.txt)

```text title="Abridged — scoring and runoff rounds only"
Scoring Round
   Cleo          -- 33 -- First place
   Ana           -- 23 -- Second place
   Beto          -- 19
Automatic Runoff Round
   Cleo          -- 6 -- First place
   Ana           -- 3
```

Cleo also beats both rivals head-to-head, so she is the **Condorcet winner** as well as the score leader — the two notions of "best" agree here, and the district map overrides both. Only Choose-One (Plurality) diverges from STAR on the combined ballots, electing Ana on first choices alone.

## What it costs

Read the score totals as the members' values and the welfare arithmetic is immediate. Cleo at 33 is the utilitarian optimum; whichever chapter winner the over-rule picks, the club is worse off:

| The delegate is… | Chosen by | Welfare (raw) | Distortion | Welfare (unit-sum) | Distortion |
|---|---|:--:|:--:|:--:|:--:|
| **Cleo** | counting all nine together | **33** | **1.00** | 3.9167 | **1.00** |
| Ana | the district map (Northside's winner) | 23 | 1.43 | 2.7639 | 1.42 |
| Beto | the district map (Southside's winner) | 19 | 1.74 | 2.3194 | 1.69 |

(Both columns because distortion is defined on unit-sum-normalized values, not raw scores. The ordering is identical either way, so nothing here turns on the normalization.)

The theory says a `k`-district architecture multiplies the worst-case welfare loss by `k`, and that the loss survives even when every district counts perfect utilities. This is that mechanism at `k = 2`, small enough to check by hand: **no ballot reform touches it**, because every district here already ran a full 0–5 score count and still discarded the best candidate. What went wrong was the requirement that the winner be *somebody's* district winner.

## Reading this fairly

A constructed example, and it shows — mirror-image chapters, three candidates, a candidate engineered to be everyone's second. It demonstrates the *mechanism* honestly; it says nothing about how often real district maps do this. Two guardrails, per [the four-part test](../paradoxes_and_whoops/reading_these_fairly.md):

- **The published experiments cut the other way.** On real-world data (the Jester dataset) the districting effect was far milder than the worst-case bound, because real electorates are **homogeneous** — when districts don't differ much, neither does the winner. The `k` is a worst case over adversarial partitions. A gerrymander is an adversarial partition; an ordinary map is not.
- **The library's other districting case shows the cost at zero.** In [Exercise 1](../../01_STAR/05_Practice/ex01_two_districts.md) the districted answer is the welfare optimum and the *centralized* STAR count is the one that gives up 13%. Both cases are real; neither is the general rule. That is the whole point of pairing them.

And this measures **welfare only**. Districts exist for representation, local accountability, and federalism — none of which distortion scores. "Districting has distortion Θ(km)" is an argument about one axis, not a verdict on districts.

## Run it yourself

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/districting_cost/cases/districting_combined.yaml
```

| Case | Ballots | Winner | Page | Source |
|---|:--:|---|---|---|
| Northside chapter | 5 | Ana | [page](cases/cases_pages/districting_north.md) | [yaml](cases/districting_north.yaml) |
| Southside chapter | 4 | Beto | [page](cases/cases_pages/districting_south.md) | [yaml](cases/districting_south.yaml) |
| Both together | 9 | **Cleo** | [page](cases/cases_pages/districting_combined.md) | [yaml](cases/districting_combined.yaml) |

## See also

- [Distributed voting — the measured price of counting by district](../../07_Concepts/topics/distributed_voting_distortion.md) — the theorems, the bounds table, and the sources
- [Distortion](../../07_Concepts/topics/distortion.md) — the parent metric
- [Exercise 1 — two districts, one mayor](../../01_STAR/05_Practice/ex01_two_districts.md) — the same architecture, opposite outcome
- [The reinforcement paradox, counted](../reinforcement_paradox/) — the criterion-shaped version of the same slicing
- [Summability](../../07_Concepts/topics/summability/README.md) — the *other* thing precincts do to a count, and the one this is constantly confused with
