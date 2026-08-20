---
search:
  exclude: true
---

# No Condorcet Winner — Ranked Robin (Copeland): a two-way tie, settled head-to-head

*Generated from [`bv2138_cxrf8v_ranked_robin.yaml`](../bv2138_cxrf8v_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Brad

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/cxrf8v) · **[results ↗](https://bettervoting.com/cxrf8v/results)** (election `cxrf8v` · test `BV2138`).

**Official tie-break (lot) order:** Dave > Cora > Abby > Brad > Erin — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the 'One Ranked Electorate, Many Tabulations' election (BV2138, bvid cxrf8v; BV-confirmed). 921 voters, five candidates, NO Condorcet winner (Smith set = Abby, Brad, Dave, Erin). Robert LeGrand's flagship 'the method decides' example: across ~15 methods the win splits five ways. Copeland ties Abby and Brad, and Ranked Robin's 1st Degree tiebreaker asks how the tied finalists did against each other: Brad beats Abby 463–458, so Brad is elected. Both engines agree, and BV's live result is Brad. This case was filed for years as an LH-vs-BV DIVERGENCE — the engine broke the tie on total margin over the whole field and answered Abby — until 2026-08-19, when the ladder was corrected to the method's own degrees and the divergence turned out to be a bug on our side, not a difference of opinion. See 05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
98:Abby>Cora>Erin>Dave>Brad
64:Brad>Abby>Erin>Cora>Dave
12:Brad>Abby>Erin>Dave>Cora
98:Brad>Erin>Abby>Cora>Dave
13:Brad>Erin>Abby>Dave>Cora
125:Brad>Erin>Dave>Abby>Cora
124:Cora>Abby>Erin>Dave>Brad
76:Cora>Erin>Abby>Dave>Brad
21:Dave>Abby>Brad>Erin>Cora
30:Dave>Brad>Abby>Erin>Cora
98:Dave>Brad>Erin>Cora>Abby
139:Dave>Cora>Abby>Brad>Erin
23:Dave>Cora>Brad>Abby>Erin
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 921 ballots (ranked ballots).

Ballots:
    98 × Abby > Cora > Erin > Dave > Brad
    64 × Brad > Abby > Erin > Cora > Dave
    12 × Brad > Abby > Erin > Dave > Cora
    98 × Brad > Erin > Abby > Cora > Dave
    13 × Brad > Erin > Abby > Dave > Cora
   125 × Brad > Erin > Dave > Abby > Cora
   124 × Cora > Abby > Erin > Dave > Brad
    76 × Cora > Erin > Abby > Dave > Brad
    21 × Dave > Abby > Brad > Erin > Cora
    30 × Dave > Brad > Abby > Erin > Cora
    98 × Dave > Brad > Erin > Cora > Abby
   139 × Dave > Cora > Abby > Brad > Erin
    23 × Dave > Cora > Brad > Abby > Erin

Round-Robin — every pair, head-to-head (For – Against):
   Abby  beats Cora   461 – 460
   Abby  beats Erin   511 – 410
   Abby  beats Dave   485 – 436
   Brad  beats Abby   463 – 458
   Erin  beats Cora   461 – 460
   Dave  beats Cora   461 – 460
   Brad  beats Cora   461 – 460
   Erin  beats Dave   610 – 311
   Brad  beats Erin   623 – 298
   Dave  beats Brad   609 – 312

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |      Abby       |     Cora       |     Erin       |     Dave       |     Brad       |
------------------------------------------------------------------------------------------------
  Abby > |       ---       |461 -   0 - 460 |511 -   0 - 410 |485 -   0 - 436 |458 -   0 - 463 |
  Cora > | 460 -   0 - 461 |      ---       |460 -   0 - 461 |460 -   0 - 461 |460 -   0 - 461 |
  Erin > | 410 -   0 - 511 |461 -   0 - 460 |      ---       |610 -   0 - 311 |298 -   0 - 623 |
  Dave > | 436 -   0 - 485 |461 -   0 - 460 |311 -   0 - 610 |      ---       |609 -   0 - 312 |
  Brad > | 463 -   0 - 458 |461 -   0 - 460 |623 -   0 - 298 |312 -   0 - 609 |      ---       |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Brad       3–1–0         3     +34            +5  Abby, Erin, Cora
    2  Abby       3–1–0         3    +146            -5  Erin, Dave, Cora
    3  Erin       2–2–0         2    -126             —  Dave, Cora
    4  Dave       2–2–0         2     -50             —  Brad, Cora
    5  Cora       0–4–0         0      -4             —  —

Winner — Ranked Robin (RCV-RR): Brad
   *** 2 candidates tie for the most wins (Abby, Brad) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Brad has the greatest sum of win margins over the other finalists (+5).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 5): Abby, Brad, Erin, Dave
   Outside (1):        Cora
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (Abby, Brad) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Brad is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2138_cxrf8v_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/no_condorcet_bv2138/cases/bv2138_cxrf8v_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2138_cxrf8v_irv](bv2138_cxrf8v_irv.md) · [bv2138_cxrf8v_star](bv2138_cxrf8v_star.md) · [bv2138_cxrf8v_stv](bv2138_cxrf8v_stv.md)
