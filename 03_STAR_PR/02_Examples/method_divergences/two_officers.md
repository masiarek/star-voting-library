# Two officers — where RRV parts company with the quota methods

*Three voters, three candidates, two seats. Dana takes seat 1 under every method. Then Allocated Score and SSS seat **Finn**, while RRV seats **Eli**. The three methods charge Dana's two big backers **¼, ⅓ and 5⁄9** of their weight respectively — a ladder from harshest to gentlest — and the seat flips on the last rung.*

→ Family: [when the STAR-PR methods disagree](README.md) · the other election: [Three neighbors](three_neighbors.md) · the methods: [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) · [RRV](../../01_Learn/STAR_PR/reweighted_range_voting.md)

**Level: 301 · deep dive**

---

## The ballots

| | Dana | Eli | Finn | |
|---|--:|--:|--:|---|
| **Voter 1** | **4** | 3 | 1 | Dana first, Eli a solid second |
| **Voter 2** | **4** | 2 | 2 | Dana first, Eli and Finn equal behind |
| **Voter 3** | 1 | 3 | **4** | Finn first, barely backs Dana |
| **Total** | **9** | **8** | **7** | |

Two seats, so the **Hare quota is 3 ÷ 2 = 1.5 voters**.

## Seat 1 is unanimous

Dana leads at 9, and every method elects her. Voters 1 and 2 put her there with 4 stars each; voter 3 gave her a single star.

## Seat 2: how hard are Dana's backers charged?

Voters 1 and 2 put Dana in with 4 stars each and now owe something for it. All three methods agree they owe *something*; they disagree about how much, and the answer is a clean ladder.

**Allocated Score — voters 1 and 2 drop to ¼.** The quota is 1.5 voters and the 4-star tier holds two ballots, so it overfills; fractional surplus keeps them at a quarter. Voter 3 is never reached by the tiers at all and stays at **full weight**:

| | weight | Eli | Finn |
|---|--:|--:|--:|
| Voter 1 | ¼ | 0.75 | 0.25 |
| Voter 2 | ¼ | 0.50 | 0.50 |
| Voter 3 | **1** | 3.00 | **4.00** |
| **Round 2** | | **4¼** | **4¾ ← Finn** |

**SSS — voters 1 and 2 drop to ⅓.** SSS charges against a *score* quota rather than a ballot quota: total score 9, Hare score quota 7½, so every supporter's stars are reduced in proportion to what they gave. Voter 3 pays too, landing at ⅚ — she gave Dana a star, so she is charged for a star:

| | weight | Eli | Finn |
|---|--:|--:|--:|
| Voter 1 | ⅓ | 1.00 | 0.33 |
| Voter 2 | ⅓ | 0.67 | 0.67 |
| Voter 3 | ⅚ | 2.50 | 3.33 |
| **Round 2** | | **4⅙** | **4⅓ ← Finn** |

Gentler than Allocated Score, and Eli closes from 0.50 behind to 0.17 behind — but not enough.

**RRV — voters 1 and 2 only drop to 5⁄9.** No quota is computed at all; each ballot is simply divided by `1 + (score given to winners / max score)`. Voters 1 and 2 gave 4 of 5, so `1 / 1.8 = 5⁄9`. Voter 3 gave 1 of 5, so `1 / 1.2 = ⅚` — the same as under SSS:

| | weight | Eli | Finn |
|---|--:|--:|--:|
| Voter 1 | 5⁄9 | 1.67 | 0.56 |
| Voter 2 | 5⁄9 | 1.11 | 1.11 |
| Voter 3 | ⅚ | 2.50 | 3.33 |
| **Round 2** | | **5.28 ← Eli** | **5.00** |

Voters 1 and 2 keep enough to carry their shared second choice, and **Eli takes seat 2** instead.

## What the ladder means

Line the three charges up against the same two voters:

| Method | Voters 1 & 2 charged down to | Eli − Finn | Seat 2 |
|---|--:|--:|---|
| Allocated Score | **¼** = 0.250 | −0.50 | Finn |
| SSS | **⅓** = 0.333 | −0.17 | Finn |
| RRV | **5⁄9** = 0.556 | **+0.28** | **Eli** |

