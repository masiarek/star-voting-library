# TODO — BV-migrate the ballot-style lab (+ parked backlog from 2026-07-17)

Working notes to pick up later. Not site content (excluded in `mkdocs.yml`). Delete sections as they're done.

## 1. The headline task: take the ballot-style lab live on BetterVoting

`06_Other/ballot_style_lab/` holds ten frozen scenario yamls with **no BV elections yet** — the single-winner set (01–06) and the new multi-winner wing (07a/07b Herb Garden Council Bloc-vs-PR same-ballots pair, 08 Quota Circus STAR-PR, 09 Park Bloc 4-seats). Migrate them the way the exercises set went live (BV2191–2202): specs in `bv_election_specs.py`, next free Test IDs from the registry (**BV2211+** as of this writing), create via `create_bv_test_election.py`, verify winners via `/API/ElectionResult/<id>`, freeze UI exports, wire `bv_*` fields into the yamls, regen registry, note BV-vs-LH agreement per case page.

Cautions, learned 2026-07-17:

- **07a's Bloc final seat hangs on an 83–82 score rung** — confirm the whole ladder resolves deterministically on BV before freezing; any lot/random-decided seat stays **LH-only** (don't migrate it). The lab's hunter already rejected lot-decided seeds, but verify one champion by hand.
- **Every STAR_PR race will banner "Tied!" spuriously** (`tieBreakType: random`, no tie) — the serializer quirk with three confirmed instances (`89wwvr`, `jwxr3j`, `fvg8y8`). Seats compute correctly; note the quirk in each case page rather than treating it as a divergence.
- **If any scenario ever gets an STV race:** a count whose eliminations leave one hopeful who then reaches quota **crashes BV** (`06_Other/STV/bv_stv_sole_survivor_crash/`) — design the endgame with a hopeful standing, or wait for the fix.
- **Coordination:** the lab is another session's active thread (commit `51f0a30`); pick this up there or after its index churn settles.

## 2. Loose ends from the 2026-07-17 session (BV2203–BV2210 + Burlington)

- ~~**Push**~~ — done (verified 2026-07-23: local master == GitHub master @ `5fd470c`).
- **File the STV crash issue** on Equal-Vote/bettervoting — ready-to-file text sits in [06_Other/STV/bv_stv_sole_survivor_crash/README.md](06_Other/STV/bv_stv_sole_survivor_crash/README.md).
- ~~**Freeze UI exports**~~ — done (2026-07-23), and the whole step is now AUTOMATED: new `tools_adam/fetch_bv_export.py` reproduces the UI's "Download JSON" via three anonymous GETs (`Election` + `anonymizedBallots` + `ElectionResult`; verified byte-equivalent on `vqyqkr`), and `create_bv_test_election.py` auto-freezes after casting. All eight frozen into their case folders: `7mckyg`, `b6xrdr` (FBC pair) · `7q6by8`, `fxhw6g` (burial pair) · `fvg8y8` (food-truck row, one shared export) · `39py93` (STV control) — every BV winner matches its yaml's `expected_winners`. The crashers `gvtg2h`/`8xwx43` froze `--without-results` (ElectionResult still HTTP 500 as of 2026-07-23); **re-fetch those two with `--force` once BV ships the STV fix.**
- **divergence_review builder nit:** its generated page for `bv2206…` says "Ranked Robin and Condorcet agree with STAR" while its own table shows RR = Bluebell ≠ STAR = Clover — the boilerplate doesn't read its own numbers. Fix in `build_divergence_index.py`, regen.
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

