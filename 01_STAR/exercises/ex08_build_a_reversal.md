# Exercise 8 — Build your own runoff reversal

*Every exercise so far handed you the ballots. This one doesn't. Your task: **construct** an election where the scoring-round leader loses the automatic runoff — STAR's famous "top scorer ≠ winner" behavior ([Runoff Reversal](../runoff_overturns_leader/README.md)) — using as few voters and candidates as you can. Then prove your example is as small as possible.*

**You practice:** designing elections instead of reading them — the fastest way to *own* the two-rounds mechanic. (House rules for good examples: [choosing voter counts](../../00_start_here/tips/TIPS_choosing_voter_counts.md).)

## Your task

- **(a)** Build a reversal: ballots where candidate X tops the score totals and candidate Y wins the runoff. Constraints: at most 4 candidates, at most 6 voters, whole-number scores 0–5, no ties anywhere (scores or runoff). Verify by hand, then run it through the engine and look for the `[Runoff Reversal]` block.
- **(b)** Extract the recipe: in *any* reversal, what must be true about how the score leader's points arrive, and about the other finalist's support?
- **(c)** How small can a reversal possibly be? Find the minimum number of voters (with 2 candidates), and prove nothing smaller works.
- **(d)** Your construction shows Score voting and STAR disagreeing. Someone calls that "a malfunction — the people's favorite lost." Give the two-sided answer.

## Solutions

<details>
<summary><b>(a) A sample solution (3 candidates, 5 voters)</b></summary>

| | ×3 voters | ×2 voters |
|---|:---:|:---:|
| **A** | 5 | 0 |
| **B** | 4 | 5 |
| **C** | 0 | 1 |

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   B             -- 22 -- First place
   A             -- 15 -- Second place
   C             --  2
 B and A advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   B             -- 2
   Equal Support -- 0
 A wins.
   Voters with a preference: 5 of 5 (no Equal Support).
   A 3 (60%) vs B 2 (40%); majority = 3.
```

B piles up 22 points — every single voter gives B a 4 or 5 — yet a 3-of-5 **majority scores A above B**, so A wins the runoff. The engine prints its `[Runoff Reversal]` block and the standard "not a malfunction" note. (Runnable: [ex08_minimal_reversal_3c.yaml](ex08_minimal_reversal_3c.yaml).)

</details>

<details>
<summary><b>(b) The recipe</b></summary>

A reversal needs exactly one tension, visible in the sample's columns:

- the score leader's total is built on **breadth**: high-but-not-top scores from many voters (B's three friendly 4s), and
- the runoff winner has **depth**: a *majority of decided voters* who rank them strictly higher, however thin their extra points are (A's three 5-over-4s are worth just one point each in the totals, but one full vote each in the runoff).

Squeeze those two facts together — every voter generous to B, a majority still preferring A — and the two rounds *must* disagree. That's the general shape of every case in the [Runoff Reversal set](../runoff_overturns_leader/README.md), from 5 voters to 100.

</details>

<details>
<summary><b>(c) The minimum: 3 voters, 2 candidates — and why 2 voters can't work</b></summary>

| | ×2 voters | ×1 voter |
|---|:---:|:---:|
| **A** | 5 | 0 |
| **B** | 4 | 5 |

Totals: B 13, A 10 — B leads. Runoff: the two A-first voters outvote the one B-only voter, 2–1 — **A wins**. ([ex08_minimal_reversal_2c.yaml](ex08_minimal_reversal_2c.yaml); with two candidates the finalist matrix is trivial, so the file follows house style and turns it off.)

**Why not 2 voters?** For a reversal you need a strict runoff majority for A (with 2 voters that means *both* prefer A — 1–1 is a tie, which the constraints forbid) *and* a strict score lead for B. But if both voters score A above B, then A's total is strictly larger on each ballot, so A leads the sum too — contradiction. One voter is a contradiction even faster. So **3 voters is the floor**, and 2 candidates is the floor by definition. You cannot make this phenomenon smaller.

</details>

<details>
<summary><b>(d) "The people's favorite lost!" — the two-sided answer</b></summary>

Side one: B is the favorite only under one specific definition — *sum of scores*. Under the equally natural definition *preferred by the majority*, A is the favorite, 3 votes to 2; "the score leader" and "the people's favorite" quietly beg the question. Side two, conceded honestly: the reversal *does* surprise people, and Score advocates genuinely prefer the totals verdict — this is a real philosophical fork ([three winner notions](../../00_start_here/STAR_Voting/properties_and_limits/STAR_three_winner_notions.md)), not an arithmetic error, and STAR takes the majoritarian branch *by design* ([the second-round FAQ](../../00_start_here/STAR_Voting/the_count/STAR_second_round_FAQ.md)). What you built is the disagreement in its smallest possible form; [exercise 4](ex04_olympics_1994.md) is the same fork on real Olympic ballots.

</details>

## Reading this fairly

A construction exercise *is* the four-part test's second rule in action: everything here is engineered and says so. The value isn't frequency evidence — it's that after building one, you can no longer mistake the reversal for a bug: you had to *cause* it, breadth against depth, on purpose.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex08_minimal_reversal_2c.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex08_minimal_reversal_3c.yaml
```

Sample solutions: [ex08_minimal_reversal_2c.yaml](ex08_minimal_reversal_2c.yaml) · [ex08_minimal_reversal_3c.yaml](ex08_minimal_reversal_3c.yaml). Full audit reports: [2-candidate](exercises_tabulated/ex08_minimal_reversal_2c_tabulated.txt) · [3-candidate](exercises_tabulated/ex08_minimal_reversal_3c_tabulated.txt).

---

**Where this comes from.** Original to this repo; the constructive format follows the "modify the ballots so that…" exercises in Brendan W. Sullivan, *An Introduction to the Math of Voting Methods* (2022), ch. 5. Candidates are bare A/B/C on purpose — in a pure construction the names are noise (the house naming rule's one sanctioned exception).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex08_build_a_reversal.md
