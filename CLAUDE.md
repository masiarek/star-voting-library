# CLAUDE.md — working guidance for this repo

Standing instructions for Claude when working in this project. Prefer the
canonical docs in `00_start_here/` over memory; this file is the index + the
non-obvious house rules.

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
taxonomy from memory:** see `00_start_here/TIPS_terminology.md` and `GLOSSARY.md`.

**Other voting-term canon:**
- **STAR** = Score Then Automatic Runoff (a *score* ballot + that tabulation; the
  same ballot can be Approval / Score / Proportional STAR).
- **Equal Support** is the canonical label for the no-preference runoff bucket
  (matrix legend *and* runoff) — printed **plain**, just "Equal Support". The aka
  (Equal Preference / No Preference) is documented once in `GLOSSARY.md`, **not**
  echoed on every runoff line. Do **not** reintroduce "Equal Preference" as the
  lead term.
- **Favorite Betrayal Criterion ≠ Later-No-Harm** — keep distinct. Neither STAR
  nor IRV is FBC-compliant; RCV-IRV fails it structurally (center squeeze), STAR
  only in rare constructions. See `00_start_here/STAR_Voting/favorite_betrayal_voting_301.md`.
- Spelling: **Bucklin** (not "Buckling"). **Hare ≈ IRV** single-winner, **STV**
  multi-winner. Borda & Bucklin are ranked but **not** Condorcet.

---

## Repo conventions (so output stays consistent)
- **YAML `options:` booleans → `true` / `false`** (parser also accepts t/f/y/n/etc.,
  but house style is the long form).
- **Echo-to-screen `options:` — house default is "less is more."** The on-screen
  echo should be minimal; the saved `_tabulated` copy already renders **maximum
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
- **Echo options = the minimal block + only the section(s) the doc teaches.** When a
  file backs a teaching/reporting `.md` whose embedded echo should show a specific
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
- **Voter counts — keep examples SMALL.** Default to the *fewest ballots* that
  make the point; prefer **individual ballots** (one row per voter, a handful of
  them) over large weighted blocs. A 3-voter example that shows the effect beats a
  100-voter one. Only scale up when a larger electorate is genuinely essential
  (e.g., percentages or proportional seats). When you *do* weight, `Count` values
  must be **≥ 6** (avoid collision with 0–5 scores); scaling all weights ×N
  preserves STAR/proportional winners. See `TIPS_choosing_voter_counts.md`.
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
- **Markers (all tabulate as 0):** `-` blank · `~` race abstention · `&` candidate
  abstention · `?` spoiled · `%` spoiled+reissued. **No `^`** (removed). Approval
  ballots accept only `0`/`1` (+ blank/marker = not approved).
- **Levels (101/201/301)** live ONLY in `00_start_here/CURRICULUM.md`
  (authoritative). Don't tag every file. Example folders stay content-typed
  (`01_STAR/`…`05_Ranked_Robin/`, `method_comparisons/`, `06_Other/`).
- **Where text lives:** per-file context in the YAML (`scenario_description`
  printable, `video_script` = notes, never echoed); cross-file teaching in
  Markdown. No hand-authored `.md` per YAML (the generated pages are the exception —
  see next bullet). See `ORGANIZATION.md`.
- **Folder overview pages are named exactly `README.md`** (not `README_<folder>.md`).
  GitHub only auto-renders a file named `README.md` in a folder's tree view, so each
  folder's landing/overview page **must** be `README.md` — that's what makes the folder
  show a friendly page instead of a bare file list. Keep the descriptive title in the
  file's `# H1` (e.g. `# 01_STAR — single-winner STAR`). A folder may keep *secondary*
  docs under descriptive names (e.g. `README_larry_hastings.md`, `FORK_NOTES.md`), but
  the one overview is always `README.md`.
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
- **`_tabulated`** files are generated into a `<folder>_tabulated/` subfolder
  **nested inside the source file's own folder** (e.g.
  `01_Single_winner/black_curtain/black_curtain_tabulated/`); regenerate by
  re-running the YAMLs after engine changes. They always show full context.
  Loose top-level election files are grouped under a `_main/` subfolder so their
  mirrors nest the same way (`.../_main/_main_tabulated/`). The path is computed by
  `tabulated_output_path` / `aux_tabulated_path` in the engine as
  `p.parent / (p.parent.name + "_tabulated")`.
