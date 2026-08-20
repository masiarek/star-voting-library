---
search:
  exclude: true
---

# BV2142 — Ranked Robin clone independence (1/2): a no-Condorcet cycle, LH vs BV tiebreak

*Generated from [`bv2142_4gfwdq_clone_cycle_pre.yaml`](../bv2142_4gfwdq_clone_cycle_pre.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** A

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4gfwdq) · **[results ↗](https://bettervoting.com/4gfwdq/results)** (election `4gfwdq` · test `BV2142`).

**Official tie-break (lot) order:** A > B > C > D > E > F — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The electowiki clone-independence example, part 1 (before cloning), BV-backed. 33 voters; A, B, C are in a cycle (no Condorcet winner) and tie at 4 wins. The engines DIVERGE on the tie: LH ranks by total margin — A and B tie at +101, C is lower (+95) — so LH drops C and coin-flips A/B by lot (this file pins A). But BetterVoting has no margin rung for a 3-way tie: it picks at RANDOM among A, B, C, and its log says so ("C picked in random tie-breaker, more robust tiebreaker not yet implemented") — this draw elected C, a candidate LH's margin rung would eliminate. Part 2 (BV2143) adds the clones. LH-only clean pair: clone_teaming_01_pre.yaml. Lesson: 05_Ranked_Robin/01_Learn/rr_clone_independence.md Live results: https://bettervoting.com/4gfwdq/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:A>B>C>D>E>F
11:B>C>A>D>E>F
10:C>A>B>D>E>F
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 33 ballots (ranked ballots).

Ballots:
    12 × A > B > C > D > E > F
    11 × B > C > A > D > E > F
    10 × C > A > B > D > E > F

Round-Robin — every pair, head-to-head (For – Against):
   A  beats B   22 – 11
   C  beats A   21 – 12
   A  beats D   33 –  0
   A  beats E   33 –  0
   A  beats F   33 –  0
   B  beats C   23 – 10
   B  beats D   33 –  0
   B  beats E   33 –  0
   B  beats F   33 –  0
   C  beats D   33 –  0
   C  beats E   33 –  0
   C  beats F   33 –  0
   D  beats E   33 –  0
   D  beats F   33 –  0
   E  beats F   33 –  0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |      A       |     B       |     C       |     D       |     E       |     F       |
--------------------------------------------------------------------------------------------
  A > |     ---      |22 -  0 - 11 |12 -  0 - 21 |33 -  0 -  0 |33 -  0 -  0 |33 -  0 -  0 |
  B > | 11 -  0 - 22 |    ---      |23 -  0 - 10 |33 -  0 -  0 |33 -  0 -  0 |33 -  0 -  0 |
  C > | 21 -  0 - 12 |10 -  0 - 23 |    ---      |33 -  0 -  0 |33 -  0 -  0 |33 -  0 -  0 |
  D > |  0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 |    ---      |33 -  0 -  0 |33 -  0 -  0 |
  E > |  0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 |    ---      |33 -  0 -  0 |
  F > |  0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 | 0 -  0 - 33 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  A          4–1–0         4    +101            +2  B, D, E, F
    2  B          4–1–0         4    +101            +2  C, D, E, F
    3  C          4–1–0         4     +95            -4  A, D, E, F
    4  D          2–3–0         2     -33             —  E, F
    5  E          1–4–0         1     -99             —  F
    6  F          0–5–0         0    -165             —  —

Winner — Ranked Robin (RCV-RR): A
   *** 3 candidates tie for the most wins (A, B, C) — a Condorcet cycle (no candidate beats all others). Neither the 1st nor the 2nd Degree tiebreaker separates them — resolved by lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 6): A, B, C
   Outside (3):        D, E, F
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner A is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2142_4gfwdq_clone_cycle_pre_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/clone_independence/cases/bv2142_4gfwdq_clone_cycle_pre.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2143_9pr3wr_teaming_fails](bv2143_9pr3wr_teaming_fails.md) · [clone_teaming_01_pre](clone_teaming_01_pre.md) · [clone_teaming_02_post](clone_teaming_02_post.md)
