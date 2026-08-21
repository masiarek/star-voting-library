---
name: bv-docs
description: Working on BetterVoting's help site (docs.bettervoting.com) — the Jekyll/just-the-docs setup, the local Docker preview and its three traps, front-matter and link conventions, which doc URLs the app hardcodes and can't move, the verified election-state facts, the Google-Docs backlog, and the fork/PR path. Use whenever a task touches docs.bettervoting.com, BV's docs/ folder, a BV docs PR, or publishing BV help content. NOT for BV elections/bvids/exports — that's the `bettervoting` skill.
---

# BetterVoting docs — how to work on docs.bettervoting.com

Loaded on demand. This is about **BV's help site**. For BV *elections* (minting, bvids, exports, case naming) load the **`bettervoting`** skill instead — different job, different rules.

## Where things are

| What | Where |
|---|---|
| The docs source | `docs/` in the BV checkout — `/Volumes/T7/Voting/BetterVoting/bv-copy-fix` |
| Published at | <https://docs.bettervoting.com> (CNAME in `docs/CNAME`) |
| Built by | GitHub Pages' own Jekyll, straight from `docs/`. **No workflow in `.github/workflows/`** |
| Theme | `remote_theme: just-the-docs/just-the-docs`, `color_scheme: custom` |
| Upstream | `Equal-Vote/bettervoting` · **fork is `masiarek/star-server`** (pre-rename name) |

The repo's own analysis lives in this repo at `07_Concepts/tabulation_engines/BV/`:
- [the IA proposal](../../../07_Concepts/tabulation_engines/BV/bv_docs_information_architecture.md) — competitor comparison, proposed nav, publishing order, the BPML verdict
- [draft-state findings](../../../07_Concepts/tabulation_engines/BV/bv_draft_state_test_votes.md) — what "test votes" means, verified against source

## Local preview (do this before writing anything)

**The docs are NOT in `docker-compose.yml`** — that runs the app (backend, db, keycloak). Preview needs its own Jekyll. From `docs/`:

```bash
docker run --rm -v "$PWD":/site -w /site -v bvdocs-gems:/usr/local/bundle -p 4000:4000 ruby:2.7 sh -c "bundle install && bundle exec jekyll serve --host 0.0.0.0 --port 4000"
```

Three traps, each of which cost a round trip the first time:

1. **`jekyll/jekyll:3.9` does not exist.** Those images are unmaintained; the pull fails. Use a `ruby:` base + the `github-pages` gem (what Pages itself runs).
2. **`ffi` must be pinned `< 1.17`** — newer versions need Ruby >= 3.0 and won't resolve against the Ruby 2.7 that `github-pages`' Jekyll 3.9 wants.
3. **The repo identity must be set.** `jekyll-github-metadata` refuses to build without it: *"No repo name found."* It normally reads the `origin` remote, but the command mounts only `docs/` so `.git` is outside the container. Either `repository: Equal-Vote/bettervoting` in `_config.yml` (proposed in the preview PR) or `-e PAGES_REPO_NWO=Equal-Vote/bettervoting` on the command.

The `bvdocs-gems` named volume caches the gem set — cold start is minutes, warm rebuild ~7 seconds. If the Gemfile isn't on your branch yet, pull it across with `git show docs/local-preview:docs/Gemfile > docs/Gemfile` for testing, then delete it before committing.

**Port 4000 already allocated?** A previous preview container is still up: `docker stop bvdocs`.

## Page conventions

**Front matter** — every page needs it, and `parent` is the one that bites:

```yaml
---
layout: default
title: Election States
nav_order: 1
parent: BetterVoting Documentation
---
```

- **`parent:` must match the parent page's `title:` character-for-character, emoji included.** BV's own guide warns about this. A mismatch means the page silently doesn't appear in the nav. **This is unverifiable in the GitHub web editor** — it's the main reason to preview locally.
- Section parents: `BetterVoting Documentation` (help/), `Other Tools`, `Contribution Guide`, and inside it `💻 Developers` / `☁️ DevOps` / `✍ ️Writers` — note the odd space in the Writers one, copy it exactly.
- `nav_order` is per-folder and sparse. Existing help/: election_states 1, paper_ballots 5, hand_count 6, **ties 6 (collision — their order is arbitrary)**, security_options 7, preliminary_results 8, faq 99, beta 99.

