---
search:
  exclude: true
---

# Nine candidates, 25 voters — ranking all nine, counted by Ranked Robin

*Generated from [`bv2280_37yf8x_rr_full.yaml`](../bv2280_37yf8x_rr_full.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Finn

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/37yf8x) · **[results ↗](https://bettervoting.com/37yf8x/results)** (election `37yf8x` · test `BV2280`).

**Official tie-break (lot) order:** Ada > Ben > Cleo > Dev > Emma > Finn > Gus > Hugo > Iris — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

THE CONTROL. Every voter ranks all nine candidates, nothing truncated and nothing
rounded, and Ranked Robin returns Finn — the candidate who beats each of the other
eight head-to-head.

This is the full-resolution ranked ballot that Condorcet-efficiency simulations
normally hand to ranked methods. It is also an idealization: no large-field
jurisdiction issues it. bv2280_37yf8x_rr_top5.yaml cuts it down to five
ranks, which is what a real ranked ballot looks like, and the winner changes.

Compare with bv2280_37yf8x_star.yaml: the 0–5 score ballot agrees with this
one. Compare with bv2280_37yf8x_irv_full.yaml: the SAME ballots, counted by
instant runoff, do not — which is the cleanest evidence in this folder that the paper
and the count are separate things.

Construction: build_cases.py in this folder. 25 voters and 9 candidates at frozen
positions on one spectrum — Ada −0.73 · Ben −0.37 · Cleo −0.18 · Dev −0.17 ·
Emma −0.11 · Finn +0.24 · Gus +0.41 · Hugo +0.80 · Iris +0.84; utility = minus the
distance; scores = each voter's own min-max scaling onto 0–5; rankings = those same
utilities in order. Nothing is tuned to the result, and **no count in this folder is
settled by a tie-break** — that was a search constraint, so every winner here survives
any lot rule.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Ben>Cleo>Dev>Ada>Emma>Finn>Gus>Hugo>Iris    # voter at -0.43
Gus>Hugo>Iris>Finn>Emma>Dev>Cleo>Ben>Ada    # voter at +0.60
Ada>Ben>Cleo>Dev>Emma>Finn>Gus>Hugo>Iris    # voter at -0.67
Iris>Hugo>Gus>Finn>Emma>Dev>Cleo>Ben>Ada    # voter at +0.89
Finn>Gus>Emma>Dev>Cleo>Ben>Hugo>Iris>Ada    # voter at +0.18
Emma>Dev>Cleo>Ben>Finn>Gus>Ada>Hugo>Iris    # voter at -0.13
Gus>Hugo>Iris>Finn>Emma>Dev>Cleo>Ben>Ada    # voter at +0.59
Hugo>Iris>Gus>Finn>Emma>Dev>Cleo>Ben>Ada    # voter at +0.72
Gus>Finn>Emma>Hugo>Iris>Dev>Cleo>Ben>Ada    # voter at +0.34
Hugo>Iris>Gus>Finn>Emma>Dev>Cleo>Ben>Ada    # voter at +0.69
Finn>Gus>Emma>Dev>Cleo>Hugo>Iris>Ben>Ada    # voter at +0.23
Ben>Cleo>Dev>Emma>Ada>Finn>Gus>Hugo>Iris    # voter at -0.30
Ben>Ada>Cleo>Dev>Emma>Finn>Gus>Hugo>Iris    # voter at -0.51
Iris>Hugo>Gus>Finn>Emma>Dev>Cleo>Ben>Ada    # voter at +0.89
Emma>Dev>Cleo>Finn>Ben>Gus>Ada>Hugo>Iris    # voter at -0.05
Gus>Hugo>Iris>Finn>Emma>Dev>Cleo>Ben>Ada    # voter at +0.60
Finn>Gus>Emma>Dev>Cleo>Hugo>Iris>Ben>Ada    # voter at +0.28
Ben>Cleo>Dev>Emma>Ada>Finn>Gus>Hugo>Iris    # voter at -0.40
Hugo>Gus>Iris>Finn>Emma>Dev>Cleo>Ben>Ada    # voter at +0.62
Ada>Ben>Cleo>Dev>Emma>Finn>Gus>Hugo>Iris    # voter at -0.63
Finn>Gus>Emma>Dev>Cleo>Hugo>Iris>Ben>Ada    # voter at +0.27
Ada>Ben>Cleo>Dev>Emma>Finn>Gus>Hugo>Iris    # voter at -0.61
Ada>Ben>Cleo>Dev>Emma>Finn>Gus>Hugo>Iris    # voter at -1.33
Cleo>Dev>Emma>Ben>Finn>Ada>Gus>Hugo>Iris    # voter at -0.23
Ada>Ben>Cleo>Dev>Emma>Finn>Gus>Hugo>Iris    # voter at -1.82
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 25 ballots (ranked ballots).

Ballots:
     1 × Ben > Cleo > Dev > Ada > Emma > Finn > Gus > Hugo > Iris
     3 × Gus > Hugo > Iris > Finn > Emma > Dev > Cleo > Ben > Ada
     5 × Ada > Ben > Cleo > Dev > Emma > Finn > Gus > Hugo > Iris
     2 × Iris > Hugo > Gus > Finn > Emma > Dev > Cleo > Ben > Ada
     1 × Finn > Gus > Emma > Dev > Cleo > Ben > Hugo > Iris > Ada
     1 × Emma > Dev > Cleo > Ben > Finn > Gus > Ada > Hugo > Iris
     2 × Hugo > Iris > Gus > Finn > Emma > Dev > Cleo > Ben > Ada
     1 × Gus > Finn > Emma > Hugo > Iris > Dev > Cleo > Ben > Ada
     3 × Finn > Gus > Emma > Dev > Cleo > Hugo > Iris > Ben > Ada
     2 × Ben > Cleo > Dev > Emma > Ada > Finn > Gus > Hugo > Iris
     1 × Ben > Ada > Cleo > Dev > Emma > Finn > Gus > Hugo > Iris
     1 × Emma > Dev > Cleo > Finn > Ben > Gus > Ada > Hugo > Iris
     1 × Hugo > Gus > Iris > Finn > Emma > Dev > Cleo > Ben > Ada
     1 × Cleo > Dev > Emma > Ben > Finn > Ada > Gus > Hugo > Iris

Round-Robin — every pair, head-to-head (For – Against):
   Cleo  beats Ben    16 –  9
   Dev   beats Ben    16 –  9
   Ben   beats Ada    20 –  5
   Emma  beats Ben    16 –  9
   Finn  beats Ben    14 – 11
   Gus   beats Ben    13 – 12
   Ben   beats Hugo   13 – 12
   Ben   beats Iris   13 – 12
   Dev   beats Cleo   15 – 10
   Cleo  beats Ada    19 –  6
   Emma  beats Cleo   15 – 10
   Finn  beats Cleo   13 – 12
   Gus   beats Cleo   13 – 12
   Cleo  beats Hugo   16 –  9
   Cleo  beats Iris   16 –  9
   Dev   beats Ada    19 –  6
   Emma  beats Dev    15 – 10
   Finn  beats Dev    13 – 12
   Gus   beats Dev    13 – 12
   Dev   beats Hugo   16 –  9
   Dev   beats Iris   16 –  9
   Emma  beats Ada    18 –  7
   Finn  beats Ada    16 –  9
   Gus   beats Ada    15 – 10
   Hugo  beats Ada    13 – 12
   Iris  beats Ada    13 – 12
   Finn  beats Emma   13 – 12
   Gus   beats Emma   13 – 12
   Emma  beats Hugo   17 –  8
   Emma  beats Iris   17 –  8
   Finn  beats Gus    16 –  9
   Finn  beats Hugo   17 –  8
   Finn  beats Iris   17 –  8
   Gus   beats Hugo   20 –  5
   Gus   beats Iris   21 –  4
   Hugo  beats Iris   23 –  2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |     Ben      |    Cleo     |    Dev      |    Ada      |    Emma     |    Finn     |    Gus      |    Hugo     |    Iris     |
-----------------------------------------------------------------------------------------------------------------------------------------
   Ben > |     ---      | 9 -  0 - 16 | 9 -  0 - 16 |20 -  0 -  5 | 9 -  0 - 16 |11 -  0 - 14 |12 -  0 - 13 |13 -  0 - 12 |13 -  0 - 12 |
  Cleo > | 16 -  0 -  9 |    ---      |10 -  0 - 15 |19 -  0 -  6 |10 -  0 - 15 |12 -  0 - 13 |12 -  0 - 13 |16 -  0 -  9 |16 -  0 -  9 |
   Dev > | 16 -  0 -  9 |15 -  0 - 10 |    ---      |19 -  0 -  6 |10 -  0 - 15 |12 -  0 - 13 |12 -  0 - 13 |16 -  0 -  9 |16 -  0 -  9 |
   Ada > |  5 -  0 - 20 | 6 -  0 - 19 | 6 -  0 - 19 |    ---      | 7 -  0 - 18 | 9 -  0 - 16 |10 -  0 - 15 |12 -  0 - 13 |12 -  0 - 13 |
  Emma > | 16 -  0 -  9 |15 -  0 - 10 |15 -  0 - 10 |18 -  0 -  7 |    ---      |12 -  0 - 13 |12 -  0 - 13 |17 -  0 -  8 |17 -  0 -  8 |
  Finn > | 14 -  0 - 11 |13 -  0 - 12 |13 -  0 - 12 |16 -  0 -  9 |13 -  0 - 12 |    ---      |16 -  0 -  9 |17 -  0 -  8 |17 -  0 -  8 |
   Gus > | 13 -  0 - 12 |13 -  0 - 12 |13 -  0 - 12 |15 -  0 - 10 |13 -  0 - 12 | 9 -  0 - 16 |    ---      |20 -  0 -  5 |21 -  0 -  4 |
  Hugo > | 12 -  0 - 13 | 9 -  0 - 16 | 9 -  0 - 16 |13 -  0 - 12 | 8 -  0 - 17 | 8 -  0 - 17 | 5 -  0 - 20 |    ---      |23 -  0 -  2 |
  Iris > | 12 -  0 - 13 | 9 -  0 - 16 | 9 -  0 - 16 |13 -  0 - 12 | 8 -  0 - 17 | 8 -  0 - 17 | 4 -  0 - 21 | 2 -  0 - 23 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Finn       8–0–0         8     +38  Gus, Emma, Dev, Cleo, Ben, Hugo, Iris, Ada
    2  Gus        7–1–0         7     +34  Emma, Dev, Cleo, Ben, Hugo, Iris, Ada
    3  Emma       6–2–0         6     +44  Dev, Cleo, Ben, Hugo, Iris, Ada
    4  Dev        5–3–0         5     +32  Cleo, Ben, Hugo, Iris, Ada
    5  Cleo       4–4–0         4     +22  Ben, Hugo, Iris, Ada
    6  Ben        3–5–0         3      -8  Hugo, Iris, Ada
    7  Hugo       2–6–0         2     -26  Iris, Ada
    8  Iris       1–7–0         1     -70  Ada
    9  Ada        0–8–0         0     -66  —

Winner — Ranked Robin (RCV-RR): Finn
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 9): Finn
   Outside (8):        Ben, Cleo, Dev, Ada, Emma, Gus, Hugo, Iris
   One member ⇒ Finn is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Finn is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2280_37yf8x_rr_full_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/ballot_expressiveness/cases/bv2280_37yf8x_rr_full.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [ballot_expressiveness_c9_irv_top5](ballot_expressiveness_c9_irv_top5.md) · [bv2280_37yf8x_irv_full](bv2280_37yf8x_irv_full.md) · [bv2280_37yf8x_rr_top5](bv2280_37yf8x_rr_top5.md) · [bv2280_37yf8x_star](bv2280_37yf8x_star.md)
