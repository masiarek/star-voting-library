# BV2133 — Pet poll II (STAR): the consensus Cat wins

*Generated from [`bv2133_dyxrbr_pet2_star.yaml`](../bv2133_dyxrbr_pet2_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cat

## Scenario

One of four races in the BV2133 "Pet poll II" (BetterVoting election dyxrbr) — 32 voters, four pets (Dog, Cat, Fish, Bird), tallied four ways, each electing a DIFFERENT pet. This is the STAR race: Cat (84) and Fish (72) lead on score and advance; Cat wins the automatic runoff 22-10, so STAR elects the consensus, Cat. The other races elect Dog (Plurality), Fish (RCV-IRV), and Bird (Approval). BV also elects Cat. Live results: https://bettervoting.com/dyxrbr/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dog,Cat,Fish,Bird
9: 0,2,1,4
10: 2,4,5,3
7: 3,2,1,0
6: 5,2,1,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../pet_poll_four_winners_tabulated/bv2133_dyxrbr_pet2_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Dog     |   * Cat     |   * Fish    |     Bird    |
---------------------------------------------------------------------------
           Dog > |     ---      |13 -  0 - 19 |13 -  0 - 19 |13 -  0 - 19 |
         * Cat > | 19 -  0 - 13 |    ---      |22 -  0 - 10 |23 -  0 -  9 |
        * Fish > | 19 -  0 - 13 |10 -  0 - 22 |    ---      |23 -  0 -  9 |
          Bird > | 19 -  0 - 13 | 9 -  0 - 23 | 9 -  0 - 23 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Cat — matches the STAR winner

[Divergence from STAR]
  STAR                   = Cat
  Choose-One (Plurality) = Dog   (differs from STAR)
  RCV-IRV                = Fish   (differs from STAR)
  Approval               = Bird   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: pet_poll_four_winners_tabulated/bv2133_dyxrbr_pet2_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 32 ballots.
Count × Dog,Cat,Fish,Bird
   10 ×   2,  4,   5,   3
    9 ×   0,  2,   1,   4
    7 ×   3,  2,   1,   0
    6 ×   5,  2,   1,   0

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Dog         6   0   7  10   0   9  |    71   2.2
Cat         0  10   0  22   0   0  |    84   2.6
Fish       10   0   0   0  22   0  |    72   2.3
Bird        0   9  10   0   0  13  |    66   2.1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cat           -- 84 -- First place
   Fish          -- 72 -- Second place
   Dog           -- 71
   Bird          -- 66
 Cat and Fish advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cat           -- 22 -- First place
   Fish          -- 10
   Equal Support --  0
 Cat wins.
   Runoff math:
     32  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     32  voters with a preference  (majority = 17)
           Cat 22 (69%)  ·  Fish 10 (31%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cat
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_winners/bv2133_dyxrbr_pet2_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2133_dyxrbr_pet2_star.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2133_dyxrbr_pet2_approval](bv2133_dyxrbr_pet2_approval.md) · [bv2133_dyxrbr_pet2_irv](bv2133_dyxrbr_pet2_irv.md) · [bv2133_dyxrbr_pet2_plurality](bv2133_dyxrbr_pet2_plurality.md)
