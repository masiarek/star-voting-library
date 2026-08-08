# RCTab cross-check — running our cases through the certified tabulator

[RCTab](https://www.rcvresources.org/rctab) is the federally-tested (VVSG), state-certified, open-source tabulator that US jurisdictions actually run on election night. This folder converts this repo's ranked-ballot cases into RCTab input and runs them, so a case can be checked against production election software rather than only against other teaching engines.

The concept page — what RCTab is, what its agreement is and isn't worth — is [RCTab](../../../07_Concepts/tabulation_engines/rctab.md). The findings from the first run are on [Batch elimination](../../../07_Concepts/topics/ties/batch_elimination.md#what-a-certified-tabulator-does-instead).

## The two scripts

| | |
|---|---|
| [`rctab_convert.py`](rctab_convert.py) | a ranked YAML → `<stem>.csv` + `<stem>_config.json`. **No Java needed.** |
| [`rctab_crosscheck.py`](rctab_crosscheck.py) | runs RCTab on those files, parses its report, diffs it against ours, and runs the two sweeps. |
| [`ut_json_export.py`](ut_json_export.py) | a ranked YAML → **Universal RCV Tabulator JSON** (the shape RCTab's own `_detailed_report.json` uses), recomputing the per-candidate transfers our text report omits. **No Java needed.** Feeds [RCVis](../../../07_Concepts/tabulation_engines/rcvis.md) for Sankey art; refuses score ballots, and disagrees with the engine on a dead tie (see its docstring). |

## STV — the leg that was missing

Multi-seat cases convert too, and this is where the cross-check earns its keep. Ranked Robin has three independent counts behind it; **STV had one and a half.** BetterVoting is the usual second opinion, and it *crashes* on any count whose eliminations leave a sole hopeful who then reaches quota — the [sole-survivor bug](../../../06_Other/STV/bv_stv_sole_survivor_crash/README.md) — which is exactly the shape of the repo's gentlest STV case. Those cases rested on the vendored `pyrankvote` alone.

**All ten STV elections in the library now agree with RCTab on the seated set**, including the two BetterVoting cannot count at all.

That comparison is only worth anything because the **quota is pinned on both sides**, and RCTab makes it a config field. Its own `docs/config_file_documentation.txt`:

```text title="RCTab config_file_documentation.txt — quoted, not paraphrased"
"nonIntegerWinningThreshold" optional
  if true,  threshold = V/(S+1) + 10^-d
  if false, threshold = floor(V/(S+1)) + 1
  note: only valid for multi-seat contests
```

That is this repo's [fork 1](../../../06_Other/STV/README.md#where-it-genuinely-gets-complicated) as a checkbox. The converter sets it **true**, because `pyrankvote` elects at `votes - 1e-6 >= V/(S+1)` — strictly above the exact Droop quota by a hair, the same shape as RCTab's `+ 10⁻ᵈ`. Left false, RCTab would count an election one whole vote different and any disagreement would be about configuration rather than about the count. `--hand-count-quota` flips it back on purpose, which is how you make the fork move real numbers instead of describing it.

Multi-seat also picks `winnerElectionMode: multiWinnerAllowMultipleWinnersPerRound` — "may elect more than one winner per round when there are multiple candidates exceeding the winning threshold", which is what `pyrankvote` does in one pass. The `OnlyOneWinnerPerRound` sibling would stagger the seats and desynchronise the rounds against ours.

A non-STV multi-seat case is **refused** rather than converted: every multi-winner mode RCTab has is STV, so pointing it at Bloc RR, SNTV or Bloc STAR would compare two different methods and call it agreement.

### What it found

Agreement on winners was the boring half, as ever. Running ex14 three ways separated two things the repo had been treating as one:

| | hand count, quota 4 | ours, exact 3.00 | RCTab, exact 3.0001 |
|---|---|---|---|
| Brontë after Austen's surplus | 2 | 3.00 — ties Camus | 2.9995 — just short |
| eliminations | Dickens, Brontë | **none** | Dickens, Brontë |
| seats | Austen + Camus | Austen + Camus | Austen + Camus |

Our engine's vanishing elimination round looks like a consequence of the exact quota. It isn't: RCTab uses the same exact quota and eliminates normally. Ours sets the bar at exactly `V/(S+1)`, so Brontë lands on precisely 3.00, ties Camus, and is set aside by a "cannot change the result" shortcut; RCTab's bar is a hair higher, so she lands on 2.9995 and is simply eliminated. **Quota fork and tie handling are two different forks**, and only a third engine makes them separable. Written up on [exercise 14, part (f)](../../../01_STAR/05_Practice/ex14_transfer_machine.md#f).

## Which RCTab you have matters

RCTab refuses a config claiming a version newer than itself (`Unable to process a config file with version 2.1.0 using older version 2.0.0`), so `rctab_crosscheck.py` asks the installed app for its version and writes that into the config. `--pin-version` opts out. Two 2.0.0-vs-2.1.0 differences are handled for you: the version string, and `idColumnIndex`, which 2.0.0 rejects outright on a `CSV` source. `RCTAB_HOME` may point at an unpacked release (`bin/RCTab`) **or** at a macOS `RCTab.app`.

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

## The whole IRV corpus — `rctab_sweep.py`

`rctab_crosscheck.py` is the microscope (one case, round by round, with the sweeps). [`rctab_sweep.py`](rctab_sweep.py) is the wide-angle lens: it converts and counts **every** ranked case in the library in one pass, one line each, so a regression anywhere shows up as a row that stopped saying AGREE.

```bash
RCTAB_HOME=… uv run STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/rctab_sweep.py --irv
```

**69 single-winner IRV elections, 68 AGREE, 1 disagreement — and the disagreement was already documented.** 8 of the 69 needed a tiebreak to reach an answer at all. Ranked Robin is refused rather than swept: RCTab implements no Condorcet method, so agreement there would be a coincidence of the profile rather than a check of anything.

The one disagreement is [`coombs_ex20_district1`](../../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex20_district1.yaml), and it is the sweep earning its keep. That file's own description had flagged a **first-round elimination tie** — A and B level on 9, and which one goes decides the election (drop A → B wins 18–16; drop B → C wins 25–9). Our engine drops A silently; rcv-lab.org drops B, which is how the tie was originally noticed. RCTab drops B, elects C 25–9, and — unlike either of the others — *prints the tie in its audit log*. Sweeping its declared candidate order over all six permutations returns C three times and B three times.

So the corpus contains exactly one case where two engines legitimately differ, it was known and written down beforehand, and a certified tabulator has now independently confirmed both branches are legal. That is the outcome you want from a cross-check: no silent surprises, and the one loud result lands on a caveat the library had already published.

**Skips are printed, never swallowed.** A case the converter refuses — equal ranks, a score ballot, a non-STV multi-seat method — is listed with its reason, and the summary always states how many were converted, skipped and failed. A sweep that quietly counted 60 of 70 and reported "all agree" would be worse than useless.

## What agreement here is worth — and what it isn't

RCTab is certified as an **implementation**. A match is real evidence that our arithmetic is the arithmetic jurisdictions run. It is **not** evidence that instant runoff picks good winners: every [center squeeze](../../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) and [exhausted ballot](../../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) critique in this library survives RCTab counting perfectly. Don't cite a green check here as a verdict on the method.

## Gotchas found the hard way

- `decimalPlacesForVoteArithmetic` must be **1–20**; `"0"` is rejected by config validation even though it is meaningless for a whole-vote single-winner count.
- The `genericCsv` provider is **absent from the published documentation** — it is in the code (`ContestConfig.java`, `Provider.CSV`) and in the v2.1.0 release. Read the source, not the docs site, when a field looks missing.
- The bundled `sample_input/generic_csv_test/` ships the config but **not** its CSV; get that from the [upstream test data](https://github.com/BrightSpots/rcv/tree/develop/src/test/resources/network/brightspots/rcv/test_data/generic_csv_test) if you want to self-test the install. Worth doing once — it reproduces upstream's expected winner (Cucumber, round 4, 53.84%) and proves the toolchain before you trust it on your own files.
- RCTab's **`batchElimination` is not the operation our `batch_all_out_*` cases are named after.** Its batch drops candidates who are *mathematically out of reach* (the leapfrogging test in `Tabulator.runBatchElimination`), not candidates tied for last — so turning it on changes nothing in these cases, and RCTab structurally never empties the field. See [batch_elimination.md](../../../07_Concepts/topics/ties/batch_elimination.md) limit 4.

*Sibling: [`pref_voting` cross-check](../pref_voting_tabulation_engine/README.md) — the academic referee, which covers Condorcet and the score family too.*
