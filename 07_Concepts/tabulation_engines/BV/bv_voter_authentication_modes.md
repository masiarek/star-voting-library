# BetterVoting's six voter-authentication modes — and why there is no "demo election" flag

**Level: reference · deep dive**

**One line:** BetterVoting has no field marking an election as a demo — "demo / unlimited voting" is *derived* from three settings that together resolve to one of six canonical modes, and knowing which mode an election is in decides what its results can honestly claim.

A common question when reading a downloaded `_bv_export.json`: *which key says this was a demo?* None of them. This page explains what to read instead, and why the distinction matters beyond bookkeeping.

For the raw field definitions see [BV's election table](database_schema/electionDB.md); for every key in an export, [the JSON export format](bv_json_export_format.md). This page is about what those fields *mean together*.

---

## There is no demo flag

BetterVoting's `Election` object carries `election_id`, `title`, `description`, `state`, `races`, `settings`, `owner_id`, `admin_ids`, `is_public`, `ballot_source`, `public_archive_id`, and the usual dates. Checked against the domain model and against the frozen exports in this repo, there is **no `is_demo`, no `is_test`, no `demo`** — and nothing else that flags an election as practice rather than real.

Two nearby fields are easy to mistake for one, and neither is:

- **`is_public`** — whether the election is listed publicly. A serious election can be public; a throwaway one can be unlisted.
- **`ballot_source`** — `live_election` or `prior_election`, i.e. whether the ballots were cast here or imported from a previous election. It describes *where the ballots came from*, not how carefully they were cast.

The property people mean by "demo" is **how hard it is to vote more than once**, and that lives in the settings.

---

## The three settings, and the six modes they form

Three settings interact: `voter_access`, `voter_authentication`, and `invitation`. They are not independent — only six combinations are legal, and BetterVoting names them:

| Mode | `voter_access` | Authentication | One person can vote… |
|---|---|---|---|
| `open_open` | `open` | none | **unlimited times** |
| `open_unique_cookie` | `open` | `voter_id` (browser cookie) | once per browser |
| `open_unique_keycloak` | `open` | `email` (account) | once per account |
| `open_unique_ip_address` | `open` | `ip_address` | once per IP address |
| `closed_admin_managed_ids` | `closed` | `voter_id`, from a roll | once, per admin-issued id |
| `closed_bv_managed_ids` | `closed` | `voter_id` + `invitation: email` | once, per emailed invitation |

**The derivation is a shared function, not something to hand-roll:** `getVoterAuthenticationMode(settings)` returns the mode for a settings block and throws if the combination is not one of the six. It is the declared single source of truth for the triple, so any tool asking "what kind of election is this?" should call it rather than pattern-match the raw fields.

### Reading it from an export

A real frozen export from this repo (`t4by6x`):

```text
voter_access          : open
voter_authentication  : {ip_address: false, voter_id: false, email: false}   ← all false
ballot_source         : live_election
state                 : open
```

All three authentication flags false, with `voter_access: open`, is **`open_open`** — no authentication of any kind. That is what "demo election" means on BetterVoting: not a flag, a mode.

---

## Only one of the six is genuinely unlimited

The four `open_*` modes are easy to lump together as "open voting." They are not the same, and reporting them alike overstates three of them and flatters the fourth:

- **`open_open`** places no barrier at all. One person can cast as many ballots as they like.
- **`open_unique_cookie`** is limited by a browser cookie — cleared, or a private window, and the limit is gone.
- **`open_unique_ip_address`** is limited per IP, which also *over*-restricts: a household or an office shares one.
- **`open_unique_keycloak`** requires an account, the strongest of the four and still self-serve.

Only the two `closed_*` modes involve an electorate someone defined in advance.

---

## Why the mode decides what a result can claim

This is the reason the distinction is worth a page rather than a footnote.

**Turnout is only meaningful in a closed election.** Turnout is votes cast over an eligible electorate. In the four `open_*` modes there is no roll and therefore no denominator — nothing to be a percentage *of*. The same applies to quorum, non-voter lists, and any "who hasn't voted yet" report.

**Delivery reporting needs `closed_bv_managed_ids` specifically.** Bounce and delivery events only exist where BetterVoting sent the invitations, which is the email-invitation mode alone. `closed_admin_managed_ids` has a roll but no emails, so it can report voted / not-voted and never delivered / bounced. See [the email-events table](database_schema/emailEventsDB.md).

**Tie-break reproducibility means less than it appears in an open election.** BetterVoting's random tie-break is a seeded shuffle whose seed is derived from the raw ballot count and the race id — deterministic, and reproducible by anyone with the export. But in `open_open` the ballot count is unbounded and inflatable by a single voter, so the seed is too.

That does not make the tie-break broken: anyone able to cast unlimited ballots can simply win outright, which makes the tie-break the least of the problem. It does mean **reproducible is not the same as trustworthy** — the same seed, printed on the same report, supports an integrity claim in a closed election and does not in an open one. A report that shows the seed without naming the mode invites the stronger reading.

---

## Practical notes

**When quoting a result, name the mode.** A margin from an `open_open` demo and a margin from an invitation-only election are not comparable numbers, and nothing in the export stops them being placed side by side.

**When converting an export to a case file**, record the resolved mode rather than leaving each consumer to re-derive it from three fields — the derivation is cheap but easy to get subtly wrong, and the raw fields do not read as a single fact.

**When designing a report**, treat the mode as the legend. Whether an artefact is *available at all* — not merely empty — depends on it, and an empty turnout figure reads as "nobody voted" rather than "this question does not apply here."

---

## Related

- [BV's election table](database_schema/electionDB.md) — the raw field definitions
- [The BetterVoting JSON export, field by field](bv_json_export_format.md) — every key in `Election` / `Ballots` / `Results`
- [BV's email-events table](database_schema/emailEventsDB.md) — what delivery reporting is built on
- [How to read a BetterVoting results page](reading_a_bv_results_page.md)
- [What API election creation can and cannot do](bv_api_election_creation_notes.md)

---

*Written against BetterVoting's source and the frozen exports in this repo. Intended to be portable: if it is useful upstream it should move to [docs.bettervoting.com](https://docs.bettervoting.com) with the repo-specific paragraphs above dropped.*
