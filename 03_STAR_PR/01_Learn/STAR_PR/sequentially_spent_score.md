# Sequentially Spent Score (SSS) — the smoother quota method

*Same idea as [Allocated Score](allocated_score.md) — seat the top scorer, then spend a quota's worth of ballot weight — but instead of using supporters **up** in whole groups, every supporting ballot spends score **proportionally** toward the quota. A smoother allocation of the same budget.*

→ Family: [the three STAR-PR methods](README.md) · the theory underneath: [the math behind proportional STAR](the_math_behind_proportional_star.md) · the method it refines: [Allocated Score](allocated_score.md)

**Level: 301 · deep dive**

---

## How it counts

Think of each voter as holding a **budget of stars**. Seat the highest-scoring candidate, then charge that candidate's supporters for the seat — each ballot paying in proportion to the score it gave, until one quota has been collected. A ballot that gave the winner 5 stars pays more than one that gave 3; neither is necessarily emptied.

That is the whole difference from Allocated Score, which sorts supporters into score groups and marks them represented group by group — 5-star group first, then 4-star — until the quota is filled, with only the final group split fractionally. SSS spreads the same cost across every supporter at once instead of exhausting them in tiers.

The principle behind the budget has a name — **vote unitarity** (Keith Edmonds, the method's designer): influence is spent *only in exchange for representation gained*, so a voter who scored the winner 0 pays nothing and keeps their full budget for later rounds. The election where that rule visibly decides a seat: [the two bullet voters](../../03_Criteria/vote_unitarity/README.md).

`voting_method: sss` plus `num_winners: k`.

## Watch it count

The same 63 ballots as the other two methods, so the three counts are directly comparable:

<!-- report:02b_c5_b63_proportional-sss -->
```text
[Divergence from STAR]
  STAR                   = Ben
  Choose-One (Plurality) = Alice   (differs from STAR)
  Approval               = Alice   (differs from STAR)

--- Sequentially Spent Score Voting Method (3 winners) ---

[Sequentially Spent Score]
 Tabulating 63 ballots to fill 3 seats.
Count × Alice,Ben,Cara,Dan,Eve
   18 ×     5,  4,   3,  0,  0
   15 ×     0,  0,   0,  5,  4
   12 ×     4,  5,   3,  0,  0
    9 ×     3,  4,   5,  0,  0
    9 ×     0,  0,   0,  4,  5

[Sequentially Spent Score: Round 1]
 The highest-scoring candidate wins a seat.
   Ben           -- 168 -- First place
   Alice         -- 165
   Cara          -- 135
   Dan           -- 111
   Eve           -- 105
 Ben wins a seat.

[Sequentially Spent Score: Round 1: Ballot allocation round]
 Total score is 168, Hare score quota is 105, giving back surplus.
 Reducing each ballot's stars by their vote * 3/8.
 Reweighted 39 ballots:
    27 ballots voted 4, stars reduced from 5 to 5/2, reweighted to 1/2.
    12 ballots voted 5, stars reduced from 5 to 15/8, reweighted to 3/8.

[Sequentially Spent Score: Round 2]
 The highest-scoring candidate wins a seat.
   Dan           -- 111     -- First place
   Eve           -- 105
   Alice         --  76+1/2
   Cara          --  63
 Dan wins a seat.

[Sequentially Spent Score: Round 2: Ballot allocation round]
 Total score is 111, Hare score quota is 105, giving back surplus.
 Reducing each ballot's stars by their vote * 2/37.
 Reweighted 24 ballots:
    15 ballots voted 5, stars reduced from 5 to 10/37, reweighted to 2/37.
    9 ballots voted 4, stars reduced from 5 to 45/37, reweighted to 9/37.

[Sequentially Spent Score: Round 3]
 The highest-scoring candidate wins a seat.
   Alice         -- 76+1/2  -- First place
   Cara          -- 63
   Eve           -- 14+7/37
 Alice wins a seat.

[Sequentially Spent Score: Winners — Sequentially Spent Score Voting Method (3 winners)]
 Alice
 Ben
 Dan
```
<!-- /report -->

**Alice, Ben, Dan** — the same slate Allocated Score and RRV reach on this electorate. On a clean two-coalition race the three tabulations usually agree; they part company on closer or more fragmented fields, which is exactly where the family difference below starts to bite.

## Where it stands, honestly

**SSS is a quota method**, like Allocated Score and unlike [RRV](reweighted_range_voting.md). It passes the [Hare Quota Criterion](../what_proportional_means.md) — a cohesive quota-sized faction can force a seat — and it inherits the same structural exposure that guarantee brings with it, the non-monotonicity that produces the [Alabama paradox](../../03_Criteria/alabama_paradox/README.md). That paradox is *demonstrated* in this library for Allocated Score; whether SSS's proportional spending changes the picture is **not something anyone here has checked**, and it would be a good and entirely runnable question.

**One piece of that exposure *has* been checked, and SSS shares it.** Because SSS also spends score from the top down, it inherits Allocated Score's [free-riding cliff](../../03_Criteria/free_riding/README.md): on the library's worked case, a bloc that scores a landslide winner 4 instead of 5 flips the second seat under **both** quota methods, while [RRV](reweighted_range_voting.md) — a divisor method with no score groups — holds. SSS's smoother, proportional spending is not a defence against this one.

**Equal Vote's own assessment**, worth quoting with its lean stated: they describe SSS as innovative, easy to explain, and promising — but newer, and still a proposal for further study rather than a settled recommendation. It is one of the committee's **three finalists** (with Allocated Score and Sequential Monroe), and Allocated Score is the one they actually recommend. That is an advocacy body ranking methods it favors; the criteria themselves are standard and checkable.

**Coverage here is thinner than Allocated Score's, and that is worth saying plainly.** Eight case files use `sss`, against 26 for Allocated Score. Nothing about the method makes it hard to test — the gap is this library's, not SSS's.

## Scenarios in this library

| Scenario | What it shows | Read · run |
|---|---|---|
| **The 63-ballot baseline** | The count above, directly comparable with the [Allocated](allocated_score.md) and [RRV](reweighted_range_voting.md) runs on identical ballots. | [page](../../02_Examples/cases/cases_pages/02b_c5_b63_proportional-sss.md) · [yaml](../../02_Examples/cases/02b_c5_b63_proportional-sss.yaml) |
| **Free riding** | SSS shares Allocated Score's cliff: the same one-star free ride flips the second seat here too. | [lesson](../../03_Criteria/free_riding/README.md) · [count](../../03_Criteria/free_riding/cases/cases_pages/free_ride_hylland_sss.md) |
| **STAR-PR, 3 seats** | A civic-priorities race — Housing, Schools, SmallBiz — counted on the same ballots as the STV file, which is what makes the [STV head-to-head](../../../method_comparisons/stv_vs_star_pr/README.md) possible. | [page](../../02_Examples/cases/cases_pages/03b_star_pr_3seats.md) · [yaml](../../02_Examples/cases/03b_star_pr_3seats.yaml) |
| **The two bullet voters** | Vote unitarity deciding a seat: two voters who spent nothing on the round-1 winner keep their full budgets and elect Amy. Also the regression profile for a fork-fixed engine defect ([upstream #19](https://github.com/larryhastings/starvote/issues/19)). | [lesson](../../03_Criteria/vote_unitarity/README.md) · [page](../../03_Criteria/vote_unitarity/cases/cases_pages/two_bullet_voters_sss.md) · [yaml](../../03_Criteria/vote_unitarity/cases/two_bullet_voters_sss.yaml) |

## Related

- **The other two tabulations:** [Allocated Score](allocated_score.md) — the recommended one · [Reweighted Range Voting](reweighted_range_voting.md) — the divisor alternative
- **The shared theory:** [the math behind proportional STAR](the_math_behind_proportional_star.md)
- **What the quota guarantees:** [what "proportional" actually means](../what_proportional_means.md)
