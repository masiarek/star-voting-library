# Exercise 10 — Later-no-harm: the reticent ballots

*Generated from [`ex10_reticent.yaml`](../ex10_reticent.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Amir

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/g6q42v) · **[results ↗](https://bettervoting.com/g6q42v/results)** (election `g6q42v`).

## Scenario

Nine voters, three candidates. Amir's four fans withhold everything
below their favorite: Amir 5, Bess 0, Cato 0. Scoring round: Amir 24,
Cato 15, Bess 13 — Amir and Cato advance, and Amir wins the runoff 6-3.
The companion file ex10_generous.yaml reruns the election with those
fans scoring honestly (Amir 5, Bess 3, Cato 0): Bess reaches the runoff
instead and beats Amir 5-4. Scoring a later choice DID harm their
favorite — the later-no-harm failure STAR accepts by design. The
exercise asks which reading is right: did the generous 3s harm Amir, or
did the reticent 0s hide the consensus winner Bess? Exercise:
ex10_later_no_harm.md. Ballots and cast are this repo's own.
Live on BetterVoting (Test ID BV2195): https://bettervoting.com/g6q42v/results
— with an RCV-IRV race (also Amir). No Ranked Robin race on purpose:
the rank conversion of these sparse ballots yields a Condorcet cycle
whose 3-way tie BV resolves at random — not freezable.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amir,Bess,Cato
5,0,0 # 4 voters: Amir fans, scoring NOTHING below their favorite
5,0,0
5,0,0
5,0,0
2,5,0 # 2 voters: Bess first, mild nod to Amir
2,5,0
0,1,5 # 3 voters: Cato first, a token point to Bess
0,1,5
0,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Amir,Bess,Cato
    4 ×    5,   0,   0
    3 ×    0,   1,   5
    2 ×    2,   5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Amir          -- 24 -- First place
   Cato          -- 15 -- Second place
   Bess          -- 13
 Amir and Cato advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Amir          -- 6 -- First place
   Cato          -- 3
   Equal Support -- 0
 Amir wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Amir 6 (67%)  ·  Cato 3 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Amir
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Amir   |    Bess   |  * Cato   |
-----------------------------------------------------
      * Amir > |    ---     |4 - 0 - 5  |6 - 0 - 3  |
        Bess > | 5 - 0 - 4  |   ---     |2 - 4 - 3  |
      * Cato > | 3 - 0 - 6  |3 - 4 - 2  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Amir > Cato > Bess > Amir)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amir       4  0  0  2  0  3  |    24   2.7
Bess       2  0  0  0  3  4  |    13   1.4
Cato       3  0  0  0  0  6  |    15   1.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex10_reticent_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex10_reticent.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
