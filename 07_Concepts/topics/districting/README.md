# Topic: Districting — when the lines decide, and no method can undo them

**Topic hub — a cross-method view.** Every voting method on this site answers one question: *given these ballots, who wins?* **Districting asks something no method controls** — who gets grouped with whom before any counting starts. Split one electorate into several, elect a winner in each, and the aggregate result becomes a function of **where the lines fall**, not only of how people voted.

> **The one idea to take away:** *districting is a **pre-tabulation** choice, and a better count cannot reverse it.* STAR, Ranked Robin, Approval and IRV can all be perfectly correct **inside every district** and still produce an aggregate nobody would have chosen. The failure is upstream of the tabulator, which is exactly why it survives every reform that only changes the count.

**Level: 201 → 301 · for debaters**

---

## The distinction that keeps getting muddled: districting vs. summability

These look identical — both split ballots into geographic pieces — and they are opposite questions.

| | [**Summability**](../summability/README.md) | **Districting** (this hub) |
|---|---|---|
| The question | can precinct subtotals be **added** to recover the one true winner? | each district elects **its own** winner; what does the aggregate mean? |
| The pieces are | an implementation detail — merged before anyone is elected | the actual constituencies — never merged |
| It's a property of | the **count** (STAR ✅, Ranked Robin ✅, IRV ❌) | the **architecture** — no method is immune |
| Fixed by | choosing a summable method | only by changing the districts, or [electing more than one per district](../electing_more_than_one.md) |

So "our method is summable" answers the auditing question and says **nothing** about the districting question. Keep them apart in an argument; conflating them concedes a point you didn't have to.

## Where each piece is treated

| The idea | What it says | Page |
|---|---|---|
| **The theory** | what the *architecture* costs, measured with the same instrument as [distortion](../distortion.md): counting by district has a price you can bound | [Distributed voting — the price of counting by district](../distributed_voting_distortion.md) (301) |
| **The paradox** | **reinforcement / inconsistency**: two districts each elect X, the merged electorate elects someone else. Additive rules (Score, Approval, Plurality) are immune by arithmetic; STAR, Ranked Robin and IRV are not | [The multiple-districts paradox](../../voting_paradoxes/multiple_districts.md) |
| **The cost, counted** | Ana is adored in Northside, Beto in Southside, Cleo is everybody's solid second — and **Cleo wins no district at all** while being the best choice overall | [The districting cost](../../../method_comparisons/districting_cost/README.md) |
| **The reversal, counted** | both halves pick Ada; the whole picks Cara. At ≥ 8 voters **no** Condorcet method can avoid it | [Reinforcement paradox](../../../method_comparisons/reinforcement_paradox/README.md) |
| **The elimination version** | B wins **both** districts and is *eliminated* when they merge — the IRV-specific shape of the same problem | [IRV isn't summable](../../../06_Other/RCV_IRV/concepts/RCV_IRV_lack_of_summability.md#worked-example-two-districts-both-won-by-b-merged-b-loses) · [summability demo](../../../method_comparisons/summability_demo/README.md) |
| **Seats vs. votes** | over half the seats on under half the votes — and why *"that's just gerrymandering"* is the wrong diagnosis | [False majorities](../false_majorities.md) (201) |
| **The law** | "one person, one vote" as the courts mean it **is** a districting rule (*Reynolds v. Sims*, *Wesberry*) — settled, and every method here clears it | [One person, one vote](../one_person_one_vote.md) |
| **The structural answer** | multi-member districts with proportional seats: fewer lines to draw, and far harder to draw for advantage | [Proportional STAR](../../../03_STAR_PR/01_Learn/STAR_PR/README.md) · [Electing more than one](../electing_more_than_one.md) |
| **The downstream effects** | wasted votes, packing and cracking, and the two-party equilibrium single-member lines produce | [Wasted votes](../wasted_votes.md) · [Two-party dominance](../two_party_dominance.md) |
| **Try it yourself** | a city whose two districts each run their own count, and what the merge does | [Two districts, one mayor (ex01)](../../../01_STAR/05_Practice/ex01_two_districts.md) |

## Reading it fairly

Three cautions, because this topic invites overclaiming in both directions.

**Against overclaiming *for* reform:** single-member districts are not *made* unfair by gerrymandering — the [structural distortion is there in fairly drawn lines too](../false_majorities.md), which is a stronger argument and a more honest one. But the mirror error is just as common: a better ballot does **not** fix districting, and no page here should imply it does. STAR in every district is still one winner per district.

**Against overclaiming *against* districts:** the published experiments cut both ways. On real-world preference data the measured cost of counting by district is [much smaller than the worst case](../distributed_voting_distortion.md) — real electorates are comparatively homogeneous, and homogeneity is what saves you. Quote the worst case as a worst case, per [reading these fairly](../../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md).

**And keep the vocabulary straight.** *Reinforcement* (a.k.a. consistency / join-consistency) is the criterion; the *multiple-districts paradox* is its failure; *gerrymandering* is the deliberate manipulation of where lines fall; *malapportionment* is districts of unequal population, which is the thing the law actually forbids. They are four different claims and only one of them is illegal. → [glossary](../../GLOSSARY.md)

## See also

- [Distortion](../distortion.md) — the ballot-level version of the same accounting: what does *this* design choice cost in welfare?
- [Central tabulation](../central_tabulation.md) — the operational cousin: what it costs when every ballot must physically travel
- [What makes a good winner?](../what_makes_a_good_winner.md) · [Plurality](../plurality.md)
