# Reversal symmetry — RCV-IRV, reversed: A wins AGAIN (worst = best)

*Generated from [`reversal_irv_reversed.yaml`](../reversal_irv_reversed.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** A

## Scenario

The original election (reversal_irv_original) with EVERY voter's ballot reversed — each now
expresses the exact opposite preference, as if trying to elect the WORST candidate. You would
expect A (the original winner) to now finish last. Instead RCV-IRV elects A AGAIN (16-8): B has
the fewest first-choices, is eliminated, and B's ballots flow to A. So IRV's "best" candidate and
its "worst" candidate are the same — a reversal symmetry FAILURE. This is a real, IRV-specific
defect (concede it). Caveats on ../README.md: the electorate is a Condorcet cycle, so there is no
"correct" winner; STAR gives B then A (no winner=loser); source is Range-advocacy (lean disclosed).

## Parameters (from the YAML)

```yaml
voting_method: RCV_IRV
num_winners: 1
expected_winners:
- A
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
9:A>C>B
8:C>B>A
7:B>A>C
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Reversal symmetry — RCV-IRV, reversed: A wins AGAIN (worst = best)
 Tabulating 24 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                  9  Hopeful
C                  8  Hopeful
B                  7  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
A                 16  Elected
C                  8  Rejected
B                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): A, C, B
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   RCV-IRV winner A is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reversal_irv_reversed_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reversal_symmetry/cases/reversal_irv_reversed.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [reversal_irv_original](reversal_irv_original.md) · [reversal_star_original](reversal_star_original.md) · [reversal_star_reversed](reversal_star_reversed.md)
