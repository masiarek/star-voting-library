# Range / Score Voting

*Every voter **grades each candidate** on a fixed scale (say 0–5); the candidate
with the **highest total score wins**. No runoff, no elimination — just add up
the grades. Range is the most expressive single-mark method: Approval with more
than one bit, and STAR without the runoff.*

→ **Run it:** the 101 case [`06_Other/Range/range_101_c3_b5.yaml`](../../06_Other/Range/range_101_c3_b5.yaml)
([tabulated](../../06_Other/Range/Range_tabulated/range_101_c3_b5_RANGE_tabulated.txt)) ·
the **Black Curtain, read as Range** → [`black_curtain_range.md`](../../method_comparisons/black_curtain/black_curtain_range.md) ·
Engine: [the Range engine](../../Range_tabulation_engine/README_range_tabulation_engine.md)
(pref_voting). · Family: [Approval](../Approval_Voting/approval_voting.md) ·
[STAR](../STAR_Voting) · [fidelity ladder](../scores_and_ranks/fidelity_ladder.md).

> **Non-EVC method.** Range is what STAR *improves on*, so this library teaches
> *about* it rather than promoting it — it lives in
> [other methods](../../06_Other/README_06_Other.md), not the
> numbered root folders. The honest comparison is the point.

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

Counting is a single sum. Totals: Beth 21, Cole 15, Amy 11 → **Beth wins.** No
finalists, no rounds. (Larger scales — 0–9, 0–10, 0–99 — work the same way;
`rangevoting.org` favors a wide scale.)

## Where it sits in the scored family

- **Approval** is Range at **1-bit** resolution — grades restricted to `{0, max}`.
- **STAR** is Range's **score round + an automatic runoff**. The runoff exists
  precisely to blunt Range's strategy problem (below).
- So the three are one family at increasing resolution/robustness:
  **Approval → Range → STAR.** See the
  [fidelity ladder](../scores_and_ranks/fidelity_ladder.md).

## Pros and cons

| Pros | Cons |
|---|---|
| ✅ **Maximally expressive** — say *how much* you like each candidate, independently. | ⚠️ **Strategy-exposed.** A voter's rational play is often to give only max/min (exaggerate), which **collapses Range toward Approval**. |
| ✅ **No vote-splitting / spoiler** in the choose-one sense — scoring a new candidate never lowers another's score. | ⚠️ **Not majoritarian.** A candidate a slim majority *strongly* prefers can lose to one a broad group *mildly* likes. Range fails the **Majority Criterion**. |
| ✅ **Precinct-summable & simple to tally** — just add columns; none of RCV-IRV's round-by-round machinery. | ⚠️ **The scale / normalization problem.** Honest voters using the scale differently — or a shifted "where's my line" — changes results (the [approval-line](../Approval_Voting/approval_honest_limits.md) issue, one notch up). |
| ✅ **Monotone** — more support never hurts a candidate (unlike IRV). | ⚠️ **Fails Later-No-Harm** — grading a compromise can cost your favorite. |
| ✅ **Passes the [Equal Vote / balance test](../STAR_Voting/equally_weighted_vote.md)** and elects the utilitarian/consensus winner. | ⚠️ **Scale granularity can flip the winner** — see the [301 case](../scores_and_ranks/scale_granularity_flips_the_winner.md). |

**The one-line summary:** Range asks the richest question, but rewards
exaggeration; **STAR keeps Range's expressive ballot and adds a runoff** to make
honesty safer. Which trade-off you want is the whole debate.

## Ballot examples

- [`06_Other/Range/range_101_c3_b5.yaml`](../../06_Other/Range/range_101_c3_b5.yaml) — the intro above (0–5, three candidates).
- **Black Curtain, read as Range** — the four Black Curtain elections tabulated by
  the range engine: [`black_curtain_range.md`](../../method_comparisons/black_curtain/black_curtain_range.md).
  Range elects the broadly-liked candidate (Bob, Cal, Ann…) where STAR's runoff
  hands the seat to the majority's favorite — the sharpest illustration of the
  Range-vs-STAR trade-off.

## Links

- **[The Center for Range Voting — rangevoting.org](https://rangevoting.org/)** —
  Warren D. Smith's canonical range-voting site (research, Bayesian-regret
  simulations, and strong advocacy — read it as an *advocate's* case, alongside
  the cons above).
- [Equal Vote Coalition](https://www.equal.vote/) — STAR and the scored family.
- Glossary: **Score / Range voting** — [`../GLOSSARY.md`](../GLOSSARY.md).

## Tabulation (the details)

Range files here are tabulated by
[`Range_tabulation_engine/range_tabulation.py`](../../Range_tabulation_engine/README_range_tabulation_engine.md),
which wraps **pref_voting**'s `score_voting` and cross-checks it against a hand
sum. Full report for the 101 case:
[`range_101_c3_b5_RANGE_tabulated.txt`](../../06_Other/Range/Range_tabulated/range_101_c3_b5_RANGE_tabulated.txt).

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
