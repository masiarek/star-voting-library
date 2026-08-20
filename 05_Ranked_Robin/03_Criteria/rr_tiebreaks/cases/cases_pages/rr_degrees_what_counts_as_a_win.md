---
search:
  exclude: true
---

# What counts as a win — the rung before the 1st Degree

*Generated from [`rr_degrees_what_counts_as_a_win.yaml`](../rr_degrees_what_counts_as_a_win.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Bella

## Scenario

Four voters rank four candidates, each with a different favourite, and two of the six matchups end level: Aaron and Bella split 2-2, and so do Bella and Caleb. Nobody ranked anyone equal — the draws come from the electorate dividing evenly, which is the ordinary way a small round robin produces one.
That leaves two candidates at the top with different-shaped records:

  Bella  1 win, 2 draws, 0 losses   — she is never beaten
  Dana   2 wins, 0 draws, 1 loss    — beaten only by Bella

Ranked Robin's tie-break protocol has a famous four-degree ladder, but this file is about the rule that runs BEFORE any of it: who is tied for the top in the first place. The published definition is "elect the candidate who pairwise beats the greatest number of candidates" — read literally, that counts wins and nothing else, and the source's own worked example scores a candidate with three wins and a draw as 3, not 3.5. Every implementation, this engine included, instead scores a draw as half a win, which is the standard Copeland tally.
The two readings elect different people here:

  wins + half-draws   Bella 2.0, Dana 2.0 — tied, so both are FINALISTS, and
                      the 1st Degree separates them on the margin of their own
                      matchup (Bella beat Dana 3-1). BELLA is elected.
  wins only           Dana 2, Bella 1, Aaron 1, Caleb 0 — no tie at all.
                      DANA is elected outright, with no tie-breaker.

Note which way the literal reading errs: it elects Dana, who lost a matchup, over Bella, who lost none. That is the reason to read it as loose drafting rather than as a rule two engines got wrong — but it is a judgement call about a published definition, not a finding, and it is written up as an open question. Lesson: degrees_of_ties.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Aaron>Bella>Dana>Caleb
Dana>Aaron>Caleb>Bella
Bella>Dana>Aaron>Caleb
Caleb>Bella>Dana>Aaron
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 4 ballots (ranked ballots).

Ballots:
     1 × Aaron > Bella > Dana > Caleb
     1 × Dana > Aaron > Caleb > Bella
     1 × Bella > Dana > Aaron > Caleb
     1 × Caleb > Bella > Dana > Aaron

Round-Robin — every pair, head-to-head (For – Against):
   Aaron  ties  Bella   2 – 2
   Dana   beats Aaron   3 – 1
   Aaron  beats Caleb   3 – 1
   Bella  beats Dana    3 – 1
   Bella  ties  Caleb   2 – 2
   Dana   beats Caleb   3 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Aaron   |  Bella   |  Dana    |  Caleb   |
--------------------------------------------------------
  Aaron > |    ---    |2 - 0 - 2 |1 - 0 - 3 |3 - 0 - 1 |
  Bella > | 2 - 0 - 2 |   ---    |3 - 0 - 1 |2 - 0 - 2 |
   Dana > | 3 - 0 - 1 |1 - 0 - 3 |   ---    |3 - 0 - 1 |
  Caleb > | 1 - 0 - 3 |2 - 0 - 2 |1 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Bella      1–0–2         2      +2            +2  Dana
    2  Dana       2–1–0         2      +2            -2  Aaron, Caleb
    3  Aaron      1–1–1       1.5      +0             —  Caleb
    4  Caleb      0–2–1       0.5      -4             —  —

Winner — Ranked Robin (RCV-RR): Bella
   *** 2 candidates tie on the highest Copeland score (2): Bella, Dana — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Bella has the greatest sum of win margins over the other finalists (+2).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 4): Bella, Dana, Aaron, Caleb
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   group held open by draws, so the strongest "candidate" is a set, not a
   person. Some members DO beat others, but no member beats them all — a draw
   blocks the sweep. No loop closes either, so there is no cycle for Minimax /
   Ranked Pairs / Schulze to resolve: which member wins is left to the
   tiebreak, not to a cycle rule. See
   05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md.
   Note: the Copeland leaders (Bella, Dana) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Bella is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   Fine print: this set contains a pairwise DRAW, and a draw is enough to keep a
   candidate in the Smith set but not in the tighter Schwartz set — so Schwartz
   may be smaller here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/rr_degrees_what_counts_as_a_win_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/rr_degrees_what_counts_as_a_win.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [bv2270_8h4bvh_head_to_head_vs_margin](bv2270_8h4bvh_head_to_head_vs_margin.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md) · [rr_degrees_finalists_vs_field](rr_degrees_finalists_vs_field.md) · [rr_degrees_three_way_cycle](rr_degrees_three_way_cycle.md)
