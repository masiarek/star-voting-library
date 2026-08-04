---
search:
  exclude: true
---

# Ranked Robin — the half-point for a draw decides the election (LH-only)

*Generated from [`copeland_half_credit_decides.yaml`](../copeland_half_credit_decides.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn) · **1 seat** · **Expected winner:** Alice

**Official tie-break (lot) order:** Alice > Bruno > Carmen > Dmitri > Elena — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

30 ranked ballots, 5 candidates: the chess club elects its president. This case isolates the ONE thing that separates the Copeland score from a raw win count — the half-credit a drawn matchup earns.
Alice finishes 2-1-1 — winning two head-to-heads, DRAWING one, and outright LOSING to Carmen. Carmen and Dmitri each finish 2-2-0 and Bruno 1-1-2, so three rivals match Alice on raw wins, and one of them won their face-to-face matchup. Yet Alice wins, because Copeland scores a draw as half a win: Alice 2 + 0.5 = 2.5 against three candidates on exactly 2.0. The half-point IS the margin of victory.
Two lessons ride on that. First, "most head-to-head wins" is a shorthand, not the rule — the rule is the Copeland score, and the two come apart the moment any matchup is drawn. Second, Ranked Robin does not promise to elect someone who beat everybody; when nobody beats everybody, it elects the best overall round-robin record, and that winner may well have lost a match.
LH-ONLY ON PURPOSE. Nothing here is un-freezable — the result is fully deterministic (Alice is the unique Copeland leader, so no tiebreak is reached) — but the case is a pure engine-mechanics illustration with no BetterVoting election behind it. Compare the sibling case dead_heat_lot_tiebreak, where the half-credit produces a TIE and the lot ladder has to finish the job; here it produces a decisive, outright winner.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
9:Alice>Elena>Dmitri>Bruno>Carmen
8:Carmen>Bruno>Alice>Elena>Dmitri
7:Dmitri>Bruno>Carmen>Alice>Elena
6:Carmen>Alice>Dmitri>Elena>Bruno
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 30 ballots (ranked ballots).

Ballots:
     9 × Alice > Elena > Dmitri > Bruno > Carmen
     8 × Carmen > Bruno > Alice > Elena > Dmitri
     7 × Dmitri > Bruno > Carmen > Alice > Elena
     6 × Carmen > Alice > Dmitri > Elena > Bruno

Round-Robin — every pair, head-to-head (For – Against):
   Alice   beats Elena    30 –  0
   Alice   beats Dmitri   23 –  7
   Alice   ties  Bruno    15 – 15
   Carmen  beats Alice    21 –  9
   Elena   beats Dmitri   17 – 13
   Elena   ties  Bruno    15 – 15
   Carmen  beats Elena    21 –  9
   Dmitri  beats Bruno    22 –  8
   Dmitri  beats Carmen   16 – 14
   Bruno   beats Carmen   16 – 14

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |    Alice     |   Elena     |   Dmitri    |   Bruno     |   Carmen    |
-----------------------------------------------------------------------------------
   Alice > |     ---      |30 -  0 -  0 |23 -  0 -  7 |15 -  0 - 15 | 9 -  0 - 21 |
   Elena > |  0 -  0 - 30 |    ---      |17 -  0 - 13 |15 -  0 - 15 | 9 -  0 - 21 |
  Dmitri > |  7 -  0 - 23 |13 -  0 - 17 |    ---      |22 -  0 -  8 |16 -  0 - 14 |
   Bruno > | 15 -  0 - 15 |15 -  0 - 15 | 8 -  0 - 22 |    ---      |16 -  0 - 14 |
  Carmen > | 21 -  0 -  9 |21 -  0 -  9 |14 -  0 - 16 |14 -  0 - 16 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Alice      2–1–1       2.5     +34  Dmitri, Elena
    2  Carmen     2–2–0         2     +20  Alice, Elena
    3  Dmitri     2–2–0         2      -4  Carmen, Bruno
    4  Bruno      1–1–2         2     -12  Carmen
    5  Elena      1–2–1       1.5     -38  Dmitri

Winner — Ranked Robin (RCV-RR): Alice
   the highest Copeland score (2.5 = wins + ½·ties).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (5 of 5): Alice, Dmitri, Bruno, Carmen, Elena
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (Alice) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Alice is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   Fine print: this set contains a pairwise DRAW, and a draw is enough to keep a
   candidate in the Smith set but not in the tighter Schwartz set — so Schwartz
   may be smaller here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/copeland_half_credit_decides_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/02_Examples/copeland_score/cases/copeland_half_credit_decides.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)
