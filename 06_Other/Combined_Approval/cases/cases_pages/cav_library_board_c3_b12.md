---
search:
  exclude: true
---

# Library board by Combined Approval Voting — the newcomer nobody dislikes

*Generated from [`cav_library_board_c3_b12.yaml`](../cav_library_board_c3_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Combined Approval Voting (CAV)](../..) · **1 seat** · **Expected winner:** Cleo

## Scenario

Twelve neighbours elect one seat on a town library board.

Alma and Byron are the known quantities, and both are polarising: four voters
vote For each of them, and roughly as many vote Against. Cleo is a newcomer.
Only three voters have met her — all three vote For — and the other nine have
no opinion and abstain. Nobody votes Against her.

Under CAV an abstention is genuinely free: it adds nothing and subtracts
nothing. So Cleo's nine blanks cost her nothing, her three approvals stand
unopposed, and she wins on net score (+3) ahead of Byron (+1) and Alma (−1).

The companion file `cav_library_board_blank_is_zero_c3_b12.yaml` gives these
twelve voters the SAME marks on an ordinary score ballot, where an unmarked
candidate scores 0 — the bottom of the scale rather than the middle. That one
change reverses the field completely: Byron 10, Alma 8, Cleo 6. Read the pair
together; the difference is entirely in what a blank is taken to mean.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alma,Byron,Cleo
2,0,1   # 1  Alma's camp — For Alma, Against Byron, no opinion on Cleo
2,0,1   # 2  Alma's camp
2,0,1   # 3  Alma's camp
2,0,1   # 4  Alma's camp
0,2,1   # 5  Byron's camp — mirror image
0,2,1   # 6  Byron's camp
0,2,1   # 7  Byron's camp
0,2,1   # 8  Byron's camp
1,1,2   # 9  knows only Cleo, and likes her
0,1,2   # 10 Against Alma, no opinion on Byron, For Cleo
1,1,2   # 11 knows only Cleo, and likes her
1,2,1   # 12 For Byron, no opinion on the other two
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/cav_library_board_c3_b12_CAV_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Combined Approval Voting (CAV, single winner) ---
  Library board by Combined Approval Voting — the newcomer nobody dislikes
 Tabulating 12 ballots on the three-level For / abstain / Against
 ballot. Highest NET score (approvals − disapprovals) wins.

[Scenario]
  Twelve neighbours elect one seat on a town library board.
  
  Alma and Byron are the known quantities, and both are polarising: four voters
  vote For each of them, and roughly as many vote Against. Cleo is a newcomer.
  Only three voters have met her — all three vote For — and the other nine have
  no opinion and abstain. Nobody votes Against her.
  
  Under CAV an abstention is genuinely free: it adds nothing and subtracts
  nothing. So Cleo's nine blanks cost her nothing, her three approvals stand
  unopposed, and she wins on net score (+3) ahead of Byron (+1) and Alma (−1).
  
  The companion file `cav_library_board_blank_is_zero_c3_b12.yaml` gives these
  twelve voters the SAME marks on an ordinary score ballot, where an unmarked
  candidate scores 0 — the bottom of the scale rather than the middle. That one
  change reverses the field completely: Byron 10, Alma 8, Cleo 6. Read the pair
  together; the difference is entirely in what a blank is taken to mean.

Ballots (2 = For, 1 = abstain, 0 = Against):
  Alma, Byron, Cleo
  2, 0, 1
  2, 0, 1
  2, 0, 1
  2, 0, 1
  0, 2, 1
  0, 2, 1
  0, 2, 1
  0, 2, 1
  1, 1, 2
  0, 1, 2
  1, 1, 2
  1, 2, 1

Vote tally:
          For   Abstain   Against      Net
  Cleo      3         9         0       +3  ← winner
  Byron     5         3         4       +1
  Alma      4         3         5       -1

Verification 1 — affine invariance (the (0,1,2) reading):
  The same marks summed as 0/1/2 must exceed the net total by exactly
  the ballot count (12) for every candidate, and must rank the field
  the same way. That is what makes CAV 'three-level score voting'.
    Cleo   net   +3   +12 =   15  (0/1/2 sum 15)
    Byron  net   +1   +12 =   13  (0/1/2 sum 13)
    Alma   net   -1   +12 =   11  (0/1/2 sum 11)
  ✓ holds — the (−1,0,+1) and (0,1,2) scales agree.

Verification 2 — pref_voting score_voting on the (0,1,2) profile: Cleo
  (✓ agrees with the CAV count)

Winner — Combined Approval Voting (single winner)
  Cleo
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/Combined_Approval/cases/cav_library_board_c3_b12.yaml
```

## See also

- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [cav_library_board_blank_is_zero_c3_b12](cav_library_board_blank_is_zero_c3_b12.md)
