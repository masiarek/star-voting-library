# Solid coalitions — the guarantee STAR-PR is described as having, and doesn't

*A **solid coalition** is a group of voters who all prefer the same set of candidates to everything else. Proportionality for Solid Coalitions (PSC) says that if such a group holds a full quota, it must win a seat. Allocated Score is routinely filed under the school of methods that promise this. It does not deliver it — and the way it fails is more interesting than the fact that it does.*

**Level: 301 · deep dive**

→ the method: [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) · what proportionality promises: [what "proportional" actually means](../../01_Learn/what_proportional_means.md) · the neighbouring result: [free riding](../free_riding/README.md) · the single-winner half: [equal ranks on an IRV ballot](../../../method_comparisons/equal_rank_irv/README.md)

---

## The counterexample

Nine voters, four candidates, three seats. **Three of the nine — exactly one Hare quota — give Dinah a 5 and score every other candidate strictly lower.** They are a textbook solid coalition, at full quota, with maximum enthusiasm. PSC says they get a seat.

<!-- ballots:solid_coalition_quota_gets_nothing -->
*(No ballot art for `solid_coalition_quota_gets_nothing` — draw it with `build_style_ballot_images.py --from-yaml 03_STAR_PR/03_Criteria/solid_coalitions/cases/solid_coalition_quota_gets_nothing.yaml`.)*

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Arun,Bela,Curtis,Dinah
3,1,4,0
3,4,0,5    # solid for Dinah — but a 4 for Arun, which is what spends this ballot
0,4,4,0
4,0,0,5    # solid for Dinah — and a 4 for Arun
4,3,2,1
5,3,5,0
3,5,2,3
2,1,2,1
4,0,0,5    # solid for Dinah — and a 4 for Arun
```
<!-- /ballots -->

Allocated Score elects **Arun, Bela and Curtis**.

<!-- report:solid_coalition_quota_gets_nothing -->
```text
--- Allocated Score Voting Method (3 winners) ---

[Allocated Score Voting]
 Tabulating 9 ballots to fill 3 seats.
Count × Arun,Bela,Curtis,Dinah
    2 ×    4,   0,     0,    5
    1 ×    3,   1,     4,    0
    1 ×    3,   4,     0,    5
    1 ×    0,   4,     4,    0
    1 ×    4,   3,     2,    1
    1 ×    5,   3,     5,    0
    1 ×    3,   5,     2,    3
    1 ×    2,   1,     2,    1

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Arun          -- 28 -- First place
   Bela          -- 21
   Dinah         -- 20
   Curtis        -- 19
 Arun wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 3 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 1 ballot at score 5.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 2]
 Remaining allocation quota is 2.
 Allocating 3 ballots at score 4.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 66.67% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/3.
 3 ballots reweighted from 1 to 1/3.

[Allocated Score Voting: Round 2]
 Tabulating 8 remaining ballots.
Count × Arun,Bela,Curtis,Dinah
    2 ×    4,   0,     0,    5
    1 ×    3,   1,     4,    0
    1 ×    3,   4,     0,    5
    1 ×    0,   4,     4,    0
    1 ×    4,   3,     2,    1
    1 ×    5,   3,     5,    0
    1 ×    3,   5,     2,    3
    1 ×    2,   1,     2,    1

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 3 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 1 ballot at score 5.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 2]
 Remaining allocation quota is 2.
 Allocating 2 ballots at score 4.

[Allocated Score Voting: Round 3]
 Tabulating 5 remaining ballots.
Count × Arun,Bela,Curtis,Dinah
    2 ×    4,   0,     0,    5
    1 ×    3,   1,     4,    0
    1 ×    3,   4,     0,    5
    1 ×    0,   4,     4,    0
    1 ×    4,   3,     2,    1
    1 ×    5,   3,     5,    0
    1 ×    3,   5,     2,    3
    1 ×    2,   1,     2,    1

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 Arun
 Bela
 Curtis
