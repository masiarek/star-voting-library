# The score leader can win no seat

**One line:** Bloc STAR is **not** "the top N by points." Every seat is settled by the **automatic runoff**, so seats go to whoever is *preferred* head-to-head — and a broadly acceptable compromise candidate can lead every scoring round by a wide margin, reach every runoff, lose every one of them narrowly, and end the night with nothing.

→ The single-winner version of the same step: [runoff reversal](../../01_STAR/02_Examples/runoff_overturns_leader/) · the mechanics: [Bloc STAR](bloc_star.md) · not to be confused with [the majority sweep](majority_sweep.md)

**Level: 201 → 301 · deep dive**

---

## The claim people actually make

Ask around and Bloc STAR gets described as "score everyone, the top N win." Half the repo's own shorthand says it that way, and for a lot of elections it happens to be true. It is still the wrong model, and it fails exactly where multi-winner elections get interesting.

The correct model is the one in [the method page](bloc_star.md): each seat runs the **whole** STAR count, scoring round *and* runoff. The scoring round only picks two finalists. The runoff picks the winner. So the score order is a **shortlist**, not a result — and a candidate can top that shortlist forever without ever converting it.

## BV1835 — 100 voters, 4 seats, and the leader takes nothing

Five candidates, four seats, so exactly one candidate loses. The electorate is two mirror-image camps of 49 that share no candidates at all, plus a 2-voter swing bloc:

```text
Count × Ava,Bianca,Cedric,Deegan,Eli
   25 ×   3,     5,     4,     0,  0
   25 ×   3,     0,     0,     5,  4
   24 ×   3,     4,     5,     0,  0
   24 ×   3,     0,     0,     4,  5
    2 ×   0,     5,     4,     3,  2
```

**Ava is the compromise.** 98 of the 100 voters score her a 3 — above the pair they zeroed out, below their own two. Nobody's favorite, almost nobody's enemy. She leads the scoring round by 63 points:

--8<-- "02_STAR_Bloc/02_Examples/cases/cases_pages/bv1835_8h3yrx_score_leader_no_seat.md:report"
Then it happens again. And again. And again:

| Seat | Scoring round | Runoff | Seat goes to |
|:--:|---|---|---|
| 1 | **Ava 294**, Bianca 231, Cedric 228, Deegan 227, Eli 224 | Bianca **51** – Ava 49 | Bianca |
| 2 | **Ava 294**, Cedric 228, Deegan 227, Eli 224 | Cedric **51** – Ava 49 | Cedric |
| 3 | **Ava 294**, Deegan 227, Eli 224 | Deegan **51** – Ava 49 | Deegan |
| 4 | **Ava 294**, Eli 224 | Eli **51** – Ava 49 | Eli |

**Winners: Bianca, Cedric, Deegan, Eli.** Ava reaches all four runoffs as the top-scoring finalist and loses all four by the same two votes. BetterVoting agrees exactly — same four winners, same seat order, `tieBreakType: "none"` in all four rounds, no tie and no lot anywhere. The result is fully deterministic; there is nothing to appeal to.

Full count: [`bv1835_8h3yrx_score_leader_no_seat`](../02_Examples/cases/cases_pages/bv1835_8h3yrx_score_leader_no_seat.md) · two-view lesson: [BV1835](../02_Examples/bv1835_8h3yrx_score_leader_no_seat.md) · [yaml](../02_Examples/cases/bv1835_8h3yrx_score_leader_no_seat.yaml)

## Why the 51–49 repeats

Because the two camps cancel and a tiny bloc decides. On *Ava vs. anybody*, the camps split 49–49: each camp scored Ava 3 and their own pair 5/4, so half the electorate prefers the other candidate and half prefers Ava. The 2-voter swing bloc scored Ava **0** and everyone else 5/4/3/2, so it breaks every one of those ties against her — 51–49, four times.

That also makes Ava the **Condorcet loser**: she loses every head-to-head matchup in the race. The engine says so in as many words, and adds the twist that she'd have won under Approval:

```text
[Condorcet Loser]
  Condorcet Loser: Ava — loses every head-to-head matchup — elected by Approval!

[Divergence from STAR]
  STAR     = Bianca
  Approval = Ava   (differs from STAR)
```

So the point tally and the preference tally genuinely disagree here, and Bloc STAR follows the preference tally. Both times. Every time.

## Is this a defect?

It depends on what you think the scoring round is *for*, and the honest answer is that both readings are coherent.

**Reading 1 — working as designed.** This is [runoff reversal](../../01_STAR/02_Examples/runoff_overturns_leader/), STAR's signature step, repeated once per seat. The whole reason STAR appends a runoff to a score ballot is that raw point totals reward a candidate everybody tolerates over the candidate more voters actually prefer — and reward strategic minimization besides. The runoff asks the majority directly, and here the majority answered four times. A method that seated Ava would be Score voting, not STAR, and the repo's own [Approval / Score critique](../../04_Approval/01_Learn/approval_honest_limits.md) is exactly the argument for not doing that.

**Reading 2 — the multi-winner sting.** In a single-winner race a runoff reversal costs the score leader *the* seat, and that is the deal you signed up for. Here it costs them **all four**, and there is no rung anywhere in Bloc STAR at which "led every round and lost every round" earns anything. A body that wanted its compromise figure in the room does not get her, no matter how many seats it has. If that is the goal, the fix is a different method — a Condorcet-flavored count like [Bloc Ranked Robin](bloc_star_vs_other_bloc_methods.md), or a proportional one — not a complaint about the tabulation.

What the case is **not** is [the majority sweep](majority_sweep.md). Nobody sweeps here: the two camps take two seats each, a perfectly proportional-looking 2–2. The score leader alone is excluded, and she is excluded by the runoff, not by anybody's majority.

## What to take away

- **Read the runoff line, not the score line.** In a Bloc result the scoring round tells you who the finalists were; the runoff tells you who won. Reporting a Bloc race by its score totals will eventually publish the wrong winner.
- **A large score lead is not a safe seat.** Ava's 63-point margin bought her four appearances in the runoff and nothing else. Margins in the two rounds are not commensurable and shouldn't be compared.
- **Being everyone's second choice is a weaker position in Bloc than it looks.** The compromise candidate has to actually be *preferred* by more than half of the deciding voters in at least one pair — and against a field of factional favorites, they may never be.

## See also

- [Bloc STAR](bloc_star.md) — elect, remove, re-run
- [The majority sweep](majority_sweep.md) — the other, more famous surprise
- [Honest limits](bloc_honest_limits.md)
- [When the top-scoring candidate isn't the winner](../../01_STAR/02_Examples/runoff_overturns_leader/) — the single-winner worked set
- [The Condorcet loser paradox](../../07_Concepts/voting_paradoxes/condorcet_loser_paradox.md) · [Approval, honest limits](../../04_Approval/01_Learn/approval_honest_limits.md)
