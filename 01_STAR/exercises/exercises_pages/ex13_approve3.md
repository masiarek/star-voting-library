# Exercise 13 — Where do you draw the line? Approve 3 and up

*Generated from [`ex13_approve3.yaml`](../ex13_approve3.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Ash

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/qdtqf2) · **[results ↗](https://bettervoting.com/qdtqf2/results)** (election `qdtqf2`).

## Scenario

The nine honest opinions of ex13_opinions.yaml converted to Approval
ballots under the GENEROUS reading: approve everyone you scored 3 or
higher. Approvals: Ash 7 of 9, Cora 6, Beck 5 — ASH wins. Compare
ex13_approve4.yaml (same opinions, stricter line: Beck wins) and
ex13_bullet.yaml (favorites only: Cora wins). One electorate, one
question the ballot cannot ask precisely — where the approval line
sits decides the election. Exercise: ex13_draw_the_line.md.
Live on BetterVoting (Test ID BV2200): https://bettervoting.com/qdtqf2/results
— this is the "approve 3 and up" race; BV agrees: Ash 7.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ash,Beck,Cora
1,1,0 # 3 voters: scored Ash 5, Beck 4 — both clear the 3+ line
1,1,0
1,1,0
0,1,1 # 2 voters: scored Beck 5, Cora 3 — both approved
0,1,1
1,0,1 # 4 voters: scored Cora 5, Ash 3 — both approved
1,0,1
1,0,1
1,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../exercises_tabulated/ex13_approve3_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 9 ballots (any non-zero score = approval).

Ballots:
   columns = Ash, Beck, Cora      (1 = approve; 0 / blank / marker = not approved)
     3 × 1,1,0
     2 × 0,1,1
     4 × 1,0,1

   Ash  -- 7 (78%) -- Elected
   Cora -- 6 (67%)
   Beck -- 5 (56%)

[Approval Distribution] (how many candidates each ballot approved)
   18 approvals across 9 ballots — average 2.0 of 3 (range 2–2).
     approved 2: 9 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Ash   |  Cora  |  Beck  |
   ----------------------------------
   Ash   |   --   |  57%   |  43%   |
   Cora  |  67%   |   --   |  33%   |
   Beck  |  60%   |  40%   |   --   |

Winner — Approval Voting (single winner)
  Ash
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex13_approve3.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
