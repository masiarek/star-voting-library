# Range / Score Voting

*Every voter **grades each candidate** on a fixed scale (say 0–5); the candidate with the **highest total score wins**. No runoff, no elimination — just add up the grades. Range is the most expressive single-mark method: Approval with more than one bit, and STAR without the runoff.*

→ **Run it:** the 101 case [`06_Other/Range/cases/range_101_c3_b5.yaml`](../../06_Other/Range/cases/range_101_c3_b5.yaml) ([tabulated](../../06_Other/Range/cases/cases_tabulated/range_101_c3_b5_RANGE_tabulated.txt)) · the **Black Curtain, read as Range** → [The Black Curtain, read as Range / Score voting](../../method_comparisons/black_curtain/black_curtain_range.md) · Engine: [the Range engine](../../06_Other/Range/Range_tabulation_engine/) (pref_voting). · Family: [Approval](../Approval_Voting/approval_voting.md) · [STAR](../STAR_Voting) · [fidelity ladder](../scores_and_ranks/fidelity_ladder.md).

> **Non-EVC method.** Range is what STAR *improves on*, so this library teaches *about* it rather than promoting it — it lives in [other methods](../../06_Other/), not the numbered root folders. The honest comparison is the point.

---

## How it works

The ballot is a **score grid** — grade every candidate independently, e.g. 0–5:

```
Amy,Beth,Cole
5,4,0
5,3,1
0,4,5
1,5,4
0,5,5
```

Counting is a single sum. Totals: Beth 21, Cole 15, Amy 11 → **Beth wins.** No finalists, no rounds. (Larger scales — 0–9, 0–10, 0–99 — work the same way; `rangevoting.org` favors a wide scale.)

## Where it sits in the scored family

- **Approval** is Range at **1-bit** resolution — grades restricted to `{0, max}`.
- **STAR** is Range's **score round + an automatic runoff**. The runoff exists precisely to blunt Range's strategy problem (below).
- So the three are one family at increasing resolution/robustness: **Approval → Range → STAR.** See the [fidelity ladder](../scores_and_ranks/fidelity_ladder.md).

## Pros and cons

| Pros | Cons |
|---|---|
| ✅ **Maximally expressive** — say *how much* you like each candidate, independently. | ⚠️ **Strategy-exposed.** A voter's rational play is often to give only max/min (exaggerate), which **collapses Range toward Approval**. |
| ✅ **No vote-splitting / spoiler** in the choose-one sense — scoring a new candidate never lowers another's score. | ⚠️ **Not majoritarian.** A candidate a slim majority *strongly* prefers can lose to one a broad group *mildly* likes. Range fails the **Majority Criterion**. |
| ✅ **Precinct-summable & simple to tally** — just add columns; none of RCV-IRV's round-by-round machinery. | ⚠️ **The scale / normalization problem.** Honest voters using the scale differently — or a shifted "where's my line" — changes results (the [approval-line](../Approval_Voting/approval_honest_limits.md) issue, one notch up). |
| ✅ **Monotone** — more support never hurts a candidate (unlike IRV). | ⚠️ **Fails Later-No-Harm** — grading a compromise can cost your favorite. |
| ✅ **Passes the [Equal Vote / balance test](../STAR_Voting/properties_and_limits/equally_weighted_vote.md)** and elects the utilitarian/consensus winner. | ⚠️ **Scale granularity can flip the winner** — see the [301 case](../scores_and_ranks/scale_granularity_flips_the_winner.md). |

**The one-line summary:** Range asks the richest question, but rewards exaggeration; **STAR keeps Range's expressive ballot and adds a runoff** to make honesty safer. Which trade-off you want is the whole debate.

## A worked comparison — one electorate, four cardinal methods

