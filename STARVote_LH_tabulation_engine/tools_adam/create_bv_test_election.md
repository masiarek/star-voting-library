# `create_bv_test_election.py` — create BetterVoting test elections via the API

**Purpose.** Spin up a real [BetterVoting](https://bettervoting.com) election **and cast its ballots** straight through the REST API — no clicking through the builder UI. It's the first half of the repo's BV-backed test-case pipeline: create on BV → export → reproduce in the LH engine → freeze. Driving the API instead of the UI makes case creation fast, scriptable, and reproducible (define the election once, re-run any time).

Script: [`create_bv_test_election.py`](create_bv_test_election.py). (It replaced an earlier approach that drove the BV builder UI with Playwright and a saved login session — the API path is faster and needs no stored login.)

## How to run it

Dependencies are declared inline (PEP 723), so `uv` installs them into an ephemeral env — no `pip`, no `.venv` pollution:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py
```

It prints each new `bettervoting.com/<id>` URL and saves the created election object to `_demo_dropbox/`.

## Defining the election(s)

Edit the `ELECTIONS` list near the top of the script. Each entry is self-contained:

```python
{
    "title": "BV999 - short descriptive title",
    "description": "one-line context",
    "method": "STAR",          # STAR | Approval | STAR_PR | ...
    "num_winners": 1,          # >1 + method STAR = Bloc STAR on BV
    "candidates": ["Ann", "Bob", "Cal"],
    "ballots": [[5, 0, 3], [0, 4, 5]],   # one row per voter, aligned to candidates
    "expected": "free text (what should win)",
}
```

Score range depends on the method: **Approval = 0/1**, **STAR / Bloc / STAR_PR = 0–5**. Add as many entries as you like; the script creates each and casts its ballots (one throwaway voter per row). Leave `ELECTIONS = []` when idle so a stray run does nothing.

## Auth (no credential stored)

The BV backend requires **asymmetric RS256**: the election carries a PEM **public** key in `auth_key`, and the request's `custom_id_token` is a JWT signed with the matching **private** key. The script mints a fresh keypair per run — self-consistent, so **no real BV password or secret is used or stored**. (The old HS256 "secret == user id" recipe is stale.)

`owner_id` is set from `BV_USER_ID` (default: Adam's real account, so elections appear in `/manage`). Override per run:

```bash
BV_USER_ID=<your-bv-account-id> uv run …/create_bv_test_election.py
```

## After it runs

The plain API GET the script saves lacks `Ballots`/`Results`. For the **frozen `_bv_export.json`** a case needs, grab the full export (Election + Ballots + Results) from the BV UI and drop it in `_demo_dropbox/`. Then reproduce it in the LH engine and build the case files (see the repo `CLAUDE.md`, "Workflow — building a BV-backed test case," steps 3–6).

## Known limitation

API-created elections are **public, listable, and exportable** — but **not UI-administrable** (you can't edit / close / delete them from `/admin`, even as the owner). BV authorizes admin off a server-side role binding written only by the authenticated create flow, not off `owner_id`/`admin_ids`. Full write-up + a ready-to-file BV issue: [Creating BetterVoting elections via the API](../../00_start_here/tabulation_engines/BV/bv_api_election_creation_notes.md).

## See also

- [BV — BetterVoting (the live web app)](../../00_start_here/tabulation_engines/BV/README.md)
- Repo `CLAUDE.md` — the full 9-step BV-backed case workflow.