Nothing else differs — same ballots, same seat 1, same arithmetic afterwards. As the charge gets gentler, the two partly-satisfied voters keep more say and their second choice climbs, until at RRV it overtakes. A **quota** method decides those voters have *had their seat* and spends them down hard; a **divisor** method decides they are merely *partly satisfied* and turns them down by a proportion. The first hands seat 2 to the one voter still hungry; the second lets the partly-fed keep bidding.

Note where the two quota methods differ from each other, since it is easy to miss: Allocated Score leaves voter 3 at **full** weight because the score tiers never reach her, while SSS charges her ⅚ for the single star she gave Dana. Same winner here, different books — and [Three neighbors](three_neighbors.md) is the election where that same bookkeeping gap changes the seat.

Neither is a malfunction. This is the [Balinski–Young](../../01_Learn/STAR_PR/the_math_behind_proportional_star.md) trade showing up in three ballots: the quota methods guarantee that a quota-sized faction can force a seat and pay with the non-monotonicity behind the [Alabama paradox](../../03_Criteria/alabama_paradox/README.md); RRV is coherent and monotone and pays by [failing the Hare Quota Criterion](../../01_Learn/what_proportional_means.md). Here that abstraction has a face: voter 3 is a one-person faction just over a 1.5 quota's worth of unspent weight, and only the quota methods guarantee she gets the seat.

## The counts

**Allocated Score → Dana, Finn**

<!-- report:two_officers_allocated -->
```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 3 ballots to fill 2 seats.
Dana,Eli,Finn
   4,  3,   1
   4,  2,   2
   1,  3,   4

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Dana          -- 9 -- First place
   Eli           -- 8
   Finn          -- 7
 Dana wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 1+1/2 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 4.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 75.00% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/4.
 2 ballots reweighted from 1 to 1/4.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Finn          -- 4+3/4 -- First place
   Eli           -- 4+1/4
 Finn wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Dana
 Finn
```
<!-- /report -->

**Sequentially Spent Score → Dana, Finn**

<!-- report:two_officers_sss -->
```text
--- Sequentially Spent Score Voting Method (2 winners) ---

[Sequentially Spent Score]
 Tabulating 3 ballots to fill 2 seats.
Dana,Eli,Finn
   4,  3,   1
   4,  2,   2
   1,  3,   4

[Sequentially Spent Score: Round 1]
 The highest-scoring candidate wins a seat.
   Dana          -- 9 -- First place
   Eli           -- 8
   Finn          -- 7
 Dana wins a seat.

[Sequentially Spent Score: Round 1: Ballot allocation round]
 Total score is 9, Hare score quota is 7+1/2, giving back surplus.
 Reducing each ballot's stars by their vote * 1/6.
 Reweighted 3 ballots:
    2 ballots voted 4, stars reduced from 5 to 5/3, reweighted to 1/3.
    1 ballot voted 1, stars reduced from 5 to 25/6, reweighted to 5/6.

[Sequentially Spent Score: Round 2]
 The highest-scoring candidate wins a seat.
   Finn          -- 4+1/3 -- First place
   Eli           -- 4+1/6
 Finn wins a seat.

[Sequentially Spent Score: Winners — Sequentially Spent Score Voting Method (2 winners)]
 Dana
 Finn
```
<!-- /report -->

**Reweighted Range Voting → Dana, Eli**

<!-- report:two_officers_rrv -->
```text
--- Reweighted Range Voting Method (2 winners) ---

[Reweighted Range Voting]
 Tabulating 3 ballots to fill 2 seats.
Dana,Eli,Finn
   4,  3,   1
   4,  2,   2
   1,  3,   4

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Dana          -- 9 -- First place
   Eli           -- 8
   Finn          -- 7
 Dana wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 Reweighted 3 ballots:
   2 ballots reweighted from 1 to 5/9.
   1 ballot reweighted from 1 to 5/6.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Eli           -- 5+5/18 -- First place
   Finn          -- 5
 Eli wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (2 winners)]
 Dana
 Eli
```
<!-- /report -->

## Related

- **The companion election:** [Three neighbors](three_neighbors.md) — the same trick applied to the two quota methods
- **The methods:** [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) · [Sequentially Spent Score](../../01_Learn/STAR_PR/sequentially_spent_score.md) · [Reweighted Range Voting](../../01_Learn/STAR_PR/reweighted_range_voting.md)
- **At a bigger size:** the [Lackner & Skowron shadow election](README.md#bigger-and-not-minimal) splits Allocated Score and RRV on a real academic profile
