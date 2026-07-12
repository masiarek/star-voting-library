# STAR mono-raise-delete — part 1: baseline, X wins

*Generated from [`mono_raise_delete_before.yaml`](../mono_raise_delete_before.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** X

## Scenario

Part 1 of the STAR mono-raise-delete pair (a 301 nuance). STAR satisfies the
standard monotonicity criterion (mono-raise: raising a candidate's score, and
nothing else, never hurts them) — but NOT the stronger mono-raise-delete
(D. R. Woodall, Voting Matters 1996): "X should not be harmed if X is raised on
some ballots AND all candidates now below X on those ballots are deleted."

Baseline: 30 voters. Scoring round makes X (87) and Y (84) the finalists, with
Z third (72); the runoff is X vs Y, which X wins 21-9. X WINS.

In part 2 (mono_raise_delete_after.yaml), nine voters whose ballots read
Z>X>Y raise X (3 -> 4) AND delete the one candidate now below X — Y -> 0.
That pure "raise X and bury the losers below X" move drops Y from 84 to 66,
below Z's 72, so the finalists become X and Z instead of X and Y. X still leads
the scoring, but now faces Z in the runoff and loses. Raising X made X lose:
STAR fails mono-raise-delete. The soft spot is finalist selection, not X's own
score. See 00_start_here/STAR_Voting/STAR_monotonicity.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
X,Y,Z
12: 5,4,0
9: 3,2,5
9: 0,2,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = X
  Choose-One (Plurality) = Z   (differs from STAR)
  RCV-IRV                = Z   (differs from STAR)
  RCV-RR (Condorcet)     = Z   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: monotonicity_tabulated/mono_raise_delete_before_RCV-IRV_tabulated.txt
  RCV-RR round-robin: monotonicity_tabulated/mono_raise_delete_before_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 30 ballots.
Count × X,Y,Z
   12 × 5,4,0
    9 × 3,2,5
    9 × 0,2,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   X             -- 87 -- First place
   Y             -- 84 -- Second place
   Z             -- 72
 X and Y advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   X             -- 21 -- First place
   Y             --  9
   Equal Support --  0
 X wins.
   Runoff math:
     30  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     30  voters with a preference  (majority = 16)
           X 21 (70%)  ·  Y 9 (30%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 X
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * X      |    * Y      |      Z      |
-------------------------------------------------------------
           * X > |     ---      |21 -  0 -  9 |12 -  0 - 18 |
           * Y > |  9 -  0 - 21 |    ---      |12 -  0 - 18 |
             Z > | 18 -  0 - 12 |18 -  0 - 12 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Z — STAR elected X instead (Z was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
X          12   0   9   0   0   9  |    87   2.9
Y           0  12   0  18   0   0  |    84   2.8
Z           9   0   9   0   0  12  |    72   2.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../monotonicity_tabulated/mono_raise_delete_before_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/mono_raise_delete_before.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [mono_raise_delete_after](mono_raise_delete_after.md) · [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md)
