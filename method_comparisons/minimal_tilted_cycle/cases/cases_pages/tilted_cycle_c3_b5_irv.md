# Minimal tilted cycle — 5 voters, margins 3–1–1 (RCV-IRV)

*Generated from [`tilted_cycle_c3_b5_irv.yaml`](../tilted_cycle_c3_b5_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [rcv-irv](../../../../00_start_here) · **1 seat** · **Expected winner:** Cara

## Scenario

The same five ballots as tilted_cycle_c3_b5_rr.yaml — the minimal tilted
Condorcet cycle from Brandt, Dong & Peters (arXiv:2411.19857), Fig. 1 —
counted by instant runoff instead.

Ben holds just one first choice, so IRV eliminates him first; his ballot
(Ben > Cara > Ada) transfers to Cara, who wins 3–2 over Ada.

Worth noting what IRV does NOT see: Ada's 4–1 crushing of Ben is the largest
majority anywhere on these ballots, and it never enters the count. IRV reads
first preferences; the cycle lives in the pairwise margins.

In a cycle there is no Condorcet winner, so IRV cannot be accused of missing
one — this is a legitimate answer, not a failure. It simply lands on a
different candidate than Copeland's margins tiebreak (Ada) and than leximin
(Ada), and agrees with Nanson (Cara). Five voters, four defensible answers:
that is what a cycle costs. See the folder README.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Ada>Ben>Cara
1:Ben>Cara>Ada
2:Cara>Ada>Ben
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/tilted_cycle_c3_b5_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Minimal tilted cycle — 5 voters, margins 3–1–1 (RCV-IRV)
 Tabulating 5 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ada                2  Hopeful
Cara               2  Hopeful
Ben                1  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Cara               3  Elected
Ada                2  Rejected
Ben                0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Cara
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minimal_tilted_cycle/cases/tilted_cycle_c3_b5_irv.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [tilted_cycle_c3_b5_rr](tilted_cycle_c3_b5_rr.md)