**Links — use the `.md` form.** `jekyll-relative-links` ships with the `github-pages` gem and rewrites `.md` → `.html` at build. So `[Preliminary Results](preliminary_results.md)` works **both** on the published site and when reading the source on GitHub. Bare `.html` works only on the site; extensionless works only on the site. BV's repo contains all three; `.md` is the one to write.

**Callouts** are configured (`callouts_level: quiet`) — `highlight`, `important`, `new`, `note`, `warning`:

```markdown
{: .warning }
> **Test ballots are deleted when you finalize.**
```

**Liquid runs over page source before Markdown, including inside code fences.** Any literal `{{...}}` must be wrapped in `{% raw %}…{% endraw %}` or Liquid eats it — silently, if it parses; with a build warning, if it doesn't. This is invisible in GitHub's preview and broke a live page for months.

**Mermaid is not enabled.** Adding it means a `mermaid:` key in `_config.yml`. Don't slip it into a content PR.

## Sidebar structure ≠ folder structure (verified 2026-08-08)

**just-the-docs builds the nav from front matter, not from directories.** Proof from BV's own repo: `index.md` sits at the docs root and is the `parent:` of `help/faq.md` in a subfolder. So **you can reorganize the sidebar into sections without moving a single file or changing a single URL** — add a section page with `has_children: true`, then set `parent:` on its children wherever they live.

This matters because moving files is expensive here and re-parenting is free:

