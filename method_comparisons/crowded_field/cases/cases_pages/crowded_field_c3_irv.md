---
search:
  exclude: true
---

# Crowded field, rung 3 — 3 candidates, 65 voters, counted by RCV-IRV

*Generated from [`crowded_field_c3_irv.yaml`](../crowded_field_c3_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** Diego

**Official tie-break (lot) order:** Ana > Diego > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 1, counted by RCV-IRV on the voters' real rankings. Diego takes 34 first
choices of 65 — an outright majority in round 1 — and the count ends there. Nothing
for instant runoff to get wrong yet.

Round 1 of this report is also the Choose-One (Plurality) result: Diego, 34 of 65.

Same 65 voters and the same fixed candidate positions as crowded_field_c3_star.yaml,
on a ranked ballot — the same ballots as crowded_field_c3_ranked_robin.yaml, counted by
elimination instead of head-to-head.

Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
settled by a tie-break.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:Ana>Diego>Greta    # bloc at 0
10:Ana>Diego>Greta    # bloc at 4
13:Diego>Ana>Greta    # bloc at 8
9:Diego>Greta>Ana    # bloc at 12
12:Diego>Greta>Ana    # bloc at 16
8:Greta>Diego>Ana    # bloc at 20
7:Greta>Diego>Ana    # bloc at 24
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Crowded field, rung 3 — 3 candidates, 65 voters, counted by RCV-IRV
 Tabulating 65 ballots (ranked ballots).

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Diego             34  Elected
Ana               16  Rejected
Greta             15  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Diego
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Diego
   Outside (2):        Ana, Greta
   One member ⇒ Diego is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Diego is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/crowded_field_c3_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c3_irv.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_approval](crowded_field_c3_approval.md) · [crowded_field_c3_ranked_robin](crowded_field_c3_ranked_robin.md) · [crowded_field_c3_star](crowded_field_c3_star.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_ranked_robin](crowded_field_c5_ranked_robin.md) · [crowded_field_c5_star](crowded_field_c5_star.md) · [crowded_field_c7_approval](crowded_field_c7_approval.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_ranked_robin](crowded_field_c7_ranked_robin.md) · [crowded_field_c7_star](crowded_field_c7_star.md)
