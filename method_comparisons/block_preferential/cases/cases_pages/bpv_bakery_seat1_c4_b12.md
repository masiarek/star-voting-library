---
search:
  exclude: true
---

# Block preferential voting — seat 1 of 2 (bakery co-op board)

*Generated from [`bpv_bakery_seat1_c4_b12.yaml`](../bpv_bakery_seat1_c4_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** Almond

## Scenario

BLOCK PREFERENTIAL VOTING (also called preferential block voting) is the
winner-take-all, multi-seat version of instant runoff: run a full IRV count,
seat the winner, strike that winner from every ballot, and run IRV again for
the next seat. Every voter helps decide every seat, so it is majoritarian —
NOT proportional, and not STV.
This file is SEAT 1: an ordinary RCV-IRV count on the whole 12-voter, four
candidate field. A 7-voter savoury-free majority (5 Almond-first + 2 Brioche
first) faces a 5-voter Croissant/Danish minority.
Round 1: Almond 5, Croissant 5, Brioche 2, Danish 0. Textbook Hare would drop
Danish alone (nothing to transfer), then Brioche, whose 2 ballots move to
Almond for 7 of 12 — a majority — and the first seat. The vendored pyrankvote
BATCHES the two: Brioche and Danish are both marked Rejected in round 1, since
their 2 combined votes cannot catch either leader. Same winner, one fewer
round printed.
Seat 2 continues in bpv_bakery_seat2_c3_b12.yaml, on these same ballots with
Almond struck out. The pair together IS one block-preferential count.
Lesson: 06_Other/RCV_IRV/concepts/variants/RCV-IRV-block-preferential.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
5:Almond>Brioche>Croissant>Danish
2:Brioche>Almond>Croissant>Danish
5:Croissant>Danish>Almond>Brioche
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Block preferential voting — seat 1 of 2 (bakery co-op board)
 Tabulating 12 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Almond             5  Hopeful
Croissant          5  Hopeful
Brioche            2  Rejected
Danish             0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Almond             7  Elected
Croissant          5  Rejected
Brioche            0  Rejected
Danish             0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Almond

--- Transfers and inactive ballots (what the round tables leave out) ---
The tables above give each candidate's round total but not where a
transferred vote came FROM, nor how many ballots stopped counting.
Both are recomputed from the ballots, using the eliminations the
count above actually made.

ROUND 1 — 12 of 12 ballots still active; majority = 7
   Danish eliminated with 0:
      → (held no ballots)
   Brioche eliminated with 2:
      → Almond                    2

FINAL ROUND — 12 of 12 ballots still active; majority = 7
   Almond                    7  (58.3% of the still-active)  ← elected
   Croissant                 5  (41.7% of the still-active)
   Never exhausted, never transferred:
      5 ballots held by Croissant carried a lower ranking that was never read
      (the count stopped here, so those preferences did nothing).

Inactive ballots at the final round: 0 of 12 (0.0%).
   Almond's 7 is a majority of the 12 still active AND of all 12 cast (58.3%).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): Almond
   Outside (3):        Brioche, Croissant, Danish
   One member ⇒ Almond is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Almond is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bpv_bakery_seat1_c4_b12_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/block_preferential/cases/bpv_bakery_seat1_c4_b12.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bpv_bakery_block_plurality_c4_b12](bpv_bakery_block_plurality_c4_b12.md) · [bpv_bakery_seat2_c3_b12](bpv_bakery_seat2_c3_b12.md) · [bpv_bakery_stv_c4_b12](bpv_bakery_stv_c4_b12.md)
