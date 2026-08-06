# YAML election files — why, what, how

Every claim in this library is backed by a **runnable election**: one small text file that a person can read and a tabulation engine can count. That file is YAML. This page explains **why** the format is YAML, **what** is actually in one of these files, and **how** a file travels from the moment you write it to the result you see on this website.

The folder you're standing in holds the two *ends* of that journey — the importer that brings real BetterVoting elections **in**, and the deliberately-broken files that prove bad input fails **politely**. Both are described [at the bottom](#whats-in-this-folder).

> **Teaching elections don't live here.** They live next to the lessons they teach — [`01_STAR/`](../01_STAR/README.md), [`02_STAR_Bloc/`](../02_STAR_Bloc/README.md), [`03_STAR_PR/`](../03_STAR_PR/README.md), [`method_comparisons/`](../method_comparisons/README.md) — one canonical copy each. Browse them all in the [test-case catalog](../07_Concepts/YAML_test_case_index/README.md).

---

## Why YAML

### One file, two readers

The design goal is a single artifact that is **human-readable and machine-runnable at the same time**. A person reads the scenario and the ballots and understands the election; the engine parses the very same file, tabulates it, and a test asserts the winner. No translation step, no second copy.

The usual alternative splits a test case in two — prose for humans (a doc describing the scenario) and data for machines (a fixture the code runs). The two **drift apart**: the doc says one thing, the fixture does another, and nobody notices until a count is wrong. You can't *read* the machine copy or *run* the human copy. This library refuses that split. There is one artifact, and it is legible both ways.

→ The argument in full, with the payoff: **[Why YAML? One file a person reads and a computer runs](why_yaml_test_cases.md)**

### Why YAML specifically, and not CSV or JSON

"One file, two readers" is the *goal*; YAML is the format that actually delivers it. Three of its features are doing the work — and each is exactly what the alternatives lack:

| Format | Why not |
|---|---|
| **CSV** | Holds the ballot grid beautifully and *nothing else* — no voting method, no seat count, no expected winner, no explanation. You'd end up with a CSV plus a sidecar file describing it, which is the drift problem again. |
| **JSON** | Machine-perfect, human-hostile. **No comments at all**, so a ballot row can never explain itself. The ballot grid becomes either an escaped one-line string or hundreds of nested objects — unreadable either way, and a nightmare to diff. |
| **Spreadsheet / database** | Not plain text: no meaningful `git diff`, no line-by-line review, no stable public URL, and it needs an application to open. |

What YAML adds on top of the grid:

1. **The literal block (`|-`) keeps a grid a grid.** Everything indented under `ballots: |-` is preserved *verbatim*, so the ballots stay aligned columns you can read down — not an escaped string, not nested objects.
2. **`#` comments survive in the file.** A ballot row can say what it demonstrates, right where it sits, and the engine ignores it.
3. **It's plain text.** Diffable, reviewable in a pull request, permanently linkable, and readable in any editor for the next twenty years.

> **And declaring the method is what makes validation possible at all.** A ballot is not valid or invalid on its own — `0,0,1,1` is a perfectly good Approval or STAR ballot and an **invalid Plurality** one, two votes in a one-vote race. Until the file names the method, the seats and the candidates, there is nothing to check the ballots *against*, and every stray comma, out-of-range score or ranked row passes silently. → **[Eight lines of CSV, eight questions](csv_ambiguity.md)** works all of it through on eight real ballots.

**The engine's own author reached the same conclusion — by a different route.** Larry Hastings gave `starvote` a native text format for exactly the reason above; his note at the bottom of the parser says he "got tired of CSV files." His answer, `.starvote`, is INI-like, and every ballot line *names* the candidate it scores, so nothing is positional. Ours is YAML, chosen because the same file also has to carry the scenario prose, the display options, and an enforced answer key. Both are doors into the same engine — and, worth knowing, they don't share a tie-break default: [The `.starvote` ballot file format](../07_Concepts/tabulation_engines/LH_starvote/starvote_file_format.md).

