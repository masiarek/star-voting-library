# Allocated Score — the recommended STAR-PR tabulation

*Seat the highest scorer, then mark **one quota's worth** of that winner's strongest supporters as represented and set them aside. Repeat until the seats are full. It is the Equal Vote Coalition's recommended Proportional STAR, the method BetterVoting runs as `STAR_PR`, and the one this library exercises most.*

→ Family: [the three STAR-PR methods](README.md) · the theory underneath: [the math behind proportional STAR](the_math_behind_proportional_star.md) · what a quota does and doesn't promise: [what "proportional" actually means](../what_proportional_means.md) · the majoritarian contrast: [Bloc STAR](../../../02_STAR_Bloc/README.md)

**Level: 301 · deep dive**

---

## How it counts

Three moves, repeated once per seat:

1. **Winner selection** — elect the highest-scoring remaining candidate.
2. **Allocating voters** — mark **one quota's worth** of that winner's strongest supporters as represented. Supporters are sorted into groups by the score they gave the winner: the 5-star group is allocated first, then 4-star, and so on until the quota is filled.
3. **Fractional surplus** — the last group added is usually a little larger than the quota needs. The extra is returned to that group and shared evenly, so those voters keep partial influence over later seats.

Subsequent rounds include everyone not yet *fully* represented. Partial representation is real here, and it is the point of a scored ballot: it records not just **whether** a voter is represented but **to what degree**.

