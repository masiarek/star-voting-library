# Center Squeeze — STAR (ranks→scores): agrees with Condorcet, not IRV

*Generated from [`bv2137_ywckmg_star.yaml`](../bv2137_ywckmg_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Anderson

## Scenario

One of four races in the Center Squeeze election (BV2137, bvid ywckmg; BV-confirmed). 100 voters, three candidates, ONE ranked electorate tabulated four ways. Anderson is the Condorcet winner (beats Reagan 55–45, Carter 65–35) but holds the fewest first-choices (20). Ranks mapped to 0–5 scores (top=5,bottom=1). Anderson tops the score round (340) and wins the automatic runoff → STAR → Anderson, matching Ranked Robin, unlike IRV.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Reagan,Anderson,Carter
45: 5,3,1
20: 1,5,3
35: 1,3,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Anderson
  Choose-One (Plurality) = Reagan   (differs from STAR)
  RCV-IRV                = Carter   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: center_squeeze_bv2137_tabulated/bv2137_ywckmg_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Reagan,Anderson,Carter
   45 ×      5,       3,     1
   35 ×      1,       3,     5
   20 ×      1,       5,     3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Anderson      -- 340 -- First place
   Carter        -- 280 -- Tied for second place
   Reagan        -- 280 -- Tied for second place
 Anderson advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Carter        -- 55 -- Second place
   Reagan        -- 45
   Equal Support --  0
 Anderson and Carter advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Anderson      -- 65 -- First place
   Carter        -- 35
   Equal Support --  0
 Anderson wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Anderson 65 (65%)  ·  Carter 35 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Anderson
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Reagan   | * Anderson  |    Carter   |
-------------------------------------------------------------
      * Reagan > |     ---      |45 -  0 - 55 |45 -  0 - 55 |
    * Anderson > | 55 -  0 - 45 |    ---      |65 -  0 - 35 |
        Carter > | 55 -  0 - 45 |35 -  0 - 65 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Anderson — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Reagan     45   0   0   0  55   0  |   280   2.8
Anderson   20   0  80   0   0   0  |   340   3.4
Carter     35   0  20   0  45   0  |   280   2.8
```

</details>

Everything in one file: the [`_tabulated` mirror](../center_squeeze_bv2137_tabulated/bv2137_ywckmg_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/center_squeeze_bv2137/bv2137_ywckmg_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2137_ywckmg_star.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2137_ywckmg_irv](bv2137_ywckmg_irv.md) · [bv2137_ywckmg_ranked_robin](bv2137_ywckmg_ranked_robin.md) · [bv2137_ywckmg_stv](bv2137_ywckmg_stv.md)
