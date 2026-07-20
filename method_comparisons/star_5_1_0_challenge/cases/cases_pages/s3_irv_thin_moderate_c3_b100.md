# RCV-IRV on the same electorate — also squeezes the center (→ Ana)

*Generated from [`s3_irv_thin_moderate_c3_b100.yaml`](../s3_irv_thin_moderate_c3_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Ana

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/rfyk46) · **[results ↗](https://bettervoting.com/rfyk46/results)** (election `rfyk46`).

## Scenario

The thin-moderate electorate as ranked ballots under RCV-IRV. Beth has the
fewest first-choices (5) and is eliminated first; her ballots flow to Ana, who
wins 53–47. IRV fails to elect the Condorcet winner (Beth). This matches the
strategic-5-1-0 STAR result (s2): under 5-1-0 with a thin moderate base, STAR
and IRV fail the SAME way — rb-j's core point, confirmed.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
48:Ana>Beth>Cole
47:Cole>Beth>Ana
5:Beth>Ana>Cole
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/s3_irv_thin_moderate_c3_b100_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  RCV-IRV on the same electorate — also squeezes the center (→ Ana)
 Tabulating 100 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ana               48  Hopeful
Cole              47  Hopeful
Beth               5  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Ana               53  Elected
Cole              47  Rejected
Beth               0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ana
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/star_5_1_0_challenge/cases/s3_irv_thin_moderate_c3_b100.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [s1_sincere_thin_moderate_c3_b100](s1_sincere_thin_moderate_c3_b100.md) · [s2_strategic_510_thin_moderate_c3_b100](s2_strategic_510_thin_moderate_c3_b100.md) · [s4_strategic_510_real_moderate_c3_b100](s4_strategic_510_real_moderate_c3_b100.md) · [s5_irv_real_moderate_c3_b100](s5_irv_real_moderate_c3_b100.md)
