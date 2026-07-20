# Exercise 6 — Bullet voting backfires: the strategic ballots

*Generated from [`ex06_bullet_backfire.yaml`](../ex06_bullet_backfire.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cash

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/7f4f7q) · **[results ↗](https://bettervoting.com/7f4f7q/results)** (election `7f4f7q`).

## Scenario

The same nine voters as ex06_bullet_honest.yaml, but Ari's four fans now
bullet vote — Ari 5, Bree 0, Cash 0 — hoping to drag Ari past the
compromise candidate. It works halfway: Bree crashes from 25 points to
13 and out of the runoff, and Ari (20) becomes a finalist. But the
runoff Ari inherits is against Cash (21) — and Ari loses it 5-4, because
zeroing Bree never manufactured any Ari-over-Cash preferences. The
bullet voters demoted their sure second choice and elected their
nightmare. STAR's runoff is exactly the feature that makes this gamble
costly. Exercise: ex06_bullet_backfire.md. Ballots and cast are this
repo's own.
Live on BetterVoting (Test ID BV2194): https://bettervoting.com/7f4f7q/results
— with RCV-IRV and Ranked Robin races: on the bullet ballots all three
methods elect Cash.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ari,Bree,Cash
5,0,0 # 4 voters: Ari fans BULLET VOTING (honest ballot was 5,3,0)
5,0,0
5,0,0
5,0,0
0,2,5 # 4 voters: Cash fans, unchanged
0,2,5
0,2,5
0,2,5
0,5,1 # 1 voter: Bree all the way, unchanged
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Cash
  Choose-One (Plurality) = Ari   (differs from STAR)
  Approval               = Ari   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Ari,Bree,Cash
    4 ×   5,   0,   0
    4 ×   0,   2,   5
    1 ×   0,   5,   1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cash          -- 21 -- First place
   Ari           -- 20 -- Second place
   Bree          -- 13
 Cash and Ari advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cash          -- 5 -- First place
   Ari           -- 4
   Equal Support -- 0
 Cash wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Cash 5 (56%)  ·  Ari 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cash
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ari    |    Bree   |  * Cash   |
-----------------------------------------------------
       * Ari > |    ---     |4 - 0 - 5  |4 - 0 - 5  |
        Bree > | 5 - 0 - 4  |   ---     |1 - 4 - 4  |
      * Cash > | 5 - 0 - 4  |4 - 4 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cash — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ari        4  0  0  0  0  5  |    20   2.2
Bree       1  0  0  4  0  4  |    13   1.4
Cash       4  0  0  0  1  4  |    21   2.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex06_bullet_backfire_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex06_bullet_backfire.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/ex06_bullet_backfire.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
