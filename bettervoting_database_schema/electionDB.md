# `electionDB` — Elections

Stores each election's full configuration: its races, candidates, settings, lifecycle state, and
ownership. Versioned with the `create_date` / `update_date` / `head` pattern (see
[README](./README.md)).

- **Domain type:** `Election` (`packages/shared/src/domain_model/Election.ts`)
- **Primary key:** `(election_id, update_date)`
- **Indexes:** `electionDB_head` on `head`; unique `electionDB_unique_head` on `(election_id)` where `head = true`

## Columns

| Column | Type | Notes |
|---|---|---|
| `election_id` | varchar | Logical id (part of PK). Always lowercase. |
| `title` | varchar | One-line title (3–256 chars unless draft). |
| `description` | text | Markup description. |
| `frontend_url` | varchar | Base URL for the frontend. |
| `start_time` | varchar | Election start (ISO string). |
| `end_time` | varchar | Election end (ISO string). |
| `owner_id` | varchar | `user_id` of the owner. |
| `audit_ids` | json | `Uid[]` — accounts with audit access. |
| `admin_ids` | json | `Uid[]` — accounts with admin access. |
| `credential_ids` | json | `Uid[]` — accounts with credentialling access. |
| `state` | varchar | `draft \| finalized \| open \| closed \| archived`. |
| `races` | json (**not null**) | `Race[]` — see nested types below. |
| `settings` | json | `ElectionSettings` — see below. |
| `auth_key` | varchar | RS256 public key (PEM) for API-created elections' custom token auth. |
| `claim_key_hash` | varchar | Hash of the claim key (added 2024-01-27). |
| `is_public` | boolean | Whether the election is publicly listed. |
| `create_date` | varchar (**not null**) | First-created timestamp. |
| `update_date` | varchar (**not null**) | This version's timestamp (part of PK). |
| `head` | boolean (**not null**) | `true` = current version. |
| `ballot_source` | varchar (**not null**, default `live_election`) | `live_election` (voters) or `prior_election` (admin-uploaded). |
| `public_archive_id` | varchar | Maps a public-archive election to its real one (e.g. `Genola_11022021_CityCouncil`). |

**Dropped:** `support_email` (removed 2025-01-29; superseded by `settings.contact_email`).

## Nested JSON: `races` → `Race[]`

| Field | Type | Notes |
|---|---|---|
| `race_id` | string | Race mnemonic. |
| `title` | string | Display caption. |
| `description?` | string | Markup. |
| `voting_method` | `STAR \| STAR_PR \| Approval \| RankedRobin \| IRV \| Plurality \| STV` | Tabulation method. |
| `num_winners` | number | 1–100. |
| `candidates` | `Candidate[]` | See below. |
| `precincts?` | string[] | Restrict race to precincts; null = open to all. |
| `enable_write_in?` | boolean | Allow write-ins. |
| `write_in_candidates?` | `WriteInCandidate[]` | `{ candidate_name, aliases[], approved }`. |

### `Candidate`
`candidate_id`, `candidate_name` (3–256), and optional `full_name`, `bio`, `party`, `party_url`,
`candidate_url`, `photo_filename`.

## Nested JSON: `settings` → `ElectionSettings`

Selected fields (all optional unless noted):

| Field | Type | Notes |
|---|---|---|
| `voter_access` | `open \| closed \| registration` | Who may vote. |
| `voter_authentication` | object | `{ voter_id?, email?, phone?, address?, ip_address?, registration_data?, registration_api_endpoint? }`. |
| `invitation` | `email \| address` | Requires `voter_access = closed`. |
| `reminders` | boolean | Requires `voter_access = closed`. |
| `ballot_updates` | boolean | Voters may update ballots before close (email-list elections only). |
| `public_results` | boolean | Public may view results (gates the results endpoint). |
| `random_candidate_order` | boolean | Randomize ballot candidate order. |
| `require_instruction_confirmation` | boolean | Force instruction acknowledgement. |
| `break_ties_randomly` | boolean | Whether true ties break randomly. |
| `term_type` | `poll \| election` | Wording. |
| `max_rankings` | number | Rank cap for ranked methods. |
| `contact_email` | string | Public contact (replaced `support_email`). |
| `exhaust_on_N_repeated_skipped_marks` | number | Skipped-rank exhaustion threshold (IRV/STV). |
| `draggable_ballot` | boolean | Draggable IRV ballot UI. |
| `time_zone` | TimeZone | Display time zone. |

> `election_id` + `create_date`/`update_date`/`head` are omitted when constructing a `NewElection`;
> the model generates them inside the write transaction.
