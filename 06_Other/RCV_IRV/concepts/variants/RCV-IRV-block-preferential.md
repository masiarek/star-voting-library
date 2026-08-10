# RCV-IRV (Block Preferential) — instant runoff, run once per seat

*The multi-winner instant runoff that is **not** STV. Fill one seat by a full IRV count, strike the winner off every ballot, and run the whole count again for the next seat — with every voter's ballot back at full strength. The result is majoritarian: a cohesive majority takes **every** seat.*

**Level: 201 · for voters**

→ Family: [Which RCV-IRV?](RCV_IRV_variants.md) · single-winner original: [RCV-IRV (Hare)](../RCV-IRV-Hare.md) · the proportional multi-winner cousin: [STV](../../../STV/README.md)

---

## In one line

**Block preferential voting** (also *preferential block voting*, *exhaustive preferential voting*) is [instant runoff](../RCV-IRV-Hare.md) repeated: run IRV on the ranked ballots, elect the winner, delete that candidate from every ballot, run IRV again — until all N seats are filled.

The word doing the work is **delete**. Nothing else is spent. The voters who elected the first winner get an undiminished ballot for the second seat, and the ones who elected nobody get exactly what they had before: no more, no less. That is the whole difference from [STV](../../../STV/README.md), where a winner's votes are consumed by a quota and only the *surplus* moves on.

## How the count works

1. Count first preferences on the full field.
2. Nobody over 50% of continuing ballots? Eliminate the last-place candidate, transfer those ballots to their next choice, repeat. (This is [Hare](../RCV-IRV-Hare.md), unmodified.)
3. Seat the winner. **Strike that candidate from every ballot** — including the ballots that just elected them.
4. Go back to step 1 with the reduced field, until N seats are filled.

## Worked example — the bakery co-op board, 2 seats

Twelve members, four candidates, two seats. A 7-member majority (5 who rank **Almond** first, 2 who rank **Brioche** first) and a 5-member minority who rank **Croissant** then **Danish**.

<!-- ballots:bpv_bakery_seat1_c4_b12 -->
Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
5:Almond>Brioche>Croissant>Danish
2:Brioche>Almond>Croissant>Danish
5:Croissant>Danish>Almond>Brioche
```
<!-- /ballots -->

**Seat 1** is an ordinary IRV count. Danish has no first preferences and Brioche only 2 — together they cannot catch either leader, so both go out (the engine batches them; textbook Hare drops Danish first, then Brioche, and lands in the same place). Brioche's two ballots move to Almond:

<!-- report:bpv_bakery_seat1_c4_b12 -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Block preferential voting — seat 1 of 2 (bakery co-op board)
 Tabulating 12 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Almond             5  Hopeful
Croissant          5  Hopeful
Brioche            2  Rejected
Danish             0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Almond             7  Elected
Croissant          5  Rejected
Brioche            0  Rejected
Danish             0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Almond

--- Transfers and inactive ballots (what the round tables leave out) ---
The tables above give each candidate's round total but not where a
transferred vote came FROM, nor how many ballots stopped counting.
Both are recomputed from the ballots, using the eliminations the
count above actually made.

ROUND 1 — 12 of 12 ballots still active; majority = 7
   Danish eliminated with 0:
      → (held no ballots)
   Brioche eliminated with 2:
      → Almond                    2

FINAL ROUND — 12 of 12 ballots still active; majority = 7
   Almond                    7  (58.3% of the still-active)  ← elected
   Croissant                 5  (41.7% of the still-active)
   Never exhausted, never transferred:
      5 ballots held by Croissant carried a lower ranking that was never read
      (the count stopped here, so those preferences did nothing).

Inactive ballots at the final round: 0 of 12 (0.0%).
   Almond's 7 is a majority of the 12 still active AND of all 12 cast (58.3%).
```
<!-- /report -->

**Seat 2** strikes Almond from all twelve ballots and starts over. The two Brioche-first voters are joined by the five Almond-first voters, whose second preference was Brioche all along — 7 of 12, an outright majority in a single round:

