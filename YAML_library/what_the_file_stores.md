# What the file stores — and why the answer key isn't a report

**Level: reference · deep dive**

**One line:** a case file stores the election's **inputs** and a one-line **answer key**; every report in this library is *generated* from that file and never typed beside it.

A case file has three sections, in this order:

| # | Section | Keys | Who reads it |
|---|---|---|---|
| 1 | **Context and parameters** | `election_title`, `scenario_description`, `voting_method`, `num_winners`, and the optional extras (`lot_numbers`, `quorum`, `blocs`, `options`) | a person, plus the engine for the parameters |
| 2 | **The ballots** | `ballots: \|-` | both |
| 3 | **The expected result** | `expected_winners` | a person, and the pytest suite |

Here is the whole of section 3, in the repo's [canonical leading example](../01_STAR/02_Examples/cases/bv2187_qrw6wb_ann-bob-cal.yaml):

```yaml
expected_winners:
  - Bob
```

That's it — a name. Not the scoring round, not the runoff, not the matrix. This page is about that decision, because it's the one people (including this repo's own author) reliably expect to have gone the other way.

---

## The question

If the file already carries the scenario *and* the ballots *and* the verdict, why not carry the **count** too — the round-by-round report — so one file holds the whole election end to end?

It's a fair question, it was the original design, and the machinery for it still exists. Three forms of "expected" have lived in this repo:

| Form | Holds | Files today |
|---|---|---|
| `expected_winners:` | a list of names | **564** — every hand-written case |
| `expected_results: winners:` | the same list, nested | **28** — BetterVoting imports, written by the [converter](1_positive/01_convert_json_yaml.py) |
| `expected_results:` + `report: \|-` | names **and** the full plain-text count | **0** |

The third row is not a missing feature. Run any file with **`--save`** and the engine writes it for you:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/02_Examples/cases/bv2187_qrw6wb_ann-bob-cal.yaml --save
```

That appends an `expected_results:` block holding the winners **and** the whole ANSI-stripped report, indented into the YAML. It works. Nothing in the library uses it, and the converter that *defaults* to embedding the report has its own note at the branch — *"MINIMAL yaml: keep the expected winner, drop the bulky report"* — which is why all 28 imported cases carry winners only.

---

## Why the report isn't stored

### 1. An answer key has to be independent of the engine

You write `expected_winners: Bob` because *you* worked out that Bob wins — from the ballots, by hand or from BetterVoting's own published result. The engine then has to agree with you. That's a real test: two independent parties, one claim.

A pasted report is copied **from** the engine. It can only ever test the engine against a snapshot of itself — and a snapshot taken at the moment someone happened to run `--save`. It proves the engine still prints what it printed, which is a much weaker thing than proving it still elects who it should elect.

### 2. Snapshots break on cosmetic changes, and the diff looks identical to a regression

On 2026-08-09 the runoff summary became default-on and grew its reconciling funnel:

```text
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Bob 2 (67%)  ·  Ann 1 (33%)
```

Nothing about any winner changed. With reports stored in the sources, that one improvement would have rewritten **564 case files**, and the resulting diff — hundreds of files, thousands of changed report lines — would have been indistinguishable, on review, from a count that had silently gone wrong. The library would have learned to skim exactly the diff it most needs to read.

### 3. It's already there, in a file with the same name

Every run writes a full-detail audit copy beside the source, same stem, in the folder's `_tabulated` mirror:

```text
01_STAR/02_Examples/cases/bv2187_qrw6wb_ann-bob-cal.yaml
01_STAR/02_Examples/cases/cases_tabulated/bv2187_qrw6wb_ann-bob-cal_tabulated.txt
```

The [mirror](../01_STAR/02_Examples/cases/cases_tabulated/bv2187_qrw6wb_ann-bob-cal_tabulated.txt) ignores every display option and prints *everything* — the preference matrix, the Condorcet check, the score distribution, both rounds, the divergence block. It is strictly more complete than anything `--save` would have embedded, it is regenerated on every run, and a pytest fails the suite when it drifts. Storing a second copy in the source buys nothing and adds a way to be wrong.

### 4. Size, and what a reader is looking at

The canonical file is **44 lines**; its mirror is **137**. Fold the report in and the ballots — the thing a reader came for — sit at the top of a file that's mostly output. The house rule is *store rich, display clean* ([ORGANIZATION.md](ORGANIZATION.md)); a stored report is the opposite trade, storing what's already derivable and crowding the screen with it.

### 5. Two truths in one artifact

The whole design is **one file, one truth** — that's what [Why YAML](why_yaml_test_cases.md) argues: no prose copy drifting from a data copy. An input file that also contains an output contains something that goes stale the moment a ballot changes. When the stored report and the live count disagree, which one is the case? There is no good answer, so the situation is designed out.

---

## Where the count actually lives

Four generated surfaces, all derived from the YAML, none hand-maintained:

| Surface | What it's for |
|---|---|
| the **on-screen report** | what you show live; house defaults keep it tight, `--full` shows everything |
| **`<stem>_tabulated.txt`** | the audit record — always full detail, same stem as the YAML |
| the **`cases_pages/<stem>.md`** page | the reader-facing surface, teaching first and the full count at the bottom |
| the **[registry and catalog](../07_Concepts/YAML_test_case_index/README.md)** | every case in the library, sortable |

And when a hand-written lesson needs a count *on the page*, it doesn't paste one either — it marks the spot and the page builder fills it from that case's generated page:

```text
<!-- report:<the case's stem> -->
<!-- /report -->
```

Same principle, one level up: the report is generated into the lesson, so it can't drift from the file it claims to describe. A `check_pasted_reports` hygiene check fails the build on a hand-pasted one. → [CLAUDE.md](../CLAUDE.md)

---

## History

The original schema *did* store the report. Before the Larry Hastings engine landed (2026-05-17), cases used a nested `test_election_parameters:` shape, and one of the thirteen files then in the repo — `YAML_library/1_positive/bv22.yaml` — carried a hand-typed block:

```yaml
      expected_winner: Carmen
      expected_report: |
        Candidate Votes Percentage
        ========= ===== ==========
        Andre     0     0%
        Blake     2     40.00%
        Carmen    3     60.00%

        Votes tallied: 5
        Abstentions: 1
```

It never spread past that one file, and it went away with the old schema on the day the engine arrived and started writing `_tabulated` mirrors — a generated report making a typed one redundant the same week it would have had to be maintained by hand. `--save` is what survived of the idea: still implemented, still correct, and deliberately not the house form.

**If you do want a self-contained file** — handing one election to someone with no checkout, or snapshotting a report before an engine change to diff against afterwards — `--save` is exactly the tool. Just don't commit the result as a case file: the tests read `expected_winners`, and nothing checks a stored report.

---

## See also

- [YAML election files — why, what, how](README.md) — the format's front door, and the five stages a file travels
- [Why YAML? One file a person reads and a computer runs](why_yaml_test_cases.md) — the one-artifact argument this page applies
- [Organizing the YAML files](ORGANIZATION.md) — store rich, display clean
- [YAML Test Case — Authoring Template](YAML_authoring_template.md) — every field, ready to copy

# file: what_the_file_stores.md
