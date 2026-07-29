# Reversal symmetry — RCV-IRV, original: A wins (best)

*Generated from [`reversal_irv_original.yaml`](../reversal_irv_original.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** A

## Scenario

A reversal-symmetry demonstration (from rangevoting.org / Warren Smith — a Range-advocacy
source, so advocacy-leaning; disclosed). 24 voters, three candidates, a Condorcet CYCLE
(A>B>C>A — no candidate beats all others). Counted by RCV-IRV, A wins: C has the fewest
first-choices, is eliminated, and C's ballots flow to A (15-9). The companion
reversal_irv_reversed reverses EVERY ballot — as if voters were choosing the WORST
candidate — and A wins AGAIN. That winner=loser outcome is a failure of the reversal
symmetry criterion, which RCV-IRV and plurality fail but additive methods (Range, Borda,
Approval) and some Condorcet methods (Ranked Pairs, Schulze) satisfy. See ../README.md;
STAR and Ranked Robin do NOT reproduce the winner=loser on this example.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
9:B>C>A
8:A>B>C
7:C>A>B
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Reversal symmetry — RCV-IRV, original: A wins (best)
 Tabulating 24 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
B                  9  Hopeful
A                  8  Hopeful
C                  7  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
A                 15  Elected
B                  9  Rejected
C                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): B, C, A
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   RCV-IRV winner A is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reversal_irv_original_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reversal_symmetry/cases/reversal_irv_original.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [reversal_irv_reversed](reversal_irv_reversed.md) · [reversal_star_original](reversal_star_original.md) · [reversal_star_reversed](reversal_star_reversed.md)
