# Exercise 11 — Recruit a spoiler: Axl enters the race

*Generated from [`ex11_spoiler_added.yaml`](../ex11_spoiler_added.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Alba

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/93gjx6) · **[results ↗](https://bettervoting.com/93gjx6/results)** (election `93gjx6`).

## Scenario

The same nine voters as ex11_two_way_base.yaml, plus a third name on
the ballot: Axl, a near-clone of Alba (recruited, in the exercise's
story, by Brett's campaign to split Alba's vote). Alba's five-voter
camp splits its FIRST choices 3-2 between the clones but scores both
4-5; Brett's four voters are unchanged. Choose-One now elects BRETT
(4 first choices vs 3 and 2) — the spoiler worked. STAR shrugs:
scoring round Alba 23, Axl 22, Brett 20 — the CAMP keeps both finalist
slots and the runoff is Alba vs Axl, which Alba wins 3-2 (Brett's four
voters score the clones 0-0: Equal Support). RCV-IRV also survives
this one: Axl is eliminated first and his votes come home to Alba —
crowding by pure clones is the one spoiler variant IRV genuinely
handles. The dirty trick only pays under Choose-One. (Axl shares
Alba's initial ON PURPOSE — they are clones; the distinct-initials
naming rule yields to the lesson here.) Exercise:
ex11_recruit_a_spoiler.md. Ballots and cast are this repo's own.
Live on BetterVoting (Test ID BV2198): https://bettervoting.com/93gjx6/results
— four races: Choose-One falls for the clone (Brett); RCV-IRV, STAR,
and Ranked Robin all hold (Alba).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alba,Axl,Brett
5,4,0 # 3 voters: Alba's camp, Alba first among the clones
5,4,0
5,4,0
4,5,0 # 2 voters: Alba's camp, Axl first among the clones
4,5,0
0,0,5 # 4 voters: Brett's camp, unchanged
0,0,5
0,0,5
0,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Alba
  Choose-One (Plurality) = Brett   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Alba,Axl,Brett
    4 ×    0,  0,    5
    3 ×    5,  4,    0
    2 ×    4,  5,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alba          -- 23 -- First place
   Axl           -- 22 -- Second place
   Brett         -- 20
 Alba and Axl advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alba          -- 3 -- First place
   Axl           -- 2
   Equal Support -- 4
 Alba wins.
   Runoff math:
     9  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Alba 3 (60%)  ·  Axl 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alba
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Alba   |  * Axl    |   Brett   |
-----------------------------------------------------
      * Alba > |    ---     |3 - 4 - 2  |5 - 0 - 4  |
       * Axl > | 2 - 4 - 3  |   ---     |5 - 0 - 4  |
       Brett > | 4 - 0 - 5  |4 - 0 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Alba — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alba       3  2  0  0  0  4  |    23   2.6
Axl        2  3  0  0  0  4  |    22   2.4
Brett      4  0  0  0  0  5  |    20   2.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex11_spoiler_added_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex11_spoiler_added.yaml
```

## See also

- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