<!-- report:bpv_bakery_seat2_c3_b12 -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Block preferential voting — seat 2 of 2 (bakery co-op board)
 Tabulating 12 ballots (ranked ballots).

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Brioche            7  Elected
Croissant          5  Rejected
Danish             0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Brioche
```
<!-- /report -->

**Board: Almond and Brioche.** The 58% majority holds both seats; the 42% minority holds none — and no minority voter did anything wrong. They ranked sincerely, their ballots stayed active to the end, and they were simply outvoted twice by the same seven people.

## The property to remember: clones of the first winner take everything

That example is not a pathological construction; it is the method working as designed. Because every ballot is restored to full strength after each seat, whatever majority elected the first winner is still there — intact — to elect the second, third and fourth. Wikipedia states the consequence flatly: clones of the first winning candidate are **guaranteed** to win every available seat, and the method "regularly produces complete landslide majorities."

The same ballots make the point twice over. Throw the rankings away entirely and let each voter mark two names — plain [plurality block voting](../../../../method_comparisons/multi_member_plurality/README.md) — and the board is unchanged:

<!-- report:bpv_bakery_block_plurality_c4_b12 -->
```text
--- Block Voting (plurality-at-large) — 2 winners ---
 Tabulating 12 ballots (2 votes/voter).

Votes (most votes fill the seats):
   Almond        7  <- Elected
   Brioche       7  <- Elected
   Croissant     5
   Danish        5

Winners — Block Voting (plurality-at-large), 2 seats:
   1. Almond   (7 votes)
   2. Brioche   (7 votes)
```
<!-- /report -->

Now count the *same* ranked ballots with a quota instead, and a seat moves:

<!-- report:bpv_bakery_stv_c4_b12 -->
```text
--- STV / Single Transferable Vote (multi-winner — 2 seats) ---
  The same ballots under STV — 2 seats, and the minority gets one
 Tabulating 12 ballots (ranked ballots).
 2 seats; quota = 4.00 (exact Droop, votes/(seats+1)) — 33.3% of 12.
 Elected at >= quota, and every surplus is measured from it.
 (Hand-count Droop, floor(12/3)+1 = 5, is a different but equally standard rule.)

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Almond             5  Elected
Croissant          5  Elected
Brioche            2  Rejected
Danish             0  Rejected


Winner(s) — STV / Single Transferable Vote (multi-winner — 2 seats)
  Almond
  Croissant
