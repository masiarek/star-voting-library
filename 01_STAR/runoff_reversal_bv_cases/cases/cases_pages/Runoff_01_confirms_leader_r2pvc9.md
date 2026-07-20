# Runoff 01 — Runoff confirms the leader (control)

*Generated from [`Runoff_01_confirms_leader_r2pvc9.yaml`](../Runoff_01_confirms_leader_r2pvc9.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Aspen

## Scenario

A REAL BetterVoting election (BV id r2pvc9), captured 2026-06-28. The control
case for the Runoff Reversal set: the Scoring-Round leader (Aspen) is ALSO the
candidate more voters prefer head-to-head, so the runoff CONFIRMS the leader —
proof the runoff isn't rigged against whoever has the most stars. Winner = the
Condorcet winner. Level 101. Full two-view lesson: Runoff_01_confirms_leader_r2pvc9.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Aspen, Birch, Cedar
5, 2, 1
2, 5, 0
5, 3, 0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Aspen,Birch,Cedar
    5,    2,    1
    2,    5,    0
    5,    3,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Aspen         -- 12 -- First place
   Birch         -- 10 -- Second place
   Cedar         --  1
 Aspen and Birch advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Aspen         -- 2 -- First place
   Birch         -- 1
   Equal Support -- 0
 Aspen wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Aspen 2 (67%)  ·  Birch 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Aspen
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Aspen   | * Birch   |   Cedar   |
-----------------------------------------------------
     * Aspen > |    ---     |2 - 0 - 1  |3 - 0 - 0  |
     * Birch > | 1 - 0 - 2  |   ---     |3 - 0 - 0  |
       Cedar > | 0 - 0 - 3  |0 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Aspen — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Aspen      2  0  0  1  0  0  |    12   4.0
Birch      1  0  1  1  0  0  |    10   3.3
Cedar      0  0  0  0  1  2  |     1   0.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/Runoff_01_confirms_leader_r2pvc9_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_reversal_bv_cases/cases/Runoff_01_confirms_leader_r2pvc9.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md) · [Runoff_08_ca_governor_reversal_gvdy42](Runoff_08_ca_governor_reversal_gvdy42.md)
