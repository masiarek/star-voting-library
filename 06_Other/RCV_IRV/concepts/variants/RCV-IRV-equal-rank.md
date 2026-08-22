# RCV-IRV with equal ranks — Approval-IRV and Split-IRV

*Every other page in this folder varies **who gets eliminated**. This one varies the **ballot**: what if a voter may mark two candidates equal? Instant runoff has no answer built in — it was defined for strict rankings — so an answer has to be chosen, and there are two.*

**Level: 301 · deep dive**

→ Family: [Which RCV-IRV?](RCV_IRV_variants.md) · the default it extends: [RCV-IRV (Hare)](../RCV-IRV-Hare.md) · the ballot: [weak ranks](../../../../07_Concepts/scores_and_ranks/weak_ranks.md) · the worked cases: [equal ranks on an IRV ballot](../../../../method_comparisons/equal_rank_irv/README.md)

---

## In one line

A ballot's **top surviving choices** may be a set rather than a single name, and the only question is what that set is worth: **Approval-IRV** gives each of them a full point, **Split-IRV** gives them a point between them. Eliminate the lowest, transfer, repeat — everything else about instant runoff is unchanged.

## Why this isn't already settled

On a US ranked ballot, two candidates in one rank column is an **overvote**. Depending on the jurisdiction the ballot is rejected outright, or counted until the doubled rank is reached and then set aside. That is not the count declining to handle a tie so much as the *rule* not having one: Hare's method takes a linear order, and a tie isn't one.

So this variant is not a proposal to count existing ballots differently. It is a proposal to **accept a ballot that is currently thrown away** — and the case for it is partly operational. In San Francisco's 2019 mayoral election, 899 of 206,117 ballots (0.4%) could be read as a coherent ranking with at least one deliberate tie; in Scotland's 2017 local elections 1.6% of ballots were rejected for multiple top choices. Those ballots are not confused, they are unrepresentable.

## How the count works, step by step

1. Every ballot **votes for its highest-ranked candidates who are still standing** — possibly more than one.
2. Score them: **Approval-IRV** hands each one a full point; **Split-IRV** splits one point evenly (three top choices → ⅓ each).
3. **Eliminate the lowest-scoring** candidate.
4. Repeat. Ballots whose whole top class is gone drop to their next class.

On a ballot with no ties, every top class has exactly one name and both rules *are* ordinary Hare IRV. They can only differ once somebody marks a tie.

## Which one is right

