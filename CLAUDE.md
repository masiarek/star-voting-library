# CLAUDE.md — working guidance for this repo

Standing instructions for Claude when working in this project — and the house
conventions for anyone contributing (human front door: [CONTRIBUTING.md](CONTRIBUTING.md)).
The Claude-only operational grants live at the [bottom of this file](#agent-operations-claude-specific).

## What this is
A **STAR Voting education** repo built on a fork of Larry Hastings' `starvote`
(single-winner STAR engine + extra reporting), plus a vendored RCV-IRV engine,
example YAML elections, teaching docs, and Larry↔Adam conversation scripts.
Audience: voters, presenters, and debaters learning/teaching STAR.

---

## Terminology policy (important — keep it consistent & correct)

**Background:** "RCV" is widely used loosely to mean IRV (FairVote-era usage that
also trained most AIs to be sloppy). We meet people where they are, but we stay
precise. The key idea: **RCV names a BALLOT (ranked); IRV names one TABULATION of
it.** Other tabulations of the *same* ranked ballot: **Ranked Robin** (Condorcet
/ "consensus"), **STV** (proportional).

**House style:**
- **Default to `RCV-IRV`** in this repo's method comparisons, engine output, and
  debate/teaching docs. Unambiguous, and already the engine's term.
- **Use `IRV`** in technical/critical passages — center squeeze, exhausted
  ballots, non-monotonicity are **IRV-specific**, *not* properties of all ranked
  ballots (Ranked Robin isn't squeezed). Saying "RCV does X" there is imprecise
  and an easy target.
- **Reserve bare `RCV`** for "the ranked-ballot family," and say so when used that
  way.
- **Name `Ranked Robin` / `STV`** explicitly; never fold them into "RCV" = IRV.
- **Don't be a purist who derails.** When others use "RCV" loosely, keep their
  word, correct once, move on. Don't fight the wind.

**US-usage caveat (the nuance):** `RCV-IRV` is a deliberate *house* compound, **not
standard US usage** — appending "IRV" can look odd or confusing to a general
public audience, who only know "RCV." So:
- **Technical / debate / engine / docs → `RCV-IRV` (or `IRV`).** Precision wins.
- **Public-facing copy (slides, intro talk) → "RCV" is fine**, but clarify *once*
  on first mention: e.g. *"RCV — ranked ballots counted by instant runoff (IRV)."*
  Then use the familiar word.

Family tree, when-to-use table, and glossary are canonical — **do not restate the
taxonomy from memory:** see `07_Concepts/tips/TIPS_terminology.md` and `GLOSSARY.md`.

**Other voting-term canon:**
- **STAR** = Score Then Automatic Runoff (a *score* ballot + that tabulation; the
  same ballot can be Approval / Score / Proportional STAR).
- **Equal Support** is the canonical label for the no-preference runoff bucket
  (matrix legend *and* runoff) — printed **plain**, just "Equal Support". The aka
  (Equal Preference / No Preference) is documented once in `GLOSSARY.md`, **not**
  shown on screen on every runoff line. Do **not** reintroduce "Equal Preference" as the
  lead term.
- **Favorite Betrayal Criterion ≠ Later-No-Harm** — keep distinct. Neither STAR
  nor IRV is FBC-compliant; RCV-IRV fails it structurally (center squeeze), STAR
  only in rare constructions. See `01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md`.
- Spelling: **Bucklin** (not "Buckling"). **Hare ≈ IRV** single-winner, **STV**
  multi-winner. Borda & Bucklin are ranked but **not** Condorcet.

---

## Repo conventions (so output stays consistent)
- **Case files carry NO `options:` block** (deleted from all 501 case files on 2026-08-09). The engine's own defaults are the house on-screen style, and the Preference Matrix switches itself off for multi-winner and 2-candidate races; `--full` prints everything, and the `_tabulated` mirror always does. Only the option-demo files set `options:`. Changing what the engine prints, or the runoff summary, the Smith-set block or the RCV-IRV transfer block → **load the `engine-rendering` skill**. Reader-facing account: [`options.md`](01_STAR/01_Learn/reporting/reporting_LH/options.md).
- **The machine-readable result contract (`--json`) → load the `result-contract` skill.** The one rule worth carrying without it: every number in the JSON comes from the same function the printed report calls, so adding a family means extending the shared tally and **never** writing a second count inside [`result_json.py`](STARVote_LH_tabulation_engine/result_json.py).
- **Voter counts — keep examples SMALL.** Default to the *fewest ballots* that
  make the point; prefer **individual ballots** (one row per voter, a handful of
  them) over large weighted blocs. A 3-voter example that shows the effect beats a
  100-voter one. Only scale up when a larger electorate is genuinely essential
  (e.g., percentages or proportional seats). When you *do* weight, `Count` values
  must be **≥ 6** (avoid collision with 0–5 scores); scaling all weights ×N
  preserves STAR/proportional winners. See `07_Concepts/tips/TIPS_choosing_voter_counts.md`.
- **Quote a candidate or contest name that YAML would retype** — unquoted `No` parses as `False`, `12:30` as `750` — above all in `expected_winners:` and `election_title:`. Machine-checked (`check_yaml_name_types`; its comment carries the history).
- **A ballot's weight goes BEFORE the scores**, on every surface: `3 × 5,2,0`, never `5,2,0 ×3` — in Markdown, YAML comments and `scenario_description` prose alike. Machine-checked (`check_ballot_weight_side`).
- **Candidate names — a fresh, easy cast per scenario; the same cast within one.**
  Prefer a *new* set of names for each scenario (memorable beats uniform — "the
  Ada/Ben/Cara split," "the Tennessee cities") over one fixed roster. Four rules:
  (1) **common and easy to say** — no obscure or confusable names (the "Cy" problem);
  (2) **distinct initials, in order** — A, B, C, D… so names line up with the ballot
  columns and reading order; (3) **phonetically distinct within a scenario** — avoid
  rhyming/blurring pairs (Dana/Hana, Ben/Glen) that don't carry when spoken aloud in a
  recording; (4) **use a theme when one fits** (Star Wars, cities, flavors) — that's
  the best kind of variety. **Variety _between_ scenarios, consistency _within_:** a
  matched pair or family (e.g. `05a`/`05b`) keeps the *same* cast — it's the same
  election with one thing changed, so new names would imply a different election. Use
  bare `A/B/C/D` only for purely abstract/academic illustrations where names are noise.
  **Canonical reusable elections** (Ann/Bob/Cal, the team lunch, the runoff reversal,
  Tennessee, the pets) are registered in `07_Concepts/tips/TIPS_canonical_elections.md`
  with their jobs and the two rules — *one election per page* and *canonical = frozen
  ballots* (same cast ⇒ same election; a new lesson gets a new cast, never a tweak).
  Reuse a canonical for generic examples instead of minting a new cast.
- **Markers (all tabulate as 0):** `-` blank · `~` race abstention · `&` candidate
  abstention · `?` spoiled · `%` spoiled+reissued. **No `^`** (removed). Approval
  ballots accept only `0`/`1` (+ blank/marker = not approved).
- **Levels (101/201/301)** live ONLY in the curriculum — now a hub
  (`07_Concepts/CURRICULUM.md`) plus one page per level
  (`07_Concepts/curriculum/CURRICULUM_101.md` / `_201.md` / `_301.md`); the hub links them and holds no
  level content itself, so there's a single source of truth per level (no sync
  drift). Don't tag every file. Example folders stay content-typed
  (`01_STAR/`…`05_Ranked_Robin/`, `method_comparisons/`, `06_Other/`).
- **One door per voting method.** A method's concept pages live inside its own folder (`01_STAR/`…`05_Ranked_Robin/`, in `01_Learn/`; the two `06_Other` methods still use `concepts/`), and that folder's `README.md` is its start-here. `07_Concepts/` is **cross-method only** — never put a method-specific page back into it. Inside a method folder the second level is a fixed, ordered set of buckets — `01_Learn/`, `02_Examples/`, `03_Criteria/`, `04_Real_Elections/`, `05_Practice/`, `09_Parked/` — and each method takes only the ones it needs. **Capitalize the word after the number** (MkDocs builds sidebar labels from folder names, so `02_examples` would show up lowercase), and keep difficulty out of folder names. **Moving or renaming pages → load the `moving-pages` skill first**: `migrate_concept_links.py` must run *before* the `git mv`, and it silently misses three things.
- **Where text lives:** per-file context in the YAML (`scenario_description`
  printable, `video_script` = notes, never shown on screen); cross-file teaching in
  Markdown. No hand-authored `.md` per YAML (the generated pages are the exception —
  see next bullet). See `YAML_library/ORGANIZATION.md`.
- **Folder overview pages are named exactly `README.md`** (not `README_<folder>.md`).
  GitHub only auto-renders a file named `README.md` in a folder's tree view, so each
  folder's landing/overview page **must** be `README.md` — that's what makes the folder
  show a friendly page instead of a bare file list. Keep the descriptive title in the
  file's `# H1` (e.g. `# 01_STAR — single-winner STAR`). A folder may keep *secondary*
  docs under descriptive names (e.g. `README_larry_hastings.md`, `FORK_NOTES.md`), but
  the one overview is always `README.md`.
- **The repo publishes as a searchable website** — <https://masiarek.github.io/star-voting-library/>, built by root `mkdocs.yml` (MkDocs Material) straight from the repo's own Markdown and deployed by `.github/workflows/docs.yml` on every push to master. Two rules stay here because they bite outside any site task: **`site/` is generated output — never commit**, and a **`redirects.redirect_maps` entry is permanent** — published URLs are quoted in BetterVoting election descriptions that can never be edited, so a deleted redirect is an unfixable 404. For everything else — the plugin-vs-hook decision, `NAV_ORDER` and sidebar order, local preview, the two kinds of redirect and when to retire one → **load the `site-build` skill**. Details + known nits: [`website_build.md`](07_Concepts/about_this_repo/website_build.md).
- **Research-paper topics live OUTSIDE this repo**, in the private companion <https://github.com/masiarek/star-voting-research-topics> — don't search this repo for them. Adding or editing a topic → **load the `research-topics` skill**.
- **When creating education pages or cross-referencing, prefer the `.md` page over
  the raw `.yaml` (and MD/links in general).**
  The generated per-election pages (`<set>_pages/<name>.md`, built by
  `STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`) are the reader-friendly surface: **lead with them**
  in tables, navs, and cross-references (left-most / primary link). Link a `.yaml`
  only when the *tabulatable source* is genuinely the point (e.g. a "run this file"
  command), and **demote** it (right-most column / secondary link). Page structure is
  **teaching first, raw tally last**: the `scenario_description` and educational value
  up top, then the **ballots**, then the **results** — with the full engine detail (the
  same content as the `_tabulated` mirror, or the mirror embedded) at the **bottom** of
  the page, so the reader gets the lesson before the numbers.
- **Link a folder by naming its `README.md`**: `[label](some_folder/README.md)`, never `some_folder/` or `some_folder` — MkDocs leaves the bare form unrewritten and it 404s on the site. If a generator emits one, fix the generator, not its output. Machine-checked (`check_folder_links`).
- **A repo path in backticks must be a link**, not bare code text: put the backticks in the label and a page-relative path in the href. A root-relative path in code text opens the wrong file from any page that isn't at the root. Generated pages and this file are exempt. Machine-checked (`check_code_span_paths`).
- **Voice — learner by default; "how to teach it" is a folder, not a mode.**
  The asymmetry decides it: a learner page serves a presenter fine (they read
  *"you score every candidate 0–5"* and say *"you all score…"*), but a presenter
  page **fails** a learner — someone who lands on *"explain to your audience
  that…"* has been handed a script for a job they didn't take. Traffic runs one
  way too: every inbound link from the wild delivers a learner; presenters are a
  small group who deliberately walk into `hands_on/`. So:
  - **learner-you** — the default. The `01_Learn` spine, `getting_started/`,
    `voting_styles/`, every `start_here`.
  - **reference-neutral** (third person, the `**One line:** …` openers) — the
    201/301 property and theory pages: `properties_and_limits/`, `the_count/`,
    most of `07_Concepts/topics/`.
  - **presenter-you** — `hands_on/` and slide decks **only**.
  - **Never two voices in one page.** If a learner page needs a presenter aside,
    *link* to `hands_on/`; don't switch person mid-page. (This is the drift that
    let `teaching_star_voting.md` claim it owned `STAR_start_here.md`'s
    structure.)
  - **Titles name the subject, not the reader's task** — "The STAR ballot &
    voting styles", not "How to learn the ballot". The exception is `hands_on/`,
    where the task *is* the subject ("Count a STAR election by hand").
- **`**Level:**` tags have one shape**: `**Level: <rung> · <audience>**` — rung `101` / `201` / `301` / `401`, an arrow range (`201 → 301`) or `reference`; audience `for voters` · `for presenters` · `for debaters` · `deep dive`. No "Voting" prefix and no parenthetical inside the bold; any elaboration goes after the closing `**`. Pick the audience before writing the page, since it decides the voice. Untagged pages are fine. Machine-checked (`check_levels`).
- **External sourcing — match the source to the claim, and disclose the lean.**
  Cite by tier: **electowiki** for *niche/branded method definitions & mechanics*
  (Ranked Robin, STAR variants, exotic methods — where Wikipedia is thin, it's the
  clearest); **Wikipedia** for the *neutral family term, notability, and any
  criteria/critical claim* (it has NPOV pressure, electowiki doesn't); **academic**
  (Stanford Encyclopedia, papers) for *rigor* (impossibility theorems, VSE math,
  proofs). electowiki and the campaign sites (equal.vote, starvoting.org,
  electionscience.org, fairvote.org, rangevoting.org) are **advocacy-adjacent** —
  fine for *definitions*, weak for *verdicts*; **whenever we lean on one, disclose
  its lean inline** (as the naming decoder, `how_to_learn`, and the "leans toward"
  table do). Never trade the repo's neutrality for better niche coverage.
- **Link key terms on first meaningful use — with restraint** (a habit, not a gate). The first time a page uses a jargon term with a canonical home — Condorcet winner/loser, center squeeze, monotonicity, later-no-harm, favorite betrayal, Equal Support, exhausted ballots, mutual majority, VSE, summability, Copeland / Ranked Robin, spoiler effect, the impossibility theorems — link it there. (1) Link to aid, not decorate; (2) never self-link the page's own subject; (3) link a term once per page; (4) prefer the topic hub, else the concept page, else the `GLOSSARY` entry; (5) **in a parallel list, link all or none** — a bullet list, table column or run-on sentence naming several methods side by side is linked consistently or not at all (rule 3 still wins, so a term linked earlier on the page stays unlinked). The one exception to rule 3, rare and deliberate: a term may link two anchors that answer two different questions, such as the definition where a summary table needs it and the evidence where the prose relies on it. When in doubt, fewer links.
- **Case folders: `README.md` at the top, sources in `cases/`.** The `.yaml` and `_bv_export.json` files live in `cases/`, so the engine nests the generated mirrors and pages inside it as `cases/cases_tabulated/` and `cases/cases_pages/`. A companion page's `<!-- case-meta:start -->` … `<!-- case-meta:end -->` block is written by `build_yaml_pages.py` — change the YAML and rerun it; never hand-edit inside the markers. Folders without a README keep the flat layout, and engine, tool and test-fixture folders are never reorganized. Details → the `new-case` skill.
- **Markdown prose: do NOT hard-wrap paragraphs (Adam's preference).** Write each
  paragraph as a single unwrapped line (soft wrap) — no fixed ~76/80-char line limit. Hard-wrapping is cosmetic: Markdown collapses single newlines inside a paragraph into spaces, so wrapped and unwrapped prose render identically. Keep real line breaks only where they're semantic: blank lines between paragraphs, fenced code blocks, tables, and list items.
- **Embedding an engine report or an output snippet in a Markdown page → load the `embedding-reports` skill.** The two rules that bite without it: engine reports are **generated** into a page (`<!-- report:<stem> -->` … `<!-- /report -->`), never hand-pasted; and an **annotated or curated** fence is never convertible — label it `title="Abridged for the lesson — not verbatim engine output"` rather than replacing it.
- **Ballot art, and showing a case's ballots on a page → load the `ballot-art` skill.** Art is drawn by `tools_adam/scripts/build_style_ballot_images.py`, never hand-embedded, and a hand-authored page shows its election with a `<!-- ballots:<stem> -->` block rather than a retyped Markdown table — the block already carries the numbers.
- **Cross-reference slides by title** via `07_Concepts/LINKS.md`
  short names — never page numbers or `#slide=id…` deep links.
- **Case-file naming.** LH-only cases (no BV election) get a descriptive name. BV-backed cases lead with the bvid — `b<bvid>_<descriptor>`, or `bv<testid>_<bvid>_<descriptor>` when a sheet Test ID exists — on every file of the group, including every case of a multirace set. Details → the `bettervoting` skill.
- **Never edit or migrate a frozen `_bv_export.json`.** It is the repo's only record of what BetterVoting permanently stores, so its paths are historical, like `mkdocs.yml`'s redirect keys (`migrate_concept_links.py` skips these files for that reason). The full account and the audit recipe are in the `bettervoting` skill.
- **Filed a bug upstream? Add a row to `07_Concepts/about_this_repo/upstream_bug_reports.md`.**
  Running one election through several engines is a good bug detector, so this repo files a
  fair number of reports against projects it doesn't own — BetterVoting, Larry's `starvote`,
  once GitHub Pages. They then get forgotten, because the page that motivated the report goes
  on to say something else. That page is the standing follow-up list (18 rows as of
  2026-08-09, 16 open), and it holds the API one-liner that re-checks every state at once.
  Two rules: it tracks only reports **we opened** — not every upstream issue the repo cites,
  which need no follow-up from us; and a **missing-guard** finding in BetterVoting goes to
  Arend privately *before* it goes on any page (the `bettervoting-qa` ground rule outranks
  the table). When one closes, the job isn't to flip the word — it's to ask what this repo
  teaches that the fix invalidates.
- **BetterVoting (BV) work → load the `bettervoting` skill.** Everything BV-specific lives
  there and loads on demand: minting with `create_bv_test_election.py` / `bv_election_specs.py`,
  fetching exports with `fetch_bv_export.py`, screenshots in `img/<bvid>_<what>.png`, the
  clickable `/results` lead line, the BV→repo description backlink, the `BV<n>` collision
  rule, `BV_registry.md` regeneration, and BV's method strings + bloc multi-winner.
  **Read it BEFORE creating or fetching any BV election** — BV titles, descriptions and
  numbers are PERMANENT and unfixable, so those rules have to be right the first time.
- **BetterVoting *documentation* work → load the `bv-docs` skill.** A different job from
  the one above, so a different skill: BV's help site (docs.bettervoting.com) is Jekyll +
  just-the-docs built by GitHub Pages from `docs/` in the BV checkout, and the skill holds
  the local Docker preview (plus its three traps), the front-matter `parent:` exact-match
  rule, the `.md` link convention, the eight doc URLs the *app* hardcodes (two of them deep
  anchors, so heading text is load-bearing), the verified election-state facts, and the
  fork/PR path. Load it before writing or moving any BV help page — and note the real
  bottleneck is that ~60 pages sit unpublished in Google Docs, so the job is usually
  publish/dedupe/shelve rather than write.

## Scratch drafting and new cases

Draft new scenarios in `trash_delete.yaml` and tabulate until the behavior shows; nothing there is permanent. The first line of the `ballots:` block is the candidate header (there is no `candidates:` key), weighted rows use a `Count:` header, and the title key is `election_title:`. **Delete the scratch files, and the junk `YAML_tabulated/` folder a run at the repo root creates, when done — never commit them.** The worked template, the tabulate command and the promotion steps → **load the `new-case` skill**.

## Engines
Running, cross-checking, or writing about a count → **load the `tabulation-engines` skill**: what each engine dispatches, the Ranked Robin tiebreak ladder and how BetterVoting's differs, the Minimax / Coombs / successive-elimination / grade-method tools, `abcvoting`, and the error messages. Reader-facing: [`07_Concepts/tabulation_engines/`](07_Concepts/tabulation_engines/README.md). Four facts worth carrying without it:
- `STARVote_LH_tabulation_engine/starvote_larry_hastings.py` is the main engine — STAR, Bloc STAR and proportional STAR, and by `voting_method` also RCV-IRV, Approval, Ranked Robin and Plurality, single- and multi-winner. RCV-IRV runs through vendored `pyrankvote` in `06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py`.
- **Cross-check every Ranked Robin case three ways** — this engine, BetterVoting's frozen export, and the third-party `pref_voting` Copeland (`tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py`) — not just the awkward ones. Ranked Robin's own tiebreak is Copeland → 1st Degree → 2nd Degree → lot.
- **The 0–5 score cap is the fork's teaching guardrail, not an engine limit** (`validate_star_rows(…, max_score=5)`); Score / Range voting is tabulable.
- Quick checks can use system `python3` (the engines are vendored); the user runs via their `.venv` / `uv`.

## Tests
The suite lives in `STARVote_LH_tabulation_engine/tests/`; read the modules for what each one covers. Four things about it are not visible from the code:
- **`test_harness_selfcheck.py` exists to prove the winner check is not vacuous** — deliberately-wrong answer keys in `tests/harness_cases/` must NOT match the engine's real result. Don't "fix" a failing harness case; it is supposed to disagree.
- **`test_json_to_yaml_conversion.py` was written for a specific class of breakage** — engine-signature drift, of which the `parse_ballots_from_string` arity bug was the instance. It converts a real export in an isolated tmp dir, so it catches the drift a unit test on the converter would miss.
- **Run from the engine dir**, not the repo root: `pytest tests/test_single_winner_positive.py tests/test_negative_validation.py`.
- **The pre-commit hook is wired by hand and does not survive a fresh clone:**
  `git config core.hooksPath STARVote_LH_tabulation_engine/tools_adam/scripts/git-hooks`

## Git
- **Commit after every significant addition or completed piece of work** (Adam's standing rule), with a real message: a short imperative summary, then a body saying what changed and why. Regenerated `_tabulated` / `_pages` / index files go in the same commit as their source.
- **Several sessions work on this repo at once — prefer a git worktree per session.** In the shared checkout they share one working tree, index and `HEAD`, and even a pathspec commit (`git commit -- <paths>`) takes whatever the pre-commit hook stages. The hook stages only what its own generators changed (`stage_regenerated`, tested by `tests/test_precommit_staging.py`), so a regenerated index reflecting another session's *committed* work may legitimately ride along. Check `git show --stat HEAD` afterwards, and stop on any deletion you didn't make (`git show --diff-filter=D --name-only HEAD`).
- **Re-fetch `origin/master` immediately before committing an entry to a shared index file** — `07_Concepts/GLOSSARY.md`, the `YAML_test_case_index` tables, `PARADOX_index.md`, a folder README's case table. Writing that entry is the last step of whoever built the thing, so a colleague's often lands between your first check and your commit; a worktree hides theirs until they push, which makes this worse, not better.
- **Never rewrite history to unpick a sweep, and never `git stash`.** Report muddled attribution instead; the content is what matters.
- **Transient breakage is usually another session mid-operation** — a held `.git/index.lock` (wait; never delete it), committed files reported as untracked, a sudden flood of hygiene or test failures. Wait for the tree to settle and re-run before "fixing" any of it.
- **`check_repo_hygiene.py` warns about links to files that aren't committed yet** (`check_untracked_link_targets`). CI builds the committed tree, where `mkdocs build --strict` fails on them; if it fires on another session's in-flight files, wait for those to land before pushing.

## When unsure
Consistency matters more than cleverness here. If a terminology or convention
question isn't covered by the `07_Concepts/` docs, ask rather than guess.

---

## Agent operations (Claude-specific)

*Everything below is operational instruction from Adam to Claude — human
contributors can stop reading here.*

### File access (standing permission from Adam)

Adam grants Claude permission to **read, edit, and delete** files anywhere in
this repo's working copy — whether that's the T7 checkout
(`/Volumes/T7/Voting/Larry Hastings/YAML`) or a fresh clone of
`masiarek/star-voting-library`. No need to ask before modifying or removing
files here as part of a requested task. (Note: file *deletion* is also gated by
the app's permission layer, so a new session may still prompt once to enable
it — approve and proceed.)

### Working autonomy (standing instruction from Adam — 2026-07-24)

**Be self-driven. Don't wait for approval.** Adam's words: *"You have very good
sense of direction — I agree with 99%, and even if we go the wrong direction these
are educational materials, mostly. This is not critical code that must be carefully
reviewed. I am reading these pages and coming back to you if I find something
questionable. So please be more self-driven, no need to wait for my approvals."*

So: when you've analyzed a task and have a clear, sensible direction, **just do it** —
build the page, write the case, make the edit, commit, and push. Don't stop to ask
"want me to build this?" or offer a menu of options and wait. **Tell Adam what you
did** (a short summary + what changed), and flag anything genuinely uncertain so he
can spot-check while reading. Adam is the reviewer-after-the-fact, not a gate you
wait at.

Still confirm for the genuinely irreversible / outward-facing (per the safety rules):
creating **permanent public BetterVoting elections** (they can't be deleted — lock
the ballot set first), sending anything on Adam's behalf, or a destructive action you
can't undo. Everything internal to this repo — edits, new pages, deletions, commits,
pushes (standing auth) — proceeds without asking.
