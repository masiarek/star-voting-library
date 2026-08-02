---
search:
  exclude: true
---

# IRV buries the centrist — Ossipoff's 303-voter one-dimensional example (BV2158)

*Generated from [`bv2158_gr72hd_ossipoff_centrist_irv.yaml`](../bv2158_gr72hd_ossipoff_centrist_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** D

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/gr72hd) · **[results ↗](https://bettervoting.com/gr72hd/results)** (election `gr72hd`).

## Scenario

Mike Ossipoff's 1-D example (via rangevoting.org). Candidate C is the centrist:
C is the PLURALITY winner (100 first-choices, most of any) AND the Condorcet winner
(beats every rival ~2:1). Yet RCV-IRV ELIMINATES C in round 3 and elects D. Sincere
ballots; a realistic 'one-dimensional politics' taper. Ranked-ballot case (no scores
invented). Approval/STAR/Condorcet/Ranked Robin would all elect C. Level 301.
Source: https://www.rangevoting.org/rangeVirv.html (section 12).
Live results: https://bettervoting.com/gr72hd/results (all races LH<->BV confirmed).
Lesson: bv2158_gr72hd_ossipoff_centrist_irv.md
Live on BetterVoting: https://bettervoting.com/gr72hd/results (BV-confirmed; STAR is race 1).

## Parameters (from the YAML)

```yaml
expected_winners: [D]
bv_election_id: gr72hd
bv_test_id: BV2158
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
50:A>B>C>D>E
51:B>A>C>D>E
100:C>D>B>E>A
53:D>E>C>B>A
49:E>D>C>B>A
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
 Tabulating 303 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
C                100  Hopeful
D                 53  Hopeful
B                 51  Hopeful
A                 50  Hopeful
E                 49  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
D                102  Hopeful
C                100  Hopeful
B                 51  Hopeful
A                 50  Rejected
E                  0  Rejected

ROUND 3
Candidate      Votes  Status
-----------  -------  --------
D                102  Hopeful
B                101  Hopeful
C                100  Rejected
A                  0  Rejected
E                  0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
D                202  Elected
B                101  Rejected
C                  0  Rejected
A                  0  Rejected
E                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  D
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 5): C
   Outside (4):        A, B, D, E
   One member ⇒ C is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner D is OUTSIDE the Smith set. ✗
      Every member of the set (C) beats D head-to-head, yet
      RCV-IRV elected D anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2158_gr72hd_ossipoff_centrist_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/cases/bv2158_gr72hd_ossipoff_centrist_irv.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2155_cphxpt_tennessee_four_ways](bv2155_cphxpt_tennessee_four_ways.md) · [bv2156_3grpbb_star_misses_condorcet](bv2156_3grpbb_star_misses_condorcet.md) · [bv2157_mmcmpy_condorcet_cycle_rps](bv2157_mmcmpy_condorcet_cycle_rps.md) · [bv2159_f4cjpy_brams_irv_pathologies](bv2159_f4cjpy_brams_irv_pathologies.md) · [bv2183_dfw8rj_forced_exhaustion_ceiling](bv2183_dfw8rj_forced_exhaustion_ceiling.md)
