# No Condorcet Winner — Ranked Robin (Copeland): a tie LH and BV break differently

*Generated from [`bv2138_cxrf8v_ranked_robin.yaml`](../bv2138_cxrf8v_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Abby

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/cxrf8v) · **[results ↗](https://bettervoting.com/cxrf8v/results)** (election `cxrf8v`).

**Official tie-break (lot) order:** Dave > Cora > Abby > Brad > Erin — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the 'One Ranked Electorate, Many Tabulations' election (BV2138, bvid cxrf8v; BV-confirmed). 921 voters, five candidates, NO Condorcet winner (Smith set = Abby, Brad, Dave, Erin). Robert LeGrand's flagship 'the method decides' example: across ~15 methods the win splits five ways. Copeland ties Abby and Brad. LH breaks the tie by total margin → Abby; BetterVoting breaks it head-to-head (Brad beats Abby 463–458) → Brad. A documented LH-vs-BV tiebreak DIVERGENCE: expected_winners is LH's Abby; BV's live result is Brad.

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

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2138_cxrf8v_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Abby       3–1–0         3    +146  Dave, Erin, Cora
    2  Brad       3–1–0         3     +34  Abby, Erin, Cora
    3  Dave       2–2–0         2     -50  Brad, Cora
    4  Erin       2–2–0         2    -126  Dave, Cora
    5  Cora       0–4–0         0      -4  —

Winner — Ranked Robin (RCV-RR): Abby
   *** 2 candidates tie for the most wins (Abby, Brad) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/no_condorcet_bv2138/cases/bv2138_cxrf8v_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2138_cxrf8v_irv](bv2138_cxrf8v_irv.md) · [bv2138_cxrf8v_star](bv2138_cxrf8v_star.md) · [bv2138_cxrf8v_stv](bv2138_cxrf8v_stv.md)
