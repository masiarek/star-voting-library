---
search:
  exclude: true
---

# SAV seats the pair that represents everybody; AV strands three voters

*Generated from [`approval_sav_covers_everyone_c3_b17_brams_kilgour.yaml`](../approval_sav_covers_everyone_c3_b17_brams_kilgour.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../01_Learn) · **2 seats** · **Expected winners:** Ash, Bree

## Scenario

Brams & Kilgour, Satisfaction Approval Voting (MPRA 22709, 2010) —
Proposition 5: "SAV can find a minimal representative set when both AV and
the greedy algorithm fail to do so." Seventeen voters, three candidates, TWO
seats. The paper's a,b,c are named Ash, Bree, Cole here.

  AV  (one vote per mark):  Ash 10, Bree 9, Cole 8   ->  Ash, Bree
  SAV (one vote per ballot, split):
      Ash  5x1/2 + 5x1/2       = 5
      Bree 5x1/2 + 4x1         = 6 1/2
      Cole 5x1/2 + 3x1         = 5 1/2                ->  Bree, Cole

AV's pair leaves the three Cole-only voters with nobody. SAV's pair
represents ALL SEVENTEEN voters, and is the smallest set that can — a
"minimal representative set" in the paper's terms.

Ash is the most-approved candidate and is elected by neither measure that
matters here: every one of Ash's supporters already has a second choice
seated. Note what did the work — the ten slate voters each SPLIT their vote,
so Ash (approved by all ten of them and nobody else) collected only 5, while
Bree and Cole combined half-votes with the WHOLE votes of bullet voters.

Unlike the companion disjointness case, PAV agrees with SAV here — it also
returns {Bree, Cole}. Spectrum:

  python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py \
    04_Approval/02_Examples/multiwinner/cases/approval_sav_covers_everyone_c3_b17_brams_kilgour.yaml \
    --rules av,sav,pav,seqpav,cc,seqphragmen

Concept page:
04_Approval/01_Learn/Multiwinner_Approval/satisfaction_approval_voting.md

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ash,Bree,Cole
1,1,0   # 5 voters — Ash and Bree
1,1,0
1,1,0
1,1,0
1,1,0
1,0,1   # 5 voters — Ash and Cole
1,0,1
1,0,1
1,0,1
1,0,1
0,1,0   # 4 voters — Bree only
0,1,0
0,1,0
0,1,0
0,0,1   # 3 voters — Cole only
0,0,1
0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/approval_sav_covers_everyone_c3_b17_brams_kilgour_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (2 winners) ---
 Tabulating 17 ballots (any non-zero score = approval).

Ballots:
   columns = Ash, Bree, Cole      (1 = approve; 0 / blank / marker = not approved)
     5 × 1,1,0
     5 × 1,0,1
     4 × 0,1,0
     3 × 0,0,1

   Ash  -- 10 (59%) -- Elected
   Bree -- 9 (53%) -- Elected
   Cole -- 8 (47%)

[Approval Distribution] (how many candidates each ballot approved)
   27 approvals across 17 ballots — average 1.6 of 3 (range 1–2).
     approved 1: 7 ballots
     approved 2: 10 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Ash   |  Bree  |  Cole  |
   ----------------------------------
   Ash   |   --   |  50%   |  50%   |
   Bree  |  56%   |   --   |   0%   |
   Cole  |  62%   |   0%   |   --   |

Winners — Approval Voting (2 winners)
  Ash, Bree
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/02_Examples/multiwinner/cases/approval_sav_covers_everyone_c3_b17_brams_kilgour.yaml
```

## See also

- [Vote splitting (worked set)](../../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [approval_bloc_2seats_c4_b6](approval_bloc_2seats_c4_b6.md) · [approval_bloc_3seats_c6_b5](approval_bloc_3seats_c6_b5.md) · [approval_bloc_4seats_c7_b12_lackner_skowron](approval_bloc_4seats_c7_b12_lackner_skowron.md) · [approval_sav_disjoint_c4_b10_brams_kilgour](approval_sav_disjoint_c4_b10_brams_kilgour.md)