Fractional surplus is what makes step 3 fair rather than arbitrary. Voters who gave the winner the *same* score are treated identically, instead of an alphabetical or random cut deciding which of them gets used up. ([electowiki](https://electowiki.org/wiki/Allocated_Score) adds that it preserves independence of irrelevant alternatives and monotonicity, though that claim carries a `citation needed` there — treat it as unverified.)

`voting_method: allocated` plus `num_winners: k`.

## Watch it count

63 ballots, 5 candidates, 3 seats. 39 voters back Alice/Ben/Cara, 24 back Dan/Eve — watch both fractional-surplus reweights, and the third seat going to the minority that [Bloc STAR](../../../02_STAR_Bloc/01_Learn/majority_sweep.md) would have shut out:

<!-- report:02a_c5_b63_proportional-allocated-score -->
```text
[Divergence from STAR]
  STAR                   = Ben
  Choose-One (Plurality) = Alice   (differs from STAR)
  Approval               = Alice   (differs from STAR)

--- Allocated Score Voting Method (3 winners) ---

[Allocated Score Voting]
 Tabulating 63 ballots to fill 3 seats.
Count × Alice,Ben,Cara,Dan,Eve
   18 ×     5,  4,   3,  0,  0
   15 ×     0,  0,   0,  5,  4
   12 ×     4,  5,   3,  0,  0
    9 ×     3,  4,   5,  0,  0
    9 ×     0,  0,   0,  4,  5

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Ben           -- 168 -- First place
   Alice         -- 165
   Cara          -- 135
   Dan           -- 111
   Eve           -- 105
 Ben wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 21 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 12 ballots at score 5.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 2]
 Remaining allocation quota is 9.
 Allocating 27 ballots at score 4.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 33.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 2/3.
 27 ballots reweighted from 1 to 2/3.

[Allocated Score Voting: Round 2]
 Tabulating 51 remaining ballots.
Count × Alice,Ben,Cara,Dan,Eve
   18 ×     5,  4,   3,  0,  0
   15 ×     0,  0,   0,  5,  4
   12 ×     4,  5,   3,  0,  0
    9 ×     3,  4,   5,  0,  0
    9 ×     0,  0,   0,  4,  5

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 21 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 15 ballots at score 5.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 2]
 Remaining allocation quota is 6.
 Allocating 9 ballots at score 4.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 66.67% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/3.
 9 ballots reweighted from 1 to 1/3.

[Allocated Score Voting: Round 3]
 Tabulating 36 remaining ballots.
Count × Alice,Ben,Cara,Dan,Eve
   18 ×     5,  4,   3,  0,  0
   15 ×     0,  0,   0,  5,  4
   12 ×     4,  5,   3,  0,  0
    9 ×     3,  4,   5,  0,  0
    9 ×     0,  0,   0,  4,  5

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 Alice
 Ben
 Dan
```
<!-- /report -->

## Where it stands, honestly

**It is a quota method, and it buys its guarantee from the family with the monotonicity problems.** Allocated Score passes the [Hare Quota Criterion](../what_proportional_means.md) — a cohesive quota-sized faction can force a seat. Classical apportionment theory says that guarantee has a price: quota methods are not house-size monotone, which is the door the **Alabama paradox** comes through.

That is not hypothetical here. This library asked the question and answered it: **[Allocated Score has the Alabama paradox](../../03_Criteria/alabama_paradox/README.md)**. Five gardeners, four candidates — a two-seat committee elects Basil and Dahlia, a *three*-seat committee elects Aster, Basil and Clover. Dahlia was on the smaller committee and is off the bigger one, with no ballot changed. The trade against a divisor method like [RRV](reweighted_range_voting.md) is a genuine [Balinski–Young](the_math_behind_proportional_star.md) one, not a winner.

**Provenance, with the lean stated.** Allocated Score is the consensus method of the Equal Vote 0–5 STAR Proportional Representation Research Committee, which spent roughly two years from 2018 comparing options at each stage of the tabulation (credited to Parker Friedland, Keith Edmonds, Jameson Quinn, Sara Wolk and others). That is an advocacy body selecting among methods it favors — what makes it checkable here regardless is that the procedure is precisely specified and independently reimplementable.

**Three named variants** you will meet in the same discussions:

- **Droop-quota Allocated Score** — swapping Hare for Droop mitigates free-riding but biases toward larger factions.
- **Sequential Monroe** — Allocated Score with a different *selection* rule (highest-scoring quota rather than highest-scoring candidate). One of the committee's three finalists; **the LH engine does not implement it**, so a third of the recommended shortlist has no runnable case in this library.
- **Allocated STAR** — adds a runoff on the **final** seat, so the last seat is decided the way single-winner STAR decides one.

## Scenarios in this library

Allocated Score is the STAR-PR method with real coverage here — **17 case files across seven folders**, against two apiece for [SSS](sequentially_spent_score.md) and [RRV](reweighted_range_voting.md). Gathered:

| Scenario | What it shows | Read · run |
|---|---|---|
| **The 63-ballot baseline** | The count above — two coalitions, three seats, both surplus reweights. | [page](../../02_Examples/cases/cases_pages/02a_c5_b63_proportional-allocated-score.md) · [yaml](../../02_Examples/cases/02a_c5_b63_proportional-allocated-score.yaml) |
| **The Alabama paradox** | Add a seat, someone loses one. The monotonicity price of a quota method, at 2 and 3 seats. | [lesson](../../03_Criteria/alabama_paradox/README.md) |
| **Fractional surplus, isolated** | The step-3 remainder handled on its own, cross-checked against BetterVoting. | [lesson](../../03_Criteria/bv_fixture_crosscheck/README.md) · [count](../../03_Criteria/bv_fixture_crosscheck/cases/cases_pages/bkk2gxj_fractional_surplus.md) |
| **Shadow — Lackner & Skowron** | The academic running example from the multi-winner literature; seats **A, B, C, D**. Compare with [RRV on the identical ballots](reweighted_range_voting.md), which seats **F** instead of D. | [page](../../02_Examples/cases/cases_pages/lackner_skowron_shadow_star_pr_c7_b12.md) · [yaml](../../02_Examples/cases/lackner_skowron_shadow_star_pr_c7_b12.yaml) |
| **A presidential board** | A realistic multi-seat board election, BV-backed. | [lesson](../../02_Examples/bv2130_presidential_board_star_pr.md) · [count](../../02_Examples/cases/cases_pages/bv2130_presidential_board_star_pr.md) |
| **Two seats, one neighborhood** | The same ten ballots that Bloc STAR sweeps — counted proportionally instead. The clearest bloc-vs-PR pair in the library. | [exercise 12](../../../01_STAR/05_Practice/ex12_bloc_vs_proportional.md) · [count](../../../01_STAR/05_Practice/cases/cases_pages/ex12_proportional_share.md) |
| **Quota circus** | Six candidates, 29 ballots, two seats — quota behavior under an awkward field. | [page](../../../06_Other/ballot_style_lab/cases/cases_pages/08_c6_b29_quota-circus-pr-2-seats.md) |
| **Herb council, 3 seats** | The ballot-style lab's PR half, beside its [bloc twin](../../../06_Other/ballot_style_lab/cases/cases_pages/07a_c5_b36_herb-council-bloc-3-seats.md). | [page](../../../06_Other/ballot_style_lab/cases/cases_pages/07b_c5_b36_herb-council-pr-3-seats.md) |
| **Food-Truck Row** | One electorate, five counts; this is its proportional share. | [set](../../../method_comparisons/food_truck_row/README.md) · [count](../../../method_comparisons/food_truck_row/cases/cases_pages/bv2210_fvg8y8_star_pr_share.md) |
| **Pets governance** | Six methods on one electorate — the proportional committee. | [set](../../../method_comparisons/pets_governance/README.md) · [count](../../../method_comparisons/pets_governance/cases/cases_pages/pets_gov_star_pr.md) |
| **Bloc vs PR, minimal** | The smallest possible pair: same ballots, both counts. | [set](../../../method_comparisons/bloc_vs_pr/README.md) · [count](../../../method_comparisons/bloc_vs_pr/cases/cases_pages/blocs_pr_c9_b10.md) |

## Related

- **The other two tabulations:** [Sequentially Spent Score](sequentially_spent_score.md) · [Reweighted Range Voting](reweighted_range_voting.md)
- **The shared theory:** [the math behind proportional STAR](the_math_behind_proportional_star.md) — quotas, apportionment, the JR → PJR → EJR hierarchy
- **The ranked-ballot cousin:** [STV vs STAR-PR](../stv/proportional_stv_vs_star.md) on one shared electorate
- **The plain-language fork:** [Electing more than one, simply](../../../07_Concepts/topics/electing_more_than_one.md)
