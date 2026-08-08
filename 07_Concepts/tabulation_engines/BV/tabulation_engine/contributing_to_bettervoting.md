# Contributing to BetterVoting — process notes (for next time)

A record of how the first code contribution went, so the workflow (and its gotchas) isn't re-derived from scratch. Written after PR **[#1419](https://github.com/Equal-Vote/bettervoting/pull/1419)** — "Clean up the ballot-data export (JSON v2 + CSV Raw/Official)".

> **Outcome (recorded 2026-08-07) — the PR was SPLIT, and half of it shipped.** A maintainer (jacksonloper) opened **[#1428](https://github.com/Equal-Vote/bettervoting/pull/1428)** four days later, extracting this PR's **CSV bug fixes** onto a branch named `masiarek/csv-escaping-fix`, explicitly crediting the author and **keeping Adam's authorship on the commit** (`309d84b0`, in BV's `main` history). It merged 2026-07-16, and added a third bug fix of its own (the Download menu unmounting mid-fetch). The **JSON v2 format and the Raw/Official CSV split** were held back — "the rest needs some contemplation" — and #1419 was closed on 2026-07-15. So the tracking issue **[#1420](https://github.com/Equal-Vote/bettervoting/issues/1420)** stays open and BV still ships the v1 export, documented in [the BV JSON export reference](../bv_json_export_format.md).
>
> **Follow-up (2026-08-07):** the format half is back as **[PR #1492](https://github.com/Equal-Vote/bettervoting/pull/1492)**, reshaped to be purely additive — `+391/−0`, the existing "Download JSON" untouched and byte-identical, the compact shape offered as a second menu item. Deletions are the thing a maintainer has to think about; a diff with none of them asks a much smaller question. Same `buildElectionExport`, now verified across 197 distinct real exports as well as the unit suite.
>
> **The lesson for next time: land bug fixes and format/product changes as separate PRs.** No technical objection to the v2 format was ever posted — the only review comment on #1419 was CodeRabbit flagging one stale test assertion. What stalled it is that a bundled PR forces an all-or-nothing decision, and *changing an existing public download* is a judgement call a maintainer can't make on a Tuesday, while *fixing a corrupt CSV* is obvious. Bundled, the obvious part waits on the deliberate part; split, the obvious part merges in a week. A maintainer doing the split by hand is a friendly outcome, not a rebuff — but it is work you can do yourself, and doing it yourself keeps the deliberate half alive as an open PR instead of a closed one.

> **Running it locally** (dev server vs Docker, and the AirPlay / Keycloak / `crypto.randomUUID` / shared-rebuild gotchas) → [running_bettervoting_locally.md](running_bettervoting_locally.md).

## The setup facts (easy to forget)

- **Upstream repo:** `Equal-Vote/bettervoting` (was formerly "star-server").
- **My fork:** `github.com/masiarek/star-server` — it kept the *old* name from when I forked it years ago, but it's still a fork of `Equal-Vote/bettervoting`, so it works fine.
- **I do NOT have direct push to `Equal-Vote/bettervoting`.** `git push origin` returns `403 denied to masiarek`. Contributions go **fork → PR**. (They may grant me direct contributor access later, but I've never asked, and there's still a **required approval by another person** either way.)
- **Local clone:** `/Volumes/T7/Voting/BetterVoting/BV/bettervoting`, remote `origin = Equal-Vote/bettervoting`. I add a `fork` remote pointing at my fork:
  ```
  git remote add fork https://github.com/masiarek/star-server.git
  ```
- **Git identity** wasn't set in this clone — had to `git config user.email` / `user.name` once.

## The workflow we followed (export-cleanup example)

1. **Diagnosed the problem.** The "Download JSON" export was literally `JSON.stringify({Election, Ballots, Results})` of the raw in-memory objects (`packages/frontend/src/components/Election/Results/BallotDataExport.tsx`), leaking the tabulator's internal shape (O(n²) pairwise maps, mixed casing, inconsistent timestamps).
2. **Fixed it in the right layer.** The export is a **view**, so the transform went in `packages/shared/src/utils/exportFormat.ts` (`buildElectionExport`) — no change to the tabulation engine, the results endpoint, or what the UI renders. Wired it into `downloadJson`.
3. **Wrote a unit test.** `packages/backend/src/test/exportFormat.test.ts` (Jest).
4. **Verified on real data.** Ran the actual transform against saved exports in `06_Other/_demo_dropbox/` — 69% of legacy size on a 51-candidate election, 60% on a small one, all defects gone. (This is what proved it before ever touching CI.)
5. **Branch + commit.**
   ```
   git checkout -b feature/clean-json-export
   git add <the 3 files only>
   git commit    # descriptive message: what changed and why
   ```
6. **Push to my fork.**
   ```
   git push -u fork feature/clean-json-export
   ```
7. **Open the PR against upstream.**
   ```
   gh pr create --repo Equal-Vote/bettervoting \
     --base main --head masiarek:feature/clean-json-export \
     --title "..."
   # choose the pull_request_template, fill Description / Screenshots / Related Issues
   ```
   → PR #1419.
8. **(Optional) File a tracking issue** and add `fixes #N` to the PR's Related Issues.
   **Caveat:** issue creation may be **restricted** in this repo ("Issue creation is restricted"). If so, skip it — the PR is self-contained.
9. **Approval.** Another maintainer reviews/approves before merge. That's the gate — not my push access.

## Gotchas hit (and fixes)

- **Stale `packages/backend/build/` directory** shadows `src` and creates duplicate Jest haste-map mocks; it also made babel choke on TS in the new test. `rm -rf packages/backend/build` before `npm test -w @equal-vote/star-vote-backend`. Worth a separate PR to gitignore `build/`.
- **`<placeholders>` in pasted commands** — angle brackets are shell redirection; they error with "Read-only file system" / "no such file". Always substitute the real value.
- **`--body-file` needs the real path** (quoted if it has spaces).

## Why Docker was NOT needed (the surprise)

I installed Docker assuming I'd need it — I didn't, for this kind of change. Here's the split:

**Docker (`docker compose up`) spins up the full runtime stack** — app + PostgreSQL + Keycloak + nginx + Playwright. You need it when you want to **run the actual application** or run **end-to-end (Playwright) tests**, because those need a live database, auth server, and browser.

**What we did needed none of that:**

- The change was a **pure function** (`buildElectionExport`) — no DB, no auth, no network, no running server.
- **Unit tests are Jest** — plain Node, no services. `npm test -w @equal-vote/star-vote-backend`.
- **Type/build checks are `tsc`** — plain Node.
- **Verification** ran the transpiled function against **saved JSON exports** on disk.

So the rule of thumb:

| Task | Docker needed? |
|---|---|
| Build / typecheck (`tsc`, `npm run build`) | No |
| Lint | No |
| **Unit tests** (Jest, tabulators, pure functions) | No |
| Run the app locally end-to-end | Yes (needs Postgres + Keycloak) — or provide those yourself |
| **E2E / Playwright tests** | Yes (the compose stack includes them) |
| Anything touching the DB layer / migrations against a real Postgres | Yes (or a local Postgres) |

Bottom line: for a self-contained frontend/shared change covered by unit tests, Docker is overkill. Keep it installed for the day you touch the backend runtime, auth, migrations, or need to run the E2E suite.

## Reusable checklist

- [ ] Change in the smallest correct layer (view vs engine vs DB).
- [ ] Unit test added (Jest — no Docker).
- [ ] Verified on real data where possible.
- [ ] `git checkout -b feature/...`, stage only the intended files, descriptive commit.
- [ ] `git push -u fork <branch>` (fork = `masiarek/star-server`).
- [ ] `gh pr create --repo Equal-Vote/bettervoting --base main --head masiarek:<branch>`.
- [ ] Fill the PR template; link an issue if creation is allowed.
- [ ] Wait for another maintainer's approval.
