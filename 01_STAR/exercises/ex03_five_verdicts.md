# Exercise 3 — One electorate, five verdicts

*An office votes on the snack to stock: Apple, Banana, or Cherry. Nine people fill in one score ballot each — and then the count is run five different ways. How many different winners can one small electorate produce? Commit to a number before you start.*

**You practice:** reading one electorate through five tabulations — [Choose-One](../../00_start_here/topics/plurality.md), RCV-IRV, Approval, Score, and STAR — and the core lesson that **the method, not the ballot, picks the winner** ([ballot vs count](../../00_start_here/topics/rcv_irv_vs_star.md)).

Work each part on paper before opening its solution. The YAML at the bottom is runnable; its `expected_winners` key is regression-tested, and the `_tabulated` mirror is the full audit report.

## The ballots

Nine voters, three snacks, scores 0–5 (rows are candidates, columns are voter blocs):

| | ×4 voters | ×3 voters | ×2 voters |
|---|:---:|:---:|:---:|
| **Apple** | 5 | 0 | 0 |
| **Banana** | 0 | 5 | 1 |
| **Cherry** | 3 | 4 | 5 |

For the ranked methods, read each column top-to-bottom by score (the ×4 bloc ranks Apple > Cherry > Banana, and so on). For Approval, use the bridge rule **approve = score 3 or higher**.

## Your task

- **(a) Choose-One:** each voter marks only their favorite. Who wins?
- **(b) RCV-IRV:** rank by scores, eliminate the last-place candidate, transfer, recount. Who wins?
- **(c) Approval** (approve = 3+): who wins, and with what share of the 9 voters?
- **(d) Score:** add the points. Who wins?
- **(e) STAR:** two finalists, then the automatic runoff. Who wins, and by what margin?
- **(f)** Tally your verdicts. What is the *strongest* thing you can say against the Choose-One winner from these same ballots?

## Solutions

<details>
<summary><b>(a) Choose-One — Apple</b></summary>

First choices: Apple 4, Banana 3, Cherry 2. **Apple wins** with 44% — and a majority of the office (5 of 9) scored Apple a flat zero. This is the [wasted-votes](../../00_start_here/topics/wasted_votes.md) baseline every other method is reacting to.

</details>

<details>
<summary><b>(b) RCV-IRV — Banana</b></summary>

First-choice ranks: Apple 4, Banana 3, Cherry 2 → **Cherry is eliminated first** (fewest firsts). Cherry's two voters transfer to Banana (they scored Banana 1 > Apple 0), so the final round is Apple 4 vs Banana 5. **Banana wins.** Note what just happened to Cherry — scored 3+ by all nine voters, eliminated before anyone looked: the same squeeze mechanism as [exercise 5](ex05_center_squeeze.md).

</details>

<details>
<summary><b>(c) Approval — Cherry, unanimously</b></summary>

Approve = 3+: the ×4 bloc approves {Apple, Cherry}, the ×3 bloc {Banana, Cherry}, the ×2 bloc {Cherry}. Totals: **Cherry 9 of 9**, Apple 4, Banana 3. The candidate with the *fewest* first choices carries *every single voter* — that's the information Choose-One throws away. (More on the bridge rule and its lean: [Approval Voting](../../00_start_here/Approval_Voting/README.md).)

</details>

<details>
<summary><b>(d) Score — Cherry</b></summary>

Apple 4×5 = **20**, Banana 3×5 + 2×1 = **17**, Cherry 4×3 + 3×4 + 2×5 = **34** of a possible 45. **Cherry wins** going away.

</details>

<details>
<summary><b>(e) STAR — Cherry, 5–4</b></summary>

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Cherry        -- 34 -- First place
   Apple         -- 20 -- Second place
   Banana        -- 17
 Cherry and Apple advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Cherry        -- 5 -- First place
   Apple         -- 4
   Equal Support -- 0
 Cherry wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Cherry 5 (56%) vs Apple 4 (44%); majority = 5.
```

**Cherry wins** — and unlike Score's bare total, the runoff line shows Cherry beating the Choose-One winner head-to-head, 5 voters to 4.

</details>

<details>
<summary><b>(f) The tally — and the verdict on Apple</b></summary>

| Method | Winner |
|---|---|
| Choose-One | **Apple** |
| RCV-IRV | **Banana** |
| Approval | **Cherry** |
| Score | **Cherry** |
| STAR | **Cherry** |
| Ranked Robin | **Cherry** |

Three different winners from one electorate (the engine's `[Divergence from STAR]` block prints exactly this on screen). The strongest statement against Apple: **Apple is the [Condorcet loser](../../00_start_here/GLOSSARY.md)** — Apple loses head-to-head to Cherry (4–5) *and* to Banana (4–5), yet Choose-One elects it. Cherry, meanwhile, is the Condorcet winner. Which verdict is "right" is a genuine question with three defensible answers — see [three winner notions](../../00_start_here/STAR_Voting/properties_and_limits/STAR_three_winner_notions.md) — but "the candidate a majority beats head-to-head twice over" is a hard winner to defend.

</details>

## Reading this fairly

Engineered, and openly so: the ballots are built so the verdicts fan out (a real electorate this small usually agrees with itself). The point is not "Choose-One always does this" — it is that *the ballots alone don't determine the winner*, so arguing about methods is arguing about which information gets counted. The [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) applies before any of these verdicts becomes a talking point.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex03_five_verdicts.yaml
```

Source: [ex03_five_verdicts.yaml](ex03_five_verdicts.yaml). Full audit report: [mirror](exercises_tabulated/ex03_five_verdicts_tabulated.txt).

---

**Where this comes from.** The one-electorate-many-methods format follows the worked comparisons in Brendan W. Sullivan, *An Introduction to the Math of Voting Methods* (619 Wreath Publishing, 2022), ch. 5 (his Indian/Pizza/Thai running example, where the Plurality loser sweeps the cardinal methods); the ballots and cast here are this repo's own, built on the STAR 0–5 scale.

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex03_five_verdicts.md
