# RCV-IRV Fails the Equal Vote (Equality) Criterion

**One line:** RCV-IRV does **not** deliver an equally weighted vote. Because it counts only one ranking at a time and eliminates candidates sequentially, two voters with exactly opposite preferences often **cannot cancel each other out** — so vote-splitting and the spoiler effect survive. STAR, Score, and Approval pass this test; RCV-IRV does not.

→ The property itself, and why STAR passes it: [The Equally Weighted Vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md). Related IRV-specific failures: [center squeeze](RCV_IRV_center_squeeze.md) · [exhausted ballots](RCV_IRV_exhausted_ballots.md). Curriculum: [301.4](../CURRICULUM.md).

---

## The test it fails

The **Equal Vote Criterion** (the "Test of Balance") asks: for any ballot one voter casts, can another voter cast an *equal-and-opposite* ballot so the two together change nothing? If yes, no voter's ballot outweighs another's. The full concept — and the worked example where two opposite score ballots cancel — is on the STAR page, [The Equally Weighted Vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md). RCV-IRV fails it for two connected reasons: **vote-splitting** and **ballot exhaustion**.

## Why RCV-IRV fails: one active ranking at a time

Under RCV-IRV your ballot only counts for one candidate at a time, and candidates are eliminated round by round. Whether your later preferences ever get counted depends on the *order* others are eliminated — which is outside your control. So two opposite voters don't reliably net to zero the way two opposite score ballots do.

### A worked scenario

Three candidates, A, B, C. Two voters hold opposite views of the front-runners:

- **Voter X** loves **A**, hates **B**.
- **Voter Y** loves **B**, hates **A**.

Under a method that passes the Equal Vote (Score or STAR), X and Y cancel **perfectly** on A-vs-B and weigh C equally — balance holds. Under **RCV-IRV** they often can't:

- X ranks **A > C**, Y ranks **B > C**.
- A and B split the anti-C support. If both are eliminated before consolidating, **both ballots transfer to C** — and **C wins**.

X and Y did *not* have an equal-and-opposite effect. They inadvertently **both helped C** by splitting the opposition. Their votes were not equally weighted — the hallmark failure of the Equality Criterion.

### The same failure, counted — balanced ballots flip the winner

Here it is with real numbers — the exact mirror of the STAR case where opposite ballots *do* cancel ([equal & opposite](../../01_STAR/equal_and_opposite/)). Three candidates on a line — **Ada** (left), **Bruno** (center), **Cyrus** (right) — and a small electorate where Bruno is the compromise:

```
4: Bruno > Ada  > Cyrus
3: Ada   > Bruno > Cyrus
2: Cyrus > Bruno > Ada
```

**Before.** Bruno is the [Condorcet winner](../topics/condorcet/) — he beats Ada 6–3 and Cyrus 7–2 — *and* RCV-IRV elects him too: Cyrus has the fewest first-choices (2) and is eliminated, his ballots flow to Bruno, Bruno wins 6–3. IRV and the head-to-head agree.

Now add **three exact-opposite pairs** — each `Ada > Bruno > Cyrus` matched by its perfect reverse `Cyrus > Bruno > Ada`. Under Score, STAR, or [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) these **cancel**: every pairwise margin just grows symmetrically and **Bruno stays the Condorcet winner** (now 9–6 and 10–5). The balanced ballots changed nothing about whom a majority prefers.

But watch RCV-IRV:

```
Round 1:  Ada 6   Cyrus 5   Bruno 4     ← Bruno now has the FEWEST first-choices
          → Bruno eliminated
Round 2:  Ada 10  Cyrus 5               → Ada wins
```

The six new ballots put their first-choices on the two **extremes** (Ada +3, Cyrus +3) and *none* on the **center** (Bruno +0) — because IRV only ever counts the top of each ballot. Perfectly balanced ballots, which cancel under every other method, **squeezed the center candidate out and handed the win to an extreme.** Equal and opposite in, a flipped winner out — the effect was not zero.

