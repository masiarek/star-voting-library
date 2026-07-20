# BV2203 — The transfer machine, flag probe (STV 2 seats, write-in key omitted)

*Generated from [`bv2203_gvtg2h_flag_probe.yaml`](../bv2203_gvtg2h_flag_probe.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Austen, Camus

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/gvtg2h) · **[results ↗](https://bettervoting.com/gvtg2h/results)** (election `gvtg2h`).

## Scenario

Bisection probe #1 for the BetterVoting STV sole-survivor crash: the
exercise-14 ballots byte-for-byte (5:Austen>Bronte>Camus>Dickens,
1:Bronte>Camus, 3:Camus>Dickens; 2 seats; Droop quota 4), created with
the enable_write_in key OMITTED from the race object — the one config
key that separated the crashing elections (tk776t, bj8dfc) from the
working older STV races (ywckmg, kcf8vf). Key confirmed absent on the
created race. RESULT: still crashes (error cc9625bb) — the flag is
acquitted, which pointed the investigation at the count itself: the
eliminations consume Dickens and Bronte, and Camus reaches quota as the
SOLE remaining hopeful — the endgame BetterVoting's IRV.ts cannot
redistribute a surplus from ([].reduce with no initial value throws).
Full lab notebook: README.md in this folder. Seats below are the LH
engine's (BV errors until fixed).
Live on BetterVoting (Test ID BV2203): https://bettervoting.com/gvtg2h
— results page errors by design of the probe.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
5:Austen>Bronte>Camus>Dickens
1:Bronte>Camus
3:Camus>Dickens
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2203_gvtg2h_flag_probe_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- STV / Single Transferable Vote (multi-winner — 2 seats) ---
  BV2203 — The transfer machine, flag probe (STV 2 seats, write-in key omitted)
 Tabulating 9 ballots (ranked ballots).
 2 seats; Droop quota = 4 (44.4% of 9).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Austen             5  Elected
Camus              3  Hopeful
Bronte             1  Hopeful
Dickens            0  Hopeful

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Austen          3.00  Elected
Camus           3.00  Elected
Bronte          3.00  Rejected
Dickens         0.00  Rejected


Winner(s) — STV / Single Transferable Vote (multi-winner — 2 seats)
  Austen
  Camus
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/STV/bv_stv_sole_survivor_crash/cases/bv2203_gvtg2h_flag_probe.yaml
```

## See also

- [Glossary](../../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2204_39py93_control_standing_hopefuls](bv2204_39py93_control_standing_hopefuls.md) · [bv2205_8xwx43_minimal_sole_survivor](bv2205_8xwx43_minimal_sole_survivor.md)
