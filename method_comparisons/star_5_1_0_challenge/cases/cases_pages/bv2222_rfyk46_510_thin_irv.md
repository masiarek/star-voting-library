# RCV-IRV on the same electorate — also squeezes the center (→ Ana)

*Generated from [`bv2222_rfyk46_510_thin_irv.yaml`](../bv2222_rfyk46_510_thin_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

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

The count, step by step — the rounds and how the winner is reached:

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

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Beth
   Outside (2):        Ana, Cole
   One member ⇒ Beth is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Ana is OUTSIDE the Smith set. ✗
      Every member of the set (Beth) beats Ana head-to-head, yet
      RCV-IRV elected Ana anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 00_start_here/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2222_rfyk46_510_thin_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/star_5_1_0_challenge/cases/bv2222_rfyk46_510_thin_irv.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2221_2kcwbw_sincere](bv2221_2kcwbw_sincere.md) · [bv2222_rfyk46_510_thin_star](bv2222_rfyk46_510_thin_star.md) · [bv2223_dyh93j_510_real_irv](bv2223_dyh93j_510_real_irv.md) · [bv2223_dyh93j_510_real_star](bv2223_dyh93j_510_real_star.md)
