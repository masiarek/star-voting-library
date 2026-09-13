---
name: new-case
description: Drafting a new election scenario in trash_delete.yaml, the three YAML schema gotchas, promoting a scratch case to a real one, the README-plus-cases/ folder layout, and the generated case-meta block on companion pages. Load before writing a new case file, creating a case folder, or touching a companion page's case-meta block.
---

# Drafting and filing a new case

*Migrated out of `CLAUDE.md` on 2026-09-12 so it loads on demand instead of in every session. The rules below are unchanged.*

## Case-folder layout

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
- **Companion pages carry a generated `case-meta` block.** A case with both a generated page
  (`<set>/cases/cases_pages/<stem>.md`) and a hand-authored companion (`<set>/<stem>.md`) gets a
  method / seats / expected-winners line plus a full-count link under the companion's H1,
  written by `build_yaml_pages.py` between `<!-- case-meta:start -->` / `<!-- case-meta:end -->`.
  **Don't hand-edit inside the markers or restate those facts alongside them** — change the YAML
  and rerun the generator. `tests/test_yaml_pages_current.py` fails when a block drifts.

## Scratch drafting (any method)

Draft new scenarios in `trash_delete.yaml` and tabulate until the behavior shows (a tie
rung, a method divergence, a criterion failure…). Nothing there is permanent; iterate
freely, keep examples small. **Two gotchas:** there is **no separate `candidates:` key** —
the **first line of the `ballots:` block is the candidate header**, comma-separated; and
weighted rows use a `Count:` header (`Count:Ada,Ben,Cara` then `15:5,2,0` per bloc).
A third: the title key is **`election_title:`**, not `title:` — the engine accepts bare
`title` as an alias so a scratch file *runs* either way, but it is not in the documented
schema, so `check_top_level_keys` fails the moment that scratch case is promoted to a
real one (which is exactly how 8 files drifted before 2026-08-07).

```yaml
election_title: Scratch (delete me)
voting_method: STAR
num_winners: 1
ballots: |-
  Ada,Ben,Cara
  5,2,0
  0,4,5
  2,5,4
expected_winners: [Ben]
```

(No `options:` block — the engine's defaults are the house style; add `--full`
to the run for the everything-on render.)

Tabulate with `.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py trash_delete.yaml`.
The run writes `_tabulated` mirrors into a sibling `<parentdir>_tabulated/` folder — for a
scratch file at the repo root that's a junk `YAML_tabulated/` directory; **delete it (and
the scratch files) when done, never commit them.**

**Promoting a scratch case to a real one:** LH-only cases (no BetterVoting election — e.g.
a reproduction of a Larry `starvote` test file) go straight to case files + `_tabulated`
mirror + indexes + commit. For a **BV-backed** case, the full nine-step mint/freeze/
reproduce loop is in the **`bettervoting` skill**.
