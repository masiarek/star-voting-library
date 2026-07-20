# Equal & opposite — the base election (Comet wins)

*Generated from [`equal_and_opposite_01_base_c6_b3.yaml`](../equal_and_opposite_01_base_c6_b3.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Comet

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/36f4v2) · **[results ↗](https://bettervoting.com/36f4v2/results)** (election `36f4v2`).

## Scenario

Three voters, six candidates (Astra, Bolt, Comet, Dune, Echo, Flux). STAR
elects Comet — highest score total (14) and winner of the automatic runoff
over Echo, 2–1. This is the "before" half of the Equally Weighted Vote
demonstration: its twin adds two voters with exact-opposite ballots and shows
the winner never moves. See the lesson: equal_and_opposite/README.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Astra, Bolt, Comet, Dune, Echo, Flux
3, 2, 5, 1, 4, 0
2, 4, 5, 0, 3, 1
4, 1, 4, 2, 5, 0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Astra,Bolt,Comet,Dune,Echo,Flux
    3,   2,    5,   1,   4,   0
    2,   4,    5,   0,   3,   1
    4,   1,    4,   2,   5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Comet         -- 14 -- First place
   Echo          -- 12 -- Second place
   Astra         --  9
   Bolt          --  7
   Dune          --  3
   Flux          --  1
 Comet and Echo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Comet         -- 2 -- First place
   Echo          -- 1
   Equal Support -- 0
 Comet wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Comet 2 (67%)  ·  Echo 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Comet
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    Astra   |    Bolt   | * Comet   |    Dune   |  * Echo   |    Flux   |
-----------------------------------------------------------------------------------------
       Astra > |    ---     |2 - 0 - 1  |0 - 1 - 2  |3 - 0 - 0  |0 - 0 - 3  |3 - 0 - 0  |
        Bolt > | 1 - 0 - 2  |   ---     |0 - 0 - 3  |2 - 0 - 1  |1 - 0 - 2  |3 - 0 - 0  |
     * Comet > | 2 - 1 - 0  |3 - 0 - 0  |   ---     |3 - 0 - 0  |2 - 0 - 1  |3 - 0 - 0  |
        Dune > | 0 - 0 - 3  |1 - 0 - 2  |0 - 0 - 3  |   ---     |0 - 0 - 3  |2 - 0 - 1  |
      * Echo > | 3 - 0 - 0  |2 - 0 - 1  |1 - 0 - 2  |3 - 0 - 0  |   ---     |3 - 0 - 0  |
        Flux > | 0 - 0 - 3  |0 - 0 - 3  |0 - 0 - 3  |1 - 0 - 2  |0 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Comet — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Astra      0  1  1  1  0  0  |     9   3.0
Bolt       0  1  0  1  1  0  |     7   2.3
Comet      2  1  0  0  0  0  |    14   4.7
Dune       0  0  0  1  1  1  |     3   1.0
Echo       1  1  1  0  0  0  |    12   4.0
Flux       0  0  0  0  1  2  |     1   0.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../equal_and_opposite_tabulated/equal_and_opposite_01_base_c6_b3_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/equal_and_opposite/equal_and_opposite_01_base_c6_b3.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [equal_and_opposite_02_plus_cancel_c6_b5](equal_and_opposite_02_plus_cancel_c6_b5.md)
