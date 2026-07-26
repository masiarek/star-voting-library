# Exercise 15a — a Yes/No profile (which method is this?)

*Generated from [`ex15_approval_yes_no.yaml`](../ex15_approval_yes_no.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Blair

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/d4v2dh) · **[results ↗](https://bettervoting.com/d4v2dh/results)** (election `d4v2dh`).

## Scenario

Part (a) of Exercise 15 — "Read the ballot, name the method."

35 voters, three candidates, and a ballot that records only Yes or No per
candidate — no ranking, no scores, and voters approve different NUMBERS of
candidates. That combination identifies the method: this is APPROVAL VOTING.
Blair wins with 28 approvals of 35 ballots (80%), ahead of Cosmo 22 and
Ada 15.

Note the shares add to well over 100% — approval percentages are shares of
BALLOTS, not of a divided pie, and that is the tell most readers miss.

A textbook-style prompt (a Yes/No table with weighted voter blocs), rebuilt
here with named candidates so the columns line up A/B/C -> Ada/Blair/Cosmo.
Companion file ex15_approval_pairwise.yaml re-reads these same ballots
pairwise; part (b) is ex15_score_profile.yaml.

Exercise page: ../ex15_read_the_ballot.md
Live results: https://bettervoting.com/d4v2dh/results (BV2258, race 1 of 2 —
BetterVoting's own Approval count agrees: Blair.)

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Count:Ada,Blair,Cosmo
15:0,1,1
8:1,1,0
7:1,0,1
5:0,1,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/ex15_approval_yes_no_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 35 ballots (any non-zero score = approval).

Ballots:
   columns = Ada, Blair, Cosmo      (1 = approve; 0 / blank / marker = not approved)
    15 × 0,1,1
     8 × 1,1,0
     7 × 1,0,1
     5 × 0,1,0

   Blair -- 28 (80%) -- Elected
   Cosmo -- 22 (63%)
   Ada   -- 15 (43%)

[Approval Distribution] (how many candidates each ballot approved)
   65 approvals across 35 ballots — average 1.9 of 3 (range 1–2).
     approved 1: 5 ballots
     approved 2: 30 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
          | Blair  | Cosmo  |  Ada   |
   -----------------------------------
   Blair  |   --   |  54%   |  29%   |
   Cosmo  |  68%   |   --   |  32%   |
   Ada    |  53%   |  47%   |   --   |

Winner — Approval Voting (single winner)
  Blair
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex15_approval_yes_no.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md) · [ex15_approval_pairwise](ex15_approval_pairwise.md) · [ex15_score_profile](ex15_score_profile.md)
