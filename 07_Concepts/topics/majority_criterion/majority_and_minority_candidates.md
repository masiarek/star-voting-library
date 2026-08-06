# "Majority candidate" and "minority candidate" — five senses, and which one you're using

**Level: 201 → 301 · for debaters**

**One line:** *majority candidate* names at least five different things, *minority candidate* is nearly automatic once three people are running, and almost every argument that turns on these words is really an argument about which sense is meant.

Companion to [the Majority Criterion](README.md), which handles the *method property*. This page handles the *candidate label* — the thing people actually say out loud in a debate.

---

## The problem, as Hillinger poses it

Claude Hillinger raises it as a definitional aside and then walks past it, but it is the more useful half:

> With several candidates, it will be hard for anyone to win an arithmetic majority.

If a "minority candidate" is one elected without more than half the vote, then in any field of three or more the winner is a minority candidate **as a matter of arithmetic**, not as a matter of failure. The label describes the size of the field at least as much as it describes the winner. So the literature reaches for a repair — and its favourite repair, as Hillinger notes, is the [Condorcet winner](../condorcet/README.md): the candidate who beats every rival head-to-head. That repair has its own hole, which Condorcet knew about: the pairwise contest can cycle, and then no such candidate exists.

Neither observation settles anything, and Hillinger's own conclusion is the right one — you do not need to resolve this to see that plurality's outcomes are bad. But you *do* need to resolve it before saying "minority winner!" in an argument, because your opponent is allowed to ask which sense you meant.

## The five senses, side by side

