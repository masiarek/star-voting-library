# When the STAR-PR methods disagree

*Allocated Score, SSS and RRV usually elect the same slate — which makes it easy to assume the choice between them is academic. It isn't. Two elections of **three voters each** are enough to split all three apart, and the seat turns on one thing: what a winner **costs** the voters who backed them.*

→ The methods themselves: [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) · [SSS](../../01_Learn/STAR_PR/sequentially_spent_score.md) · [RRV](../../01_Learn/STAR_PR/reweighted_range_voting.md) · the hub: [the three STAR-PR methods](../../01_Learn/STAR_PR/README.md) · the theory: [the math behind proportional STAR](../../01_Learn/STAR_PR/the_math_behind_proportional_star.md)

**Level: 301 · deep dive**

---

## The two elections

Both are 3 candidates, 3 voters, 2 seats — the smallest size at which any of this can happen. In both, seat 1 is unanimous across the methods and **the entire argument is about seat 2**.

| Election | Allocated | SSS | RRV | What it separates |
|---|---|---|---|---|
| **[Three neighbors](three_neighbors.md)** | **Bo**, Cleo | **Ana**, Cleo | **Ana**, Cleo | The two **quota** methods, from each other |
| **[Two officers](two_officers.md)** | Dana, **Finn** | Dana, **Finn** | Dana, **Eli** | The **quota** family, from the **divisor** one |

Between them every pair disagrees somewhere: Allocated ≠ SSS and Allocated ≠ RRV in the first, RRV ≠ SSS and RRV ≠ Allocated in the second.

## Why they can disagree at all

All three fill seat 1 the same way — elect the highest scorer. They differ only in what happens **next**, and there are exactly two decisions to make:

**1. Do you *spend* ballot weight, or *divide* it?** Allocated Score and SSS are **quota** methods: they charge a seat's cost against a quota's worth of ballot weight and use those voters up. RRV is a **divisor** method: nobody is ever used up, every ballot is simply divided by `1 + (score given to winners / max score)`. [Two officers](two_officers.md) is that difference, isolated — the same two voters land at weight **0.25** under the quota methods and **0.556** under RRV. Exhausted versus merely turned down, and it changes the seat.

**2. If you spend, do you charge by *tier* or in *proportion*?** Allocated Score sorts a winner's supporters into score groups and allocates them group by group — every 5-star backer first, then every 4-star backer — until the quota is full, splitting only the last group. SSS charges **every** supporter at once, each paying in proportion to the score they gave. [Three neighbors](three_neighbors.md) is that difference, isolated: a lukewarm 2-star supporter is never reached by the tiers, so Allocated Score leaves her at full weight and she picks seat 2 by herself.

That is the whole taxonomy, and it is why the classification in [what "proportional" actually means](../../01_Learn/what_proportional_means.md) is load-bearing rather than bookkeeping: quota methods pass the Hare Quota Criterion and pay for it with the non-monotonicity that produces the [Alabama paradox](../../03_Criteria/alabama_paradox/README.md); RRV is coherent and monotone and pays for that by not guaranteeing a quota.

## How these were found

Both were located by exhaustive smallest-first search over random 0–5 profiles, walking up from 3 ballots, and **neither involves a tie or a lot**. Each candidate profile was tabulated under five different tiebreaker seeds and discarded unless all five agreed — so what you are looking at is a property of the methods, not a coin toss. The hand-arithmetic in each page reproduces the engine's weights exactly.

Worth stating plainly: these are *constructed minimal* examples, not observed elections. They prove the disagreement is real and show its mechanism at a size you can check by hand; they say nothing about how often it happens on realistic ballots. On this library's larger PR cases the three methods usually agree — the [63-ballot baseline](../cases/cases_pages/02a_c5_b63_proportional-allocated-score.md) has all three electing Alice, Ben and Dan.

## Bigger, and not minimal

One more divergence, on a real academic profile rather than a constructed one — the **Lackner & Skowron shadow election**, 7 candidates, 12 ballots, 4 seats:

| Method | Winners |
|---|---|
| [Allocated Score](../cases/cases_pages/lackner_skowron_shadow_star_pr_c7_b12.md) | A, B, C, **D** |
| [RRV](../cases/cases_pages/lackner_skowron_shadow_star_pr_rrv_c7_b12.md) | A, B, C, **F** |

Three seats agree, the fourth doesn't — the same quota-versus-divisor split as [Two officers](two_officers.md), at a size where hand-checking stops being practical.

## The cases

| Case | Method | Winners | Read · run |
|---|---|---|---|
| Three neighbors | `allocated` | Bo, Cleo | [count](cases/cases_pages/three_neighbors_allocated.md) · [yaml](cases/three_neighbors_allocated.yaml) |
| Three neighbors | `sss` | Ana, Cleo | [count](cases/cases_pages/three_neighbors_sss.md) · [yaml](cases/three_neighbors_sss.yaml) |
| Three neighbors | `rrv` | Ana, Cleo | [count](cases/cases_pages/three_neighbors_rrv.md) · [yaml](cases/three_neighbors_rrv.yaml) |
| Two officers | `allocated` | Dana, Finn | [count](cases/cases_pages/two_officers_allocated.md) · [yaml](cases/two_officers_allocated.yaml) |
| Two officers | `sss` | Dana, Finn | [count](cases/cases_pages/two_officers_sss.md) · [yaml](cases/two_officers_sss.yaml) |
| Two officers | `rrv` | Dana, Eli | [count](cases/cases_pages/two_officers_rrv.md) · [yaml](cases/two_officers_rrv.yaml) |
