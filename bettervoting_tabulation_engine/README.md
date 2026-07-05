# BetterVoting (BV) Tabulation Engine — technical description

Reverse-engineered from the source of [Equal-Vote/bettervoting](https://github.com/Equal-Vote/bettervoting)
(local clone: `/Volumes/T7/Voting/BetterVoting/BV/bettervoting`). This folder documents **how
BetterVoting.com actually counts ballots** — the same engine behind the live site and the
sandbox. All paths below are relative to that repo root.

## Where it lives

BetterVoting is a TypeScript monorepo with three packages: **shared** (domain types),
**backend** (Express API + the tabulators), and **frontend** (React 17 / MUI results views).
The engine is entirely **server-side** — the browser never tabulates; it only renders the
JSON result object.

```
packages/shared/src/domain_model/ITabulators.ts     # the input/output type contract
packages/backend/src/Tabulators/                     # the engine
packages/backend/src/Controllers/Election/
    getElectionResultsController.ts                  # production entry point (GET /API/ElectionResult/:id)
    sandboxController.ts                             # sandbox entry point
packages/frontend/src/components/Election/Results/   # renders roundResults / summaryData / logs
```

## How a count runs

`getElectionResultsController` authorizes the request, loads every ballot, and for each race
builds a candidate list (including approved write-ins) and a **Cast Vote Record** (`rawVote[]`,
`marks: candidateId -> score/rank`). It then calls
`shuffleCandidatesForRandomTiebreak(...)` to fix a reproducible `tieBreakOrder`, dispatches to
the right tabulator via the `VotingMethods` map in `VotingMethodSelecter.ts`, and returns
`{ election, results }`.

Every tabulator has the same signature and is **pure** — no DB, no IO:

```ts
(candidates, votes, nWinners?, electionSettings?) => ResultsType
```

The full production pipeline in `getElectionResultsController.ts`:

1. **Authorize** — an open election with `public_results: false` throws `Forbidden`; otherwise the caller needs `canViewPreliminaryResults`.
2. **Load ballots** — `BallotModel.getBallotsByElectionID(id)`.
3. **Build candidates** per race — `race.candidates` plus any *approved* write-ins (ids from `makeWriteInCandidateId`).
4. **Build the CVR** — each ballot's vote for the race becomes a `rawVote` (`marks: candidateId -> score/rank`); write-ins are resolved to candidates by alias (`trimLower`), duplicates keep the first and warn, `overvote_rank`/`has_duplicate_rank` are carried along.
5. **Shuffle** — `shuffleCandidatesForRandomTiebreak(...)` fixes a reproducible `tieBreakOrder`; the resulting id order is returned as `perm`.
6. **Tabulate** — `VotingMethods[voting_method](candidates, cvr, num_winners, settings)`.
7. **Respond** — random-tie logs get `tiebreak_candidate_names` attached, `writeInDiagnostics` is added, and the response is `{ election, results }` (one entry per race).

The **sandbox** (`sandboxController.ts`) calls the same `VotingMethods` map with no persistence or auth gating.

## Type contract (`ITabulators.ts`)

Inputs and outputs are shared types, so the engine emits the exact objects the UI renders:

- **`rawVote`** `{ marks: candidateId -> number|null, overvote_rank?, has_duplicate_rank? }`
- **`candidate`** `{ id, name, tieBreakOrder, votesPreferredOver, winsAgainst }`
- **`genericResults`** `{ votingMethod, elected, tied, other, roundResults[], summaryData, tieBreakType }`
- **`roundResults`** `{ winners, runner_up, tied, tieBreakType, logs[] }`
- **`summaryData`** always carries `nOutOfBoundsVotes`, `nAbstentions`, `nTallyVotes` (where `nVotes = nOutOfBoundsVotes + nAbstentions + nTallyVotes`), plus method-specific fields.
- **`tieBreakType`** ∈ `none | score | head_to_head | five_star | random`.

## The shared core (`Util.ts`)

Most methods lean on three helpers:

- **`getSummaryData`** filters invalid ballots (bounds / abstention → `nOutOfBoundsVotes`,
  `nAbstentions`, `nTallyVotes`) and builds the cross-candidate matrices: pairwise
  `votesPreferredOver` / `winsAgainst`, total `score`, `copelandScore`, and `fiveStarCount`.
  A `cardinal` vs `ordinal` switch decides whether "preferred" means higher score or lower rank
  (with rank 0 remapped to ∞).
- **`sortCandidates`** — generic multi-field sort that always falls back to `tieBreakOrder` and
  uses `fraction.js` for exact comparisons.
- **`runBlocTabulator`** — generic bloc/sequential multi-winner driver used by STAR, Approval,
  Plurality and Ranked Robin.

## The seven methods

| Method | File | Ballot | Core rule |
|---|---|---|---|
| **STAR** | `Star.ts` | score 0–5 | Score to pick top-2, then pairwise automatic runoff. Tie cascade: score → head-to-head → five-star → random |
| **STAR_PR** | `AllocatedScore.ts` | score 0–5 | Proportional (Allocated Score), Hare quota `V/nWinners`, ballot weight spent on winners |
| **Approval** | `Approval.ts` | approve 0/1 | Most approvals; random tiebreak |
| **Plurality** | `Plurality.ts` | choose-one | Most votes; tracks overvotes; random tiebreak |
| **Ranked Robin** | `RankedRobin.ts` | ranked | Highest Copeland (win +1, tie +0.5); 2-way tie → head-to-head; else random |
| **IRV** | `IRV.ts` | ranked | Eliminate lowest, transfer to next choice, quota `⌊n/2+1⌋` |
| **STV** | `IRV.ts` | ranked | IRV + Droop quota `⌊n/(nWinners+1)+1⌋` and fractional surplus transfer |

IRV/STV/STAR_PR use **`fraction.js`** (exact rationals) so surplus and weight transfers never
drift on floating point. Every round emits `logs` (i18n keys) that become the human-readable
count narrative in the results UI.

A few method specifics worth keeping:

- **IRV/STV ballot exhaustion** is tracked as `nExhaustedViaOvervote`, `nExhaustedViaSkippedRank`, and `nExhaustedViaDuplicateRank`. Skipped-rank exhaustion is governed by `exhaust_on_N_repeated_skipped_marks` in `ElectionSettings`; a ballot also exhausts when its top remaining rank equals its `overvote_rank`.
- **STV surplus transfer** — on election, surplus fraction `= (maxVotes − quota) / maxVotes`; each of the winner's ballots is down-weighted by that fraction (floored to 5 dp) and redistributed. If the remaining candidates can fill every remaining seat, they are all elected.
- **STAR tie-breaks** escalate to the most "extreme" protocol reached, reported via `setTieBreak` in priority order `none → score → head_to_head → five_star → random`.

## Deterministic "random" tie-breaks

`shuffleCandidatesForRandomTiebreak.ts` + `tinyrand.ts` make random tie-breaks **reproducible**:
a deterministic PRNG (TinyRand, language-agnostic) is seeded with
`(rawVoteCount + hash(raceId)) >>> 0` and shuffles candidates once into a fixed order. The raw-vote
term re-rolls the order as new ballots arrive; the race hash keeps identical-candidate races from
sharing a tie order. `electionCreateDate` is passed but currently unused (reserved for versioning).

> This is exactly the surface area of open issue **#1417** — because the seed tracks the live
> ballot count, the tie-break lot order isn't fixed until polls close. The issue proposes
> deterministic **pre-published** lot numbers instead.

## Tests

Jest unit tests sit beside each tabulator (`*.test.ts`); run with
`npm test -w @equal-vote/star-vote-backend`. Root fixture: `tabulator_test_cases.yaml`.

# file: README.md
