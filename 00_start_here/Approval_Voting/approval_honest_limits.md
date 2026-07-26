# Approval Voting — Honest Limits

**One line:** Approval is the *simplest* equal-vote method — mark everyone you approve, most approvals wins — and that simplicity is both its strength and its weakness. It throws away preference **strength and order**, and it hands the voter one hard, unavoidable decision: **where to draw the approval line.** STAR was designed largely to fix exactly this gap.

→ Overview: [**Approval Voting**](approval_voting.md) (how it works) · the same critiques as the academic literature states them, with the parts that don't survive scrutiny marked: [Approval in the theory literature](approval_in_the_literature.md). · Companion critical pages (parity across methods): [STAR's limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md) · [Ranked Robin (RCV-RR) limits](../RCV_Ranked_Robin/RCV_RR_honest_limits.md) · [RCV-IRV fails the Equal Vote](../RCV_IRV/RCV_IRV_equal_vote.md). Approval *does* pass the [Equal Vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md). Curriculum: [301.4](../CURRICULUM.md).

---

## 1. No preference strength or order

An Approval ballot is binary per candidate: approve or not. You cannot say "I **love** A but merely **tolerate** B" — both get the same checkmark. All intensity *and* all ranking information is discarded. For voters who feel strongly about ordering their approved candidates, that expressiveness is simply gone.

## 2. The approval-threshold dilemma (the central critique)

Because the ballot is binary, the entire strategic burden collapses onto **one question: where do I draw my approval line?** Two voters with *identical* honest opinions can rationally approve different sets — one bullet-votes their favorite, the other approves their top three — and those choices can swing the result. There is no honest, obvious threshold; the method makes the voter do the strategic work that STAR's 0–5 scale and runoff absorb.

The academic literature makes this sharper than "voters find it hard." Researchers don't agree on what approving even *means* — a ranking compressed to two levels, a genuine like/dislike primitive with no hidden ranking underneath, or a ranking plus a meaningful dividing line (a "true zero"). On the middle reading there is exactly one sincere ballot per voter and no incentive to deviate; on the first, if the line has no intrinsic meaning, there is **no basis for calling any Approval ballot insincere at all**. Which is why the strategy argument never resolves: [the three views, and what each does to the strategy question](approval_in_the_literature.md#why-the-strategy-argument-never-settles).

## 3. Strong incentive to bullet-vote (or over-approve)

Two opposite pressures pull on every ballot: approve **only** your favorite (so you don't help a rival you also approve), or approve **widely** (to block a worse candidate). Both are rational depending on the polls, so Approval outcomes can hinge on how strategically the electorate reads the race rather than on sincere opinion. A related wrinkle: voters whose favorite *is* a front-runner have little incentive to approve anyone else — and if that behavior is widespread, candidates already seen as "electable" gain a built-in edge.

Two published answers to *where should the line go?*, both cited in [the theory literature page](approval_in_the_literature.md): at your **mean** utility (Duddy et al., 2013 — it maximizes the separation between the candidates you approve and those you don't), or near the utility you assign to the **expected winner** (Laslier, 2009 — the strategically best line, and roughly what voters actually do). The second one is this section's polls-dependency, stated as a finding rather than a worry.

## 4. Can miss a majority favorite (lowest-common-denominator)

A broadly **inoffensive** candidate approved by many can beat a candidate who is the *first choice of a majority* but polarizing. Sometimes that broad-consensus winner is the right call — but Approval can't distinguish "everyone's warm second choice" from "the majority's passionate first choice," because it never sees the difference. The clearest worked instance is the one the Approval camp published itself — 60% rank A first, B is approved on all 100 ballots and wins: [Hamlin & Hua §4.1, counted five ways](../../method_comparisons/approval_majority_criterion/README.md), with [the claim-check](hamlin_hua_2023.md) of their defence of it. Worked in five ballots, with the [Condorcet winner](../topics/condorcet/) of the underlying opinions lost in the compression — and the pairwise matrix showing exactly where it went: [When compression moves the Condorcet winner](../../method_comparisons/black_curtain/condorcet_compression.md). The [Approval + Top-Two](approval_top_two.md) package answers this with a second, head-to-head election between the two most-approved — and the reason it must be a *second* election (an automatic runoff from 0/1 ballots just echoes the approval count) is the cleanest demonstration of what the checkmark discards.

## 5. Fails Later-No-Harm

Approving a second choice can help that candidate beat your favorite. (STAR and Ranked Robin share this tradeoff; RCV-IRV is the one that keeps Later-No-Harm.)

## 6. A ballot-security wrinkle

Because *every* combination of marks is a valid Approval ballot, filling in **extra** bubbles on someone else's ballot is undetectable — there's no overvote to flag. (On a Choose-One ballot the same tampering voids the ballot, which is at least visible.) Poll workers should never be alone with ballots under any method, but Approval warrants extra chain-of-custody care. A known mitigation, noted on the [Equal Vote Approval page](https://www.equal.vote/approval): print an explicit **Yes / No** bubble pair per candidate, so a blank is distinguishable from a deliberate "No" — see the [ballot mockups](approval_voting.md#the-ballot) on the overview page ([double-bubble image](img/approval_ballot_yes_no_double_bubble.png)).

## Keep it in perspective

Approval's limits are the flip side of real strengths: it passes the **Equal Vote**, is trivially easy to explain and to tabulate (add the approvals; precinct-summable), and it already ends *forced* vote-splitting. STAR keeps Approval's equal-vote guarantee while adding the missing **strength + order** (a 0–5 score) and a **majority runoff** to answer the threshold dilemma — which is precisely the gap the Equal Vote Coalition set out to close when STAR was designed. Every method trades something away (Gibbard); Approval trades expressiveness for simplicity.
