# Choosing Among the Equal Vote Methods — STAR, Approval, Ranked Robin

The [Equal Vote Coalition](https://www.equal.vote) endorses three single-winner methods, and this repo teaches all three: **[STAR](STAR_Voting/STAR_start_here.md)** (score, then automatic runoff), **[Approval](Approval_Voting/approval_voting.md)** (mark the ones you like, most marks win), and **[Ranked Robin](RCV_Ranked_Robin/ranked_robin.md)** (rank them, most head-to-head wins). All three clear the low bar that matters most — they end the [spoiler effect](spoiler_effect.md) and the [choose-one](plurality.md) status quo, and they let you support a favorite without betraying them the way [RCV-IRV](rcv_irv_vs_star.md) can.

This page is **not** "which one is best." That answer depends on what you weigh, and reasonable people land differently. It's a map of the **tradeoffs** — where each method genuinely shines, and what each gives up — so you can choose with eyes open. It aims to be even-handed to all three; each has a companion *honest-limits* page, linked throughout.

## The tradeoff triangle

Think of the three as points on a triangle, trading three things off against each other — **simplicity**, **expressiveness**, and **decisiveness/precision**:

- **Approval** — the *simplest*. A yes/no ballot, the lowest cognitive load, the easiest count. The price: it captures the least — no order, no strength, just "acceptable or not."
- **Ranked Robin** — the most *analytically precise*. It elects the [Condorcet winner](STAR_Voting/STAR_three_winner_notions.md) (the candidate who beats every other head-to-head) whenever one exists — the sharpest, least "squishy" definition of a winner. The price: ranking a full field is the heaviest ballot, the pairwise count is the hardest to explain, and it ignores *how much* you prefer one candidate over another.
- **STAR** — the *middle path*. More expressive than Approval (it keeps order **and** strength), far easier to explain than Ranked Robin (add the stars, top two advance, the majority-preferred finalist wins). The price: it is **not** guaranteed to elect the Condorcet winner, and like the other two it gives up Later-No-Harm.

No method dominates the triangle. Picking one is picking which corner you're willing to move away from.

## At a glance

| | Approval | Ranked Robin | STAR |
|---|---|---|---|
| Ballot | approve (0/1) | rank order | score 0–5 |
| Cognitive load | **lowest** | highest (rank the field) | low–moderate |
| Captures preference *order* | no | yes | yes |
| Captures preference *strength* | no | no | **yes** |
| Ease of explaining the **count** | very easy | **hardest** (pairwise grid) | easy (stars → top 2 → majority) |
| Elects the Condorcet winner? | not guaranteed | **yes, when one exists** | usually, not guaranteed |
| Later-No-Harm | fails | fails | fails |
| Main strategic worry | where to set your approval line | burial (insincere ranking) | exaggeration / normalization — but the runoff visibly punishes it |

Every method in that table fails Later-No-Harm — so "it fails LNH" isn't a reason to pick one over another *within* this set.

## The case for each

### STAR — the balance

Four arguments recur, and they are strongest as reasons to prefer STAR over **Ranked Robin** (they are weaker against Approval, which wins on raw simplicity):

1. **Explainability protects the system.** A method the public can understand *and verify for themselves* is more legitimate and more durable. STAR's count is easy to narrate; Ranked Robin's pairwise matrix is not. (Approval is easier still — this argument places STAR *ahead of Ranked Robin*, not ahead of Approval.)
2. **Intensity can matter more than bare pairwise dominance.** STAR's sharpest disagreement with Ranked Robin is the rare case where a [Condorcet winner exists but STAR elects someone else](../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md): a candidate who beats everyone head-to-head, but only as a broadly-liked *lukewarm* second choice with little strong support. STAR weighs **strength and breadth of support**, not just the direction of preference — so it can prefer a candidate with deep, wide support over a milquetoast pairwise winner. Whether that's *right* is a genuine values question (Ranked Robin advocates consider the Condorcet winner the correct answer by definition), and it's the "squishiest" of these arguments — but it's a real, principled difference, not a bug.
3. **The honesty story is the most legible.** All three EVC methods are fairly strategy-resistant, but STAR makes the *reason honesty pays* unusually easy to show: exaggerate, and the runoff can hand the win to a candidate you like less. (This is "easiest to explain," not "uniquely strategy-proof" — a [brute-force simulation](STAR_Voting/favorite_betrayal_voting_301.md) finds burying rarely helps in STAR, but the method still isn't favorite-betrayal-proof.)
4. **Scoring is lighter than ranking.** A 0–5 score is less cognitive work than force-ranking a full field — a real advantage over Ranked Robin. (Approval's yes/no is lighter still.)

**What STAR gives up:** it is not Condorcet-compliant, it fails Later-No-Harm by design, and it has rare residual vote-splitting. Full list: [STAR's honest limits](STAR_Voting/STAR_honest_limits.md).

### Approval — the simplicity

Approval's case is the mirror image of STAR's #1 and #4: it is **the simplest method that fixes the spoiler effect.** One binary mark per candidate, the lowest possible cognitive load, an instantly auditable count, and precinct-summable. For a low-stakes poll, a first rollout, or an audience with zero appetite for voting theory, "simplest thing that works" is a strong argument.

**What Approval gives up:** it captures neither order nor strength (a 5-star favorite and a barely-acceptable candidate get the same mark), it forces the awkward **approval-threshold** decision on every voter, it can elect a lowest-common-denominator winner over a majority favorite, and it too fails Later-No-Harm. Full list: [Approval's honest limits](Approval_Voting/approval_honest_limits.md).

### Ranked Robin — the precision

Ranked Robin's case is the one STAR's #2 argues *against*, and it's a serious one: when a **Condorcet winner exists, Ranked Robin elects it** — the candidate a majority prefers over every single rival, one-on-one. That is the least arbitrary, most defensible definition of "the people's choice," and it needs no talk of scores or intensity. If you believe pairwise majority rule is the gold standard, Ranked Robin delivers it directly.

**What Ranked Robin gives up:** when there's **no** Condorcet winner (a [cycle](RCV_Ranked_Robin/ranked_robin.md)), it needs a tiebreak and the "clear winner" evaporates; it ignores preference strength (the "milquetoast winner" critique STAR presses); its count is the hardest of the three to explain to a newcomer; and it also fails Later-No-Harm. Full list: [Ranked Robin's honest limits](RCV_Ranked_Robin/RCV_RR_honest_limits.md).

## A practitioner's perspective

*The section above is deliberately neutral. What follows is one advocate's reasoned view — offered as testimony, not as the repo's verdict.*

> I used to be a Ranked Robin / Condorcet advocate — it has the sharpest "ideal winner" and the least squishy criteria, and I figured we should use the best method available whether or not everyone follows it. *"Precision beats communication,"* I'd say. I've come around. With democracy itself feeling fragile, I now have a deeper appreciation for how much *ease of explanation protects the system* — it's better to include people both in the process **and** in the understanding of it. And on the one edge case where STAR and Condorcet part ways, I've found I actually side with STAR: if a candidate has intense support from a bare majority but is so weakly regarded by nearly half the electorate that two others out-score them overall, that polarization is a red flag — I'd want my method to weigh breadth and strength of support, not just pairwise dominance. It feels squishier, because we're trained to think in terms of one thing beating another — but I think it's right.

That view is contestable — a committed Condorcet advocate would answer that a candidate who beats everyone head-to-head *is* the majority's choice, intensity notwithstanding — and that disagreement is exactly the values question this page leaves open.

## The bottom line

- Want the **simplest** thing that ends vote-splitting? **Approval.**
- Want the method that most directly elects the **head-to-head majority winner**? **Ranked Robin.**
- Want the **balance** — expressive, explainable, and attentive to how *strongly* people feel? **STAR.**

All three beat the status quo, and the honest differences between them are tradeoffs, not knockouts. Read each method's honest-limits page alongside its case, and decide which corner of the triangle fits your election.

**See also:** [STAR FAQ (mechanics, with worked examples)](STAR_Voting/STAR_FAQ.md) · [RCV-IRV vs. STAR](rcv_irv_vs_star.md) · [Three notions of "winner"](STAR_Voting/STAR_three_winner_notions.md) · [Curriculum](CURRICULUM.md) · [Glossary](GLOSSARY.md)
