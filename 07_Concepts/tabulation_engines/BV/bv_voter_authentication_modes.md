# BetterVoting's six voter-authentication modes — and why there is no "demo election" flag

**Level: reference · deep dive**

**One line:** BetterVoting has no field marking an election as a demo — "demo / unlimited voting" is *derived* from three settings that together resolve to one of six canonical modes, and knowing which mode an election is in decides what its results can honestly claim.

A common question when reading a downloaded `_bv_export.json`: *which key says this was a demo?* None of them. This page explains what to read instead, and why the distinction matters beyond bookkeeping.

For the raw field definitions see [BV's election table](database_schema/electionDB.md); for every key in an export, [the JSON export format](bv_json_export_format.md). This page is about what those fields *mean together*.

---

## Terminology — why "demo election" isn't quite right

**Manage Voters asks two independent questions**, and "demo election" collapses them into one. That collapse is the whole inaccuracy:

> **Would you like your election to be restricted to a pre-defined voter list?** &nbsp; ○ Yes &nbsp; ● No
>
> **Who can vote?**
> Limit to one Vote per… &nbsp;○ device &nbsp;○ user (login required) &nbsp;○ WiFi/cellular network &nbsp;● no limit

The first sets **`voter_access`** — is there an electorate at all? The second sets **`voter_authentication`** — how hard is it to vote twice? They are orthogonal, and *both* answers are needed to name what you are looking at. The screen above is **unrestricted + no limit**, i.e. `open_open`.

So the accurate description of that election is a two-part phrase — *"unrestricted, with no vote limit"* — and `open_open` is simply its compact name. There is no single word on the screen for it, which is exactly why one gets improvised.

**What makes "demo election" inaccurate is that it names a *purpose* while the screen sets a *mechanism*.** Nothing here says "demo". The two come apart in both directions:

- A **demo can be restricted** — a classroom exercise with a real emailed roll is still a demo.
- **No limit can be a mistake** — a real election configured carelessly is `open_open` and nobody meant it as a demonstration.

Same shape as the [RCV / IRV distinction](../../tips/TIPS_terminology.md) this repo keeps: one word names what you're doing, the other names the mechanism you're doing it with, and collapsing them costs you an argument later.

### What BetterVoting itself calls it

Three different things, and the admin-facing one is not a noun phrase at all. The form (`ElectionAuthForm.tsx`) asks the question as a **sentence**, with the modes as its endings — each carrying a tooltip with a fuller title and description:

| Surface | What it says |
|---|---|
| Source / mode name | **`open_open`** |
| The option an admin clicks | **"no limit"** — completing *"Limit to one vote per…"* |
| Its tooltip title | **"No Voting Limit"** |
| Its tooltip description | *"Allows unlimited votes per device. Great for demos or where all your voters are sharing the same device."* |

**So "demo election" comes from BetterVoting's own vocabulary** — the word "demos" is in the tooltip a user reads while choosing the setting. It is a description of what the mode is *good for*, though, never its name.

> **A dead key, worth not citing.** `en.yaml` also holds `demo_title: "Allows multiple votes per device"` and `demo_description: "Great for demonstrations…"`. Neither is referenced by any component — apparently leftovers from an earlier wizard. They read like evidence that BetterVoting calls this a "demo election"; they are not, because nobody ever sees them.

### The four options, mapped

| Admin picks | Mode |
|---|---|
| one vote per **device** | `open_unique_cookie` |
| one vote per **WiFi/cellular network** | `open_unique_ip_address` |
| one vote per **user (login required)** | `open_unique_keycloak` |
| **no limit** | `open_open` |

Reading them as a sentence makes the family obvious in a way the mode names don't: they are four answers to *"one vote per what?"*, and `open_open` is the answer "per nothing."

### House usage

- **Technical writing — exports, code, case files, anything precise → `open_open`.** It is the mode's actual name, it encodes *both* axes, and it cannot be misread.
- **Prose that needs to be plain → "unrestricted, no vote limit."** Two facts, because the screen sets two. *"Open"* alone is ambiguous: three of the four unrestricted settings still limit voting.
- **Walking someone through the UI → "no limit"**, quoting the question with it: *"under **Who can vote?**, choose **no limit**."* An instruction naming anything else sends the reader hunting for a control that isn't there.
- **"Demo election" stays for *intent*** — it is the word BetterVoting's own tooltip uses, and it is the honest reason we run most of ours. But it is a claim about *why*, so pair it with the mode on first mention: *"a demo election (unrestricted, no vote limit — `open_open`)"*. Never let it stand as the technical description.
- **Don't write "No Voting Limit" as though it were the control.** It is the tooltip's title, not the option's label.

### One trap: "public" is a different axis

BetterVoting's wizard also offers **"Public election"**, described as *"one person, one vote… open to anyone via the Browse Polls page."* That is about **listing and discoverability**, and its description asserts the *opposite* of unlimited voting. "Public", "open", and "no voting limit" are three different properties, and only the last is what "demo" informally means. The `is_public` field is the one that tracks listing.

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
