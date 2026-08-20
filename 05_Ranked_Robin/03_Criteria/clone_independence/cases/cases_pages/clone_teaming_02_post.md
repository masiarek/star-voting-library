---
search:
  exclude: true
---

# Clone independence (2/2) — teaming: A runs clones, and hands the win to C

*Generated from [`clone_teaming_02_post.yaml`](../clone_teaming_02_post.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** C

**Official tie-break (lot) order:** A1 > A2 > B > C > D > E > F — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The electowiki Ranked Robin clone-independence example, part 2 of 2 (the "after"). Same election as part 1, but the A-faction now runs two clones, A1 and A2 (voters rank them together, A1>A2, in A's old slot). This "teaming" reshapes the field: by absorbing votes the clones push B out of the top tier (B falls to 4 wins while A1 and C reach 5), so the finalists are now A1 and C rather than A, B and C. Running clones therefore CHANGED THE OUTCOME — part 1 ends in a lot between A and B, part 2 elects a single winner outright — which is a clone-independence (crowding) failure, and it needs the top cycle to work. But it backfires on the faction that ran the clones. Ranked Robin's 1st Degree tiebreaker compares the finalists only, and C beats A1 head-to-head 21-12, so C wins. NOTE the tiebreak sensitivity, which is the real lesson here: the teaming ATTACK only succeeds against an engine that reaches for total margin over the whole field first (A1 +134 vs C +104) — this engine did until 2026-08-19, and electowiki's own worked example of teaming asserts the same A1 win, which its own 1st Degree rule does not support. See 05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md. Companion: clone_teaming_01_pre.yaml · lesson: 05_Ranked_Robin/01_Learn/rr_clone_independence.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:A1>A2>B>C>D>E>F
11:B>C>A1>A2>D>E>F
10:C>A1>A2>B>D>E>F
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 33 ballots (ranked ballots).

Ballots:
    12 × A1 > A2 > B > C > D > E > F
    11 × B > C > A1 > A2 > D > E > F
    10 × C > A1 > A2 > B > D > E > F

Round-Robin — every pair, head-to-head (For – Against):
   A1  beats A2   33 –  0
   A1  beats B    22 – 11
   C   beats A1   21 – 12
   A1  beats D    33 –  0
   A1  beats E    33 –  0
   A1  beats F    33 –  0
   A2  beats B    22 – 11
   C   beats A2   21 – 12
   A2  beats D    33 –  0
   A2  beats E    33 –  0
   A2  beats F    33 –  0
   B   beats C    23 – 10
   B   beats D    33 –  0
   B   beats E    33 –  0
   B   beats F    33 –  0
   C   beats D    33 –  0
   C   beats E    33 –  0
   C   beats F    33 –  0
   D   beats E    33 –  0
   D   beats F    33 –  0
   E   beats F    33 –  0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
       |      A1      |     A2      |     B       |     C       |     D       |     E       |     F       |
-----------------------------------------------------------------------------------------------------------
  A1 > |     ---      |33 -  0 -  0 |22 -  0 - 11 |12 -  0 - 21 |33 -  0 -  0 |33 -  0 -  0 |33 -  0 -  0 |
  A2 > |  0 -  0 - 33 |    ---      |22 -  0 - 11 |12 -  0 - 21 |33 -  0 -  0 |33 -  0 -  0 |33 -  0 -  0 |
   B > | 11 -  0 - 22 |11 -  0 - 22 |    ---      |23 -  0 - 10 |33 -  0 -  0 |33 -  0 -  0 |33 -  0 -  0 |
   C > | 21 -  0 - 12 |21 -  0 - 12 |10 -  0 - 23 |    ---      |33 -  0 -  0 |33 -  0 -  0 |33 -  0 -  0 |
   D > |  0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 |    ---      |33 -  0 -  0 |33 -  0 -  0 |
   E > |  0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 |    ---      |33 -  0 -  0 |
   F > |  0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  C          5–1–0         5    +104            +9  A1, A2, D, E, F
    2  A1         5–1–0         5    +134            -9  A2, B, D, E, F
    3  A2         4–2–0         4     +68             —  B, D, E, F
    4  B          4–2–0         4     +90             —  C, D, E, F
    5  D          2–4–0         2     -66             —  E, F
    6  E          1–5–0         1    -132             —  F
    7  F          0–6–0         0    -198             —  —

Winner — Ranked Robin (RCV-RR): C
   *** 2 candidates tie for the most wins (A1, C) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: C has the greatest sum of win margins over the other finalists (+9).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 7): A1, C, A2, B
   Outside (3):        D, E, F
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (A1, C) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner C is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/clone_teaming_02_post_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/clone_independence/cases/clone_teaming_02_post.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2142_4gfwdq_clone_cycle_pre](bv2142_4gfwdq_clone_cycle_pre.md) · [bv2143_9pr3wr_teaming_fails](bv2143_9pr3wr_teaming_fails.md) · [clone_teaming_01_pre](clone_teaming_01_pre.md)
