---
search:
  exclude: true
---

# Best Cycle-Breaking Rule — the cycle itself, and who each rule crowns

*Generated from [`cycle_vote_on_the_rule_rr_c5_b999.yaml`](../cycle_vote_on_the_rule_rr_c5_b999.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Schulze Method

**Official tie-break (lot) order:** Ranked Pairs > Schulze Method > Minimax > Copeland's Rule > Flip a Coin — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The same 999 ballots as cycle_vote_on_the_rule_irv_c5_b999.yaml, counted as
Ranked Robin so the pairwise table is on screen. Reproduced from the "Best
Cycle-Breaking Rule" sample election published by RCV Lab (rcv-lab.org),
converted from its downloadable cast vote record. Synthetic — the source
config is stamped "RCV Lab synthetic", from "The Condorcet Paradox Society" —
and built to make exactly this point.

The candidates are the cycle-breaking rules themselves, and the ballots cycle:

    Ranked Pairs   beats  Schulze Method   492-394   (margin  98)
    Schulze Method beats  Minimax          542-341   (margin 201)
    Minimax        beats  Ranked Pairs     466-413   (margin  53)

No Condorcet winner. Smith set = those same three. Copeland's Rule and Flip a
Coin lose to all three and to nobody but each other.

SO WHICH RULE WINS THE VOTE ABOUT RULES? Run the whole family and the answer
is less chaotic than the setup promises, which is the actual lesson:

    Copeland (= Ranked Robin)   Minimax, Ranked Pairs, Schulze  (3-way tie)
    Minimax                     Ranked Pairs
    Ranked Pairs                Ranked Pairs
    Schulze (beat path)         Ranked Pairs
    Split Cycle                 Ranked Pairs
    Stable Voting               Ranked Pairs
    RCV-IRV                     Ranked Pairs

Every refined rule elects RANKED PAIRS, including Schulze and Minimax — each
voting for a rival over itself. The lone rule that cannot decide is
COPELAND'S RULE, which counts wins and losses only: all three cycle members
go 3-1, so it returns a three-way tie. It is also the candidate that finished
fourth, on 61 first choices.

AND THAT IS WHERE THIS ENGINE PARTS COMPANY. LH's Ranked Robin IS Copeland,
so it hits that same three-way tie and breaks it by TOTAL MARGIN — where
Schulze Method leads on +1327 to Ranked Pairs' +1264. So the report below
elects SCHULZE METHOD while every margin-reading rule above elects Ranked
Pairs. Not a bug in either: Copeland-plus-a-tiebreak is a different rule from
Minimax or Ranked Pairs, and a cycle is precisely where different rules are
allowed to differ. It is the cleanest demonstration in this folder of why the
refined rules were invented at all.

The tiebreak here is decided by margin, not by lot — the three totals are far
apart — so the result is reproducible from the file. lot_numbers is published
anyway, per house practice.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
82:Ranked Pairs>Schulze Method
70:Schulze Method>Minimax
65:Minimax>Ranked Pairs
56:Ranked Pairs>Schulze Method>Minimax>Copeland's Rule
49:Schulze Method>Minimax>Ranked Pairs>Copeland's Rule
45:Schulze Method>Minimax>Ranked Pairs
44:Copeland's Rule>Flip a Coin
44:Minimax>Ranked Pairs>Schulze Method>Copeland's Rule
42:Ranked Pairs>Schulze Method>Minimax
41:Flip a Coin>Copeland's Rule
39:Schulze Method>Ranked Pairs
34:Ranked Pairs>Minimax
30:Minimax>Schulze Method>Ranked Pairs>Copeland's Rule
27:Minimax>Ranked Pairs>Schulze Method
23:Schulze Method>Ranked Pairs>Minimax>Copeland's Rule
21:Minimax>Schulze Method
20:Ranked Pairs>Minimax>Schulze Method
19:Schulze Method
18:Ranked Pairs>Minimax>Schulze Method>Copeland's Rule
18:Schulze Method>Ranked Pairs>Minimax
16:Minimax>Schulze Method>Ranked Pairs
16:Ranked Pairs
14:Minimax
12:Ranked Pairs>Schulze Method>Copeland's Rule>Minimax
12:Schulze Method>Minimax>Copeland's Rule>Ranked Pairs
11:Minimax>Ranked Pairs>Copeland's Rule>Schulze Method
11:Ranked Pairs>Schulze Method>Minimax>Copeland's Rule>Flip a Coin
9:Minimax>Ranked Pairs>Schulze Method>Copeland's Rule>Flip a Coin
9:Schulze Method>Minimax>Copeland's Rule
9:Schulze Method>Minimax>Ranked Pairs>Copeland's Rule>Flip a Coin
8:Ranked Pairs>Schulze Method>Copeland's Rule
7:Minimax>Ranked Pairs>Copeland's Rule
6:Schulze Method>Ranked Pairs>Minimax>Copeland's Rule>Flip a Coin
5:Minimax>Schulze Method>Ranked Pairs>Copeland's Rule>Flip a Coin
5:Ranked Pairs>Minimax>Schulze Method>Copeland's Rule>Flip a Coin
4:Copeland's Rule
4:Flip a Coin>Copeland's Rule>Ranked Pairs
4:Ranked Pairs>Copeland's Rule>Schulze Method
4:Schulze Method>Copeland's Rule>Minimax>Ranked Pairs
3:Copeland's Rule>Flip a Coin>Ranked Pairs
3:Copeland's Rule>Flip a Coin>Schulze Method
3:Flip a Coin
3:Minimax>Copeland's Rule
3:Schulze Method>Copeland's Rule
2:Copeland's Rule>Schulze Method>Minimax>Ranked Pairs
2:Flip a Coin>Copeland's Rule>Minimax
2:Flip a Coin>Copeland's Rule>Schulze Method
2:Minimax>Copeland's Rule>Ranked Pairs>Schulze Method
2:Minimax>Ranked Pairs>Copeland's Rule>Schulze Method>Flip a Coin
2:Ranked Pairs>Copeland's Rule>Schulze Method>Minimax
2:Ranked Pairs>Schulze Method>Copeland's Rule>Minimax>Flip a Coin
2:Schulze Method>Copeland's Rule>Minimax
2:Schulze Method>Minimax>Copeland's Rule>Ranked Pairs>Flip a Coin
2:Schulze Method>Ranked Pairs>Copeland's Rule
1:Copeland's Rule>Flip a Coin>Minimax
1:Copeland's Rule>Minimax
1:Copeland's Rule>Ranked Pairs>Schulze Method
1:Copeland's Rule>Ranked Pairs>Schulze Method>Minimax
1:Copeland's Rule>Schulze Method
1:Minimax>Copeland's Rule>Ranked Pairs>Schulze Method>Flip a Coin
1:Minimax>Schulze Method>Copeland's Rule
1:Ranked Pairs>Copeland's Rule
1:Ranked Pairs>Minimax>Copeland's Rule
1:Ranked Pairs>Minimax>Copeland's Rule>Schulze Method>Flip a Coin
1:Schulze Method>Ranked Pairs>Copeland's Rule>Minimax
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 999 ballots (ranked ballots).

Ballots:
    82 × Ranked Pairs > Schulze Method
    70 × Schulze Method > Minimax
    65 × Minimax > Ranked Pairs
    56 × Ranked Pairs > Schulze Method > Minimax > Copeland's Rule
    49 × Schulze Method > Minimax > Ranked Pairs > Copeland's Rule
    45 × Schulze Method > Minimax > Ranked Pairs
    44 × Copeland's Rule > Flip a Coin
    44 × Minimax > Ranked Pairs > Schulze Method > Copeland's Rule
    42 × Ranked Pairs > Schulze Method > Minimax
    41 × Flip a Coin > Copeland's Rule
    39 × Schulze Method > Ranked Pairs
    34 × Ranked Pairs > Minimax
    30 × Minimax > Schulze Method > Ranked Pairs > Copeland's Rule
    27 × Minimax > Ranked Pairs > Schulze Method
    23 × Schulze Method > Ranked Pairs > Minimax > Copeland's Rule
    21 × Minimax > Schulze Method
    20 × Ranked Pairs > Minimax > Schulze Method
    19 × Schulze Method
    18 × Ranked Pairs > Minimax > Schulze Method > Copeland's Rule
    18 × Schulze Method > Ranked Pairs > Minimax
    16 × Minimax > Schulze Method > Ranked Pairs
    16 × Ranked Pairs
    14 × Minimax
    12 × Ranked Pairs > Schulze Method > Copeland's Rule > Minimax
    12 × Schulze Method > Minimax > Copeland's Rule > Ranked Pairs
    11 × Minimax > Ranked Pairs > Copeland's Rule > Schulze Method
    11 × Ranked Pairs > Schulze Method > Minimax > Copeland's Rule > Flip a Coin
     9 × Minimax > Ranked Pairs > Schulze Method > Copeland's Rule > Flip a Coin
     9 × Schulze Method > Minimax > Copeland's Rule
     9 × Schulze Method > Minimax > Ranked Pairs > Copeland's Rule > Flip a Coin
     8 × Ranked Pairs > Schulze Method > Copeland's Rule
     7 × Minimax > Ranked Pairs > Copeland's Rule
     6 × Schulze Method > Ranked Pairs > Minimax > Copeland's Rule > Flip a Coin
     5 × Minimax > Schulze Method > Ranked Pairs > Copeland's Rule > Flip a Coin
     5 × Ranked Pairs > Minimax > Schulze Method > Copeland's Rule > Flip a Coin
     4 × Copeland's Rule
     4 × Flip a Coin > Copeland's Rule > Ranked Pairs
     4 × Ranked Pairs > Copeland's Rule > Schulze Method
     4 × Schulze Method > Copeland's Rule > Minimax > Ranked Pairs
     3 × Copeland's Rule > Flip a Coin > Ranked Pairs
     3 × Copeland's Rule > Flip a Coin > Schulze Method
     3 × Flip a Coin
     3 × Minimax > Copeland's Rule
     3 × Schulze Method > Copeland's Rule
     2 × Copeland's Rule > Schulze Method > Minimax > Ranked Pairs
     2 × Flip a Coin > Copeland's Rule > Minimax
     2 × Flip a Coin > Copeland's Rule > Schulze Method
     2 × Minimax > Copeland's Rule > Ranked Pairs > Schulze Method
     2 × Minimax > Ranked Pairs > Copeland's Rule > Schulze Method > Flip a Coin
     2 × Ranked Pairs > Copeland's Rule > Schulze Method > Minimax
     2 × Ranked Pairs > Schulze Method > Copeland's Rule > Minimax > Flip a Coin
     2 × Schulze Method > Copeland's Rule > Minimax
     2 × Schulze Method > Minimax > Copeland's Rule > Ranked Pairs > Flip a Coin
     2 × Schulze Method > Ranked Pairs > Copeland's Rule
     1 × Copeland's Rule > Flip a Coin > Minimax
     1 × Copeland's Rule > Minimax
     1 × Copeland's Rule > Ranked Pairs > Schulze Method
     1 × Copeland's Rule > Ranked Pairs > Schulze Method > Minimax
     1 × Copeland's Rule > Schulze Method
     1 × Minimax > Copeland's Rule > Ranked Pairs > Schulze Method > Flip a Coin
     1 × Minimax > Schulze Method > Copeland's Rule
     1 × Ranked Pairs > Copeland's Rule
     1 × Ranked Pairs > Minimax > Copeland's Rule
     1 × Ranked Pairs > Minimax > Copeland's Rule > Schulze Method > Flip a Coin
     1 × Schulze Method > Ranked Pairs > Copeland's Rule > Minimax

Round-Robin — every pair, head-to-head (For – Against):
   Ranked Pairs     beats Schulze Method    492 – 394
   Minimax          beats Ranked Pairs      466 – 413
   Ranked Pairs     beats Copeland's Rule   723 – 149
   Ranked Pairs     beats Flip a Coin       748 – 103
   Schulze Method   beats Minimax           542 – 341
   Schulze Method   beats Copeland's Rule   722 – 145
   Schulze Method   beats Flip a Coin       750 – 103
   Minimax          beats Copeland's Rule   689 – 151
   Minimax          beats Flip a Coin       716 – 103
   Copeland's Rule  beats Flip a Coin       419 –  52

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
                    |   Ranked Pairs    | Schulze Method   |     Minimax      | Copeland's Rule  |   Flip a Coin    |
---------------------------------------------------------------------------------------------------------------------
     Ranked Pairs > |        ---        | 492 - 113 - 394  | 413 - 120 - 466  | 723 - 127 - 149  | 748 - 148 - 103  |
   Schulze Method > |  394 - 113 - 492  |       ---        | 542 - 116 - 341  | 722 - 132 - 145  | 750 - 146 - 103  |
          Minimax > |  466 - 120 - 413  | 341 - 116 - 542  |       ---        | 689 - 159 - 151  | 716 - 180 - 103  |
  Copeland's Rule > |  149 - 127 - 723  | 145 - 132 - 722  | 151 - 159 - 689  |       ---        | 419 - 528 -  52  |
      Flip a Coin > |  103 - 148 - 748  | 103 - 146 - 750  | 103 - 180 - 716  |  52 - 528 - 419  |       ---        |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate        W–L–T  Copeland  Margin  Beats
    1  Schulze Method   3–1–0         3   +1327  Minimax, Copeland's Rule, Flip a Coin
    2  Ranked Pairs     3–1–0         3   +1264  Schulze Method, Copeland's Rule, Flip a Coin
    3  Minimax          3–1–0         3   +1003  Ranked Pairs, Copeland's Rule, Flip a Coin
    4  Copeland's Rule  1–3–0         1   -1322  Flip a Coin
    5  Flip a Coin      0–4–0         0   -2272  —

Winner — Ranked Robin (RCV-RR): Schulze Method
   *** 3 candidates tie for the most wins (Ranked Pairs, Schulze Method, Minimax) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 5): Ranked Pairs, Schulze Method, Minimax
   Outside (2):        Copeland's Rule, Flip a Coin
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Schulze Method is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/cycle_vote_on_the_rule_rr_c5_b999_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/cycle_resolution/cases/cycle_vote_on_the_rule_rr_c5_b999.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [cycle_copeland_ties_c4_b21](cycle_copeland_ties_c4_b21.md) · [cycle_family_splits_c5_b77](cycle_family_splits_c5_b77.md) · [cycle_schulze_vs_ranked_pairs_c4_b40](cycle_schulze_vs_ranked_pairs_c4_b40.md) · [cycle_vote_on_the_rule_irv_c5_b999](cycle_vote_on_the_rule_irv_c5_b999.md)
