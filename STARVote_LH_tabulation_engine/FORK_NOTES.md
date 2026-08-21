# Fork Notes — starvote (vendored fork)

> **This page covers only the vendored upstream `starvote/` package.** For the full, consolidated list of *everything* we add to or change in the LH tabulator — new methods, new reports, and fixes — see **[`LH_ENGINE_CHANGES.md`](LH_ENGINE_CHANGES.md)** (canonical).

This directory contains a **vendored fork** of Larry Hastings' STAR Voting engine, [`larryhastings/starvote`](https://github.com/larryhastings/starvote). We do not submit pull requests upstream; we edit the engine directly here and keep it as part of this project (the `masiarek/star-voting-library` repo).

## What is what

| Path | Origin | Edit it when… |
|------|--------|---------------|
| `starvote/` (`__init__.py`, `__main__.py`, `reference.py`) | **Upstream engine** (Larry Hastings) | You're changing how the *voting algorithm itself* works — scoring, tabulation, tiebreak mechanics, CLI/option parsing of the engine. |
| `starvote_larry_hastings.py` | **Our code** | Anything about how *we* run, feed, or present an election — our `LotNumberTiebreaker`, matrix visualization, colored output, file loading. This `import starvote`; it should never duplicate engine logic. |
| `tools_adam/` | **Our code** | Helper/automation scripts (conversion, simulation, BetterVoting automation, etc.). |
| `tests/`, `test_elections/` | Mixed | Upstream tests plus ours. |

**Rule of thumb:** "Would Larry want this in the engine for everyone?" → it goes in `starvote/`. "Is this about *my* analysis, display, or workflow?" → it goes in our script/tools.

> Our wrapper script (`starvote_larry_hastings.py`), its display options, and the `_tabulated` output format are documented in **[starvote_larry_hastings.py — presentation wrapper](README_larry_hastings.md)**.

## Upstream baseline

The pristine upstream version is **starvote 2.1.6**, verified byte-identical to the PyPI release. It is recorded as the git tag:

```
starvote-upstream-2.1.6   ->  commit daa6bbd
```

### See exactly what we've changed in the engine, any time

```bash
# full diff of our engine edits vs pristine upstream
git diff starvote-upstream-2.1.6 -- STARVote_LH_tabulation_engine/starvote/

# just a summary
git diff --stat starvote-upstream-2.1.6 -- STARVote_LH_tabulation_engine/starvote/
```

## Current divergence from upstream 2.1.6

**The engine algorithm is essentially unchanged.** `git diff --stat` against the tag reports a large line count (≈ +725 / −299 even with `-w`), but that is almost entirely **line-reflow** (signatures and long calls re-wrapped): the two files are ~97 % character-identical once whitespace is removed, `__version__` is still `2.1.6`, no functions were removed, and exactly **one** helper was added (`bool_converter`). The *functional* edits are two optional output toggles plus five **bug fixes** (three detailed below; the SSS zero-score-ballot fix is documented in [BUG_sss_zero_score_ballots.md](BUG_sss_zero_score_ballots.md) and the Allocated Score count-vs-weight fix below and in [BUG_allocated_count_vs_weight.md](BUG_allocated_count_vs_weight.md) — the consolidated table lives in [LH_ENGINE_CHANGES.md §1](LH_ENGINE_CHANGES.md)):

- **`print_averages`** option (default `False`) + CLI flag `-a` / `--print-averages` and config key `print averages = <bool>`. Suppresses the averages line unless asked.
- **`print_maximum_score`** option (default `False`) + CLI flag `-M` / `--print-maximum-score` and config key `print maximum score = <bool>`. Suppresses the "Maximum score is …" line unless asked.
- `bool_converter` parses those two boolean config keys.
- Both options are forwarded to method functions only when they differ from the default, so older/reference method implementations don't break.

### Bug fix — five-star tiebreak default score (2025)

