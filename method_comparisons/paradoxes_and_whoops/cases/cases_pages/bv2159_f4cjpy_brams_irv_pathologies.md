---
search:
  exclude: true
---

# Many IRV pathologies in one election — Brams' 21-voter sampler (BV2159)

*Generated from [`bv2159_f4cjpy_brams_irv_pathologies.yaml`](../bv2159_f4cjpy_brams_irv_pathologies.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** B

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/f4cjpy) · **[results ↗](https://bettervoting.com/f4cjpy/results)** (election `f4cjpy`).

## Scenario

Steven Brams' example (Notices of the AMS, 1982; via rangevoting.org). IRV elects B,
but G is the Condorcet winner (beats B 14-7, beats everyone). The same election shows
a no-show paradox, a truncation incentive, favorite-betrayal, and non-monotonicity —
several IRV pathologies at once. Sincere, academically sourced, ranked ballots.
Approval/STAR/Condorcet/Ranked Robin would elect G. Level 301.
Source: https://www.rangevoting.org/rangeVirv.html (section 12); Brams 1982.
Live results: https://bettervoting.com/f4cjpy/results (all races LH<->BV confirmed).
Lesson: bv2159_f4cjpy_brams_irv_pathologies.md
Live on BetterVoting: https://bettervoting.com/f4cjpy/results (BV-confirmed; STAR is race 1).

## Parameters (from the YAML)

```yaml
bv_test_id: BV2159
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
7:B>G>N>F
6:G>B>N>F
5:N>G>B>F
3:F>N>G>B
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
 Tabulating 21 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
B                  7  Hopeful
G                  6  Hopeful
N                  5  Hopeful
F                  3  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
N                  8  Hopeful
B                  7  Hopeful
G                  6  Rejected
F                  0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
B                 13  Elected
N                  8  Rejected
G                  0  Rejected
F                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  B
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): G
   Outside (3):        B, N, F
   One member ⇒ G is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner B is OUTSIDE the Smith set. ✗
      Every member of the set (G) beats B head-to-head, yet
      RCV-IRV elected B anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2159_f4cjpy_brams_irv_pathologies_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/cases/bv2159_f4cjpy_brams_irv_pathologies.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2155_cphxpt_tennessee_four_ways](bv2155_cphxpt_tennessee_four_ways.md) · [bv2156_3grpbb_star_misses_condorcet](bv2156_3grpbb_star_misses_condorcet.md) · [bv2157_mmcmpy_condorcet_cycle_rps](bv2157_mmcmpy_condorcet_cycle_rps.md) · [bv2158_gr72hd_ossipoff_centrist_irv](bv2158_gr72hd_ossipoff_centrist_irv.md) · [bv2183_dfw8rj_forced_exhaustion_ceiling](bv2183_dfw8rj_forced_exhaustion_ceiling.md)
