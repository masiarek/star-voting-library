# What "proportional" actually means

**One line:** exact proportionality has one unambiguous definition and almost no real election meets it, so every proportional method is really a set of *criteria and metrics* for how closely it comes — and once there are no parties to count, even deciding what to be proportional *to* becomes a choice.

→ the method this folder teaches: [STAR-PR](STAR_PR/README.md) · the formulas underneath: [the math behind proportional STAR](STAR_PR/the_math_behind_proportional_star.md) · the majoritarian alternative: [Bloc STAR](../../02_STAR_Bloc/README.md)

**Level: 201 → 301 · deep dive**

---

## The definition, and why it almost never applies

[Wikipedia](https://en.wikipedia.org/wiki/Proportional_representation) puts the strict version plainly: a seat allocation is proportional **only** if seat shares equal vote shares, and is otherwise disproportional.

That is the only version of the word with a single meaning. It also describes a situation that barely occurs. It requires factions that are perfectly cohesive — every member voting the same way — *and* perfectly sized to the seats available. Three seats and three factions of exactly one third each: proportional. Almost anything else: some remainder has to go somewhere.

So in practice "proportional" names a **family of methods judged by criteria**, not a property an election either has or lacks. Labels like *proportional*, *semi-proportional* and *proportionate* get attached to systems fairly loosely; what actually distinguishes them is which pass/fail criteria they meet and how they score on continuous metrics.

## Quotas: the unit of "one seat's worth"

When factions don't divide evenly, a **quota** formula decides who gets the leftover seat. Two are standard:

- **Hare quota** = votes ÷ seats. With three winners, roughly ⅓ of voters.
- **Droop quota** = ⌊votes ÷ (seats + 1)⌋ + 1. With three winners, roughly ¼.

The trade-off between them is the usual one: **Hare favors smaller factions; Droop is more resistant to strategic voting.** Formulas, apportionment theory, and the JR → PJR → EJR guarantee hierarchy are all one level down, in [the math behind proportional STAR](STAR_PR/the_math_behind_proportional_star.md).

The corresponding pass/fail test is the **Hare Quota Criterion**: if any faction holding a quota's worth of voters can *always* win a seat by voting as a bloc, the method passes.

**A quota is a guarantee, not a price.** It states what a faction can force; it does not state what a seat costs. Because some factions are larger than they need to be, they leave fewer voters behind them for the remaining seats — so candidates can and often do win on **less** than a full quota. If not enough candidates clear the threshold, the last seat still has to go to somebody.

## The part that gets harder without parties

Party-list PR is the easy case to reason about: a quarter of the voters back a party, that party takes a quarter of the seats. Much of Europe runs some version of it.

The STAR-PR project deliberately doesn't. Equal Vote's stated reasoning — and this is an advocacy source, so read it as their argument rather than a neutral finding — is that **closed** lists, where voters choose a party rather than candidates, tend to increase partisanship and polarization and to advantage party insiders over grassroots candidates; that nearly half the US electorate registers with no party at all, making a party-shaped ballot a poor fit; and that while **open** lists fix some of this, an expressive score ballot makes them unnecessary. Their committee therefore didn't consider party-list proposals.

That choice has a cost, and it is the honest centerpiece of this page: **with no parties, there is no longer an obvious thing to be proportional to.** Proportional to what — party affiliation? geography? demographics? positions on specific issues? The answer depends on what the voters themselves care about and on what actually separates the factions in that particular election. Non-partisan proportionality is real, but it is proportionality to *revealed voter preference* rather than to any pre-declared category.

This is where a 0–5 ballot does specific work. A choose-one ballot records only which faction a voter belongs to. A score ballot records **which candidates a voter feels represented by and to what degree** — including partial and overlapping representation, which is what real factions look like: they overlap, they are fuzzy at the edges, and voters belong to several at once.

## More seats, lower threshold — and the limits of that

The threshold to win falls as seats rise, and expected proportionality rises with it. That relationship is real, and it is also the argument's own limit:

- **Very low thresholds let highly polarizing candidates in.** With ten winners the threshold is around a tenth, so a candidate strongly opposed by 90% of voters can still take a seat. Proportionality is indifferent to how much the other 90% dislike them — that is what makes it proportional.
- **Very large bodies trade away accountability**, and depending on how districts are drawn, local and geographic representation with it.

There is no setting that maximizes everything. District magnitude is a genuine design choice with losses on both sides.

## What proportionality does not promise

Worth stating before advocating for any of this, because the claim is easy to overreach:

Proportional methods have been shown to increase **descriptive representation** — bodies elected proportionally tend to be more diverse than those elected at large. But a non-partisan proportional method **cannot guarantee proportionality of any single characteristic**. It does not promise that a group forming a fifth of the electorate wins a fifth of the seats along whichever axis an advocate happens to name. What it guarantees is about *cohesive groups of voters* getting representation, and voters are not perfectly cohesive along any one line.

Promising more than that is the fastest way to lose the argument in front of an audience that will check.

## Proportionality picks the quadrant, not the candidate

The sharpest way to see the limit. Put the candidates in a two-dimensional political space — four quadrants, an even spread of voters — and hold a four-winner race. **Every** proportional method elects one candidate from each quadrant; that is what makes them proportional, and on that question they agree.

They do not agree on *which* candidate from each quadrant, and proportionality has nothing to say about it. Because candidates also vary along an axis that has nothing to do with their politics: how **consensus** or how **polarizing** they are. Each quadrant contains a candidate almost everyone finds tolerable, a broadly representative one, and one adored by their own corner and detested outside it. All three are equally "proportional" choices.

So there is a second frontier underneath the first — consensus winners at one end, polarized winners at the other, representative-but-diversified in between — and choosing along it is a design decision, not a proportionality decision. Equal Vote's stated target is a winner set as diversified and representative as possible **without being needlessly polarizing**, which is the argument for a method that also knows how *strongly* voters feel rather than only which faction they belong to.

It also explains the earlier warnings without contradiction: a very low threshold raises measured proportionality while pushing the winner set toward the polarized end. Those are two different axes, and a method can move the wrong way along one while improving on the other.

## How to measure it after the fact

Proportionality is measurable once an election is over: what share of voters elected someone they feel represented by, and how strongly? A score ballot supports this directly — it already records degree of support, so the same ballots that ran the election can measure how well it represented the people who cast them.

Worked in this library on a shared electorate, both ways: [STV vs STAR-PR](../../method_comparisons/stv_vs_star_pr/README.md) counts one 100-voter, 3-seat election with each proportional method (they agree; the majoritarian one doesn't), and [exercise 12](../../01_STAR/05_Practice/ex12_bloc_vs_proportional.md) does the same at whiteboard scale.

## The families underneath: why RRV differs

The criterion difference isn't arithmetic trivia — it follows from which *school* of proportionality a method descends from. [electowiki](https://electowiki.org/wiki/Proportional_representation) groups them by philosophy, and the grouping predicts the behavior:

| School | Roughly | Methods |
|---|---|---|
| **PSC / Monroe** | each seat should "own" a quota of voters outright | STV (ordinal), Sequential Monroe, **Allocated Score** |
| **Unitary** | each voter has one vote's worth to spend, and spends it | Sequentially Spent Score, Sequentially Shrinking Quota |
| **Thiele** | reweight ballots by how much representation they've already got | Reweighted Range Voting, Sequential Proportional Approval, Single Distributed Vote |
| **Phragmén** | spread the "load" of electing winners evenly across voters | Sequential Phragmén, Sequential Ebert |

Quota-owning schools (PSC/Monroe, Unitary) hand a cohesive quota-sized faction a seat by construction. **That is the design philosophy, not a theorem, and the difference is checkable:** PSC is an *ordinal* axiom and Allocated Score is a *cardinal* method, so the guarantee does not actually follow — [here is a nine-voter election where a full quota rates its candidate a 5, prefers her to everyone, and wins no seat](../03_Criteria/solid_coalitions/README.md). **Thiele-school methods don't make that promise** — they equalize satisfaction rather than allocate quotas — which is precisely why RRV fails the Hare Quota Criterion above. Not a bug in RRV; a different answer to what "proportional" should mean.

Worth knowing that the taxonomy is itself unsettled at the edges: electowiki flags both RRV and Sequentially Shrinking Quota as *"may not be strictly"* their family but following from the theory, and lists the **stable winner set** philosophy with no known method at all — it is an open question whether a Hare-stable winner set always exists.

## Where the question is still open

Equal Vote's STAR-PR committee settled on **Allocated Score** as the vetted, recommended tabulation, and named three finalists worth further study and piloting: **Allocated Score, Sequentially Spent Score, and Sequential Monroe**. Reweighted Range is *not* among them, which is consistent rather than incidental — it is the one that doesn't pass the Hare Quota Criterion.

Two things follow that are worth knowing before treating any of this as settled. **Sequential Monroe is a named finalist this library cannot currently run** — the LH engine implements `allocated`, `sss` and `rrv`, so a third of the recommended shortlist has no runnable case here. And the committee's own listed next steps — a "criteria checker", broader simulations across election scenarios and strategies, and work on *ideal winner sets* and the optimal trade-off between competing constraints — are open questions, not conclusions. The right posture for a repo like this one is that proportional STAR's method selection is **an active research area with a current recommendation**, not a closed result.

## Who advocates what — read the lean

Almost every accessible source on proportional representation is published by an organization that favors one particular proportional method. That doesn't make them wrong; it makes the lean worth knowing before weighing a verdict. Per [electowiki](https://electowiki.org/wiki/Proportional_representation)'s own advocacy listing:

| Organization | Predominantly advocates |
|---|---|
| [FairVote](https://fairvote.org) | STV |
| [Center for Election Science](https://electionscience.org) | Proportional Approval Voting |
| [Equal Vote Coalition](https://equal.vote) | **Proportional STAR** — including this repo's subject, and the source of much of this page |
| Fix Our House · ProRep Coalition | proportional representation generally, method-agnostic |

The house rule applies here as everywhere: these are good sources for **definitions and mechanics** and weak ones for **verdicts**. For the neutral family term and for any criteria claim, prefer [Wikipedia](https://en.wikipedia.org/wiki/Proportional_representation); for rigor on the impossibility results underneath, prefer the academic literature.

One consequence worth stating plainly: this library is published by a STAR-focused project, so its proportional pages lean the same way. The corrective is that every claim here has a runnable election behind it — you can check the counts rather than taking the framing.

## See also

- [STAR-PR](STAR_PR/README.md) — the method: the ordinary 0–5 ballot, counted by reweighting
- [The math behind proportional STAR](STAR_PR/the_math_behind_proportional_star.md) — quota arithmetic, apportionment theory, JR/PJR/EJR
- [Bloc STAR](../../02_STAR_Bloc/README.md) — the majoritarian counterpart, where a cohesive majority can take every seat
- [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md) — the plain-language version of the fork
- [Allocated Score](https://electowiki.org/wiki/Allocated_Score) (electowiki) — the definition of Proportional STAR's official tabulation; a method-definition source, advocacy-adjacent on verdicts

*(The framing on this page — non-partisan proportionality, the quota-vs-threshold distinction, the "diverse how?" question, and the descriptive-representation caveat — follows Equal Vote's own STAR-PR presentation materials. Equal Vote advocates for these methods; the criteria and quota definitions are standard and checkable, the design arguments are theirs.)*
