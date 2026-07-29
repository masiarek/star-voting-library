# Winning the most matchups does *not* make you the Condorcet winner

A claim that circulates in voting-reform discussion, and is easy to believe:

> If you win head-to-head against more candidates than anyone else, you must be the Condorcet winner. So adding up head-to-head victories just describes the Condorcet winner.

It isn't true. This page is the counterexample, and the explanation of exactly which step fails.

## The counterexample

Eighteen voters, five candidates, three equal blocs:

| Voters | Ranking |
|---:|---|
| 6 | Blake > Erin > Amy > Cora > Diego |
| 6 | Amy > Cora > Erin > Diego > Blake |
| 6 | Diego > Cora > Blake > Erin > Amy |

Every pair meets:

```
Cora  beats Blake  12 – 6      Blake beats Erin   12 – 6
Cora  beats Erin   12 – 6      Blake beats Amy    12 – 6
Cora  beats Diego  12 – 6      Erin  beats Amy    12 – 6
Amy   beats Cora   12 – 6      Erin  beats Diego  12 – 6
Amy   beats Diego  12 – 6      Diego beats Blake  12 – 6
```

Giving:

```
Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Cora       3–1–0         3     +12  Blake, Erin, Diego
    2  Amy        2–2–0         2      +0  Cora, Diego
    3  Blake      2–2–0         2      +0  Amy, Erin
    4  Erin       2–2–0         2      +0  Amy, Diego
    5  Diego      1–3–0         1     -12  Blake

Winner — Ranked Robin (RCV-RR): Cora
   the most head-to-head wins (3).
```

**Cora wins three of four matchups — strictly more than anyone else, not tied.** Cora is elected.

**And Amy beats Cora, 12–6.**

So Cora is not the Condorcet winner. There is no Condorcet winner here at all: the [Smith set](../../00_start_here/topics/smith_set.md) is all five candidates, one big [cycle](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md).

## Which step fails

The true statement and the false one look almost identical, and only one direction holds.

**True:** a Condorcet winner always has the *uniquely* highest Copeland score. This is easy to see — a Condorcet winner takes all n−1 matchups, which is the maximum possible, and every other candidate has lost at least that one matchup to them, so nobody else can exceed n−2. The gap is guaranteed, not coincidental.

**False:** the converse — that the uniquely highest score implies a Condorcet winner. Being the *best* in the tournament is simply not the same as being *undefeated*, and when nobody is undefeated somebody is still best.

That's the whole error: reading a one-way implication as an equivalence. It's an easy slip precisely because in the great majority of real elections a Condorcet winner does exist, and there the two descriptions genuinely do coincide.

## What the counterexample deliberately avoids

There is **not a single drawn matchup** in this profile. Every pair has a clear winner, so `wins + ½·ties` and the raw win count are identical here.

That matters, because the other well-known gap in "most matchups won" is about *draws* — [a drawn matchup is worth half a win](../copeland_score/), and a half-point can decide an election. Someone hearing that objection could reasonably reply "fine, but that's a technicality about tie-credit."

This case closes that escape route. No draws, no half-points, no tie-breaking — the claim fails on its own terms.

## Free with the first lesson: Cora has zero first-choice votes

Look at the blocs again. They lead with Blake, Amy and Diego. First choices split **6–6–6–0–0**: Cora and Erin are nobody's favorite.

Cora is the broadly-acceptable second choice — ranked 2nd by twelve of the eighteen voters — and that is exactly why Cora wins the round robin while collecting no first-place support at all. It's the same reason [Ranked Robin resists center squeeze](../../00_start_here/RCV_Ranked_Robin/why_ranked_robin.md): it never asks "who is your favorite?", only "which of these two do you prefer?"

It also means **Choose-One and RCV-IRV cannot produce an answer here without a coin flip.** Both deadlock three ways at 6 — Choose-One immediately, IRV after eliminating the two candidates with no first choices. That's why this case is a single Ranked Robin race and not a method line-up: the other methods' results here aren't reproducible, so there'd be nothing honest to freeze.

## Why the margin-based methods can't rescue it either

Every matchup in this profile is **12–6**. Every single one — so every pairwise margin is exactly 6. The tournament is perfectly regular.

Run it through the rest of the Condorcet family and that symmetry shows up immediately:

| Method | Winner |
|---|---|
| **Copeland (= Ranked Robin)** | **Cora** |
| Minimax | all five (genuine tie) |
| Ranked Pairs | all five (genuine tie) |
| Schulze | all five (genuine tie) |
| Split Cycle | all five (genuine tie) |
| Stable Voting | Cora |

Methods that decide by *margin* have nothing to work with when every margin is identical. Copeland, which counts only **how many** opponents you beat, is one of the few here that returns a decisive answer.

This is worth setting beside the [companion case](../copeland_score/), which pushes in the opposite direction — there Copeland is the lone outlier and every margin-aware method overrules it. Together they're an honest picture of the [C1/C2 trade-off](../../00_start_here/topics/what_a_method_reads.md): discarding margins costs you in one profile and saves you in another. Neither case makes Copeland right or wrong; they show what the choice actually buys and spends.

## The shorthand shows up in official copy too

Equal Vote's own [Ranked Robin description](https://www.equal.vote/ranked_robin) states the rule as:

> "The candidate who wins the most one-on-one matchups is elected."

As a description of *the tabulation*, that is correct — it is what the method does, and it's what elected Cora above. The trouble is only when it gets read as a description of *the outcome* ("…and that candidate is therefore the Condorcet winner"). The method is a [Condorcet method](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md) because it elects the Condorcet winner **whenever one exists** — which is a promise about a conditional, not a guarantee that its winner always beat everybody.

There's also a small internal tension worth noticing: the same page advertises that Ranked Robin lets voters rank candidates equally — and equal rankings are what produce drawn matchups, which is what "most matchups won" doesn't account for. The feature and the shorthand pull against each other.

## Cross-checks

- **LH engine** → Cora, Copeland 3, unique leader
- **`pref_voting`** (independent implementation, Copeland as wins − losses) → Cora, `AGREE ✓ (unique Copeland winner)`

Fully deterministic — Cora is the unique Copeland leader, so no tiebreak rung is reached and the result does not depend on lot order.

## Run it yourself

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/most_wins_vs_condorcet/cases/most_wins_is_not_condorcet.yaml
```

## See also

- [The Copeland score — a draw is worth half a win](../copeland_score/) — the companion case: the *other* way "most matchups won" comes apart
- [Ranked Robin vs. "the Condorcet winner"](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md) — same animal, until there's a cycle
- [The Smith set](../../00_start_here/topics/smith_set.md) — the generalized Condorcet winner, which is what "best" means when nobody is undefeated
- [Honest limits](../../00_start_here/RCV_Ranked_Robin/RCV_RR_honest_limits.md)

*(Up: [05_Ranked_Robin](../README.md) · concept docs: [Ranked Robin (RCV-RR)](../../00_start_here/RCV_Ranked_Robin/README.md))*

# file: README.md
