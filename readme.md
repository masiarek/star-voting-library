# STAR Voting — Education & Test-Case Library

A teaching repository for **STAR Voting** built around a vendored, lightly-tweaked fork of Larry Hastings' [`starvote`](https://github.com/larryhastings/starvote) tabulation engine. It pairs a real counting engine with a library of example elections, plain-language tabulation output, a BetterVoting import path, and a test suite — for voters, presenters, and debaters learning and teaching STAR.

**Why this exists.** Most voting-method debates run on hand-waving and toy examples. The goal here is to make STAR (and the methods it's compared against) *legible*: every claim is backed by a runnable election and a transparent, auditable count. The **BetterVoting import path** is the bridge to reality — take a genuine election run on [BetterVoting](https://bettervoting.com) (the Equal Vote Coalition's free STAR platform), convert its JSON export into a canonical YAML, re-tabulate it with an engine whose every step is legible, and confirm the result matches BetterVoting's official tally. Real elections become teachable, reproducible cases — not just textbook constructions.

---

## The big picture: one YAML file, a pipeline around it

Everything here orbits a single, human-readable **YAML election file** as the source of truth. The pieces fit together as a pipeline:

```
 author ──▶ validate ──▶ tabulate ──▶ verify ──▶ publish
   │                         │                       │
   │                         ├─▶ screen echo         └─▶ a browsable <name>.md page
   │                         └─▶ _tabulated.txt          (the friendly, linkable surface)
   │                             (the full record)
   ├─ hand-write the YAML, or
   └─ import a BetterVoting JSON export (converter → canonical YAML)
```

1. **Author.** Write a small YAML election by hand, *or* import a real **BetterVoting JSON export** with the converter. The converter produces a canonical YAML: real candidate names as IDs, aligned ballot columns, the election's official tie-break (lot) order, and the embedded expected winner.
2. **Validate.** The engine rejects malformed files with clear, plain-language errors and **no Python tracebacks** (bad YAML, missing `ballots:`, wrong column counts, out-of-range scores, ranked ballots under a score method, method/seat mismatches…). Negative test cases lock this behavior in.
3. **Tabulate.** Run the YAML election file through the engine. It prints an annotated, round-by-round **interactive echo** to the screen, and writes a full-detail **`_tabulated.txt`** sibling for the record. STAR (single / Bloc / PR), Approval, **Ranked Robin**, and RCV-IRV are dispatched automatically based on the file.
4. **Verify.** Each file embeds its expected winner — `expected_winners:` in hand-written files, an `expected_results:` block in BetterVoting imports — and a **pytest** suite checks them (positive winners, negative errors, JSON→YAML conversion, tie-break logic, Ranked Robin, plus non-vacuous self-checks), wired into a pre-commit hook.
5. **Publish.** `STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py` renders each election into a **browsable Markdown page** (`<folder>/<folder>_pages/<name>.md`) — title, method, the scenario description, the ballots, and the full tabulation report, with auto cross-references. A pytest keeps these pages in sync with their YAML, so they're always current. This `.md` page — not the raw `.yaml` — is the reader-facing surface.

> **House rule — link the `.md` page, not the raw `.yaml`.** The generated pages are the friendly, reader-first surface: lead with them in tables, navs, and cross-references; link a `.yaml` only when the *runnable source* is genuinely the point (e.g. a "run this file" command), and demote it. See `CLAUDE.md`.

This is *not* a black box that just prints a winner — the whole point is that the count is **legible and reproducible**, so it can be taught and audited.

---

## Repository map

