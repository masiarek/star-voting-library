# Exercise 1 — Two districts, one mayor: the COMBINED city

*Generated from [`ex01_district_combined.yaml`](../ex01_district_combined.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Carmen

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/923q3d) · **[results ↗](https://bettervoting.com/923q3d/results)** (election `923q3d`).

## Scenario

All 18 ballots — West and East together. Both districts separately elect
Avery, but combined the runner-ups change: Blake (33) only exists in West and
Diego (33) only in East, while Carmen scores 32 in BOTH — so citywide it is
Avery 70 vs Carmen 64 in the runoff, and Carmen wins it 10-8 head-to-head.
STAR fails the CONSISTENCY criterion: winning every district does not
guarantee winning the whole. (Note this is NOT a summability failure — score
totals and the preference matrix still add across precincts; what you cannot
add is each district's declared winner.) Part 3 of 3 of the consistency
exercise (ex01_two_districts.md). Ballots adapted from a RangeVoting.org
example, posed as an exercise in Brendan W. Sullivan, "An Introduction to
the Math of Voting Methods" (2022), ch. 5.
Live on BetterVoting (Test ID BV2190): https://bettervoting.com/923q3d/results
— the election carries a second, Ranked Robin race on the same opinions
(equal ranks allowed): Elena, the citywide Condorcet winner, wins it 4-0.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Avery,Blake,Carmen,Diego,Elena
3,3,4,0,5 # 5 West voters: Elena first, Carmen second, Avery = Blake
3,3,4,0,5
3,3,4,0,5
3,3,4,0,5
3,3,4,0,5
5,5,3,0,0 # 3 West voters: Avery = Blake at the top, Carmen third
5,5,3,0,0
5,5,3,0,0
5,3,3,0,0 # 1 West voter: Avery over Blake
3,0,4,3,5 # 5 East voters: Elena first, Carmen second, Avery = Diego
3,0,4,3,5
3,0,4,3,5
3,0,4,3,5
3,0,4,3,5
5,0,3,5,0 # 3 East voters: Avery = Diego at the top, Carmen third
5,0,3,5,0
5,0,3,5,0
5,0,3,3,0 # 1 East voter: Avery over Diego
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Carmen
  Choose-One (Plurality) = Elena   (differs from STAR)
  RCV-IRV                = Elena   (differs from STAR)
  Approval               = Avery   (differs from STAR)
  RCV-RR (Condorcet)     = Elena   (differs from STAR)
  Note: 18 of 18 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/ex01_district_combined_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/ex01_district_combined_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Avery)
 - Runoff Round Winner   = (Carmen)
  Candidate Avery earned the highest total score, but
  Candidate Carmen won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 18 ballots.
Count × Avery,Blake,Carmen,Diego,Elena
    5 ×     3,    3,     4,    0,    5
    5 ×     3,    0,     4,    3,    5
    3 ×     5,    5,     3,    0,    0
    3 ×     5,    0,     3,    5,    0
    1 ×     5,    3,     3,    0,    0
    1 ×     5,    0,     3,    3,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Avery         -- 70 -- First place
   Carmen        -- 64 -- Second place
   Elena         -- 50
   Blake         -- 33
   Diego         -- 33
 Avery and Carmen advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Carmen        -- 10 -- First place
   Avery         --  8
   Equal Support --  0
 Carmen wins.
   Runoff math:
     18  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     18  voters with a preference  (majority = 10)
           Carmen 10 (56%)  ·  Avery 8 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Carmen
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Avery    |    Blake    |  * Carmen   |    Diego    |    Elena    |
-----------------------------------------------------------------------------------------
       * Avery > |     ---      |10 -  8 -  0 | 8 -  0 - 10 |10 -  8 -  0 | 8 -  0 - 10 |
         Blake > |  0 -  8 - 10 |    ---      | 3 -  1 - 14 | 9 -  0 -  9 | 4 -  4 - 10 |
      * Carmen > | 10 -  0 -  8 |14 -  1 -  3 |    ---      |14 -  1 -  3 | 8 -  0 - 10 |
         Diego > |  0 -  8 - 10 | 9 -  0 -  9 | 3 -  1 - 14 |    ---      | 4 -  4 - 10 |
         Elena > | 10 -  0 -  8 |10 -  4 -  4 |10 -  0 -  8 |10 -  4 -  4 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Elena — STAR elected Carmen instead (Elena was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Avery       8   0  10   0   0   0  |    70   3.9
Blake       3   0   6   0   0   9  |    33   1.8
Carmen      0  10   8   0   0   0  |    64   3.6
Diego       3   0   6   0   0   9  |    33   1.8
Elena      10   0   0   0   0   8  |    50   2.8
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex01_district_combined_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex01_district_combined.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/IRV_DIFFERS_ARTIFACT/ex01_district_combined.md) — its entry in the divergence review ledger
- [Summability (topic hub)](../../../../00_start_here/topics/summability/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
