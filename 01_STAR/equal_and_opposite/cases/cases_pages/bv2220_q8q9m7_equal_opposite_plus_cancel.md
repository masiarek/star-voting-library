# Equal & opposite — add two mirror ballots, Comet still wins

*Generated from [`bv2220_q8q9m7_equal_opposite_plus_cancel.yaml`](../bv2220_q8q9m7_equal_opposite_plus_cancel.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Comet

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/q8q9m7) · **[results ↗](https://bettervoting.com/q8q9m7/results)** (election `q8q9m7`).

## Scenario

The base election plus two voters with exact-opposite opinions on every
candidate — their scores sum to 5 for each (Astra 2+3, Bolt 1+4, Comet 0+5,
Dune 1+4, Echo 5+0, Flux 4+1). Every candidate's score total rises by exactly
5, so the scoring order is untouched, and the two ballots cancel 1–1 in the
automatic runoff. STAR still elects Comet: an equally weighted vote,
demonstrated — any ballot can be perfectly cancelled by its exact opposite,
which is why STAR has no forced vote-splitting. See equal_and_opposite/README.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Astra, Bolt, Comet, Dune, Echo, Flux
3, 2, 5, 1, 4, 0
2, 4, 5, 0, 3, 1
4, 1, 4, 2, 5, 0
2, 1, 0, 1, 5, 4    # mirror A — exact opposite of mirror B
3, 4, 5, 4, 0, 1    # mirror B — exact opposite of mirror A
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Astra,Bolt,Comet,Dune,Echo,Flux
    3,   2,    5,   1,   4,   0
    2,   4,    5,   0,   3,   1
    4,   1,    4,   2,   5,   0
    2,   1,    0,   1,   5,   4
    3,   4,    5,   4,   0,   1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Comet         -- 19 -- First place
   Echo          -- 17 -- Second place
   Astra         -- 14
   Bolt          -- 12
   Dune          --  8
   Flux          --  6
 Comet and Echo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Comet         -- 3 -- First place
   Echo          -- 2
   Equal Support -- 0
 Comet wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Comet 3 (60%)  ·  Echo 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Comet
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    Astra   |    Bolt   | * Comet   |    Dune   |  * Echo   |    Flux   |
-----------------------------------------------------------------------------------------
       Astra > |    ---     |3 - 0 - 2  |1 - 1 - 3  |4 - 0 - 1  |1 - 0 - 4  |4 - 0 - 1  |
        Bolt > | 2 - 0 - 3  |   ---     |1 - 0 - 4  |2 - 2 - 1  |2 - 0 - 3  |4 - 0 - 1  |
     * Comet > | 3 - 1 - 1  |4 - 0 - 1  |   ---     |4 - 0 - 1  |3 - 0 - 2  |4 - 0 - 1  |
        Dune > | 1 - 0 - 4  |1 - 2 - 2  |1 - 0 - 4  |   ---     |1 - 0 - 4  |3 - 0 - 2  |
      * Echo > | 4 - 0 - 1  |3 - 0 - 2  |2 - 0 - 3  |4 - 0 - 1  |   ---     |4 - 0 - 1  |
        Flux > | 1 - 0 - 4  |1 - 0 - 4  |1 - 0 - 4  |2 - 0 - 3  |1 - 0 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Comet — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Astra      0  1  2  2  0  0  |    14   2.8
Bolt       0  2  0  1  2  0  |    12   2.4
Comet      3  1  0  0  0  1  |    19   3.8
Dune       0  1  0  1  2  1  |     8   1.6
Echo       2  1  1  0  0  1  |    17   3.4
Flux       0  1  0  0  2  2  |     6   1.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2220_q8q9m7_equal_opposite_plus_cancel_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/equal_and_opposite/cases/bv2220_q8q9m7_equal_opposite_plus_cancel.yaml
```

## See also

- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2219_36f4v2_equal_opposite_base](bv2219_36f4v2_equal_opposite_base.md)
