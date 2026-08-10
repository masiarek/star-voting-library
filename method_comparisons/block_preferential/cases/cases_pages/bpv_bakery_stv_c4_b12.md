---
search:
  exclude: true
---

# The same ballots under STV — 2 seats, and the minority gets one

*Generated from [`bpv_bakery_stv_c4_b12.yaml`](../bpv_bakery_stv_c4_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Almond, Croissant

## Scenario

The control for the block-preferential pair: identical ballots, identical two
seats, counted PROPORTIONALLY instead.
STV's Droop quota here is 12 / (2 + 1) = 4 (the engine's exact form; the
hand-count rule floor(12/3) + 1 = 5 is the other standard reading, and both
land in the same place on these ballots). Almond has 5 and Croissant has 5 —
both clear quota in the first round, both are seated, and the board splits 1-1
between the 7-voter majority and the 5-voter minority.
Block preferential voting on these same ballots elects Almond AND Brioche — a
clean sweep for the majority (bpv_bakery_seat1_c4_b12.yaml +
bpv_bakery_seat2_c3_b12.yaml). Same ranked ballot, same voters, opposite
philosophy: the ballot decides what voters can say, the COUNT decides how the
seats are shared.
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
--- STV / Single Transferable Vote (multi-winner — 2 seats) ---
  The same ballots under STV — 2 seats, and the minority gets one
 Tabulating 12 ballots (ranked ballots).
 2 seats; quota = 4.00 (exact Droop, votes/(seats+1)) — 33.3% of 12.
 Elected at >= quota, and every surplus is measured from it.
 (Hand-count Droop, floor(12/3)+1 = 5, is a different but equally standard rule.)

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Almond             5  Elected
Croissant          5  Elected
Brioche            2  Rejected
Danish             0  Rejected


Winner(s) — STV / Single Transferable Vote (multi-winner — 2 seats)
  Almond
  Croissant
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
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bpv_bakery_stv_c4_b12_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/block_preferential/cases/bpv_bakery_stv_c4_b12.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bpv_bakery_block_plurality_c4_b12](bpv_bakery_block_plurality_c4_b12.md) · [bpv_bakery_seat1_c4_b12](bpv_bakery_seat1_c4_b12.md) · [bpv_bakery_seat2_c3_b12](bpv_bakery_seat2_c3_b12.md)