- **File/location:** `starvote/__init__.py`, `_maximum_score_count_round()`, the 2-candidate fast path (the `if len(candidates) == 2:` branch).
- **What changed:** `ballot_get(candidate1, 1)` → `ballot_get(candidate1, 0)`. The `.get()` default for the *second* candidate was `1` while the first candidate (and the general N-candidate path) correctly used `0`.
- **Effect:** this function powers the **five-star** tiebreaker (it counts votes equal to `maximum_score`). With the wrong default, a ballot that *omits* candidate1 contributed a phantom score of `1`; that only equals `maximum_score` when `maximum_score == 1` (Approval-style), so the miscount was **dormant for normal 0–5 STAR** (full ballots always include both candidates, and `1 ≠ 5`). It was still a latent correctness bug, now aligned with `candidate0` and the general path so all three agree.
- **Why upstream:** it's the *voting algorithm's* tiebreak mechanics, so it lives in `starvote/` (per the table above), not our wrapper. Consider offering it to Larry.
- **Regression guard:** the four `01_STAR/03_Criteria/tie_break_dead_rung/` cases exercise the five-star rung firing vs. falling through to the lot in both rounds.

### Bug fix — an unopposed race elected the first LETTER of the candidate's name (2026-08-21)

- **File/location:** `starvote/__init__.py`, `_star_round()`, the "Only one candidate, they win." short-circuit.
- **What changed:** `return list(scores)[0][0]` → `return list(scores)[0]`.
- **Effect:** `_scoring_round()` returns a **dict** (`_sort_score_dict` rebuilds one), so `list(scores)[0]` is already the candidate's *name*; the second index took that name's first **character**. A single-winner STAR race with one candidate on the ballot elected `A` for `Ada`, `Z` for `Zebra`. Everything downstream inherited it — the winner line, and the `[Runoff Reversal]` block comparing `(Ada)` against `(A)` and reporting a reversal that did not happen. Confined to **single-winner STAR with exactly one candidate**: Bloc/PR paths reach their last seat by a different route and were checked to be correct.
- **Why it survived:** not one of this library's ballot-carrying cases is uncontested, so the whole suite was blind to it — while an **uncontested seat** is one of the most ordinary things a real ballot carries.
- **Found by:** [`tools_adam/tie_taxonomy_sweep.py`](tools_adam/tie_taxonomy_sweep.py), probing degenerate election shapes alongside the tie sweep it was built for.
- **Why upstream:** it is the engine's own return value, so it lives in `starvote/`. **Not yet reported to Larry** — worth an issue (it is the third slip found in `_star_round`, after [#18](https://github.com/larryhastings/starvote/issues/18)).
- **Regression guard:** [`tests/test_single_candidate.py`](tests/test_single_candidate.py), which asserts on multi-character names in every case — a one-letter candidate passes even with the bug.

### Bug fix — SSS ballot allocation gated on verbosity (2026-08)

- **File/location:** `starvote/__init__.py`, `sequentially_spent_score()`, the "Ballot allocation round" block.
- **What changed:** the ballot-allocation machinery (building `remaining_decorated_ballots` / `remaining_weighted_ballots`, the star-spending/reweighting loop, and the `decorated_ballots = remaining_decorated_ballots` reassignment) was nested inside `if options.verbosity:`; it is now dedented so it runs at every verbosity, with only the printing still guarded.
- **Effect:** at the engine's default `verbosity=0`, no ballots were ever spent or reweighted, so SSS silently degenerated into repeated bloc score voting and could return **different winners** than the same election run verbosely — the defining proportionality of the method vanished in quiet runs. Reported upstream as [larryhastings/starvote#17](https://github.com/larryhastings/starvote/issues/17) (open; latest release 2.1.6 affected). Full analysis: [BUG_sss_verbosity.md](BUG_sss_verbosity.md).
- **Why upstream:** it's the voting algorithm's allocation mechanics, so it lives in `starvote/` (per the table above), not our wrapper. Offer it to Larry via issue #17.
- **Regression guard:** `tests/test_verbosity_invariance.py` asserts verbosity-invariant winners for `sss` / `allocated` / `rrv` / `bloc` plus the exact proportional SSS outcome.

