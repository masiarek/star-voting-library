---
search:
  exclude: true
---

# Margins matter — Ranked Robin (Copeland) ties all three

*Generated from [`margins_ranked_robin.yaml`](../margins_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn) · **1 seat** · **Expected winner:** Berry

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kdjjkq) · **[results ↗](https://bettervoting.com/kdjjkq/results)** (election `kdjjkq` · test `BV2251`).

**Official tie-break (lot) order:** Almond > Berry > Cocoa — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Twelve gelato voters, three flavours, a rock-paper-scissors cycle: Almond beats Berry 7-5, Berry beats Cocoa 8-4, Cocoa beats Almond 7-5. Copeland counts WINS and throws the margins away, so every flavour goes 1-1-0 and the Copeland winning set is all three. That is the whole point of the profile: the same tournament, WEIGHTED by those margins, is the Borda count — and Borda separates them (Berry +2, Almond 0, Cocoa -2). LH breaks the Copeland tie by total margin (Berry +2) and elects Berry, which is exactly the margin-weighted answer; BetterVoting falls past its head-to-head rung on a 3-way tie and picks at RANDOM, so BV's crowned winner is a coin flip and only its pairwise matrix is freezable. Structural twin of the 304-ballot textbook profile in margins_paper_exact_304.yaml.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Almond>Berry>Cocoa
Almond>Berry>Cocoa
Almond>Berry>Cocoa
Almond>Berry>Cocoa
Almond>Berry>Cocoa
Berry>Cocoa>Almond
Berry>Cocoa>Almond
Berry>Cocoa>Almond
Cocoa>Almond>Berry
Cocoa>Almond>Berry
Cocoa>Berry>Almond
Cocoa>Berry>Almond
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 12 ballots (ranked ballots).

Ballots:
     5 × Almond > Berry > Cocoa
     3 × Berry > Cocoa > Almond
     2 × Cocoa > Almond > Berry
     2 × Cocoa > Berry > Almond

Round-Robin — every pair, head-to-head (For – Against):
   Almond  beats Berry    7 – 5
   Cocoa   beats Almond   7 – 5
   Berry   beats Cocoa    8 – 4

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |  Almond   |  Berry   |  Cocoa   |
----------------------------------------------
  Almond > |    ---    |7 - 0 - 5 |5 - 0 - 7 |
   Berry > | 5 - 0 - 7 |   ---    |8 - 0 - 4 |
   Cocoa > | 7 - 0 - 5 |4 - 0 - 8 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Berry      1–1–0         1      +2  Cocoa
    2  Almond     1–1–0         1      +0  Berry
    3  Cocoa      1–1–0         1      -2  Almond

Winner — Ranked Robin (RCV-RR): Berry
   *** 3 candidates tie for the most wins (Almond, Berry, Cocoa) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): Almond, Berry, Cocoa
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Berry is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/margins_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/copeland_vs_borda_margins/cases/margins_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [margins_irv](margins_irv.md) · [margins_paper_exact_304](margins_paper_exact_304.md) · [margins_star](margins_star.md)
