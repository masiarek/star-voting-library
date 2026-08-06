---
search:
  exclude: true
---

# SAV vs AV — the same ballots elect two disjoint committees

*Generated from [`approval_sav_disjoint_c4_b10_brams_kilgour.yaml`](../approval_sav_disjoint_c4_b10_brams_kilgour.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Ada, Ben

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4hfwqd) · **[results ↗](https://bettervoting.com/4hfwqd/results)** (election `4hfwqd` · test `BV2271`).

## Scenario

Brams & Kilgour's own worked example (Satisfaction Approval Voting, MPRA
22709, 2010, section 2) — the proof of their Proposition 2: "AV and SAV can
elect disjoint subsets of candidates." Ten voters, four candidates, TWO
seats. Four voters approve a two-person slate; six bullet-vote.

The paper's candidates a,b,c,d are named Ada, Ben, Cleo, Dev here.

  AV  (one vote per mark, the LH engine's Approval_Multi_Winner):
      Ada 4, Ben 4, Cleo 3, Dev 3   ->  Ada, Ben
  SAV (one vote per BALLOT, split evenly among the marks):
      Ada 4x1/2 = 2, Ben 2, Cleo 3x1 = 3, Dev 3   ->  Cleo, Dev

Not one candidate in common. The slate voters' marks were worth a whole vote
each under AV and half a vote each under SAV, and half was not enough.

Which is "right" depends on what you count. AV's pair represents 4 of the 10
voters; SAV's represents 6 — the paper's argument for SAV. Run the file
through the abcvoting engine for the whole spectrum:

  python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py \
    04_Approval/02_Examples/multiwinner/cases/approval_sav_disjoint_c4_b10_brams_kilgour.yaml \
    --rules av,sav,pav,seqpav,cc,seqphragmen

PAV splits the difference — it ties {Ada,Cleo}, {Ada,Dev}, {Ben,Cleo},
{Ben,Dev}, one seat from each side, which is the proportional answer for a
40% bloc holding 2 seats. Concept page:
04_Approval/01_Learn/Multiwinner_Approval/satisfaction_approval_voting.md

Live on BetterVoting (BV2271, election 4hfwqd): the SAME ten voters under the
three methods BV can tabulate — Approval, STAR and Ranked Robin, all bloc at
2 seats. All three elect Ada and Ben, so SAV is the lone dissenter rather
than bloc Approval being the outlier. Two-view page:
bv2271_4hfwqd_sav_disjoint.md
Live results: https://bettervoting.com/4hfwqd/results

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ada,Ben,Cleo,Dev
1,1,0,0   # 4 voters — the two-person slate
1,1,0,0
1,1,0,0
1,1,0,0
0,0,1,0   # 3 voters — Cleo only
0,0,1,0
0,0,1,0
0,0,0,1   # 3 voters — Dev only
0,0,0,1
0,0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/approval_sav_disjoint_c4_b10_brams_kilgour_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (2 winners) ---
 Tabulating 10 ballots (any non-zero score = approval).

Ballots:
   columns = Ada, Ben, Cleo, Dev      (1 = approve; 0 / blank / marker = not approved)
     4 × 1,1,0,0
     3 × 0,0,1,0
     3 × 0,0,0,1

   Ada  -- 4 (40%) -- Elected
   Ben  -- 4 (40%) -- Elected
   Cleo -- 3 (30%)
   Dev  -- 3 (30%)

[Approval Distribution] (how many candidates each ballot approved)
   14 approvals across 10 ballots — average 1.4 of 4 (range 1–2).
     approved 1: 6 ballots
     approved 2: 4 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Ada   |  Ben   |  Cleo  |  Dev   |
   -------------------------------------------
   Ada   |   --   |  100%  |   0%   |   0%   |
   Ben   |  100%  |   --   |   0%   |   0%   |
   Cleo  |   0%   |   0%   |   --   |   0%   |
   Dev   |   0%   |   0%   |   0%   |   --   |

Winners — Approval Voting (2 winners)
  Ada, Ben
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/02_Examples/multiwinner/cases/approval_sav_disjoint_c4_b10_brams_kilgour.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [Vote splitting (worked set)](../../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [approval_bloc_2seats_c4_b6](approval_bloc_2seats_c4_b6.md) · [approval_bloc_3seats_c6_b5](approval_bloc_3seats_c6_b5.md) · [approval_bloc_4seats_c7_b12_lackner_skowron](approval_bloc_4seats_c7_b12_lackner_skowron.md) · [approval_sav_covers_everyone_c3_b17_brams_kilgour](approval_sav_covers_everyone_c3_b17_brams_kilgour.md)
