# Creating BetterVoting elections via the API — what works, what doesn't

Notes on `STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py`, the script that creates BV test elections (and casts their ballots) through the REST API instead of the builder UI. Written up after a round of testing on 2026-07-05, so the limitation below isn't re-discovered later.

## How the script authenticates

The BV backend requires **asymmetric RS256** auth for API creation: the election carries a PEM **public** key in `auth_key`, and the request's `custom_id_token` is a JWT signed with the matching **private** key. The script mints a fresh keypair per run — self-consistent, so no real BV account credential is stored or used. (The old HS256 "secret == user id" recipe is stale.)

The election's `owner_id` is whatever the script's `BV_USER_ID` says. **Set it to your real BetterVoting account id** so the elections it creates show up in your `/manage` list — the default is now Adam's account (`ea09e7c7-b00d-427a-bef8-32ade437d49d`, "Admin1"). That id is not a secret; it is the `owner_id` in every frozen `_bv_export.json` in this repo.

## What works

- **Creation + ballot casting** via `POST /API/Elections` and `POST /API/Election/{id}/vote`.
- **Public visibility**: the election is live at `bettervoting.com/<id>`, votes tabulate, and the results are exportable (Election + Ballots + Results) from the UI.
- **`/manage` listing**: with `owner_id` = your account, the election appears in *My Elections & Polls* and is searchable by title. (Before this fix, script elections were owned by a throwaway identity and were invisible there.)

## Ballot-data export format — the `precinct` column

BetterVoting's **Ballot Data** export (the per-ballot CSV, `Ballot Data - <title>-<id>.csv`) has this shape: `ballot_id, precinct, <Candidate1>, <Candidate2>, …`. Two things worth knowing:

- **There is always a `precinct` column** (column B), part of BV's precinct-tagging / `precinctFilteredElection` feature. It is **blank** unless the election actually defines precincts — API-created elections don't, so every row's precinct is empty. It's harmless: the JSON→YAML importer ignores it (only the candidate columns + `ballot_id` matter).
- **Ranked methods put a rank in each candidate cell** (`1` = top … `0` = unranked), and **equal ranks are preserved** — a tie like `Ava=Bianca=Cedric` exports as `1,1,1,…`. Confirmed on **BV2140** (`48hjkv`): the exported ballots round-trip the tied ranks exactly, and BV's `RankedRobin.ts` tabulated them to the same winner/records as the LH engine. So BV both **accepts equal-rank ballots on creation and counts ties the same way** LH does.

## What does NOT work — the `/admin` gate (a real BV limitation)

**You cannot administer an API-created election from the UI**, even though you own it. Opening `/<id>/admin` returns *"Only the users with admin access on the election can view this page."*

This was tested directly, and the result is counter-intuitive — two elections with the **same `owner_id` (my account)**:

| Election | how created | `admin_ids` | `/admin` |
|---|---|---|---|
| `r4dqvd` (BV2105) | BV builder UI | `null` | ✅ full admin |
| `xb8r6v` (throwaway) | API script | `[my account]` | ❌ denied |

The election that **works** has `admin_ids: null`; the one that's **denied** explicitly lists my account in `admin_ids`. So BV's `/admin` authorization reads **neither `owner_id` nor `admin_ids`** from the election record — it uses a server-side role/permission binding (`voterAuth.roles` / `permissions`, empty on the API-created one) that only the **authenticated (Keycloak) create flow** writes. Setting `admin_ids` in the create payload persists in the record but is **ignored** for authorization.

**Consequences for the test-case workflow:**

- API-created elections are public, listable, and exportable — enough for the reproduce-and-freeze pipeline (create → export → reproduce in LH → freeze `_bv_export.json`).
- They are **not** UI-administrable from your real login: you cannot edit, close, **rename**, or **delete** them from the UI (no API endpoint either). Throwaways linger in `/manage` until a BV admin with DB access removes them.
- Don't bother setting `admin_ids` in the payload — proven no-op for authz.

**Orphans awaiting BV-admin DB cleanup** (created via the API, undeletable by us):

| bvid | why orphaned |
|---|---|
| `9tgj9d`, `xb8r6v` | early throwaways, labeled "ZZZ DELETE ME" |
| `bwbc6d` | Pet-poll test, created before the Test ID was wired into the title (un-numbered) |
| `mw9kpp` | Pet-poll test, superseded — its public title carried the old `trash delete test —` junk prefix (since removed) |
| `9hmbg8` | Scratch SNTV confirmation (Plurality, 2 winners → c, b) — junk title "wqefwefwe…"; proved BV multi-winner Plurality = SNTV, then discardable |

**Lesson (why the title guard exists):** because API elections are **public and permanent**, the title must be right on the *first* create — there is no rename or delete. `create_bv_test_election.py` now (a) prepends only the `BV<n>` Test ID (no "trash/delete/test" junk), and (b) runs a pre-check that **blocks junk/placeholder titles** and reminds you the title is permanent + public. Set `BV_ALLOW_JUNK_TITLE=1` only to override deliberately.

## Ready-to-file BetterVoting GitHub issue

If BV should fix this, the reproduction and evidence below are a clean report (paste into a new issue at `github.com/Equal-Vote/bettervoting`):

---

**Title:** Election owner can't access `/admin` — admin authorization ignores `owner_id` / `admin_ids`

An election whose `owner_id` is my account appears in my `/manage` list, but opening `/<id>/admin` denies me: *"Only the users with admin access on the election can view this page."*

**Repro:** Create an election via `POST /API/Elections` with `owner_id` set to my account id (second test: also `admin_ids: [my id]`). It appears in `/manage`, but `/<id>/admin` denies admin access.

**Evidence** — two elections, **same `owner_id` (my account)**:

| Election | created via | `admin_ids` | `/admin` result |
|---|---|---|---|
| UI-created | builder UI | `null` | ✅ full admin |
| API-created | `POST /API/Elections` | `[my account]` | ❌ denied |

The election that **works** has `admin_ids: null`; the one that's **denied** explicitly lists me in `admin_ids`. So `/admin` authorization depends on neither `owner_id` nor `admin_ids`; it appears to use a server-side role binding written only by the authenticated create flow (`voterAuth.roles`/`permissions` are empty on the API-created election).

**Impact:** I can see but not administer — edit, close, or **delete** — my own election. API-created elections can't be cleaned up from the UI.

**Ask (any one of):** honor `owner_id`/`admin_ids` for `/admin` authorization; **or** provide a "claim" path to bind an owned election to my account; **or** document the intended behavior so the API-creation path is usable end-to-end.

---

## Related

- [BV — BetterVoting (the live web app)](README.md)
- The script + how to run it: [`create_bv_test_election.py` — tool guide](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.md)
- The BV-backed case workflow is documented in the repo's `CLAUDE.md` (steps 3–4).
