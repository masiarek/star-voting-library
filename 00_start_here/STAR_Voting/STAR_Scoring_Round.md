# The Scoring Round

**One line:** STAR's **first** step. Add up every candidate's stars across all ballots; the **two highest-scoring candidates become the Finalists** and advance to the [Automatic Runoff](STAR_Automatic_Runoff.md). That's the whole first round — simple addition. The scoring round measures *how much* support each candidate has; the runoff then decides *how many* voters prefer each finalist (**S**core **T**hen **A**utomatic **R**unoff).

→ Round 2: [The Automatic Runoff](STAR_Automatic_Runoff.md) · the whole report: [Reading a STAR report](../tabulation_engines/LH_starvote/reading_a_star_report.md) · the two-step count vs IRV: [Tabulation, step by step](../tabulation_star_vs_irv.md).

---

## What the round does

1. On each ballot, every candidate has a score from **0 to 5** (equal scores allowed; a blank counts as 0).
2. **Add up each candidate's scores** across all ballots — plain summation.
3. The **two highest totals** are the **Finalists**. Everyone else is done; only the top two advance to the runoff.

This is *utilitarian aggregation* — it rewards **total** support. A candidate rated a solid 4 by almost everyone can out-total a candidate given 5 by a passionate few and 0 by the rest. Whether that top-total candidate actually *wins* is the runoff's job, not the scoring round's.

```
Scoring Round
  The two highest-scoring candidates advance to the next round.
    Carmen -- 15 (average 5)     -- First place
    Andre  -- 12 (average 4)     -- Second place
    David  --  8 (average 2+2/3)
    Ella   --  1 (average 1/3)
    Blake  --  0 (average 0)
  Carmen and Andre advance.
```

## Totals decide — averages are just for reading

The report prints each candidate's **total** and, in parentheses, the **average** per ballot. **The total is what ranks them and picks the finalists;** the average is a readability aid (it says "about how many stars per voter"). With every ballot scoring every candidate, total and average rank candidates the same way — but it's the *total* the engine advances on.

## Equal scores are allowed — and honest scoring is safe

