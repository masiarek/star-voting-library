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

## Status

**Not wired up.** This page documents an opportunity, not a shipped cross-check — there is no RCTab converter, config generator, or guard test in the repo today, and no RCTab result is quoted anywhere in this library. The barrier is modest (a JDK 21 toolchain, a CSV writer, a JSON diff) but real enough that it hasn't been paid, and the payoff is narrower than it first looks: it would cover the ranked-ballot engine only, which `pref_voting` already cross-checks for IRV winners.

What would make it worth doing is the *tie* work above — the one place where our engine is knowingly weak and RCTab is explicit. If you're picking this up, start there rather than with the cases that already agree.

*Up: [tabulation engines](README.md) · the method: [RCV-IRV](../../06_Other/RCV_IRV/README.md) · the other referees: [`pref_voting`](cross_checking_with_pref_voting.md) · [BetterVoting](bettervoting_and_the_engine.md).*