Not a matter of taste — there is a theorem. Delemazure & Peters (EC'24) look at the whole class of "score somehow, drop the lowest, repeat" rules and prove **Approval-IRV is the unique one that keeps the properties instant runoff is sold on**:

| | Approval-IRV | Split-IRV |
|---|---|---|
| **Independence of clones** | ✅ | ❌ |
| **Respect for cohesive majorities** | ✅ | ❌ |
| **Indifference monotonicity** | ✅ | ❌ |
| **Generalized PSC** (multi-winner: Approval-STV vs Split-STV) | ✅ | ❌ |

The awkward part is that **Split-IRV is the one in the field.** It is the natural reading — one voter, one vote, divided — and it is what the John Muir Trust has used for trustee elections since 1998, the London Mathematical Society since 1999, and what R's `vote` package implements. It descends from the Meek/Warren/Hill construction in *Voting Matters*, which replaced each tied ballot with weighted copies of every way of breaking the tie; Split-IRV is that idea in polynomial time.

**Independence of clones is the expensive loss.** It is [instant runoff's central claim over Choose-One](../why_rcv_irv.md) — that a similar candidate can't spoil the race — and Tideman proved strict-ballot IRV has it. An organization that allows equal ranks the intuitive way has given that up without being told.

## Worked example — five voters, and the rules disagree

<!-- ballots:equal_rank_five_voters -->
The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| # | Ballot as marked | Aida | Bram | Chloe | Dante |
|:--:|:--|:--:|:--:|:--:|:--:|
| 1 | <img src="../../../../method_comparisons/equal_rank_irv/cases/img/equal_rank_five_voters_ballot_1.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — Aida and Bram equal-first: Aida 5, Bram 5, Chloe 4, Dante 0."> | 5 | 5 | 4 | 0 |
| 2 | <img src="../../../../method_comparisons/equal_rank_irv/cases/img/equal_rank_five_voters_ballot_2.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — a three-way equal-first, Chloe alone below: Aida 5, Bram 5, Chloe 2, Dante 5."> | 5 | 5 | 2 | 5 |
| 3 | <img src="../../../../method_comparisons/equal_rank_irv/cases/img/equal_rank_five_voters_ballot_3.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — Bram alone on top, Aida and Chloe equal: Aida 3, Bram 5, Chloe 3, Dante 0."> | 3 | 5 | 3 | 0 |
| 4 | <img src="../../../../method_comparisons/equal_rank_irv/cases/img/equal_rank_five_voters_ballot_4.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — Chloe alone on top, Bram and Dante equal-last: Aida 3, Bram 0, Chloe 5, Dante 0."> | 3 | 0 | 5 | 0 |
| 5 | <img src="../../../../method_comparisons/equal_rank_irv/cases/img/equal_rank_five_voters_ballot_5.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — the one fully strict ballot: Aida 4, Bram 0, Chloe 2, Dante 5."> | 4 | 0 | 2 | 5 |
<!-- /ballots -->

**Approval-IRV.** Round 1 top-choice counts: Bram 3, Aida 2, Dante 2, Chloe 1 → Chloe out. Then Dante. Then Aida beats Bram head-to-head. **Aida wins.**

**Split-IRV.** Aida is a *shared* first choice on two ballots and an outright first choice on none, so she scores ½ + ⅓ = 0.83 — the lowest in the room — and is **eliminated first**. Bram wins.

Same five ballots. The only difference is what a tie is worth.

Run it, and the rest of the set:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/approval_irv_report.py method_comparisons/equal_rank_irv/cases/equal_rank_five_voters.yaml
```

## What it does and doesn't fix

- ✅ **Accepts ballots that are currently spoiled** — and the spoilage isn't evenly distributed: in San Francisco the weak-order rate correlates negatively with precinct income (r = −0.4).
- ✅ **Less work for the voter.** Rank a few candidates top, a few bottom, and skip the ones you can't separate — no need to invent an order you don't feel.
- ✅ **Partly softens favorite betrayal.** Rank your favorite *and* the front-runner joint-first and your vote is live for both. It doesn't eliminate the incentive, but the paper shows the honest version is safe in a precise sense (Section 4).
- ❌ **Fixes the ballot, not the count.** Approval-IRV is still non-monotonic, still not Condorcet-consistent, still [center-squeezable](../RCV_IRV_center_squeeze.md). Everything this repo says about IRV's *tabulation* survives intact.
- ❌ **More complicated instructions**, which is its own source of voter error — possibly giving back some of the spoiled ballots it saves.

## Where it's used

**Approval-IRV: nowhere.** It was described by Svante Janson in 2016, from his historical work on Phragmén's 1903 Swedish methods, and discussed sporadically on election-methods mailing lists since 1996 — but it has never been adopted, and the 2024 paper is its first axiomatic study. **Split-IRV: in real organizational use**, as above.

## A note for this repo's readers

The problem this variant exists to solve **does not arise on a score ballot.** A 0-5 ballot has always let a voter rate two candidates the same, and [STAR reads that as genuine indifference](../../../../07_Concepts/scores_and_ranks/weak_ranks.md) rather than as a spoiled mark. Worth saying without gloating: this is a serious paper doing serious work to give ranked ballots an expressiveness that most of the world's ranked elections lack — and on the profiles built to separate good behavior from bad, STAR mostly lands where Approval-IRV does. Mostly. [The full comparison](../../../../method_comparisons/equal_rank_irv/README.md) includes the profile where STAR fails an axiom Approval-IRV keeps.

## Related

- [RCV-IRV (Hare)](../RCV-IRV-Hare.md) — the strict-ballot default this generalizes
- [Which RCV-IRV?](RCV_IRV_variants.md) — the family table
- [Weak ranks](../../../../07_Concepts/scores_and_ranks/weak_ranks.md) · [strict vs. weak ranks](../../../../07_Concepts/scores_and_ranks/strict_vs_weak_ranks.md)
- [Equal ranks on an IRV ballot](../../../../method_comparisons/equal_rank_irv/README.md) — six runnable cases and the STAR comparison

Sources: Théo Delemazure & Dominik Peters, ["Generalizing Instant Runoff Voting to Allow Indifferences"](https://arxiv.org/abs/2404.11407) (EC'24; [ACM DL](https://dl.acm.org/doi/10.1145/3670865.3673501)) — **lean: neutral academic social choice**, and explicit that Approval-IRV inherits IRV's known defects. Prior art: Svante Janson, "Phragmén's and Thiele's election methods" (2016), §18.2; Meek, Warren and Hill in *Voting Matters* (1994–2001) for the Split construction; [electowiki](https://electowiki.org/wiki/Instant-runoff_voting) for the family definitions.