### Bug fix — unbreakable-tie message never interpolated (2026-08)

- **File/location:** `starvote/__init__.py`, `_star_round()`, both `options.break_tie(...)` calls (the Scoring Round and Automatic Runoff Round dead ends).
- **What changed:** two characters. `"{int_to_words(len(tie), flowery=False)}-way tie in …"` → `f"…"`. The strings were plain literals, so the placeholder was never interpolated.
- **Effect:** presentation only, and only through the Python API — the `UnbreakableTieError` message read `{int_to_words(len(tie), flowery=False)}-way tie in Scoring Round` instead of `three-way tie in Scoring Round`. Because `_star_round()` serves **both** single-winner STAR and Bloc STAR, both methods raised the raw source text; the equivalent strings in `allocated_score_voting()` and `sequentially_spent_score()` already carried the `f` prefix, which is why the proportional methods looked fine. The printed report and the CLI are unaffected (the CLI prints its own `[Unbreakable Tie]` block and exits 0), and **no winner anywhere changes** — the exception is raised only when a tie is already unbreakable.
- **Why upstream:** it is inside the engine's tiebreak mechanics, so it lives in `starvote/` (per the table above). Present in upstream 2.1.6 *and* on upstream `main` (lines 1690 / 1717 there). Reported as [larryhastings/starvote#18](https://github.com/larryhastings/starvote/issues/18) (open) — filed separately from #17 because that one changes winners and this one cannot. Repro also in the [errata note](../07_Concepts/tabulation_engines/LH_starvote/starvote_file_format.md#errata-the-unbreakable-tie-message-leaks-a-placeholder).
- **Regression guard:** `tests/test_unbreakable_tie_message.py` pins the wording for the three reachable `_star_round()` ties and `ast`-parses the engine so no `break_tie()` description can carry an uninterpolated `{placeholder}` again (including the allocated / SSS sites, whose ties are awkward to provoke).

### Bug fix — scoring-round rung 1 counted preference votes, not matchups won (2026-08)