- **Markdown prose: do NOT hard-wrap paragraphs (Adam's preference).** Write each
  paragraph as a single unwrapped line (soft wrap) — no fixed ~76/80-char line limit. Hard-wrapping is cosmetic: Markdown collapses single newlines inside a paragraph into spaces, so wrapped and unwrapped prose render identically. Keep real line breaks only where they're semantic: blank lines between paragraphs, fenced code blocks, tables, and list items.
- **Embed LH output as text in Markdown (Adam's preference), sized to the election.**
  When a teaching/reporting `.md` discusses a result, paste the actual LH output inline
  as a fenced code block (strip ANSI) rather than only linking the `_tabulated` file —
  the reader should see the output on the page. **Match the depth to the election:**
  - **Small / simple** examples → embed the **short echo** (the on-screen render with
    the file's minimal options), not a full dump.
  - **Large or complex** elections (many ballots/candidates), or docs whose point *is*
    the matrix / Condorcet / score-distribution detail → embed the fuller
    **`_tabulated`** report, or just the specific section being discussed.

  Either way, keep a link to the full `_tabulated` mirror too.
- **BV screenshots live in the case folder's `img/` subfolder, prefixed with the
  BetterVoting election ID** — `img/<bv_id>_<what>.png` (e.g.
  `img/r2pvc9_result_bars.png`, `img/r2pvc9_runoff_pct.png`, `img/r2pvc9_runoff_pie.png`,
  `img/r2pvc9_race_details.png`). The id prefix keeps images traceable and collision-free;
  the `img/` subfolder keeps the lesson folder uncluttered. (PyCharm pastes generic
  `img_N.png` into the folder root; **move into `img/` and rename** to this convention
  when incorporating the case, and give each `![alt](…)` a descriptive caption.)
- **BV-backed teaching cases (e.g. the Runoff Reversal set) → `Runoff_NN_<descriptor>_<bvid>`.**
  Zero-padded sequence (`Runoff_01`, `Runoff_02`, …) for sort order + the teaching
  progression, a short descriptor, and the BetterVoting election id as the final suffix
  for traceability. Each case is a trio: the **two-view lesson** `…_<bvid>.md` (View 1 =
  BetterVoting screenshots, View 2 = the LH text report, plus the ballots), the
  tabulatable `…_<bvid>.yaml`, and the frozen `…_<bvid>_bv_export.json`. Filenames carry
  the order/meaning; the BV id lives on the images, in the filename suffix, and in the
  YAML (`election_description` + the results URL).
- **Cross-reference slides by title** via `00_start_here/LINKS.md`
  short names — never page numbers or `#slide=id…` deep links.
- **Case-file naming.** Two accepted forms; the **bvid is the load-bearing id**
  (unique, stable, traceable by construction — no assignment step needed):
  - **If the election already has a sheet Test ID** (e.g. the older QA rows —
    `bv95a`, `bv130`, `bv1525`), lead with it: `bv<testid>_<bvid>_<descriptor>`
    (e.g. `bv95a_9m6rxr_favorite_survives.yaml`). It sorts with the (retained) QA
    sheet and is findable by ID.
  - **Otherwise (a fresh case with no pre-assigned Test ID)** — DON'T stop to
    assign one; lead with the bvid: `b<bvid>_<descriptor>` (e.g.
    `b26khr3_nota_wins`). The auto-generated repo registry indexes it either way.
  - **LH-only** reference (no BV election) → omit the bvid segment, descriptive name.

  Applies to the whole case group — `.yaml`, two-view `.md`, frozen
  `_bv_export.json`, `_tabulated` mirror. Older cases keep their names; re-align
  only if you're already touching them.
- **Every BV-backed case `.md` links the live BetterVoting results — clickably.**
  When a case has a real BV election, its page must carry a prominent, clickable
  link to the **results** page near the top (not just the bare election id, and
  not only the vote page). House form is a lead line right under the H1/summary:
  `**▶ Live on BetterVoting:** [vote](https://bettervoting.com/<bvid>) ·
  **[results ↗](https://bettervoting.com/<bvid>/results)** (election \`<bvid>\`).`
  Always link `/<bvid>/results` (the tabulated outcome), and mirror it in the YAML
  (`election_description` / a `Live results:` line pointing at the same
  `/results` URL). LH-only references with no BV election skip this.
- **Machine-readable BV fields + the repo registry.** A case `.yaml` may carry
  `bv_test_id`, `bv_election_id`, and `bv_results_url` as top-level fields — the
  tabulation engine ignores them; `tools_adam/scripts/build_bv_registry.py` reads
  them (falling back to the frozen `_bv_export.json` for the true election id, and
  the `bv…` filename for the Test ID) and regenerates
  `00_start_here/YAML_test_case_index/BV_registry.md` + `bv_cases.csv` — a
  sortable, repo-native index (method / winners / candidates / ballots / bvid /
  page / yaml). **The repo registry is canonical for tabulation cases** — the
  `.yaml` (source of truth) + `.md` (writeup) + the auto-generated
  `BV_registry.md` / `bv_cases.csv`. Regenerate it when adding a BV case.
  **No Google-Sheet sync is required for tabulation cases** (decided 2026-07 —
  the auto-registry already does the sheet's job at zero manual cost, and the bvid
  is the case id so there's no Test-ID to assign). The Google Sheet is retained
  **only** for the *extraordinary* non-tabulation QA that has no YAML home — UI,
  roles, archive, casting, "delete a race," video walkthroughs, pass/fail — which
  Adam maintains by hand when he wants to.
- **Creating BetterVoting elections — DON'T do it by hand.** No need to click
  through the BV builder UI (it's slow and fiddly). Use
  `STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py` — a
  uv-run (PEP 723) script that creates elections **and casts ballots** via the BV
  REST API (`POST /API/Elections`, `POST /API/Election/{id}/vote`). Define the
  election(s) — title, candidates, ballots, method, seats — in the script's
  `ELECTIONS` list and run `uv run …/create_bv_test_election.py`; it prints the new
  `bettervoting.com/<id>` URLs. Auth is asymmetric **RS256** (the API requires a
  PEM public key in `auth_key`; the script mints a fresh keypair and signs the
  `custom_id_token` with the private key — no real account credential needed). It
  saves the election object to `_demo_dropbox/`, but that plain GET lacks
  `Ballots`/`Results`; for the **frozen `_bv_export.json`** grab the full export
  from the BV UI (Election + Ballots + Results). Proven end-to-end (BV95a `9m6rxr`,
  BV95b `7pdq3r`). The old API doc's HS256 "secret == user id" trick is **stale** —
  the backend now demands RS256.
  - **BV methods & multi-winner (correction — 2026-07).** BV's seven
    `voting_method` strings are `STAR | STAR_PR | Approval | RankedRobin | IRV |
    Plurality | STV`. There is **no separate "Bloc STAR" string**, but BV *does*
    do bloc multi-winner: its `runBlocTabulator` drives **STAR, Approval,
    Plurality and Ranked Robin** whenever `num_winners > 1`. So **Bloc STAR =
    `STAR` + `num_winners: 3`** and **Bloc Approval = `Approval` +
    `num_winners: 2`**. (An earlier claim that BV couldn't do Bloc STAR /
    multi-winner Approval was WRONG — it can; the pets-governance set is fully
    BV-backable.) Ballot encoding per method: STAR/STAR_PR = scores 0-5;
    Approval/Plurality = 0/1; ranked (IRV/STV/RankedRobin) = **ranks** in the
    score slot (1 = top … 0 = unranked), validated `0..max_rankings`. Multi-race
    elections carry several `races[]`; each voter votes every race — grouped in
    `00_start_here/YAML_test_case_index/multirace_elections.md`.
  - **BV titles are PERMANENT and PUBLIC.** API-created elections can't be
    renamed, closed, or deleted (only a BV admin with DB access can purge them),
    and the title shows on the public results page — so give a real, meaningful
    title on the FIRST create (no "trash/delete/test" junk). The script prepends
    only the `BV<n>` Test ID and runs a pre-check that blocks junk/placeholder
    titles. See `bv_api_election_creation_notes.md` (orphan list included).
  - **Set `owner_id` to your real BV account** (the script default is Adam's
    `ea09e7c7-…`/Admin1) so the elections show up in `/manage`. **But** API-created
    elections are public, listable, and exportable **only** — they are **NOT
    UI-administrable** (you can't edit/close/**delete** them from `/admin`): BV
    authorizes admin off a server-side role binding written only by the
    authenticated create flow, not off `owner_id`/`admin_ids` (setting `admin_ids`
    is a proven no-op). Full write-up + a ready-to-file BV issue:
    `00_start_here/tabulation_engines/BV/bv_api_election_creation_notes.md`.

## Workflow — building a BV-backed test case

The loop that's working well (**Adam** = human, **AI** = assistant):

1. **Brainstorm in `trash_delete.yaml`** (AI + Adam). Draft the scenario —
   candidates, ballots, method, seats — in the scratch file and tabulate it with
   the LH engine until it demonstrates the intended behavior (a tie rung, a
   method divergence, a criterion failure…). Nothing here is permanent; iterate
   freely, keep examples small.
2. **Go / no-go** (Adam decides). If the scenario earns its keep, promote it to a
   real case; otherwise it stays scratch / gets discarded.
3. **Create the BV election** (AI runs it; Adam must be signed in to BV). Add the
   election(s) to `create_bv_test_election.py`'s `ELECTIONS` list and
   `uv run …/create_bv_test_election.py` — it creates the election **and casts the
   ballots** via the API and prints `bettervoting.com/<id>`. Never build it by
   hand in the UI. (Auth is asymmetric RS256; no real credential is stored.)
4. **Export the full JSON** (Adam). The API GET returns only the election *config*,
   so export the full **Election + Ballots + Results** from the BV UI and drop it
   in `_demo_dropbox/`.
5. **Reproduce in LH** (AI). Convert/import the export into a `.yaml` (converter:
   `YAML_library/1_positive/01_convert_json_yaml.py`); for a random tie-break, pin
   `lot_numbers` to BV's `perm`. Confirm LH's winner(s) match — or characterize the
   divergence. Freeze the export as `_bv_export.json`.
6. **Build the case files** (AI). Name `bv<testid>_<bvid>_<descriptor>.{yaml,md,
   _bv_export.json}` (see naming rule above). The `.md` is the per-election page:
   the clickable `▶ … /results` lead line, ballots, the **inline LH tabulation
   echo**, why the winner wins, and the BV-vs-LH agreement/divergence.
   `expected_winners` goes in the yaml.
7. **Regenerate indexes + mirrors** (AI). Run the yaml through the engine (writes
   its `_tabulated` mirror), then `tools_adam/scripts/build_yaml_index.py`, the
   folder `README.md` table, and `build_divergence_index.py` if it diverges.
8. **Verify + commit** (AI). The pre-commit hook runs the STAR suite + repo-hygiene;
   commit with a descriptive message. **Adam pushes** (the sandbox has no push
   credentials — always hand Adam the `git push https://github.com/masiarek/YAML.git
   master` line).
9. **Registry regenerates itself** (AI). `build_bv_registry.py` writes
   `BV_registry.md` + `bv_cases.csv` from the case's `bv_*` fields — that's the
   canonical tracker. **No Google-Sheet update is required for tabulation cases**
   (decided 2026-07). Only ding Adam to touch the sheet for an *extraordinary*
   non-tabulation QA case (UI / roles / archive / casting / video) that has no YAML.

**LH-only cases** (no BetterVoting election — e.g. a reproduction of a Larry
`starvote` test file) skip steps 3–4 and the `<bvid>` filename segment; everything
else is the same.

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
  result can't be frozen). Worked: `00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md`.
- `06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py` — vendored pyrankvote; reads
  ranked (`A>C>B`) or score ballots.
- `abcvoting_tabulation_engine/abc_tabulation.py` — multi-winner Approval (ABC)
  rules via Martin Lackner's `abcvoting` (optional `pip install abcvoting`;
  everything guards on it). `av` doubles as an independent cross-check of the
  LH bloc-Approval count; `seqpav` / `pav` / `seqphragmen` add the proportional
  rules the LH engine doesn't have. Tested by `tests/test_abcvoting_crosscheck.py`
  (skips if the library is absent).
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
question isn't covered by the `00_start_here/` docs, ask rather than guess.
