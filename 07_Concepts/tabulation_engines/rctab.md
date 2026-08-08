# RCTab — the certified tabulator that counts real RCV elections

**One line:** [RCTab](https://www.rcvresources.org/rctab) is the federally-tested, open-source tabulator that actual US jurisdictions use to count ranked-choice elections — which makes it a *different kind* of witness from this library's other cross-checks, and the one whose agreement would carry the most weight outside a classroom.

→ upstream: [BrightSpots/rcv](https://github.com/BrightSpots/rcv) (Java, MPL-2.0) · docs: [rctab-docs.readthedocs.io](https://rctab-docs.readthedocs.io/) · compare: [cross-checking with `pref_voting`](cross_checking_with_pref_voting.md).

---

## Why this one is worth knowing about

This library already checks itself against two outside engines — [BetterVoting](bettervoting_and_the_engine.md) and [`pref_voting`](cross_checking_with_pref_voting.md). Both are excellent, and neither is what a county actually runs on election night.

RCTab is. Built by Bright Spots with the Ranked Choice Voting Resource Center, it is described by its publisher as the most comprehensive [RCV](../../06_Other/RCV_IRV/concepts/RCV_or_IRV_whats_the_right_word.md) tabulation module tested under the federal Voluntary Voting System Guidelines, and it has been through state certification in New York, Utah and Michigan. It reads cast vote records straight out of Dominion, ES&S, Hart and Clear Ballot systems. When RCTab and this repo's vendored engine agree on a ballot set, that agreement means something a second teaching engine can't supply: *the counting rules we teach are the counting rules that get used.* <!-- terminology-ok: bare RCV names the certified product and the linked page title -->

That authority cuts both ways, and it is worth being precise about what a match would and wouldn't prove. RCTab is certified as an *implementation*, not as an endorsement of instant runoff as a method — every critique this library makes of [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md), [exhausted ballots](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) and [non-monotonicity](../../06_Other/RCV_IRV/concepts/RCV_IRV_non_monotonicity.md) survives RCTab counting the ballots perfectly. A cross-check against it would confirm our arithmetic, not settle the argument.

## Does it have an API?

**No web API — but yes, a scriptable command line, which is the part that matters for us.**

There is no REST or HTTP service, no hosted endpoint, and no published library entry point. RCTab is a desktop JavaFX application you run locally. What it *does* have is a headless mode:

```bash
rcv --cli path/to/config.json
```

or, building from source with the Gradle wrapper:

```bash
./gradlew run --args="--cli path/to/config.json"
```

It needs **JDK 21**. A contest is described entirely by a JSON config file (CVR file paths, candidate list, tabulation rules, output settings), and each run writes three timestamped artifacts:

| Output | Use to us |
|---|---|
| summary `.csv` | round-by-round vote totals per candidate, plus the winner(s) |
| summary `.json` | the same data, machine-readable — this is what a comparison harness would parse |
| audit `.log` | the full elimination/transfer trail |

So the automation shape is: emit a config + a CVR file per case → run the CLI → parse the summary JSON → diff the winner and the round-by-round tallies against our own report. That's the same pattern as the existing `pref_voting` guard, just with a subprocess and a JVM in the middle instead of a Python import.

## What it could check — and what it can't

RCTab counts **ranked ballots only**. Its winner-election modes are `singleWinnerMajority`, four multi-winner STV variants, and `multiPassIrv` — every one of them a ranked count.

| Our method | RCTab can check it? |
|---|---|
| **RCV-IRV** (single-winner) | ✅ this is exactly its job |
| **STV** (multi-winner) | ✅ several transfer variants |
| **STAR** | ❌ no score ballots at all |
| **Score / Range**, **Approval**, **Majority Judgment** | ❌ same |
| **Ranked Robin** (Copeland) | ❌ ranked ballots, but RCTab implements no Condorcet method |

So RCTab is a candidate cross-check for **exactly one** of this library's engines: the vendored `pyrankvote` in [`RCV_IRV_tabulation_engine/`](../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/README.md). It has nothing to say about the STAR side, where [`pref_voting`](cross_checking_with_pref_voting.md) and BetterVoting remain the referees.

## The bridge: the `genericCsv` provider

The obvious objection is that we don't have Dominion CVR exports — our cases are small YAML files. The answer is a sixth provider that the **published documentation doesn't mention**: alongside `cdf`, `clearBallot`, `dominion`, `ess` and `hart`, the code carries

```java
CSV("genericCsv", "CSV"),
```

confirmed present in the released **v2.1.0** tag (2026-07-07), not just on `develop`. Its reader's own header states the design: *"Parses a CSV with candidates in columns, cast vote records in rows, and vote rankings in cells."* One contest per file.

The layout is set by four 1-based config fields on the CVR source — `firstVoteColumnIndex`, `firstVoteRowIndex`, and the optional `idColumnIndex` / `precinctColumnIndex` / `batchColumnIndex`. The first row at or after `firstVoteColumnIndex` holds **candidate names** (a blank one is a fatal error); every later row is one ballot, and each cell holds that candidate's **rank as an integer**, blank meaning unranked.

Which is to say: RCTab's generic CSV has the same shape as this repo's `ballots:` block — a candidate header row, then one row per voter, one column per candidate. Converting a case is a transposition, not a translation.

## The trap: a rank is not a score

The two formats look alike and mean opposite things, so any converter has to invert.

| | Our score ballot | RCTab generic CSV |
|---|---|---|
| Header | `Ada,Ben,Cara` | `Ada,Ben,Cara` |
| A row | `5,2,0` | `1,2,3` |
| Best value | **highest** (5) | **lowest** (rank 1) |
| Omitted | `0`, or a [marker](../../YAML_library/ORGANIZATION.md) — counted, worth nothing | **blank** — not ranked at all |

A converter that passed our numbers through unchanged would hand RCTab a ballot ranking the voter's *favorite* last. And our ranked cases are written in the `A>C>B` string form rather than as columns, so those need expanding into rank integers per candidate — with ties refused, since RCTab's ranked ballots don't take equal ranks.

## Where it would earn its keep

Beyond confirming winners, there's one specific gap RCTab is unusually well-suited to close. The vendored `pyrankvote` has a [known limitation on elimination ties](../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/README.md#known-limitation-elimination-ties): when the ballot-based ladder runs out, the winner falls out of the order the ballot rows happen to be written in, and the report doesn't say so. That's the soft spot behind the [batch-elimination cases](../topics/ties/batch_elimination.md) and the `put_two_universes` / `batch_all_out_*` stress tests.

RCTab makes that choice explicit instead. Its `tiebreakMode` is a required, named setting — `random`, `stopCountingAndAsk`, `previousRoundCountsThenRandom`, `previousRoundCountsThenAsk`, `useCandidateOrder`, `generatePermutation` — and `useCandidateOrder` in particular is a *declared, reproducible* rule where ours is an accident of file layout. Running the pathological cases through RCTab under each mode would turn "the engine has a quiet tiebreak" into a documented comparison of how production systems make the same decision out loud. It has the flags for the other awkward corners too: `batchElimination`, `continueUntilTwoCandidatesRemain`, `exhaustOnDuplicateCandidate`, `maxSkippedRanksAllowed`, and three `overvoteRule` settings — each one a policy question our engine answers implicitly.

## Status: wired up

The converter and runner live in [`tools_adam/rctab_tabulation_engine/`](../../STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/README.md) — `rctab_convert.py` (YAML → CSV + config, no Java needed) and `rctab_crosscheck.py` (runs RCTab, parses its report, diffs it against ours). The converted inputs for the cases run so far are committed beside them.

**First run: the four tie cases.** All four winners agree with this repo's engine. The interesting results were the two sweeps, written up on [Batch elimination § what a certified tabulator does instead](../topics/ties/batch_elimination.md#what-a-certified-tabulator-does-instead):

- **RCTab is anonymous where our engine is not.** Across every ballot-row ordering (6, 6 and 24 runs) its winner never moves; the vendored pyrankvote's changes with the typing order.
- **Its arbitrariness is declared.** The dead tie still decides the election, but the lever is the candidate order in the config — and every tiebreak is named in the audit log, including the 2–2 final round our own report passes over in silence.
- **Its `batchElimination` is a different rule** from the one our cases are named after: it drops candidates who are mathematically out of reach, never candidates merely tied, so it cannot empty the field.

**Second run: every STV case in the library.** All ten agree with this repo's engine on the seated set — and this is the run that mattered most, because STV is where our cross-checking was thinnest. Ranked Robin is checked three ways; STV had `pyrankvote` and BetterVoting, and BetterVoting **crashes** on any count ending with a sole hopeful at quota ([the sole-survivor bug](../../06_Other/STV/bv_stv_sole_survivor_crash/README.md)), which is the shape of the repo's gentlest STV case. Those cases rested on a single engine until now. RCTab counts them without complaint.

Two things make that comparison meaningful rather than decorative:

- **The quota is pinned on both sides.** RCTab's `nonIntegerWinningThreshold` is documented in its own config reference as `threshold = V/(S+1) + 10^-d` when true and `floor(V/(S+1)) + 1` when false — [fork 1](../../06_Other/STV/README.md#where-it-genuinely-gets-complicated) as a checkbox. The converter sets it **true**, matching the exact Droop bar `pyrankvote` applies. Left false it would count an election one whole vote different, and every disagreement would be about configuration.
- **It separated two forks we had been treating as one.** Our engine finishes ex14 with *no elimination round at all*, which reads like a consequence of the exact quota. It isn't — RCTab uses the same exact quota and eliminates normally. Ours puts the bar at exactly `V/(S+1)`, so Brontë lands on precisely 3.00, ties Camus, and is set aside by a "cannot change the result" shortcut; RCTab's bar sits a hair higher, she lands on 2.9995, and is simply eliminated. Quota choice and tie handling are **different forks**, and only a third engine made them separable. ([Exercise 14, part (f)](../../01_STAR/05_Practice/ex14_transfer_machine.md#f).)

It is a **report, not a guard** — there's no pytest gating on RCTab, because that would put a 66 MB JVM download in the test path. Run it when a ranked case's tie behaviour matters, and whenever an STV result is going to be quoted.

**Scope hasn't changed:** this covers the ranked-ballot engine only — now both of its counts, IRV and STV. STAR, Score, Approval and Ranked Robin still answer to [`pref_voting`](cross_checking_with_pref_voting.md) and BetterVoting. A multi-seat case that *isn't* STV is refused rather than converted, since every multi-winner mode RCTab has is STV: pointing it at Bloc RR, SNTV or Bloc STAR would compare two methods and call it agreement.

*Up: [tabulation engines](README.md) · the method: [RCV-IRV](../../06_Other/RCV_IRV/README.md) · the other referees: [`pref_voting`](cross_checking_with_pref_voting.md) · [BetterVoting](bettervoting_and_the_engine.md).*
