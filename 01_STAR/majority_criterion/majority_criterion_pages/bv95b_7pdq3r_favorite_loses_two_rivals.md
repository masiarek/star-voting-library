# BV95b — Majority Criterion: favorite LOSES when the majority backs TWO rivals

*Generated from [`bv95b_7pdq3r_favorite_loses_two_rivals.yaml`](../bv95b_7pdq3r_favorite_loses_two_rivals.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bruno

## Scenario

Backs sheet row BV95b (pair with BV95a / mc_01).
The same 5-voter election as mc_01, changed in ONE spot: the 3-voter majority
that top-scores Ada now also gives Cleo a 3 (they honestly like a SECOND other
candidate), instead of 0.

Ada 15, Bruno 22, Cleo 19. Now BOTH Bruno and Cleo out-score Ada, so the top
two by score are Bruno and Cleo — Ada never reaches the runoff and LOSES,
despite being the top choice of a 3-of-5 majority. Bruno wins the runoff.

This is STAR's Majority-Criterion failure, and it shows exactly why it is mild:
the majority had to support TWO other candidates to lose their favorite (Score
and Approval can drop the favorite on just ONE). That is the point of the
Relaxed Majority Criterion, which STAR passes. See
../../00_start_here/topics/majority_criterion/README.md.

Reproduced on BetterVoting (election 7pdq3r): BV also elects Bruno
(nTallyVotes 5), confirming the LH result. Frozen export:
bv95b_7pdq3r_favorite_loses_two_rivals_bv_export.json. Live:
https://bettervoting.com/7pdq3r/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Bruno,Cleo
5,4,3
5,4,3
5,4,3
0,5,5
0,5,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../majority_criterion_tabulated/bv95b_7pdq3r_favorite_loses_two_rivals_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ada    | * Bruno   |  * Cleo   |
-----------------------------------------------------
         Ada > |    ---     |3 - 0 - 2  |3 - 0 - 2  |
     * Bruno > | 2 - 0 - 3  |   ---     |3 - 2 - 0  |
      * Cleo > | 2 - 0 - 3  |0 - 2 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ada — STAR elected Bruno instead (Ada was eliminated in the scoring round)

[Divergence from STAR]
  STAR                   = Bruno
  Choose-One (Plurality) = Ada   (differs from STAR)
  RCV-IRV                = Ada   (differs from STAR)
  RCV-RR (Condorcet)     = Ada   (differs from STAR)
  Note: 2 of 5 ballots (40%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: majority_criterion_tabulated/bv95b_7pdq3r_favorite_loses_two_rivals_RCV-IRV_tabulated.txt
  RCV-RR round-robin: majority_criterion_tabulated/bv95b_7pdq3r_favorite_loses_two_rivals_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Count × Ada,Bruno,Cleo
    3 ×   5,    4,   3
    2 ×   0,    5,   5

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        3  0  0  0  0  2  |    15   3.0
Bruno      2  3  0  0  0  0  |    22   4.4
Cleo       2  0  3  0  0  0  |    19   3.8

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 22 -- First place
   Cleo          -- 19 -- Second place
   Ada           -- 15
 Bruno and Cleo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 3 -- First place
   Cleo          -- 0
   Equal Support -- 2
 Bruno wins.
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Bruno 3 (100%)  ·  Cleo 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bruno
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/majority_criterion/bv95b_7pdq3r_favorite_loses_two_rivals.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/IRV_DIFFERS_ARTIFACT/bv95b_7pdq3r_favorite_loses_two_rivals.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv95a_9m6rxr_favorite_survives_one_rival](bv95a_9m6rxr_favorite_survives_one_rival.md)
