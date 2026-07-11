# Runoff reversal, the jarring case — the near-consensus favorite loses a 51–49 runoff to a polarizing rival

*Generated from [`reversal_jarring_c3_b100.yaml`](../reversal_jarring_c3_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Rye

## Scenario

A *jarring* runoff reversal — the genuine philosophical drawback of STAR, shown honestly. 100 voters, three candidates: Uma is a near-consensus, high-utility candidate (49 give her a 5, 51 give her a 4 — a 4.5/5 average), Rye is polarizing (51 love him, 49 reject him), Tao is a no-hoper. Uma dominates the SCORE round 449 to Rye's 255 (Tao 49) — almost twice Rye's total — yet the runoff is Uma vs Rye, and Rye wins 51–49: a bare majority prefers him head-to-head. A utilitarian says STAR just elected the candidate who makes the electorate less happy overall; a majoritarian says 51 > 49 is the most legitimate thing an election can report. STAR is a hybrid (cardinal ballot, ordinal finish) and this is exactly where those two values pull apart — STAR chooses majority preference over utility maximization. Concede it plainly; it's a real cost, not a bug. Companion reversal_convincing_c3_b100 is the *convincing* reversal.
Lesson: 00_start_here/STAR_Voting/STAR_second_round_FAQ.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Uma,Rye,Tao
51:4,5,0    # love Rye, but Uma is a strong 4
49:5,0,1    # love Uma, reject Rye
```

## What the engine says

Full report from the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/reversal_jarring_c3_b100_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |      * Uma      |     * Rye      |       Tao      |
-------------------------------------------------------------------------
            * Uma > |       ---       | 49 -   0 -  51 |100 -   0 -   0 |
            * Rye > |  51 -   0 -  49 |      ---       | 51 -   0 -  49 |
              Tao > |   0 -   0 - 100 | 49 -   0 -  51 |      ---       |

[Condorcet Winner]
  Condorcet Winner: Rye — matches the STAR winner

[Divergence from STAR]
  STAR     = Rye
  Approval = Uma   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Uma)
 - Runoff Round Winner   = (Rye)
  Candidate Uma earned the highest total score, but
  Candidate Rye won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Uma,Rye,Tao
   51 ×   4,  5,  0
   49 ×   5,  0,  1

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Uma        49  51   0   0   0   0  |   449   4.5
Rye        51   0   0   0   0  49  |   255   2.6
Tao         0   0   0   0  49  51  |    49   0.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Uma           -- 449 -- First place
   Rye           -- 255 -- Second place
   Tao           --  49
 Uma and Rye advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Rye           -- 51 -- First place
   Uma           -- 49
   Equal Support --  0
 Rye wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Rye 51 (51%)  ·  Uma 49 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Rye
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/reversal_jarring_c3_b100.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/reversal_jarring_c3_b100.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [Runoff_01_confirms_leader_r2pvc9](Runoff_01_confirms_leader_r2pvc9.md) · [Runoff_02_atom_reversal_yx9447](Runoff_02_atom_reversal_yx9447.md) · [Runoff_03_enthusiasts_vs_majority_rkgtpk](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) · [Runoff_04_reversal_at_scale_bfjqmg](Runoff_04_reversal_at_scale_bfjqmg.md) · [Runoff_05_reversal_with_equal_support_xgkw3w](Runoff_05_reversal_with_equal_support_xgkw3w.md) · [Runoff_06_confirms_at_scale_d664xw](Runoff_06_confirms_at_scale_d664xw.md) · [Runoff_07_flat_ballot_bv_bug_tf73v9](Runoff_07_flat_ballot_bv_bug_tf73v9.md) · [Runoff_08_ca_governor_reversal_gvdy42](Runoff_08_ca_governor_reversal_gvdy42.md) · [reversal_convincing_c3_b100](reversal_convincing_c3_b100.md)
