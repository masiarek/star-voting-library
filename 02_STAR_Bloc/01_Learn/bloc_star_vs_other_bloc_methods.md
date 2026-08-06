# Bloc STAR among the at-large methods

**One line:** Bloc STAR is one of several ways to fill N seats majoritarianly — alongside Block Plurality, Limited Voting, SNTV, Bloc Approval and Bloc Ranked Robin. They all answer "who does the majority most want?", and they differ in what the ballot lets you say and how badly a side is punished for running too many candidates.

→ The other half of the map: [proportional methods](../../03_STAR_PR/01_Learn/README.md) · the fork itself: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md) · the mechanics here: [Bloc STAR](bloc_star.md)

**Level: 201 · for voters**

---

## The family

Every method in this table fills N seats without any notion of a fair share. What separates them is the **ballot**, and one structural quirk of the count that only Bloc STAR has.

| Method | Ballot | How the seats are filled | Vote-splitting risk |
|---|---|---|:--:|
| **SNTV** (single non-transferable vote) | mark **1** candidate | top N by first choices | **severe** |
| **Limited Voting** | mark **k < N** | top N by marks | high |
| **Block Plurality** (plurality-at-large) | mark **N** | top N by marks | moderate |
| **Bloc Approval** | mark **any number** | top N by approvals | low |
| **Bloc Ranked Robin** | rank them | top N by head-to-head record | none |
| **Bloc STAR** | score all **0–5** | **sequential**: run STAR, seat the winner, remove, repeat | none |

The plurality family — [Block, Limited and SNTV](../../method_comparisons/multi_member_plurality/README.md) — differs *only* in votes per voter, and that one dial slides the outcome from majority sweep (3:0) to minority-tops-the-poll (2:1 with the minority leading) on the same 60/40 electorate.

## The structural difference: Bloc STAR is sequential

Look at the "how the seats are filled" column again. Five of the six methods produce **one ranking of all candidates and cut it at N**. Bloc STAR can't: STAR's second round is a **head-to-head between exactly two finalists**, and there is no way to read "the top four" out of a two-person runoff. So it has to elect one seat, remove that candidate, and run the whole count again.

Three things follow, and none of them are obvious from the family table:

- **Bloc STAR's result is a sequence, not a set.** The winners come out in the order they were seated, and that order is meaningful — it says which seat a tie decided, and gives a rough strength ranking of the winners. [Bloc Ranked Robin](../../method_comparisons/food_truck_row/cases/cases_pages/bv2210_fvg8y8_bloc_rr_sweep.md) prints a seat order too, but there it's just the record table sorted.
- **The scoring round is only a shortlist.** Since the runoff decides every seat, the point leader can be shut out entirely — see [the score leader can win no seat](score_leader_no_seat.md). Under Bloc Approval or Block Plurality that is impossible by construction: the tally *is* the result.
- **A tie has somewhere to propagate to.** Break a tie for seat 1 and you've changed which candidates remain for seat 2. In a top-N method a tie only ever swaps the last seat. See [ties, seat by seat](bloc_tiebreaks.md).

## The property that separates it from SNTV: no vote splitting

This is the practical argument, and [Food-Truck Row](../../method_comparisons/food_truck_row/README.md) makes it in one table. One 100-voter electorate, two seats: a **57-voter savory majority running three trucks** against a **43-voter sweet minority running two**.

| | first choices | SNTV | **Bloc STAR** | Bloc Ranked Robin | STAR-PR | STV |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| *savory : sweet (57 : 43)* | | **0 : 2** | **2 : 0** | **2 : 0** | **1 : 1** | **1 : 1** |

Under SNTV the 57% majority wins **nothing**: one non-transferable vote split three ways tops out at 20, behind both sweet trucks. The engine names it outright on the file:

```text
[Vote-splitting check]
  Choose-One first choices: Donut 22, Eclair 21, Arepa 20, Bao 19, Churro 18
  Plurality winner: Donut (22, 22.0%)
  Bloc 'Savory' = Arepa, Bao, Churro: combined 57 (57.0%); winner Donut is OUTSIDE it.
  => VOTE SPLITTING: the 'Savory' bloc is an outright majority (57 vs
     Donut's 22) but split across 3 candidates, so Donut won Choose-One.
     STAR elected Arepa.
```

Bloc STAR has nothing to split. Support **pools** across a side's candidates because scoring one costs you nothing on the others, so running a third truck can't cost the savory side a seat. That is the same property single-winner STAR is sold on, and it survives intact into the multi-winner case. It is also why the sweep is the *only* structural complaint worth making about Bloc STAR — you have to actually be a majority to sweep, and no amount of candidate-rationing gets you one.

## Ranked ballots don't buy you proportionality

The clearest lesson in that table is the pair of columns that agree. **Bloc Ranked Robin sweeps just as hard as Bloc STAR** (2:0), while **STV and STAR-PR both split the seats** (1:1) — one on a ranked ballot, one on a scored one.

So sweeps and shares are decided by the **count** — quotas, reweighting, transfers — not by the ballot's shape. "We'll switch to ranked ballots so minorities get represented" does not follow, and stating it that way in a public argument is a hostage to fortune. The ballot decides what voters can *say*; the count decides how seats are *shared*.

## Choosing

Once you've decided you want a majoritarian body at all ([the fork](../../07_Concepts/topics/electing_more_than_one.md) is the bigger decision), the choice within the family comes down to two questions:

1. **Do you want expressiveness, or the simplest possible count?** Bloc STAR and Bloc Approval both let voters support as many candidates as they like; only Bloc STAR lets them say *how much*, at the cost of a two-round count and a per-seat runoff to explain. Block Plurality's tally is a child's arithmetic — and it's the one that walks straight into vote splitting.
2. **Do you want one ballot for every race?** This is the underrated one. The 0–5 STAR ballot is the *same physical ballot* for single-winner, Bloc, and [proportional](../../03_STAR_PR/01_Learn/README.md) races — so a jurisdiction can change what a body is for without retraining its voters. SNTV and Limited Voting change the instruction line with the seat count.

And if the sweep is what you're trying to avoid, don't shop within this family at all — every method on this page will sweep. Go to [STAR-PR](../../03_STAR_PR/01_Learn/STAR_PR/README.md) or [STV](../../06_Other/STV/README.md).

## See also

- [Bloc STAR](bloc_star.md) · [the majority sweep](majority_sweep.md) · [honest limits](bloc_honest_limits.md)
- [Food-Truck Row](../../method_comparisons/food_truck_row/README.md) — one electorate, five counts, three outcomes
- [Block, Limited & SNTV](../../method_comparisons/multi_member_plurality/README.md) — the plurality family on one 60/40 electorate
- [Pets Governance](../../method_comparisons/pets_governance/README.md) — six methods, one electorate, at 3 seats
- [Approval — Multi-Winner](../../04_Approval/01_Learn/Multiwinner_Approval/approval_multiwinner.md) — bloc approval and its proportional adaptations
