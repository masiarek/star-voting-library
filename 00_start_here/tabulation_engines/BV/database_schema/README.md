# BetterVoting (BV) Database Schema

Reverse-engineered from the source of [Equal-Vote/bettervoting](https://github.com/Equal-Vote/bettervoting)
(local clone: `/Volumes/T7/Voting/BetterVoting/BV/bettervoting`). This documents the **production
PostgreSQL schema** — the tables that store elections, ballots, voter rolls, and email events.

The relational shape is defined by **Kysely migrations** in
`packages/backend/src/Migrations/`; the JSON columns are typed by the shared domain model in
`packages/shared/src/domain_model/`. The `Database` interface
(`packages/backend/src/Models/Database.ts`) ties table names to those domain types:

```ts
export interface Database {
    electionDB:     Election,
    electionRollDB: ElectionRoll,
    ballotDB:       Ballot,
    emailEventsDB:  EmailEvent
}
```

## Tables

| Table | Purpose | Per-table doc |
|---|---|---|
| `electionDB` | Election config: races, candidates, settings, state, ownership | [electionDB.md](./electionDB.md) |
| `ballotDB` | Cast ballots (votes per race) | [ballotDB.md](./ballotDB.md) |
| `electionRollDB` | Voter roll: who may vote, auth, submission status | [electionRollDB.md](./electionRollDB.md) |
| `emailEventsDB` | SendGrid email delivery/engagement events | [emailEventsDB.md](./emailEventsDB.md) |

## The load-bearing design idea: append-only "head" versioning

`electionDB`, `ballotDB`, and `electionRollDB` are **versioned, not updated in place**. Every row
carries three bookkeeping columns:

- `create_date` — when the logical object was first created
- `update_date` — when *this row* (this version) was written
- `head: boolean` — `true` on the single current version, `false` on superseded ones

Each "edit" **inserts a new row** with a fresh `update_date` and flips the old head to `false`,
so the table keeps a full history of every election/ballot/roll. This is why the **primary keys
are composite** and include `update_date`, and why reads filter on `head = true`.

A **partial unique index** (`where head = true`) enforces that exactly one version of each logical
object is the head at any moment (migration `2026_04_27_unique_head`):

| Table | Primary key | Unique-head index (`where head = true`) |
|---|---|---|
| `electionDB` | `(election_id, update_date)` | unique `(election_id)` |
| `ballotDB` | `(ballot_id, update_date)` | unique `(ballot_id, election_id)` |
| `electionRollDB` | `(election_id, voter_id, update_date)` | unique `(election_id, voter_id)` |

`emailEventsDB` is the exception — it's a plain append-only event log with a `serial` primary key
and no head-versioning.

## Relationships (logical — enforced in code, not by FK constraints)

There are no declared foreign keys; the tables are joined on shared id columns in the models:

```
electionDB (election_id)
   ├──< electionRollDB (election_id)          one election → many voter-roll entries
   │        └── ballot_id ──> ballotDB.ballot_id   roll points at the voter's head ballot
   ├──< ballotDB (election_id)                one election → many ballots
   └──< emailEventsDB (election_id, voter_id) email events reference an election + voter
```

## Migration history

| Migration | Change |
|---|---|
| `2023_07_03_Initial` | Creates `electionDB`, `electionRollDB`, `ballotDB` |
| `2024_01_27_Create_Date` | Adds `claim_key_hash`, `is_public`, `create_date` to elections; swaps `ip_address` → `ip_hash` on rolls & ballots |
| `2024_01_29_pkeys_and_heads` | Introduces the `create_date`/`update_date`/`head` versioning + composite PKs; adds `electionDB_head` index |
| `2025_01_29_admin_upload` | Adds `ballot_source` + `public_archive_id`; drops obsolete `support_email` (→ `settings.contact_email`) |
| `2026_03_19_email_events` | Creates `emailEventsDB` + its indexes |
| `2026_04_27_unique_head` | Adds the partial unique-head indexes on the three versioned tables |

Run migrations with `npm run migrate:latest -w @equal-vote/star-vote-backend` (up/down one step
via `migrate:up` / `migrate:down`).

## Notes

- **Engine / access layer:** PostgreSQL via Kysely (type-safe query builder). `DATABASE_URL` sets the connection; `DEV_DATABASE=FALSE` disables SSL for local Postgres.
- **JSON columns** store whole domain objects (e.g. `races: Race[]`, `settings: ElectionSettings`, `votes: Vote[]`), so the "schema" is half relational, half TypeScript interface — the per-table docs describe both.
- **`election_id` is always lowercase** (future-proofing against custom slugs colliding with routes).
- **Legacy columns** that current code neither reads nor writes are called out per table (e.g. `ballotDB.user_id`, `ballotDB.ip_hash`, `electionRollDB.address`, `electionRollDB.registration`).