> **Nor is either one the standard.** The election-methods world has a dedicated ballot *interchange* format, **ABIF**, which packs ranks and scores into one dense line (`Allie/5 =Billy/5 >Candace/4`). It maps onto just our `ballots:` block — our file wraps method, options, and the answer key around it. Honest side-by-side: [ABIF vs. our YAML grid](../07_Concepts/scores_and_ranks/abif_format.md).

---

## What it is

The schema is **flat**. Only three keys are required: how to count, how many seats, and the ballots. A fourth — `expected_winners` — is what turns an election into a *test case*.

Here is a complete, real file. This is the repo's canonical leading example, [`bv2187_qrw6wb_ann-bob-cal.yaml`](../01_STAR/02_Examples/cases/bv2187_qrw6wb_ann-bob-cal.yaml), stripped to its essential keys:

```yaml
voting_method: STAR     # STAR | Approval | RankedRobin | RCV_IRV | bloc | sss | rrv | allocated
num_winners: 1          # seats to fill (1 = single-winner)
ballots: |-             # header row of candidate names, then one row per voter
  Ann,Bob,Cal
  5,4,0                 # this voter likes BOTH Ann and Bob — no vote-splitting fear
  3,5,2
  0,3,5
expected_winners:       # the answer key: the pytest suite finds this key and checks it
  - Bob
```

**The ballot grid, in five rules:**

- **Row 1 is the candidate names**, comma-separated. There is no separate `candidates:` key — the header row *is* the candidate list. Every voter row must have the same number of columns.
- **Scores are `0`–`5`.** (Approval ballots take only `0`/`1`. A file whose rows are written as *ranks* instead — `A>C>B` — routes to RCV-IRV automatically.)
- **Markers** record *why* a score is zero: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled and re-issued. All five tabulate as 0, but the file remembers the difference — a distinction a flat grid of numbers would flatten away. → [Abstention vs. a zero vs. "None of the Above"](../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md)
- **Weighted rows** prefix a count: `42 × 0,3,5`. House rule: weights must be **≥ 6**, so a count is never mistaken for a 0–5 score.
- **`# comments`** are allowed at the end of any row.

Everything else in the file is optional and additive: an `election_title`, a printable `scenario_description`, `options:` controlling how much of the report appears on screen, `lot_numbers:` pinning the official tie-break order, `eligible_voters` / `quorum` for turnout reporting, `blocs:` for the vote-splitting check.

That optional half follows one rule — **store rich, display clean**. Keep the context *in* the file and let `options:` decide what reaches the screen; you never have to delete information to get a tidy demo. → [Organizing the YAML files](ORGANIZATION.md)

→ Every field, every option, the full marker table, and the house style rules: **[YAML Test Case — Authoring Template](YAML_authoring_template.md)**

---

## How it works

Five stages. The same file carries through all of them:

```
 author ──▶ validate ──▶ tabulate ──▶ verify ──▶ publish
  │                         │                       │
  │                         ├─▶ on-screen report    └─▶ a browsable <name>.md page
  │                         └─▶ _tabulated.txt          (the reader-facing surface)
  │                             (the full audit record)
  ├─ hand-write the YAML, or
  └─ import a BetterVoting JSON export (converter → canonical YAML)
```

### 1. Author, or import

Write the file by hand from the [template](YAML_authoring_template.md) — or import a real election. [`1_positive/01_convert_json_yaml.py`](1_positive/01_convert_json_yaml.py) turns a BetterVoting JSON export into a canonical YAML: real candidate names as IDs, aligned columns, the election's official tie-break (lot) order, and an embedded answer key. That's how a live public election becomes a permanent, re-countable case here. → [BetterVoting and the engine](../07_Concepts/tabulation_engines/bettervoting_and_the_engine.md)

### 2. Validate — the engine is the validator

There is no separate lint step. Run the file, and every realistic mistake comes back as a **plain-language message with no traceback**, and a non-zero exit code:

