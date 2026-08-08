# The BetterVoting JSON export — field-by-field

**Level: reference · deep dive**

**One line:** a BetterVoting export is `JSON.stringify({Election, Ballots, Results})` of three raw in-memory objects — not a designed format — so it mixes casing, repeats every candidate four times, overloads one `score` field to mean score *or* rank, and is the reason [issue #1420](https://github.com/Equal-Vote/bettervoting/issues/1420) is open.

This page documents what the export actually contains, so a reader can open any frozen `*_bv_export.json` in this repo and know what each key means. It is the JSON counterpart to [How to read a BetterVoting results page](reading_a_bv_results_page.md) (the *visual* report) and to [BV's database schema](database_schema/README.md) (the *storage* model — the `Election` block below is essentially one `electionDB` row).

Everything here was checked against the **211 frozen exports** committed in this repo (401 race results across seven voting methods), not against a single sample — where a key is inconsistent, the counts say so.

---

## The three top-level keys

| Key | What it is | API endpoint that produces it |
|---|---|---|
| `Election` | The election's configuration: races, candidates, settings, ownership, state | `GET /API/Election/{id}` → `.election` |
| `Ballots` | Every cast ballot, anonymized | `GET /API/Election/{id}/anonymizedBallots` → `.ballots` |
| `Results` | BetterVoting's own tabulation, **one entry per race** | `GET /API/ElectionResult/{id}` → `.results` |

The UI's "Download JSON" button concatenates exactly these three. [`fetch_bv_export.py`](../../../STARVote_LH_tabulation_engine/tools_adam/fetch_bv_export.py) reproduces it from the three anonymous GETs — verified byte-identical on `vqyqkr` for `Election` and `Results`, and identical up to ballot order for `Ballots`.

Two variants appear in the frozen corpus:

- **`Results: []` plus a `_note`** — written by `fetch_bv_export.py --without-results` when BV's tabulator 500s on that election (the STV sole-survivor crashers). The gap is self-documenting rather than silent.
- **`election` / `precinctFilteredElection` / `voterAuth`** (lowercase, one file) — a raw `GET /Election` response saved before the house format settled. Not the export shape; don't copy it.

---

## `Election`

Present in all 210 exports that have the key. Values below are what the corpus actually contains.

| Field | Type | Notes |
|---|---|---|
| `election_id` | string | The 6-character **bvid** (`yyvwrj`). The whole repo names case files after it. |
| `title` | string | **Permanent and public** — the API cannot rename it. House rule: it carries the `BV<n>` test id. |
| `description` | string \| null | Also permanent. `null` on UI-created elections; ours always ends in the lesson backlink. |
| `frontend_url` | string | Always `""` in practice. Dead field. |
| `start_time` / `end_time` | ISO-8601 \| null | `null` on 206 of 211 — an election with no window is simply open. |
| `owner_id` | uuid | Creator. Does **not** grant UI admin rights (see [the API notes](bv_api_election_creation_notes.md)). |
| `audit_ids` / `admin_ids` / `credential_ids` | null | `null` in **every** frozen export. Setting `admin_ids` at mint is ignored by BV. |
| `state` | enum | `open` (188) · `draft` (12) · `closed` (10). Results tabulate on demand — an election need not be closed. |
| `races` | array | One object per contest. See below. |
| `settings` | object | See below. |
| `auth_key` | string \| absent | The RS256 public PEM. Present on only 22 exports; the API requires it at *create* time. |
| `claim_key_hash` | sha-256 hex | Owner's claim key digest. |
| `is_public` | bool \| null | `null` on 197 — meaning "not set", not "false". Listability is decided elsewhere. |
| `create_date` | **ISO-8601 string** | e.g. `2026-07-30T02:14:33.849Z`. |
| `update_date` | **epoch-ms string** | e.g. `"1785378669765"`. A *different encoding of the same kind of value* — one of the defects #1420 names. |
| `head` | bool | `true` on the current version. BV stores elections append-only; see [database_schema](database_schema/README.md). |
| `ballot_source` | enum | `live_election` throughout (vs an admin bulk upload). |
| `public_archive_id` | null | Unused in the corpus. |

### `Election.settings`

Only the first six keys appear on every election; the rest are era-dependent, so **read them with `.get()`, never by index**.

| Field | Seen | Values |
|---|---|---|
| `voter_access` | 210/210 | `open` |
| `voter_authentication` | 210/210 | Object of flags — `{"ip_address": false, "voter_id": false, …}`, sometimes `{}` |
| `ballot_updates` | 210/210 | `false` |
| `public_results` | 210/210 | `true` |
| `random_candidate_order` | 210/210 | `false` (198) / `true` (12) |
| `require_instruction_confirmation` | 210/210 | `true` (204) / `false` (6) |
| `time_zone` | 198/210 | `America/Los_Angeles`, `America/New_York` |
| `term_type` | 25/210 | `election` |
| `contact_email` | 25/210 | string, often `""` |
| `draggable_ballot` | 19/210 | `false` |
| `max_rankings` | 1/210 | Normally lives on the **race**, not here |

### `Election.races[]`

| Field | Seen | Notes |
|---|---|---|
| `title` | 419/419 | Permanent. The `/vote` page leads with it, which is why house rule puts `BV<n>` on every race title. |
| `race_id` | 419/419 | `"0"` on single-race elections; a uuid on ones minted by our script. `Ballots[].votes[].race_id` joins to this. |
| `num_winners` | 419/419 | Seats. |
| `voting_method` | 419/419 | `STAR` · `Approval` · `Plurality` · `IRV` · `STV` · `RankedRobin` · `STAR_PR` (BV's own strings). |
| `candidates` | 419/419 | `[{candidate_id, candidate_name}]`. **Ballot order is this order.** |
| `description` | 410/419 | Per-race blurb. |
| `enable_write_in` | 247/419 | Absent entirely on pre-flag-era races. |
| `max_rankings` | 146/419 | Ranked methods only — the rank cap. |

---

## `Ballots`

Flat and simple — three nested levels and nothing else:

```jsonc
{ "ballot_id": "b-kk2bwj7v",
  "election_id": "yyvwrj",
  "precinct": null,                  // null in all 419 frozen ballots
  "votes": [                         // one entry per RACE the voter voted in
    { "race_id": "0",
      "scores": [ { "candidate_id": "c-pb2", "score": 4 } ] } ] }
```

**`score` is overloaded — its meaning depends on the race's `voting_method`.** This is the single biggest trap in the format, because nothing inside `Ballots` says which reading applies; you must join back to `races[].voting_method`.

| Method | What `score` means | Values seen in the corpus |
|---|---|---|
| STAR, STAR_PR, Bloc STAR | A **score**, 0–5 | `0`–`5`, plus `null` |
| Approval | Approved or not | `0` / `1` only |
| Plurality | Chosen or not | `0` / `1`, plus `null` |
| IRV, STV, RankedRobin | A **rank** — `1` = top choice | `1`–`9` observed; `0` = unranked; plus `null` |

So a `3` means "three stars" on one race and "third choice" on the next race of the same election.

### `null` vs `0` — the distinction that matters

**A `null` score means the voter left that candidate blank; a `0` means they actively scored zero.** BV's tabulators count both as zero, but the export preserves the difference — 518 `null` scores across the frozen corpus. That is the raw material for every abstention lesson in this repo, and [`01_convert_json_yaml.py`](../../../YAML_library/1_positive/01_convert_json_yaml.py) carries it across as the blank marker `-` rather than flattening it to `0`.

The *CSV* download did flatten it (blank cell, ambiguous against a real `0`), which is what the Raw/Official split in PR #1419 was for. See [the abstain issues index](abstain_issues_index.md) for how this interacts with BV's open abstention tickets.

---

## `Results`

One entry per race, in race order. Seven top-level fields are universal; four more are method-specific.

| Field | Seen | Notes |
|---|---|---|
| `votingMethod` | 401/401 | **camelCase** — while `Election` and `Ballots` are snake_case. |
| `elected` | 401/401 | The winner(s), as full candidate objects. |
| `tied` / `other` | 401/401 | The rest, also as full candidate objects. |
| `roundResults` | 401/401 | Per-round detail; see below. |
| `summaryData` | 401/401 | The tally. |
| `tieBreakType` | 401/401 | `none` (338) · `random` (40) · `score` (14) · `head_to_head` (6) · `five_star` (3) — **which rung of the ladder actually fired.** |
| `perm` | 401/401 | Candidate ids in **tiebreak priority order**. See below. |
| `writeInDiagnostics` | 97 | Write-in handling. |
| `exhaustedVoteCounts`, `nExhaustedViaOvervote`, `nExhaustedViaSkippedRank`, `nExhaustedViaDuplicateRank` | 57 | **IRV/STV only** — exhausted-ballot accounting. |
| `logs` | 13 | A race-level log array on a few results, separate from the per-round one. |

### The candidate object, repeated four times

The same candidate object appears in `elected`, `tied`, `other`, `summaryData.candidates`, **and** again inside every `roundResults[].winners` / `.runner_up`. It carries:

| Field | Methods | Meaning |
|---|---|---|
| `id`, `name` | all | |
| `tieBreakOrder` | all | Integer, **ascending = higher priority**. |
| `votesPreferredOver` | all | Map `{opponent_id: count}` — **including self-vs-self at 0**. This is the O(n²) bloat #1420 names. |
| `winsAgainst` | all | Map `{opponent_id: bool}` — the pairwise wins, self-pair included. |
| `score` | STAR, Approval, Plurality, Score | The scoring-round total (or approvals / votes). |
| `fiveStarCount` | STAR only | Five-star counts — tiebreak rung 2. |
| `copelandScore` | RankedRobin only | Pairwise wins. |
| `hareScores` | IRV/STV only | Per-round vote counts. |

`winsAgainst` is genuinely useful despite the bloat: it encodes the full pairwise relation, which is how a **Condorcet cycle** shows up in a frozen file (`bv2212_g3f7r2` records Alice▸Ben, Ben▸Carla, Carla▸Alice).

### `summaryData`

`candidates` plus the ballot accounting, which is where the **denominators** come from:

- `nTallyVotes` — ballots that counted in this race
- `nAbstentions` — ballots that skipped it
- `nOutOfBoundsVotes` — rejected values
- `nOvervotes` — Plurality only
- `spentAboves`, `splitPoints`, `weight_on_splits`, `weightedScoresByRound` — STAR_PR only (the reweighting trace)

### `roundResults[]`

`winners` · `runner_up` · `tied` · `tieBreakType` · `logs`, plus `eliminated` on IRV/STV and `exhaustedVoteCount` / `isStartOfSearch` on IRV.

Round counts are method-shaped: STAR is usually one round (147 of 178), IRV usually two to four, and **STAR_PR emits zero rounds** — its trace lives in `summaryData` instead. One IRV race in the corpus has 60 rounds.

### `logs` — two incompatible shapes

| Shape | Methods | Example |
|---|---|---|
| **i18n dict** | STAR, IRV, STV | `{"key": "tabulation_logs.star.runoff_win", "winner": "A", "winner_votes": 1, …}` |
| **Plain English string** | Plurality, RankedRobin, Approval | `"Sushi wins the round after a random tiebreaker"` |

Anything parsing logs must handle both. The dict form is the good one — it names the rung (`runoff_tiebreak`, `five_star_tied`, `random_second`) in a machine-readable key. Surfacing these in BV's own report is tracked in [#1432](https://github.com/Equal-Vote/bettervoting/issues/1432).

### `perm` — the pre-drawn lot

`perm` lists candidate ids in tiebreak priority order, highest first, and `summaryData.candidates[].tieBreakOrder` is the same information spread across candidates. Despite BV labelling rung 3 `"random"`, it is a **seeded** shuffle — `seed = (rawVoteCount + hash(raceId)) >>> 0` — so the export records the complete order and a re-tally reproduces it. Replay it with [`bv_replay_tiebreak.py`](../../../STARVote_LH_tabulation_engine/tools_adam/bv_replay_tiebreak.py).

The full mapping into a YAML `lot_numbers:` line is its own page: [Tie-Breaking in BetterVoting JSON](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking_JSON.md), with the ladder itself in [STAR Tie-Breaking — The Full Chain](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md).

---

## The other direction — what a mint can populate

Sending a case *to* BetterVoting goes through [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py), which **clones a template election and overwrites part of it**. Only three groups of fields are ours:

| Group | Fields | Set by |
|---|---|---|
| **We set** | `title`, `description`; per race `title`, `voting_method`, `num_winners`, `max_rankings`, `enable_write_in`, `candidates[]` | The spec in [`bv_election_specs.py`](../../../STARVote_LH_tabulation_engine/tools_adam/bv_election_specs.py) |
| **Inherited from the template** | the whole `settings` block — `voter_access`, `voter_authentication`, `ballot_updates`, `public_results`, `random_candidate_order`, `require_instruction_confirmation`, `time_zone`, `term_type`, `contact_email`, `draggable_ballot`, `start_time`, `end_time` | Whichever election `BV_TEMPLATE_ID` points at (default `pet`) |
| **Server-assigned** | `election_id`, `create_date`, `update_date`, `head`, `state`, `claim_key_hash`, `ballot_source`, and every `Results` field | BetterVoting |

Three consequences worth knowing before minting:

1. **`settings` is not spec-controllable.** To change voter access or the candidate-order flag, point `BV_TEMPLATE_ID` at an election that already has the setting you want — there is no per-spec override.
2. **`admin_ids` is accepted and ignored.** API-minted elections are public, listable and exportable, but never UI-administrable. Setting it was tested; it does nothing.
3. **`title` and `description` are permanent.** No API path edits them. This is why the URL in a description backlink gets `curl`-checked for a 200 *before* the mint.

Ballots are cast separately (one POST per ballot), which populates `Ballots[].votes[].scores[]`. `Results` is never sent — BV computes it, and that is exactly what makes it a genuine cross-check of the LH count rather than an echo of it.

The end-to-end workflow lives in the **`bettervoting` skill** and the [tool guide](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.md).

---

## Known defects, and the open issue

Adam filed **[#1420 — "Download JSON export leaks the tabulator's internal object shape"](https://github.com/Equal-Vote/bettervoting/issues/1420)** (open since 2026-07-05), naming four defects, all of which the corpus above confirms:

1. Every candidate's O(n²) `votesPreferredOver` / `winsAgainst` maps, keyed by uuid, **self-pairs included**, duplicated across `elected` / `tied` / `other` / `summaryData` / `roundResults`.
2. `Results` in camelCase while `Election` and `Ballots` are snake_case.
3. Inconsistent timestamps — ISO-8601 `create_date` beside epoch-ms-string `update_date`.
4. No `format_version`, so a consumer cannot tell which era of export it has.

**[PR #1419](https://github.com/Equal-Vote/bettervoting/pull/1419)** — "Clean up the ballot-data export (JSON v2 + CSV Raw/Official)" — implemented a fix in `packages/shared/src/utils/exportFormat.ts`: candidates listed once, a deduped `pairwise` matrix keyed by name, `{id,name}` refs, snake_case throughout, ISO timestamps, `format_version: 2`, `score: null` preserved, and the CSV split into Official Count / Raw Audit. It measured 69–74% of legacy size on real exports from this repo.

**The PR was split, not rejected.** A maintainer extracted its **CSV bug fixes** into [PR #1428](https://github.com/Equal-Vote/bettervoting/pull/1428) — on a branch named `masiarek/csv-escaping-fix`, with the commit keeping Adam's authorship — and merged that on 2026-07-16. The **format redesign** was deferred with "the rest needs some contemplation", and #1419 was closed on 2026-07-15. So the export shipping today has correct CSV escaping and download behaviour, but the JSON is still v1 — which is what this page documents, and why #1420 stays open.

The contribution workflow and what was learned from it: [contributing to BetterVoting](tabulation_engine/contributing_to_bettervoting.md).

Related open tickets: [#1160](https://github.com/Equal-Vote/bettervoting/issues/1160) (dual raw/processed export), [#1432](https://github.com/Equal-Vote/bettervoting/issues/1432) (surface tie-break explanations).

---

## What this repo reads out of an export

| Consumer | Reads |
|---|---|
| [`01_convert_json_yaml.py`](../../../YAML_library/1_positive/01_convert_json_yaml.py) | `Election.races[]` → one YAML per race; `Ballots` → the score block (`null` → `-`); `perm` or `tieBreakOrder` → `lot_numbers:`; `elected` → the answer key |
| [`bv_replay_tiebreak.py`](../../../STARVote_LH_tabulation_engine/tools_adam/bv_replay_tiebreak.py) | Re-derives the seeded shuffle and checks it against `perm` |
| [`build_multirace_index.py`](../../../STARVote_LH_tabulation_engine/tools_adam/scripts/build_multirace_index.py) | `Election.races[]` + `Ballots` + `Results` — the source of truth for the multirace index |
| Case pages | `elected` and `tieBreakType`, quoted as BV's independent verdict beside the LH count |

Worked examples to open alongside this page: [`bv2105r2_w3vvff_ice_cream_recheck_bv_export.json`](../../../02_STAR_Bloc/02_Examples/cases/bv2105r2_w3vvff_ice_cream_recheck_bv_export.json) (Bloc STAR with `null` scores) and [`bv2261_y2fbpc_tiebreak_recorded_bv_export.json`](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/bv2261_y2fbpc_tiebreak_recorded_bv_export.json) (a recorded tiebreak order).

---

## See also

- [How to read a BetterVoting results page](reading_a_bv_results_page.md) — the same data as the visual report
- [BV database schema](database_schema/README.md) — where `Election` and `Ballots` are stored
- [BetterVoting and the LH engine — one election, two reports](../bettervoting_and_the_engine.md)
- [BV API election creation notes](bv_api_election_creation_notes.md) — what the API can and cannot do
- [Tie-Breaking in BetterVoting JSON](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking_JSON.md) — `perm` → `lot_numbers:` in full
