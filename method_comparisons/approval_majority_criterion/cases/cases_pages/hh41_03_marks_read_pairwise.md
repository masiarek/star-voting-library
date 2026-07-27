# Hamlin & Hua §4.1 — the same marks read pairwise: 60 of 100 voters express no preference

*Generated from [`hh41_03_marks_read_pairwise.yaml`](../hh41_03_marks_read_pairwise.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

The SAME approval marks as hh41_01_approval_as_printed.yaml, read as a score
ballot (approved = 5, not approved = 0) so the engine prints the pairwise
matrix and the runoff line. Magnitude is irrelevant — every head-to-head count
below depends only on the two-class ORDER — but 5/0 is used rather than 1/0
because the engine's built-in Approval cross-check reads "a score of 3+ is an
approval" and would misread a 1/0 ballot. Same convention, same reason, as
../../black_curtain/cases/Black_Curtain_01b_c3_b5_dichotomous.yaml.

This answers the obvious follow-up question: if approval misses the majority
favorite, would bolting a runoff onto the approval ballot fix it? No — and the
runoff line says exactly why:

  Voters with a preference: 40 of 100 (60 Equal Support).

The 60 voters who prefer A to B approved BOTH, so in a head-to-head between
them they say nothing. B wins the runoff 40-0. The deciding preference wasn't
outvoted, it was never recorded — the information was lost when the ballot was
marked, not when it was counted. On these ballots B is legitimately the
Condorcet winner; on the underlying preferences (hh41_02) A is. That gap is
the compression.

Claim-check page: ../../../00_start_here/Approval_Voting/hamlin_hua_2023.md
Companion set: ../../black_curtain/condorcet_compression.md
Set overview: ../README.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
60:5,5,0   # approved A and B — and no preference between them
30:0,5,5   # approved B and C
10:0,5,5   # approved C and B
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = B
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Note: 100 of 100 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/hh41_03_marks_read_pairwise_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × A,B,C
   60 × 5,5,0
   40 × 0,5,5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 500 -- First place
   A             -- 300 -- Second place
   C             -- 200
 B and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 40 -- First place
   A             --  0
   Equal Support -- 60
 B wins.
   Runoff math:
     100  ballots cast
   −  60  Equal Support (no preference between the two finalists)
     ───
      40  voters with a preference  (majority = 21)
           B 40 (100%)  ·  A 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |    * B      |      C      |
-------------------------------------------------------------
           * A > |     ---      | 0 - 60 - 40 |60 -  0 - 40 |
           * B > | 40 - 60 -  0 |    ---      |60 - 40 -  0 |
             C > | 40 -  0 - 60 | 0 - 40 - 60 |    ---      |

[Condorcet Winner]
  Condorcet Winner: B — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: C — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A           60    0    0    0    0   40  |   300   3.0
B          100    0    0    0    0    0  |   500   5.0
C           40    0    0    0    0   60  |   200   2.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/hh41_03_marks_read_pairwise_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/approval_majority_criterion/cases/hh41_03_marks_read_pairwise.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_DIFFERS_ARTIFACT/hh41_03_marks_read_pairwise.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [The Black Curtain (worked set)](../../../black_curtain/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [hh41_01_approval_as_printed](hh41_01_approval_as_printed.md) · [hh41_02_preferences_ranked_robin](hh41_02_preferences_ranked_robin.md) · [hh41_04_stipulated_utilities_star](hh41_04_stipulated_utilities_star.md) · [hh41_05_majority_bullet_votes](hh41_05_majority_bullet_votes.md)
