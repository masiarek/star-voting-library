# Contributing to BetterVoting — process notes (for next time)

A record of how the first code contribution went, so the workflow (and its gotchas) isn't re-derived from scratch. Written after PR **#1419** — "Clean up the JSON ballot-data export (v2 format)".

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
