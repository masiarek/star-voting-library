# BV2142 — Ranked Robin clone independence (1/2): a no-Condorcet cycle, LH vs BV tiebreak

*Generated from [`bv2142_4gfwdq_clone_cycle_pre.yaml`](../bv2142_4gfwdq_clone_cycle_pre.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** A

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4gfwdq) · **[results ↗](https://bettervoting.com/4gfwdq/results)** (election `4gfwdq`).

**Official tie-break (lot) order:** A > B > C > D > E > F — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The electowiki clone-independence example, part 1 (before cloning), BV-backed. 33 voters; A, B, C are in a cycle (no Condorcet winner) and tie at 4 wins. The engines DIVERGE on the tie: LH ranks by total margin — A and B tie at +101, C is lower (+95) — so LH drops C and coin-flips A/B by lot (this file pins A). But BetterVoting has no margin rung for a 3-way tie: it picks at RANDOM among A, B, C, and its log says so ("C picked in random tie-breaker, more robust tiebreaker not yet implemented") — this draw elected C, a candidate LH's margin rung would eliminate. Part 2 (BV2143) adds the clones. LH-only clean pair: clone_teaming_01_pre.yaml. Lesson: 00_start_here/RCV_Ranked_Robin/rr_clone_independence.md Live results: https://bettervoting.com/4gfwdq/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:A>B>C>D>E>F
11:B>C>A>D>E>F
10:C>A>B>D>E>F
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2142_4gfwdq_clone_cycle_pre_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  A          4–1–0         4    +101  B, D, E, F
    2  B          4–1–0         4    +101  C, D, E, F
    3  C          4–1–0         4     +95  A, D, E, F
    4  D          2–3–0         2     -33  E, F
    5  E          1–4–0         1     -99  F
    6  F          0–5–0         0    -165  —

Winner — Ranked Robin (RCV-RR): A
   *** 3 candidates tie for the most wins (A, B, C) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/clone_independence/cases/bv2142_4gfwdq_clone_cycle_pre.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2143_9pr3wr_teaming_fails](bv2143_9pr3wr_teaming_fails.md) · [clone_teaming_01_pre](clone_teaming_01_pre.md) · [clone_teaming_02_post](clone_teaming_02_post.md)
