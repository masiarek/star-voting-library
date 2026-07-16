# Brams Example 6 — three counts, three winners (STAR sides with head-to-head)

*Generated from [`brams_ex6_three_winners_c3_b9.yaml`](../brams_ex6_three_winners_c3_b9.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cole

## Scenario

Example 6 of Brams & Potthoff, "The paradox of grading systems" (Public
Choice 165, 2015): nine voters in three like-minded blocs grade three
candidates {0..2}, and three grading aggregations crown three DIFFERENT
winners — proven by the authors' exhaustive search to be the unique
minimal party-structured example of this strong paradox:
  - Highest grade total (Score): Amos 11, Bree 10, Cole 10 -> AMOS.
  - Highest median grade: Bree 2 (Amos 1, Cole 1)          -> BREE.
  - Head-to-head (Condorcet): Cole beats Amos 3-2 and Bree 4-2 -> COLE.
STAR sides with head-to-head: Bree/Cole tie at 10 for second place, the
tie breaks to Cole (he beats Bree 4-2), and Cole wins the runoff 3-2 with
4 Equal Support ballots. Every voter here has dichotomous preferences, so
their natural Approval ballots elect Cole too (6-5-7) — but a uniform
any-non-zero cut elects Amos (9-5-7). Where the 0/1 line falls decides
the approval winner; no cut is canonical.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amos,Bree,Cole
2,2,0   # bloc 1 (2 voters) — Amos and Bree top, Cole bottom
2,2,0
1,2,2   # bloc 2 (3 voters) — Bree and Cole top, Amos middling
1,2,2
1,2,2
1,0,1   # bloc 3 (4 voters) — Amos and Cole middling, Bree bottom
1,0,1
1,0,1
1,0,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Cole
  Choose-One (Plurality) = Amos   (differs from STAR)
  RCV-IRV                = Amos   (differs from STAR)
  Approval               = Amos   (differs from STAR)
  Note: 9 of 9 ballots (100%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: brams_grading_paradox_tabulated/brams_ex6_three_winners_c3_b9_RCV-IRV_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Amos)
 - Runoff Round Winner   = (Cole)
  Candidate Amos earned the highest total score, but
  Candidate Cole won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Amos,Bree,Cole
    4 ×    1,   0,   1
    3 ×    1,   2,   2
    2 ×    2,   2,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Amos          -- 11 -- First place
   Bree          -- 10 -- Tied for second place
   Cole          -- 10 -- Tied for second place
 Amos advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Cole          -- 4 -- Second place
   Bree          -- 2
   Equal Support -- 3
 Amos and Cole advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cole          -- 3 -- First place
   Amos          -- 2
   Equal Support -- 4
 Cole wins.
   Runoff math:
     9  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Cole 3 (60%)  ·  Amos 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cole
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Amos   |  * Bree   |    Cole   |
-----------------------------------------------------
      * Amos > |    ---     |4 - 2 - 3  |2 - 4 - 3  |
      * Bree > | 3 - 2 - 4  |   ---     |2 - 3 - 4  |
        Cole > | 3 - 4 - 2  |4 - 3 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cole — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amos       0  0  0  2  7  0  |    11   1.2
Bree       0  0  0  5  0  4  |    10   1.1
Cole       0  0  0  3  4  2  |    10   1.1
```

</details>

Everything in one file: the [`_tabulated` mirror](../brams_grading_paradox_tabulated/brams_ex6_three_winners_c3_b9_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/brams_grading_paradox/brams_ex6_three_winners_c3_b9.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_DIFFERS_ARTIFACT/brams_ex6_three_winners_c3_b9.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Exhausted ballots (conversation)](../../../00_start_here/RCV_IRV/exhausted_ballots_301.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [brams_ex3_two_candidates_c2_b5](brams_ex3_two_candidates_c2_b5.md) · [brams_grading_paradox_c3_b3](brams_grading_paradox_c3_b3.md)
