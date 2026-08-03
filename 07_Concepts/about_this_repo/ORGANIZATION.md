# Organizing the YAML files (conventions)

Where things live, what goes in the YAML vs a Markdown file, and how to get a clean demo without losing your documentation.

## The core principle: storage ≠ display

Most of the second-guessing ("if I document the scenario in the YAML it clutters my recording") comes from treating *where the text lives* and *what shows on screen* as the same decision. They aren't.

- **Keep the scenario text in the YAML** — one source of truth, travels with the ballots, can't drift out of sync.
- **Control what prints with an option** — `show_description: false` hides the long description on screen for a clean demo, *without removing it from the file*. The saved `_tabulated` file always keeps the full text.

So: store rich, display clean. You never have to choose.

## What goes where

| Content | Lives in | Prints on screen? |
|---------|----------|-------------------|
| `election_title` | YAML | yes (one-line banner) |
| `scenario_description` — short, audience-facing "what" | YAML | yes, unless `show_description: false` |
| `video_script` — presenter notes, cues, "how to present" | YAML | **no** (never shown on screen) |
| Cross-file teaching (lessons, sequences, comparisons, "why") | **Markdown** (`07_Concepts/`, folder READMEs) | n/a |

Rule of thumb: **per-file context → in the YAML; cross-file teaching → Markdown.** If a paragraph is about *this one election*, it belongs in the file. If it's about how several examples fit together, it belongs in an `.md`.

## Generated pages: a browsable `.md` per YAML — but never hand-written

Every election YAML also gets a **generated** Markdown page in `<folder>/<folder>_pages/<stem>.md` (`STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`): title, method (linked to its concept docs), the file's own scenario description, the ballots with a how-to-read line, the engine's full report (from the `_tabulated` mirror), and auto cross-references (folder README, topic hubs, divergence-ledger entry, siblings, glossary, index). `tests/test_yaml_pages_current.py` fails the suite if a page drifts from its sources — so the pages are always right, precisely because nobody edits them. The educational *prose* on a page comes from the YAML's own `scenario_description`; improve the YAML, regenerate, and the page follows.

## Don't: a separate HAND-WRITTEN `.md` per YAML, or a folder per scenario

Tempting, but it creates exactly the sync problem you already dislike with the Google Docs:

- **Per-YAML `.md`** doubles maintenance and drifts out of sync. The YAML already has two slots — `scenario_description` (printable) and `video_script` (notes) — which cover everything a single file needs.
- **A folder per scenario** (`yaml` + `md` + `_tabulated` together) fragments navigation: you can no longer skim a folder of examples, and the lesson order gets buried. Heavy for no benefit.

## Folder structure

Group by **teaching role**, not by file type.

**Inside a method folder, the second level is a fixed spine** (reorganized 2026-08-02). Every method uses the same numbered buckets, in the same reading order, and takes only the ones it needs:

| | Bucket | Holds |
|---|---|---|
| **01** | `01_Learn/` | concept pages for this method |
| **02** | `02_Examples/` | the teaching progression and themed example sets |
| **03** | `03_Criteria/` | criterion probes, tie-breaking, edge behavior |
| **04** | `04_Real_Elections/` | live BetterVoting races reconciled against the engine |
| **05** | `05_Practice/` | exercises with tested answer keys |
| **09** | `09_Parked/` | kept, but off the learning path |

Before this, `01_STAR/` had sixteen sibling folders that mixed four different axes at one level — kinds of material (`concepts`, `exercises`), criteria (`majority_criterion`), mechanisms (`tie_break_ladder`) and single artifacts (`pet_real_bv_election`) — sorted alphabetically, which is what the sidebar showed. The buckets exist so a reader learns the shape once and can then navigate every method.

**Difficulty is deliberately NOT in the folder names.** A case is often 101 for its basic idea and 301 for the deep dive; levels live in [CURRICULUM.md](../CURRICULUM.md) and in per-set tables, so a case can appear at two levels without being duplicated or moved. The numeric prefix orders the sidebar (MkDocs derives nav order and labels straight from folder names); capitalize the word after the number, or MkDocs renders the label lowercase.

Prefixed folders are also why every rename here is expensive: see the redirect rule below.

Prominence follows the library's mission: the **equal-vote (EVC) methods get the numbered, front-rank folders**; other methods appear mainly as contrast material.

