# The control case — here the runoff CONFIRMS the score leader

*Generated from [`04_c4_b3_runoff-confirms-leader.yaml`](../04_c4_b3_runoff-confirms-leader.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Blue

## Scenario

Same machinery, opposite result — and that's the point. Blue is both the biggest
star pile (14) AND the majority's preferred finalist, so the automatic runoff
simply confirms the scoring leader: Blue wins either way.

This is why STAR's runoff isn't "rigged against front-runners." It only overturns
the leader when the star total and the head-to-head majority disagree (01a-03);
when the leader really is the most-preferred candidate, the leader wins.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amber, Blue, Coral, Dune
    2,    5,     1,    0
    2,    5,     0,    1
    5,    4,     0,    0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Amber,Blue,Coral,Dune
    2,   5,    1,   0
    2,   5,    0,   1
    5,   4,    0,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Blue          -- 14 -- First place
   Amber         --  9 -- Second place
   Coral         --  1
   Dune          --  1
 Blue and Amber advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blue          -- 2 -- First place
   Amber         -- 1
   Equal Support -- 0
 Blue wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Blue 2 (67%)  ·  Amber 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Blue
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Amber   |  * Blue   |   Coral   |    Dune   |
-----------------------------------------------------------------
     * Amber > |    ---     |1 - 0 - 2  |3 - 0 - 0  |3 - 0 - 0  |
      * Blue > | 2 - 0 - 1  |   ---     |3 - 0 - 0  |3 - 0 - 0  |
       Coral > | 0 - 0 - 3  |0 - 0 - 3  |   ---     |1 - 1 - 1  |
        Dune > | 0 - 0 - 3  |0 - 0 - 3  |1 - 1 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Blue — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amber      1  0  0  2  0  0  |     9   3.0
Blue       2  1  0  0  0  0  |    14   4.7
Coral      0  0  0  0  1  2  |     1   0.3
Dune       0  0  0  0  1  2  |     1   0.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/04_c4_b3_runoff-confirms-leader_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/cases/04_c4_b3_runoff-confirms-leader.yaml
```

## See also

- [Runoff reversal (worked set)](../../README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [reversal_convincing_c3_b100](reversal_convincing_c3_b100.md) · [reversal_jarring_c3_b100](reversal_jarring_c3_b100.md)
