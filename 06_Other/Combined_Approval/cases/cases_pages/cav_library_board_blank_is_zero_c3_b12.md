---
search:
  exclude: true
---

# Library board on a blank-is-zero score ballot — the same twelve voters

*Generated from [`cav_library_board_blank_is_zero_c3_b12.yaml`](../cav_library_board_blank_is_zero_c3_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [range](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Byron

## Scenario

The counterfactual twin of `cav_library_board_c3_b12.yaml`. Same twelve
neighbours, same library board seat, same opinions — and the same physical
marks: a voter who was For a candidate gives them the top grade, a voter who
was Against gives them the bottom, and a voter with no opinion leaves the row
blank.

The one thing that changes is what a blank MEANS. On a CAV ballot an unmarked
row is an abstention worth 0 on a −1…+1 scale, i.e. the MIDDLE. On an ordinary
score ballot an unmarked row is worth 0 on a 0…5 scale, i.e. the BOTTOM — the
same mark a voter uses to say "worst possible candidate."

That single reinterpretation reverses the entire field. Cleo, the newcomer
whom nine voters simply don't know, is charged nine bottom grades she never
cast, and drops from first (+3 net under CAV) to last (6 points here). Byron
wins with 10, Alma takes 8.

This is the mechanism behind the empirical finding in the 2012 French
evaluative-voting experiments: moving from a (0,1,2) scale to a (−1,0,+1)
scale left polarising candidates roughly where they were but raised the scores
of broadly-liked and, especially, lesser-known candidates. The scales are
affine-equivalent on identical ballots; they are not equivalent once voters
leave rows blank.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alma,Byron,Cleo
2,0,    # 1  Alma's camp — Cleo left blank
2,0,    # 2  Alma's camp
2,0,    # 3  Alma's camp
2,0,    # 4  Alma's camp
0,2,    # 5  Byron's camp
0,2,    # 6  Byron's camp
0,2,    # 7  Byron's camp
0,2,    # 8  Byron's camp
,,2     # 9  knows only Cleo
0,,2    # 10 Against Alma, Byron blank, For Cleo
,,2     # 11 knows only Cleo
,2,     # 12 For Byron only
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/cav_library_board_blank_is_zero_c3_b12_RANGE_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Range / Score Voting (single winner) ---
  Library board on a blank-is-zero score ballot — the same twelve voters
 Tabulating 12 ballots on a 0–2 scale (range/score: highest total wins, no runoff).

[Scenario]
  The counterfactual twin of `cav_library_board_c3_b12.yaml`. Same twelve
  neighbours, same library board seat, same opinions — and the same physical
  marks: a voter who was For a candidate gives them the top grade, a voter who
  was Against gives them the bottom, and a voter with no opinion leaves the row
  blank.
  
  The one thing that changes is what a blank MEANS. On a CAV ballot an unmarked
  row is an abstention worth 0 on a −1…+1 scale, i.e. the MIDDLE. On an ordinary
  score ballot an unmarked row is worth 0 on a 0…5 scale, i.e. the BOTTOM — the
  same mark a voter uses to say "worst possible candidate."
  
  That single reinterpretation reverses the entire field. Cleo, the newcomer
  whom nine voters simply don't know, is charged nine bottom grades she never
  cast, and drops from first (+3 net under CAV) to last (6 points here). Byron
  wins with 10, Alma takes 8.
  
  This is the mechanism behind the empirical finding in the 2012 French
  evaluative-voting experiments: moving from a (0,1,2) scale to a (−1,0,+1)
  scale left polarising candidates roughly where they were but raised the scores
  of broadly-liked and, especially, lesser-known candidates. The scales are
  affine-equivalent on identical ballots; they are not equivalent once voters
  leave rows blank.

Ballots:
  Alma, Byron, Cleo
  2, 0, 0
  2, 0, 0
  2, 0, 0
  2, 0, 0
  0, 2, 0
  0, 2, 0
  0, 2, 0
  0, 2, 0
  0, 0, 2
  0, 0, 2
  0, 0, 2
  0, 2, 0

Total score (sum of all grades):
  Byron          10  ← winner
  Alma           8
  Cleo           6

Cross-check — pref_voting score_voting: Byron  (✓ agrees with the hand count)

Winner — Range / Score Voting (single winner)
  Byron
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/Combined_Approval/cases/cav_library_board_blank_is_zero_c3_b12.yaml
```

## See also

- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [cav_library_board_c3_b12](cav_library_board_c3_b12.md)
