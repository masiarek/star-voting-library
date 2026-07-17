# Claim check — "ordered majority rule" and the argument that Condorcet, IIA, and monotonicity aren't desirable

*A worked example of reading advocacy-adjacent theory critically. The arXiv paper [A Majority Rule Philosophy for Instant Runoff Voting](https://arxiv.org/abs/2308.08430) (2023; one of its authors is affiliated with [FairVote](../advocacy_organizations.md), so read it as a defense of RCV-IRV, not a neutral survey) makes an unusually sophisticated pro-IRV argument: it defines a new property — **ordered majority rule** — claims IRV uniquely satisfies it, and concludes that because that property is incompatible with the [Condorcet criterion](README.md), [independence of irrelevant alternatives](../../GLOSSARY.md), and [monotonicity](../monotonicity/), those three properties are "not desirable." This page states the argument fairly, separates its one honest point from its sleight of hand, and checks the load-bearing claim against a countable election. The critique here isn't original — it distills the sharp responses the paper drew on [votingtheory.org](https://votingtheory.org/forum/post/2850) from cfrank, Toby Pereira, and Jack Waugh.*

**Why this page exists.** This is the *strongest* version of the "Condorcet doesn't matter" argument a STAR audience will meet — dressed in a theorem rather than an op-ed (compare the [FairVote op-ed claim-check](fairvote_condorcet_claim_check.md) and [Edelman's "Myth of the Condorcet Winner"](edelman_condorcet_myth.md)). It's worth learning to answer precisely, because the refutation is clean and reusable.

## The paper's argument, in one paragraph

*Ordered majority rule* (the paper's own term): the relative social order between any two candidates X and Y is determined **only by ballots from voters who do not prefer another "major" candidate**, ignoring all "minor" candidates — where major vs. minor is itself "self-consistently determined by the social order created by the voting method." The paper argues IRV is the unique method satisfying this, that Condorcet / IIA / monotonicity all demand the *opposite* (that voters who prefer some third candidate should still get a say in the X-vs-Y ranking), and therefore concludes those criteria are undesirable "for situations where allowing supporters of a major candidate to have influence over the relative social ranking between other major candidates is deemed inappropriate."

## The tell: a mechanism dressed as a principle

**"Ordered majority rule" is not an independent standard IRV happens to meet — it is IRV's elimination algorithm restated as a virtue.** cfrank put the finger on it: the social order is defined by the major/minor split, and the major/minor split is defined by the social order. That is circular by construction. When a criterion's definition *is* the method, "IRV is the **only** method that satisfies it" carries **no normative weight** — you have drawn the target around where the arrow already landed. (cfrank also notes the paper asserts the uniqueness rather than proving it, and that the property is never fully defined outside the context of IRV.)

This is the single most transferable lesson here, good far beyond this paper: **when someone claims "method X uniquely satisfies criterion Y," check whether Y was reverse-engineered from X.** If it was, the "uniqueness" is a magic trick, not evidence.

## Is the property even desirable? (the values fork the paper hides)

Strip away the circularity and a genuine values question remains — and it's the opposite of settled. Ordered majority rule says: *when deciding between the two frontrunners A and B, only voters who don't prefer some other major candidate should count.* Toby Pereira's objection is the majority view, and I think the correct one:

> "If there are two candidates who might win — A and B — why should only people who like A and B get any say in who is elected? Someone might dislike them both, but still much prefer one to the other. I see this as a bad criterion."

The paper treats *"ignore those voters"* as a feature. Most people's intuition — and STAR's whole design — treats *capturing* them as the point.

## The countable check: the opposition decides the A-vs-B race

The paper's plain-English summary promises that ordered majority rule "ensures the election of a candidate from the majority coalition while **preventing opposition voters from influencing the choice of candidate from the faction they oppose**." Toby's counterexample shows the sentence failing on its own terms. Three candidates, 100 voters, C a third bloc that ranks both frontrunners last ([`omr_opposition_decides.yaml`](../../../method_comparisons/ordered_majority_rule/omr_opposition_decides.yaml)):

```
35 × A > B > C
33 × B > A > C
32 × C > B > A
```

A leads on first choices (35 to B's 33). Under IRV, C is eliminated and **its second preferences hand the A-vs-B contest to B, 65–35**:

```
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                 35  Hopeful
B                 33  Hopeful
C                 32  Rejected

FINAL RESULT
B                 65  Elected
A                 35  Rejected
```

The 32 opposition voters — who rank *both* A and B dead last — are exactly who decided that B, not A, is "the majority coalition's candidate." So much for "preventing opposition voters from influencing the choice."

**Be precise about what this does and doesn't show.** B is *also* the Condorcet winner here (B beats A 65–35 and C 68–32), so IRV isn't misfiring on the *outcome* — this is not a [center squeeze](../center_squeeze/). The point is narrower and entirely about the sales pitch: the marketing sentence is false, while the *technical* criterion wriggles free only because it reclassifies the C-voters as "minor" and therefore not "opposition" — which is the circularity again. The English claim and the formal claim are two different animals, and the paper leans on the persuasive English one.

```
Win–loss record — Copeland score:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          2–0–0         2     +66  A, C
    2  A          1–1–0         1      +6  C
    3  C          0–2–0         0     -72  —

Winner — Ranked Robin (RCV-RR): B — the Condorcet winner.
```

Full engine detail: [`_tabulated` mirror](../../../method_comparisons/ordered_majority_rule/ordered_majority_rule_tabulated/omr_opposition_decides_tabulated.txt).

## STAR's answer to the honest core

The paper's defensible instinct is real: a voter's *support vs. opposition* matters, and pure rankings don't record it. But that instinct argues **against** the paper's own method, and Jack Waugh said it plainly on the thread: *ranked ballots don't tell us whether voters support or oppose a candidate — rating ballots would.* That's the [cardinal critique of ordinal methods](../scoring-methods-vs-ranked-voting.md), and RCV-IRV is exactly as ordinal and intensity-blind as any Condorcet method. STAR's score ballot lets the both-dislikers say *how much* they prefer one frontrunner over the other — so their real preference counts, without letting a weak preference override a strong one. "Only frontrunner-supporters get a say between the frontrunners" is a bug that score ballots fix, not a principle to enshrine.

## The precision nit: Arrow is ordinal-only

Jack Waugh's other point is correct and worth keeping straight: the paper leans on impossibility results as if they condemn *all* voting systems, but **Arrow's theorem applies only to ranked (ordinal) systems.** Cardinal systems — Score, Approval, STAR — sidestep Arrow entirely (Gibbard's strategy theorem still bites, but that is a *different* claim about manipulability, not about IIA). Overstating Arrow's scope is the kind of impossibility-theorem sloppiness this repo flags for the rigor tier — see [the math behind Condorcet](../../RCV_Ranked_Robin/the_math_behind_condorcet.md).

## Net assessment

The paper's honest core — *ranked ballots don't capture intensity, so majority-pairwise order isn't the only defensible standard* — is true, and this repo agrees with it (the [majoritarian/utilitarian split](../what_makes_a_good_winner.md), [STAR's honest limits](../../STAR_Voting/properties_and_limits/STAR_honest_limits.md)). But that core is an argument for **cardinal** ballots, not for RCV-IRV. What's wrapped around it is a criterion defined circularly to fit IRV, a uniqueness claim asserted rather than proved, a plain-English selling point its own examples contradict, and an overstatement of Arrow's reach. "IRV uniquely satisfies the property we built to describe IRV" is not a defense of IRV — it's a mirror. Read theory papers, from every camp, with the ballots in hand.

Related: [Condorcet topic hub](README.md) · [FairVote claim check](fairvote_condorcet_claim_check.md) · [Edelman's Condorcet myth](edelman_condorcet_myth.md) · [Center squeeze](../center_squeeze/) · [Favorite betrayal (301)](../../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) · [Scoring methods vs ranked](../scoring-methods-vs-ranked-voting.md) · [What makes a "good" winner?](../what_makes_a_good_winner.md) · [Advocacy organizations](../advocacy_organizations.md)

# file: ordered_majority_rule_irv.md
