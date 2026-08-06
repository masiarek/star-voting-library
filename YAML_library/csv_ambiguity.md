# Eight lines of CSV, eight questions

**Level: reference · deep dive**

**One line:** a bare CSV of scores can't say what it is, so the same eight lines have eight different readings — which is the whole argument for putting the election *in* the file.

This page works through the example posted in **[Equal-Vote/bettervoting#778 — "YAML File standard"](https://github.com/Equal-Vote/bettervoting/issues/778)** (Feb 2025), because it is the tidiest statement of the problem this library's file format exists to solve. The ticket is about BetterVoting's upload/discussion format; the library is what that proposal turned into once it had an engine behind it.

## The example

Eight ballot lines, exactly as a CSV upload might arrive:

```text title="ex1 — a bare CSV, from bettervoting#778"
line 1:   0,1,0,0
line 2:   0,0,0,0
line 3:   0,1,0
line 4:   0,0,1,1
line 5:   0,0,0,0
line 6:   0,1,0
line 7:   0,0,0,0
line 8:   0, ,0,,
```

Before reading a single ballot you already can't answer: **what method counts this?** Plurality, Approval, STAR, IRV, Ranked Robin? Are those **scores or ranks**? Is it **single- or multi-winner**? And how many candidates are even in the race — three, or four?

Then the lines themselves:

| Line | What it looks like | What it could mean |
|---|---|---|
| 2, 7 | `0,0,0,0` | A voter who deliberately scored everyone zero · a ballot that was left blank · a spoiled ballot · a file-format error |
| 3, 6 | `0,1,0` — three values, not four | The last candidate was left blank on purpose · a candidate-level abstention · a truncated row |
| 4 | `0,0,1,1` | Fine under Approval or STAR; under **Plurality** it's two votes in a one-vote race — an invalid ballot, or a mis-declared method |
| 5 | a value that is a space | Is whitespace even legal? And is a blank an abstention, a spoiled ballot, or a deliberate non-mark? |
| 8 | `0, ,0,,` | Five fields where there should be four. Blank, spoiled, abstained, or a stray comma? |
| all | — | Are **weighted** rows allowed at all? (BetterVoting's ballot-multiplier request is [#349](https://github.com/Equal-Vote/bettervoting/issues/349).) |

Every one of those questions is answerable — just not from the file. Which means it gets answered by whoever loads it, differently each time, and silently.

## What the format has to carry

Two separate jobs, and a grid of numbers does neither:

1. **The election's configuration** — the method, the seat count, the candidate names, the tie-break order. Without it the same grid tabulates to different winners, quite legitimately. (That the same ballots yield different winners under different methods isn't a bug; it's [the point](../method_comparisons/README.md). Which is exactly why the file has to say which one it means.)
2. **The intent behind every zero** — a real low score, a blank, a deliberate abstention and a spoiled ballot all tabulate as `0`, but they are four different things, and a report that folds them together can't tell participation from rejection. → [Abstention vs. a zero vs. "None of the Above"](../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md)

## The same eight lines, in the schema that settled

```yaml
voting_method: STAR
num_winners: 1
ballots: |-
  A,B,C,D
  0,1,0,0   # line 1 - four real scores, nothing ambiguous
  ~,~,~,~   # line 2 - race abstention: skipped the whole race
  0,1,0,&   # line 3 - candidate-level abstention on D
  0,0,1,1   # line 4 - four real scores
  ?,?,?,?   # line 5 - spoiled ballot
  0,1,0,-   # line 6 - D left blank
  0,0,0,0   # line 7 - all zeros ON PURPOSE - this is NOT an abstention
  0,-,0,-   # line 8 - B and D left blank
lot_numbers: [A, B, C, D]
expected_winners: [B]
```

Nothing was added to the *tally* — every marker still counts as zero, and the winner is the same. What was added is the file's ability to **say what it is**: the method, the seats, the candidate names, the tie-break order, and one marker per cell recording why that cell is a zero. The `#` comments survive in the file, so a row explains itself where it sits.

Run it, and the count comes out with the intent intact — note the abstention line:

<!-- report:csv_ambiguity_ex1_c4_b8 -->
```text
[Divergence from STAR]
  STAR     = B
  Approval = A   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 8 ballots. Note: 2 of 8 ballots are marked as abstentions.
A,B,C,D
0,1,0,0
~,~,~,~
0,1,0,&
0,0,1,1
?,?,?,?
0,1,0,-
0,0,0,0
0,-,0,-
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 3 -- First place
   C             -- 1 -- Tied for second place
   D             -- 1 -- Tied for second place
   A             -- 0
 B advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   C             -- 0 -- Tied for second place
   D             -- 0 -- Tied for second place
   Equal Support -- 8
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   C             -- 0 -- Tied for second place
   D             -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['A', 'B', 'C', 'D']

[Tiebreaker: Lot Number Priority]
  Tie among: ['C', 'D']
  Resolved: ['C'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 3 -- First place
   C             -- 1
   Equal Support -- 4
 B wins.
   Runoff math:
     8  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     4  voters with a preference  (majority = 3)
           B 3 (75%)  ·  C 1 (25%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```
<!-- /report -->

**2 of 8** — the race abstention and the spoiled ballot. The all-zero ballot on line 7 stayed in the count, which is what its voter asked for.

→ The runnable file: [`csv_ambiguity_ex1_c4_b8.md`](../01_STAR/02_Examples/cases/cases_pages/csv_ambiguity_ex1_c4_b8.md) · [`.yaml`](../01_STAR/02_Examples/cases/csv_ambiguity_ex1_c4_b8.yaml)

## Does an all-equal ballot count as an abstention?

Line 7 carries a claim in its comment — *"this voter marked all candidates as zero (this is not abstention!)"* — and the two engines disagree about it. The rule in the Larry Hastings engine is **a ballot is an abstention when it is marked as one**, never when it merely holds equal scores:

| Ballot | LH engine | Counted as an abstention? |
|---|---|:-:|
| `~,~,~,~` (race abstention) | marker | **yes** |
| `&,&,&,&` (candidate abstention) | marker | **yes** |
| `?,?,?,?` (spoiled) | marker | **yes** |
| `%,%,%,%` (spoiled and re-issued) | marker | **yes** |
| `-,-,-,-` (all blank) | marker | **yes** |
| `0,0,0,0` (real zeros) | scores | no |
| `3,3,3,3` · `5,5,5,5` (all-equal scores) | scores | no |
| `0,-,0,-` (zeros and blanks) | mixed | no |

BetterVoting's rule went the other way: since **[#884](https://github.com/Equal-Vote/bettervoting/issues/884)** a ballot whose marks are *all equal* — all 3s, all 0s, a mix of 0s and nulls — is counted as an abstention. Which reading is right is a live disagreement, not a bug report; the whole cluster of tickets it feeds is catalogued in the [BV abstain / blank / zero issue index](../07_Concepts/tabulation_engines/BV/abstain_issues_index.md).

Worth noticing either way: the argument is only *possible* because the format distinguishes a marker from a score. In the bare CSV, line 2 and line 7 are the same eight characters.

## What changed between the 2025 sketch and the schema as it settled

The ticket proposed a nested container — `election_parameters:` holding an `election id`, an `election title`, abstention permissions, a count of races, a `ballot format parameters` block declaring the marker characters, and then `race_1:` with the method, the candidates and the ballots. Two and a half thousand tabulated ballots later, five things came out differently:

| The 2025 sketch | Where it landed | Why |
|---|---|---|
| Nested `election_parameters: → race_1: → ballots:` | **Flat.** Three required keys: `voting_method`, `num_winners`, `ballots` | Indentation depth is where hand-written YAML goes wrong. The engine still recognizes the nested shape by name and prints the flat template — see below |
| `candidates: [A,B,C,D]` as its own key | **The header row of the ballot block is the candidate list** | One place to change a name, and the columns can't drift out of step with the header |
| `single_or_multi_winner: single` | `num_winners: 1` | A seat count answers both questions and also carries "three seats" |
| `ballot format parameters:` declaring each marker character per file | **One fixed vocabulary**, the same in every file: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled and re-issued | A per-file alphabet means two files with the same characters can mean different things. `%` was added; `^` was dropped in favour of `-` |
| `number of races` + `race_1:`, `race_2:`… | **One race per file**, with a multi-race election held together by a shared filename prefix and a shared frozen export | Each race is separately runnable, testable and linkable; the set is still indexed as one election in [multi-race elections](../07_Concepts/YAML_test_case_index/multirace_elections.md) |

Two of those are enforced rather than merely documented. Feed today's engine the nested sketch and it names the old schema in the error:

```text title="Abridged for the lesson — not verbatim engine output"
Error: no 'ballots:' block found in 'feb2025_sketch.yaml'.
(If this is the old nested schema 'election_parameters -> races ->
 race_1 -> ballots', convert it to the flat form shown below.)
```

And the retired `^` marker has a [deliberately-broken fixture](2_negative/neg_marker_caret.yaml) keeping it retired:

```text title="Abridged for the lesson — not verbatim engine output"
Error: STAR ballots use scores 0..5 (blank or a marker counts as 0).
  Offending ballot(s)  [Austin,Boston,Cairo]:
    ballot 1: 5, ^, 2   (invalid: Boston=^)
  Accepted marks: 0..5, blank, or a marker (-, ~, &, ?, %).
```

**One idea from the sketch had no home anywhere — so it was filed upstream.** `race abstention allowed:` and `candidate abstention allowed:` describe what the *rules of the election* permit, not what a voter did. This library records the ballot rather than the rulebook, so there's no key for it here; BetterVoting has no field for it either, which means an export can't distinguish *"nobody abstained"* from *"abstaining was impossible."* Filed 2026-08-06 as **[#1485 — Record the abstention policy on the race](https://github.com/Equal-Vote/bettervoting/issues/1485)**, scoped to the recording side because [#699](https://github.com/Equal-Vote/bettervoting/issues/699) already holds the admin-setting half. Report archived at [`bv_github_issue_abstention_policy.md`](../07_Concepts/tabulation_engines/BV/bv_github_issue_abstention_policy.md).

## The weights question

`Are weights allowed?` — yes, as a count prefix on a row:

```yaml
ballots: |-
  Ann,Bob,Cal
  42 × 5,4,0
  17 × 0,3,5
```

Separators `×`, `:`, `x` or `X`; house rule is that a weight must be **≥ 6**, so a count is never misread as a 0–5 score. (Keep examples small anyway — a handful of individual voters teaches better than a hundred weighted ones. → [Choosing voter counts](../07_Concepts/tips/TIPS_choosing_voter_counts.md).)

## Related

- [Why YAML? One file a person reads and a computer runs](why_yaml_test_cases.md) — the design argument in full
- [YAML election files — why, what, how](README.md) — the format, the five stages, the folder
- [YAML Test Case — Authoring Template](YAML_authoring_template.md) — every field, every option, the full marker table
- [ABIF vs. our YAML grid](../07_Concepts/scores_and_ranks/abif_format.md) — the election-methods world's dedicated ballot *interchange* format, and how it compares
- [BV abstain / blank / zero — issue index](../07_Concepts/tabulation_engines/BV/abstain_issues_index.md) — the ticket cluster this one sits in
- [The test-case catalog](../07_Concepts/YAML_test_case_index/README.md) — every election in the library, by method
