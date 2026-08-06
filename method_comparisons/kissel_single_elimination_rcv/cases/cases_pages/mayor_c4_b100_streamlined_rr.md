---
search:
  exclude: true
---

# The mayor's race (Ranked Robin) — Cora beats everyone head-to-head

*Generated from [`mayor_c4_b100_streamlined_rr.yaml`](../mayor_c4_b100_streamlined_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Cora

## Scenario

The identical 100 ballots as …_irv.yaml, counted by Ranked Robin (RCV-RR / Copeland). Cora wins the round-robin 3-0: 67-33 over Ada, 69-31 over Blake, 84-16 over Dean. She is the Condorcet winner, and she is the SECOND choice of every other bloc on the ballot — which is exactly the information the paper's single-elimination model throws away when it keeps only the top two first-choice finishers. Ranked Robin needs no rounds, no elimination order and no transfers to see it; it reads every ballot in every pairing, once.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
33:Ada>Cora>Blake>Dean     # Ada's voters — Cora is their second choice
31:Blake>Cora>Ada>Dean     # Blake's voters — Cora is their second choice too
20:Cora>Blake>Ada>Dean     # the moderates, leaning Blake
16:Dean>Cora>Blake>Ada     # Dean's voters — Cora again
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 100 ballots (ranked ballots).

Ballots:
    33 × Ada > Cora > Blake > Dean
    31 × Blake > Cora > Ada > Dean
    20 × Cora > Blake > Ada > Dean
    16 × Dean > Cora > Blake > Ada

Round-Robin — every pair, head-to-head (For – Against):
   Cora   beats Ada     67 – 33
   Blake  beats Ada     67 – 33
   Ada    beats Dean    84 – 16
   Cora   beats Blake   69 – 31
   Cora   beats Dean    84 – 16
   Blake  beats Dean    84 – 16

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |     Ada      |    Cora     |   Blake     |    Dean     |
--------------------------------------------------------------------
    Ada > |     ---      |33 -  0 - 67 |33 -  0 - 67 |84 -  0 - 16 |
   Cora > | 67 -  0 - 33 |    ---      |69 -  0 - 31 |84 -  0 - 16 |
  Blake > | 67 -  0 - 33 |31 -  0 - 69 |    ---      |84 -  0 - 16 |
   Dean > | 16 -  0 - 84 |16 -  0 - 84 |16 -  0 - 84 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Cora       3–0–0         3    +140  Blake, Ada, Dean
    2  Blake      2–1–0         2     +64  Ada, Dean
    3  Ada        1–2–0         1      +0  Dean
    4  Dean       0–3–0         0    -204  —

Winner — Ranked Robin (RCV-RR): Cora
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): Cora
   Outside (3):        Ada, Blake, Dean
   One member ⇒ Cora is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Cora is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/mayor_c4_b100_streamlined_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/kissel_single_elimination_rcv/cases/mayor_c4_b100_streamlined_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [kissel_five_way_c5_b1000_irv](kissel_five_way_c5_b1000_irv.md) · [kissel_five_way_c5_b1000_rr](kissel_five_way_c5_b1000_rr.md) · [kissel_five_way_c5_b1000_star](kissel_five_way_c5_b1000_star.md) · [mayor_c4_b100_streamlined_irv](mayor_c4_b100_streamlined_irv.md) · [mayor_c4_b100_streamlined_star](mayor_c4_b100_streamlined_star.md)
