# CLAUDE.md — working guidance for this repo

Standing instructions for Claude when working in this project. 

## What this is
A **STAR Voting education** repo built on a fork of Larry Hastings' `starvote`
(single-winner STAR engine + extra reporting), plus a vendored RCV-IRV engine,
example YAML elections, teaching docs, and Larry↔Adam conversation scripts.
Audience: voters, presenters, and debaters learning/teaching STAR.

---

## File access (standing permission from Adam)

Adam grants Claude permission to **read, edit, and delete** files anywhere under
`/Volumes/T7/Voting/Larry Hastings/YAML` (this repo). No need to ask before
modifying or removing files here as part of a requested task. (Note: file
*deletion* is also gated by the app's permission layer, so a new session may
still prompt once to enable it — approve and proceed.)

---

## Working autonomy (standing instruction from Adam — 2026-07-24)

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
  only in rare constructions. See `01_STAR/concepts/properties_and_limits/favorite_betrayal_voting_301.md`.
- Spelling: **Bucklin** (not "Buckling"). **Hare ≈ IRV** single-winner, **STV**
  multi-winner. Borda & Bucklin are ranked but **not** Condorcet.

---

## Repo conventions (so output stays consistent)
- **YAML `options:` booleans → `true` / `false`** (parser also accepts t/f/y/n/etc.,
  but house style is the long form).