- **File/location:** `starvote/__init__.py`, new `_matchups_won_round()` and the rung-1 branch of `_star_round()`; mirrored in the wrapper's `resolve_finalists()`.
- **What changed:** when three or more candidates tie in the scoring round, rung 1 now counts **matchups won** (each head-to-head decided by how many ballots preferred each side, then pairs counted) instead of `_preference_round()`'s sum of per-ballot pairwise preferences. Drawn matchups are won by neither, matching `ranked_robin_tally`'s Copeland convention. A two-way tie still uses `_preference_round()`, where the two measures coincide and its vote counts are the more informative thing to print; the Automatic Runoff is untouched. When every matchup among the tied group is drawn the report now says so, because an all-zero row here means something different from an all-zero row on the five-star rung below.
- **Effect:** upstream's tally is compare-then-aggregate; the published protocol's is aggregate-then-compare. They agree at two candidates and can disagree at three or more — upstream can score a candidate who loses *every* head-to-head equal to candidates who win theirs, letting the five-star rung advance him. Equal Vote's [Official Tiebreaker Protocol](https://www.starvoting.org/ties) resolves a tie of three or more by "comparing the tied candidates head to head and eliminating the candidate(s) who lost the most match-ups", repeated as needed. No winner changed across the corpus. Fourteen committed `_tabulated` mirrors moved: eleven changed numbers, three (whose ballots express no preference at all) gained only the new all-draws line. Four of the eleven changed which rung decided the finalists — `cycle_C05_fewV28_bloc_1` and `06_c4_b24_narrow-bands` keep the same pair by a different route, while `cycle_C10_fewV28_bloc_1` (C + F → C + D) and `cycle_C10_fewV29_bloc_2` (A + C → C + F) seat a different pair, both still electing C. Every one is listed before-and-after in [the teaching page's appendix](../01_STAR/01_Learn/Tie_Breaking_STAR/matchups_won_vs_preference_votes.md#appendix-all-fourteen-mirrors-before-and-after).
- **Why upstream:** it is the tiebreak ladder inside `_star_round`, so it lives in `starvote/`. Not yet reported; the label upstream prints ("preferred in the most head-to-head matchups") describes the corrected statistic rather than the one the code computed.
- **Regression guard:** [`01_STAR/03_Criteria/tie_break_ladder/cases/tie_break_ladder_matchups_eliminate_loser.yaml`](../01_STAR/03_Criteria/tie_break_ladder/cases/tie_break_ladder_matchups_eliminate_loser.yaml) plus its `_tabulated` mirror (`tests/test_tabulated_mirrors_current.py`). Note the answer key alone cannot catch a regression there — a candidate who loses every matchup also loses the runoff he was wrongly advanced into, so it is the finalist pair in the mirror that moves, not the winner.

### Bug fix — Allocated Score fills the quota by ballot count, not weight (2026-08)

- **File/location:** `starvote/__init__.py`, `allocated_score_voting()`, the "Ballot allocation round" loop.
- **What changed:** the score group's weight sum (`allocation_weight = sum(t[INDEX_WEIGHT] for t in supporters[score_start:])`) replaces the row count in the overfill test, the quota subtraction, and the fractional-surplus factor (`quota ÷ allocation_weight`). When the two differ, the verbose report adds one line: `These ballots carry a remaining weight of W.` Round-1 output is byte-identical to upstream.
- **Effect:** winners change on any profile where a second allocation event touches already-reduced ballots — a bloc holding 3+ quotas paid `1 − quota/n` per seat *forever* (geometric decay, D'Hondt-flavored) instead of surrendering one quota of weight per seat. On the 41/19/6 fingerprint (5 seats) upstream elects 4-1-0; the fix, BetterVoting production, and the reference implementation shipped in `starvote/reference.py` all elect 3-1-1. Two repo cases flipped to the correct committee with the fix.
- **Why upstream:** allocation mechanics, so it lives in `starvote/` (per the table above). Reported as [larryhastings/starvote#20](https://github.com/larryhastings/starvote/issues/20) (open); full analysis in [BUG_allocated_count_vs_weight.md](BUG_allocated_count_vs_weight.md).
- **Regression guard:** `tests/test_allocated_weight_accounting.py` (fingerprint, the coop-board organic case, and a single-surplus fixture that must NOT change), plus `expected_winners` on the fingerprint case file.

> **Note on `example.py` and the vendored README's transcripts.** `example.py`
> here is NOT upstream's 3-ballot Amy/Brian/Chuck example — it was repurposed as
> a single-ballot **tiebreak-cascade demo** (scoring tie → head-to-head →
> five-star → Hashed Ballots). The vendored `README.md` still shows the upstream
> example and transcripts with averages/"Maximum score" lines that the fork's
> `print_averages=False` / `print_maximum_score=False` defaults now suppress —
> the README is kept as upstream wrote it; trust this file for what differs.

> **Correction (do not repeat the old claim):** the **`No Preference` → `Equal Support`** relabel, the Runoff (Preference) Matrix, `[Divergence from STAR]`, the `[Runoff Reversal]` summary, and `show_runoff_percent` are **NOT** engine edits — they all live in our wrapper `starvote_larry_hastings.py`. The vendored `starvote/` package still prints "No Preference" internally. Keeping the engine pristine-but-for-these-documented-edits is deliberate: it makes re-pulling a future upstream release trivial.

To regenerate this list precisely at any time, run the `git diff` commands above and compare the `def`/`class` inventory of the two versions.

## How to pull a future upstream update (if ever wanted)

1. Download the new pristine version (e.g. `pip download starvote==X.Y.Z --no-deps --no-binary :all:`).
2. Tag it: copy the new `starvote/` over a clean checkout, commit, `git tag starvote-upstream-X.Y.Z`.
3. Re-apply our diff: `git diff starvote-upstream-2.1.6 starvote-upstream-X.Y.Z` shows what upstream changed; resolve against our edits listed above.

Because our edits are small and localized, re-applying them by hand is the simplest path.
