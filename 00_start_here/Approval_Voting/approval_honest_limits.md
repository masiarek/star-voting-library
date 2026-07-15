# Approval Voting — Honest Limits

**One line:** Approval is the *simplest* equal-vote method — mark everyone you approve, most approvals wins — and that simplicity is both its strength and its weakness. It throws away preference **strength and order**, and it hands the voter one hard, unavoidable decision: **where to draw the approval line.** STAR was designed largely to fix exactly this gap.

→ Overview: [**Approval Voting**](approval_voting.md) (how it works). · Companion critical pages (parity across methods): [STAR's limits](../STAR_Voting/STAR_honest_limits.md) · [Ranked Robin (RCV-RR) limits](../RCV_Ranked_Robin/RCV_RR_honest_limits.md) · [RCV-IRV fails the Equal Vote](../RCV_IRV/RCV_IRV_equal_vote.md). Approval *does* pass the [Equal Vote](../STAR_Voting/equally_weighted_vote.md). Curriculum: [301.4](../CURRICULUM.md).

---

## 1. No preference strength or order

An Approval ballot is binary per candidate: approve or not. You cannot say "I **love** A but merely **tolerate** B" — both get the same checkmark. All intensity *and* all ranking information is discarded. For voters who feel strongly about ordering their approved candidates, that expressiveness is simply gone.

## 2. The approval-threshold dilemma (the central critique)

Because the ballot is binary, the entire strategic burden collapses onto **one question: where do I draw my approval line?** Two voters with *identical* honest opinions can rationally approve different sets — one bullet-votes their favorite, the other approves their top three — and those choices can swing the result. There is no honest, obvious threshold; the method makes the voter do the strategic work that STAR's 0–5 scale and runoff absorb.

## 3. Strong incentive to bullet-vote (or over-approve)

Two opposite pressures pull on every ballot: approve **only** your favorite (so you don't help a rival you also approve), or approve **widely** (to block a worse candidate). Both are rational depending on the polls, so Approval outcomes can hinge on how strategically the electorate reads the race rather than on sincere opinion. A related wrinkle: voters whose favorite *is* a front-runner have little incentive to approve anyone else — and if that behavior is widespread, candidates already seen as "electable" gain a built-in edge.

## 4. Can miss a majority favorite (lowest-common-denominator)

A broadly **inoffensive** candidate approved by many can beat a candidate who is the *first choice of a majority* but polarizing. Sometimes that broad-consensus winner is the right call — but Approval can't distinguish "everyone's warm second choice" from "the majority's passionate first choice," because it never sees the difference. The [Approval + Top-Two](approval_top_two.md) package answers this with a second, head-to-head election between the two most-approved — and the reason it must be a *second* election (an automatic runoff from 0/1 ballots just echoes the approval count) is the cleanest demonstration of what the checkmark discards.

## 5. Fails Later-No-Harm

Approving a second choice can help that candidate beat your favorite. (STAR and Ranked Robin share this tradeoff; RCV-IRV is the one that keeps Later-No-Harm.)

## 6. A ballot-security wrinkle

Because *every* combination of marks is a valid Approval ballot, filling in **extra** bubbles on someone else's ballot is undetectable — there's no overvote to flag. (On a Choose-One ballot the same tampering voids the ballot, which is at least visible.) Poll workers should never be alone with ballots under any method, but Approval warrants extra chain-of-custody care. A known mitigation, noted on the [Equal Vote Approval page](https://www.equal.vote/approval): print an explicit **Yes / No** bubble pair per candidate, so a blank is distinguishable from a deliberate "No" — see the [ballot mockups](approval_voting.md#the-ballot) on the overview page ([double-bubble image](img/approval_ballot_yes_no_double_bubble.png)).

## Keep it in perspective

Approval's limits are the flip side of real strengths: it passes the **Equal Vote**, is trivially easy to explain and to tabulate (add the approvals; precinct-summable), and it already ends *forced* vote-splitting. STAR keeps Approval's equal-vote guarantee while adding the missing **strength + order** (a 0–5 score) and a **majority runoff** to answer the threshold dilemma — which is precisely the gap the Equal Vote Coalition set out to close when STAR was designed. Every method trades something away (Gibbard); Approval trades expressiveness for simplicity.