```
07_Concepts/        CROSS-METHOD material only: guided start, glossary,
                      curriculum, TIPS/authoring canon, conventions (Markdown)
  topics/             cross-method CONCEPT pages (spoiler effect, wasted votes,
                      ballot styles, criteria…) + per-topic hubs (summability/,
                      monotonicity/, center_squeeze/, …)
  voting_paradoxes/ scores_and_ranks/ tabulation_engines/ books/ …
                      the rest of the material that belongs to no single method
01_STAR/              single-winner STAR — the headline method
  01_Learn/           concept pages FOR THIS METHOD (start here, the count,
                      properties & limits, hands-on, reporting/); the
                      Larry↔Adam conversation scripts live beside their
                      topics, indexed in conversation_scripts.md
  02_Examples/        the teaching progression — the smallest elections, one
                      new idea each — plus themed sets like
                      runoff_overturns_leader/
  02_Examples/cases/cases_tabulated/   their generated _tabulated.txt mirrors
  03_Criteria/        criterion probes and the tie-breaking cascade
  04_Real_Elections/  live BetterVoting races, reconciled against the engine
  05_Practice/        predict-then-peek exercises with tested answer keys
  09_Parked/          kept, but off the learning path
02_STAR_Bloc/         Bloc STAR (multi-winner, majoritarian)
03_STAR_PR/           proportional STAR (sss / allocated / rrv)
04_Approval/          Approval Voting
05_Ranked_Robin/      Ranked Robin (RCV-RR / Copeland)
06_Other/             non-EVC reference methods + auxiliary engines/tools, each in its own subfolder —
  RCV_IRV/            RCV-IRV example + its engine (RCV_IRV_tabulation_engine/)
  STV/                STV example
  Range/              Range example + its engine (Range_tabulation_engine/)
  abcvoting_tabulation_engine/   multi-winner Approval (ABC) cross-check (optional)
  simulations/        Monte-Carlo scripts (favorite-betrayal / runoff-reversal rates)
  _demo_dropbox/      watch-folder demo (drop a BV export, get YAML + tabulation)
method_comparisons/   SAME ballots, DIFFERENT methods — black_curtain,
                      center_squeeze, monotonicity, split_voting, summability,
                      paradoxes_and_whoops, BV_Library, divergence_review
YAML_library/         BetterVoting JSON→YAML converter + positive/negative fixtures
STARVote_LH_tabulation_engine/   the STAR engine, its tests/, and
  tools_adam/         Adam's tooling — the build scripts (scripts/), the
                      pref_voting cross-check engine, find_*divergence.py
```

- **`_tabulated` output nests INSIDE the source file's own folder** as `<folder>/<folder>_tabulated/` (the engine computes this: `tabulated_output_path`). Loose files live in a folder's `02_Examples/cases/` subfolder (still `_main/` under `method_comparisons/`) so their mirrors nest the same way. Generated, regenerable, separate from source, but right next to the YAML it came from. (Committed by choice; they could be gitignored instead.)
- **One door per voting method (2026-07-29).** A method's concept pages live in **that method's own folder**, in its `01_Learn/` bucket — `01_STAR/01_Learn/`, `04_Approval/01_Learn/`, `05_Ranked_Robin/01_Learn/` (the two `06_Other/` methods still use the older `concepts/` name: `06_Other/RCV_IRV/concepts/`, `06_Other/Range/concepts/`), and so on. The folder's `README.md` is the method's **start-here**: what the method is, then its concepts, then its runnable examples. They used to sit in a parallel `07_Concepts/<Method>/` tree, which gave every method two competing front doors — the case folder was a top-level nav section, so that is where readers landed, but the page that actually taught the method was somewhere else entirely.
- **`07_Concepts/` is now cross-method material only** — topics, paradoxes, scores-and-ranks, curriculum, glossary, engines. Nothing in it competes with a method folder for the same reader.
- **Every relocated page keeps a permanent redirect** in `mkdocs.yml`'s `redirect_maps` (120 of them). Published URLs are quoted in permanent BetterVoting election descriptions that cannot be edited after the election goes live, so those redirects are not housekeeping — deleting one creates an unfixable 404. Moving concept pages again? Use `tools_adam/scripts/migrate_concept_links.py`, which resolves relative links against each source file rather than blind-replacing strings, and add the new redirects.
- **Markdown teaching docs cluster in `07_Concepts/`** (cross-method) and in each method folder's `01_Learn/` and `README.md`, so the prose has a home that isn't tangled with the data.

## The clean-demo / recording recipe

For a file you'll show on camera:

```yaml
options:
  show_description: false   # hide the long write-up
  show_matrix: false
  show_condorcet: false
  show_score_counts: false
  brief: true
  show_irv: false
```

That leaves just the title banner, the ballots, and the tabulation. The full context is still in the file (and in its `_tabulated` copy) for anyone studying it later. Flip the flags back to `true` for a workshop or self-study.

> Tip: keep `scenario_description` to 1–3 short paragraphs (the audience-facing "what"), and put longer staging notes in `video_script` — it never prints, so it can be as detailed as you like without ever cluttering a demo.

See also: [TIPS_choosing_voter_counts.md](../tips/TIPS_choosing_voter_counts.md) · [CURRICULUM.md](../CURRICULUM.md).
