# `create_bv_test_election.py` — create BetterVoting test elections via the API

**Purpose.** Spin up a real [BetterVoting](https://bettervoting.com) election **and cast its ballots** straight through the REST API — no clicking through the builder UI. It's the first half of the repo's BV-backed test-case pipeline: create on BV → export → reproduce in the LH engine → freeze. Driving the API instead of the UI makes case creation fast, scriptable, and reproducible (define the election once, re-run any time).

Script: [`create_bv_test_election.py`](create_bv_test_election.py). (It replaced an earlier approach that drove the BV builder UI with Playwright and a saved login session — the API path is faster and needs no stored login.)

## How to run it

Dependencies are declared inline (PEP 723), so `uv` installs them into an ephemeral env — no `pip`, no `.venv` pollution:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py
```

It prints each new `bettervoting.com/<id>` URL and saves the created election object to `06_Other/_demo_dropbox/`.

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

There is nothing to authenticate. `POST /API/Elections` carries no auth middleware and takes `owner_id` straight from the request body, so **no BV password, secret, or token is used or stored**.

The script used to set the election's `auth_key` (a PEM RS256 public key) and sign a matching `custom_id_token`. That was unnecessary — and harmful: an election with an `auth_key` makes BV substitute the custom-token identity for your Keycloak one on every election-scoped route, so your own login gets no roles and **the admin sidebar disappears**, permanently. It is omitted by default since 2026-08-15. Set `BV_AUTH_KEY=1` only for a run that needs owner-scoped reads (the non-fatal `/ballots` count check), knowing that election can never be administered or repaired afterwards. Full story: [Creating BV elections via the API](../../07_Concepts/tabulation_engines/BV/bv_api_election_creation_notes.md#the-admin-gate-and-how-it-was-closed).

`owner_id` is set from `BV_USER_ID` (default: Adam's real account, so elections appear in `/manage`). Override per run:

```bash
BV_USER_ID=<your-bv-account-id> uv run …/create_bv_test_election.py
```

## After it runs

The plain API GET the script saves lacks `Ballots`/`Results`. For the **frozen `_bv_export.json`** a case needs, grab the full export (Election + Ballots + Results) from the BV UI and drop it in `06_Other/_demo_dropbox/`. Then reproduce it in the LH engine and build the case files (see the repo `CLAUDE.md`, "Workflow — building a BV-backed test case," steps 3–6).

## Known limitation

An election minted **open** is permanent: it can never be renamed, re-described, closed or deleted. `editElection` accepts only elections whose `state` is `draft`, and the UI has no delete control at all. So the title, the description and its backlink have to be right on the first create.

Two things that are *no longer* limitations. API-created elections **are** administrable from the account named in `owner_id` — the sidebar was missing only because this script used to set the election's `auth_key`, which makes BV substitute a custom-token identity for your Keycloak one ([the full story](../../07_Concepts/tabulation_engines/BV/bv_api_election_creation_notes.md#the-admin-gate-and-how-it-was-closed)). And a spec may carry `state: "draft"`, which mints a private rehearsal that stays editable and archivable — the way to try something without leaving a permanent public artifact.

## See also

- [BV — BetterVoting (the live web app)](../../07_Concepts/tabulation_engines/BV/README.md)
- Repo `CLAUDE.md` — the full 9-step BV-backed case workflow.
