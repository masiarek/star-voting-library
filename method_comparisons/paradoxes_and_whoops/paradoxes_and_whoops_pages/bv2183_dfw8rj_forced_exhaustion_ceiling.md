# BV2183 — Forced Exhaustion Ceiling (RCV-IRV, 2-rank cap)

*Generated from [`bv2183_dfw8rj_forced_exhaustion_ceiling.yaml`](../bv2183_dfw8rj_forced_exhaustion_ceiling.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Ada

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dfw8rj) · **[results ↗](https://bettervoting.com/dfw8rj/results)** (election `dfw8rj`).

## Scenario

A DELIBERATELY-CONSTRUCTED worst case — not a typical election — showing the
ceiling of RCV-IRV ballot exhaustion under a ranking cap. Read it fairly: the
point is what the mechanism *permits*, not what real elections look like (real
exhaustion runs ~10-27%, milder than this; see the exhausted-ballots page).

50 voters, five candidates, but the ballot caps each voter at 2 rankings.
Three minor candidates (Cleo, Dev, Eli) form a rotating bloc; their 21 voters
spent both ranks on minor candidates (all the cap allowed), so as those are
eliminated one by one, all 21 ballots EXHAUST — none ever reaches the two real
contenders. Ada beats Ben 15-14 (margin of ONE) while 21 ballots (42%) are
discarded — MORE than the winner's own 15 votes. Ada's "majority" is 15 of 50
= 30% of the electorate. Lift the 2-rank cap (let voters rank all five) and,
in single-winner IRV, the forced exhaustion vanishes entirely — this is a
property of the ballot design, not the voters. See forced_vs_voluntary
exhaustion.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
15:Ada>Cleo
14:Ben>Dev
8:Cleo>Eli
7:Dev>Cleo
6:Eli>Dev
```

## What the engine says

Full report from the [`_tabulated` mirror](../paradoxes_and_whoops_tabulated/bv2183_dfw8rj_forced_exhaustion_ceiling_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  BV2183 — Forced Exhaustion Ceiling (RCV-IRV, 2-rank cap)
 Tabulating 50 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ada               15  Hopeful
Ben               14  Hopeful
Cleo               8  Hopeful
Dev                7  Hopeful
Eli                6  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
Ada               15  Hopeful
Ben               14  Hopeful
Dev               13  Hopeful
Cleo               8  Rejected
Eli                0  Rejected

ROUND 3
Candidate      Votes  Status
-----------  -------  --------
Ada               15  Hopeful
Ben               14  Hopeful
Dev               13  Rejected
Cleo               0  Rejected
Eli                0  Rejected
Blank Votes        8  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Ada               15  Elected
Ben               14  Rejected
Dev                0  Rejected
Cleo               0  Rejected
Eli                0  Rejected
Blank Votes       21  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ada
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/bv2183_dfw8rj_forced_exhaustion_ceiling.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Exhausted ballots (conversation)](../../../00_start_here/RCV_IRV/exhausted_ballots_301.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2155_cphxpt_tennessee_four_ways](bv2155_cphxpt_tennessee_four_ways.md) · [bv2156_3grpbb_star_misses_condorcet](bv2156_3grpbb_star_misses_condorcet.md) · [bv2157_mmcmpy_condorcet_cycle_rps](bv2157_mmcmpy_condorcet_cycle_rps.md) · [bv2158_gr72hd_ossipoff_centrist_irv](bv2158_gr72hd_ossipoff_centrist_irv.md) · [bv2159_f4cjpy_brams_irv_pathologies](bv2159_f4cjpy_brams_irv_pathologies.md)
