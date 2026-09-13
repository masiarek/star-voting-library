---
name: moving-pages
description: The method-folder layout (one door per voting method, the fixed numbered buckets) and how to move or rename pages without breaking links — migrate_concept_links.py, why redirect keys are permanent, and the three things the script silently misses. Load before moving, renaming or reorganizing any page or folder.
---

# Method folders and moving pages

*Migrated out of `CLAUDE.md` on 2026-09-12 so it loads on demand instead of in every session. The rules below are unchanged.*

- **One door per voting method (reorganized 2026-07-29).** A method's concept
  pages live **inside that method's folder**, in its `01_Learn/` bucket —
  `01_STAR/01_Learn/` (incl. `01_Learn/reporting/`), `03_STAR_PR/01_Learn/`,
  `04_Approval/01_Learn/`, `05_Ranked_Robin/01_Learn/`. The two 06_Other
  methods still use the older `concepts/` name:
  `06_Other/RCV_IRV/concepts/`, `06_Other/Range/concepts/`. The folder's
  `README.md` is that method's **start-here** (what it is → its concepts → its
  runnable examples).
- **The method-folder spine (reorganized 2026-08-02).** Inside `01_STAR/`…
  `05_Ranked_Robin/`, the second level is a fixed, ordered set of buckets —
  `01_Learn/`, `02_Examples/`, `03_Criteria/`, `04_Real_Elections/`,
  `05_Practice/`, `09_Parked/` — and each method takes only the ones it needs.
  Adding a case set? Put it in the bucket that fits rather than creating a new
  second-level sibling. **Capitalize the word after the number** (`02_Examples`,
  not `02_examples`): MkDocs derives sidebar labels from folder names and
  renders an all-lowercase name lowercase. **Difficulty stays out of the folder
  names** — a case is often 101 for its basic idea and 301 for the deep dive, so
  levels live in `07_Concepts/CURRICULUM.md` and per-set tables, never in a path. They previously lived in a parallel `07_Concepts/<Method>/`
  tree, which gave each method two competing front doors. **`07_Concepts/` is now
  cross-method only** (topics, paradoxes, scores_and_ranks, curriculum, glossary,
  engines, tips, books) — don't put method-specific pages back into it.
  **Moving concept pages again?** Use
  `tools_adam/scripts/migrate_concept_links.py` (resolves relative links per
  source file — a blind string replace corrupts them), run it **before** the
  `git mv`, and add a `redirect_maps` entry per moved page. Those redirects are
  **permanent**: published URLs are quoted in BetterVoting election descriptions
  that can never be edited, so a deleted redirect is an unfixable 404.
  **Three things that script will NOT do for you** — each one fails silently,
  and all three bit the 2026-08-02 reorganization:
  1. **Repoint existing redirect DESTINATIONS.** You must pass `--exclude
     mkdocs.yml` (its redirect *keys* are historical URLs and must never move),
     but that also leaves every *value* pointing into the folder you just moved.
     Those already-published URLs then 404 — the exact outcome the redirects
     exist to prevent. Freeze the keys, repoint the values by hand, and assert
     every destination exists on disk afterward — **machine-checked since
     2026-08-21** (`check_redirect_maps` in `check_repo_hygiene.py`, gated by
     `tests/test_md_links.py`), which also refuses a *duplicate* key: PyYAML
     keeps the last value, which is how two 2026-08-02 leftovers kept the docs
     deploy red for 14 commits after `04a8eea` deleted their targets.
  2. **Fix segment-wise paths in Python.** `REPO_ROOT / "01_STAR" / "_main"`
     contains no literal `01_STAR/_main`, so the literal pass cannot see it, and
     a glob over the now-missing directory yields **nothing without erroring** —
     parameterized cases just vanish. `tests/test_case_roots_exist.py` now fails
     the suite when a test module names a path that doesn't resolve; keep it.
  3. **Touch `.claude/`.** It is in the script's `SKIP_DIRS`, so paths inside
     the repo's own skill files survive every rename. Grep it by hand.
  And re-read the *prose* afterward: the literal pass cannot tell a live path
  from a sentence about the old path, and a link whose visible label is a
  backticked folder name keeps saying the old name after its target is
  repointed — the label is text, not a path.