```
Error: the number of scores per ballot doesn't match the number of candidates. There are 3 candidate(s) (Austin, Boston, Cairo), so each ballot row needs exactly 3 comma-separated score(s).
  Offending ballot(s)  [Austin,Boston,Cairo]:
    ballot 2: 4, 5   (has 2 value(s), expected 3)
  Tip: use the SAME separator for the header and every row — commas
       (or tabs), e.g. 'A, B, C' then '5, 4, 0'. Mixing commas and
       spaces is the usual cause of a wrong value count.
```

Every one of those messages is pinned by a deliberately-broken fixture in `2_negative/` — the safety net described below.

### 3. Tabulate

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/02_Examples/cases/bv2187_qrw6wb_ann-bob-cal.yaml
```

No flag says which method to use twice: `voting_method:` alone dispatches STAR (single / Bloc / PR), Approval, Ranked Robin, or RCV-IRV, and ranked ballots route themselves. The engine prints an annotated, round-by-round count — here the Scoring Round picks two finalists and the Automatic Runoff decides between them:

<!-- report:bv2187_qrw6wb_ann-bob-cal -->
```text
[Divergence from STAR]
  STAR                   = Bob
  Choose-One (Plurality) = Ann   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Ann,Bob,Cal
  5,  4,  0
  3,  5,  2
  0,  3,  5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bob           -- 12 -- First place
   Ann           --  8 -- Second place
   Cal           --  7
 Bob and Ann advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bob           -- 2 -- First place
   Ann           -- 1
   Equal Support -- 0
 Bob wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Bob 2 (67%)  ·  Ann 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bob
```
<!-- /report -->

Notice what the file never had to state: the totals, the finalists, the head-to-head count, the majority threshold. All of it is *derived* from those three ballot rows. **How much of it lands on screen** is the one thing the file does control — that's the optional `options:` block, which can hide the description, show the full pairwise grid, add the score-distribution table, and so on. It never changes the winner or the numbers.

→ The whole count for this election, every section forced on, plus the preference matrix and the score distribution: [`bv2187_qrw6wb_ann-bob-cal.md`](../01_STAR/02_Examples/cases/cases_pages/bv2187_qrw6wb_ann-bob-cal.md)

### 4. Verify

The same run writes a full-detail **`_tabulated.txt`** sibling — the audit copy, which ignores `options:` and always prints everything, headed by the name of the source file it came from.

Meanwhile the file's own answer key is enforced: **`expected_winners:`** in a hand-written case, an **`expected_results:`** block (per-round detail) in a BetterVoting import. A pytest suite discovers every file that has one and fails if the engine elects somebody else — alongside tests for the negative fixtures, the JSON→YAML conversion, the tie-break ladder, Ranked Robin, and non-vacuous self-checks that prove the winner check isn't rubber-stamping. It's wired into a pre-commit hook, so a regression can't land quietly.

```bash
cd STARVote_LH_tabulation_engine && pytest tests/test_single_winner_positive.py tests/test_negative_validation.py
```

### 5. Publish

Everything a reader sees is **generated from the YAML** and never hand-maintained in parallel:

- the **on-screen report** (what you show live),
- the full-detail **`_tabulated.txt`** record (the audit copy),
- the browsable **`.md` page** in `cases_pages/` (the reader-facing surface, built by [`build_yaml_pages.py`](../STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py)),
- the sortable **[registry and catalog](../07_Concepts/YAML_test_case_index/README.md)** of every case in the library.

Because they're generated, they can't drift from the source — and a pytest fails the suite if one does. Edit the YAML, regenerate, done.

> **House rule — link the `.md` page, not the raw `.yaml`.** The generated page is the reader-first surface: lead with it in tables, navs, and cross-references, and link a `.yaml` only when the *runnable source* is genuinely the point (a "run this file" command). See [CLAUDE.md](../CLAUDE.md).

None of this is a black box that prints a winner. The point of the whole chain is that the count stays **legible and reproducible** — one file that **teaches**, **runs**, **verifies**, and **audits**.

---

## What's in this folder

Two jobs, at opposite ends of the pipeline above.

### `1_positive/` — the BetterVoting import pipeline

- `01_convert_json_yaml.py` — converts a real BetterVoting JSON export into a canonical election YAML (real candidate names, aligned columns, the election's official lot order, embedded `expected_results`).
- Converter input: the frozen real BetterVoting export lives at
  `01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/…_bv_export.json`
  (the test copies it into a temp dir; nothing here is mutated).
- [`lot_tiebreak_bv_order.yaml`](1_positive/lot_tiebreak_bv_order.yaml) / [`lot_tiebreak_published_order.yaml`](1_positive/lot_tiebreak_published_order.yaml) — a matched pair, and a neat demonstration of why the tie-break order belongs *in the file*. Identical ballots (`4,0` and `0,4` — a dead-tied two-candidate race); the only difference is `lot_numbers:`, and it decides the election: BetterVoting's drawn order elects **Ben**, the pre-published deterministic order elects **Ada**.
- `_generated/` + `_generated_tabulated/` — converter output and its tabulation mirror.

Guarded end to end by [`tests/test_json_to_yaml_conversion.py`](../STARVote_LH_tabulation_engine/tests/test_json_to_yaml_conversion.py) and [`tests/test_lot_number_tiebreak.py`](../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py) (export → converter → YAML → engine).

### `2_negative/` — the validation safety net

Every file here is a deliberately broken election that must make the engine **reject it with a plain-language, user-friendly error and no traceback** — which is what makes stage 2 above trustworthy for anyone writing YAML by hand. Every realistic mistake gets a fixture, and the fixture pins the exact message the author will see.

**Self-describing contract** — each fixture declares its expected message as comments, so adding a case never touches the test suite:

```yaml
# NEGATIVE: what's wrong with this file, in one line.
# expect: substring that must appear in the error output
# expect: another required substring
voting_method: STAR
...
```

[`tests/test_negative_validation.py`](../STARVote_LH_tabulation_engine/tests/test_negative_validation.py) auto-discovers every `*.yaml` here and asserts: non-zero exit, no traceback, an `Error:` message, and every declared `# expect:` substring. A fixture that tabulates "successfully" is a bug.

