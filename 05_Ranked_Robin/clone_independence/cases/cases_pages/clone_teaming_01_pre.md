# Clone independence (1/2) — before cloning: A, B, C tie in a cycle

*Generated from [`clone_teaming_01_pre.yaml`](../clone_teaming_01_pre.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** A

**Official tie-break (lot) order:** A > B > C > D > E > F — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The electowiki Ranked Robin clone-independence example, part 1 of 2 (the "before"). 33 voters, six candidates; A, B, C sit in a top cycle (A beats B, B beats C, C beats A) and tie for the most pairwise wins (4 each). Ranked Robin's tiebreak looks at total win margin: A and B tie there too (+101 each), C is lower (+95), so C is dropped and the A-vs-B tie is settled by lot — a coin flip. This file pins the lot to A. The point of the pair is what a faction can do about that coin flip: see part 2, clone_teaming_02_post, where the A-faction runs clones to convert this 50/50 into a certain win. This is a clone-independence (teaming) FAILURE, and it can only happen when there is no Condorcet winner. Companion: clone_teaming_02_post.yaml · lesson: 00_start_here/RCV_Ranked_Robin/rr_clone_independence.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:A>B>C>D>E>F
11:B>C>A>D>E>F
10:C>A>B>D>E>F
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/clone_teaming_01_pre_tabulated.txt) (regenerated on every run; every analysis forced on):

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
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/clone_independence/cases/clone_teaming_01_pre.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2142_4gfwdq_clone_cycle_pre](bv2142_4gfwdq_clone_cycle_pre.md) · [bv2143_9pr3wr_teaming_fails](bv2143_9pr3wr_teaming_fails.md) · [clone_teaming_02_post](clone_teaming_02_post.md)
