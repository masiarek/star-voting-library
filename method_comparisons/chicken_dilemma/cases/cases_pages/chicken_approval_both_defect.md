---
search:
  exclude: true
---

# Chicken / Burr dilemma — Approval, both sides defect: C wins on 40%

*Generated from [`chicken_approval_both_defect.yaml`](../chicken_approval_both_defect.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **1 seat** · **Expected winner:** C

## Scenario

The third horn of the Burr dilemma, and the one the set previously only
described in prose. Same 100 voters as chicken_approval and chicken_star: 60
prefer either ally to C, 40 want C.

In chicken_approval the 60 cooperate honestly and A and B tie 60-60 — the
1800 Jefferson-Burr outcome, and the reason each side is tempted to defect.
Here both sides give in to that temptation. The 35 A-first voters approve only
A; the 25 B-first voters approve only B. Neither is voting dishonestly about
who they prefer; each is simply withholding approval from an ally to win the
intra-faction contest.

A 35, B 25, C 40. C wins with 40 of 100 while SIXTY voters preferred either
ally. The faction did not lose because the ballot forced it to split — Approval
never forces that. It lost because its two halves each declined to support the
other.

This is Approval's exact counterpart to STAR's residual split
(method_comparisons/split_voting/_main/05a_residual_split_bullet-voting.yaml,
where a 60% side loses to a 40% opponent the same way). Both are SELF-inflicted:
the ballot offered a remedy and the voters declined it. That is a real and
meaningful difference from Choose-One, where no remedy is on offer at all — but
it is not immunity, and neither method should be sold as immune.

Where the avalanche starts: with a of the 35 A-first voters and b of the 25
B-first voters bullet-voting, A holds 60 - b approvals and B holds 60 - a. C
takes the lead only once BOTH a > 20 and b > 20 — so it is not one defector
who does the damage, it is defection becoming general. That threshold is what
makes the Approval slope slippery, and it is exactly what STAR's runoff
removes: see chicken_star.yaml, where supporting both allies honestly costs
nothing.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Count:A,B,C
35:1,0,0   # A-first voters bullet-vote — no approval for ally B
25:0,1,0   # B-first voters bullet-vote — no approval for ally A
40:0,0,1   # the C bloc, unchanged and undivided
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/chicken_approval_both_defect_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 100 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C      (1 = approve; 0 = not approved)
    35 × 1,0,0
    25 × 0,1,0
    40 × 0,0,1

   C -- 40 (40%) -- Elected
   A -- 35 (35%)
   B -- 25 (25%)

[Approval Distribution] (how many candidates each ballot approved)
   100 approvals across 100 ballots — average 1.0 of 3 (range 1–1).
     approved 1: 100 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   C    |   A    |   B    |
   -------------------------------
   C  |   --   |   0%   |   0%   |
   A  |   0%   |   --   |   0%   |
   B  |   0%   |   0%   |   --   |

Winner — Approval Voting (single winner)
  C
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/chicken_dilemma/cases/chicken_approval_both_defect.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [chicken_approval](chicken_approval.md) · [chicken_star](chicken_star.md)
