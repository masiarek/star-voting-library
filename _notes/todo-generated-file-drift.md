# TODO — regen_all on a clean master is not a no-op

Working note. Not site content (excluded via `todo-*.md` in `mkdocs.yml`). Delete this file once `git status` is clean after a regen on a fresh checkout.

**Verified 2026-08-04**, found while adding BV1835 and deliberately kept out of that commit — the drift is pre-existing and unrelated. A local session was started to fix it and may have landed the work already; check `git log` before redoing it.

## The symptom

A clean detached worktree at `origin/master`, with nothing edited, reports seven files modified after a single regen:

```bash
git worktree add --detach /tmp/ctrl origin/master && cd /tmp/ctrl && python3 STARVote_LH_tabulation_engine/tools_adam/scripts/regen_all.py && git status --short
```

- `01_STAR/02_Examples/cases/cases_pages/03d_c5_b5_style-gallery-five-more.md`
- `07_Concepts/YAML_test_case_index/{bv_cases,elections,paradox_cases,races}.csv`
- `method_comparisons/divergence_review/{INDEX.md,divergence.csv}`
- plus a new untracked `method_comparisons/divergence_review/cases/IRV_DIFFERS_ARTIFACT/03d_c5_b5_style-gallery-five-more.md`

That noise lands in every unrelated branch, so anyone adding a case has to hand-separate their own rows from it. The control experiment above is the only reliable way to tell the two apart — eyeballing which diffs "look intentional" does not work.

## Two causes, mixed together

1. **Row-order churn in the CSVs.** Appears to date from `efe7c370` "Park the flat-scores tie set", which moved cases into `01_STAR/09_Parked/` without the indexes being regenerated in the same commit. The `Flat_scores_ties_*` rows move position; the diff reads as ~9 insertions / 8 deletions of unchanged data.
2. **Line endings.** The committed CSVs are CRLF; the generators write LF. Git reports `CRLF will be replaced by LF` on every regen of `paradox_cases.csv`, `races.csv` and `divergence.csv`.

## The fix

Regenerate and commit the stale outputs, and settle the line endings — either a `.gitattributes` rule pinning the generated `*.csv`, or make the writers emit CRLF to match what is committed. Pick one and state it in `CONTRIBUTING.md`, because the next person to run the generators will hit this again otherwise.

**Done when:** the reproduction above leaves `git status` clean.

## Fresh-machine setup (needed to run the above)

`regen_all.py` and the pytest suite both need packages that a bare Python does not have:

```bash
python3 -m pip install pyyaml pref_voting pytest
```

Without `pyyaml`, five of the seven generators fail instantly with `PyYAML is required`. Without `pref_voting` the suite still passes but skips the cross-checks — and per `CLAUDE.md` a pref_voting-less **pytest** run also rewrites five `_RANGE_tabulated.txt` mirrors in place, which then propagates into `range_101_c3_b5.md` and looks like a real failure. With all three installed the suite is **967 passed, 2 skipped, 0 failed** (2026-08-04).