- **`06_Other/ballot_style_lab/` half-finished `cases/` migration** — all ten yamls exist BOTH at folder top and in `cases/`, byte-identical (`cmp` verified), plus a stale top-level `ballot_style_lab_pages/` alongside the live `cases/cases_pages/` + `cases/cases_tabulated/`. The README already links only the `cases/` copies, so the top-level yamls + old pages dir are pure leftovers. Since test discovery globs both `*.yaml` and `cases/*.yaml`, the ten cases double-run in the suite. Fix: delete the ten top-level yamls + `ballot_style_lab_pages/`, regen indexes/registry, confirm nothing else links the old paths. Known stale references already (hygiene warn-only output): two divergence-review pages under `method_comparisons/divergence_review/cases/IRV_DIFFERS_ARTIFACT/` (05, 06) still link the removed top-level `ballot_style_lab_tabulated/` mirror path — the divergence regen will fix them once the duplicates are gone.
- **Three regenerated `_tabulated` mirrors sit uncommitted** in `method_comparisons/preference_vs_support/cases/cases_tabulated/` (bv2225/bv2226 — they gained their scenario-description headers). Diff is a legit regeneration; commit it (left alone this session in case a concurrent session owns the change).
- **`build_divergence_index.py` boilerplate nit (§2's old finding, still unfixed)** — line ~392 hardcodes "Ranked Robin and Condorcet agree with STAR" without reading its own table (bv2206 page contradicts itself). Fix in the builder, regen.

**Content gaps (survey sweep):**

- **5 rendered `REPLACE_*.png` image placeholders on 4 Ranked Robin case pages** — `05_Ranked_Robin/condorcet_vs_ranked_robin/bv2140_48hjkv_most_pairwise_wins.md` (2), `clone_independence/bv2143_9pr3wr_teaming_fails.md`, `clone_independence/bv2142_4gfwdq_clone_cycle_pre.md`, `rr_tiebreaks/bv2141_3r3yf7_four_degree_tie.md` — these are the site's 5 known build warnings. Plus 3 pages with commented-out (uncaptured) screenshot slots: `01_STAR/runoff_overturns_leader/teaching_runoff_reversal.md`, `00_start_here/STAR_reporting/reporting_ties.md` (2 slots), `00_start_here/STAR_reporting/reporting_diff_BV_LH.md`.
- **Missing folder `README.md` landing pages** (the site renders these sections as bare file lists): `00_start_here/{about_this_repo, curriculum, tabulation_engines, tips, other_ranked_methods}`, `00_start_here/STAR_Voting/{getting_started, the_count, properties_and_limits, reference}`, `00_start_here/proportional_representation/stv/`, and `method_comparisons/split_voting/_main/` (the only `_main` in method_comparisons without one).
- **Method-folder imbalance — the 201/301-promised areas are the thinnest:** `03_STAR_PR` has 9 yaml cases but only ONE written lesson (`_main/bv2130_presidential_board_star_pr.md`; the allocated-score / RRV / sequential-Monroe / SSS / Lackner–Skowron cases have no teaching page); `04_Approval` has 4 yamls / 2 docs. Compare `01_STAR` (118 yaml / 187 md).
- **`00_start_here/voting_paradoxes/README.md` "Planned" section is unbuilt** — Ostrogorski's, Anscombe's, multiple-elections, Simpson's, plus Absolute-Majority and Pareto-dominated pages, each wanting a tagged case.
- **External-link blind spot:** `check_external_links.py` is advisory-only (not in CI) and explicitly skips `bettervoting.com` + Google Docs — so the site-wide BV `/results` links and the 6 Google-Doc links in `voting_paradoxes/README.md` are verified by nothing. Worth at least a HEAD-check variant or a periodic manual pass.
- **Stale committed working artifacts** in `STARVote_LH_tabulation_engine/tools_adam/`: June-2026 sweep dumps (`star_irv_divergence_C3_B*_20260619-*.csv`, `star_irv_log.txt`, `four_way_log.txt`, `star_irv_hits.csv`) sitting alongside the scripts — move to a scratch/output dir or delete.
- **Minor:** `00_start_here/about_this_repo/website_build.md` hardcodes the "5 build warnings" count — will drift as screenshots land; reword to "the known `REPLACE_*` placeholders".

**Tooling / tests (survey sweep):**

- **No "regen-all" entrypoint — the highest-value automation gap.** The 8 generators are split three ways: pre-commit hook regenerates 3 (`build_divergence_index`, `build_multirace_index`, `build_catalog`), pytest drift-guards cover 2 (`build_yaml_index` via `test_yaml_index_current.py`, `build_yaml_pages` via `test_yaml_pages_current.py`), and 3 are fully manual (`build_bv_registry`, `build_paradox_index`, `check_external_links`). One `regen_all.py` (or Make target) that runs them all in the right order would end the "which builders do I run" question for good.
- **Zero test CI.** `.github/workflows/` has only `docs.yml` (site deploy); the 22-file pytest suite never runs in CI, and the pre-commit hook runs only a 6-file subset. A GitHub Actions pytest job on push/PR is the second-highest-value gap — it would also catch mirror/page/index drift that the commit-time subset misses (currently 0 of 187 spot-checked mirrors stale, but nothing guards that).
- **Builder scripts are largely untested:** no tests at all for `build_bv_registry`, `build_catalog`, `build_paradox_index`, `build_multirace_index`, `build_divergence_index`, or `check_external_links`; `check_repo_hygiene.py` is exercised only as a live repo scan (via `test_md_links.py` / `test_content_quality.py`), never against fixtures — a regression in a checker would pass silently on a clean repo.
- **No first-class `voting_method: Score` on the teaching CLI** — plain score/range is offloaded to `06_Other/Range/Range_tabulation_engine/`, an inconsistency given the engine's own scoring round IS the tally (the known "capability is not the blocker" item). Borda / Bucklin / 3-2-1 are likewise absent as methods — fine as-is (they're teaching-page topics, not house methods), just recorded.
- **Vendored engines have no test dirs of their own** (`06_Other/RCV_IRV/RCV_IRV_tabulation_engine/`, `06_Other/abcvoting_tabulation_engine/`) — covered only via the main suite's crosschecks. Acceptable, but worth remembering if either is ever edited directly.
- **Minor:** 7 files in `tools_adam`/`tests` carry owner-only permissions (`-rw-------`) while siblings are world-readable — cosmetic inconsistency.

# file: todo-bv-migrate-ballot-style-lab.md
