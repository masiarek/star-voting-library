# Reversal symmetry — RCV-IRV, reversed: A wins AGAIN (worst = best)

*Generated from [`reversal_irv_reversed.yaml`](../reversal_irv_reversed.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** A

## Scenario

The original election (reversal_irv_original) with EVERY voter's ballot reversed — each now
expresses the exact opposite preference, as if trying to elect the WORST candidate. You would
expect A (the original winner) to now finish last. Instead RCV-IRV elects A AGAIN (16-8): B has
the fewest first-choices, is eliminated, and B's ballots flow to A. So IRV's "best" candidate and
its "worst" candidate are the same — a reversal symmetry FAILURE. This is a real, IRV-specific
defect (concede it). Caveats on ../README.md: the electorate is a Condorcet cycle, so there is no
"correct" winner; STAR gives B then A (no winner=loser); source is Range-advocacy (lean disclosed).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
9:A>C>B
8:C>B>A
7:B>A>C
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/reversal_irv_reversed_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reversal_symmetry/cases/reversal_irv_reversed.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [reversal_irv_original](reversal_irv_original.md) · [reversal_star_original](reversal_star_original.md) · [reversal_star_reversed](reversal_star_reversed.md)
