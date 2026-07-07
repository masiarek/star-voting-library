# Center Squeeze — IRV (Hare): the center gets squeezed out

*Generated from [`bv2137_ywckmg_irv.yaml`](../bv2137_ywckmg_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Carter

## Scenario

One of four races in the Center Squeeze election (BV2137, bvid ywckmg; BV-confirmed). 100 voters, three candidates, ONE ranked electorate tabulated four ways. Anderson is the Condorcet winner (beats Reagan 55–45, Carter 65–35) but holds the fewest first-choices (20). IRV eliminates the low-first-choice centrist Anderson FIRST, then Carter beats Reagan 55–45. IRV → Carter, NOT the Condorcet winner.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
45:Reagan>Anderson>Carter
20:Anderson>Carter>Reagan
35:Carter>Anderson>Reagan
```

## What the engine says

Full report from the [`_tabulated` mirror](../center_squeeze_bv2137_tabulated/bv2137_ywckmg_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Center Squeeze — IRV (Hare): the center gets squeezed out
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
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/center_squeeze_bv2137/bv2137_ywckmg_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2137_ywckmg_ranked_robin](bv2137_ywckmg_ranked_robin.md) · [bv2137_ywckmg_star](bv2137_ywckmg_star.md) · [bv2137_ywckmg_stv](bv2137_ywckmg_stv.md)
