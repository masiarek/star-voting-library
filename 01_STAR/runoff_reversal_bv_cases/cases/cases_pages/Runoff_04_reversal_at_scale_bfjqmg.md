# Runoff 04 — the reversal holds at scale (67/33)

*Generated from [`Runoff_04_reversal_at_scale_bfjqmg.yaml`](../Runoff_04_reversal_at_scale_bfjqmg.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Olive

## Scenario

A REAL BetterVoting election (BV id bfjqmg), captured 2026-06-28. The atom
(Runoff_02) blown up to a real crowd: three voters love Maple (5s) and push
Maple's total to the top of the Scoring Round (39), but six voters prefer Olive,
so Olive wins the Automatic Runoff 6-3 — a clean 2-to-1 majority (67/33). Proof
a reversal isn't a small-numbers fluke. Maple leads on HOW MUCH; Olive wins on
HOW MANY. Winner = the Condorcet winner. Level 101. Full two-view lesson:
Runoff_04_reversal_at_scale_bfjqmg.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Maple, Olive, Pine
4, 5, 0
4, 5, 0
4, 5, 0
5, 1, 2
5, 1, 2
4, 5, 0
5, 1, 2
4, 5, 0
4, 5, 0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Olive
  Approval = Maple   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Maple)
 - Runoff Round Winner   = (Olive)
  Candidate Maple earned the highest total score, but
  Candidate Olive won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Maple,Olive,Pine
    6 ×     4,    5,   0
    3 ×     5,    1,   2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Maple         -- 39 -- First place
   Olive         -- 33 -- Second place
   Pine          --  6
 Maple and Olive advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Olive         -- 6 -- First place
   Maple         -- 3
   Equal Support -- 0
 Olive wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Olive 6 (67%)  ·  Maple 3 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Olive
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Maple   | * Olive   |    Pine   |
-----------------------------------------------------
     * Maple > |    ---     |3 - 0 - 6  |9 - 0 - 0  |
     * Olive > | 6 - 0 - 3  |   ---     |6 - 0 - 3  |
        Pine > | 0 - 0 - 9  |3 - 0 - 6  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Olive — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Maple      3  6  0  0  0  0  |    39   4.3
Olive      6  0  0  0  3  0  |    33   3.7
Pine       0  0  0  3  0  6  |     6   0.7
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/Runoff_04_reversal_at_scale_bfjqmg_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_reversal_bv_cases/cases/Runoff_04_reversal_at_scale_bfjqmg.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/Runoff_04_reversal_at_scale_bfjqmg.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md) · [Runoff_08_ca_governor_reversal_gvdy42](Runoff_08_ca_governor_reversal_gvdy42.md)
