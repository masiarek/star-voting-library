# RCTab cross-check — running our cases through the certified tabulator

[RCTab](https://www.rcvresources.org/rctab) is the federally-tested (VVSG), state-certified, open-source tabulator that US jurisdictions actually run on election night. This folder converts this repo's ranked-ballot cases into RCTab input and runs them, so a case can be checked against production election software rather than only against other teaching engines.

The concept page — what RCTab is, what its agreement is and isn't worth — is [RCTab](../../../07_Concepts/tabulation_engines/rctab.md). The findings from the first run are on [Batch elimination](../../../07_Concepts/topics/ties/batch_elimination.md#what-a-certified-tabulator-does-instead).

## The two scripts

| | |
|---|---|
| [`rctab_convert.py`](rctab_convert.py) | a ranked YAML → `<stem>.csv` + `<stem>_config.json`. **No Java needed.** |
| [`rctab_crosscheck.py`](rctab_crosscheck.py) | runs RCTab on those files, parses its report, diffs it against ours, and runs the two sweeps. |

Converted inputs for the cases run so far are committed under [`rctab_cases/`](rctab_cases/) — small, and they make the result reproducible without re-running the converter.

## Getting RCTab

The [release zips](https://github.com/BrightSpots/rcv/releases) bundle their own JDK 21, so nothing else is required. **Verify the published `.sha512` before unpacking** — it is right there next to the asset:

```bash
gh release download v2.1.0 --repo BrightSpots/rcv --pattern "rctab_v2.1.0_macOS_X64.zip*"
shasum -a 512 -c <(sed 's/$/  rctab_v2.1.0_macOS_X64.zip/' rctab_v2.1.0_macOS_X64.zip.sha512)
unzip rctab_v2.1.0_macOS_X64.zip -d unpacked
export RCTAB_HOME="$PWD/unpacked/rcv"
```

RCTab writes an `rcv_*.log` into the **working directory** on every launch, so run it from a scratch dir, not from the repo. `rctab_crosscheck.py` already contains its runs inside the case output folder and cleans up after itself.

## Running it

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/rctab_crosscheck.py 06_Other/RCV_IRV/cases/batch_all_out_cycle_c3_b3.yaml --candidate-orders all --row-permutations
```

```
  RCTab count:
    round 1 (threshold 2):  Amy 1  Bruno 1  Clara 1   [eliminated Clara → Amy+1]
    round 2 (threshold 2):  Amy 2  Bruno 1   [ELECTED Amy]
    ⚖  Candidate "Clara" lost a tie-breaker in round 1 against "Amy" and "Bruno". …
  RCTab      : Amy
  this repo  : Amy
  ✅ AGREE
```

## The two things that make this worth doing

**The winner agreeing is the boring half.** All four tie cases agree, which is reassuring and not very interesting. The interesting half is *how each engine reaches a decision the ballots don't settle*:

- `--row-permutations` re-runs the case under every ordering of the ballot rows. An **anonymous** rule ignores who cast which ballot, so the winner must not move. RCTab's doesn't (6/6, 24/24). The vendored pyrankvote's does — three different winners across six orderings.
- `--candidate-orders` varies the declared candidate order, which is what `tiebreakMode: useCandidateOrder` breaks ties by. RCTab's winner **does** move here — but the lever is a value written in the config and named in the audit log, where ours is the order the YAML's ballot rows happen to be typed in.

Both engines are arbitrary on a dead tie. Only one is auditable. That is the whole finding.

## Two traps the converter handles for you

**A rank is not a score.** Our ballots and RCTab's mean opposite things by the same numbers — our `5` is best and our `0` is a counted zero; RCTab's `1` is best and *blank* is unranked. A pass-through would rank every voter's favourite last.

**Equal ranks are refused by default.** This repo's ranked ballots may tie candidates in a level (`Ava=Bianca>Cara`) and the LH engine honours that as indifference. RCTab has no such concept — two candidates at one rank is an **overvote**, disposed of by `overvoteRule`. Converting silently would compare two different elections, so it stops. `--allow-equal-ranks` is there for studying the overvote rules on purpose.

Score files are refused outright: RCTab counts ranked ballots only, so it has nothing to say about STAR, Score, Approval or Ranked Robin.

## What agreement here is worth — and what it isn't

RCTab is certified as an **implementation**. A match is real evidence that our arithmetic is the arithmetic jurisdictions run. It is **not** evidence that instant runoff picks good winners: every [center squeeze](../../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) and [exhausted ballot](../../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) critique in this library survives RCTab counting perfectly. Don't cite a green check here as a verdict on the method.

## Gotchas found the hard way

- `decimalPlacesForVoteArithmetic` must be **1–20**; `"0"` is rejected by config validation even though it is meaningless for a whole-vote single-winner count.
- The `genericCsv` provider is **absent from the published documentation** — it is in the code (`ContestConfig.java`, `Provider.CSV`) and in the v2.1.0 release. Read the source, not the docs site, when a field looks missing.
- The bundled `sample_input/generic_csv_test/` ships the config but **not** its CSV; get that from the [upstream test data](https://github.com/BrightSpots/rcv/tree/develop/src/test/resources/network/brightspots/rcv/test_data/generic_csv_test) if you want to self-test the install. Worth doing once — it reproduces upstream's expected winner (Cucumber, round 4, 53.84%) and proves the toolchain before you trust it on your own files.
- RCTab's **`batchElimination` is not the operation our `batch_all_out_*` cases are named after.** Its batch drops candidates who are *mathematically out of reach* (the leapfrogging test in `Tabulator.runBatchElimination`), not candidates tied for last — so turning it on changes nothing in these cases, and RCTab structurally never empties the field. See [batch_elimination.md](../../../07_Concepts/topics/ties/batch_elimination.md) limit 4.

*Sibling: [`pref_voting` cross-check](../pref_voting_tabulation_engine/README.md) — the academic referee, which covers Condorcet and the score family too.*
