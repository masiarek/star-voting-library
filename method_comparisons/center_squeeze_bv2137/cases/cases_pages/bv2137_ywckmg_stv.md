# Center Squeeze — STV (1 seat = IRV single-winner): same squeeze

*Generated from [`bv2137_ywckmg_stv.yaml`](../bv2137_ywckmg_stv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../../00_start_here/proportional_representation) · **1 seat** · **Expected winner:** Carter

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ywckmg) · **[results ↗](https://bettervoting.com/ywckmg/results)** (election `ywckmg`).

## Scenario

One of four races in the Center Squeeze election (BV2137, bvid ywckmg; BV-confirmed). 100 voters, three candidates, ONE ranked electorate tabulated four ways. Anderson is the Condorcet winner (beats Reagan 55–45, Carter 65–35) but holds the fewest first-choices (20). Single-seat STV is IRV: Anderson eliminated first, Carter wins. STV → Carter.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
45:Reagan>Anderson>Carter
20:Anderson>Carter>Reagan
35:Carter>Anderson>Reagan
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2137_ywckmg_stv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Center Squeeze — STV (1 seat = IRV single-winner): same squeeze
 Tabulating 100 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Reagan            45  Hopeful
Carter            35  Hopeful
Anderson          20  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Carter            55  Elected
Reagan            45  Rejected
Anderson           0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Carter
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/center_squeeze_bv2137/cases/bv2137_ywckmg_stv.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2137_ywckmg_irv](bv2137_ywckmg_irv.md) · [bv2137_ywckmg_ranked_robin](bv2137_ywckmg_ranked_robin.md) · [bv2137_ywckmg_star](bv2137_ywckmg_star.md)
