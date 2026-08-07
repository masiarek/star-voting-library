# Three neighbors — where Allocated Score and SSS part company

*Three voters, three candidates, two seats. Cleo takes seat 1 under every method. Then Allocated Score seats **Bo**, who scored 3 points in total, while SSS and RRV seat **Ana**, who scored 8. The disagreement is entirely about what one lukewarm supporter's two stars cost her.*

→ Family: [when the STAR-PR methods disagree](README.md) · the other election: [Two officers](two_officers.md) · the methods: [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) · [SSS](../../01_Learn/STAR_PR/sequentially_spent_score.md)

**Level: 301 · deep dive**

---

## The ballots

| | Ana | Bo | Cleo | |
|---|--:|--:|--:|---|
| **Neighbor 1** | 4 | 0 | **5** | loves Cleo, likes Ana |
| **Neighbor 2** | 0 | 2 | 2 | lukewarm on both, nothing for Ana |
| **Neighbor 3** | 4 | 1 | **5** | loves Cleo, likes Ana |
| **Total** | **8** | **3** | **12** | |

Two seats, so the **Hare quota is 3 ÷ 2 = 1.5 voters**.

## Seat 1 is unanimous

Cleo leads on score, 12 to Ana's 8, and every method elects her. Nothing interesting yet — the interesting part is the bill.

## Seat 2: who paid for Cleo?

Cleo's support came from three different places: two 5-star ballots and one 2-star ballot. Each method charges for that differently.

**Allocated Score allocates by score tier.** It takes the 5-star group first — neighbors 1 and 3, two ballots — and that alone overfills the 1.5-voter quota. Fractional surplus returns the excess, leaving those two at **quarter weight**; the 4-star tier is never reached, and neither is the 2-star tier. So **neighbor 2 is never allocated at all and keeps her full weight of 1.0**:

| | weight | Ana | Bo |
|---|--:|--:|--:|
| Neighbor 1 | 0.25 | 1.00 | 0.00 |
| Neighbor 2 | **1.00** | 0.00 | **2.00** |
| Neighbor 3 | 0.25 | 1.00 | 0.25 |
| **Round 2 total** | | **2.00** | **2.25** |

Neighbor 2 outweighs the other two combined and elects her best remaining candidate. **Bo takes seat 2** — on three total points, against Ana's eight.

**SSS charges every supporter in proportion to the score they gave.** Neighbor 2's two stars for Cleo were real support, so they cost her real weight. She can no longer outweigh what neighbors 1 and 3 have left, and their 4-star backing carries **Ana** in instead.

**RRV** divides rather than spends, and lands with SSS: **Ana**.

## Is Bo's win a bug?

No — and this is the part worth sitting with. Neighbor 2 is a minority of one who got only partial representation from Cleo, and Allocated Score's answer is that she is therefore still owed a say. Handing seat 2 to the voter who is least represented is *exactly* what a proportional method is supposed to do. Score totals are not the standard here; [Bloc STAR](../../../02_STAR_Bloc/README.md) would elect Ana and Cleo and leave neighbor 2 with nothing at all.

The genuine disagreement is narrower, and it is about accounting: **did neighbor 2's two stars for Cleo buy her anything?** Allocated Score says no — she never reached a tier, so she is untouched and fully owed. SSS says yes — she got partial value and should pay partially for it. Both are defensible readings of "represented to a degree", which is why both are on Equal Vote's shortlist.

## The counts

**Allocated Score → Bo, Cleo**

<!-- report:three_neighbors_allocated -->
```text
[Divergence from STAR]
  STAR     = Cleo
  Approval = Ana   (differs from STAR)

--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 3 ballots to fill 2 seats.
Ana,Bo,Cleo
  4, 0,   5
  0, 2,   2
  4, 1,   5

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Cleo          -- 12 -- First place
   Ana           --  8
   Bo            --  3
 Cleo wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 1+1/2 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 75.00% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/4.
 2 ballots reweighted from 1 to 1/4.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Bo            -- 2+1/4 -- First place
   Ana           -- 2
 Bo wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Bo
 Cleo
```
<!-- /report -->

**Sequentially Spent Score → Ana, Cleo**

<!-- report:three_neighbors_sss -->
```text
[Divergence from STAR]
  STAR     = Cleo
  Approval = Ana   (differs from STAR)

--- Sequentially Spent Score Voting Method (2 winners) ---

[Sequentially Spent Score]
 Tabulating 3 ballots to fill 2 seats.
Ana,Bo,Cleo
  4, 0,   5
  0, 2,   2
  4, 1,   5

[Sequentially Spent Score: Round 1]
 The highest-scoring candidate wins a seat.
   Cleo          -- 12 -- First place
   Ana           --  8
   Bo            --  3
 Cleo wins a seat.

[Sequentially Spent Score: Round 1: Ballot allocation round]
 Total score is 12, Hare score quota is 7+1/2, giving back surplus.
 Reducing each ballot's stars by their vote * 3/8.
 Reweighted 3 ballots:
    2 ballots voted 5, stars reduced from 5 to 15/8, reweighted to 3/8.
    1 ballot voted 2, stars reduced from 5 to 15/4, reweighted to 3/4.

[Sequentially Spent Score: Round 2]
 The highest-scoring candidate wins a seat.
   Ana           -- 3     -- First place
   Bo            -- 1+7/8
 Ana wins a seat.

[Sequentially Spent Score: Winners — Sequentially Spent Score Voting Method (2 winners)]
 Ana
 Cleo
```
<!-- /report -->

**Reweighted Range Voting → Ana, Cleo**

<!-- report:three_neighbors_rrv -->
```text
[Divergence from STAR]
  STAR     = Cleo
  Approval = Ana   (differs from STAR)

--- Reweighted Range Voting Method (2 winners) ---

[Reweighted Range Voting]
 Tabulating 3 ballots to fill 2 seats.
Ana,Bo,Cleo
  4, 0,   5
  0, 2,   2
  4, 1,   5

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Cleo          -- 12 -- First place
   Ana           --  8
   Bo            --  3
 Cleo wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 Reweighted 3 ballots:
   2 ballots reweighted from 1 to 1/2.
   1 ballot reweighted from 1 to 5/7.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Ana           -- 4       -- First place
   Bo            -- 1+13/14
 Ana wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (2 winners)]
 Ana
 Cleo
```
<!-- /report -->

## Related

- **The companion election:** [Two officers](two_officers.md) — the same trick applied to the quota-versus-divisor split
- **The methods:** [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) · [Sequentially Spent Score](../../01_Learn/STAR_PR/sequentially_spent_score.md) · [Reweighted Range Voting](../../01_Learn/STAR_PR/reweighted_range_voting.md)
- **What a quota promises:** [what "proportional" actually means](../../01_Learn/what_proportional_means.md)
