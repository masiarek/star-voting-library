# Exercise 7 — The vanishing votes that never vanished (a park-tree ballot drill)

*Generated from [`ex07_vanishing_votes.yaml`](../ex07_vanishing_votes.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Aspen

## Scenario

A park board picks a tree. Nine ballot papers come back: two score the
finalists equal at the top (5-5), one at 3-3, one bullet-votes Cedar
(0,0,5), one is all zeros, one is completely blank — and only three
express a preference between the finalists Aspen and Birch. The drill:
predict every number in the two-line runoff summary before peeking.
Scoring round: Aspen 24, Birch 20, Cedar 13. Runoff: Aspen 2, Birch 1,
Equal Support 6 — "Voters with a preference: 3 of 9 (6 Equal Support)".
The 9 counts every tabulated ballot: the blank abstention folds into
Equal Support on this line, and the separate engine Note ("1 of 9
ballots is marked as an abstention") carries the cast-vs-abstained
split. No vote vanished: equal scores are counted in full in the
scoring round and then have no preference to give between equals.
Exercise: ex07_vanishing_votes.md. Ballots and cast are this repo's own.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Aspen,Birch,Cedar
5,5,0 # equal top pair — full weight in scoring, Equal Support in the runoff
5,5,3 # same, with a nod to Cedar
3,3,5 # Cedar first — and equal on the two finalists
5,2,0 # a clear Aspen preference
4,1,0 # a clear Aspen preference
2,4,0 # a clear Birch preference
0,0,5 # bullet vote for Cedar — zero on both finalists is still Equal Support
0,0,0 # all zeros — a CAST ballot that supports no one
-,-,- # completely blank — a true abstention, not a cast ballot
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots. Note: 1 of 9 ballots is marked as an abstention.
Aspen,Birch,Cedar
    5,    5,    0
    5,    5,    3
    3,    3,    5
    5,    2,    0
    4,    1,    0
    2,    4,    0
    0,    0,    5
    0,    0,    0
    -,    -,    -
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Aspen         -- 24 -- First place
   Birch         -- 20 -- Second place
   Cedar         -- 13
 Aspen and Birch advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Aspen         -- 2 -- First place
   Birch         -- 1
   Equal Support -- 6
 Aspen wins.
   Runoff math:
     9  ballots cast
   − 6  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Aspen 2 (67%)  ·  Birch 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Aspen
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Aspen   | * Birch   |   Cedar   |
-----------------------------------------------------
     * Aspen > |    ---     |2 - 6 - 1  |5 - 2 - 2  |
     * Birch > | 1 - 6 - 2  |   ---     |5 - 2 - 2  |
       Cedar > | 2 - 2 - 5  |2 - 2 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Aspen — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total   Avg
Aspen      3  1  1  1  0  2    1  |    24   3.0
Birch      2  1  1  1  1  2    1  |    20   2.5
Cedar      2  0  1  0  0  5    1  |    13   1.6
```

</details>

Everything in one file: the [`_tabulated` mirror](../exercises_tabulated/ex07_vanishing_votes_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex07_vanishing_votes.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../00_start_here/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