- **On-screen report `options:` — house default is "less is more."** The on-screen
  on-screen report should be minimal; the saved `_tabulated` copy already renders **maximum
  info automatically** (engine forces every analysis on, regardless of the file's
  options — don't hand-set that). Single-winner default block:

  ```
  options:
    show_description: false
    show_matrix: true
    matrix_finalists_only: true
    show_condorcet: false
    show_score_counts: false
    show_irv: false
    show_runoff_percent: true
    brief: true
    collapse_ballots: true
    count_separator: "×"
  ```

  (`show_runoff_percent: true` is in the *minimal* block on purpose — the
  self-reconciling runoff line is a compact, broadly-useful two-line summary, worth showing on
  almost any single-winner result. The *engine* default remains `false`; this is the
  house recommendation for YAML files.)

  **Multi-winner** uses the same block but with `show_matrix: false` and
  `matrix_finalists_only: false` (a "Top 2 Finalist" matrix is a single-winner
  concept and prints misleadingly for PR/Bloc). **Exceptions:** the options-demo
  files (`04b_…display-options-all`, `display_options_demo`, and the engine's
  `options_examples` reference) keep their illustrative
  all-on settings — they exist to showcase options; and **two-candidate intro
  files set `show_matrix: false`** — with only two candidates the finalists matrix
  is trivial (it just echoes the runoff). The `[Divergence from STAR]`
  block prints whenever methods differ regardless of these flags, so comparative
  demos keep their punch on screen even with the minimal block.
- **On-screen report options = the minimal block + only the section(s) the doc teaches.** When a
  file backs a teaching/reporting `.md` whose embedded on-screen report should show a specific
  section, flip ON *just that flag* (keep everything else minimal; the `_tabulated`
  mirror still forces full detail). `show_runoff_percent` is already on in the minimal
  block, so the per-doc triggers are the heavier sections:
  - score-distribution shape → `show_score_counts: true`
  - full pairwise grid / Condorcet → `matrix_finalists_only: false` and/or `show_condorcet: true`
  - RCV-IRV divergence → `show_irv: true`
  - a plain result with no section to feature → leave the minimal block as-is
    (which already shows the runoff line).

  Ballot display: **`collapse_ballots: false`** when each ballot is a distinct teaching
  case (small, one row per voter — e.g. the abstention cases); **`true`** otherwise.
  Example: `flat_scores_abstention_c3_b8` teaches abstentions + score distribution +
  the runoff denominator, so it sets `show_score_counts: true` and
  `show_runoff_percent: true` but leaves `show_condorcet: false` /
  `matrix_finalists_only: true` (the full matrix/Condorcet is the matrix page's job and
  lives in the mirror).
- **`show_description`**: per the block above, default `false` (clean demo —
  description stays in the file and the always-full `_tabulated` copy, hidden on
  screen). Flip to `true` only for a deliberate study/reference render.
- **`show_runoff_percent`**: *engine* default `false`, but **on in the house minimal
  block** — it's a compact, broadly-useful two-line summary, worth showing on almost any
  single-winner result. When `true`, prints a two-line, **self-reconciling** runoff
  summary under the Automatic Runoff winner — e.g.
  `Voters with a preference: 363 of 461 (98 Equal Support). Dog 190 (52%) vs Cat 173
  (48%); majority = 182` — using the **decided-voters** denominator (Equal Support
  excluded) but stating it against the total ballots with the Equal Support gap named
  inline, so the denominator never has to be inferred. The always-full `_tabulated`
  copy forces it on AND expands it into a "Runoff math" funnel (`461 − 98 = 363`,
  majority) — don't hand-set that. The wording/funnel are locked by
  `tests/test_runoff_percent.py`; change them together.
- **`show_smith_set`** (Ranked Robin only): same contract as `show_runoff_percent` —
  engine default `false` on screen, **always forced on in the `_tabulated` mirror**.
  Prints the **Smith set** (the smallest group whose every member beats every
  candidate outside it), says whether that's a lone Condorcet winner, a top cycle or
  an all-draws **dead heat**, and whether the winner landed inside it. The dead-heat /
  cycle branch shares one predicate (`_all_pairs_draw`) with the Ranked Robin winner
  line, so the two lines can't contradict each other — keep it that way. Deliberately separate from `show_matrix`
  so a file can opt the echo into one without the other, and **not** in the house
  minimal block (the mirror already carries it). **RCV-IRV mirrors get the same block
  automatically** (no option — the IRV path has no options plumbing). The two uses are
  opposite: RR is Smith-efficient so the block is descriptive; RCV-IRV is not, so it's
  a genuine pass/fail. Wording locked by `tests/test_smith_set.py`; concept page
  `07_Concepts/topics/smith_set.md`.
- **Voter counts — keep examples SMALL.** Default to the *fewest ballots* that
  make the point; prefer **individual ballots** (one row per voter, a handful of
  them) over large weighted blocs. A 3-voter example that shows the effect beats a
  100-voter one. Only scale up when a larger electorate is genuinely essential
  (e.g., percentages or proportional seats). When you *do* weight, `Count` values
  must be **≥ 6** (avoid collision with 0–5 scores); scaling all weights ×N
  preserves STAR/proportional winners. See `07_Concepts/tips/TIPS_choosing_voter_counts.md`.
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
- **One door per voting method (reorganized 2026-07-29).** A method's concept
  pages live **inside that method's folder**, under `concepts/` —
  `01_STAR/concepts/` (incl. `concepts/reporting/`), `03_STAR_PR/concepts/`,
  `04_Approval/concepts/`, `05_Ranked_Robin/concepts/`,
  `06_Other/RCV_IRV/concepts/`, `06_Other/Range/concepts/`. The folder's
  `README.md` is that method's **start-here** (what it is → its concepts → its
  runnable examples). They previously lived in a parallel `07_Concepts/<Method>/`
  tree, which gave each method two competing front doors. **`07_Concepts/` is now
  cross-method only** (topics, paradoxes, scores_and_ranks, curriculum, glossary,
  engines, tips, books) — don't put method-specific pages back into it.
  **Moving concept pages again?** Use
  `tools_adam/scripts/migrate_concept_links.py` (resolves relative links per
  source file — a blind string replace corrupts them), run it **before** the
  `git mv`, and add a `redirect_maps` entry per moved page. Those redirects are
  **permanent**: published URLs are quoted in BetterVoting election descriptions
  that can never be edited, so a deleted redirect is an unfixable 404.
- **Where text lives:** per-file context in the YAML (`scenario_description`
  printable, `video_script` = notes, never shown on screen); cross-file teaching in
  Markdown. No hand-authored `.md` per YAML (the generated pages are the exception —
  see next bullet). See `07_Concepts/about_this_repo/03_ORGANIZATION.md`.
- **Folder overview pages are named exactly `README.md`** (not `README_<folder>.md`).
  GitHub only auto-renders a file named `README.md` in a folder's tree view, so each
  folder's landing/overview page **must** be `README.md` — that's what makes the folder
  show a friendly page instead of a bare file list. Keep the descriptive title in the
  file's `# H1` (e.g. `# 01_STAR — single-winner STAR`). A folder may keep *secondary*
  docs under descriptive names (e.g. `README_larry_hastings.md`, `FORK_NOTES.md`), but
  the one overview is always `README.md`.