- Six doc URLs are hardcoded in the app (see the table above), two as deep anchors. A move breaks them and needs a coordinated frontend PR.
- **Redirects work — since 2026-08-20** (PR #1535 added `plugins: [jekyll-redirect-from]` to `_config.yml`; before that, `redirect_from:` in front matter emitted nothing and the old URL just 404'd). Put the old address in the moved page's front matter, as a `redirect_from:` list entry (`- /help/old_name.html`), and the build writes a stub there with a `<meta http-equiv="refresh">` to the new one. Re-verified on a live build 2026-08-21. Two limits: the entry has to stay forever (the old address works only while it is listed), and **a redirect is per-page, not per-anchor** — renaming a heading still breaks `ties.html#random-tie-breakers` and `faq.html#write-in-scores-not-counted`, which the app links directly.

Default answer to "should we create folders?": **no — restructure the sidebar with `parent:`.** Folders are storage; the sidebar is the information architecture, and only one of them is visible to users.

## URLs are load-bearing — the app hardcodes them

Eight links from the app into the docs. Moving or renaming any of these pages breaks the product, and two are **deep anchors**, so the heading text is load-bearing too:

| URL | From |
|---|---|
| `/help/paper_ballots.html` | `App.tsx` route `/paper_ballots`, `Header.tsx` menu |
| `/help/hand_count.html` | `App.tsx` route `/hand_count` |
| `/help/ties.html` | `App.tsx` route `/ties` |
| `/help/ties.html#random-tie-breakers` | `en.yaml` — shown when a tie is broken |
| `/help/faq.html#write-in-scores-not-counted` | `Results.tsx` "Learn more" |
| `/help/preliminary_results.html` | `en.yaml` `learn_link` |
| `/other_tools/google_forms.html`, `/other_tools/google_sheets.html` | `en.yaml` |
| `/contributions/0_contribution_guide.html` | `App.tsx` route `/volunteer` |

Two are **already broken** and worth fixing if you're nearby: the backend's Keycloak error points at `/contributions/1_local_setup.html` (really `contributions/developers/1_local_setup.md`), and BV's own state-overview Google Doc points at `/help/1_faq.html` (really `/help/faq.html`).

## Verified product facts (don't re-derive these)

Checked against source. If a Google Doc draft contradicts one, the draft is wrong.

**Election states** — `validElectionStates = ['draft','finalized','open','closed','archived']`. There is **no test state**.

| State | Voters can vote? | Admin can edit? |
|---|---|---|
| draft | Yes — test ballots | **Yes — the only editable state** |
| finalized | No | No |
| open | Yes — real ballots | No |
| closed | No | No |
| archived | No | No |

- Voting gate: `castVoteController` allows only `open` and `draft`; else *"Election is not open"*.
- Edit gate: `editElectionController` allows only `draft`; else *"Election is not editable"*.
- **Draft is the test mode.** It skips authentication, the voter roll, `assertVoterMayVote`, and `ballot_updates` — so a draft test does **not** confirm voter restrictions, one-person-one-vote, or vote-changing.
- **Finalize** is one-way, draft-only, once; auto-deletes all draft ballots; stamps `max_rankings` default 6 if unset.
- **Transitions are lazy/read-triggered** (`updateElectionStateIfNeeded`) — no scheduler. No start time ⇒ finalize opens it **immediately**. No end time ⇒ **never** auto-closes.
- **Manual open/close only when no start/end times are set** — *"Cannot open or close an election with scheduled start and end times."* The two routes are exclusive.
- **Archive works from any state** (rejects only if already archived).

**Election vs Poll** — `settings.term_type` is a **vocabulary setting only**. Every use feeds `useSubstitutedTranslation`; nothing branches on it. It swaps candidate→choice, race→question, ballot/vote→response, and rides into emails and share text. It changes nothing about how voting works.

## The real bottleneck: content is unpublished, not unwritten

The site has ~7 user-facing pages. BV's Google-Docs corpus has 60+ — registration, ballot secrecy, quorum, proxy voting, receipts, exports, quick polls, demo mode, checklists, a glossary, all five states. The state-overview doc is itself headed *"Draft document before moving it to 'Official User Documentation'"*. **The Drive → site pipeline is already the intended workflow; it just hasn't run.**

So the job is **publish → dedupe → shelve**, not write. Expect duplicates (3 docs on Poll-vs-Election, 2 on states, 2 on checklists) and drafts marked `clean-up required` / `non-approved content` / `missing document`.

**Two editorial rules the Drive drafts keep breaking:**

1. **Answer the product question, not the general one.** The Poll-vs-Election drafts explain what political scientists mean by "poll." The user staring at that radio button wants to know what happens if they click it.
2. **Don't hedge where the code is definite.** "usually read-only", "typically", "may be locked down" are tells that a draft was written from general knowledge. Check the source and say the thing.

**The BPML sheet** is the right backlog and the wrong navigation. Keep it as the coverage matrix (its `missing` cells are it doing its job); don't ship its L1/L2/L3 hierarchy as the site's nav — users search for tasks, not process nodes.

## PR workflow

The fork was never renamed, so `gh` needs explicit flags — plain `gh pr create` guesses wrong:

```bash
git push fork <branch>
gh pr create --repo Equal-Vote/bettervoting --base main --head masiarek:<branch> --title "..." --body-file <file>
```

- Branch off `origin/main`, not off whatever branch is checked out (the checkout often sits on unrelated in-flight work).
- **Keep the web-UI flow as the recommended default in anything you write.** Arend recommends editing on GitHub for small changes, and he's right — local preview is the second gear for new pages and structural work, not a replacement. Framing it as a fix for a broken process reads badly.
- Batch by section, not by page — 60 pages as 60 PRs will stall. And get the nav structure agreed *before* filling it, or every content PR relitigates placement.

**Merged, and now the toolchain** (check state before assuming): [#1501](https://github.com/Equal-Vote/bettervoting/pull/1501) local preview + Liquid fix (adds `docs/Gemfile` and `repository:`), [#1535](https://github.com/Equal-Vote/bettervoting/pull/1535) redirects. So the preview command above needs no Gemfile shuttling any more — `docs/Gemfile` is on `main`.
