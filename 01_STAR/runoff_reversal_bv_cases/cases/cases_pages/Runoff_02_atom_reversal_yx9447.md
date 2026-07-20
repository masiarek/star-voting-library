# Runoff 02 — the atom (smallest runoff reversal)

*Generated from [`Runoff_02_atom_reversal_yx9447.yaml`](../Runoff_02_atom_reversal_yx9447.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Boston

## Scenario

A REAL BetterVoting election (BV id yx9447), captured 2026-06-28. The smallest
possible Runoff Reversal: the Scoring-Round leader (Austin) LOSES the Automatic
Runoff to Boston, the candidate more voters prefer head-to-head. All three voters
like Austin (5, 4, 4), but two of them prefer Boston (Boston 5 over Austin 4), so
Boston wins the runoff 2-1. Winner = the Condorcet winner (not a startling case).
Level 101. Full two-view lesson: Runoff_02_atom_reversal_yx9447.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Austin, Boston, Cairo
5, 1, 2
4, 5, 0
4, 5, 0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Boston
  Approval = Austin   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Austin)
 - Runoff Round Winner   = (Boston)
  Candidate Austin earned the highest total score, but
  Candidate Boston won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Count × Austin,Boston,Cairo
    2 ×      4,     5,    0
    1 ×      5,     1,    2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Austin        -- 13 -- First place
   Boston        -- 11 -- Second place
   Cairo         --  2
 Austin and Boston advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Boston        -- 2 -- First place
   Austin        -- 1
   Equal Support -- 0
 Boston wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Boston 2 (67%)  ·  Austin 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Boston
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Austin  | * Boston  |   Cairo   |
-----------------------------------------------------
    * Austin > |    ---     |1 - 0 - 2  |3 - 0 - 0  |
    * Boston > | 2 - 0 - 1  |   ---     |2 - 0 - 1  |
       Cairo > | 0 - 0 - 3  |1 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Boston — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Austin     1  2  0  0  0  0  |    13   4.3
Boston     2  0  0  0  1  0  |    11   3.7
Cairo      0  0  0  1  0  2  |     2   0.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/Runoff_02_atom_reversal_yx9447_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_reversal_bv_cases/cases/Runoff_02_atom_reversal_yx9447.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/Runoff_02_atom_reversal_yx9447.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md) · [Runoff_08_ca_governor_reversal_gvdy42](Runoff_08_ca_governor_reversal_gvdy42.md)
