# BV2132 — Pet poll (STAR): the consensus center Cat wins

*Generated from [`bv2132_ykjjhy_pet_star.yaml`](../bv2132_ykjjhy_pet_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cat

## Scenario

One of the four races in the BV2132 "Pet poll" (BetterVoting election ykjjhy) — the same 22 voters, three pets (Dog, Cat, Fish), tallied four ways. This is the STAR race. By score, Cat (78) and Fish (62) advance; in the automatic runoff Cat beats Fish 15-7, so STAR elects Cat — who is also the Condorcet winner (beats Dog 13-9 and Fish 15-7). Contrast the Plurality race (Dog) and the RCV-IRV race (Fish), where the consensus candidate is squeezed out. BV also elects Cat. Live results: https://bettervoting.com/ykjjhy/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dog,Cat,Fish
9: 5,3,1
7: 0,3,5
6: 0,5,3
```

## What the engine says

Full report from the [`_tabulated` mirror](../pet_poll_four_methods_tabulated/bv2132_ykjjhy_pet_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Dog     |   * Cat     |   * Fish    |
-------------------------------------------------------------
           Dog > |     ---      | 9 -  0 - 13 | 9 -  0 - 13 |
         * Cat > | 13 -  0 -  9 |    ---      |15 -  0 -  7 |
        * Fish > | 13 -  0 -  9 | 7 -  0 - 15 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Cat — matches the STAR winner

[Divergence from STAR]
  STAR                   = Cat
  Choose-One (Plurality) = Dog   (differs from STAR)
  RCV-IRV                = Fish   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: pet_poll_four_methods_tabulated/bv2132_ykjjhy_pet_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 22 ballots.
Count × Dog,Cat,Fish
    9 ×   5,  3,   1
    7 ×   0,  3,   5
    6 ×   0,  5,   3

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Dog         9   0   0   0   0  13  |    45   2.0
Cat         6   0  16   0   0   0  |    78   3.5
Fish        7   0   6   0   9   0  |    62   2.8

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cat           -- 78 -- First place
   Fish          -- 62 -- Second place
   Dog           -- 45
 Cat and Fish advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cat           -- 15 -- First place
   Fish          --  7
   Equal Support --  0
 Cat wins.
   Runoff math:
     22  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     22  voters with a preference  (majority = 12)
           Cat 15 (68%)  ·  Fish 7 (32%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cat
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_methods/bv2132_ykjjhy_pet_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2132_ykjjhy_pet_approval](bv2132_ykjjhy_pet_approval.md) · [bv2132_ykjjhy_pet_irv](bv2132_ykjjhy_pet_irv.md) · [bv2132_ykjjhy_pet_plurality](bv2132_ykjjhy_pet_plurality.md)
