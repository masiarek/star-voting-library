# TODO — BV-migrate the ballot-style lab (+ parked backlog from 2026-07-17)

Working notes to pick up later. Not site content (excluded in `mkdocs.yml`). Delete sections as they're done.

## 1. The headline task: take the ballot-style lab live on BetterVoting — ✅ DONE (2026-07-24, commit `895a65c`)

All ten cases migrated and BV==LH verified (winners fetched via `/API/ElectionResult`):

| case | Test ID | bvid | method | BV = LH |
|---|---|---|---|---|
| 01 graders-divide | BV2234 | `4jmgrd` | STAR | Clara |
| 02 cliff-city | BV2235 | `fm8cbv` | STAR | Churro |
| 03 bullet-storm | BV2236 | `w9f4vd` | STAR | Carla (runoff tie → score tiebreak; BV agrees) |
| 04 noise-soup | BV2237 | `74pbyg` | STAR | Caleb |
| 05 squeeze-survives | BV2238 | `td7jfy` | STAR | Ben |
| 06 narrow-bands | BV2239 | `gyv2qt` | STAR | Beige (scoring tie → head-to-head; BV agrees) |
| 07a herb-bloc | BV2244 | `9dx494` | Bloc STAR 3 | Basil, Chive, Dill (the 83–82 rung; BV agrees) |
| 07b herb-PR | BV2245 | `pmrq4q` | STAR_PR 3 | Anise, Basil, Chive (LH `allocated` == BV `STAR_PR`) |
| 08 quota-circus | BV2246 | `qdh9qp` | STAR_PR 2 | Amir, Bree |
| 09 park-bloc | BV2247 | `v9rhhr` | Bloc STAR 4 | Aspen, Cedar, Dogwood, Elm |

Resolved cautions: **07a's 83–82 rung resolves deterministically on BV** (Dill, by scoring-round score) — migrated, not LH-only. **No case turned out BV-random**; BV's STAR tiebreaker and STAR-PR both matched LH, so all ten are BV-backed. The spurious STAR_PR "Tied!" banner is cosmetic (seats compute correctly). No STV races, so the sole-survivor crash didn't apply.

Method note: minting was done with a standalone driver (`scratchpad/mint_lab.py`) that builds each spec straight from the frozen yaml via the engine's parser (BV ballots provably == LH), calling `create_bv_test_election.create()` directly — no edits to the shared `bv_election_specs.ELECTIONS`.

**Orphans (disclosed in `bv_api_election_creation_notes.md`):** the four multi-winner cases were first minted single-winner because the driver read the raw `num_winners:` key instead of the engine-normalized `seats:` — undeletable wrong-seat elections `6btm9k`/`g6x8b9`/`f2vtc9`/`xm93tw` (titled BV2240–2243), superseded by the correct BV2244–2247.

## 2. Loose ends from the 2026-07-17 session (BV2203–BV2210 + Burlington)

