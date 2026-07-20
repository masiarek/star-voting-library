# Exercise 13 — Where do you draw the line? The honest opinions (STAR)

*Generated from [`ex13_opinions.yaml`](../ex13_opinions.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cora

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/qdtqf2) · **[results ↗](https://bettervoting.com/qdtqf2/results)** (election `qdtqf2`).

## Scenario

The reference election for the approval-threshold exercise: nine voters'
honest 0-5 opinions about Ash, Beck, and Cora — 3×(Ash 5, Beck 4),
2×(Beck 5, Cora 3), 4×(Cora 5, Ash 3). On the full scores, STAR
advances Ash (27) and Cora (26) and Cora wins the runoff 6-3; plain
Score voting would say Ash. The exercise then converts these SAME
opinions to Approval ballots under three defensible thresholds — and
gets three different Approval winners: approve 3+ elects Ash (7 of 9),
approve 4+ elects Beck (5), approve only 5s elects Cora (4). The
instructions, not the opinions, pick the winner. Companion files:
ex13_approve3.yaml / ex13_approve4.yaml / ex13_bullet.yaml. Exercise:
ex13_draw_the_line.md. Ballots and cast are this repo's own.
Live on BetterVoting (Test ID BV2200): https://bettervoting.com/qdtqf2/results
— one election, four races (STAR + the three approval thresholds); BV
agrees on all four winners.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ash,Beck,Cora
5,4,0 # 3 voters: Ash first, Beck a strong second
5,4,0
5,4,0
0,5,3 # 2 voters: Beck first, Cora mild
0,5,3
3,0,5 # 4 voters: Cora first, Ash tolerable
3,0,5
3,0,5
3,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Cora
  Approval = Ash   (differs from STAR)
  RCV-RR   = Ash   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: cases_tabulated/ex13_opinions_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Ash)
 - Runoff Round Winner   = (Cora)
  Candidate Ash earned the highest total score, but
  Candidate Cora won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Ash,Beck,Cora
    4 ×   3,   0,   5
    3 ×   5,   4,   0
    2 ×   0,   5,   3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ash           -- 27 -- First place
   Cora          -- 26 -- Second place
   Beck          -- 22
 Ash and Cora advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cora          -- 6 -- First place
   Ash           -- 3
   Equal Support -- 0
 Cora wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Cora 6 (67%)  ·  Ash 3 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cora
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ash    |    Beck   |  * Cora   |
-----------------------------------------------------
       * Ash > |    ---     |7 - 0 - 2  |3 - 0 - 6  |
        Beck > | 2 - 0 - 7  |   ---     |5 - 0 - 4  |
      * Cora > | 6 - 0 - 3  |4 - 0 - 5  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Ash > Beck > Cora > Ash)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ash        3  0  4  0  0  2  |    27   3.0
Beck       2  3  0  0  0  4  |    22   2.4
Cora       4  0  2  0  0  3  |    26   2.9
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex13_opinions_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex13_opinions.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/CYCLE_OR_THREE_WAY/ex13_opinions.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
