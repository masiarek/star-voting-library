# `ballotDB` — Ballots

Stores each cast ballot: one row per ballot version, holding the voter's scores/ranks for every
race on the ballot. This is the table the tabulation engine reads (via `BallotModel`) to build the
Cast Vote Record. Versioned with the `create_date` / `update_date` / `head` pattern (see
[README](./README.md)).

- **Domain type:** `Ballot` (`packages/shared/src/domain_model/Ballot.ts`)
- **Primary key:** `(ballot_id, update_date)`
- **Index:** unique `ballotDB_unique_head` on `(ballot_id, election_id)` where `head = true`

## Columns

| Column | Type | Notes |
|---|---|---|
| `ballot_id` | varchar | Logical ballot id (part of PK). |
| `election_id` | varchar | Election this ballot belongs to. |
| `user_id` | varchar | **LEGACY** — never written or read by current code; use the roll's `voter_id`. |
| `status` | varchar | Ballot status (e.g. `saved`, `submitted`). |
| `date_submitted` | varchar | Submission time (unix ms as string / `Date.now()`). |
| `ip_hash` | varchar | **LEGACY** — never written or read now; IP dedup lives on `electionRollDB.ip_hash`. |
| `votes` | json (**not null**) | `Vote[]` — one per race. See below. |
| `history` | json | `BallotAction[]` — `{ action_type, actor, timestamp }`. |
| `precinct` | varchar | Voter's precinct. |
| `create_date` | varchar (**not null**) | First-created timestamp. |
| `update_date` | varchar (**not null**) | This version's timestamp (part of PK). |
| `head` | boolean (**not null**) | `true` = current version. |

**History:** `ip_address` (varchar) existed in the initial schema and was dropped in 2024-01-27 in
favor of `ip_hash`.

## Nested JSON: `votes` → `Vote[]`

One entry per race the voter voted in.

| Field | Type | Notes |
|---|---|---|
| `race_id` | string | Must match a race on the election. |
| `scores` | `Score[]` | One per candidate. |
| `overvote_rank?` | number | Rank at which the ballot overvoted (ranked methods). |
| `has_duplicate_rank?` | boolean | Voter repeated a rank. |

### `Score`
| Field | Type | Notes |
|---|---|---|
| `candidate_id` | string | Candidate id, or empty for a write-in. |
| `score` | number \| null | 0–5 integer; `null` = candidate not scored. |
| `write_in_name?` | string | Present for write-in scores. |

**Per-method score bounds (validated on submit in `ballotValidation`):**
STAR / STAR_PR → 0–5; Approval / Plurality → 0–1; IRV / STV / RankedRobin → 0..`max_rankings`.
Max 10 write-ins per race; write-in name ≤ 100 chars and only if the race enables write-ins.

> `OrderedVote` (`number[]`) is an alternate compact form used in **bulk uploads**, where the
> race/candidate order is mapped separately and a trailing number encodes `overvote_rank`.
