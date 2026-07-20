# Equal support example ("I like both flavors")

*Generated from [`01c_c2_b3_two-candidates.yaml`](../01c_c2_b3_two-candidates.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Choco

## Scenario

Now we add a third ballot, from Julia, who likes both flavors equally (both 5 stars).
Because she scores the two finalists the same, her ballot counts as
"Equal Support = 1" in the Automatic Runoff Round.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Choco,Vanilla
    5,      3       # Caroline — Choco (5) over Vanilla (3)
    5,      0       # George - he likes only one flavor (Choco)
    5,      5       # Julia - she likes both flavors equally
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Choco,Vanilla
    5,      3
    5,      0
    5,      5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Choco         -- 15 -- First place
   Vanilla       --  8 -- Second place
 Choco and Vanilla advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Choco         -- 2 -- First place
   Vanilla       -- 0
   Equal Support -- 1
 Choco wins.
   Runoff math:
     3  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Choco 2 (100%)  ·  Vanilla 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Choco
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |   * Choco   | * Vanilla  |
--------------------------------------------
      * Choco > |     ---     | 2 - 1 - 0  |
    * Vanilla > |  0 - 1 - 2  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Choco — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Choco      3  0  0  0  0  0  |    15   5.0
Vanilla    1  0  1  0  0  1  |     8   2.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/01c_c2_b3_two-candidates_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/silly_two_cand_STAR/cases/01c_c2_b3_two-candidates.yaml
```

## See also

- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md)
