# Satisfaction Approval Voting (SAV) — one vote, split among everyone you approve

**Level: 301 · deep dive**

*The same Yes/No ballot as [Approval](../approval_voting.md), a different way of adding it up. Under [bloc Approval (AV)](approval_multiwinner.md) every approved candidate gets a **whole** vote; under **SAV** each voter has **one** vote, split evenly among the candidates they approved. Approve four, and each gets ¼. Proposed by Steven Brams and D. Marc Kilgour in 2010, and — under the name **equal and even cumulative voting** — used for real, in Peoria, Illinois, since 1991. Every number on this page is reproduced with Martin Lackner's [`abcvoting`](https://github.com/martinlackner/abcvoting) and checked against an independent implementation of the paper's own formula.*

Source: Brams, S. J. & Kilgour, D. M. (2010), [*Satisfaction Approval Voting*](https://mpra.ub.uni-muenchen.de/22709/), MPRA Paper 22709 — prepared for the Midwest Political Science Association, Chicago, 22–25 April 2010. Section and proposition numbers below are the paper's.

---

## The rule

A voter's **satisfaction score** is *the fraction of their approved candidates who are elected*. SAV elects the size-`k` committee that maximises the **sum** of all voters' satisfaction scores:

```
s(S) = Σ_i  |V_i ∩ S| / |V_i|          (V_i = voter i's approval set, S = the committee)
```

That looks like it needs checking every possible committee. It doesn't — the paper's **Proposition 1** shows the objective is *additive*, so:

> **Under SAV, the `k` winners are simply the `k` candidates with the highest individual satisfaction scores**, where a candidate's score is `Σ 1/|V_i|` over the voters who approved them.

So the whole method is one pass: **a voter approving `n` candidates gives each of them `1/n` of a vote; add the columns; the top `k` win.** That is exactly as summable and as hand-countable as plain Approval — the only change is that the ballot is worth 1 vote total rather than 1 vote *per mark*.

| | what one voter contributes to each approved candidate |
|---|---|
| **AV** (bloc Approval) | `1` — approve more, and you push harder for all of them |
| **SAV** | `1/n` — one vote, divided; approving more **dilutes** each |
| **[PAV](thiele_methods.md)** | `1/j` where `j` counts the voter's approved **winners** — diminishing returns on *representation*, not on marks |

The PAV row is the distinction worth holding onto. SAV divides by how many you **approved**; PAV divides by how many of yours **won**. That one difference is why PAV is proportional and clone-independent while SAV is neither.

## The worked example (§2, Proposition 2)

Four candidates, ten voters, **two seats**. Four voters approve a two-person slate; the other six bullet-vote:

| voters | approve |
|---:|---|
| 4 | Ada, Ben |
| 3 | Cleo |
| 3 | Dev |

| | Ada | Ben | Cleo | Dev | elects |
|---|:--:|:--:|:--:|:--:|---|
| **AV** — one vote per mark | **4** | **4** | 3 | 3 | **Ada, Ben** |
| **SAV** — one vote, split | 4×½ = 2 | 4×½ = 2 | 3×1 = **3** | 3×1 = **3** | **Cleo, Dev** |

The two methods elect **disjoint** committees from identical ballots — that is the paper's **Proposition 2**, and this is its proof. The slate voters' marks were worth a full vote each to AV and half a vote each to SAV, and half a vote was not enough.

Which answer is better depends on what you are counting. Brams & Kilgour count *voters left with nobody*: `{Cleo, Dev}` gives six voters a representative, `{Ada, Ben}` only four. On that measure SAV wins, and that is the paper's whole argument — AV "can fail to reflect the diversity of interests in the electorate."

Runnable, with the full six-rule comparison: **[the disjointness case](../../02_Examples/multiwinner/cases/approval_sav_disjoint_c4_b10_brams_kilgour.yaml)**, and live on BetterVoting under three methods — see [Worked examples](#worked-examples-in-this-repo) below.

## Where SAV sits on the spectrum

The [ABC-rule spectrum](abc_rules_spectrum.md) runs from **utilitarian** (AV: maximise total approvals) to **egalitarian** (CC: cover as many voters as possible). SAV is not a point on the [Thiele](thiele_methods.md) dial at all — a Thiele method weights by *how many of your approved candidates won*, and SAV weights by *how many you approved*, which is a property of the ballot rather than of the outcome. It sits **beside** the family, aimed at the same coverage goal as CC but reached by a much cheaper computation (CC is NP-hard; SAV is one addition pass).

That cheapness is the trade. SAV *usually* moves toward coverage, but it does not optimise for it, and the paper is candid about the gap — see the next two sections.

## What SAV buys you (Proposition 5)

Seventeen voters, three candidates, two seats:

| voters | approve |
|---:|---|
| 5 | Ash, Bree |
| 5 | Ash, Cole |
| 4 | Bree |
| 3 | Cole |

AV counts Ash 10, Bree 9, Cole 8 and elects **{Ash, Bree}** — leaving the three Cole-only voters with nobody. SAV scores Ash 5, Bree 6½, Cole 5½ and elects **{Bree, Cole}**, which represents **all seventeen voters** and is the smallest set that can. Ash, approved by more voters than anyone, is elected by neither measure of merit that matters here — every one of Ash's supporters already has a second choice in the committee.

Note what did the work: the ten slate voters each split their vote, so Ash — approved by all ten of them and nobody else — collected only 5. Bree and Cole each combined half-votes from the slate with **whole** votes from bullet voters, and the bullet voters decided it.

Runnable: **[the coverage case](../../02_Examples/multiwinner/cases/approval_sav_covers_everyone_c3_b17_brams_kilgour.yaml)**.

## What SAV costs you — the authors' own counter-examples

A paper that only showed its method winning would not be worth citing. Brams & Kilgour prove the other direction too:

- **Proposition 3 — an AV outcome can be *more* representative than SAV's.** With `2: a`, `5: ab`, `6: cde` and two seats, every AV committee (`{a,c}`, `{a,d}`, `{a,e}`) represents **all 13** voters; SAV elects `{a,b}`, representing **7**. The six `cde` voters split three ways and each of their candidates collected only 6×⅓ = 2.
- **Proposition 4 — a committee can beat *both*.** With `4: ab`, `4: acd`, `3: ade`, `1: e`, AV and SAV agree on `{a,d}` (11 of 12 voters represented) while `{a,e}` represents all 12.
- **Proposition 6 — SAV, AV and the greedy coverage heuristic can *all* miss.** With `3: ab`, `3: ac`, `2: b`, `1: c`, all three return `{a,b}`, while `{b,c}` is the minimal representative set.

The honest summary is the one the paper gives: SAV "generally" — not always — represents more voters than AV, and maximising total satisfaction is a *proxy* for coverage, not a guarantee of it.

## Clones, spoilers, and the incentive that runs backwards

This is where SAV is most interesting for this library, because it inverts the usual [spoiler](../../../07_Concepts/topics/spoiler_effect.md) story. Twelve voters, two seats, everyone bullet-voting:

| | before the split | after `a` splits into clones `a₁`, `a₂` (its 5 supporters approve both) |
|---|---|---|
| profile | `5: a`, `4: b`, `3: c` | `5: a₁a₂`, `4: b`, `3: c` |
| **AV** | `{a, b}` — represents 9 of 12 | **`{a₁, a₂}`** — represents **5** of 12 |
| **SAV** | `{a, b}` — represents 9 of 12 | **`{b, c}`** — represents 7 of 12 |

Under AV, running a second clone is a **winning strategy**: the five-voter faction takes both seats and two-thirds of the electorate ends up unrepresented. Under SAV the same move is self-defeating — `a₁` and `a₂` land on 2½ each and both lose. Brams & Kilgour make the point directly: because SAV divides one vote among all of a voter's approvals, it **discourages** clones, whereas AV "creates the greatest incentive to form clones."

So SAV's vote-splitting is not an accident of the design; it *is* the design, and it points the strategic incentive at coalition-building rather than at candidate-multiplying.

The flip side is the one the critics press, and it is equally real: a faction that *cannot* coordinate — that runs three candidates and whose voters sincerely approve all three — is punished for it, whatever its size. Under SAV a voting bloc has to know how many seats it is entitled to and mark exactly that many. **Neither AV nor SAV is proportional; they fail in opposite directions**, and PAV is the rule that fails in neither, because it divides by winners rather than by marks.

## Semi-proportional, and what that means precisely

Applied to **party lists** (§5), SAV apportions seats by the **Jefferson/d'Hondt** method with a quota constraint — a genuine, if large-party-favouring, proportional rule. Applied to **individual candidates**, that guarantee does not carry over, because the divisor becomes the number of candidates a voter marked rather than the size of their party. This is the precise sense in which SAV is called **semi-proportional**: proportional over parties, and proportional over candidates only to the extent that voters coordinate their marks. It is the same bargain [SNTV](../../../method_comparisons/sntv_village_council/) and cumulative voting strike.

## In the wild

- **Peoria, Illinois** has elected its five at-large council seats by **equal and even cumulative voting** since 1991, adopted in settlement of a 1987 Voting Rights Act suit ([FairVote](https://archive.fairvote.org/?page=1939) — an advocacy source, cited here for the factual history). A voter selects up to five candidates and their five votes are divided equally among them: pick two and each gets 2.5. Dividing 5 votes instead of 1 scales every score by the same constant, so **Peoria's rule ranks candidates exactly as SAV does** — with the one difference that Peoria *caps* approvals at the number of seats, where SAV as defined imposes no cap.
- **The Game Theory Society, 2003** (§3) — 161 voters elected 12 of 24 council members by AV. Recomputing those ballots under SAV swaps **2 of the 12** winners: the candidates who finished 10th and 12th are displaced by those who finished 13th and 14th. The SAV committee leaves 2 voters unrepresented; the AV committee leaves 5. The authors flag the obvious caveat themselves — voters might well have marked different ballots had SAV been the announced rule, so this is a recount, not a prediction.

## Strategy

The decision-theoretic analysis (§4) enumerates the 19 contingencies in which one voter can change a 3-candidate, 2-seat outcome. The result: **every strategy is undominated except approving of your least-preferred candidate**. Approving your top two performs about as well as bullet-voting, even though doing so halves the weight behind your favourite. So SAV does not push voters toward bullet-voting the way the vote-splitting arithmetic might suggest — which is the paper's answer to the natural first objection.

## Claim-check: the Wikipedia retelling doesn't add up

Wikipedia's SAV article illustrates the method with a version of §2 dressed in 1824 clothing — Adams, Clay and Webster as Whigs, against Crawford and Jackson. It is a corrupted copy of the example above, and three of its numbers are wrong. Recorded here because the page is many readers' first contact with SAV, and because the underlying result (Proposition 2) is perfectly sound and deserves a correct telling.

| Wikipedia says | what the arithmetic gives |
|---|---|
| "there are 10 voters" | the blocs it then lists are 6 + 3 + 3 = **12** |
| "despite winning a full majority of the vote, the Whigs receive no seats" | 6 of 12 is **exactly half**, not a majority. In Brams & Kilgour's original the slate bloc is **4 of 10 — 40%**, and no majority is claimed |
| "Had one of the three candidates dropped out, the remaining two would have received **4 votes and swept both seats**" | each survivor gets 6/2 = **3** — a **four-way tie** with Crawford and Jackson at 3, and no sweep. (Had *two* dropped out, the survivor would score 6 and take **one** seat.) "4 votes" is the original's number for a bloc of **4** voters, left behind when someone inflated the bloc to 6 |

The mangling is mechanical: the original's `4 voters: ab` became `6 voters: Adams, Clay, Webster`. That preserves the satisfaction score that makes the example work (4×½ = 2, and 6×⅓ = 2 — the slate candidates still finish below the bullet-voted rivals at 3) while breaking the voter count, the majority claim, and the dropout arithmetic around it.

One framing point beyond the arithmetic. Wikipedia presents this outcome as a **failure** — a "wipeout" caused by "spoiler effects." Brams & Kilgour present the *same committee on the same ballots* as the **point**: it represents six voters where AV's represents four. Both readings are defensible and they are counting different things; what is not defensible is presenting either one as the arithmetic. The genuine criticism of SAV is sharper and narrower than the article's, and the authors state it themselves in Propositions 3, 4 and 6.

## Run it here

`sav` is one of `abcvoting`'s rules, so any approval YAML in this repo can be counted under it:

```bash
python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py \
  04_Approval/02_Examples/multiwinner/cases/approval_sav_disjoint_c4_b10_brams_kilgour.yaml \
  --rules av,sav,pav,seqpav,cc,seqphragmen
```

The LH engine's `voting_method: Approval_Multi_Winner` is the **AV** half of every comparison on this page — it counts one vote per mark. SAV, PAV and the rest come from the [`abcvoting` engine](../../../06_Other/abcvoting_tabulation_engine/README.md).

## Worked examples in this repo

| Case | Seats | The lesson | Live |
|---|:--:|---|---|
| [SAV vs AV — disjoint committees](../../02_Examples/multiwinner/bv2271_4hfwqd_sav_disjoint.md) | 2 | Proposition 2 on the paper's own ballots: AV elects `{Ada, Ben}`, SAV elects `{Cleo, Dev}`, no overlap. Bloc **STAR** and **Ranked Robin** both agree with AV — so SAV is the lone dissenter, not AV the outlier | **BV2271** · [results ↗](https://bettervoting.com/4hfwqd/results) |
| [SAV covers everyone AV leaves out](../../02_Examples/multiwinner/bv2272_dr6fmg_sav_coverage.md) | 2 | Proposition 5: AV's `{Ash, Bree}` strands three voters; SAV's `{Bree, Cole}` is the minimal set representing all 17 — and **PAV agrees with SAV here**, while *sequential* PAV does not | **BV2272** · [results ↗](https://bettervoting.com/dr6fmg/results) |

Each live election carries the same electorate under **Approval, STAR and Ranked Robin** (BetterVoting has no SAV tabulator). Within each election all three agree — which is the useful negative result: SAV's answer is not one that the methods in ordinary use ever reach.

## References

- Brams, S. J. & Kilgour, D. M. (2010), [*Satisfaction Approval Voting*](https://mpra.ub.uni-muenchen.de/22709/), MPRA Paper 22709 — the primary source for every proposition above.
- [Satisfaction approval voting](https://en.wikipedia.org/wiki/Satisfaction_approval_voting) (Wikipedia) — the neutral-tier source for notability and the Peoria usage; see the claim-check above before relying on its worked example.
- Lackner, M. & Skowron, P. (2023), [*Multi-Winner Voting with Approval Preferences*](https://doi.org/10.1007/978-3-031-09016-5) — the textbook framing of ABC rules that this page's "spectrum" section leans on.
- Companion pages: [Approval — multi-winner](approval_multiwinner.md) · [ABC-rule spectrum](abc_rules_spectrum.md) · [Thiele methods](thiele_methods.md) · [the ABC engine](../../../06_Other/abcvoting_tabulation_engine/README.md)