**Covered mistake catalog** (each has a fixture): bad YAML syntax · missing / empty ballots · ballots written as a YAML list instead of a `|-` block · wrong / extra columns · out-of-range, negative, decimal, and two-digit scores · invalid characters and the removed `^` marker · ranked ballots under a score method (STAR and Approval) · mixed ranked + score rows · 0–5 scores under Approval · unknown `voting_method` (typos get a "did you mean" suggestion) · `num_winners` zero / non-numeric / exceeding the candidate count · single-winner method asked for multiple seats · duplicate candidate names · `lot_numbers` naming a candidate not on the ballot · header with no voter rows · a completely blank file, comments-only file, and empty ballots block · multiple races in one YAML (one election per file; multi-race BV *JSON* exports are legitimate — the converter splits them into one YAML per race) · duplicate top-level keys (YAML silently keeps the last!) · two `---` YAML documents in one file · multiple errors reported together.

→ The reasoning behind failing this loudly: [Validation philosophy](../07_Concepts/about_this_repo/repository_guide.md#validation-philosophy)

---

## History note

Until 2026-07 this folder also held flattened copies of the `Runoff_*`, `Flat_scores_ties_*`, `Whoops_*`, and `center_squeeze_voteline_1d` teaching cases. They had already diverged from their canonical siblings and the test harness runs the canonical files directly, so the copies were removed. If you need one of those cases, use the canonical copies in their current homes: `01_STAR/04_Real_Elections/runoff_reversal_bv_cases/cases/`, `01_STAR/09_Parked/Flat_scores_ties/cases/`, `method_comparisons/paradoxes_and_whoops/cases/`, and `method_comparisons/center_squeeze/cases/`.

# file: README.md
