---
search:
  exclude: true
---

# BV2183 — Forced Exhaustion Ceiling (RCV-IRV, 2-rank cap)

*Generated from [`bv2183_dfw8rj_forced_exhaustion_ceiling.yaml`](../bv2183_dfw8rj_forced_exhaustion_ceiling.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** Ada

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dfw8rj) · **[results ↗](https://bettervoting.com/dfw8rj/results)** (election `dfw8rj` · test `BV2183`).

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

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
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
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (5 of 5): Dev, Ada, Cleo, Ben, Eli
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (Dev) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   RCV-IRV winner Ada is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   Fine print: this set contains a pairwise DRAW, and a draw is enough to keep a
   candidate in the Smith set but not in the tighter Schwartz set — so Schwartz
   may be smaller here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2183_dfw8rj_forced_exhaustion_ceiling_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/cases/bv2183_dfw8rj_forced_exhaustion_ceiling.yaml
```

## See also

- [Exhausted ballots (conversation)](../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2155_cphxpt_tennessee_four_ways](bv2155_cphxpt_tennessee_four_ways.md) · [bv2156_3grpbb_star_misses_condorcet](bv2156_3grpbb_star_misses_condorcet.md) · [bv2157_mmcmpy_condorcet_cycle_rps](bv2157_mmcmpy_condorcet_cycle_rps.md) · [bv2158_gr72hd_ossipoff_centrist_irv](bv2158_gr72hd_ossipoff_centrist_irv.md) · [bv2159_f4cjpy_brams_irv_pathologies](bv2159_f4cjpy_brams_irv_pathologies.md)
