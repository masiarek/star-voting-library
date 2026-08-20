---
search:
  exclude: true
---

# Kim (A,B)-scoring — the ranking alone (Ranked Robin reference)

*Generated from [`bv2275_6mcgkq_ranked_robin.yaml`](../bv2275_6mcgkq_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Almond

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6mcgkq) · **[results ↗](https://bettervoting.com/6mcgkq/results)** (election `6mcgkq` · test `BV2275`).

## Scenario

THE SAME 36 VOTERS as every other file in this folder, with nothing but their
rankings — no score dial at all.

  12 voters   Almond > Berry  > Cocoa
   8 voters   Berry  > Almond > Cocoa
   7 voters   Cocoa  > Almond > Berry
   9 voters   Cocoa  > Berry  > Almond

The other five files change what a voter's SECOND choice is worth and get five
results out of one electorate. This file is the control. Ranked Robin reads the
rankings and nothing else, so there is no dial to turn:

  Almond beats Berry  19 - 17
  Almond beats Cocoa  20 - 16
  Berry  beats Cocoa  20 - 16

Almond wins every matchup — the Condorcet winner — and that answer does not
move no matter where the (A,B) dial is set, because the dial is not an input to
it. Worth stating plainly rather than letting it read as a verdict: the reason
the pairwise answer is stable here is that it *ignores* the thing the rest of
the folder is about. Ranked Robin cannot tell the lukewarm electorate from the
intense one either — the two approval files have byte-identical rankings and
elect different candidates, and this file returns the same winner for both.
Stability and blindness are the same fact seen from two sides.

Race 6 of BV2275. LH, BetterVoting and pref_voting's independent Copeland all
agree on Almond.

Concept page: 07_Concepts/topics/ordinal_vs_cardinal_mechanism_design.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:Almond>Berry>Cocoa
8:Berry>Almond>Cocoa
7:Cocoa>Almond>Berry
9:Cocoa>Berry>Almond
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 36 ballots (ranked ballots).

Ballots:
    12 × Almond > Berry > Cocoa
     8 × Berry > Almond > Cocoa
     7 × Cocoa > Almond > Berry
     9 × Cocoa > Berry > Almond

Round-Robin — every pair, head-to-head (For – Against):
   Almond  beats Berry    19 – 17
   Almond  beats Cocoa    20 – 16
   Berry   beats Cocoa    20 – 16

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |    Almond    |   Berry     |   Cocoa     |
-------------------------------------------------------
  Almond > |     ---      |19 -  0 - 17 |20 -  0 - 16 |
   Berry > | 17 -  0 - 19 |    ---      |20 -  0 - 16 |
   Cocoa > | 16 -  0 - 20 |16 -  0 - 20 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Almond     2–0–0         2      +6  Berry, Cocoa
    2  Berry      1–1–0         1      +2  Cocoa
    3  Cocoa      0–2–0         0      -8  —

Winner — Ranked Robin (RCV-RR): Almond
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Almond
   Outside (2):        Berry, Cocoa
   One member ⇒ Almond is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Almond is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2275_6mcgkq_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/kim_ordinal_vs_cardinal/cases/bv2275_6mcgkq_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2275_6mcgkq_a0_plurality](bv2275_6mcgkq_a0_plurality.md) · [bv2275_6mcgkq_a1_negative](bv2275_6mcgkq_a1_negative.md) · [bv2275_6mcgkq_ahalf_borda](bv2275_6mcgkq_ahalf_borda.md) · [bv2275_6mcgkq_approval_intense](bv2275_6mcgkq_approval_intense.md) · [bv2275_6mcgkq_approval_lukewarm](bv2275_6mcgkq_approval_lukewarm.md)
