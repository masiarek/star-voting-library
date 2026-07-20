# Preference vs. Support — the two things a score says that a rank can't

*The single most useful idea for understanding score ballots. A **ranking** asks one question — "which do you like **more**?" A **score** asks two — "which do you like **more**?" *and* "**how much** do you like each?" The first is **preference** (order). The second is **support** (level). Ranks keep the first and throw away the second — which is exactly the information that tells a winner everyone loves apart from a winner nobody wanted.*

→ The general form of this distinction: [scores vs. ranks](scores_vs_ranks.md). This page is the vivid special case — and, near the bottom, the [three comebacks](#the-comebacks-answered) a sharp Condorcet advocate will raise, answered.

---

## The example that makes it click

Four candidates. Two ballots:

| | A | B | C | D |
|---|:--:|:--:|:--:|:--:|
| **Ballot 1** | 1 | 0 | 1 | 0 |
| **Ballot 2** | 5 | 4 | 5 | 4 |

**Same preference:** both say *A and C over B and D* (with A = C and B = D). **Opposite support:** Ballot 1 says *"none of these, really — but if you're making me choose, the odd ones"*; Ballot 2 says *"honestly, all four are fine — the odd ones by a hair."*

Now write each as a **ranking**. Both collapse to the *identical* ballot:

> **A = C  >  B = D**

The ranking **cannot tell them apart.** The reluctant voter and the enthusiastic voter are recorded as saying the exact same thing. Everything that separated *"I tolerate them"* from *"I love them"* — the **support** — is gone.

And here's the part that makes this a *clean* example, not a lucky one: **the gaps are identical too.** Every preference on both ballots is a one-point preference (A is exactly one above B on each). So the two ballots share their order **and** their pairwise margins — even a hypothetical method that read cardinal *margins* couldn't split them. The **only** thing that differs is the *level*: are these 1s-and-0s, or 5s-and-4s? That's the isolation. This example changes nothing but support, and shows that support is precisely what an order can't hold.

## The same thing, as a live election

The single-ballot version is the *idea*; here it is as a real 36-voter election you can re-run — the [**Preference vs. Support** case](../../method_comparisons/preference_vs_support/) (live on BetterVoting, [BV2225](https://bettervoting.com/ywx39y/results) / [BV2226](https://bettervoting.com/82gg36/results)). Two elections with **byte-identical rankings** — the only change is how hard the two wings score the centrist **Blair**: a grudging **1**, or a genuine **4**.

| Method | Reads… | Blair scored **1** (tolerated) | Blair scored **4** (supported) | Moved? |
|---|---|:--:|:--:|:--:|
| **RCV-IRV** | order only | Alex | Alex | ❌ can't |
| **Ranked Robin** | order only | Blair | Blair | ❌ can't |
| **STAR** | order **+ support** | **Alex** | **Blair** | ✅ **only method that responds** |

Because the *rankings* never change, IRV and Ranked Robin return byte-identical results in both — they cannot tell a tolerated centrist from a beloved one. STAR reads the support, so it alone moves. That's this whole page, as ballots: same preference, different support, and only the score-ballot method can see it.

## The two questions, named

- **Preference** — *which* do you like more? A **relative / order** question: "A over B." Every ballot format captures at least a slice of it — choose-one only your favorite, approval a two-level cut, ranks and scores the full order.
- **Support** — *how much* do you like each one, on its own? An **independent / level** question: each candidate is judged against the scale, not against the others ("A is a 5"). Only a rated ballot answers it — approval's yes/no is the crude two-level case; letter-grade ballots (Majority Judgment) are another.

A score is preference **and** support in a single mark. A rank keeps only the order. To be strict about it: a rank drops *two* cardinal things — the **level** of each candidate (support) *and* the **size of the gaps** between adjacent choices (A ≫ B vs. A > B-by-a-hair). This page is about the level; just know the gaps go too.

> **A note on the word.** The election-methods literature usually calls this *preference intensity*, *cardinal preference*, or a *grade*. This library says **support** because that's what the mark means politically — how much you actually back the candidate. (It's also why STAR's runoff "no-preference" bucket is named [**Equal Support**](../GLOSSARY.md): scoring two finalists the same.)

## The race analogy

A ranking is a race that records only the **finishing order** — not the **times**, and not whether anyone actually ran fast. A photo finish between two world-record sprinters and a photo finish between two people crawling backwards produce the *same order column*: "1st, 2nd." A track scout handed only "finished 1st" would demand the clock before signing anyone — but a ranked ballot certifies the win without ever asking. **Scores keep the clock.**

*(One honest seam, since a debate opponent will pull it: a stopwatch is objective, and a voter's 0–5 is self-reported. The analogy shows what ranks **discard**, not that scores measure the clock perfectly — that cost is the [last section](#the-honest-cost-of-support).)*

## Why it matters

1. **A mandate vs. a resignation.** A candidate can win by *preference* while having almost no *support* — the "least-bad" pick of a field nobody liked. Ranks can't tell "won a race everyone wanted" from "won a race everyone wanted to leave." Scores can: the [scoring round](../STAR_Voting/the_count/STAR_Scoring_Round.md) shows a winner averaging 4.5/5 versus 1.2/5 — same order, very different mandates.
2. **Protest and honest indifference.** A score ballot lets you say *"I have a slight preference but I support none of you"* (`1,0,1,0`) — or *"I'm happy with the whole field"* (`5,4,5,4`). A ranking read as pure order gives you at most one crude support signal — rank vs. don't-rank — and nothing finer: it can't distinguish *"my grudging best"* from *"my genuine favorite."*
3. **Consensus vs. compromise.** Support is how you tell a broadly-loved [consensus winner](../topics/what_makes_a_good_winner.md) from a barely-tolerated compromise — *even when they share the same preference order.*
4. **STAR uses both, on purpose.** [STAR](../STAR_Voting/STAR_start_here.md) reads **support** to pick the two finalists (the scoring round) and **preference** to choose between them (the [automatic runoff](../STAR_Voting/the_count/STAR_Automatic_Runoff.md)). Drop the support half and you're back to a ranked method that can't tell the sprinters from the crawlers. (And yes — the runoff deliberately blinds itself to support again, reverting to pure preference between the two finalists. By then support has done its one job: choosing *who* is in the runoff.)

## The comebacks, answered

The example wins against a newcomer instantly. A prepared Condorcet advocate will knock on exactly three doors — so here they are, opened first. (In a debate, the side that concedes *first and precisely* keeps the frame.)

**1. "Allow equal ranks and the ballot already shows `A = C > B = D` — so what's lost?"** That collapsed ballot is *already the most expressive ranked format there is* — a weak order with ties, exactly what [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) accepts. The loss has nothing to do with whether ties are allowed. **No ordinal format, however permissive, records magnitude** — a [weak-ranked](weak_ranks.md) second choice "could be as good as your favorite or almost as bad as your last choice," and the ballot can't say which. Permissiveness buys you ties, not levels.

**2. "With truncation, the reluctant voter ranks A = C and leaves B, D unranked; the enthusiast ranks all four — different ballots, so the rank *did* tell them apart."** True — truncation is a **real support signal, but a one-bit one**: ranked-vs-unranked is a crude personal approval line ("above my threshold"). It's ambiguous (unranked can mean *"unknown"* as much as *"unsupported"*), most tabulations read unranked as simply tied-last (restoring the collapse), and — decisively — it still can't say whether the *ranked* candidates are loved or merely tolerated. Ballot 2's voter backs B and D at a solid 4/5; no truncation choice can record that. One crude bit is not the level.

**3. "Voters will min/max, so support is fiction anyway."** The sharpest one, and worth owning: strategically flatten Ballot 1 (`1,0,1,0`) to `5,0,5,0` — and flatten Ballot 2 (`5,4,5,4`) to **the identical `5,0,5,0`.** Under full strategic voting the reluctant and the enthusiastic voter cast the *same* ballot; support is exactly the information strategy erases. Two honest answers: (i) real rated elections show most voters **don't** flatten — intermediate scores are used heavily; and (ii) **STAR specifically penalizes flattening** — score your two favorites both 5 and you forfeit your vote between them in the runoff — so STAR's strategic optimum sits much closer to sincere than pure Score's does ([strategic voting](../topics/strategic_voting.md), [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md)).

## The honest cost of support

Support isn't free, and this library doesn't pretend it is. Reading *level* means trusting voters to use the scale sincerely, and it leans on a **shared scale** — 0–5 with plain verbal anchors ("great … terrible") is a common language of grades, the same social technology as letter grades and star reviews (Balinski & Laraki's case for grading). Comparing one person's "5" to another's is a real assumption.

But notice the trade, because this is where the debate actually sits: **pure preference isn't assumption-free either.** Majority rule makes its own normative call — that every voter's preference counts *equally, however faint*: a razor-thin "prefer" outweighs another voter's passionate one. That's the [utilitarian-vs-majoritarian](../topics/what_makes_a_good_winner.md) choice, and the [one-person-one-vote](../topics/one_person_one_vote.md) question ("why should intensity override a majority?") is answered squarely by STAR's design: every ballot carries the *same maximum influence* (giving less than full support is the voter's own choice — [the equally weighted vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md)), and the **majoritarian runoff is exactly the check** that keeps raw intensity from overriding a genuine majority. Support to find the finalists; preference to confirm the winner. That's the [cardinal-vs-ordinal tradeoff](../topics/arrow_theorem_and_star.md) — made, not dodged.

## Related

- [Scores vs. ranks](scores_vs_ranks.md) — the general form of this distinction (relative vs. absolute)
- [Weak ranks](weak_ranks.md) — even a ranking *with ties* records order only, never level
- [The score ballot](score_ballot.md) · [the fidelity ladder](fidelity_ladder.md) — a score carries both; converting *down* to a rank loses the support, converting *up* has to fabricate it
- [What makes a good winner?](../topics/what_makes_a_good_winner.md) — the utilitarian (**support**) vs. majoritarian (**preference**) ideals, and why they can disagree
- [One person, one vote](../topics/one_person_one_vote.md) — the legal standard vs. the reformer's "test of balance," and why weighing support doesn't break it
- [The equally weighted vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md) — equal *scores* say "preference: none — support: whatever level you gave both" (5/5 full, 0/0 none: the glossary's Equal Support / Equal Opposition pair)
- Glossary: [`score ballot`](../GLOSSARY.md)
