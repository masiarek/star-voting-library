# `emailEventsDB` — Email Events

An append-only log of email delivery/engagement events (from the SendGrid webhook), used to show
per-voter email status on the roll and to drive reminder logic. Unlike the other three tables this
is **not** head-versioned — it's a plain event log.

- **Domain type:** `EmailEvent` (`packages/shared/src/domain_model/EmailEvent.ts`)
- **Created by migration:** `2026_03_19_email_events`
- **Primary key:** `id` (`serial`)
- **Indexes:**
  - `idx_email_events_election_voter` on `(election_id, voter_id)`
  - `idx_email_events_message_id` on `(message_id)`

## Columns

| Column | Type | Notes |
|---|---|---|
| `id` | serial | Auto-increment primary key. |
| `message_id` | varchar (**not null**) | Provider message id (ties events to a sent email). |
| `election_id` | varchar (**not null**) | Election the email relates to. |
| `voter_id` | varchar (**not null**) | Voter the email was sent to. |
| `event_type` | varchar (**not null**) | Event kind (e.g. delivered, open, click, bounce, spamreport). |
| `event_timestamp` | timestamptz (**not null**) | When the event occurred. |
| `details` | json | Provider-specific payload (`Record<string, unknown>`). |

## How it's used

The SendGrid webhook controller writes rows here as email events arrive. When the roll is fetched,
`ElectionRollResponse.email_events` joins this table on `(election_id, voter_id)` so admins can see
each voter's invite/reminder delivery and engagement status. The `message_id` index supports
looking events up by the specific email that generated them.
