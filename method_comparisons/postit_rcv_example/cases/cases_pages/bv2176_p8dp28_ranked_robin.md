---
search:
  exclude: true
---

# The Post-it RCV example (20 voters) — Ranked Robin: a cycle, a 2-1 tie, settled head-to-head

*Generated from [`bv2176_p8dp28_ranked_robin.yaml`](../bv2176_p8dp28_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Green

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p8dp28) · **[results ↗](https://bettervoting.com/p8dp28/results)** (election `p8dp28` · test `BV2176`).

**Official tie-break (lot) order:** Purple > Green > Blue > Pink — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of three races in the Post-it RCV example (BV2176, bvid p8dp28;
BV-confirmed). The same 20 ranked ballots as the RCV-IRV race, compared
every-pair head-to-head. The pairwise picture is a genuine Condorcet cycle —
Purple beats Green 9-8, Green beats Blue 7-4, Blue beats Purple 10-9 (and
Pink beats Purple 12-8) — so no candidate beats all others, and Green and
Blue tie on record at 2-1 (Copeland 2). Ranked Robin's 1st Degree tiebreaker
looks at how the tied finalists did against EACH OTHER — Green beats Blue 7-4 —
so GREEN is elected, deterministically, and both engines say so. The frozen BV
export records Green too.
This case spent months on file as the first live BetterVoting election to show
an LH-vs-BV ladder divergence: the engine used to break the tie on total margin
over the whole field and answered BLUE (+5 vs Green's +4). That rung is Ranked
Robin's 2nd Degree, reachable only when the finalists are level against each
other, and applying it first was an engine bug, corrected 2026-08-19. See
05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md.

Live results: https://bettervoting.com/p8dp28/results
Companion races: bv2176_p8dp28_star.yaml, bv2176_p8dp28_irv.yaml.
Overview page: bv2176_p8dp28_postit_rcv_example.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Purple
Purple
Purple
Purple
Purple
Purple
Purple
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Blue>Pink
Blue>Pink
Blue>Green>Pink
Blue>Purple
Pink>Green>Purple
Pink>Purple
Pink
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 20 ballots (ranked ballots).

Ballots:
     7 × Purple
     6 × Green > Blue > Pink
     2 × Blue > Pink
     1 × Blue > Green > Pink
     1 × Blue > Purple
     1 × Pink > Green > Purple
     1 × Pink > Purple
     1 × Pink

Round-Robin — every pair, head-to-head (For – Against):
   Purple  beats Green     9 –  8
   Blue    beats Purple   10 –  9
   Pink    beats Purple   12 –  8
   Green   beats Blue      7 –  4
   Green   beats Pink      7 –  5
   Blue    beats Pink     10 –  3

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |    Purple    |   Green     |    Blue     |    Pink     |
---------------------------------------------------------------------
  Purple > |     ---      | 9 -  3 -  8 | 9 -  1 - 10 | 8 -  0 - 12 |
   Green > |  8 -  3 -  9 |    ---      | 7 -  9 -  4 | 7 -  8 -  5 |
    Blue > | 10 -  1 -  9 | 4 -  9 -  7 |    ---      |10 -  7 -  3 |
    Pink > | 12 -  0 -  8 | 5 -  8 -  7 | 3 -  7 - 10 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Green      2–1–0         2      +4            +3  Blue, Pink
    2  Blue       2–1–0         2      +5            -3  Pink, Purple
    3  Pink       1–2–0         1      -5             —  Purple
    4  Purple     1–2–0         1      -4             —  Green

Winner — Ranked Robin (RCV-RR): Green
   *** 2 candidates tie for the most wins (Green, Blue) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Green has the greatest sum of win margins over the other finalists (+3).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 4): Green, Blue, Purple, Pink
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (Green, Blue) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Green is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2176_p8dp28_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/postit_rcv_example/cases/bv2176_p8dp28_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2176_p8dp28_irv](bv2176_p8dp28_irv.md) · [bv2176_p8dp28_star](bv2176_p8dp28_star.md) · [bv2177_v8r66y_approval](bv2177_v8r66y_approval.md) · [bv2177_v8r66y_plurality](bv2177_v8r66y_plurality.md) · [bv2178_8kg698_irv](bv2178_8kg698_irv.md) · [bv2178_8kg698_ranked_robin](bv2178_8kg698_ranked_robin.md) · [bv2178_8kg698_star](bv2178_8kg698_star.md)
