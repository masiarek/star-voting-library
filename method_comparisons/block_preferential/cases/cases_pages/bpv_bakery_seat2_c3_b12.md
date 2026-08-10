---
search:
  exclude: true
---

# Block preferential voting — seat 2 of 2 (bakery co-op board)

*Generated from [`bpv_bakery_seat2_c3_b12.yaml`](../bpv_bakery_seat2_c3_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** Brioche

## Scenario

SEAT 2 of the block-preferential count begun in bpv_bakery_seat1_c4_b12.yaml.
Almond won seat 1, so Almond is struck from every ballot and the SAME twelve
voters — all of them, including the five who already got nothing — count
again for the second seat.
That is the whole difference between block preferential voting and STV. STV
would have spent the majority's ballots on the seat they already won; block
preferential voting hands them back at full strength. Brioche now holds 7 of
12 first preferences outright and takes seat 2 in a single round.
Final board: Almond and Brioche — both from the 7-voter (58%) majority. The
5-voter (42%) minority elects nobody. Run the same ballots under STV
(bpv_bakery_stv_c4_b12.yaml) and the seats split 1-1.
Lesson: 06_Other/RCV_IRV/concepts/variants/RCV-IRV-block-preferential.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
5:Brioche>Croissant>Danish
2:Brioche>Croissant>Danish
5:Croissant>Danish>Brioche
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Block preferential voting — seat 2 of 2 (bakery co-op board)
 Tabulating 12 ballots (ranked ballots).

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Brioche            7  Elected
Croissant          5  Rejected
Danish             0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Brioche
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Brioche
   Outside (2):        Croissant, Danish
   One member ⇒ Brioche is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Brioche is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bpv_bakery_seat2_c3_b12_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/block_preferential/cases/bpv_bakery_seat2_c3_b12.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bpv_bakery_block_plurality_c4_b12](bpv_bakery_block_plurality_c4_b12.md) · [bpv_bakery_seat1_c4_b12](bpv_bakery_seat1_c4_b12.md) · [bpv_bakery_stv_c4_b12](bpv_bakery_stv_c4_b12.md)
