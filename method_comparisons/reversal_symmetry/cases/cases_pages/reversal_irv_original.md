# Reversal symmetry — RCV-IRV, original: A wins (best)

*Generated from [`reversal_irv_original.yaml`](../reversal_irv_original.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** A

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

Full report from the [`_tabulated` mirror](../cases_tabulated/reversal_irv_original_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reversal_symmetry/cases/reversal_irv_original.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [reversal_irv_reversed](reversal_irv_reversed.md) · [reversal_star_original](reversal_star_original.md) · [reversal_star_reversed](reversal_star_reversed.md)