- ~~**Push**~~ — done (verified 2026-07-23: local master == GitHub master @ `5fd470c`).
- **File the STV crash issue** on Equal-Vote/bettervoting — ready-to-file text sits in [06_Other/STV/bv_stv_sole_survivor_crash/README.md](06_Other/STV/bv_stv_sole_survivor_crash/README.md).
- ~~**Freeze UI exports**~~ — done (2026-07-23), and the whole step is now AUTOMATED: new `tools_adam/fetch_bv_export.py` reproduces the UI's "Download JSON" via three anonymous GETs (`Election` + `anonymizedBallots` + `ElectionResult`; verified byte-equivalent on `vqyqkr`), and `create_bv_test_election.py` auto-freezes after casting. All eight frozen into their case folders: `7mckyg`, `b6xrdr` (FBC pair) · `7q6by8`, `fxhw6g` (burial pair) · `fvg8y8` (food-truck row, one shared export) · `39py93` (STV control) — every BV winner matches its yaml's `expected_winners`. The crashers `gvtg2h`/`8xwx43` froze `--without-results` (ElectionResult still HTTP 500 as of 2026-07-23); **re-fetch those two with `--force` once BV ships the STV fix.**
- ~~**divergence_review builder nit:**~~ DONE (2026-07-24, commit `447eeb9`). Root cause was in `classify()`, not just the text: the `IRV_DIFFERS_ARTIFACT` guard fired on `irv_diff and (tie_ballots or irv_fragile)` before testing whether RR still sided with STAR, so 8 of 16 artifact cases had RR/Condorcet actually siding with IRV yet printed "Ranked Robin and Condorcet agree with STAR." Added `and not rr_diff` (the artifact story needs IRV to have moved *alone*); the 8 reroute to STAR_OUTLIER_RR_WITH_IRV (5) / CYCLE_OR_THREE_WAY (3) with accurate existing text, and the remaining artifact explanation now reads the real Condorcet value (says "no Condorcet winner — cycle" for the C=None cases).
- Recorded, no action needed: the burial pair's **live BV descriptions** carry a wrong slim-vs-blowout aside (permanent); corrected analysis lives in the repo yamls + `05_Ranked_Robin/burial/README.md`.

## 3. Parked proposal backlog (from the kick-the-tires menu, unbuilt)

Each line is meant to be enough to start cold. Rough priority within groups.

**Criterion cases (BV-backable pairs unless noted):**

- **STAR fails mutual majority** — a solid 60% coalition over {A, B} splits its scores and C wins; the honest "IRV beats STAR on this criterion" case. No mutual-majority case exists anywhere in the repo.
- **STAR elects outside the Smith set** — the score round promotes a candidate the whole top cycle beats; repo has zero Smith-set cases.
- **Reversal symmetry** — flip every ballot; IRV can elect the *same* winner both directions ("the favorite and least-favorite are the same person"). New paradox-tag candidate for the index.
- **The IRV "majority" asterisk** — a winner whose final-round "majority" is under 50% of ballots *cast* (exhaustion). Targets the exact sentence "IRV guarantees a majority winner"; sits beside `bv2183`.
- **STAR exaggeration pair** — same opinions, honest 0–5 vs everyone min-maxing (collapses to approval-style); what strategy buys and costs in STAR. Pairs with ex13.

**Multi-winner wing (deepens ex12/ex14 + food_truck_row):**

- **STV vs STAR-PR electing *different* sets from the same opinions** — two proportional methods disagreeing about what proportionality means; lead with the same-opinion line-up table.
- **Droop rounding at 3 seats, 60/40** — do both PR methods give 2–1?
- **Free-riding in STAR-PR** — a voter deflates a sure-winner's score to boost their second pick; the PR-world strategy nobody demos.
- **Multi-winner tie shelf (LH-only)** — STV bottom-two elimination tie, STAR-PR final-seat tie, Bloc final-seat tie; document LH's deterministic lot vs BV's random (extends the tie-ladder shelf into multi-winner, currently empty).

**Real elections (PrefLib pipeline proven by Burlington — see memory note + `method_comparisons/burlington_2009/`):**

- **Alaska 2022 special** — the Burlington sibling: center squeeze + non-monotonicity + no-show on real ballots (Graham-Squire & McCune, arXiv:2301.12075); worked prose already in `favorite_betrayal_voting_301.md` §4, needs the runnable case.
- **Eurovision** — public jury/televote data is literal score voting; a real, familiar election for the STAR intro shelf.

**Engine robustness (cheap LH negative/edge tests):**

- `num_winners` ≥ candidate count; a 1-candidate election; an all-abstain electorate; duplicate candidate names; CJK/emoji names vs report column alignment; equal-ranks input `A>B=C` (pin: clear error or support); a case exercising the `%` spoiled-and-reissued marker end-to-end.

**Tooling:**