*Ballot data adapted, with attribution, from Brendan W. Sullivan, [*An Introduction to the Math of Voting Methods*](https://books.google.com/books/about/An_Introduction_to_the_Math_of_Voting_Me.html?id=sohfzwEACAAJ) (2022, ISBN 978-1-958469-03-3), Examples 5.1–5.3. The numbers are reused for method comparison; all commentary below is original.*

Ten voters grade four candidates **A, B, C, D** on a **0–10** scale. Range just sums the grades:

```text
Total score (sum of all grades):
  C              70  ← winner
  A              61
  D              58
  B              47
```

**C wins with 70** — not because C is everyone's favorite, but because C collected many **10s**: support that's both *broad* and *strong*. Now hold those exact ballots fixed and change only the **method**:

| Method (same ballots) | Winner | Why |
|---|---|---|
| **Range / Score** (mean) | **C** — 70 pts | highest total |
| **Score, median variant** (greatest-median) | **C** — median 8.5 | half the electorate gave C 8.5 or higher |
| **STAR** (score + automatic runoff) | **C** | C leads scoring at 70, then wins the runoff over A, 6–3 |
| **Approval** (a 1-bit score) | **A** | in Sullivan's companion Example 5.1, A has 8 approvals to C's 7 |

The lesson: **the cardinal ballot's *resolution* can change the winner.** Collapse the 0–10 scale down to a single approve / don't-approve bit and **A** — with more *approvers* but fewer *enthusiasts* — overtakes C. Give voters room to say *how much*, and C's wall of 10s wins under Range, median-Range, and STAR alike. (Mean and median happen to agree here, but they needn't — some Score variants use the median precisely because a few extreme scores can't drag it the way they drag an average. Medians: A 7.0, B 5.0, **C 8.5**, D 5.5.)

**Run it:** [`range_sullivan_score_c4_b10.yaml`](../../06_Other/Range/cases/range_sullivan_score_c4_b10.yaml) ([tabulated](../../06_Other/Range/cases/cases_tabulated/range_sullivan_score_c4_b10_RANGE_tabulated.txt)) — the range engine (pref_voting `score_voting`) confirms C by both the hand sum and the median cross-check. STAR on the same ballots also elects C — worked, with the how-to for running LH on a non-standard scale, in [Unorthodox STAR — a scale wider than 0–5](../STAR_Voting/properties_and_limits/STAR_nonstandard_scale.md).

## Ballot examples

- [`06_Other/Range/cases/range_101_c3_b5.yaml`](../../06_Other/Range/cases/range_101_c3_b5.yaml) — the intro above (0–5, three candidates).
- [`06_Other/Range/cases/range_sullivan_score_c4_b10.yaml`](../../06_Other/Range/cases/range_sullivan_score_c4_b10.yaml) — Sullivan's Example 5.2 (0–10, four candidates; the worked comparison above).
- **Black Curtain, read as Range** — the four Black Curtain elections tabulated by the range engine: [The Black Curtain, read as Range / Score voting](../../method_comparisons/black_curtain/black_curtain_range.md). Range elects the broadly-liked candidate (Bob, Cal, Ann…) where STAR's runoff hands the seat to the majority's favorite — the sharpest illustration of the Range-vs-STAR trade-off.

## Links

- **[The Center for Range Voting — rangevoting.org](https://rangevoting.org/)** — Warren D. Smith's canonical range-voting site (research, Bayesian-regret simulations, and strong advocacy — read it as an *advocate's* case, alongside the cons above).
- [Equal Vote Coalition](https://www.equal.vote/) — STAR and the scored family.
- Glossary: **Score / Range voting** — [Glossary — voting methods & criteria](../GLOSSARY.md).

## Tabulation (the details)

Range files here are tabulated by [Range / Score voting tabulation engine](../../06_Other/Range/Range_tabulation_engine/), which wraps **pref_voting**'s `score_voting` and cross-checks it against a hand sum. Full report for the 101 case: [`range_101_c3_b5_RANGE_tabulated.txt`](../../06_Other/Range/cases/cases_tabulated/range_101_c3_b5_RANGE_tabulated.txt).

```text
--- Range / Score Voting (single winner) ---
  Range / Score Voting 101 — highest total score wins
 Tabulating 5 ballots on a 0–5 scale (range/score: highest total wins, no runoff).

Total score (sum of all grades):
  Beth           21  ← winner
  Cole           15
  Amy            11

Cross-check — pref_voting score_voting: Beth  (✓ agrees with the hand count)

Winner — Range / Score Voting (single winner)
  Beth
```

# file: range_voting.md
