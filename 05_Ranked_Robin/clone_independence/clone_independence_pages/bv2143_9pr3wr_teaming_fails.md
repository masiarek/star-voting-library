# BV2143 — Ranked Robin clone independence (2/2): teaming succeeds on LH, FAILS on BV

*Generated from [`bv2143_9pr3wr_teaming_fails.yaml`](../bv2143_9pr3wr_teaming_fails.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** A1

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9pr3wr) · **[results ↗](https://bettervoting.com/9pr3wr/results)** (election `9pr3wr`).

**Official tie-break (lot) order:** A1 > A2 > B > C > D > E > F — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The electowiki clone-independence example, part 2 (teaming), BV-backed. Same election as BV2142 but the A-faction runs clones A1, A2. The two engines reach OPPOSITE winners from identical ballots: A1 and C tie at 5 wins. LH breaks it by total margin — A1 +134 beats C +104 — so LH elects A1, and the teaming attack SUCCEEDS (this file pins lot but margin already decides). BetterVoting breaks the 2-way tie by head-to-head instead, and C beats A1 21-12, so BV elects C (tieBreakType "none", log "C preferred over A1 in runoff") — the teaming attack FAILS on BV. Same ballots, different tiebreak, different winner: the clone failure is a property of the margin rule, not of Ranked Robin as such. LH-only clean pair: clone_teaming_02_post.yaml. Lesson: 00_start_here/RCV_Ranked_Robin/rr_clone_independence.md Live results: https://bettervoting.com/9pr3wr/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:A1>A2>B>C>D>E>F
11:B>C>A1>A2>D>E>F
10:C>A1>A2>B>D>E>F
```

## What the engine says

Full report from the [`_tabulated` mirror](../clone_independence_tabulated/bv2143_9pr3wr_teaming_fails_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  A1         5–1–0         5    +134  B, A2, D, E, F
    2  C          5–1–0         5    +104  A1, A2, D, E, F
    3  B          4–2–0         4     +90  C, D, E, F
    4  A2         4–2–0         4     +68  B, D, E, F
    5  D          2–4–0         2     -66  E, F
    6  E          1–5–0         1    -132  F
    7  F          0–6–0         0    -198  —

Winner — Ranked Robin (RCV-RR): A1
   *** 2 candidates tie for the most wins (A1, C) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/clone_independence/bv2143_9pr3wr_teaming_fails.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2142_4gfwdq_clone_cycle_pre](bv2142_4gfwdq_clone_cycle_pre.md) · [clone_teaming_01_pre](clone_teaming_01_pre.md) · [clone_teaming_02_post](clone_teaming_02_post.md)
