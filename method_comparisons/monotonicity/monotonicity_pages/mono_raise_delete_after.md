# STAR mono-raise-delete — part 2: raise X, delete Y-below-X, X loses

*Generated from [`mono_raise_delete_after.yaml`](../mono_raise_delete_after.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Z

## Scenario

Part 2 of the STAR mono-raise-delete pair. The ONLY change from part 1
(mono_raise_delete_before.yaml): on the nine ballots that read Z>X>Y
(Z=5, X=3, Y=2, i.e. "3,2,5"), X is raised from 3 to 4 and the one candidate
now below X — Y — is deleted (dropped to 0). Those ballots become
Z=5, X=4, Y=0 ("4,0,5"). Z stays above X and is untouched, exactly as
mono-raise-delete prescribes ("delete all candidates now below X").

Effect: burying Y drops its total from 84 to 66, below Z's 72, so the finalists
change from {X, Y} to {X, Z}. X still leads the scoring round (now 96), but the
runoff is X vs Z, and Z beats X 18-12. X went from winning to losing after being
raised — STAR fails the mono-raise-delete criterion (Woodall 1996). It still
passes plain mono-raise (see the monotonicity_star_* pair, where the same kind
of change leaves X winning). Concept: 00_start_here/STAR_Voting/properties_and_limits/STAR_monotonicity.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
X,Y,Z
12: 5,4,0
9: 4,0,5
9: 0,2,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Z
  Approval = X   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (X)
 - Runoff Round Winner   = (Z)
  Candidate X earned the highest total score, but
  Candidate Z won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 30 ballots.
Count × X,Y,Z
   12 × 5,4,0
    9 × 4,0,5
    9 × 0,2,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   X             -- 96 -- First place
   Z             -- 72 -- Second place
   Y             -- 66
 X and Z advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Z             -- 18 -- First place
   X             -- 12
   Equal Support --  0
 Z wins.
   Runoff math:
     30  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     30  voters with a preference  (majority = 16)
           Z 18 (60%)  ·  X 12 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Z
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * X      |      Y      |    * Z      |
-------------------------------------------------------------
           * X > |     ---      |21 -  0 -  9 |12 -  0 - 18 |
             Y > |  9 -  0 - 21 |    ---      |12 -  0 - 18 |
           * Z > | 18 -  0 - 12 |18 -  0 - 12 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Z — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
X          12   9   0   0   0   9  |    96   3.2
Y           0  12   0   9   0   9  |    66   2.2
Z           9   0   9   0   0  12  |    72   2.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../monotonicity_tabulated/mono_raise_delete_after_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/mono_raise_delete_after.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/APPROVAL_OR_MINOR/mono_raise_delete_after.md) — its entry in the divergence review ledger
- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [mono_raise_delete_before](mono_raise_delete_before.md) · [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md)
