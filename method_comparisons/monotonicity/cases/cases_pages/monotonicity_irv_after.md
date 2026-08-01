---
search:
  exclude: true
---

# Non-monotonicity (RCV-IRV) — part 2: raising X makes X lose

*Generated from [`monotonicity_irv_after.yaml`](../monotonicity_irv_after.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** Z

## Scenario

Part 2 of the RCV-IRV monotonicity pair: four Y>Z voters move X up to first
(12:X>Y becomes 16:X>Y), a pure GAIN of support for X — and X now loses.
The extra support changed the elimination order: Y goes out first, Y's
ballots feed Z, and Z beats X 18-16. More support made the winner lose —
IRV's non-monotonicity. STAR cannot do this (more points never hurt); see
the monotonicity_star_* pair and the monotonicity topic hub.

## Parameters (from the YAML)

```yaml
voting_method: RCV_IRV
num_winners: 1
expected_winners:
- Z
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
16:X>Y
8:Y>Z
10:Z>X
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Non-monotonicity (RCV-IRV) — part 2: raising X makes X lose
 Tabulating 34 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
X                 16  Hopeful
Z                 10  Hopeful
Y                  8  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Z                 18  Elected
X                 16  Rejected
Y                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Z
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
   RCV-IRV winner Z is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/monotonicity_irv_after_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/cases/monotonicity_irv_after.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [alaska_upward_after](alaska_upward_after.md) · [alaska_upward_before](alaska_upward_before.md) · [mono_raise_delete_after](mono_raise_delete_after.md) · [mono_raise_delete_before](mono_raise_delete_before.md) · [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md) · [sf_d7_downward_after](sf_d7_downward_after.md) · [sf_d7_downward_before](sf_d7_downward_before.md)
