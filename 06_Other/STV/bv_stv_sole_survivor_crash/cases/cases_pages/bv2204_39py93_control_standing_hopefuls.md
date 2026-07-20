# BV2204 — Poets on the shelf: the control (STV 2 seats, hopefuls still standing)

*Generated from [`bv2204_39py93_control_standing_hopefuls.yaml`](../bv2204_39py93_control_standing_hopefuls.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Angelou, Cummings

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/39py93) · **[results ↗](https://bettervoting.com/39py93/results)** (election `39py93`).

## Scenario

Bisection probe #2 (the CONTROL) for the BetterVoting STV sole-survivor
crash: config identical to the crashing exercise-14 election tk776t —
STV, 2 seats, 4 candidates, write-ins off — but ballots whose count
ends with two hopefuls STILL STANDING, so no candidate is ever
eliminated. 13 voters, Droop quota = floor(13/3)+1 = 5. Round 1:
Angelou holds 6 ≥ 5, elected; her surplus of 1 transfers (six ballots
at 1/6 each) to Blake: 1+1 = 2. Round 2: Cummings holds 5 ≥ 5, elected
with zero surplus — both seats filled, Blake and Dickinson never
eliminated. PREDICTION: computes. RESULT: computes — BetterVoting
returns Angelou + Cummings, agreeing with the LH engine. Together with
probe #1 (gvtg2h: same crashing count, flag removed, still errors)
this convicts the ENDGAME — electing the last remaining hopeful at
quota — and acquits the shape and every config key. Full lab notebook:
README.md in this folder.
Live on BetterVoting (Test ID BV2204): https://bettervoting.com/39py93

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:Angelou>Blake
5:Cummings>Blake
1:Blake
1:Dickinson
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2204_39py93_control_standing_hopefuls_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- STV / Single Transferable Vote (multi-winner — 2 seats) ---
  BV2204 — Poets on the shelf: the control (STV 2 seats, hopefuls still standing)
 Tabulating 13 ballots (ranked ballots).
 2 seats; Droop quota = 5 (38.5% of 13).

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Angelou            6  Elected
Cummings           5  Elected
Blake              1  Rejected
Dickinson          1  Rejected


Winner(s) — STV / Single Transferable Vote (multi-winner — 2 seats)
  Angelou
  Cummings
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/STV/bv_stv_sole_survivor_crash/cases/bv2204_39py93_control_standing_hopefuls.yaml
```

## See also

- [Glossary](../../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2203_gvtg2h_flag_probe](bv2203_gvtg2h_flag_probe.md) · [bv2205_8xwx43_minimal_sole_survivor](bv2205_8xwx43_minimal_sole_survivor.md)
