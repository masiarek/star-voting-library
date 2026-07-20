# "One person, one vote" — the legal principle, and the reformer's stronger claim

*Two different ideas wear the same four words, and conflating them causes half the arguments about voting methods. **One is settled constitutional law; the other is a method-design criterion.** This page keeps them apart — because "RCV upholds one person, one vote" and "RCV fails the equal vote" can *both* be true, and are.*

→ Companions: [The Equally Weighted Vote (Test of Balance)](../STAR_Voting/properties_and_limits/equally_weighted_vote.md) · [RCV-IRV fails the Equal Vote](../RCV_IRV/RCV_IRV_equal_vote.md) · [exhausted ballots](../RCV_IRV/RCV_IRV_exhausted_ballots.md). Glossary: [`equally weighted vote`](../GLOSSARY.md).

---

## Sense 1 — the legal principle (settled, and every method passes it)

"One person, one vote" is a **constitutional apportionment rule** from the 1960s reapportionment cases. The Supreme Court coined the phrase in *Gray v. Sanders* (1963) and applied it in *Wesberry v. Sanders* (1964, congressional districts) and *Reynolds v. Sims* (1964, state legislatures): the **weight of each citizen's vote must, as nearly as practicable, be equal** — no one's vote may be *diluted* by living in an over-populated district.

Crucially, this is about **districting and vote-counting equality**, not about *which tabulation method* you use. A method satisfies it when every voter casts one ballot and every ballot is counted on equal terms. By that bar, **Choose-One, RCV-IRV, and STAR all pass** — and courts have specifically **upheld RCV-IRV** against one-person-one-vote challenges (the "exhausted ballots disenfranchise voters" argument has lost in court). So if the question is *"is this voting method legal / constitutional?"*, the answer for all of them is yes.

## Sense 2 — the reformer's "equally weighted vote" (a stronger, different bar)

Voting-reform advocates — especially the [Equal Vote Coalition](https://equal.vote) — use the same phrase for a **stronger, mathematical** idea: the [**Equal Vote / cancellation criterion**, the "Test of Balance."](../STAR_Voting/properties_and_limits/equally_weighted_vote.md) It asks: *for any ballot one voter casts, can another voter cast an exact-opposite ballot so the two together change nothing?* If yes, no voter's ballot can outweigh another's.

This is a **property of the tabulation**, not a legal standard — and the methods split on it:

| | Legal OPOV (Sense 1) | Test of Balance (Sense 2) |
|---|:--:|:--:|
| Choose-One (Plurality) | ✅ passes | ❌ fails (a mark can only *add*, never cancel) |
| RCV-IRV | ✅ passes | ❌ fails ([opposite ballots don't cancel under sequential elimination](../RCV_IRV/RCV_IRV_equal_vote.md)) |
| Ranked Robin (Condorcet) | ✅ passes | ✅ passes (opposites cancel in the pairwise matrix) |
| Score / STAR / Approval | ✅ passes | ✅ passes (opposite scores cancel in the sum) |

Note what that table shows: the balance failure is **not** "ranked ballots are worse than scored ones" — Ranked Robin is ranked and passes. It's specific to methods whose count is a **sequential elimination** (or a single mark), where only the top of each ballot drives the result. See the worked, runnable example: [balanced ballots flip the RCV-IRV winner](../RCV_IRV/RCV_IRV_equal_vote.md).

## Why the two get tangled — and how to keep them straight

The confusion runs both directions:

- **Reform critics** hear that RCV-IRV "fails one person, one vote" and picture *illegal* — some voters literally getting extra ballots. That's not the claim; RCV-IRV is legal and every voter casts one ballot. The reformer claim is about *whose later preferences get counted once elimination starts* — a **design** shortfall, not a **legal** one.
- **Reform defenders** (e.g. FairVote's essay, ["Enhancing Voter Equality"](https://fairvote.org/how_ranked_choice_voting_survives_the_one_person_one_vote_challenge/)) answer the *legal* charge — and win it — but that defends RCV-IRV against **Choose-One**, not against the **Test of Balance**. Both can be true at once: RCV-IRV upholds the constitutional standard *and* fails the balance criterion.

## The honest caveats (stated out loud)

- **The balance criterion isn't neutral.** It's promoted mainly by cardinal-method advocates, and cardinal methods pass it essentially by construction; even its formalizer notes it may not fully capture the informal intent. So "RCV-IRV fails *our* criterion" carries method-favoring flavor — it's largely the [spoiler](spoiler_effect.md) / [center-squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) critique in equal-vote language, not a wholly separate defect. (Ranked Robin passing it is the reminder that it isn't a scores-only trophy.)
- **The legal principle is genuinely settled** and shouldn't be waved away either. "One person, one vote" as the courts mean it is a real, hard-won standard; every reform on this site clears it.

So the precise sentence is: **all these methods give one person one vote in the legal sense; they differ on whether every voter's vote carries equal *weight through the count*, which is the reformers' bar — and there, Choose-One and RCV-IRV fall short while Score, STAR, Approval, and Ranked Robin hold up.**

## Sources

- *Gray v. Sanders* (1963), *Wesberry v. Sanders* (1964), *Reynolds v. Sims* (1964) — the reapportionment cases that established the legal principle.
- FairVote, ["How ranked choice voting survives the one-person-one-vote challenge"](https://fairvote.org/how_ranked_choice_voting_survives_the_one_person_one_vote_challenge/) — the RCV-IRV legal defense.
- Equal Vote Coalition — the [equally weighted vote / Test of Balance](../STAR_Voting/properties_and_limits/equally_weighted_vote.md) (after Mark Frohnmayer).