```
<!-- /report -->

**Ranked ballots don't buy proportionality — the count does.** This is the same lesson [Bloc STAR among the at-large methods](../../../../02_STAR_Bloc/01_Learn/bloc_star_vs_other_bloc_methods.md) draws from the score side, and it is worth holding onto in public argument: "we'll switch to ranked ballots so minorities get represented" does not follow. The ballot decides what a voter can *say*; quotas and reweighting decide how seats are *shared*.

## Is that the same as "block voting"? No — it's one member of that class

Both terms have Wikipedia articles and they are not interchangeable. **[Block voting](https://en.wikipedia.org/wiki/Block_voting)** is the umbrella: any multi-seat system where each voter helps fill *every* seat, so a majority can take them all. **[Block preferential voting](https://en.wikipedia.org/wiki/Block_preferential_voting)** is the ranked-ballot member of that class.

| Member of the class | Ballot | How the seats are filled | Covered here |
|---|---|---|---|
| **Plurality block voting** (plurality-at-large) | mark N | top N by marks | [Block vs Limited vs SNTV](../../../../method_comparisons/multi_member_plurality/README.md) |
| **Approval block voting** | mark any number | top N by approvals | [Approval — multi-winner](../../../../04_Approval/01_Learn/Multiwinner_Approval/approval_multiwinner.md) |
| **Two-round block voting** | mark N, twice | field cut, then a runoff round | — |
| **Party block voting** / general ticket | pick one *party* | the winning party's whole slate | — |
| **Block preferential voting** | rank them | sequential IRV, one seat at a time | **this page** |
| *(Limited voting — the partial cousin)* | mark k **< N** | top N by marks | [Block vs Limited vs SNTV](../../../../method_comparisons/multi_member_plurality/README.md) |

Score ballots have their own member of this class — [Bloc STAR](../../../../02_STAR_Bloc/README.md), which is structurally the closest thing to block preferential voting in the library: it too must run the count once per seat, because a two-finalist runoff can no more yield "the top four" than a majority threshold can.

What none of these are is **[STV](../../../STV/README.md)**, which reads the identical ranked ballot as block preferential voting and is *proportional*. Calling both of them "multi-winner RCV" in the same breath is how the two get confused.

## Where it has been used

- **Australian Senate, 1919–1948** — replaced by STV, and that replacement is the argument in one line: the block-preferential Senate produced lopsided one-party chambers.
- **Northern Territory** local councils (Australia).
- **United States, recent and small:** Hendersonville, North Carolina (2007–2009); Aspen, Colorado (2009); Payson and Vineyard, Utah (2019).

Adoption is thin and often short-lived, which is worth stating fairly in both directions: it is not a widespread system whose flaws are being hidden, and it is not a fringe curiosity either — it ran a national upper house for thirty years.

## Strengths & weaknesses

- ✅ **One ranked ballot, one familiar count.** A jurisdiction already running IRV can fill several seats without teaching voters anything new.
- ✅ **Transfers, so no vote splitting.** Running two like-minded candidates cannot cost a faction a seat the way [SNTV](../../../../method_comparisons/multi_member_plurality/README.md) can — the strength it genuinely has over plurality block voting.
- ✅ **A majority body, if that is what you want.** For an executive-style board meant to act as one, majoritarian is a defensible design goal, not a defect. That choice is [the bigger decision](../../../../07_Concepts/topics/electing_more_than_one.md).
- ❌ **Complete sweeps are the normal outcome**, not the edge case — a 51% bloc can take 100% of the seats.
- ❌ **It inherits every IRV property**, seat by seat: [center squeeze](../RCV_IRV_center_squeeze.md), [non-monotonicity](../RCV_IRV_non_monotonicity.md), [exhausted ballots](../RCV_IRV_exhausted_ballots.md) — and it re-rolls them once per seat.
- ❌ **It is easily mistaken for STV**, which reads the same ballot and does the opposite thing with it.
- ❌ **N full counts, not one.** Each seat is its own multi-round tally, so the count is N times the work and N times the audit surface of a single IRV race — and none of it is [summable](../RCV_IRV_lack_of_summability.md).

## Run it yourself

The three counts above are runnable case files: [Block preferential voting — the bakery co-op board](../../../../method_comparisons/block_preferential/README.md).

## Related

- [Which RCV-IRV?](RCV_IRV_variants.md) — the family, and where the multi-winner branch splits
- [RCV-IRV (Hare)](../RCV-IRV-Hare.md) — the single-winner count this repeats
- [STV](../../../STV/README.md) — the same ballot, counted proportionally
- [Bloc STAR among the at-large methods](../../../../02_STAR_Bloc/01_Learn/bloc_star_vs_other_bloc_methods.md) — the whole majoritarian family on one table
- [Electing more than one, simply](../../../../07_Concepts/topics/electing_more_than_one.md) — majoritarian or proportional, the decision that comes first
- [Clone independence in Ranked Robin](../../../../05_Ranked_Robin/01_Learn/rr_clone_independence.md) — clones as a *criterion*, and why "clones sweep" is a different claim from "clones can't hurt you"

Sources: [Block preferential voting — Wikipedia](https://en.wikipedia.org/wiki/Block_preferential_voting) (definition, count, the clone-sweep property, jurisdictions), [Block voting — Wikipedia](https://en.wikipedia.org/wiki/Block_voting) (the umbrella class and its other members), [Plurality block voting — Wikipedia](https://en.wikipedia.org/wiki/Plurality_block_voting), [Single transferable vote — Wikipedia](https://en.wikipedia.org/wiki/Single_transferable_vote).