| Area | What's there |
|---|---|
| [**STAR engine** (LH `starvote` fork)](STARVote_LH_tabulation_engine/) | The STAR engine (single-winner STAR, Bloc / proportional STAR, Approval, **Ranked Robin**), reporting options, the preference matrix, the `[Divergence from STAR]` comparison, the optional `show_runoff_percent` runoff summary, and the `lot_numbers` tie-break. Vendored fork of `starvote`; see [Fork Notes — starvote (vendored fork)](STARVote_LH_tabulation_engine/FORK_NOTES.md). |
| [**RCV-IRV engine** (pyrankvote)](06_Other/RCV_IRV/RCV_IRV_tabulation_engine/) | Vendored RCV-IRV engine. Ranked ballots (`A>B>C`) route here automatically. Concept pages: [RCV-IRV (Hare)](00_start_here/RCV_IRV/RCV-IRV-Hare.md). |
| [**pref_voting cross-check engine**](STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/) | Independent cross-check engine — wraps Eric Pacuit's `pref_voting` to verify the LH engine's Condorcet / IRV / Plurality (and report Copeland = Ranked Robin). Optional dep. |
| [**abcvoting engine**](abcvoting_tabulation_engine/) | Multi-winner **Approval / ABC** rules (Martin Lackner's `abcvoting`) — SPAV / PAV / Phragmén and an AV cross-check of the LH bloc-Approval count. Optional dep. |
| [**YAML library — imports & converter**](YAML_library/) | BetterVoting JSON → YAML converter ([`01_convert_json_yaml.py`](YAML_library/1_positive/01_convert_json_yaml.py)) and imported elections (`YAML_library/1_positive/`). |
| [**YAML library — negative fixtures**](YAML_library/) | Malformed fixtures (`YAML_library/2_negative/`) — every one must fail with the right plain-language error (see [Validation philosophy](#validation-philosophy) below). |
| [**Example elections** (01_STAR … 06_Other)](01_STAR/) | Hand-authored example elections, grouped by content type: [STAR](01_STAR/), [Bloc STAR](02_STAR_Bloc/), [proportional STAR](03_STAR_PR/), [Approval](04_Approval/), [Ranked Robin](05_Ranked_Robin/), [method comparisons](method_comparisons/), [other methods](06_Other/). |
| [**Simulations**](simulations/) | Monte-Carlo scripts: Favorite Betrayal frequency and runoff-reversal rates. |
| [**Divergence review**](method_comparisons/divergence_review/INDEX.md) | Case index + CSV of elections where methods disagree (STAR vs IRV vs Condorcet…). |
| [**Demo dropbox** (watch-folder)](_demo_dropbox/) | Watch-folder demo: drop a BetterVoting JSON export in, get canonical YAML + tabulation out. |
| [**YAML test-case index**](00_start_here/YAML_test_case_index/) | **Auto-generated catalog of every election YAML, grouped by voting method** ([`STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_index.py`](STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_index.py); a pytest keeps it current). Browse cases by method without moving files. |
| Tabulated mirrors (`*_tabulated/`) | Generated plain-text tabulation copies (regenerated by re-running the YAMLs). |
| [**Docs hub** (`00_start_here/`)](00_start_here/00_START_HERE.md) | The docs hub — [curriculum](00_start_here/CURRICULUM.md), concept pages, [glossary](00_start_here/GLOSSARY.md), [terminology](00_start_here/TIPS_terminology.md), and [organization conventions](00_start_here/ORGANIZATION.md). |
| [**Conversation scripts**](00_start_here/conversation_scripts.md) | Larry ↔ Adam debate / teaching scripts — index; episodes live beside their topics. |
| Test suite (`…/tests/`) | The [pytest suite + pre-commit hook](STARVote_LH_tabulation_engine/tests/). |

> Start with [Start Here](00_start_here/00_START_HERE.md) for the guided tour, and [CLAUDE.md — working guidance for this repo](CLAUDE.md) for the house conventions.

---

## The YAML election file

Want to author a case? The fill-in guide is [YAML Test Case — Authoring Template](00_start_here/YAML_authoring_template.md).

The schema is **flat**. The only required pieces are a voting method, a seat count, and a ballot grid (a header row of candidate names, then one row of 0–5 scores per voter):

```yaml
voting_method: STAR
num_winners: 1
ballots: |-
  Ann,Bob,Cal
  5,4,0
  3,5,2
  0,3,5
```

Hand-written files add a top-level **`expected_winners:`** list — that is the key the positive pytest suite discovers and checks:

```yaml
voting_method: STAR
num_winners: 1
ballots: |-
  Ann,Bob,Cal
  5,4,0
  3,5,2
  0,3,5
expected_winners:
- Bob
```

Richer files (the shape the BetterVoting converter produces) add candidates with explicit IDs, human context, an optional tie-break order, and an `expected_results` block (what the engine produced last time — checked by the conversion and tie-break tests):

```yaml
election:
  election_title: Ice Cream — Flavor of the Year
  races:
  - num_winners: 1
    voting_method: STAR
    candidates:
    - {cand_id: Chocolate,      candidate_name: Chocolate}
    - {cand_id: Chocolate Chip, candidate_name: Chocolate Chip}
    - {cand_id: Strawberry,     candidate_name: Strawberry}
    ballots: |-
      Chocolate, Chocolate Chip, Strawberry
              4,              5,          2
              1,              0,          5
    lot_numbers: [Strawberry, Chocolate Chip, Chocolate]   # optional, see below
    expected_results:
      winners:
      - Strawberry
```

### Ballot markers (all tabulate as 0)

A score cell is `0`–`5`, or one of these markers capturing voter intent. Each counts as 0 support, but is preserved so reports and quorums stay honest:

| Marker | Meaning |
|---|---|
| `-` | Blank / left unmarked |
| `~` | Race-level abstention (skipped the whole race) |
| `&` | Candidate-level abstention |
| `?` | Spoiled / voided ballot |
| `%` | Spoiled **and** re-issued |

Approval ballots accept only `0`/`1` (plus blank/marker = not approved).

### Weighted (grouped) ballots

For larger electorates, prefix a row with a count and `×` (or `:`/`x`):

```yaml
ballots: |-
  Ann,Bob,Cal
  42 × 0,3,5
  15 × 5,1,0
```

(House style keeps examples **small** — prefer a handful of individual ballots that make the point over big weighted blocs. See [Tips — Choosing the Number of Voters in STAR Examples](00_start_here/TIPS_choosing_voter_counts.md).)

### Tie-breaking and `lot_numbers`

`lot_numbers:` is **optional**. It's the official tie-break order (highest priority first) used only when STAR's deterministic tiebreakers can't separate the candidates. Imported BetterVoting files carry it automatically; hand-written files usually omit it (the engine then assumes CSV column order). The full ladder — and what JSON provides vs. what you may set by hand — is documented in [STAR Tie-Breaking — The Full Chain](00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md).

---

## Scored (rated) vs. ranked — the thing people conflate

People new to STAR — especially from a ranked-choice background — constantly mix up **scored** methods with **ranked** ones. They sound like cousins but do opposite things.

**Ranked = put them in order. Scored = give each a star rating.**

- **Ranked (RCV-IRV):** you line candidates up — 1st, 2nd, 3rd. Purely *relative order*. You can't say a candidate is your 1st by a mile vs. by a hair, and you can't give two candidates the same position.
- **Scored / starred (STAR, Score, Approval):** you rate each candidate independently, 0 to 5 — like rating movies. *Absolute and independent*: two candidates can both get 5, or everyone 0, because each rating stands alone.

The tell: in ranked ballots, equal marks are illegal. In scored ballots, equal marks are the whole point — that's how a voter says "I like these two the same."

**STAR** spells it out: **S**core **T**hen **A**utomatic **R**unoff. Voters star every candidate, the two highest *totals* advance, then the automatic runoff (the one idea borrowed from ranked voting) checks which finalist is preferred on more ballots.

> Terminology note: this project prefers **scored / scores / stars** over "rated / rating," because "rated" is the word most easily confused with "ranked." Equal-score ballots are counted as **Equal Support** in the runoff — they are **not** discarded.

---

## Quick start

All commands assume the project's virtualenv (`.venv` / `uv`).

**Tabulate an election file** — annotated echo on screen, plus a `_tabulated.txt` sibling:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py \
    01_STAR/your_election.yaml
```

**Import a BetterVoting JSON export** — converts every `*.json` in the folder into canonical YAML under `_generated/`:

```bash
python YAML_library/1_positive/01_convert_json_yaml.py
```

**Run the test suite** (from the engine directory):

```bash
cd STARVote_LH_tabulation_engine
pytest tests/
```

---

## Voting methods

Dispatched automatically from the file's `voting_method` (or from the ballot style — ranked `A>B>C` always routes to RCV-IRV):

- **STAR** — single-winner Score Then Automatic Runoff (the default).
- **Bloc STAR** / **proportional STAR** (`bloc`, `sss`, `rrv`, `allocated`) — multi-winner variants.
- **Approval** — score each candidate 0/1; most approvals wins.
- **Ranked Robin** (`RankedRobin`, aka RCV-RR / Copeland / Consensus) — every pair of candidates compared head-to-head; best win–loss record wins. Prints the full pairwise table and flags Condorcet cycles.
- **RCV-IRV** — ranked ballots, tabulated by the vendored RCV-IRV engine.

> Terminology: this repo says **RCV-IRV** (or **IRV**) for the instant-runoff count, reserving bare **RCV** for the ranked-ballot family. "RCV" loosely means IRV in US usage; we clarify once, then use the precise term. See [Tips — Terminology: RCV vs IRV vs RCV-IRV (and friends)](00_start_here/TIPS_terminology.md).

---

## Validation philosophy

The engine is the validator. Instead of crashing on a bad file, it prints a specific, human-readable error and exits cleanly — e.g. a missing `ballots:` block prints the key-components template; a ranked ballot under a score method explains the mismatch and how to fix it; generated `_tabulated.txt` files are refused as input. The **negative** pytest cases assert each malformed fixture produces the right message with no traceback, so the error UX itself is tested.

---

## The vendored engine

`STARVote_LH_tabulation_engine/` is a fork of Larry Hastings' `starvote`, kept in-tree so the examples and tests pin a known-good engine. Local additions (extra reporting, the preference matrix, the `[Divergence from STAR]` block, the `lot_numbers` tie-break wiring, clearer errors) are documented in [Fork Notes — starvote (vendored fork)](STARVote_LH_tabulation_engine/FORK_NOTES.md). Quick checks can use the system `python3`; the engines are vendored, not pip dependencies.

---

## Learn more

- [Start Here](00_start_here/00_START_HERE.md) — guided entry point
- [STAR Voting — Curriculum (Voting 101 / 201 / 301)](00_start_here/CURRICULUM.md) — levels 101 / 201 / 301
- [Glossary — voting methods & criteria](00_start_here/GLOSSARY.md) — terms, precisely defined
- [Concepts — deep-dive pages for the important terms](00_start_here/) — center squeeze, monotonicity, tie-breaking, STAR vs IRV…
- [CLAUDE.md — working guidance for this repo](CLAUDE.md) — house conventions for contributing consistently
