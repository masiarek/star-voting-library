# Non-monotonicity (RCV-IRV) — part 1: baseline, X wins

*Generated from [`monotonicity_irv_before.yaml`](../monotonicity_irv_before.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** X

## Scenario

Part 1 of the RCV-IRV monotonicity pair: 34 voters, X wins (Z is eliminated,
Z's ballots transfer to X). This is the baseline for the paradox — in part 2
(monotonicity_irv_after.yaml) four voters RAISE X from second to first
choice, change nothing else, and X LOSES. Keep both files side by side; the
ballots differ only in those four voters.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:X>Y
12:Y>Z
10:Z>X
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Non-monotonicity (RCV-IRV) — part 1: baseline, X wins
 Tabulating 34 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Y                 12  Hopeful
X                 12  Hopeful
Z                 10  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
X                 22  Elected
Y                 12  Rejected
Z                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  X
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): X, Y, Z
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   RCV-IRV winner X is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/monotonicity_irv_before_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/cases/monotonicity_irv_before.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [alaska_upward_after](alaska_upward_after.md) · [alaska_upward_before](alaska_upward_before.md) · [mono_raise_delete_after](mono_raise_delete_after.md) · [mono_raise_delete_before](mono_raise_delete_before.md) · [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md) · [sf_d7_downward_after](sf_d7_downward_after.md) · [sf_d7_downward_before](sf_d7_downward_before.md)
