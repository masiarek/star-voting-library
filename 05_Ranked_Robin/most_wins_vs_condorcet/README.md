# Winning the most matchups does *not* make you the Condorcet winner

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/gg9qh9) · **[results ↗](https://bettervoting.com/gg9qh9/results)** (election `gg9qh9`, BV2260).

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

So Cora is not the Condorcet winner. There is no Condorcet winner here at all: the [Smith set](../../07_Concepts/topics/smith_set.md) is all five candidates, one big [cycle](../concepts/cycle_resolution.md).

## Which step fails

The true statement and the false one look almost identical, and only one direction holds.

**True:** a Condorcet winner always has the *uniquely* highest Copeland score. This is easy to see — a Condorcet winner takes all n−1 matchups, which is the maximum possible, and every other candidate has lost at least that one matchup to them, so nobody else can exceed n−2. The gap is guaranteed, not coincidental.

**False:** the converse — that the uniquely highest score implies a Condorcet winner. Being the *best* in the tournament is simply not the same as being *undefeated*, and when nobody is undefeated somebody is still best.

That's the whole error: reading a one-way implication as an equivalence. It's an easy slip precisely because in the great majority of real elections a Condorcet winner does exist, and there the two descriptions genuinely do coincide.

## Claims, checked

These circulate together in reform discussion, usually in good faith and usually mixed in with correct statements. Sorted by verdict:

| Claim | Verdict |
|---|---|
| "Adding up head-to-head victories just ends up describing the Condorcet winner." | **False** |
| "If you win head-to-head against more candidates than anyone else, you must be the Condorcet winner." | **False** |
| "The Copeland score subtracts pairwise losses." | **True**, as one of two conventions |
| "A Condorcet winner always has the highest Copeland score." | **True** — and *uniquely* highest |
| "A candidate can have the uniquely highest Copeland score and not be a Condorcet winner." | **True** — this page is the example |
| "Ranked Robin is Copeland with Borda Count as a tiebreaker." | **Outdated** |

Taking them one at a time:

**"Adding up head-to-head victories just describes the Condorcet winner"** and **"most wins ⇒ Condorcet winner"** are the same error stated two ways, and the profile above refutes both: Cora has strictly the most wins and loses to Amy. The two descriptions coincide *whenever a Condorcet winner exists*, which is most of the time — that's why the claim feels safe. But "counting wins" and "identifying an undefeated candidate" are different operations, and they part company exactly when no one is undefeated. A method that merely counted wins wouldn't need a name; the reason Copeland is a *method* is that it still returns an answer when the Condorcet winner doesn't exist.

**"Copeland subtracts pairwise losses"** is correct — that's the `wins − losses` convention. The other convention is `wins + ½·ties`, which is what this repo's engine, BetterVoting and `pref_voting` all print. They're affine transforms of each other, so they always rank identically. Worth knowing only so that seeing two formulas doesn't read as two sources disagreeing. (Neither equals the raw *win count* once draws exist — see [the companion case](../copeland_score/).)

**"A Condorcet winner always has the highest Copeland score"** is true, and the sharper version is worth stating: *uniquely* highest, always, with no possibility of a tie at the top. A Condorcet winner takes all n−1 matchups; everyone else has lost at least that one, so nobody else can exceed n−2.

**"A candidate can have the uniquely highest Copeland score without being a Condorcet winner"** is the correction that resolves the whole confusion, and it is exactly what this page demonstrates. Cora scores 3 against everyone else's 2 or 1 — unique, not tied — and is still beaten by Amy.

**"Ranked Robin is Copeland with Borda Count as a tiebreaker"** described an earlier specification. The Borda tiebreak has since been struck from Equal Vote's own description, and neither implementation we test against uses it: this repo's engine breaks ties by total margin, then by pre-published lot order; BetterVoting's `RankedRobin.ts` uses head-to-head, then random. [Those two ladders diverge](../concepts/rr_tiebreak_lh_vs_bv.md), which is its own documented case — but neither ladder is Borda.

One more that's defensible but softer than it sounds: **"all Condorcet methods have roughly the same VSE."** True in aggregate, and true *because* the disagreements are rare — they agree by definition whenever a Condorcet winner exists. It isn't evidence that the methods are interchangeable. This page and its companion are both profiles where they diverge completely: here four of them return a five-way tie while Copeland decides; there Copeland is overruled by every one of them.

## What the counterexample deliberately avoids

There is **not a single drawn matchup** in this profile. Every pair has a clear winner, so `wins + ½·ties` and the raw win count are identical here.

That matters, because the other well-known gap in "most matchups won" is about *draws* — [a drawn matchup is worth half a win](../copeland_score/), and a half-point can decide an election. Someone hearing that objection could reasonably reply "fine, but that's a technicality about tie-credit."

This case closes that escape route. No draws, no half-points, no tie-breaking — the claim fails on its own terms.

## Free with the first lesson: Cora has zero first-choice votes

Look at the blocs again. They lead with Blake, Amy and Diego. First choices split **6–6–6–0–0**: Cora and Erin are nobody's favorite.

Cora is the broadly-acceptable second choice — ranked 2nd by twelve of the eighteen voters — and that is exactly why Cora wins the round robin while collecting no first-place support at all. It's the same reason [Ranked Robin resists center squeeze](../concepts/why_ranked_robin.md): it never asks "who is your favorite?", only "which of these two do you prefer?"

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

This is worth setting beside the [companion case](../copeland_score/), which pushes in the opposite direction — there Copeland is the lone outlier and every margin-aware method overrules it. Together they're an honest picture of the [C1/C2 trade-off](../../07_Concepts/topics/what_a_method_reads.md): discarding margins costs you in one profile and saves you in another. Neither case makes Copeland right or wrong; they show what the choice actually buys and spends.

## The shorthand shows up in official copy too

Equal Vote's own [Ranked Robin description](https://www.equal.vote/ranked_robin) states the rule as:

> "The candidate who wins the most one-on-one matchups is elected."

As a description of *the tabulation*, that is correct — it is what the method does, and it's what elected Cora above. The trouble is only when it gets read as a description of *the outcome* ("…and that candidate is therefore the Condorcet winner"). The method is a [Condorcet method](../concepts/ranked_robin_vs_condorcet.md) because it elects the Condorcet winner **whenever one exists** — which is a promise about a conditional, not a guarantee that its winner always beat everybody.

There's also a small internal tension worth noticing: the same page advertises that Ranked Robin lets voters rank candidates equally — and equal rankings are what produce drawn matchups, which is what "most matchups won" doesn't account for. The feature and the shorthand pull against each other.

## Cross-checks

Three independent implementations, one winner:

- **LH engine** (this repo) → Cora, Copeland 3, unique leader
- **`pref_voting`** (independent library, Copeland as wins − losses) → Cora, `AGREE ✓ (unique Copeland winner)`
- **BetterVoting** (`RankedRobin.ts`, live election `gg9qh9`) → **Cora** — frozen in [`…_bv_export.json`](cases/bgg9qh9_most_wins_is_not_condorcet_bv_export.json)

Fully deterministic: Cora is the unique Copeland leader, so no tiebreak rung is reached and the result does not depend on lot order. That matters here, because [LH and BetterVoting break Ranked Robin ties differently](../concepts/rr_tiebreak_lh_vs_bv.md) — this case never reaches the rung where they'd disagree, which is why it was safe to put on BetterVoting at all.

## Run it yourself

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/most_wins_vs_condorcet/cases/bgg9qh9_most_wins_is_not_condorcet.yaml
```

Want the whole count — full pairwise grid, Smith-set audit, ballot listing? See the full LH report → [`bgg9qh9_most_wins_is_not_condorcet`](cases/cases_pages/bgg9qh9_most_wins_is_not_condorcet.md), or the [`_tabulated` mirror](cases/cases_tabulated/bgg9qh9_most_wins_is_not_condorcet_tabulated.txt). Source: [`bgg9qh9_most_wins_is_not_condorcet.yaml`](cases/bgg9qh9_most_wins_is_not_condorcet.yaml).

## See also

- [The Copeland score — a draw is worth half a win](../copeland_score/) — the companion case: the *other* way "most matchups won" comes apart
- [Ranked Robin vs. "the Condorcet winner"](../concepts/ranked_robin_vs_condorcet.md) — same animal, until there's a cycle
- [The Smith set](../../07_Concepts/topics/smith_set.md) — the generalized Condorcet winner, which is what "best" means when nobody is undefeated
- [Honest limits](../concepts/RCV_RR_honest_limits.md)

*(Up: [05_Ranked_Robin](../README.md) · concept docs: [Ranked Robin (RCV-RR)](../concepts/README.md))*

# file: README.md
