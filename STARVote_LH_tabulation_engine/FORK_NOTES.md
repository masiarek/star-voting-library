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

**The engine algorithm is essentially unchanged.** `git diff --stat` against the tag reports a large line count (≈ +725 / −299 even with `-w`), but that is almost entirely **line-reflow** (signatures and long calls re-wrapped): the two files are ~97 % character-identical once whitespace is removed, `__version__` is still `2.1.6`, no functions were removed, and exactly **one** helper was added (`bool_converter`). The *functional* edits are two optional output toggles plus three **bug fixes** (see below):

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
- **Why upstream:** it is inside the engine's tiebreak mechanics, so it lives in `starvote/` (per the table above). Present in upstream 2.1.6 *and* on upstream `main` (lines 1690 / 1717 there). Reported to Larry — see the [errata note](../07_Concepts/tabulation_engines/LH_starvote/starvote_file_format.md#errata-the-unbreakable-tie-message-leaks-a-placeholder) for the repro.
- **Regression guard:** `tests/test_unbreakable_tie_message.py` pins the wording for the three reachable `_star_round()` ties and `ast`-parses the engine so no `break_tie()` description can carry an uninterpolated `{placeholder}` again (including the allocated / SSS sites, whose ties are awkward to provoke).

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
