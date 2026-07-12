# Same as before - but this time two ballots

*Generated from [`01a_c2_b2_two-candidates.yaml`](../01a_c2_b2_two-candidates.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Chocolate

## Scenario

The same election as 01a_c2_b1 with one more identical ballot: two voters,
both scoring Chocolate 5 and Vanilla 3. Nothing changes but the totals
(10 vs 6) — a first look at how the report scales counts. Compare the two
files line by line to see exactly which numbers one added ballot moves.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Chocolate,Vanilla
        5,      3       # Caroline — Chocolate (5) over Vanilla (3)
        5,      3       # Bob — same
```

## What the engine says

Full report from the [`_tabulated` mirror](../silly_two_cand_STAR_tabulated/01a_c2_b2_two-candidates_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * Chocolate  |  * Vanilla   |
--------------------------------------------------
    * Chocolate > |      ---      |  2 - 0 - 0   |
      * Vanilla > |   0 - 0 - 2   |     ---      |

[Condorcet Winner]
  Condorcet Winner: Chocolate — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Count × Chocolate,Vanilla
    2 ×         5,      3

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Chocolate  2  0  0  0  0  0  |    10   5.0
Vanilla    0  0  2  0  0  0  |     6   3.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Chocolate     -- 10 -- First place
   Vanilla       --  6 -- Second place
 Chocolate and Vanilla advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Chocolate     -- 2 -- First place
   Vanilla       -- 0
   Equal Support -- 0
 Chocolate wins.
   Runoff math:
     2  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Chocolate 2 (100%)  ·  Vanilla 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Chocolate
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/silly_two_cand_STAR/01a_c2_b2_two-candidates.yaml
```

## See also

- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md)