```
<!-- /report -->

## Why it happens

Read the three Dinah ballots again. Two of them also give **Arun a 4**.

Arun wins the first seat on total score, and Allocated Score then fills his quota from the highest-scoring ballots available — one at score 5, then the score-4 group, which is exactly where those two Dinah supporters sit. Their ballots are spent on Arun and reweighted to a third of their value. By round 2 the coalition no longer holds a quota of unspent support, and Dinah never leads a round.

**Nothing was taken by a rival faction.** The seat was consumed paying for a candidate the coalition merely liked.

## The distinction that matters

The library's [what "proportional" actually means](../../01_Learn/what_proportional_means.md) groups the methods by school, and says quota-owning schools "hand a cohesive quota-sized faction a seat by construction," listing Allocated Score among them. That is a fair statement of **design philosophy**, sourced from electowiki's taxonomy. It is not a theorem, and the gap between the two is the whole subject of this page:

- **PSC is an ordinal axiom.** It reads only the *order* on a ballot — who is above whom.
- **Allocated Score is a cardinal method.** It runs on the *magnitudes*.

A ballot's ordinal projection is not what the method counts. So an ordinal guarantee does not follow from a quota-shaped cardinal design, however naturally the school label suggests it should. Compare the ranked side, where the guarantee is real and proved: STV satisfies PSC, and [Approval-STV satisfies its weak-order generalization](../../../method_comparisons/equal_rank_irv/README.md) (Delemazure & Peters, EC'24, Thm 5.4).

## How much this is worth

**An existence claim, and nothing more.** Stated plainly because the provenance changes the value:

- This profile was **found by random search** over 0-5 ballots, not built to make a point.
- It uses the **weakest** reading of the axiom available — Hare quota rather than Droop, and strict solid commitment — so a violation here is a violation under the stronger readings too.
- Violations appeared in roughly **1 in 100** random 9-voter, 4-candidate, 3-seat profiles; requiring every coalition member to score their candidate a full 5, as here, roughly **1 in 1700**.
- **How often this matters in a real election is not answered here.** Random ballots are not electorates. The search establishes that the guarantee does not hold; it says nothing about whether cohesive real-world factions get shortchanged in practice, which would need spatial or real ballot data.

## Not the same as free riding

[Free riding](../free_riding/README.md) is a **strategy**: withhold a star from a candidate who will win anyway, and get your ballot back for the seat you care about. Every ballot on this page is **sincere** — nobody is manipulating anything, and the coalition still loses.

The two share a mechanism — which score group a ballot is spent from — and make opposite points. Free riding is about what a voter can *gain* by lying. This is about what a voter cannot *rely on* by telling the truth. Both belong in an honest account of Allocated Score, and neither is a reason to abandon it: [every proportional method trades one guarantee for another](../../01_Learn/what_proportional_means.md), and the useful question is which trade you meant to make.

## Related

- [Free riding](../free_riding/README.md) · [the Alabama paradox](../alabama_paradox/README.md) · [vote unitarity](../vote_unitarity/README.md) — the other honest limits
- [What "proportional" actually means](../../01_Learn/what_proportional_means.md) — the schools, and the criteria each one keeps
- [Equal ranks on an IRV ballot](../../../method_comparisons/equal_rank_irv/README.md) — respect for cohesive majorities is this axiom at one seat, and STAR fails that too

*Source for the axiom: Haris Aziz & Barton Lee, "The expanding approvals rule: improving proportional representation and monotonicity" (2020) — the weak-order generalization of PSC; Michael Dummett for the original. The Approval-STV result is Théo Delemazure & Dominik Peters, ["Generalizing Instant Runoff Voting to Allow Indifferences"](https://arxiv.org/abs/2404.11407) (EC'24), Theorem 5.4. **Lean: neutral academic social choice.** The counterexample and the search are this library's own, and are labelled as such above.*