| Sense | A candidate such that… | Always exists? | What it actually licenses you to say |
|---|---|:--:|---|
| **Absolute (arithmetic) majority** | more than half of voters mark them **first** | **No** — uncommon with 3+ real candidates | The strongest claim available. This is the subject of [the majority criterion](README.md) |
| **Mutual majority** | a majority ranks some **set** above all others; the winner should come from that set | **No** | A set, not a candidate — weaker than it sounds, and satisfied by IRV |
| **Condorcet / beats-all winner** | beats **every** rival head-to-head | **No** — [cycles](../../voting_paradoxes/condorcet_loser_paradox.md) | "A majority prefers them to *any one* rival." Pairwise, one at a time — not one coalition of over half |
| **Runoff majority** (STAR's) | preferred by more of the **decided voters** between the two finalists | **Yes**, barring a tie | Only a fact about the two finalists. This is what [STAR's automatic runoff](../../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) delivers |
| **Majority of consensus** | the smallest 50%+1 clustered where opinion actually concentrates | Only a rated ballot can see it | The sharper critique, worked at [*whose* majority is it?](README.md#a-sharper-version-of-the-objection-whose-majority-is-it) |

**The trap is that rows 1 and 3 both get called "the majority winner."** They are different candidates in general: a beats-all winner may hold no absolute majority at all, and a candidate with an absolute majority is always the beats-all winner but is answering a different question. This library treats *majority winner* as an **unsafe alias** for the Condorcet winner for exactly that reason — the full alias table is in [the naming decoder](../../../05_Ranked_Robin/01_Learn/condorcet_naming_decoder.md#the-winner-has-aliases-too-and-they-are-not-the-methods).

## What "majority" means on a score ballot

On a ranked ballot the word has one obvious reading: over half the voters put X first. On a **score** ballot even that isn't obvious, because there is no "first" — there is a number in every box. Four readings are available, and they are not equivalent:

| Reading | "X has a majority" means | The problem |
|---|---|---|
| **1. Half the scale** | X's average score is over half the maximum (above 2.5 on a 0–5 ballot) | **Several candidates can hold one at once.** It's a threshold on an average, not a majority *of* anybody |
| **2. Share of all points** | X received over half of every point awarded in the election | **Almost nobody ever does.** With three candidates X would need more points than the other two combined; the denominator grows with the field |
| **3. Majority favorite** | over half of ballots score X **strictly higher** than every other candidate | Well-defined and the right one — but need not exist, and a coarse scale produces ties at the top |
| **4. Pairwise / runoff** | over half of the voters *with a preference* rate X above Y | Always exists between two candidates (barring a tie), and says nothing about the rest of the field |

**The house answer:** this library uses **3** whenever it says *majority* about a candidate — it's the reading [the majority criterion](README.md) is stated in — and **4** whenever it says *majority* about [STAR's runoff](../../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md), where the phrase is always *"of voters with a preference"* and the [runoff-percentage line](../../../01_STAR/01_Learn/the_count/runoff_percentages.md) prints the denominator rather than leaving it to be inferred. **Readings 1 and 2 are never used**, and neither should be accepted from anyone else without a definition attached.

**Why it matters — one election, three answers.** Take [the counterfactual half of the CES case](../../../method_comparisons/ces_majority_illusion/README.md#the-one-rival-two-rivals-hinge-on-this-profile), 41 voters on a 0–5 ballot:

| | Alice | Brian | Colin |
|---|--:|--:|--:|
| average score | 2.56 | 4.24 | 2.76 |
| **reading 1** — above half the scale? | ✅ | ✅ | ✅ |
| **reading 3** — majority favorite? | ✅ (21 of 41) | ❌ | ❌ |
| **reading 4** — wins the runoff? | not a finalist | ✅ | ❌ |

Under reading 1 **all three candidates** have "an absolute majority" simultaneously. Under reading 3 only Alice does. Under reading 4 it's Brian. Same 41 ballots. This is why "did the majority winner win?" is not a question a score ballot answers until you say which majority you mean.

*(The convention question underneath — should a score result be reported against the ballot count or the total points awarded? — is settled the same way by both engines this repo uses: **ballot count**. See [reading a STAR report](../../tabulation_engines/LH_starvote/reading_a_star_report.md).)*

## Why "minority winner" is weak on its own — and what makes it strong

**The weak version.** Under [Choose-One](../plurality.md), the winner's share falls roughly as the field grows, because the ballot only ever counts one favourite per voter. The repo's [pineapple progression](../../../method_comparisons/minority_winner_progression/README.md) runs this deliberately: the same electorate, the same universally-liked compromise, and a winner who drops from **34% → 25% → 11%** as the menu grows from 3 toppings to 11. Pineapple's fan club never grew. The *menu* did.

So "elected with 34%" is, by itself, a statement about how many candidates ran. It is real — **11.9% of all 5,662 US national primaries in 2022** had multiple candidates and a sub-majority winner ([how to read that figure honestly](../../../method_comparisons/split_voting/how_often_does_vote_splitting_happen.md)) — but on its own it is not yet an indictment, and a prepared opponent will say so.

**The strong version** is not about the winner's share at all. It is about what the rest of the ballot would have said, and it comes in two grades:

- **The winner is the [Condorcet loser](../../voting_paradoxes/condorcet_loser_paradox.md)** — loses every head-to-head.
- **The winner is the [absolute loser](../../voting_paradoxes/absolute_loser_paradox.md)** — an outright majority ranks them **dead last**. This is the strongest form, and the one that needs no theory to land: most voters said *anyone but this one*, and got this one.

Seven ballots are enough to show it. Hillinger's own Table 1 — 3 voters `a > b > c`, 2 `b > c > a`, 2 `c > b > a` — elects **a** on 3 first choices while **4 of the 7 rank a last**. That profile is already in this library, and already live, as [Felsenthal Example 1 (BV2144)](../../../method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_felsenthal_ex1.md): same seven ballots, cast as Ana / Bo / Cal, where it demonstrates four plurality paradoxes at once.

## Hillinger's next move, and where this library parts from him

Having noted that the literature repairs "majority candidate" with the Condorcet winner, Hillinger argues the score-sum winner is *superior* to the Condorcet winner when the two differ. That claim is asserted rather than argued in the paper, and it is precisely the question STAR answers the other way — STAR's second round exists to re-impose a majoritarian check on the sum. It is claim-checked, with his own concessions and the places he cuts against STAR, on [Cardinal utility](../cardinal_utility.md#claim-check).

**Lean disclosure:** Hillinger is advocating his own proposal (evaluative voting) against plurality, Borda, approval and IRV. Useful for the *framing* above — the definitional problem is real and he states it cleanly — and partisan on the *verdict*.

## House usage

- **Say "majority" only for over-half.** If you mean the beats-all candidate, say **beats-all winner** or **Condorcet winner**.
- **Say which sense** when the argument turns on it. "The majority-preferred **finalist**" is STAR's runoff (one pairwise result); "the majority-preferred **candidate**" reads as over the whole field, and swapping them silently would imply STAR is Condorcet-compliant, which it is not.
- **Don't lead with the winner's percentage.** Lead with what the whole ballot says — the Condorcet loser or absolute-loser fact if you have it. The percentage is the hook, not the argument.
- **A ranked ballot's "majority" is a majority of *preference*, not of enthusiasm** — it records order, not intensity ([preference vs. support](../../scores_and_ranks/preference_vs_support.md)).

## Related

- [The Majority Criterion](README.md) — the method property, the Relaxed Majority Criterion, and the Later-No-Harm link
- ["The Majority Illusion," claim-checked](the_majority_illusion_claim_checked.md) — the Approval camp's tour of these same senses, tested · [its example, counted](../../../method_comparisons/ces_majority_illusion/README.md)
- [False majorities](../false_majorities.md) — the sixth sense, at legislature scale: over half the seats on under half the votes
- [The naming decoder](../../../05_Ranked_Robin/01_Learn/condorcet_naming_decoder.md) — the same job for *Condorcet / Copeland / round-robin / Ranked Robin*
- [Minority winner](../../../method_comparisons/minority_winner/README.md) — the canonical 34% case · [the pineapple progression](../../../method_comparisons/minority_winner_progression/README.md) — 34% → 25% → 11%
- [The absolute loser paradox](../../voting_paradoxes/absolute_loser_paradox.md) · [the Condorcet loser paradox](../../voting_paradoxes/condorcet_loser_paradox.md)
- [Cardinal utility](../cardinal_utility.md) — Hillinger claim-checked · [his example, run](../../../method_comparisons/hillinger_evaluative_voting/README.md)
- [Plurality](../plurality.md) — where minority winners come from in the first place
