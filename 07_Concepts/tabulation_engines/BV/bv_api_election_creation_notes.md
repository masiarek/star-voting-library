# Creating BetterVoting elections via the API — what works, what doesn't

Notes on [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py), the script that creates BV test elections (and casts their ballots) through the REST API instead of the builder UI. Written up after a round of testing on 2026-07-05, so the limitation below isn't re-discovered later.

## How the script authenticates

It doesn't — and **since 2026-08-15 it deliberately doesn't**, because authenticating was the thing that broke `/admin`.

`POST /API/Elections` carries no auth middleware at all ([`elections.routes.ts`](https://github.com/Equal-Vote/bettervoting/blob/main/packages/backend/src/Routes/elections.routes.ts)) and takes `owner_id` verbatim from the request body, so creation needs no credential of any kind. The script used to *also* set the election's **`auth_key`** (a PEM RS256 public key) and sign a matching `custom_id_token`, on the belief that the backend required it. It does not: `auth_key` is optional in `electionValidation`, and setting it is what cost us UI admin access — see [the `/admin` gate](#the-admin-gate-and-how-it-was-closed) below. It is now **omitted by default**; `BV_AUTH_KEY=1` restores the old behaviour for a run that needs owner-scoped reads.

The election's `owner_id` is whatever the script's `BV_USER_ID` says. **Set it to your real BetterVoting account id** so the elections it creates show up in your `/manage` list — the default is now Adam's account (`ea09e7c7-b00d-427a-bef8-32ade437d49d`, "Admin1"). That id is not a secret; it is the `owner_id` in every frozen `_bv_export.json` in this repo.

## What works

- **Creation + ballot casting** via `POST /API/Elections` and `POST /API/Election/{id}/vote`.
- **Public visibility**: the election is live at `bettervoting.com/<id>`, votes tabulate, and the results are exportable (Election + Ballots + Results) from the UI.
- **`/manage` listing**: with `owner_id` = your account, the election appears in *My Elections & Polls* and is searchable by title. (Before this fix, script elections were owned by a throwaway identity and were invisible there.)
- **Full-export download WITHOUT the UI (found 2026-07-23).** The results page's "Download → Download JSON" file is reconstructible from three **anonymous** GETs — no login, no admin role:

  | export section | endpoint | note |
  |---|---|---|
  | `Election` | `GET /API/Election/{id}` → `.election` | config only on its own |
  | `Ballots` | `GET /API/Election/{id}/anonymizedBallots` → `.ballots` | public; the admin `GET …/ballots` returns **401** anonymously |
  | `Results` | `GET /API/ElectionResult/{id}` → `.results` | tabulated on demand — the election does **not** need to be closed |

  [`tools_adam/fetch_bv_export.py`](../../../STARVote_LH_tabulation_engine/tools_adam/fetch_bv_export.py) assembles these into the house frozen-export shape (`{"Election":…, "Ballots":…, "Results":…}`). Verified against the UI-downloaded `vqyqkr` export: Election and Results **byte-identical**, Ballots identical up to order (ballot order always varied between UI downloads too). `create_bv_test_election.py` now calls it automatically after casting, so a freshly minted election lands in `_demo_dropbox/` with its full export already frozen. Crash-case elections whose ElectionResult 500s (the STV sole-survivor pair) freeze with `--without-results` (`Results: []` + a self-documenting `_note`).

## Election descriptions render markdown — and only `[text](url)` links

The `description` sent at mint is **not plain text**. BetterVoting renders election and race descriptions through `formatMarkdown()` (`packages/shared/src/utils/formatMarkdown.ts`), which recognises exactly two things — `**bold**` and `[text](url)` — and sanitises everything else. Its link rule is a single regex, `rLink = /\[([^\]]*?)\]\(([^)]*?)\)/`. There is **no bare-URL autolinker**.

That is what makes the house backlink form load-bearing. `[Full lesson & tabulation](https://…)` becomes a real `<a target="_blank">`; the retired bare form, `Full lesson & tabulation: https://…`, ships as grey text a voter has to select and copy. 65 of the repo's frozen exports are permanently in that state, because a description cannot be edited after the create (see the `/admin` gate below).

BetterVoting says so on screen exactly once. The **Election Description** field on Admin Home carries the helper text `Supports **bold** and [link text](url) formatting` — and it is the last one standing: the hint was added under both Description fields, and the later `RaceForm` rewrite dropped it, so a **race** description takes the same markdown with nothing on the page saying so. Checked against the source 2026-08-08 — the string survives in `ElectionDetailsForm.tsx` and `SendEmailDialog.tsx` only.

## Ballot-data export format — the `precinct` column

BetterVoting's **Ballot Data** export (the per-ballot CSV, `Ballot Data - <title>-<id>.csv`) has this shape: `ballot_id, precinct, <Candidate1>, <Candidate2>, …`. Two things worth knowing:

- **There is always a `precinct` column** (column B), part of BV's precinct-tagging / `precinctFilteredElection` feature. It is **blank** unless the election actually defines precincts — API-created elections don't, so every row's precinct is empty. It's harmless: the JSON→YAML importer ignores it (only the candidate columns + `ballot_id` matter).
- **Ranked methods put a rank in each candidate cell** (`1` = top … `0` = unranked), and **equal ranks are preserved** — a tie like `Ava=Bianca=Cedric` exports as `1,1,1,…`. Confirmed on **BV2140** (`48hjkv`): the exported ballots round-trip the tied ranks exactly, and BV's `RankedRobin.ts` tabulated them to the same winner/records as the LH engine. So BV both **accepts equal-rank ballots on creation and counts ties the same way** LH does.

## Voter identity when casting, and ballot anonymity in the export

**How a vote is attributed to a "voter": the `temp_id` cookie.** `POST /API/Election/{id}/vote` carries a **`temp_id`** cookie, and BV keys the ballot to that value. It's how an open/anonymous poll enforces *one ballot per voter* and lets a voter **change** their vote (re-submitting with the same `temp_id` **updates** the existing ballot rather than adding a new one). In the browser this cookie is set for you; our scripts set it explicitly, so **each distinct `temp_id` = a distinct voter**. To cast N independent ballots you use N distinct `temp_id`s (`create_bv_test_election.py` uses `f"{USER_ID}_voter{idx}"`); reuse one and BV overwrites/ rejects it as the same voter re-voting. Caveat: `temp_id` is an **arbitrary string the caller chooses** — no real identity, freely settable via the API. That's why these open API polls are fine for **demos but not secure** for a real election (a real one uses authenticated voter credentials, not a self-set cookie).

**The `temp_id` does NOT appear in the export — ballots are anonymous.** A ballot record in the exported JSON looks like:

```json
{ "ballot_id": "b-vmm2y3c2", "election_id": "kjhpg6", "precinct": null,
  "votes": [ { "race_id": "0", "scores": [ {"candidate_id": "c-494", "score": 3}, … ] } ] }
```

| Field | In the export? | What it is |
|---|---|---|
| `ballot_id` | ✅ | a **random per-ballot** handle BV assigns — **not** the voter/`temp_id`, not a person |
| `election_id`, `precinct`, `votes.scores` | ✅ | which election, precinct label (usually `null`), and the 0–5 scores (+ any `write_in_name`) |
| **`temp_id`** / voter_id / user_id / IP / email | ❌ **absent** | — |

So the `temp_id` is **server-side only** (dedup / vote-changing while voting); it is **not written into the exported ballot**. The tally export is a set of **anonymous ballots** — random `ballot_id` + scores, with nothing tying a ballot back to a voter. This is the good half of the secret-ballot property, and it complements the paper-side discussion in the [paper-ballot demo](../../../01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md) (serials / E2E-V): distinguishing ballots *while voting* without letting the tally re-identify a voter. (One residual: `ballot_id` is a stable handle for *that ballot*, so an external "voter X → ballot_id Y" record could re-link them — but the export itself provides no such map.)

## The /admin gate and how it was closed

**Until 2026-08-15, you could not administer an API-created election from the UI**, even though you owned it. `/<id>/admin` answered *"Only the users with admin access on the election can view this page,"* and — the symptom that finally exposed the cause — the whole **admin sidebar vanished** from `/<id>` and `/<id>/results` as well.

### What is behind that gate — the admin URL map

The seven entries in the admin sidebar ([`Sidebar.tsx`](https://github.com/Equal-Vote/bettervoting/blob/main/packages/frontend/src/components/Election/Sidebar.tsx)), and which of them the gate actually costs you:

| Sidebar entry | URL | Behind the gate? |
|---|---|---|
| Admin Home — title, description, start/end times, **Duplicate**, **Archive** | `/<id>/admin` | 🔒 |
| Build Ballot | `/<id>/admin/build_ballot` | 🔒 |
| Manage Voters — [the two questions that set the mode](bv_voter_authentication_modes.md) | `/<id>/admin/voters` | 🔒 |
| Settings | `/<id>/admin/settings` | 🔒 |
| Preview Ballot *(draft)* / Live Ballot | `/<id>` | **public** |
| Preview Results *(draft)* / Live Results | `/<id>/results` | **public** |
| Publish & Share | `/<id>/admin/publish` | 🔒 |

Two things the table makes plain. **The two entries this repo actually uses are the two that are not admin pages** — `/<id>` to vote and `/<id>/results` to read the count are public URLs the sidebar merely links to, which is why the gate never blocked the mint → export → freeze pipeline. And **the ballot and results labels flip with `election.state`**: a draft says *Preview*, an open election says *Live*, same two URLs either way. (An eighth entry, *Edit Election Roles* → `/<id>/admin/roles`, appears only when the `ELECTION_ROLES` feature flag is on.)

Note that the sidebar is *not* gated per-page. `Sidebar.tsx` renders the whole panel only when `voterAuth?.roles?.length > 0`, so an election you hold no role on shows **no menu at all** — including on the two pages you are perfectly entitled to see. That is why the bug reads as "the menu on the left is sometimes missing" rather than as an access-denied message.

### The cause: our own `auth_key`, not BV's authorization

The original write-up of this section concluded that BV's `/admin` "reads neither `owner_id` nor `admin_ids`" and must use a server-side role binding written only by the Keycloak create flow. **That was wrong**, and the experiment behind it had two independent flaws. The corrected account:

Roles are computed in `electionPostAuthMiddleware` ([`elections.controllers.ts`](https://github.com/Equal-Vote/bettervoting/blob/main/packages/backend/src/Controllers/Election/elections.controllers.ts)) and they *do* read the election record:

```ts
if (req.user && req.election){
  if((req.election.owner_id == req.user.sub && req.user.typ !== 'TEMP_ID') || tempUserAuth){
    req.user_auth.roles.push(roles.owner)
  }
  if (req.election.admin_ids && req.election.admin_ids.includes(req.user.email)){
    req.user_auth.roles.push(roles.admin)
  }
  …
}
```

Everything hangs on `req.user`. Immediately upstream of it sits `electionSpecificAuth`, which runs on every **election-scoped** route:

```ts
const electionKey = req.election.auth_key;
if (electionKey == null || electionKey == "") return next();   // ← the normal path
var user = accountService.extractUserFromRequest(req, electionKey);
req.user = user;                                                // ← REPLACES your identity
```

With an `auth_key` set, `req.user` is no longer your Keycloak identity. It becomes whatever verifies against *that election's* key — read from the `custom_id_token` cookie, which your browser has never had. `req.user` comes back `null`, so **neither** the `owner_id` test nor the `admin_ids` test is even reached, `voterAuth.roles` is `[]`, and the sidebar renders nothing.

And `create_bv_test_election.py` set `auth_key` on every election it minted, from its first commit (2026-07-04) until this fix.

**The two flaws in the original experiment**, worth naming because both are easy to repeat:

1. **The confounder was never controlled.** The UI-created election and the API-created one differed in `auth_key`, not only in `admin_ids`. The conclusion "`admin_ids` is ignored" was drawn from the one variable that wasn't the cause.
2. **`admin_ids` was populated with the wrong field.** The test set `admin_ids: [my account **id**]`, but the check is `admin_ids.includes(req.user.email)`. Even with no `auth_key`, that election would have been denied the *admin* role — though it would have had the *owner* role anyway, and so a sidebar.

**Live confirmation** (2026-08-15, anonymous, no login needed): send a syntactically valid but unsigned `custom_id_token` cookie and see which elections try to verify it.

```bash
curl -s -o /dev/null -w "%{http_code}\n" --cookie "custom_id_token=$BOGUS" https://bettervoting.com/API/Election/pet
curl -s -o /dev/null -w "%{http_code}\n" --cookie "custom_id_token=$BOGUS" https://bettervoting.com/API/Election/8q3xcg
```

`pet` (UI-created, no `auth_key`) returns **200** — the middleware short-circuits and ignores the cookie. `8q3xcg` (BV2284, script-minted) returns **5xx** — it reaches `jwt.verify`, throws `Unauthorized`, and never gets to the role checks. Both return 200 with no cookie at all.

### The fix, and what it cannot repair

`auth_key` is **optional**: `POST /API/Elections` has no auth middleware, and `electionValidation` only checks the key's *shape* when one is present. So the script now omits it, and an API-created election is administrable from the account named in `owner_id`, sidebar and all. `BV_AUTH_KEY=1` restores the old behaviour for a run that needs owner-scoped reads — the only one left is the non-fatal `/ballots` count check, which otherwise degrades to *"HTTP 403 — skipped"*.

**Elections minted before 2026-08-15 cannot be repaired.** Clearing `auth_key` means `PATCH /API/Election/{id}`, which requires the `canEditElection` permission — which requires a role — which requires the `custom_id_token` we can no longer produce, since the keypair was minted per run and discarded. Even holding the key would not be enough: `editElection` refuses outright when `state !== 'draft'`, and these elections are open. They stay listable, votable, exportable, and permanently menu-less until someone with DB access clears the column.

**Consequences for the test-case workflow:**

- Nothing about the mint → export → freeze pipeline changes; it never used an admin page.
- New elections gain **Duplicate**, **Archive**, description edits, and **Publish & Share** — none of which the ~120 elections minted between 2026-07-04 and 2026-08-15 will ever have.
- If you do set `admin_ids`, populate it with an **email address**, not an account id.

**Orphans awaiting BV-admin DB cleanup** (created via the API, undeletable by us):

| bvid | why orphaned |
|---|---|
| `9tgj9d`, `xb8r6v` | early throwaways, labeled "ZZZ DELETE ME" |
| `bwbc6d` | Pet-poll test, created before the Test ID was wired into the title (un-numbered) |
| `mw9kpp` | Pet-poll test, superseded — its public title carried the old `trash delete test —` junk prefix (since removed) |
| `9hmbg8` | Scratch SNTV confirmation (Plurality, 2 winners → c, b) — junk title "wqefwefwe…"; proved BV multi-winner Plurality = SNTV, then discardable |
| `2jpcxd` (BV2255) | "One mark each: the traditional choose-one ballot, counted four ways" — **over-built, not wrong.** The three bullet ballots are correct in all four races (Plurality / STAR / IRV / RankedRobin, all → Ella), but the ask was for a plain single-race illustration of the *traditional voting style*, not a four-method line-up; the permanent title frames it as the latter. **Superseded by BV2256 `c8h3tb`** (one STAR race, same ballots). Lesson: when the ask is "an example OF a ballot style," one race is the deliverable — a method comparison is a different lesson, and titles can't be edited. |
| `6btm9k`, `g6x8b9`, `f2vtc9`, `xm93tw` | ballot_style_lab 07a/07b/08/09 minted with **`num_winners: 1`** by mistake (a driver read the raw `num_winners:` key, but `load_election` normalizes it to `seats:`) — so titled "BV2240–2243 — …, 3/3/2/4 seats" but actually single-winner. Ballots + method are correct; only the seat count is wrong. **Superseded by the correct multi-winner mints BV2244 `9dx494` / BV2245 `pmrq4q` / BV2246 `qdh9qp` / BV2247 `v9rhhr`.** (Lesson: when building a spec from a yaml via the engine, read `el["seats"]`, not `el["num_winners"]`.) |

**Lesson (why the title guard exists):** because API elections are **public and permanent**, the title must be right on the *first* create — there is no rename or delete. `create_bv_test_election.py` now (a) prepends only the `BV<n>` Test ID (no "trash/delete/test" junk), and (b) runs a pre-check that **blocks junk/placeholder titles** and reminds you the title is permanent + public. Set `BV_ALLOW_JUNK_TITLE=1` only to override deliberately.

## The residual upstream defect — draft, not filed

Our own misuse explains our own elections, but a real BV defect sits underneath it, and it is a different one from the issue this page used to draft. Not filed yet; check [upstream bug reports](../../about_this_repo/upstream_bug_reports.md) before assuming otherwise.

**Title:** An election with a custom `auth_key` is permanently un-administrable by its owner

`electionSpecificAuth` overwrites `req.user` with the custom-token identity on every election-scoped route. When the request has no `custom_id_token` — an ordinary Keycloak-logged-in owner opening the page in a browser — `req.user` becomes `null` rather than falling back to the account identity, so `electionPostAuthMiddleware` grants no roles and `Sidebar.tsx` renders nothing. The owner sees the election in `/manage` (that route is not election-scoped) with no way to administer it.

It cannot be undone from either side: clearing `auth_key` needs `canEditElection`, which needs a role, and `editElection` additionally refuses any election whose state is not `draft`. An integration that sets `auth_key` at create time therefore locks its own owner out for the life of the election.

**Suggested fix:** keep the custom-token identity for *voter* authorization, but compute admin roles against the account identity — e.g. resolve the Keycloak user separately in `electionPostAuthMiddleware` instead of reading the possibly-overwritten `req.user`. A blanket fallback in `electionSpecificAuth` would be simpler but changes voter-identity semantics for custom-auth elections, so it is the worse of the two.

**Repro:** `POST /API/Elections` with `owner_id` = your account id and `auth_key` = any PEM RS256 public key; log in as that account and open `/<id>` — no sidebar, and `/<id>/admin` denies you.

## Related

- [BV — BetterVoting (the live web app)](README.md)
- The script + how to run it: [`create_bv_test_election.py` — tool guide](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.md)
- The BV-backed case workflow is documented in the repo's `CLAUDE.md` (steps 3–4).

