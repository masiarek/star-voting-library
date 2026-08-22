# Vote splitting & the spoiler effect

**Level: 101 → 301 · for voters**

*Seven friends pick one tub of ice cream. Four want chocolate, three want vanilla — and the chocolate four are split over which chocolate. Vanilla wins with three votes out of seven, and all four chocolate lovers had it dead last.*

*Nobody cheated. Nobody miscounted. Re-add the votes as often as you like.*

→ The concept in one page: [the spoiler effect](../../07_Concepts/topics/spoiler_effect.md) · teaching it to a room: [the presenter's plan](teaching_vote_splitting.md) · how often it really happens: [the 2022 count, read honestly](how_often_does_vote_splitting_happen.md)

---

## What it is

**Vote splitting** is what happens when two or more similar candidates draw on the same pool of supporters, and the ballot lets each voter back only one of them. The pool divides. A candidate that fewer people wanted can come first.

The **spoiler effect** is the outcome that produces: a candidate who *cannot win* changes *who does*. Note who the spoiler is — not the candidate who benefits, but the similar one whose presence divided the pool.

Two things follow that are worth having straight from the beginning:

- **It is not a counting error.** The first election below is counted perfectly. The trouble is upstream of the count.
- **It is not the voters' fault.** Nobody in these examples votes dishonestly or strategically. The ballot simply has nowhere to record what would have changed the result.

## Start here: the smallest one

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9cff2d) · **[results ↗](https://bettervoting.com/9cff2d/results)** (election `9cff2d`, Test ID **BV2296**)

Seven friends. Three flavours. One mark each.

<!-- report:08a_smallest_spoiler_plurality -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 7 ballots.

                                             Milk Chocolate  Dark Chocolate  Vanilla 
  milk chocolate, and dark would be fine too       X               -            -    
  milk chocolate, and dark would be fine too       X               -            -    
  dark chocolate, and milk would be fine too       -               X            -    
  dark chocolate, and milk would be fine too       -               X            -    
  vanilla                                          -               -            X    
  vanilla                                          -               -            X    
  vanilla                                          -               -            X    

  Count the marks:  Vanilla 3 · Milk Chocolate 2 · Dark Chocolate 2

Winner — Choose-One / Plurality Voting Method (single winner)
 Vanilla   (3 of 7 marks)
```
<!-- /report -->

Four of the seven wanted chocolate. They got vanilla.

Now hand the same seven friends a ballot that lets them score every flavour 0–5. Nobody changes their mind; the ballot just has room for what they already thought — *"I love milk chocolate, dark chocolate is nearly as good, vanilla is nothing to me."*

<!-- report:08b_smallest_spoiler_star -->
```text
[Divergence from STAR]
  STAR                   = Milk Chocolate
  Choose-One (Plurality) = Vanilla   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Vanilla 3, Milk Chocolate 2, Dark Chocolate 2
  Plurality winner: Vanilla (3, 42.9%)
  Bloc 'Chocolate' = Milk Chocolate, Dark Chocolate: combined 4 (57.1%); winner Vanilla is OUTSIDE it.
  => VOTE SPLITTING: the 'Chocolate' bloc is an outright majority (4 vs
     Vanilla's 3) but split across 2 candidates, so Vanilla won Choose-One.
     STAR elected Milk Chocolate.

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Milk Chocolate,Dark Chocolate,Vanilla
             5,             4,      0
             5,             3,      0
             4,             5,      0
             3,             5,      0
             0,             0,      5
             1,             0,      5
             2,             1,      5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Milk Chocolate -- 20 -- First place
   Dark Chocolate -- 18 -- Second place
   Vanilla        -- 15
 Milk Chocolate and Dark Chocolate advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Milk Chocolate -- 4 -- First place
   Dark Chocolate -- 2
   Equal Support  -- 1
 Milk Chocolate wins.
   Runoff math:
     7  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           Milk Chocolate 4 (67%)  ·  Dark Chocolate 2 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Milk Chocolate
```
<!-- /report -->

Watch where Vanilla lands: **last of three**, shut out of the runoff entirely, because both chocolates now reach it.

And read the runoff line carefully, because the obvious narration is wrong. The 4 is **not** "the chocolate four reunited" — those four split 2–2 between the two chocolates, exactly as they should, since they genuinely disagree about chocolate. The margin comes from two vanilla voters leaning mildly toward milk. The score ballot did not end the chocolate lovers' disagreement. **It stopped their disagreement costing them the election.**

Counted head-to-head ([`08c`](_main/_main_pages/08c_smallest_spoiler_ranked_robin.md)), **either** chocolate beats Vanilla 4–3. That is the majority Choose-One threw away.

> **The sentence this whole page exists to deliver:** Choose-One did not count those votes wrongly. **It never asked the question whose answer would have changed the result.**

## When does it actually bite?

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vq78wk) · **[results ↗](https://bettervoting.com/vq78wk/results)** (election `vq78wk`, Test ID **BV2293** — all seven races)

Here is the part most explanations skip, and skipping it is what makes the argument fall over the first time someone tests it.

Nine people choose one fruit for the office basket. Seven want an apple, two want a banana. **Their opinions never change.** All that changes is how many apple varieties are on the list.

| Rung | Names on the ballot | Choose-One result | Verdict |
|---|---|---|---|
| **1** · 2 names ([page](_main/_main_pages/07a_apples_two_candidates.md) · [run](_main/07a_apples_two_candidates.yaml)) | Gala · Banana | **Gala 7–2** (78%) | Nothing can split. At two candidates every reasonable method is majority rule. |
| **2** · 6 names ([page](_main/_main_pages/07b_apples_six_candidates.md) · [run](_main/07b_apples_six_candidates.yaml)) | + Granny Smith, Fuji, Honeycrisp, Red Delicious | **Gala 3**, Banana 2, four apples 1 each — **33%** | The apple vote splits **five ways** and it costs them **nothing.** |
| **3** · 8 names ([page](_main/_main_pages/07c_apples_full_menu.md) · [run](_main/07c_apples_full_menu.yaml)) | + Pink Lady, McIntosh | **Banana 2 of 9 — 22%** | Now it costs them everything. |

**Rung 2 is the load-bearing one.** A winner on 33%, the losers holding twice as much between them, the vote visibly divided — and nothing went wrong at all. Gala is the candidate every whole-ballot method elects on the full menu, and the Condorcet winner besides.

> **Splitting is not the same as being spoiled.** What matters is not whether a side divides, but whether it divides *far enough* that its largest piece drops below the rival's. "The winner got under 50%" is a **screening flag, not a finding.**

At rung 3, look at the two candidates who joined: **Pink Lady and McIntosh took one vote each.** Neither could win. Together they changed who did. That is precisely what the word *spoiler* means. (Add either one alone and the race deadlocks 2–2 rather than flipping — which is also why the ladder skips seven names.)

And the sharpest fact in the set: **Banana is the [Condorcet loser](../../07_Concepts/topics/condorcet/README.md)** — beaten head-to-head by every single apple. Choose-One elected the one candidate this electorate rejects in every pairing you can run.

## The fix is a ballot, not a brand

The same nine voters, the same eight names, four different ballots:

| Ballot | Method | Winner |
|---|---|---|
| Score 0–5 | [STAR](_main/_main_pages/07d_apples_full_menu_star.md) · [run](_main/07d_apples_full_menu_star.yaml) | **Gala** — Banana finishes *last of eight*; runoff 6–3 |
| Approve any number | [Approval](_main/_main_pages/07e_apples_full_menu_approval.md) · [run](_main/07e_apples_full_menu_approval.yaml) | **Gala**, 7 of 9 |
| Rank them | [RCV-IRV](_main/_main_pages/07f_apples_full_menu_irv.md) · [run](_main/07f_apples_full_menu_irv.yaml) | **Gala** |
| Rank them | [Ranked Robin](_main/_main_pages/07g_apples_full_menu_ranked_robin.md) · [run](_main/07g_apples_full_menu_ranked_robin.yaml) | **Gala** — 7–0 head-to-head |

**Say this plainly: RCV-IRV fixes this spoiler.** Ending the classic vote-splitting spoiler is what instant-runoff was built to do, and it does it here. Its own known failure is [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) — a *different* mechanism, where a broadly-liked compromise is eliminated for holding too few first choices — and this election is not an example of it.

What every one of these ballots has in common is not a brand. It is that each one **collects support for more than one candidate**, so a voter is never forced to choose between allies.

## Four things that are not true

**"A winner under 50% means the election was spoiled."** No — see rung 2, and the deliberate control case: [`06`](_main/_main_pages/06_sub_majority_not_spoiled.md), a 41% winner that every method confirms. Same warning signs, opposite verdict. Telling them apart needs preference data, which a one-mark ballot never collects.

**"STAR and Approval are immune to vote splitting."** Overstated, and this repo's own case files say so — for *both* of them. They remove **forced** splitting: you are never made to choose between allies. A faction can still split *itself* by declining to support one.

- **STAR** — [`05a`](_main/_main_pages/05a_residual_split_bullet-voting.md): a 60% side bullet-votes its own allies apart and hands the seat to a 40% opponent. [`05b`](_main/_main_pages/05b_residual_split_expressive-fix.md) is the cure — score the ally even a 3 and the split vanishes.
- **Approval** — the **Burr dilemma**, named for the 1800 Jefferson–Burr tie. Honest cooperation leaves two allies [tied 60–60](../chicken_dilemma/cases/cases_pages/chicken_approval.md), so each is tempted to bullet-vote; when [both sides defect](../chicken_dilemma/cases/cases_pages/chicken_approval_both_defect.md), the same 60% majority loses to the same 40% opponent. The threshold is concrete: C only takes the lead once **more than 20** of A's 35 supporters *and* **more than 20** of B's 25 defect — it is defection becoming general, not one defector, that does it.

The difference from choose-one is that the remedy is in the voters' hands. That is a real difference and worth defending. It is not immunity, and neither method should be sold as immune. Full set: [the chicken / Burr dilemma](../chicken_dilemma/README.md).

**"You can tell which candidates will split by reading the ballot."** You cannot — and this is the deepest point on the page.

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8xrpyp) · **[results ↗](https://bettervoting.com/8xrpyp/results)** (election `8xrpyp`, Test ID **BV2295**)

Seven people, seven drinks, and two obvious groupings. *Fizzy* holds 4 of 7 first choices. *Sugar* holds 4 of 7. Identical headcount. Choose-One elects **Diet Cola on 29%** — and the sugar majority is the one that split and lost. The fizzy majority never split, because it was never a bloc: a Diet Cola drinker doesn't want a Cola, and scores it a 1.

[`09a`](_main/_main_pages/09a_clones_are_voters_not_labels.md) and [`09b`](_main/_main_pages/09b_same_ballots_grouped_by_label.md) are **byte-identical elections** differing only in which grouping they declare, and the engine returns opposite verdicts on the same seven ballots. **A clone set is made of voters, not categories** — and only the ballots can say which is which.

**"This is a third-party problem."** It is a problem for *any* two similar candidates, which most often means two candidates of the same party in a primary. Framing it as third parties understates it considerably.

## What it does before anyone votes

The arithmetic above is the setup. The damage is behavioural:

1. **Voters abandon their favourite.** "Don't waste your vote" is not cynicism — under choose-one it is *correct advice*, which is what makes it corrosive. → [favorite betrayal](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md)
2. **Parties ration candidates.** Clearing the field, early endorsements, pressuring people out of primaries — all rational defence against splitting, and all of it narrows what voters get to choose from.
3. **Good candidates never run at all.** The deepest harm, and the only one that leaves no trace in any result sheet. It cannot be measured, which is exactly why it goes unmentioned — say it as a structural incentive, never as a statistic.

## Every case in this folder

Run any of them:

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/08a_smallest_spoiler_plurality.yaml
```

Files declaring a `blocs:` group get the engine's `[Vote-splitting check]`, which states the verdict in numbers.

| Case | Field | The job |
|---|:--:|---|
| [`00` Plurality vs majority](_main/_main_pages/00_plurality_vs_majority.md) | 3 | "Most votes" and "over half" are different bars — where the gap lives |
| [`01` Political left split](_main/_main_pages/01_political_left_split.md) | 4 | A 66% coalition splits three ways; a 34% Conservative wins |
| [`02` Ice cream, chocolate split](_main/_main_pages/02_icecream_chocolate_split.md) | 4 | The 100-voter version, when you want percentages |
| [`03` Lunch: veggie vs meat](_main/_main_pages/03_lunch_veggie_vs_meat.md) | 4 | A 70% veggie majority loses to one burger |
| [`04` Star Wars](_main/_main_pages/04_star_wars_vote_split.md) | 3 | Skywalker and Leia split the Rebel vote |
| [`05a`](_main/_main_pages/05a_residual_split_bullet-voting.md) → [`05b`](_main/_main_pages/05b_residual_split_expressive-fix.md) | 3 | **STAR's own residual split**, and its cure |
| [`06` Sub-majority, not spoiled](_main/_main_pages/06_sub_majority_not_spoiled.md) | 3 | **The control.** A 41% winner nothing spoiled |
| [`07a`](_main/_main_pages/07a_apples_two_candidates.md) · [`07b`](_main/_main_pages/07b_apples_six_candidates.md) · [`07c`](_main/_main_pages/07c_apples_full_menu.md) | 2 → 6 → 8 | **The ladder.** One electorate, three ballot sizes, 78% → 33% → 22% |
| [`07d`](_main/_main_pages/07d_apples_full_menu_star.md) · [`07e`](_main/_main_pages/07e_apples_full_menu_approval.md) · [`07f`](_main/_main_pages/07f_apples_full_menu_irv.md) · [`07g`](_main/_main_pages/07g_apples_full_menu_ranked_robin.md) | 8 | The same nine voters under four expressive ballots — all elect Gala |
| [`08a`](_main/_main_pages/08a_smallest_spoiler_plurality.md) · [`08b`](_main/_main_pages/08b_smallest_spoiler_star.md) · [`08c`](_main/_main_pages/08c_smallest_spoiler_ranked_robin.md) | 3 | **The smallest spoiler.** Seven ballots — the 101 set-piece |
| [`09a`](_main/_main_pages/09a_clones_are_voters_not_labels.md) · [`09b`](_main/_main_pages/09b_same_ballots_grouped_by_label.md) | 7 | Two same-size groupings, opposite verdicts, identical ballots |

**Elsewhere in the repo:** [the pineapple progression](../minority_winner_progression/README.md) — **11 toppings, an 11% winner**, the large-field version · [the crowded field](../crowded_field/README.md) — at 7 candidates, four methods elect four different people · [minority winner](../minority_winner/README.md) — the canonical 34% case · [food-truck row](../food_truck_row/README.md) — multi-seat, where a 57% majority takes **zero of two seats** · [recruit a spoiler](../../01_STAR/05_Practice/ex11_recruit_a_spoiler.md) — the attack as a strategy exercise.

## Verification

The three live elections here — **BV2293** `vq78wk`, **BV2295** `8xrpyp`, **BV2296** `9cff2d` — are cross-checked race by race: **BetterVoting's own tabulator agrees with the LH engine on all twelve**, and both Ranked Robin results are confirmed a third time by [`pref_voting`](../../07_Concepts/tabulation_engines/README.md)'s independent Copeland implementation. Frozen exports sit beside the case files as `bv*_bv_export.json`.

Cases `00`–`06` are **LH-only**: their teaching contrast is Plurality vs STAR, not BetterVoting vs LH, and the two engines agree — so a BV screenshot would only duplicate the numbers already on the page.
