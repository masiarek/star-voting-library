# What makes a voting *method* good? — criteria beyond the winner

*Picking a good **winner** (see [What makes a good winner?](what_makes_a_good_winner.md)) is only half of choosing a voting method. The other half is everything around the tally: can voters use it, can citizens verify it, does it invite honest voting and real competition, is it practical to run? This page lays out those criteria — and the reason there's no clean answer: **a perfect election system will never exist**, so a good method is one that **balances** these against each other.*

→ **Level: Voting 201** — Curriculum [201.6](../CURRICULUM.md) (deeper theory at 301). Companion: [What makes a good winner?](what_makes_a_good_winner.md).

## "A perfect election system will never exist"

Arrow's impossibility theorem (ranked methods) and the Gibbard–Satterthwaite theorem (strategy-proofness) prove that no method can satisfy every desirable property at once. So the goal isn't a flawless method — it's the one that **balances the advantages against the disadvantages** for the election at hand. Which criteria matter most depends on stakes, number of candidates, single- vs multi-winner, and who's counting.

A consequence worth internalizing (Ka-Ping Yee): because *every* method must violate at least one of the five classic "reasonable behaviour" criteria, "one can always invent situations where a particular method violates one of these criteria — thus, presenting individual cases of strange behaviour proves little." A single anecdote (or even a handful) rarely settles anything; it's why reformers lean on **simulations across many electorates** ([VSE / Bayesian regret](what_makes_a_good_winner.md#measuring-it-empirically-vse--bayesian-regret)) rather than cherry-picked elections — while still using notorious real failures (Burlington 2009, Alaska 2022) to illustrate *how* a failure mode shows up in the wild.

## The criteria

