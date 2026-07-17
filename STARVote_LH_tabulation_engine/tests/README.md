# Engine test suites

The pytest suites that guard the engine and the library's cases. The pre-commit hook runs the core set on every commit; run manually from the engine directory with `pytest tests/`.

Highlights (see [CLAUDE.md](../../CLAUDE.md) and the [Repository & Engine Guide](../../00_start_here/about_this_repo/repository_guide.md) for the full story):

- `test_single_winner_positive.py` — every single-winner STAR yaml with `expected_winners` runs through the CLI and must produce the right winner (also regenerates the `_tabulated` mirrors).
- `test_harness_selfcheck.py` — meta-tests proving the winner check isn't vacuous: deliberately-wrong answer keys in `harness_cases/` must fail.
- `test_json_to_yaml_conversion.py` — guards the BetterVoting-JSON → YAML pipeline end to end.
- `test_separator_and_errors.py` + `negative_cases/` — malformed files must exit 1 with a clear message and no traceback.
- `test_runoff_percent.py` — locks the wording and math of the self-reconciling runoff summary and its `_tabulated` funnel.
- `test_ranked_robin.py`, `test_approval_mirror.py`, `test_lot_number_tiebreak.py`, `test_abcvoting_crosscheck.py` — per-method counts, tie-break reproduction, and the independent `abcvoting` cross-check (skips if the library is absent).
- `test_readme_index_complete.py`, `test_yaml_index_current.py`, `test_yaml_pages_current.py`, `test_content_quality.py` — repo hygiene: index-complete READMEs list every page, generated indexes/pages are current, content passes quality rules.
