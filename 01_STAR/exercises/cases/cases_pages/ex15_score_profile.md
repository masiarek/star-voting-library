# Exercise 15b — a 0–5 score profile (which method is this?)

*Generated from [`ex15_score_profile.yaml`](../ex15_score_profile.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../concepts) · **1 seat** · **Expected winner:** Clara

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/tfm64p) · **[results ↗](https://bettervoting.com/tfm64p/results)** (election `tfm64p`).

## Scenario

Part (b) of Exercise 15 — "Read the ballot, name the method."

Four voters rate four candidates 0-5, each candidate judged on its own scale
with no ordering required. That is a CARDINAL ballot, and adding the columns
is SCORE VOTING (aka Range): Clara 19, Diego 13, Bruno 11, Alice 7. Clara
wins.

The file runs as STAR because the teaching CLI has no first-class
voting_method: Score — and that turns out to be the useful part. STAR's
Scoring Round IS the score-voting tally, so the totals printed below are the
Score result; the runoff is the extra step Score doesn't take. Here it
changes nothing: Clara also wins the runoff 4-0, is the Condorcet winner, and
the engine prints no [Divergence from STAR] block at all because every method
agrees.

Kept deliberately: an election where nothing diverges is a fair baseline for
a library full of elections that do. Clara is scored top or joint-top by all
four voters, so there is no question for a method to disagree about.

A textbook-style prompt, rebuilt with named candidates so the rows line up
A/B/C/D -> Alice/Bruno/Clara/Diego. Part (a) is ex15_approval_yes_no.yaml.

Exercise page: ../ex15_read_the_ballot.md
Live results: https://bettervoting.com/tfm64p/results (BV2259 — BetterVoting's
own STAR count agrees: Clara.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Bruno,Clara,Diego
0,2,5,4   # voter 1
3,5,5,3   # voter 2
0,1,5,4   # voter 3
4,3,4,2   # voter 4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 4 ballots.
Alice,Bruno,Clara,Diego
    0,    2,    5,    4
    3,    5,    5,    3
    0,    1,    5,    4
    4,    3,    4,    2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Clara         -- 19 -- First place
   Diego         -- 13 -- Second place
   Bruno         -- 11
   Alice         --  7
 Clara and Diego advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Clara         -- 4 -- First place
   Diego         -- 0
   Equal Support -- 0
 Clara wins.
   Runoff math:
     4  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     4  voters with a preference  (majority = 3)
           Clara 4 (100%)  ·  Diego 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Clara
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    Alice   |   Bruno   | * Clara   | * Diego   |
-----------------------------------------------------------------
       Alice > |    ---     |1 - 0 - 3  |0 - 1 - 3  |1 - 1 - 2  |
       Bruno > | 3 - 0 - 1  |   ---     |0 - 1 - 3  |2 - 0 - 2  |
     * Clara > | 3 - 1 - 0  |3 - 1 - 0  |   ---     |4 - 0 - 0  |
     * Diego > | 2 - 1 - 1  |2 - 0 - 2  |0 - 0 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Clara — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Alice — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alice      0  1  1  0  0  2  |     7   1.8
Bruno      1  0  1  1  1  0  |    11   2.8
Clara      3  1  0  0  0  0  |    19   4.8
Diego      0  2  1  1  0  0  |    13   3.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex15_score_profile_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex15_score_profile.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md) · [ex15_approval_pairwise](ex15_approval_pairwise.md) · [ex15_approval_yes_no](ex15_approval_yes_no.md)
