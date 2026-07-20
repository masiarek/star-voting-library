# Exercise 5 — The squeezed bridge-builder (IRV vs STAR)

*Generated from [`ex05_center_squeeze.yaml`](../ex05_center_squeeze.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Brook

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6bry7c) · **[results ↗](https://bettervoting.com/6bry7c/results)** (election `6bry7c`).

## Scenario

A club presidency with two wings and one bridge-builder. Brook is scored
3+ by every single voter and beats each rival head-to-head (5-4 over
Avi, 6-3 over Cole) — the Condorcet winner. But Brook has only 2 first
choices, so RCV-IRV eliminates Brook FIRST and elects the wing candidate
Avi 5-4: the center squeeze. STAR reads the full scores instead: Brook
tops the scoring round 31-23-18 and wins the runoff against Avi 5-4.
A drill for the squeeze mechanism (see the center-squeeze topic pages);
ballots and cast are this repo's own. Exercise: ex05_center_squeeze.md.
Live on BetterVoting (Test ID BV2192): https://bettervoting.com/6bry7c/results
— three races on the same opinions: STAR (Brook), RCV-IRV (Avi — the
squeeze, live), Ranked Robin (Brook).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Avi,Brook,Cole
5,3,0 # 4 voters: Avi's wing — Brook acceptable, Cole never
5,3,0
5,3,0
5,3,0
0,3,5 # 3 voters: Cole's wing — Brook acceptable, Avi never
0,3,5
0,3,5
3,5,0 # 1 voter: Brook first, leans Avi
0,5,3 # 1 voter: Brook first, leans Cole
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Brook
  Choose-One (Plurality) = Avi   (differs from STAR)
  RCV-IRV                = Avi   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/ex05_center_squeeze_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Avi,Brook,Cole
    4 ×   5,    3,   0
    3 ×   0,    3,   5
    1 ×   3,    5,   0
    1 ×   0,    5,   3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Brook         -- 31 -- First place
   Avi           -- 23 -- Second place
   Cole          -- 18
 Brook and Avi advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Brook         -- 5 -- First place
   Avi           -- 4
   Equal Support -- 0
 Brook wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Brook 5 (56%)  ·  Avi 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Brook
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Avi    | * Brook   |    Cole   |
-----------------------------------------------------
       * Avi > |    ---     |4 - 0 - 5  |5 - 0 - 4  |
     * Brook > | 5 - 0 - 4  |   ---     |6 - 0 - 3  |
        Cole > | 4 - 0 - 5  |3 - 0 - 6  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Brook — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Avi        4  0  1  0  0  4  |    23   2.6
Brook      2  0  7  0  0  0  |    31   3.4
Cole       3  0  1  0  0  5  |    18   2.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex05_center_squeeze_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex05_center_squeeze.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/ex05_center_squeeze.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