You may give two candidates the **same** score; you are never forced to invent a preference you don't feel ([equal ranks / weak orders are a ranked-ballot problem STAR doesn't have](../scores_and_ranks/scores_vs_ranks.md)). This is also what makes the scoring round **resist vote-splitting**: because you can give two similar candidates *both* a 5, running an ally no longer bleeds your favorite's total — the two don't split a shared pool of support the way they would under choose-one. → [the spoiler effect](../spoiler_effect.md). And you never need to **exaggerate**: in a pure score election the smart move is to give your favorite 5 and everyone else 0 (any in-between score just helps a rival's total), which collapses the ballot into [Approval](../Approval_Voting/approval_voting.md). STAR's **runoff** removes that pressure, so your honest 3s and 4s in the scoring round still do real work without costing your favorite. Why that matters, and its narrow limit: [residual vote-splitting](residual_vote_splitting.md) · [STAR's honest limits](STAR_honest_limits.md).

## Is the Scoring Round just Range (Score) voting?

Essentially **yes — Round 1 *is* a Range / Score election.** You score every candidate 0–5 and add up the totals, exactly as [Score / Range voting](../Range_Voting/range_voting.md) does. The difference is what happens *next*:

- **Range voting stops here** and crowns the **highest total**. The scoring round *is* the whole election.
- **STAR doesn't.** The top two totals are only **Finalists**; the [Automatic Runoff](STAR_Automatic_Runoff.md) then elects the majority-preferred one.

That second step isn't a formality — it changes **how you should vote.** In pure Range, your ballot has the most leverage if you give only 5s and 0s (any middle score just helps a rival's total catch yours), so Range rewards **min/max "bullet" voting** and, if everyone does it, collapses toward [Approval](../Approval_Voting/approval_voting.md). STAR's runoff removes that reward: since the runoff only asks *which finalist you scored higher*, your honest 3s and 4s keep their meaning and you never have to exaggerate. So the scoring round is Range's **expressive half**; the runoff is what lets voters *use* that expressiveness honestly — [STAR's hybrid nature](STAR_hybrid_nature.md).

## Ties in the scoring round

Two kinds of tie can happen here:

- **A tie for a Finalist slot** (e.g. two candidates tie for 2nd). STAR resolves *which one advances* with the **tie-break ladder** — first the head-to-head **pairwise** result, then the **five-star** count, then, as a last resort, a documented **lot**.
- **A rare three-way (or larger) tie** for the top scores that the ladder can't split cleanly falls through to the lot.

Full ladder, lot order, and imported `tieBreakType`: [STAR Tie-Breaking](Tie_Breaking_STAR/tie_breaking.md).

## What it feeds — and what it can't decide alone

The scoring round only ever produces **two finalists**. It deliberately does **not** crown the highest total, because a big total can come from a passionate minority (**[why a second step at all?](STAR_Automatic_Runoff.md#why-a-second-step-at-all)**). The **[Automatic Runoff](STAR_Automatic_Runoff.md)** then asks the majority-protecting question the total can't — *between these two, which do more voters prefer?* When the score leader also wins the runoff (the usual case) the rounds agree; when they don't, that's a [Runoff Reversal](../../01_STAR/runoff_overturns_leader/). Why STAR is built as this two-step hybrid: [STAR's hybrid nature](STAR_hybrid_nature.md); the three different "winners" a report can name: [three winner notions](STAR_three_winner_notions.md).

## FAQ

**"Does a blank count as 0, or as 'no opinion'?"** As **0** — the lowest score. A blank is the same as scoring that candidate 0; there's no separate "skip this candidate" that removes them from the total.

**"Why totals, not averages?"** Since every ballot scores every candidate, total and average rank candidates identically — and the total is the honest measure of *how much support across the whole electorate*. The report prints the average only as a reading aid.

**"Can I give two candidates the same score?"** Yes — equal scores are allowed and never penalized. If both reach the runoff, your ballot is [Equal Support](../GLOSSARY.md) between them.

**"Should I give my favorite 5 and everyone else 0?"** You *can*, but it usually **forfeits your say in the runoff.** If your favorite doesn't make the top two, all-0s means you've expressed no preference among the candidates who *did* — so give the "acceptable" candidates 3s and 4s so your full vote lands on the better finalist. Honest scoring is also the strong strategy.

**"Does a candidate need a majority to advance?"** No. The **two highest totals** advance, full stop — majority only matters in the runoff.

**"Does scoring my second choice hurt my favorite?"** In the *scoring round*, a little — and STAR accepts this **by design.** Giving a second choice a positive score adds to *their* total, which could in principle help them out-total your favorite. That means the scoring round is **not** [Later-No-Harm](STAR_honest_limits.md#3-gives-up-later-no-harm-by-design) compliant (RCV-IRV is; STAR trades it away). The upside is bigger: if your favorite *doesn't* reach the top two, that honest support keeps you a **voice** in the runoff, and scoring an ally doesn't let a rival split your side. (Note: Later-No-Harm is a *different* criterion from favorite-betrayal — STAR never rewards ranking someone *above* your true favorite.)

**"Why not just crown the highest total and skip the runoff?"** Because a big total can come from a passionate **minority** (lots of 5s) while most voters rated that candidate low. That's the whole reason for the second step — see [Why a second step at all?](STAR_Automatic_Runoff.md#why-a-second-step-at-all) and [Runoff Reversal](../../01_STAR/runoff_overturns_leader/).

**"Can precincts add up their own subtotals?"** Yes — scoring-round totals are plain sums, so they're **summable**: precinct subtotals add to the statewide total, unlike RCV-IRV. → [summability](STAR_summability.md).

## At a glance

| | Scoring Round (Round 1) | Automatic Runoff (Round 2) |
|---|---|---|
| **Question** | *how much* total support? | *how many* prefer each finalist? |
| **Math** | add every candidate's stars | one vote per ballot, to the higher-scored finalist |
| **Output** | the **two finalists** | the **winner** |
| **Ties** | tie for a slot → [tie-break ladder](Tie_Breaking_STAR/tie_breaking.md) | even split → [tie-break ladder](Tie_Breaking_STAR/tie_breaking.md) |
| **Character** | utilitarian (total support) | majoritarian (majority preference) |

# file: STAR_Scoring_Round.md