That is the Test of Balance failing in a single election, and the mechanism is exactly [center squeeze](RCV_IRV_center_squeeze.md): under sequential elimination it's *first-choice* counts that decide who survives, so opposite ballots don't cancel — they pile onto the ends and starve the middle. **Run it:** [`06_Other/RCV_IRV/equal_vote_balance/`](../../06_Other/RCV_IRV/equal_vote_balance/) (base → Bruno, plus-balanced → Ada).

## Vote-splitting and exhaustion, precisely

- **Vote-splitting.** Elimination order means a faction that runs *more* candidates is statistically disadvantaged; opposite preferences don't cancel, they interact with who gets eliminated when. (This is the same root cause as [center squeeze](RCV_IRV_center_squeeze.md).)
- **Ballot exhaustion.** In the deciding round, some voters' later choices are never counted because their ballot already **exhausted** — so those voters get no equal-and-opposite say at the moment it matters. See [exhausted ballots](RCV_IRV_exhausted_ballots.md).

## The other side, fairly stated

FairVote argues RCV-IRV *upholds* "one person, one vote" better than Choose-One: voters can name a favorite without wasting the vote and still weigh in on the front-runners ([their essay](https://fairvote.org/how_ranked_choice_voting_survives_the_one_person_one_vote_challenge/)). The equal-vote reply: that defends RCV-IRV against *Choose-One*, not against the Test of Balance — RCV-IRV still discards some voters' later rankings in the deciding round, so the balance fails precisely in the competitive, 3+-candidate races where it matters.

## Is this a fair criticism? (the honest version)

Mostly **yes — when stated precisely**, with two caveats worth stating out loud:

- **Fair:** it is *provably* true that RCV-IRV fails the cancellation / Equal-Vote criterion that Score, STAR, and Approval pass, and this isn't abstract — it lines up with real, documented behavior (center squeeze and spoilers in competitive 3+-candidate races, and ballot exhaustion in the deciding round).
- **Caveat 1 — don't overstate it.** "RCV-IRV gives some people an unequal vote" can mislead a lay listener into thinking some voters literally get *more ballots*. They don't. Every voter casts one ballot and every first choice is counted equally; the inequality is subtler — it's about *whose later preferences get counted* once elimination starts. RCV-IRV does satisfy "one person, one vote" in the ordinary **legal** sense (courts have upheld it), which is a different bar than the Test of Balance.
- **Caveat 2 — the criterion isn't neutral.** The Equal-Vote / cancellation criterion is promoted mainly by cardinal-method advocates (the Equal Vote Coalition), and cardinal methods pass it essentially by construction; even its formalizer notes it may not fully capture the informal intent. So "RCV-IRV fails *our* criterion" carries some method-favoring flavor, and it's largely the spoiler/center-squeeze critique in equal-vote language rather than a wholly separate defect.

Bottom line: precise and fair as "RCV-IRV fails a specific, well-defined balance property that cardinal methods pass, with real spoiler/exhaustion consequences." It tips into unfair if sold as "IRV literally weights some votes more" or as a neutral, method-agnostic gold standard.

## Keep the scope precise

This is an **RCV-IRV** failure, not a property of ranked ballots in general. With only **two** candidates every method passes. And **Ranked Robin** — also an RCV (ranked) method — reads every rank and compares pairwise, so it *passes* the Equal Vote. "RCV fails the equal vote" would be the imprecise overclaim; it's **RCV-IRV's sequential-elimination count** specifically that fails. <!-- terminology-ok: teaches the RCV-vs-RCV-IRV distinction -->

## Sources

- Equal Vote Coalition — the Equal Vote / Test of Balance: <https://www.equal.vote/equalvote>
- electowiki — [Equal Vote Criterion](https://electowiki.org/wiki/Equal_Vote_Criterion)
- FairVote (contrasting view) — [How RCV survives the one-person-one-vote challenge](https://fairvote.org/how_ranked_choice_voting_survives_the_one_person_one_vote_challenge/)
- Companion page: [The Equally Weighted Vote (STAR)](../STAR_Voting/properties_and_limits/equally_weighted_vote.md)
