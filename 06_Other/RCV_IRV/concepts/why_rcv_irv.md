# Why RCV-IRV — the case for it, made fairly

*This library advocates for STAR and Ranked Robin. That is exactly why this page exists: an argument you only ever meet through its rebuttals is an argument you have not actually understood. So here is the case for ranked-choice voting counted by instant runoff, made the way its advocates make it — with the parts that hold up, held up. The critiques are real too, and they are linked at the end rather than woven through, so the case gets a clean hearing first.*

**Level: 101 · for voters**

→ Companions: [Why STAR Voting](../../../07_Concepts/topics/Why_STAR_Voting.md) · [Why Ranked Robin](../../../05_Ranked_Robin/01_Learn/why_ranked_robin.md). The mechanics: [RCV-IRV (Hare)](RCV-IRV-Hare.md). The word itself: [Is it RCV or IRV?](RCV_or_IRV_whats_the_right_word.md).

---

## The case in eight points

### 1. It fixes the spoiler that made people angry in the first place

Choose-One's signature failure is vote-splitting: two similar candidates divide a majority between them, and the candidate most voters like *least* wins with 40%. IRV genuinely fixes that one. If your first choice finishes last, your ballot moves to your next choice — the divided coalition regroups instead of losing. That was the founding promise of the reform, and on this failure it delivers. Whatever else is true, a voter who says *"I no longer have to worry that my honest first choice hands the race to my opponent"* is describing something real. → [Is RCV-IRV just plurality in sequence?](RCV_IRV_and_plurality.md)

### 2. Your backup choice can never be used against your favorite

This is **[later-no-harm](../../../07_Concepts/topics/criteria_at_a_glance.md)**, and IRV's guarantee is exact rather than statistical: adding a 2nd, 3rd or 4th preference cannot cost your 1st choice the win, because your later ranks are not read at all while your favorite is still in the race. Of the four methods in this repo's comparison table, **IRV is the only one that passes it** — STAR, Approval and Ranked Robin all fail. If what worries you is *"will supporting a compromise candidate quietly hurt the person I actually want?"*, IRV is the method that answers "no, provably."

That is a real design achievement and it should be conceded cleanly. (It is also a *different* promise from "you never have to betray your favorite" — see the limits below, where IRV does have a problem. Later-no-harm and favorite betrayal get conflated constantly, in both directions.)

### 3. A majority that agrees gets its way

IRV passes the **majority favorite** criterion and **mutual majority**: if more than half of voters rank the same candidate first, that candidate wins; and if a majority all rank the same *group* above everyone else, the winner comes from that group. Both guaranteed. STAR and Approval pass neither — STAR can and sometimes does elect a broad-consensus candidate over a polarizing majority favorite, which STAR's advocates defend as a *feature* but which is, unmistakably, the thing IRV promises not to do. If majority rule in its strict sense is your bedrock commitment, that is a genuine point for IRV and against STAR.

### 4. Running an ally cannot sink you

**Independence of clones** ✓. Two similar candidates in the same race do not knock each other out by dividing their own support — the weaker one is eliminated and their ballots flow to the stronger. Parties and coalitions can field the candidates they want without playing traffic cop. (STAR and Ranked Robin both fail this one.)

### 5. It never elects the candidate who loses to everyone

IRV passes the **Condorcet loser** criterion and the stricter weak version: a candidate who would lose head-to-head against every single rival cannot win an IRV election. That is a floor Plurality does not clear and Approval does not clear.

### 6. The count is a story people already understand

*"If your candidate can't win, your vote goes to your next choice."* It is a runoff, held instantly, and voters already know what a runoff is. That familiarity is not a rhetorical bonus — it is a practical advantage that other methods have to earn from scratch, and a method has to be adopted before it can elect anybody. The honest caveat is that this simplicity belongs to the *ballot and the story*, not to the machinery underneath ([which half?](RCV_IRV_is_simple.md)) — but the story being tellable in one sentence is real, and reformers who skip past it are missing why IRV keeps winning the argument at city council meetings.

### 7. It is the reform that actually won