### 1. Winner-selection quality
Does it tend to elect a *good* winner (majority / consensus-Condorcet / high-support-utilitarian)? Measured empirically by [Voter Satisfaction Efficiency](what_makes_a_good_winner.md#measuring-it-empirically-vse--bayesian-regret). Sub-properties are the classic **criteria**: majority, [Condorcet](condorcet), [monotonicity](monotonicity), independence of irrelevant alternatives, later-no-harm, favorite-betrayal.

### 2. Simplicity & practicality
How hard is it to **vote** and to **count**?

- **Ballot simplicity** — can a voter mark it correctly without instruction? (choose-one < approval/score < ranking.)
- **Tabulation simplicity** — can the winner be computed (and re-checked) easily? Round-by-round elimination (IRV), Borda, Minimax, Majority Judgment are heavier than a single sum.
- **Results viewability** — can a citizen look at the published totals and see *why* someone won?
- **Machine requirement** — hand-countable, or does it need software?

### 3. Summability (precinct-level counting)
Can each precinct publish a fixed-size tally that **adds up** to the national result, or must every ballot flow to one place? STAR and Approval are **summable** (a small matrix / totals per precinct); RCV-IRV and STV are **not** (transfers need the full ballot set centrally), which delays results and complicates audits. See [summability (topic hub)](summability).

### 4. Transparency & auditability
Can the public understand the process from ballots to result, and can it be checked? **Risk-limiting audits** are far easier on summable, single-round methods than on multi-round transfer methods.

### 5. Honesty (strategy-resistance)
Does the method reward **sincere** voting, or punish it? A method that pressures voters to betray their favorite (or bury a strong rival) corrupts the very data it counts. Favorite-betrayal and later-no-harm pressures, and vulnerability to burial/compromising strategy, all live here. The VSE simulations put a number on it — a **strategy-incentive ratio** (how often strategy *works* vs. *backfires* for a voter): Plurality **17.8 : 1** (strategy almost always pays), IRV ~2.7 : 1, Approval ~2.6 : 1, STAR ~**1 : 1** (strategy is as likely to backfire as to help). Low is good: it means sincere voting is safe. This strategy-resistance is arguably STAR's strongest empirical claim — under *honest* voting the top methods (STAR, Smith/Minimax/Condorcet, Approval) are close; STAR's edge is that it barely moves when voters get strategic.

### 6. Competition & representation
Does it let *all* candidates — including third parties and independents — get a clear, unpunished reflection of their support? A method with the **spoiler effect** / [vote-splitting](spoiler_effect.md) suppresses competition (voters abandon sincere favorites) and, in multi-winner form, the question becomes **proportionality** — does the elected body mirror the electorate? (see the [Pets Governance set](../../method_comparisons/pets_governance)).

### 7. Expressivity
Does the ballot let voters say what they mean — degrees of support, equal preferences, honest rankings — rather than forcing a single mark? More expressive ballots capture better data (and are what voters say they want), but must be weighed against simplicity.

### 8. Viability
Even an accurate, expressive method can fail politically if it's **too hard to explain** (Minimax, Majority Judgment, Schulze, EPR). "Analysis by paralysis": a method nobody trusts because nobody can follow the count won't be adopted or defended. Viability = accuracy × explainability × adoptability.

### 9. Cost & long-term incentives
Cost to run and audit; and the **long-term** effect on campaigning — does it reward broad coalition-building and sincere platforms, or negative campaigning and polarization?

## The trade-offs are the point

These pull against each other. The most **accurate** method may be the least **simple** (Minimax). The most **expressive** ballot is not the simplest to mark. **Summability** (STAR/Approval) buys easy audits but a score ballot asks more of voters than choose-one. A good method is a *deliberate balance*, chosen for the context:

| Priority | Leans toward |
|----------|--------------|
| Simplest possible ballot & count | Plurality / Approval |
| Consensus (Condorcet) winner, transparent | Ranked Robin |
| High-support winner + summable + audit-friendly | STAR |
| Proportional representation (multi-winner) | STV / STAR-PR |

## Where reasonable people disagree (the live debates)

These are genuine, unsettled disputes — presented as the case each side makes, not as a verdict:

- **Is VSE even the right yardstick?** VSE is *utilitarian* — it assumes summing satisfaction is the goal. Arrow (and others) argue that **cross-voter utility isn't comparable** ("my 4 vs. your 4"), so the extra information in a scored ballot is illusory and rankings are all that's legitimate. *Reply:* even a non-utilitarian usually grants "all else equal, more satisfaction for more people is better," and VSE is transparent about its assumption.
- **Do scored ballots have a stable meaning?** Critics note there's **no culture-independent mapping** from feelings to a 0–5 score (some people rate everything 4–5, others use 0/5), so a score ballot may be "a ranked ballot plus noise or compression." *Reply:* real preferences *do* carry intensity (would you rather lose \$30k, gain \$25k, or gain \$30k?), and a runoff (STAR) or 0/1 (Approval) curbs the worst gaming.
- **Can strategy be modeled at all?** VSE assumes a share of voters use simple strategies; skeptics argue real strategy depends on information and coordination and **can't be simulated naively**, so cross-method rankings deserve caution. *Reply:* VSE varied many strategy mixes and the *qualitative* ordering held; and the strategy-*resistance* result (who gains from strategy) is less model-sensitive than the raw accuracy gap.
- **Condorcet vs. cardinal.** Condorcet advocates: the pairwise-majority winner has the **strongest democratic claim**, and rankings dodge intensity-gaming. Cardinal advocates: **intensity matters**, and score methods are simpler to count/audit and monotonic. Under *honest* voting they're close; the disagreement is really about strategy and ballot philosophy.
- **Accuracy vs. simplicity.** Some conclude the accuracy gaps among *good* methods are small enough that **simplicity, transparency, and auditability** should decide (a case for Approval); others weight **expressivity** more (a case for Score/STAR). Both are defensible.

## Where the STAR case lands (stated as advocacy)

STAR-Voting advocates argue it balances the list well: an expressive 0–5 ballot that wastes no data, a two-step tally (score, then automatic runoff) that's **summable** and audit-friendly, strong VSE, and elimination of vote-splitting/spoilers — "Fair, Accurate, Equal." That's a *case*, not a theorem; opponents weigh ballot/tally complexity, or prefer a Condorcet guarantee (Ranked Robin) or proportionality (STV). This page's job is the criteria; [Why STAR](Why_STAR_Voting.md) and [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md) argue the trade-off both ways.

## Sources — and which way each leans

Almost every method comparison you'll read is written by someone with a preferred answer. That doesn't make it wrong — but read each one *knowing where it leans*. (Fuller rosters: [advocacy organizations](advocacy_organizations.md) · [who's who in voting methods](whos_who_voting_reform.md).)

| Source | What it offers | Leans toward |
|---|---|---|
| [Equal Vote Coalition](https://www.equal.vote) · [STAR Voting](https://www.starvoting.org) | STAR advocacy; the criteria & ["Farewell to Pass/Fail"](https://www.starvoting.org/pass_fail) essays | **STAR** |
| [Center for Election Science](https://electionscience.org) · [VSE](https://electionscience.github.io/vse-sim/) | Approval advocacy; the VSE simulations | **Approval** (cardinal) |
| [Center for Range Voting](https://rangevoting.org) | Bayesian-regret simulations; Score advocacy | **Score / Range** |
| [FairVote](https://fairvote.org) | the largest US RCV-IRV campaign | **RCV-IRV** |
| [Marcus Ogren — Voting in the Abstract](https://voting-in-the-abstract.medium.com/) | field-wide method analysis | **Condorcet**-leaning |
| [electowiki](https://electowiki.org/) | community method encyclopedia | reform-community (mixed) |
| [Stanford Encyclopedia — Voting Methods](https://plato.stanford.edu/entries/voting-methods/) | rigorous scholarly survey | **neutral** (academic) |
| [League of Women Voters (WA) — Review of Election Methods](https://www.lwvwa.org/resources/Documents/Review%20of%20Election%20Methods%202-12-20.pdf) | side-by-side comparison | **nonpartisan** |
| [Wikipedia — Comparison of electoral systems](https://en.wikipedia.org/wiki/Comparison_of_electoral_systems) | criteria compliance table | **neutral** (encyclopedic) |
| *this repository* | STAR-first, but tests STAR honestly against every method | **STAR** (with honest-limits pages) |

## See also

- [Criteria at a glance](criteria_at_a_glance.md) — the four methods' pass/fail across every criterion here, each failure linked to a runnable election (read *this page's* caveat first: a table is a map, not a verdict)
- [What makes a good winner?](what_makes_a_good_winner.md) — the winner-selection half
- Topic hubs: [Condorcet](condorcet) · [Summability](summability) · [Monotonicity](monotonicity) · [Center squeeze](center_squeeze) · [Ties](ties)
- [Why STAR Voting](Why_STAR_Voting.md) · [Scoring vs. ranked methods](scoring-methods-vs-ranked-voting.md) · [Glossary](../GLOSSARY.md)