- **The repo publishes as a searchable website** — <https://masiarek.github.io/star-voting-library/>,
  built by root `mkdocs.yml` (MkDocs Material + `mkdocs-same-dir` + `mkdocs-redirects`)
  straight from the
  repo's own Markdown (no `docs/` copy; `.yaml` / `_tabulated` files carried through)
  and deployed by `.github/workflows/docs.yml` on every push to master. Folder
  `README.md`s become the site's section index pages (one more reason that naming rule
  matters), and links keep GitHub's file-relative semantics (`use_directory_urls:
  false` — don't flip it). Local preview: `uvx --with mkdocs-same-dir --with
  "mkdocs-material>=9.5" --with mkdocs-redirects mkdocs serve`. `site/` is generated
  output — never commit.
  Details + known nits: `07_Concepts/about_this_repo/05_website_build.md`.
  **Site-only redirects (`redirects.redirect_maps` in `mkdocs.yml`) — use sparingly.**
  They replace the *built* page at a URL while leaving the `.md` on disk intact, so
  GitHub still renders the source but **the site never shows it**. Live case:
  `05_Ranked_Robin/README.md` → `05_Ranked_Robin/concepts/ranked_robin.md`, because
  the case folder is a top-level nav section and is where visitors land wanting "Ranked
  Robin," but the page that *teaches* the method is the concept page. Whenever you add a
  redirect, **move or mirror whatever the source said onto the destination** (here the
  case index is mirrored under "Worked examples" on `ranked_robin.md`) and leave a
  maintainer note in the redirected README — otherwise edits there silently never ship.
  Adding a plugin means updating **four** places: `mkdocs.yml` plugins, the preview
  command in its header comment, `.github/workflows/docs.yml`'s `pip install`, and
  `website_build.md`.
- **Companion repo — research-paper topics live OUTSIDE this repo.**
  <https://github.com/masiarek/star-voting-research-topics> (**private**) holds the
  vetted research-paper prospectuses that use this library as their reproducibility
  artifact — one `topics/NN_<slug>.md` per topic, plus a `README.md` slate table.
  Each topic page follows a fixed structure: status/venues/supporting-library header,
  Abstract, Research question, Methodology, Literature gap and closest prior work,
  Cautions and framing corrections, Supporting assets in star-voting-library (links
  into *this* repo at `blob/master/…`), Execution sketch. Topics 1–5 were produced by
  a 12-agent workflow (2026-07-24) and each passed a five-agent **adversarial novelty
  check**; anything added later must state its vetting level honestly rather than
  inherit that badge (topic 6, the metric distortion of STAR, started with a
  *preliminary* check and passed the full five-agent protocol on 2026-07-26 —
  its status line records the run and the residual caveats). **Don't search this repo for research topics —
  they aren't here**; clone the companion, match the house structure, update the
  README slate table, and keep the two repos pointing at each other. Working the
  other direction: when a teaching page states an open gap in print (as
  `topics/distortion.md` does for STAR's missing distortion bound), that's exactly
  the raw material for a new topic page.
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
- **Link key terms on first meaningful use — with restraint** (a gentle habit, not
  an enforced gate). The first time a page uses a *jargon* term that has a canonical
  home (a `topics/` hub, a concept page, or a `GLOSSARY` entry) — Condorcet
  winner/loser, center squeeze, monotonicity, later-no-harm, favorite betrayal,
  Equal Support, exhausted ballots, mutual majority, VSE, summability, Copeland /
  Ranked Robin, spoiler effect, the impossibility theorems — link it there so a
  newcomer can click through. But follow the overlinking discipline: (1) link to
  *aid*, not decorate — skip common words and what the audience plainly knows;
  (2) **never self-link** the page's own subject; (3) link a term **once** per page,
  not every occurrence; (4) prefer the **topic hub** if one exists, else the concept
  page, else the glossary; (5) **in a parallel list, link all or none** — when a
  bullet list, table column, or run-on sentence names several methods side by side
  (STAR · RCV-IRV · Ranked Robin · Plurality), linking only some of them reads as
  arbitrary even when each individual choice was defensible. Decide once for the
  whole list. (Rule 3 still wins: a term already linked earlier on the page stays
  unlinked, and the list is consistent *because* of that, not in spite of it — say
  so in the commit if it looks uneven.) When in doubt, fewer links read better than
  a wall of blue. (Not machine-checked — the failure mode is over-linking, not
  under-linking; rule 5 is the exception, where the failure mode is *partial*
  linking, and only a human reading the rendered page will catch it.)
- **Case-folder layout — README-alone, sources in `cases/` (repo standard, 2026-07-20).**
  In a teaching case folder, the **source files (`.yaml`, `_bv_export.json`) live in a
  `cases/` subfolder**, and only the `README.md` (plus any hand-authored teaching `.md`)
  sits at the folder top — so opening the folder shows the *explanation*, not a wall of
  data. Because the engine derives output paths from the yaml's parent
  (`p.parent / (p.parent.name + "_tabulated")`, and the parent is now `cases`), the
  generated **`_tabulated`** mirrors and built **`_pages`** nest *inside* `cases/` as
  **`cases/cases_tabulated/`** and **`cases/cases_pages/`** (e.g.
  `method_comparisons/black_curtain/cases/cases_tabulated/`). Regenerate mirrors by
  re-running the YAMLs; pages via `build_yaml_pages.py`; both always show full context.
  **New case folders follow this** (README at top, sources in `cases/`). Folders
  **without** a `README.md` keep the flat layout (yamls at top — e.g. the `jfk7pd` /
  `three_way_dead_rung_tie` sub-cases, `split_voting/_main`); **engine/tool folders and
  test-fixture folders (`2_negative`, `harness_cases`) are never reorganized.** Test
  discovery and `discover()` glob both `*.yaml` and `cases/*.yaml`, so either layout works.
- **Markdown prose: do NOT hard-wrap paragraphs (Adam's preference).** Write each
  paragraph as a single unwrapped line (soft wrap) — no fixed ~76/80-char line limit. Hard-wrapping is cosmetic: Markdown collapses single newlines inside a paragraph into spaces, so wrapped and unwrapped prose render identically. Keep real line breaks only where they're semantic: blank lines between paragraphs, fenced code blocks, tables, and list items.
- **Embed LH output as text in Markdown (Adam's preference), sized to the election.**
  When a teaching/reporting `.md` discusses a result, paste the actual LH output inline
  as a fenced code block (strip ANSI) rather than only linking the `_tabulated` file —
  the reader should see the output on the page. **Match the depth to the election:**
  - **Small / simple** examples → embed the **short on-screen report** (the on-screen render with
    the file's minimal options), not a full dump.
  - **Large or complex** elections (many ballots/candidates), or docs whose point *is*
    the matrix / Condorcet / score-distribution detail → embed the fuller
    **`_tabulated`** report, or just the specific section being discussed.

  Either way, keep a link to the full `_tabulated` mirror too.
  - **Route the short snippet to the full report (Adam likes the long LH reports).** When a
    hand-authored teaching page embeds a *short* on-screen snippet **and the example is a real
    case file**, add a one-click pointer to that case's **full generated page**
    (`…/cases_pages/<stem>.md`, which carries the matrix / Condorcet / score-distribution audit)
    or its `_tabulated` mirror — e.g. *"Want the whole count? see the full LH report → `…/cases_pages/<stem>.md`."* Keep
    the crisp snippet for the lesson; the full report stays one click away and never drifts (the
    link auto-updates; a pasted long report would go stale). **Skip this for *generic
    illustrations*** (invented candidates with no backing case file) — a "full report" link there
    is a dead end. Prefer the generated page over pasting the long report inline on a teaching
    page, which buries the lesson (e.g. the runoff page is *about* the reversal, not the matrix).
- **Cross-reference slides by title** via `07_Concepts/LINKS.md`
  short names — never page numbers or `#slide=id…` deep links.
- **Case-file naming.** **LH-only** cases (no BV election) → descriptive name, no bvid
  segment. **BV-backed** cases lead with the bvid — `b<bvid>_<descriptor>`, or
  `bv<testid>_<bvid>_<descriptor>` when a sheet Test ID already exists; details in the
  **`bettervoting` skill**. Applies to the whole case group — `.yaml`, `.md`, frozen
  `_bv_export.json`, `_tabulated` mirror. Older cases keep their names; re-align
  only if you're already touching them.
- **BetterVoting (BV) work → load the `bettervoting` skill.** Everything BV-specific lives
  there and loads on demand: minting with `create_bv_test_election.py` / `bv_election_specs.py`,
  fetching exports with `fetch_bv_export.py`, screenshots in `img/<bvid>_<what>.png`, the
  clickable `/results` lead line, the BV→repo description backlink, the `BV<n>` collision
  rule, `BV_registry.md` regeneration, and BV's method strings + bloc multi-winner.
  **Read it BEFORE creating or fetching any BV election** — BV titles, descriptions and
  numbers are PERMANENT and unfixable, so those rules have to be right the first time.

## Scratch drafting (any method)

Draft new scenarios in `trash_delete.yaml` and tabulate until the behavior shows (a tie
rung, a method divergence, a criterion failure…). Nothing there is permanent; iterate
freely, keep examples small. **Two gotchas:** there is **no separate `candidates:` key** —
the **first line of the `ballots:` block is the candidate header**, comma-separated; and
weighted rows use a `Count:` header (`Count:Ada,Ben,Cara` then `15:5,2,0` per bloc).

```yaml
title: Scratch (delete me)
voting_method: STAR
num_winners: 1
options:            # house minimal block — see "Repo conventions"
  show_runoff_percent: true
  brief: true
ballots: |-
  Ada,Ben,Cara
  5,2,0
  0,4,5
  2,5,4
expected_winners: [Ben]
```

Tabulate with `.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py trash_delete.yaml`.
The run writes `_tabulated` mirrors into a sibling `<parentdir>_tabulated/` folder — for a
scratch file at the repo root that's a junk `YAML_tabulated/` directory; **delete it (and
the scratch files) when done, never commit them.**

**Promoting a scratch case to a real one:** LH-only cases (no BetterVoting election — e.g.
a reproduction of a Larry `starvote` test file) go straight to case files + `_tabulated`
mirror + indexes + commit. For a **BV-backed** case, the full nine-step mint/freeze/
reproduce loop is in the **`bettervoting` skill**.

## Engines
- `STARVote_LH_tabulation_engine/starvote_larry_hastings.py` — STAR + Bloc/
  proportional; reporting options; `blocs:` vote-splitting check; quorum;
  `[Divergence from STAR]` comparison; optional `show_runoff_percent` runoff
  summary line (decided-voters denominator; forced on in `_tabulated`).
  Auto-dispatches to RCV-IRV / Approval / **Ranked Robin** by `voting_method`, or
  to RCV-IRV when ballots contain ranked `>` (comments with `->` are ignored).
  **Ranked Robin (RCV-RR / Copeland)** is first-class: `voting_method: RankedRobin`
  (aliases `RCV_RR` / `Copeland` / `Consensus`) prints the round-robin report
  (ballots + pairwise table + win-loss record), flags a Condorcet cycle, and
  writes its `_tabulated` mirror — it does **not** fall through to the IRV rounds.
  **Bloc RR (multi-winner):** `num_winners > 1` now elects the **top-N by record**
  (most wins → margin → lot), printing a seats list and flagging a lot-decided
  last seat — it no longer silently downgrades to one winner. **Multi-winner
  Plurality = SNTV / Bloc Plurality** (`run_plurality_multi`): `Plurality` +
  `num_winners > 1` elects the top-N by first-choice count (ties → lot);
  single-winner Plurality still routes through the STAR path. So LH multi-winner
  coverage is now complete for BV's bloc set: STAR→**Bloc STAR**,
  Approval→**Approval_Multi_Winner**, RankedRobin→**Bloc RR**, Plurality→**SNTV**,
  plus STV and STAR_PR/allocated/sss/rrv. (The old "LH has no Plurality" caveat is
  retired — single-winner via STAR path, multi-winner via SNTV.)
  **RR triple-check:** cross-verify RR cases three ways — this native tally,
  BetterVoting's `RankedRobin.ts` (the frozen `_bv_export.json` Results), and
  `pref_voting`'s independent Copeland via
  `tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py` (declared in
  `pyproject.toml`; `uv sync` then `uv run …`). **Tiebreak caveat — LH and BV
  diverge:** LH breaks a Copeland tie by margin → **lot** (deterministic); BV by
  head-to-head → **random**. So a tie-deciding case is **LH-only** (a random BV
  result can't be frozen). Worked: `05_Ranked_Robin/concepts/rr_tiebreak_lh_vs_bv.md`.
- `06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py` — vendored pyrankvote; reads
  ranked (`A>C>B`) or score ballots.
- `06_Other/abcvoting_tabulation_engine/abc_tabulation.py` — multi-winner Approval (ABC)
  rules via Martin Lackner's `abcvoting` (optional `pip install abcvoting`;
  everything guards on it). `av` doubles as an independent cross-check of the
  LH bloc-Approval count; `seqpav` / `pav` / `seqphragmen` add the proportional
  rules the LH engine doesn't have. Tested by `tests/test_abcvoting_crosscheck.py`
  (skips if the library is absent).
- **Score / range voting & the 0–5 cap (don't misstate this).** Larry's underlying
  `starvote` engine is *range-parametric*: `starvote.election(starvote.star, rows,
  maximum_score=N)` tabulates any range (verified at 0–10 → C). The **0–5 limit is the
  fork's teaching guardrail, NOT an engine limit** — `validate_star_rows(…,
  max_score=5)` in `starvote_larry_hastings.py` (def ~L2239, called with `max_score=5`
  ~L2366) rejects scores >5 on the YAML-CLI path because STAR ballots are 0–5 by
  convention; it's a single adjustable arg. **Pure Score / Range IS tabulable** — via
  `pref_voting.grade_methods` (`score_voting` = mean, `greatest_median` = the median
  variant, plus `star` / `approval` / `majority_judgement`), `starvote`'s RRV
  (`Reweighted_Range_Voting`, range-based PR), and the sim/divergence tools
  (`06_Other/simulations/star_vs_approval_divergence.py`, `tools_adam/find_divergence.py`)
  which compute the score-total winner. The STAR **Scoring Round** output is itself the
  score tally (the Score-Voting winner = whoever leads the scoring round before the
  runoff). What's absent is only a first-class `voting_method: Score` on the teaching
  CLI — **capability is not the blocker.**
- Quick checks can use system `python3` (engines are vendored); the user runs via
  their `.venv` / `uv`.
- The engine errors *clearly* (no tracebacks) for the common mistakes: bad YAML,
  no `ballots:` block / old nested schema (prints the key-components template),
  wrong column counts, invalid chars / out-of-range scores, ranked ballots under a
  score method, and method/seats mismatches. Missing `voting_method` / `num_winners`
  is a non-fatal NOTE (defaults to STAR / 1). Generated `_tabulated.txt` files are
  refused as input.

## Tests
- `STARVote_LH_tabulation_engine/tests/test_single_winner_positive.py` — every
  single-winner STAR file with `expected_winners` (in `01_STAR/`, `method_comparisons/`,
  `YAML_library/1_positive/`) is run through the CLI (which also
  writes its `_tabulated` copy) and checked for exit 0 + correct winner.
- `…/tests/test_harness_selfcheck.py` — meta-tests proving the winner check isn't
  vacuous: deliberately-wrong answer keys (single- and multi-winner) in
  `tests/harness_cases/` must NOT match the engine's real result.
- `…/tests/test_json_to_yaml_conversion.py` — guards the BetterVoting-JSON →
  YAML pipeline (`YAML_library/1_positive/01_convert_json_yaml.py`): converts a
  real export in an isolated tmp dir and checks the produced YAML tabulates to the
  embedded winners (catches engine-signature drift like the `parse_ballots_from_string`
  arity bug).
- `…/tests/test_negative_validation.py` — malformed fixtures (in `tests/negative_cases/`
  **and** the migrated `YAML_library/2_negative/`) must exit 1 with the right
  message and no traceback; covers single messages and multiple-errors-in-one-file.
- Run: `pytest tests/test_single_winner_positive.py tests/test_negative_validation.py`
  from the engine dir. A repo pre-commit hook (`STARVote_LH_tabulation_engine/tools_adam/scripts/git-hooks/`, wired via
  `git config core.hooksPath STARVote_LH_tabulation_engine/tools_adam/scripts/git-hooks`) runs these on every commit.

## Git
- **Commit after every significant addition or completed piece of work** (Adam's
  standing rule) — don't leave finished work sitting uncommitted. Write a real
  commit message: short imperative summary line, then a body listing what
  changed and why. Include regenerated `_tabulated`/`_pages`/index files in the
  same commit as their source changes.

## When unsure
Consistency matters more than cleverness here. If a terminology or convention
question isn't covered by the `07_Concepts/` docs, ask rather than guess.