Australia has elected its House of Representatives this way since **1918** — over a century of continuous national use, with real recounts, real litigation, real ballot design. In the US: Maine and Alaska statewide, New York City, and dozens of municipalities. No other alternative single-winner method has anything close to that record. Two things follow. First, the practical questions — how you print the ballot, how you educate voters, how you certify a result — have been answered somewhere, in public, under adversarial conditions. Second, an argument that IRV is unworkable is simply refuted by the evidence; the honest critiques are about *which candidate it picks*, not about whether it functions. → [What a century in Australia actually proves](case_studies/RCV_IRV_australia.md)

### 8. And it is a real improvement on what most of us use now

The repo grades the claim *"IRV is worse than what we have now"* as flatly **false** ([the mirror table](rcv_irv_false_claims.md#the-mirror-claims-our-own-side-oversells-about-irv), where we audit our own side's overreach). Choose-One hands you one mark and no way to express a second preference at all. IRV is a substantial step up from that on the axis it targets. The argument for STAR and Ranked Robin is that we can go **further** — not that IRV was a wrong turn.

---

## Where the case runs into trouble

Stated plainly, because a page that only flattered would be worth nothing:

- **[Center squeeze](RCV_IRV_center_squeeze.md)** — the candidate acceptable to nearly everyone collects few *first* preferences, precisely because nobody had to take sides for them, and is eliminated before those preferences are ever read. Burlington 2009, Alaska 2022. This is the flagship critique, and it is the direct cost of point 2 above: the only way to guarantee later-no-harm is to refuse to read your later ranks, and consensus *is* the aggregate of those later ranks. IRV took the guarantee; STAR and Ranked Robin took the agreements. A real design fork, not a bug.
- **[Non-monotonicity](RCV_IRV_non_monotonicity.md)** — in constructed cases, ranking a candidate *higher* can make them lose.
- **[Exhausted ballots](RCV_IRV_exhausted_ballots.md)** — ballots that run out of continuing candidates leave the count, which is why an IRV "majority" is a majority of *active* ballots rather than of everyone who voted.
- **[Not summable](RCV_IRV_lack_of_summability.md)** — precincts cannot report subtotals that add up, so the count has to be central.
- **Favorite betrayal** — despite point 2, IRV *does* fail this ([the 301 page](../../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md)), and center squeeze is how. Later-no-harm protects your favorite from your *own backup*; it does not protect them from being squeezed out early.

**And keep it in proportion.** Condorcet failures turned up in **2 of 182** US RCV elections studied (Graham-Squire & McCune). The failure mode is predictable in close three-way races, not routine — overstating its frequency is the fastest way to lose a technical audience, and this repo grades *"IRV usually elects the wrong winner"* as **false**. → [Alaska 301](../../../method_comparisons/alaska_2022/alaska_301.md) keeps the rarity numbers in view throughout.

## The scoreboard cuts both ways

On [the repo's own criteria table](../../../07_Concepts/topics/criteria_at_a_glance.md), counting only the rows where the two differ: **RCV-IRV passes five criteria that STAR fails** (majority favorite, mutual majority, later-no-harm, clone independence, weak Condorcet loser), and **STAR passes two that RCV-IRV fails** (monotonicity, summability). Both fail the Condorcet winner, participation, consistency and favorite betrayal.

That is not a scoreboard STAR wins, and nobody here should pretend otherwise. What it shows is that criterion-counting was never the argument: the honest case for STAR rests on *how often and how badly* each method misfires in realistic elections, and on which failures you think matter most — not on a tally of checkmarks. Even STAR's own advocates argue against the format ("[Farewell to Pass/Fail](https://www.starvoting.org/pass_fail)"). Read the table as a catalog, not a verdict, and read [what makes a voting method good?](../../../07_Concepts/topics/what_makes_a_voting_method_good.md) alongside it.

## If it's the ranked ballot you love, you have more than one option

The strongest critiques above are about **the count**, not the paper. Ranked Robin takes the identical ranked ballot — same marks, nothing to relearn — and counts every head-to-head matchup instead of eliminating in rounds, which is why it is not center-squeezed. If you came to ranked-choice voting because ranking felt like the honest way to vote, that instinct is not what any of this challenges. → [Why Ranked Robin](../../../05_Ranked_Robin/01_Learn/why_ranked_robin.md)

---

*Same treatment for every method in the library: [STAR's honest limits](../../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [Approval's limits](../../../04_Approval/01_Learn/approval_honest_limits.md) · [Ranked Robin's limits](../../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md). And the claim-by-claim index that corrects both sides: [RCV-IRV misconceptions & false claims](rcv_irv_false_claims.md).*
