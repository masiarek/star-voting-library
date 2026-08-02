---
search:
  exclude: true
---

# Downward monotonicity (San Francisco D7 2020) — AFTER: rank the loser lower, he wins

*Generated from [`sf_d7_downward_after.yaml`](../sf_d7_downward_after.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** Engardio

## Scenario

The BEFORE file (sf_d7_downward_before) exactly, with ONE change: 800 ballots of
the form Engardio>Nguyen>Melgar are shifted DOWN to Nguyen>Engardio>Melgar. Nothing
else moves. This gives the previous LOSER Engardio LESS first-place support (14119
-> 13319) — yet he now WINS. Why: the shifted votes lift Nguyen's first-round count
(10855 -> 11655) just past Melgar's 11652, so MELGAR is eliminated first instead of
Nguyen; Melgar's ballots transfer, and Engardio beats Nguyen in the final,
15819-15155. Ranking the loser lower made the loser win — the downward monotonicity
paradox (Graham-Squire & McCune, arXiv:2301.12075). As in the Alaska upward case,
the paradox works by changing the ORDER of elimination. The Melgar/Nguyen Round-1
gap is just 3 votes — this is a genuine knife-edge, which is why the real, full-scale
counts (not a reduced model) are used. Companion page: downward_monotonicity_sf.md.

## Parameters (from the YAML)

```yaml
voting_method: RCV_IRV
num_winners: 1
expected_winners: [Engardio]
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
13319:Engardio>Melgar>Nguyen
2500:Melgar>Engardio>Nguyen
3500:Melgar>Nguyen>Engardio
5652:Melgar
6909:Nguyen>Melgar>Engardio
3051:Nguyen>Engardio>Melgar
1695:Nguyen
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Downward monotonicity (San Francisco D7 2020) — AFTER: rank the loser lower, he wins
 Tabulating 36626 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Engardio       13319  Hopeful
Nguyen         11655  Hopeful
Melgar         11652  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Engardio       15819  Elected
Nguyen         15155  Rejected
Melgar             0  Rejected
Blank Votes     5652  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Engardio
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Melgar
   Outside (2):        Engardio, Nguyen
   One member ⇒ Melgar is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Engardio is OUTSIDE the Smith set. ✗
      Every member of the set (Melgar) beats Engardio head-to-head, yet
      RCV-IRV elected Engardio anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/sf_d7_downward_after_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/cases/sf_d7_downward_after.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [alaska_upward_after](alaska_upward_after.md) · [alaska_upward_before](alaska_upward_before.md) · [mono_raise_delete_after](mono_raise_delete_after.md) · [mono_raise_delete_before](mono_raise_delete_before.md) · [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md) · [sf_d7_downward_before](sf_d7_downward_before.md)
