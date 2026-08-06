---
search:
  exclude: true
---

# Margins matter — the textbook profile at its printed size (304 ballots, LH-only)

*Generated from [`margins_paper_exact_304.yaml`](../margins_paper_exact_304.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** b

**Official tie-break (lot) order:** a > b > c — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The source profile exactly as it is printed in the textbook: 102 a>b>c, 101 b>c>a, 100 c>a>b, 1 c>b>a, with a/b/c kept as the book's own placeholder letters. Reference artifact for reproducibility — LH-only, no BetterVoting election, because the twelve-ballot version (margins_ranked_robin.yaml) is the teaching copy. Everything structural matches: Copeland ties all three, the symmetric Borda scores are 0 / +2 / -2, plurality elects a, RCV-IRV elects c. Two things this size shows that the small one cannot. First, the margins are 100 / 102 / 100 — near-identical, so margin-weighting breaks a dead heat by a HAIR, where the shrunk version's 2 / 4 / 2 makes the gap look decisive. Second, the bloc counts are coprime (gcd 1), so this profile is not a scaled-up copy of anything smaller — and the lone 1-voter is load-bearing: delete it and the symmetric Borda scores become +2 / +2 / -4, a TIE between a and b, and RCV-IRV flips from c to a.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
102:a>b>c
101:b>c>a
100:c>a>b
1:c>b>a
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 304 ballots (ranked ballots).

Ballots:
   102 × a > b > c
   101 × b > c > a
   100 × c > a > b
     1 × c > b > a

Round-Robin — every pair, head-to-head (For – Against):
   a  beats b   202 – 102
   c  beats a   202 – 102
   b  beats c   203 – 101

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |        a        |       b        |       c        |
-----------------------------------------------------------
  a > |       ---       |202 -   0 - 102 |102 -   0 - 202 |
  b > | 102 -   0 - 202 |      ---       |203 -   0 - 101 |
  c > | 202 -   0 - 102 |101 -   0 - 203 |      ---       |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  b          1–1–0         1      +2  c
    2  a          1–1–0         1      +0  b
    3  c          1–1–0         1      -2  a

Winner — Ranked Robin (RCV-RR): b
   *** 3 candidates tie for the most wins (a, b, c) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): a, b, c
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner b is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/margins_paper_exact_304_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/copeland_vs_borda_margins/cases/margins_paper_exact_304.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [margins_irv](margins_irv.md) · [margins_ranked_robin](margins_ranked_robin.md) · [margins_star](margins_star.md)
