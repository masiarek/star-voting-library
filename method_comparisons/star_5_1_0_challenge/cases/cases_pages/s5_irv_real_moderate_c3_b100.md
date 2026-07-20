# RCV-IRV, real moderate base — still squeezes the center (→ Ana)

*Generated from [`s5_irv_real_moderate_c3_b100.yaml`](../s5_irv_real_moderate_c3_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Ana

## Scenario

The real-moderate electorate (40/35/25) as ranked ballots under RCV-IRV. Beth
still has the fewest first-choices (25) and is eliminated first, her ballots
flow to Ana, who wins 65–35. IRV fails the Condorcet winner regardless of
moderate base — because it only ever counts first choices. Contrast s4: the
SAME electorate under strategic-5-1-0 STAR elects Beth, the Condorcet winner.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
40:Ana>Beth>Cole
35:Cole>Beth>Ana
25:Beth>Ana>Cole
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/s5_irv_real_moderate_c3_b100_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  RCV-IRV, real moderate base — still squeezes the center (→ Ana)
 Tabulating 100 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ana               40  Hopeful
Cole              35  Hopeful
Beth              25  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Ana               65  Elected
Cole              35  Rejected
Beth               0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ana
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/star_5_1_0_challenge/cases/s5_irv_real_moderate_c3_b100.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [s1_sincere_thin_moderate_c3_b100](s1_sincere_thin_moderate_c3_b100.md) · [s2_strategic_510_thin_moderate_c3_b100](s2_strategic_510_thin_moderate_c3_b100.md) · [s3_irv_thin_moderate_c3_b100](s3_irv_thin_moderate_c3_b100.md) · [s4_strategic_510_real_moderate_c3_b100](s4_strategic_510_real_moderate_c3_b100.md)