- **Cross-engine agreement fuzzer** — random small elections through LH vs `pref_voting` (same method: STAR, IRV, Copeland), diff winners; any disagreement is a tiebreak-policy doc item or a real bug. Industrializes the RR triple-check; extends the existing `find_divergence` miners (which hunt cross-*method*, not cross-*engine*).

## 4. Library-improvement survey findings (2026-07-23)

From a repo-wide improvement survey. Verified items were checked by hand this session; the rest come from a content sweep.

**Cleanup / hygiene (verified by hand):**

- ~~**`06_Other/ballot_style_lab/` half-finished `cases/` migration**~~ — DONE (2026-07-24, commit `57583d1`). Deleted the ten byte-identical top-level yamls + the stale top-level `ballot_style_lab_pages/`; regenerated the YAML index (403, was double-counting the 10), CATALOG + `races.csv`/`elections.csv`, and the divergence review (its six ballot_style_lab case pages now point at `cases/cases_tabulated/`). repo-hygiene now reports all relative Markdown links resolve — the warn-only stale-mirror references are fixed. 147-test single-winner + drift-guard suite passes.
- **Three regenerated `_tabulated` mirrors sit uncommitted** in `method_comparisons/preference_vs_support/cases/cases_tabulated/` (bv2225/bv2226 — they gained their scenario-description headers). Diff is a legit regeneration; commit it (left alone this session in case a concurrent session owns the change).
- ~~**`build_divergence_index.py` boilerplate nit (§2's old finding)**~~ DONE (2026-07-24, commit `447eeb9`) — fixed at the classifier, not just the text; see §2 for detail.

**Content gaps (survey sweep):**

- ~~**5 rendered `REPLACE_*.png` image placeholders on 4 Ranked Robin case pages**~~ DONE (2026-07-29, commit `49651cc`). Captured all five from the live BV results pages (`4gfwdq`, `9pr3wr`, `48hjkv` ×2, `3r3yf7`), renamed to `img/<bvid>_<what>.png`, embedded with sized `<img width="640">`; the docs build is now warning-free. Building it produced `tools_adam/bv_result_screenshot.py` (headless Chrome + DevTools Protocol, clips to the result card — presets `result` / `race-details` / `chart` / `page`), so the remaining slots below are now a one-command job. **Still open:** 3 pages with commented-out (uncaptured) screenshot slots — `01_STAR/runoff_overturns_leader/teaching_runoff_reversal.md`, `00_start_here/STAR_reporting/reporting_ties.md` (2 slots), `00_start_here/STAR_reporting/reporting_diff_BV_LH.md`. These are inert (commented out ⇒ no build warning, no broken image), and one of them wants an *LH terminal* shot rather than a BV one, which the tool doesn't do.
- **Missing folder `README.md` landing pages** (the site renders these sections as bare file lists): `00_start_here/{about_this_repo, curriculum, tabulation_engines, tips, other_ranked_methods}`, `00_start_here/STAR_Voting/{getting_started, the_count, properties_and_limits, reference}`, `03_STAR_PR/concepts/stv/`, and `method_comparisons/split_voting/_main/` (the only `_main` in method_comparisons without one).
- **Method-folder imbalance — the 201/301-promised areas are the thinnest:** `03_STAR_PR` has 9 yaml cases but only ONE written lesson (`_main/bv2130_presidential_board_star_pr.md`; the allocated-score / RRV / sequential-Monroe / SSS / Lackner–Skowron cases have no teaching page); `04_Approval` has 4 yamls / 2 docs. Compare `01_STAR` (118 yaml / 187 md).
- **`00_start_here/voting_paradoxes/README.md` "Planned" section is unbuilt** — Ostrogorski's, Anscombe's, multiple-elections, Simpson's, plus Absolute-Majority and Pareto-dominated pages, each wanting a tagged case.
- **External-link blind spot:** `check_external_links.py` is advisory-only (not in CI) and explicitly skips `bettervoting.com` + Google Docs — so the site-wide BV `/results` links and the 6 Google-Doc links in `voting_paradoxes/README.md` are verified by nothing. Worth at least a HEAD-check variant or a periodic manual pass.
- ~~**Stale committed working artifacts** in `STARVote_LH_tabulation_engine/tools_adam/`~~ DONE (2026-07-24, commit `7a5bc4f`). Turned out only ONE was actually tracked (`random_star_divergence_c6_b5.csv`, 53KB) — it slipped past the `.gitignore` "Generated search outputs from the divergence-finder tools" block that already ignores its `star_irv_divergence_*` / `four_way_hits` siblings; `git rm`'d it and added `**/random_star_divergence_*.csv` to the pattern (docs reference the *script* + the frozen derived yamls, never the CSV). The June-2026 `star_irv_*` / `four_way_*` dumps were all already gitignored (untracked local scratch) — deleted them to declutter, no repo effect.
- ~~**Minor:** `00_start_here/about_this_repo/website_build.md` hardcodes the "5 build warnings" count~~ DONE (2026-07-29, commit `49651cc`) — the count is gone; the nit now records that the build is warning-free and what a returning `REPLACE_*` warning would mean.

**Tooling / tests (survey sweep):**

- ~~**No "regen-all" entrypoint — the highest-value automation gap.**~~ DONE (2026-07-24, commit `e6bc4fd`). Added `STARVote_LH_tabulation_engine/tools_adam/scripts/regen_all.py` — runs all seven generators in dependency order (`build_divergence_index → build_yaml_pages → build_yaml_index → build_catalog → build_bv_registry → build_multirace_index → build_paradox_index`; the first three are order-critical because each consumes the previous output). `--check` also runs the read-only checkers; `-q` for summary-only; exits non-zero if any generator fails (CI/Make-safe); idempotent; doesn't stage/commit. Building it surfaced a data bug the paradox builder's controlled vocabulary caught: four monotonicity cases were tagged `[monotonicity]` instead of the VOCAB tag `[non-monotonicity]` (so they never appeared under Non-monotonicity and the builder exited 1) — retagged and regenerated the paradox index. NOTE: still doesn't regenerate `_tabulated` engine mirrors (a separate mechanism — re-running each YAML through the engine); a `--mirrors` mode or a companion could close that.
- **Zero test CI.** `.github/workflows/` has only `docs.yml` (site deploy); the 22-file pytest suite never runs in CI, and the pre-commit hook runs only a 6-file subset. A GitHub Actions pytest job on push/PR is the second-highest-value gap — it would also catch mirror/page/index drift that the commit-time subset misses (currently 0 of 187 spot-checked mirrors stale, but nothing guards that).
- **Builder scripts are largely untested:** no tests at all for `build_bv_registry`, `build_catalog`, `build_paradox_index`, `build_multirace_index`, `build_divergence_index`, or `check_external_links`; `check_repo_hygiene.py` is exercised only as a live repo scan (via `test_md_links.py` / `test_content_quality.py`), never against fixtures — a regression in a checker would pass silently on a clean repo.
- **No first-class `voting_method: Score` on the teaching CLI** — plain score/range is offloaded to `06_Other/Range/Range_tabulation_engine/`, an inconsistency given the engine's own scoring round IS the tally (the known "capability is not the blocker" item). Borda / Bucklin / 3-2-1 are likewise absent as methods — fine as-is (they're teaching-page topics, not house methods), just recorded.
- **Vendored engines have no test dirs of their own** (`06_Other/RCV_IRV/RCV_IRV_tabulation_engine/`, `06_Other/abcvoting_tabulation_engine/`) — covered only via the main suite's crosschecks. Acceptable, but worth remembering if either is ever edited directly.
- **Minor:** 7 files in `tools_adam`/`tests` carry owner-only permissions (`-rw-------`) while siblings are world-readable — cosmetic inconsistency.

# file: todo-bv-migrate-ballot-style-lab.md
