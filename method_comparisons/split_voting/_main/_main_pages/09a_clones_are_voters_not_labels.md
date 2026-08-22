---
search:
  exclude: true
---

# Clones are made of voters, not labels — the sugar group splits, the fizzy group doesn't

*Generated from [`09a_clones_are_voters_not_labels.yaml`](../09a_clones_are_voters_not_labels.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Cola

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8xrpyp) · **[results ↗](https://bettervoting.com/8xrpyp/results)** (election `8xrpyp` · test `BV2295`).

## Scenario

Seven people, seven drinks, and two obvious ways to group them:

    Cola             fizzy   sugar        Diet Cola        fizzy   no sugar
    Root Beer        fizzy   sugar        Sparkling Water  fizzy   no sugar
    Lemonade         still   sugar        Unsweet Tea      still   no sugar
    Sweet Tea        still   sugar

Count first choices by label and the two groupings are EXACTLY THE SAME SIZE:
fizzy holds 4 of 7, sugar holds 4 of 7. Both are majorities. Both are spread
across four candidates. From the outside they are the same situation.

They are not. Choose-One elects DIET COLA on 2 of 7 (29%). The sugar majority
really did split and really did lose. The fizzy majority never split at all,
because it was never a bloc: a Diet Cola drinker does not want a Cola and
scores it a 1. "Fizzy" describes the drinks. It says nothing about who backs
them.

Under STAR the two sweet drinks take BOTH runoff slots, Cola beats Lemonade
4-3, and Diet Cola finishes fourth of seven in the scoring round.

This file declares the SUGAR grouping and the engine reports vote splitting.
Its twin, 09b, declares the FIZZY grouping over the identical ballots and the
engine reports no spoiler. Same election, same winner, opposite verdict — the
difference is not the arithmetic and not the size of the group, but whether the
same people actually back all of its members. Only the ballots can tell you
that, which is why no one can read a spoiler off a candidate list.
Live results: https://bettervoting.com/8xrpyp/results

## Parameters (from the YAML)

```yaml
blocs:
  Sugar (a real clone set): [Cola, Root Beer, Lemonade, Sweet Tea]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Cola,Root Beer,Lemonade,Sweet Tea,Diet Cola,Sparkling Water,Unsweet Tea
5,4,4,3,1,0,0   # cola, and anything sweet will do
4,5,3,3,1,0,0   # root beer, and anything sweet will do
3,2,5,4,0,1,0   # lemonade, and anything sweet will do
3,2,4,5,0,0,1   # sweet tea, and anything sweet will do
1,1,0,0,5,4,3   # diet cola - no sugar, thanks
1,0,0,0,5,3,4   # diet cola - no sugar, thanks
0,0,1,1,3,4,5   # unsweet tea - no sugar, thanks
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Cola
  Choose-One (Plurality) = Diet Cola   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Diet Cola 2, Cola 1, Root Beer 1, Lemonade 1, Sweet Tea 1, Unsweet Tea 1, Sparkling Water 0
  Plurality winner: Diet Cola (2, 28.6%)
  Bloc 'Sugar (a real clone set)' = Cola, Root Beer, Lemonade, Sweet Tea: combined 4 (57.1%); winner Diet Cola is OUTSIDE it.
  => VOTE SPLITTING: the 'Sugar (a real clone set)' bloc is an outright
     majority (4 vs Diet Cola's 2) but split across 4 candidates, so Diet
     Cola won Choose-One. STAR elected Cola.

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Cola,Root Beer,Lemonade,Sweet Tea,Diet Cola,Sparkling Water,Unsweet Tea
   5,        4,       4,        3,        1,              0,          0
   4,        5,       3,        3,        1,              0,          0
   3,        2,       5,        4,        0,              1,          0
   3,        2,       4,        5,        0,              0,          1
   1,        1,       0,        0,        5,              4,          3
   1,        0,       0,        0,        5,              3,          4
   0,        0,       1,        1,        3,              4,          5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cola            -- 17 -- First place
   Lemonade        -- 17 -- Second place
   Sweet Tea       -- 16
   Diet Cola       -- 15
   Root Beer       -- 14
   Unsweet Tea     -- 13
   Sparkling Water -- 12
 Cola and Lemonade advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cola            -- 4 -- First place
   Lemonade        -- 3
   Equal Support   -- 0
 Cola wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Cola 4 (57%)  ·  Lemonade 3 (43%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cola
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                        |       * Cola        |      Root Beer     |    * Lemonade      |      Sweet Tea     |      Diet Cola     |   Sparkling Water  |     Unsweet Tea    |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               * Cola > |         ---         |     4 - 2 - 1      |     4 - 0 - 3      |     4 - 0 - 3      |     4 - 0 - 3      |     4 - 0 - 3      |     4 - 0 - 3      |
            Root Beer > |      1 - 2 - 4      |        ---         |     2 - 2 - 3      |     3 - 1 - 3      |     4 - 0 - 3      |     4 - 0 - 3      |     4 - 0 - 3      |
           * Lemonade > |      3 - 0 - 4      |     3 - 2 - 2      |        ---         |     2 - 4 - 1      |     4 - 0 - 3      |     4 - 0 - 3      |     4 - 0 - 3      |
            Sweet Tea > |      3 - 0 - 4      |     3 - 1 - 3      |     1 - 4 - 2      |        ---         |     4 - 0 - 3      |     4 - 0 - 3      |     4 - 0 - 3      |
            Diet Cola > |      3 - 0 - 4      |     3 - 0 - 4      |     3 - 0 - 4      |     3 - 0 - 4      |        ---         |     4 - 1 - 2      |     4 - 1 - 2      |
      Sparkling Water > |      3 - 0 - 4      |     3 - 0 - 4      |     3 - 0 - 4      |     3 - 0 - 4      |     2 - 1 - 4      |        ---         |     2 - 2 - 3      |
          Unsweet Tea > |      3 - 0 - 4      |     3 - 0 - 4      |     3 - 0 - 4      |     3 - 0 - 4      |     2 - 1 - 4      |     3 - 2 - 2      |        ---         |

[Condorcet Winner]
  Condorcet Winner: Cola — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Sparkling Water — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate        5  4  3  2  1  0  | Total   Avg
Cola             1  1  2  0  2  1  |    17   2.4
Root Beer        1  1  0  2  1  2  |    14   2.0
Lemonade         1  2  1  0  1  2  |    17   2.4
Sweet Tea        1  1  2  0  1  2  |    16   2.3
Diet Cola        2  0  1  0  2  2  |    15   2.1
Sparkling Water  0  2  1  0  1  3  |    12   1.7
Unsweet Tea      1  1  1  0  1  3  |    13   1.9
```

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/09a_clones_are_voters_not_labels_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/09a_clones_are_voters_not_labels.yaml
```

## See also

- [Vote splitting (worked set)](../../README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
