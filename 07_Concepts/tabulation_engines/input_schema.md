# The election contract — the input half, one JSON document per contest

**Level: reference · deep dive**

**One line:** [the result contract](result_schema.md) made a *count* comparable between engines; this is the missing other half — a normalized, language-neutral description of the *election* itself, so that two implementations provably read the same contest from the same bytes.

This page is addressed to **implementers**, like its companion. If you are here to learn STAR, start at [01_STAR](../../01_STAR/README.md) instead.

> **Status: proposed. Nothing emits this yet.**
>
> [`result_schema.md`](result_schema.md) documents something that ships — `--json` works today. This page documents a **design**, published so it can be argued with before anything is built on it. The reference reader is still the YAML case file, and the schema below has no producer. What exists is the schema, the illustrations, and a test asserting they agree. The one piece of code it waits on is named at the [bottom](#what-would-have-to-be-built).

---

## Which goal this serves — read this before the design

A schema is only assessable against a purpose. [The requirements page](rust_kernel_requirements.md) puts it sharply: *"Each candidate goal produces a materially different library. Two co-primary goals is the same as no goal."* So this one names its goal rather than leaving it implicit.

**This schema is built for [G6 — a shared conformance suite](rust_kernel_requirements.md#g6-a-shared-conformance-suite-that-other-projects-adopt)**, the goal that page calls *"quietly the highest-leverage on this list, and the least glamorous."* It is also the goal that **survived** the 2026-08-10 decision that this library gets no Rust kernel: Track A is Python work that is worth doing whether or not any Rust is ever written, and this is Track A. The Rust section further down exists because a reference implementation is how you prove a suite is implementable by someone who did not write the Python — not because a kernel is planned.

What that choice buys, and what it costs, under the other goals:

| Goal | Does this schema matter? | What would have to change |
|---|---|---|
| **G1** — live tabulation in the browser (WASM) | **Yes — it is the wire format.** JSON in/out, no filesystem, small documents | Almost nothing. `source` and `expected` are already optional, and a teaching page hands the kernel structured data with no answer key. Aggregated `count` rows are ideal here |
| **G2** — exhaustive ballot-space search | **Barely.** Elections are generated in memory; JSON never enters the hot loop | The schema becomes an **output**, not an input — a discovered counterexample is emitted back as a YAML case file so the finding lands in the library. What matters is that `tabulate()` takes structs, not a document |
| **G3** — an independent third implementation | Yes — same requirements as G6 | Nothing |
| **G6** — a shared conformance suite | **It is the deliverable** | — |
| **G7** — audit artifacts and risk-limiting audits | Yes, but **the aggregation breaks** | An RLA samples *individual* ballots. `{ "count": 42, "scores": […] }` collapses 42 ballots into one row and destroys the identity an audit draws on. G7 needs one row per ballot, with batch / precinct / CVR id |
| **G8** — counting encrypted ballots | **Incompatible as written** | Each ballot is individually encrypted, so identical patterns have *different* ciphertexts and cannot be merged into a `count`. Also only the score and approval families are additively [summable](../topics/summability/README.md); IRV is not |

The G7/G8 row is the honest limit and worth stating plainly: **`count` aggregation is a fixture-format optimization, and it is what stops this from being quietly promoted to a production format.** That is the same boundary [the reference package](star_reference_package.md) draws — *a fixture format should be self-contained*, a production one must not be — and it is a reason to keep the two documents separate rather than a defect to fix.

Everything below assumes G6. Under a different primary goal, read the table above first and expect the design to move.

---

## Why the input needs a contract too

The result contract closed a real gap: an engine could get all 567 answer keys right by the wrong path. But it assumed something it never checked — that the two engines being compared had *read the same election*. Two measurements say that assumption does not survive contact with a second language.

### 1. Identical bytes, two different elections

The case corpus is YAML, and the reference reader is PyYAML, which implements **YAML 1.1**. Every YAML parser in the Rust, Go, and modern JS ecosystems implements **YAML 1.2 core schema**. Probed directly, PyYAML 6.0.3 against `serde_yaml` 0.9.34:

| Written in a case file | PyYAML 6.0.3 (the reference) | `serde_yaml` 0.9.34 (any port) |
|---|---|---|
| `No` | `False` (bool) | `"No"` (string) |
| `Yes` | `True` (bool) | `"Yes"` (string) |
| `Off` | `False` (bool) | `"Off"` (string) |
| `NO` | `False` (bool) | `"NO"` (string) |
| `12:30` | `750` (int, base-60) | `"12:30"` (string) |
| `007` | `7` (int) | `"007"` (string) |

The port is *more correct* on all six, which is exactly what makes this dangerous: conformance here means agreeing with the reference, so a correct implementation would be scored as divergent. A ballot measure (`expected_winners: [No]`), a themed cast (`007`), a time-named contest (`12:30`) all trigger it. `check_yaml_name_types` guards the Python side of this and can do nothing about the other.

The sharp version, and the reason `source.sha256` does not save you: **the hash proves two engines read the same bytes. It cannot prove they read the same election.** Hashing a normalized document instead is what closes that.

### 2. The ballot block is a bespoke DSL, and a third of the corpus depends on its forgiving edges

`ballots:` is a YAML block literal — opaque to YAML, hand-parsed by [`parse_ballots_from_string`](../../STARVote_LH_tabulation_engine/starvote_larry_hastings.py) and its helpers. Census of the 612 ballot-carrying files:

```text
 218  ranked (>)                       — no candidate header at all; names discovered by first appearance
 193  inline # comments
 183  space-aligned — no commas anywhere; rescued by a heuristic normalizer
 117  weighted (Count: header)         — and a bare `42: 5,4,3,2` weight works without one
  33  markers  -  ~  &  ?  %
  12  equal ranks (=)
```

Plus a compact underscore form (`052_225_323`) and `#,`-prefixed comment rows. **183 files are not comma-delimited.** They parse only because `_normalize_ballot_separators` sniffs whitespace-aligned columns and rewrites them, refusing when the columns are ragged. A second engine that splits on commas fails 30% of the corpus; a second engine that reimplements the sniffer now has two heuristics that must agree forever.

That is the port tax, and it is entirely avoidable. [The Rust scope note](rust_kernel_scope.md) already reached the same conclusion from the other direction: *"Let the Rust side be strict and read a normalized input."*

---

## The shape

One document is **one contest counted one way** — the same unit as a result object, so the two line up. A multi-race file becomes N documents.

```text
schema_version   the contract's version, not any engine's
source           optional provenance: what this was generated from
election         title · method · family · seats · ballot   ← the paper is declared HERE
candidates       [{ id, name }]                             ← identity, separate from display
ballots          rows whose shape is fixed by election.ballot.type
rules            winner-affecting choices the method name alone does not settle
tiebreak         the floor, named rather than defaulted
expected         the answer key — able to say "nobody"
```

Machine-readable: [`star_election.schema.json`](../../STARVote_LH_tabulation_engine/star_election.schema.json) (JSON Schema draft 2020-12).

**Five ballot types cover nineteen methods**, which is the structure worth seeing before the examples: `score` · `approval` · `choose` · `ranking` · `grade`. That is not a simplification — it is the observation that a method is a *counting rule applied to a piece of paper*, and this library already draws exactly three of those papers.

---

## One illustration per method

Every election below is a real case file, so each is checkable. The first is shown whole; the rest show only what distinguishes them, since the envelope never changes.

### STAR — the baseline

[`09_c4_b100_tennessee-capital`](../../01_STAR/02_Examples/cases/cases_pages/09_c4_b100_tennessee-capital.md), the same election [the result contract](result_schema.md) uses, so input and output can be read as a pair.

```json
{
  "$schema": "https://masiarek.github.io/star-voting-library/STARVote_LH_tabulation_engine/star_election.schema.json",
  "schema_version": "1.0.0",
  "source": {
    "file": "09_c4_b100_tennessee-capital.yaml",
    "sha256": "356c519bd232dc0484f1574dffc3be3342083c30ad8b4ddc9d026df82f4c58e1"
  },
  "election": {
    "title": "Tennessee Capital — classic STAR example",
    "declared_method": "STAR",
    "method": "star",
    "family": "score",
    "seats": 1,
    "ballot": { "type": "score", "min": 0, "max": 5 }
  },
  "candidates": [
    { "id": "memphis",     "name": "Memphis" },
    { "id": "nashville",   "name": "Nashville" },
    { "id": "chattanooga", "name": "Chattanooga" },
    { "id": "knoxville",   "name": "Knoxville" }
  ],
  "ballots": [
    { "count": 42, "scores": [5, 4, 3, 2] },
    { "count": 26, "scores": [2, 5, 4, 3] },
    { "count": 15, "scores": [2, 3, 5, 4] },
    { "count": 17, "scores": [2, 3, 4, 5] }
  ],
  "expected": { "outcome": "elected", "winners": ["nashville"] }
}
```

**No `rules` object.** That is the finding, not an omission: STAR's ladder is fixed by Equal Vote's Official protocol, the runoff denominator is the rule rather than a setting, and the lot order is already `tiebreak`. A STAR contest has essentially nothing to configure — which is a fact worth having a format able to *show*.

### STAR with markers — what a blank is

[`03d_c5_b5_style-gallery-five-more`](../../01_STAR/02_Examples/cases/cases_pages/03d_c5_b5_style-gallery-five-more.md). All five markers tabulate as the bottom of the scale; the distinction they preserve is what the voter *did*.

```json
{
  "election": { "method": "star", "family": "score", "seats": 1,
                "ballot": { "type": "score", "min": 0, "max": 5 } },
  "ballots": [
    { "scores": [5, 0, 5, 0, 0], "note": "approval-style: only 0s and 5s" },
    { "scores": [null, null, 5, 3, null], "note": "partial ballot — knows only Clara and Diego" },
    { "scores": [3, 3, 3, 3, 3], "note": "null ballot — no preference anywhere" }
  ]
}
```

| YAML glyph | JSON | Means |
|---|---|---|
| `-` | `null` | left blank |
| `~` | `"abstain_race"` | abstained from the whole contest |
| `&` | `"abstain_candidate"` | abstained on this candidate |
| `?` | `"spoiled"` | spoiled |
| `%` | `"spoiled_reissued"` | spoiled and reissued |

Names rather than glyphs, because this document is read by strangers who do not have the repo's marker table in front of them. The named markers are not decoration — [`bv655_jfrk9t_equal_opposition`](../../01_STAR/04_Real_Elections/abstain_bugs/cases/cases_pages/bv655_jfrk9t_equal_opposition.md) is a real election that turns on the difference between scoring a candidate zero and not marking them at all:

```json
{
  "election": { "method": "star", "family": "score", "seats": 1,
                "ballot": { "type": "score", "min": 0, "max": 5 } },
  "candidates": [ { "id": "opt1", "name": "Option 1" }, { "id": "opt2", "name": "Option 2" } ],
  "ballots": [
    { "scores": [0, 0], "note": "explicit equal opposition — rejects both" },
    { "scores": [5, "abstain_candidate"], "note": "Option 2 left blank" }
  ]
}
```

### Bloc STAR — seats, and a published lot

[`b484mbm_tie_every_rung`](../../02_STAR_Bloc/02_Examples/cases/cases_pages/b484mbm_tie_every_rung.md): three voters, three candidates, two seats, and every deterministic rung level, so the floor fills both seats.

```json
{
  "election": { "method": "bloc_star", "family": "score", "seats": 2,
                "ballot": { "type": "score", "min": 0, "max": 5 } },
  "candidates": [ { "id": "arden", "name": "Arden" },
                  { "id": "blythe", "name": "Blythe" },
                  { "id": "corin", "name": "Corin" } ],
  "ballots": [ { "scores": [3, 4, 5] }, { "scores": [5, 3, 4] }, { "scores": [4, 5, 3] } ],
  "tiebreak": { "floor": "published_lot", "lot_order": ["blythe", "arden", "corin"] },
  "expected": { "outcome": "elected", "winners": ["blythe", "arden"] }
}
```

`tiebreak.floor` is stated rather than assumed. On this election it is the *only* thing that decides anything, and an engine defaulting to a different floor is not wrong — it is answering a question this file failed to ask.

### STAR-PR (Allocated Score) — declared precision

[`bhk27tk_fewer_voters_than_seats`](../../03_STAR_PR/03_Criteria/bv_fixture_crosscheck/cases/cases_pages/bhk27tk_fewer_voters_than_seats.md). Same paper as STAR; a different count, with fractional reweighting.

```json
{
  "election": { "method": "allocated", "family": "score", "seats": 3,
                "ballot": { "type": "score", "min": 0, "max": 5 } },
  "ballots": [ { "scores": [5, 5, 0, 0] }, { "scores": [5, 4, 3, 0] } ],
  "rules": { "decimal_places": 6 },
  "tiebreak": { "floor": "published_lot" }
}
```

`decimal_places` answers a question [the scope note](rust_kernel_scope.md) left open as *"rationals or floats?"* — the production answer is **neither**. Fixed-point at a declared precision is reproducible across platforms (floats leak summation order under reweighting) *and* hand-auditable (nobody canvasses a fraction with a 40-digit denominator). This is RCTab's `decimalPlacesForVoteArithmetic`, and it is the best single idea in that file.

### Approval — three marks, not two

[`sav_strategy_bullet_vote_c5_b2`](../../04_Approval/03_Criteria/cases/cases_pages/sav_strategy_bullet_vote_c5_b2.md). On the double-bubble paper this library draws, an explicit **No** and an unmarked candidate are different marks that count the same.

```json
{
  "election": { "method": "approval", "family": "approval", "seats": 1,
                "ballot": { "type": "approval", "form": "double_bubble" } },
  "ballots": [
    { "approvals": [true, true, true, false, false] },
    { "approvals": [false, false, false, true, true] },
    { "approvals": [true, null, null, null, null], "note": "bullet vote — the rest left blank" }
  ]
}
```

Booleans, not `1`/`0` — an approval ballot is not a score ballot with `max: 1`, and modelling it as one loses the third state. Bloc Approval is the identical document with `"method": "approval_multi_winner"` and `"seats": 3`: the count changes, the paper does not.

### Choose-One and SNTV — where the overvote rule lives

[`bpv_bakery_block_plurality_c4_b12`](../../method_comparisons/block_preferential/cases/cases_pages/bpv_bakery_block_plurality_c4_b12.md).

```json
{
  "election": { "method": "sntv", "family": "plurality", "seats": 2,
                "ballot": { "type": "choose", "marks_allowed": 2, "overvote": "count_all" } },
  "ballots": [ { "count": 7, "marks": [true, true, false, false] },
               { "count": 5, "marks": [false, false, true, true] } ]
}
```

Single-winner Choose-One is the same document with `"marks_allowed": 1, "overvote": "spoil"`. That difference is **not derivable** — single-winner spoils an overvote so it counts for nobody, multi-winner counts every mark — and deriving one from the other elected the wrong slate on five block-voting cases in this library before the result contract was built off the engine's own tallies. Putting it on the ballot makes it impossible to assume.

### Ranked Robin — rank levels as sets

[`ranked_robin_intro_c3_b7`](../../05_Ranked_Robin/02_Examples/cases/cases_pages/ranked_robin_intro_c3_b7.md), then the equal-rank form from [`bv2140_48hjkv_most_pairwise_wins`](../../05_Ranked_Robin/02_Examples/condorcet_vs_ranked_robin/cases/cases_pages/bv2140_48hjkv_most_pairwise_wins.md).

```json
{
  "election": { "method": "ranked_robin", "family": "ranked_robin", "seats": 1,
                "ballot": { "type": "ranking", "equal_ranks": "allowed", "truncation": "allowed" } },
  "ballots": [
    { "count": 3, "ranking": [["ada"], ["ben"], ["cara"]] },
    { "count": 6, "ranking": [["ava", "bianca", "cedric"], ["eli"], ["deegan"]] },
    { "count": 9, "ranking": [["bianca", "deegan"], ["eli"], ["cedric"]] }
  ],
  "rules": { "copeland_draw_value": 0.5 }
}
```

Always array-of-arrays. Equal ranks stop being a syntax special case, truncation is just a shorter list, and — the part that matters — **preference is expressed once, by position.** [ABIF's hybrid form](../scores_and_ranks/abif_format.md) writes `Allie/5 >Billy/6`, encoding the order in both the operator and the number, where nothing forces the two to agree. Two sources of truth for one fact is a footgun; this has one.

`copeland_draw_value` is a genuine knob, and a contested one: `0.5` is what every implementation does, `0` is what Ranked Robin's published definition literally says. They come apart the moment a head-to-head is drawn — *before* any tie-break rung is reached.

### RCV-IRV — the rules that are really about the paper

[`RCV_ballot_example`](../../06_Other/RCV_IRV/cases/cases_pages/RCV_ballot_example.md).

```json
{
  "election": { "method": "rcv_irv", "family": "irv", "seats": 1,
                "ballot": { "type": "ranking", "equal_ranks": "forbidden",
                            "truncation": "allowed", "max_rankings": 3 } },
  "ballots": [ { "count": 40, "ranking": [["a"], ["c"], ["b"]] },
               { "count": 35, "ranking": [["b"], ["c"], ["a"]] },
               { "count": 25, "ranking": [["c"], ["a"], ["b"]] } ],
  "rules": { "overvote_rule": "exhaust_immediately", "max_skipped_ranks": 1,
             "batch_elimination": false }
}
```

`max_rankings` is a property of the printed grid, and it is where a large share of [exhausted ballots](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) actually come from: a 3-rank grid in a 6-candidate contest manufactures them regardless of how anyone votes. A format that cannot say "the paper only had three columns" cannot distinguish a voter who *chose* to truncate from one who ran out of boxes.

### STV — the quota is a choice

[`ex14_two_novels`](../../01_STAR/05_Practice/cases/cases_pages/ex14_two_novels.md).

```json
{
  "election": { "method": "stv", "family": "stv", "seats": 2,
                "ballot": { "type": "ranking", "equal_ranks": "forbidden", "truncation": "allowed" } },
  "ballots": [ { "count": 5, "ranking": [["austen"], ["bronte"], ["camus"], ["dickens"]] },
               { "count": 1, "ranking": [["bronte"], ["camus"]] },
               { "count": 3, "ranking": [["camus"], ["dickens"]] } ],
  "rules": { "quota": "droop_exact", "decimal_places": 6 }
}
```

Two published Droop quotas exist and differ by one vote; part (f) of that exercise works these same ballots both ways and gets different answers. `rounds.quota` in the result contract *reports* which one ran — this is where it gets *told*.

### Score / Range at 0–9 — the format outliving the guardrail

[`range_101_0to9_c3_b5`](../../06_Other/Range/cases/range_101_0to9_c3_b5.yaml). The LH engine refuses this with `UnsupportedMethod`; the document is still perfectly well-formed.

```json
{
  "election": { "method": "range", "family": "score", "seats": 1,
                "ballot": { "type": "score", "min": 0, "max": 9 } },
  "ballots": [ { "scores": [9, 7, 0] }, { "scores": [9, 6, 1] }, { "scores": [0, 8, 9] },
               { "scores": [1, 9, 8] }, { "scores": [0, 9, 7] } ]
}
```

The 0–5 cap is this fork's **teaching guardrail**, not an engine limit — Larry's `starvote` is range-parametric. `min`/`max` are required fields precisely so no reader can bake `0..=5` into a type.

### Combined Approval — a scale that goes negative

[`cav_library_board_c3_b12`](../../06_Other/Combined_Approval/cases/cav_library_board_c3_b12.yaml). CAV is a real **−1 / 0 / +1** ballot: For, abstain, Against.

```json
{
  "election": { "method": "cav", "family": "score", "seats": 1,
                "ballot": { "type": "score", "min": -1, "max": 1 } },
  "ballots": [ { "count": 4, "scores": [1, -1, 0] },
               { "count": 4, "scores": [-1, 1, 0] },
               { "count": 3, "scores": [0, 0, 1] },
               { "count": 1, "scores": [0, 0, 0] } ]
}
```

The YAML for this case encodes the scale **offset by one** — `2 = For, 1 = abstain, 0 = Against` — with a comment explaining why, because the shared ballot parser cannot read a minus sign. That is a workaround for a parser leaking into the description of a ballot, and it is the clearest single argument for a format with a declared scale: here the paper is described as the paper actually is.

### Majority Judgment — words, and a transposed source

[`mj_101_c3_b5`](../../06_Other/Majority_Judgment/cases/mj_101_c3_b5.yaml). This is where the input contract **adds** coverage: grade cases are not LH election files at all, so they have no `_tabulated` mirror, no generated page, and no entry in the result contract.

```json
{
  "election": { "method": "majority_judgment", "family": "grade", "seats": 1,
                "ballot": { "type": "grade",
                            "scale": ["To Reject", "Poor", "Acceptable", "Good", "Very Good", "Excellent"] } },
  "candidates": [ { "id": "alice", "name": "Alice" }, { "id": "bruno", "name": "Bruno" },
                  { "id": "cleo", "name": "Cleo" } ],
  "ballots": [
    { "grades": ["Excellent", "Very Good", "Good"], "note": "An Alice enthusiast" },
    { "grades": ["Excellent", "Very Good", "Good"], "note": "The same again" },
    { "grades": ["Good", "Very Good", "Acceptable"] },
    { "grades": ["Poor", "Good", "Acceptable"] },
    { "grades": [null, "Poor", "Acceptable"], "note": "Left Alice ungraded" }
  ],
  "rules": { "ungraded": "bottom_of_scale" },
  "expected": { "outcome": "elected", "winners": ["bruno"] }
}
```

Three things this one shows. The scale is **words, worst first** — Balinski and Laraki's claim is not "six levels" but a shared common language, so it travels with the ballot instead of being a constant. `ungraded` is a **rule, not bookkeeping**: it is the entire mechanism of the truncation paradox. And the source `grades:` block is **transposed** (a row per candidate, a column per voter), so the emitter transposes it back — every ballot row in this format is one voter, without exception.

### The answer key that can say "nobody"

Two cases in this library assert nothing today, because `expected_winners:` has no way to express their point. Here they do:

```json
{ "expected": { "outcome": "no_winner", "reason": "quorum not met" } }
```
```json
{ "expected": { "outcome": "rejected", "reason": "3 seats, 3 candidates — refused" } }
```

`"elected"` requires a `winners` array; the other two forbid one. *We did not check*, *we checked and nobody won*, and *this must not tabulate at all* stop looking alike.

---

## Prior art — and where it is wrong

Worth grading rather than deferring to. Certified is not the same as well-designed, and the most instructive parts of RCTab's config are the parts not to copy.

### RCTab — the only certified one, and a mixed model

RCTab's contest config is JSON: `outputSettings`, `cvrFileSources`, `candidates`, `rules`, with the **ballots in separate files named by path**. [Its config reference](rctab.md) is a `.txt` document, not a schema.

**Take:**

- **Anything that can move a winner is required, with no default.** `tiebreakMode`, `overvoteRule`, `winnerElectionMode`, `maxSkippedRanksAllowed`, `maxRankingsAllowed`, `decimalPlacesForVoteArithmetic` are all mandatory. This is the single best idea in election-software configuration and the posture the rest of this schema copies. It is also a *correction* to a natural instinct — "STAR has no knobs, so omit the block" is right about STAR and wrong as a policy.
- **Conditional requirements.** `randomSeed` is required *if and only if* the tiebreak mode is random. The schema encodes the dependency instead of trusting a reader.
- **Declared fixed-point precision**, discussed above.
- **A version-refusal policy.** RCTab hard-refuses a config newer than itself rather than guessing.
- **Candidate identity separate from the CVR string** (`code`), and `excluded` for a withdrawn candidate — a real state this library had no way to express.

**Reject:**

- **Physical layout indices in the config.** `firstVoteColumnIndex`, `firstVoteRowIndex`, `idColumnIndex`, `precinctColumnIndex` — 1-based integers describing where the data sits in a spreadsheet. This is CSV scraping, not a data format: insert a column and the config silently reads the wrong field. It exists because vendors export inconsistent CSVs, which is a real constraint and still a symptom rather than a model. [rcv-lab.org's generic CSV](rcv_lab.md) has the same shape of bug in the wild — it takes the first column as a ballot ID and returns a **wrong winner with no warning**.
- **Output settings inside the input.** `outputDirectory`, `tabulateByPrecinct`, and a `contestName` whose documented job is *naming output files*. Mixing "what to count" with "where to write it" makes the document non-portable and spoils it as a hashable specification of a contest. A pure input should not know that output exists.
- **A flat, unscoped `rules` bag.** `hareQuota`, `multiSeatBottomsUpPercentageThreshold` and `continueUntilTwoCandidatesRemain` sit in the same object no matter the election mode, so a single-winner config carries inert STV knobs. RCTab gets away with it because everything it counts is ranked; across six families it would be exactly the noise that got the `options:` block [deleted from 501 case files](../../CLAUDE.md).
- **Fields whose meaning depends on the provider.** `candidates` must be left *empty* when the CVR is CDF. A field that is authoritative in one configuration and ignored in another cannot be validated by a schema, and is a standing invitation to get it wrong.
- **Format version tied to the application version.** `tabulatorVersion` is "the version of the application that created this file." The installed build here reports `2.0.0` while its own `Info.plist` says `1.3.999`, and it refuses configs stamped newer. `star_result.schema.json` already avoids this: the number is *the contract's*, not any engine's.

### The others, briefly

| Source | Take | Leave |
|---|---|---|
| [**ABIF**](../scores_and_ranks/abif_format.md) (Lanphier) | One grammar spanning score, ranked, and approval; the aggregated `12:` count prefix | The hybrid register — `Allie/5 >Billy/6` states the order twice and nothing forces agreement |
| **NIST CDF** ([SP 1500-103](https://pages.nist.gov/CastVoteRecords/)) | Candidate objects with ids; `VoteVariation` incl. `range`; **a CVR records the ballot, not the tabulation** | Its weight — a jurisdiction interchange format, wildly heavy for a nine-voter fixture |
| [**PrefLib**](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) `.soc/.soi/.toc/.toi` | Ballot *shape* declared by file type — strict/incomplete/ties — which is this schema's `ballot` block reached independently | Four file extensions where one typed field does the same job |
| **`.blt`** (OpenSTV/OpaVote) | Withdrawn candidates as first-class; the aggregated count-then-ranking line | Terse positional syntax with `0` terminators — unreadable and unvalidatable |
| [**`pref_voting`**](cross_checking_with_pref_voting.md) / **`abcvoting`** | **Irresolute by default** — return the tied set and decline. A genuinely good answer, and one an engine should be *able* to give | — |
| [**BetterVoting**](BV/README.md) | Recording the full tiebreak permutation in the result, so a draw is replayable | A shuffle seeded from ballot *count* and race id — replayable but never derivable from how anyone voted |

**One convergence worth noting**, because it is evidence rather than preference: PrefLib encodes ballot shape in the *file extension*, RCTab in `winnerElectionMode`, this schema in `election.ballot`. Three formats designed independently all put it at the election level. None puts it on the row.

---

## Configuration and ballots — one file or two?

RCTab separates them. This library does not. **Both are right**, for different jobs, and the distinction is procedural rather than aesthetic.

|  | One file (this library) | Two files (RCTab, production) |
|---|---|---|
| Best for | **Fixtures.** One file is one complete, readable, self-contained election | **Elections.** Thousands of CVRs arriving from scanners |
| Review | Read the whole contest at a glance | Config reviewed and approved on its own |
| Lifecycle | Single artifact, single hash | **Config is authored, reviewed, approved and hashed *before* election day; ballots do not exist until after polls close** |
| Signers | One | Different people, different times |
| Failure mode | Does not scale past a page of ballots | A path can point at the wrong CVR; layout indices can silently misread |
| Diffing | A one-ballot change is a one-line diff | Ballot changes are opaque binary-ish churn |

The lifecycle row is the whole argument. Two artifacts with different authors, different approval moments and different audit trails cannot honestly live in one file — and equally, a teaching fixture split across two files stops being readable for no gain.

**So the schema supports both without choosing.** `election` + `candidates` + `rules` + `tiebreak` is the configuration; `ballots` is the data. In one document they sit together. To split them, omit `ballots` and the remainder *is* a config — hashable and approvable on its own — with the ballots supplied alongside. The schema requires `ballots` today because every case in this library is a fixture; a production profile relaxing exactly that one field is a minor version bump, not a redesign.

### What this means for a Rust core

The boundary follows the same seam:

```rust
// star-kernel — serde (derive) only. No parser, no I/O, no filesystem.
pub struct Contest {           // the configuration half: reviewable, hashable
    pub candidates: Vec<Candidate>,
    pub method:     Method,
    pub seats:      usize,
    pub rules:      Rules,     // method-scoped; empty for STAR
    pub tiebreak:   Tiebreak,
}

pub enum Ballots {             // the data half: one variant per contest, never per row
    Scores    { min: i8, max: i8, rows: Vec<ScoreRow> },
    Approvals { rows: Vec<ApprovalRow> },
    Marks     { allowed: usize, rows: Vec<MarkRow> },
    Rankings  { rows: Vec<RankingRow> },
    Grades    { scale: Vec<String>, rows: Vec<GradeRow> },
}

pub fn tabulate(c: &Contest, b: &Ballots) -> Result<Outcome, TabulationError>;
```

Four properties, each earned by something above:

1. **`Ballots` is an enum at the top, not per row.** A mixed score/ranked ballot set is not *invalid*, it is **unrepresentable** — which is the actual reason to write this in Rust rather than a dynamically-typed language.
2. **Two arguments, not one.** The signature *is* the config/ballot split, so the production profile needs no new type: the same kernel serves a fixture (both from one document) and a canvass (config approved Monday, ballots arriving Tuesday).
3. **No parser in the kernel.** `serde` derives only; `serde_json` lives in the harness crate and the WASM shim. This also sidesteps a live ecosystem problem — the cached crate on this machine is literally `serde_yaml-0.9.34+deprecated.crate`, archived upstream in 2024, and its forks are variously maintained. Under [NFR-5](rust_kernel_requirements.md)'s *"dependency budget: `serde` and little else"*, an abandoned YAML parser inside a certification-facing tabulator is real audit surface for no benefit. The kernel never sees YAML.
4. **A score entry is an enum, not an integer** — `Score(i8) | Blank | Marker(Marker)` — because five markers all tabulate as the bottom of the scale and mean different things, and a type that flattens them has discarded what several cases are *about*.

---

## What would have to be built

One thing, and it is small: **`--emit-election-json` on the LH engine**, the input mirror of `--json`. It reads a case file through the existing reader and writes this document.

That is what makes the whole design work, because it means the bespoke ballot DSL — the header row, the `Count:` prefix, the `×`, the `>` rankings, the markers, the `#,` comments, and the whitespace-alignment rescue that 183 files depend on — keeps **exactly one implementation, forever, in Python.** No second engine ever parses it, in any language. And the document it emits can be hashed, which is the thing `source.sha256` cannot do for YAML bytes read by two different parsers.

Then the corpus keeps its authoring format unchanged, and every other engine reads JSON.

## What is still missing

Stated plainly, on the same principle as the result contract:

- **No emitter, so nothing validates real cases yet.** The test below checks the schema against the illustrations on this page, which proves the schema is coherent and self-consistent — not that it can express all 612 files. Expect the conversion to find edge cases; the `3-2-1` and multi-race files are the likely first casualties.
- **Multi-contest files are out of scope by construction.** 30 case files use the older nested `election:` / `races:` shape, and each becomes N documents. Nothing yet says how the N are named or related.
- **`rules` is scoped by convention, not by the schema.** The keys are constrained as a set and each is documented with its family, but the schema does not yet *forbid* `quota` on a STAR contest. That wants the same `if`/`then` treatment `ballot.type` already gets, and is the first thing to tighten.
- **No CVR profile.** [D6 of the reference package](star_reference_package.md) is the mapping onto NIST CDF, and this schema is deliberately not it — a fixture format and a jurisdiction interchange format are different documents with different readers.

## What checks this page

[`tests/test_election_schema.py`](../../STARVote_LH_tabulation_engine/tests/test_election_schema.py) parses every JSON block on this page, validates each against the published schema, and asserts the negative cases too — that a ranked row inside a score contest is **rejected**, and that `outcome: "elected"` without a winners array is **rejected**. A schema nothing checks is documentation, not a contract.

*Up: [Tabulation engines](README.md) · the output half: [the result contract](result_schema.md) · the wider plan: [the STAR reference package](star_reference_package.md) · the consumer this was designed for: [Rust kernel scope](rust_kernel_scope.md).*
