# Approval Voting in the theory literature — the case, the critiques, and what "approve" means

*The academic treatment of Approval says something the advocacy pages on both sides tend to skip: the deepest disagreement isn't whether Approval works, it's **what a checkmark means**. Three incompatible answers are in circulation, and which one you hold decides whether Approval is nearly strategy-free or entirely strategic — before any simulation is run. This page walks the standard survey treatment: the arguments made for Approval, the criticisms made against it, which criticisms survive scrutiny, and one elegant result — on a restricted domain, Approval **is** Borda **is** Condorcet.*

→ Overview: [Approval Voting](approval_voting.md) (the ballot and the count) · critique companion: [honest limits](approval_honest_limits.md) · run it: [the Approval examples](../../04_Approval/) · [Black Curtain](../../method_comparisons/black_curtain/). Source and its lean: the last section. Curriculum: [301.4](../CURRICULUM.md).

---

## Where the method came from

Formally, an **approval ballot** is just a *subset* of the candidates — the ones this voter approves. A candidate's **approval score** is the number of voters whose subset contains them, and the winner is whoever scores highest. That's the entire definition, and it is equivalent to the familiar phrasing: vote for as many as you like, most votes wins.

The provenance is unusually recent for a voting method. Brams and Fishburn's [*Approval Voting*](../books/rated_and_score_methods.md) (2007) credits the idea to **five different groups who arrived at it independently during the 1970s** — no single inventor, which is itself a mild argument that the rule is a natural thing to land on. The multi-author reference is Laslier and Sanver's edited collection (2010), which is also where the *critiques* live; both books are on the [rated & score methods shelf](../books/rated_and_score_methods.md).

## The six arguments made for it

Restated from the survey (which frames them as the case for Approval as an improvement on [Choose-One](../topics/plurality.md) in political elections), with where this library can check each one:

| # | The argument | Where it lands here |
|---|---|---|
| 1 | **Simplicity.** The ballot is barely more complicated than a plurality ballot and the counting rule is conceptually transparent — so it's an easier sell to the public. | Agreed, and it's the core of the [stepping-stone case](approval_voting.md#the-stepping-stone-argument). |
| 2 | **It fixes plurality's worst failure** — one candidate at the minority end of a spectrum defeating several who split the majority end. | The [spoiler effect](../topics/spoiler_effect.md) and the [vote-splitting set](../../method_comparisons/split_voting/); see the real election below. |
| 3 | **Better odds the winner has majority support**, which makes a governing "mandate" easier to claim. | *Odds*, not a guarantee — Approval has no majority criterion. |
| 4 | **No wasted votes**, so minor-party candidates finally show their true level of support. | The strongest of the six, and hard to argue with: nothing on an Approval ballot punishes you for marking a long shot. |
| 5 | **Likely to elect the [Condorcet winner](../topics/condorcet/) when one exists** (Beaujard et al. 2014, who also argue Approval favors "consensual" candidates near the middle of a multidimensional issue space — a generalization of argument 2). | *Likely*, not always — the counterexample is [in this repo](#the-caveat-that-matters-in-a-real-election) and is worked at the bottom of this page. |
| 6 | **Relatively resistant to strategic manipulation.** | The most contested of the six — and, as the next two sections show, the claim can't even be evaluated until you fix what "approve" means. |

**The real election behind argument 2.** The survey's example is the **1980 U.S. Senate race in New York**: Alfonse D'Amato won with a plurality under 45%, Elizabeth Holtzman finished close behind, and Jacob Javits — who had lost the Republican primary to D'Amato and stayed in on the Liberal line — took roughly a tenth of the vote from the same end of the spectrum. The claim is that had even a small share of Javits's voters also approved Holtzman, she would have won. That is vote-splitting in its textbook form. *This repo has not modelled that election* — no ballot data exists to model it *with*, and the library's rule is to build a **model** and label it one rather than invent real ballots. The mechanism itself is runnable here in miniature: [the split-voting set](../../method_comparisons/split_voting/).

## The five criticisms — and which of them survive

| # | The criticism | Verdict |
|---|---|---|
| 1 | **There is an ambiguity at its heart** — little agreement on, or understanding of, what it *means* to approve a candidate. | **Stands, and it's the deep one.** Balinski and Laraki (2010) consider it fatal. Laslier's counter-report is that voters experience the flexibility as a *relief* — an answer to the plurality dilemma of whether to vote for the best candidate or the best one with a chance. → next section. |
| 2 | **It over-restricts expressivity**, forcing voters to compress a ranking into two levels and to declare pairs equivalent that they don't actually feel are equivalent. | **Stands.** It's [honest limits §1](approval_honest_limits.md#1-no-preference-strength-or-order), stated by the literature rather than by STAR advocates. |
| 3 | **It violates "one person, one vote."** | **Weak** — the survey reads this as an argument of convenience rather than conviction. See [one person, one vote](../topics/one_person_one_vote.md): Approval passes the mathematical version of the standard (the [Test of Balance](../STAR_Voting/properties_and_limits/equally_weighted_vote.md)). |
| 4 | **It's unfair** — voters who approve more candidates get more influence. | **No basis.** The rebuttal is pure symmetry: recast Approval in terms of *dis*approval and the identical argument says the voter who names more *non*-approved candidates is the one gaining an advantage. An objection that flips with an arbitrary relabelling isn't an objection. |
| 5 | **Some arguments for Approval are rigged by methodology** — in particular, resistance-to-manipulation results depend on how you set up a comparison between preference ballots and approval ballots. | **Stands, and cuts both ways.** This is the [claim-check habit](../../method_comparisons/single_winner_scorecard/README.md) stated in a neutral source: when a method is compared to another on a ballot type only one of them uses, check who chose the translation. |

Two of these — 3 and 4 — are the ones usually shouted, and they're the two that don't hold up. That asymmetry is worth remembering in a debate: **the strong criticisms of Approval are about expressivity and meaning, not about fairness.**

## The real fault line: what does "approve" mean?

Criticism 1 isn't a quibble — it's a genuine three-way split among researchers about what a voter is *doing* when they check a box. The survey lays out three views:

1. **A compressed ranking.** The voter really has a ranking (possibly with ties), and the approval ballot forces several distinct levels of liking down into exactly two.
2. **A dichotomous primitive.** There is no hidden ranking. The voter simply likes or dislikes each candidate, and is genuinely indifferent among those in each group.
3. **A ranking plus a line.** The voter has both a ranking *and* a meaningful dividing line between the candidates they like and those they don't — a **true zero**. Cardinal utilities can sit under view 1 as well, and under view 3 if utilities may be negative.

These are not shades of the same position. They imply different answers to whether a given ballot is even *sincere*.

## Why the strategy argument never settles

Each view produces a different verdict on argument 6 — before anyone runs a simulation:

- **If approval is a primitive (view 2):** each voter has exactly *one* sincere ballot, and no incentive whatever to cast a different one. Approval comes out looking maximally honest, essentially by construction.
- **If there's an underlying ranking (view 1):** it is never to your advantage to approve a candidate without also approving everyone you like at least as much — so a ballot is just a cut through your own ranking, and the whole decision reduces to, in the survey's phrase, "where to draw the line." But if that line carries no intrinsic meaning, **there is no basis for calling one ballot sincere and another insincere** — you may as well say every Approval ballot is strategic, or that none is.
- **If the voter has a true zero (view 3):** drawing the line anywhere else is insincere by definition — and such a voter can have a real incentive to do exactly that.

So "Approval is resistant to strategy" is downstream of a philosophical premise, not only of simulation methodology. That is criticism 5 with teeth, and it's why this argument recurs forever.

**Where voters actually draw the line** — two findings the survey cites, and both match what [honest limits §2–3](approval_honest_limits.md#2-the-approval-threshold-dilemma-the-central-critique) describes from the practical side:

- **Duddy et al. (2013):** drawing the line at your *mean* utility maximizes a measure of total separation between the approved and unapproved groups — a defensible "honest" threshold, if you want one.
- **Laslier (2009):** the strategically best line sits near the utility you assign to the *expected winner* — and voters tend to behave that way in practice. Which means Approval outcomes move with the polls, exactly as this library's threshold critique claims, now with a citation instead of an assertion.

## Approval = Borda = Condorcet — on one restricted domain

Here is the elegant part, and it is genuinely surprising the first time you meet it.

Translate each approval ballot into a weak ranking: everything approved sits above everything not approved, with indifference inside each group. That confines the ballots to the domain of **dichotomous preferences** — weak rankings with exactly two non-empty indifference classes. On that domain, three things that normally disagree collapse into one:

- **Approval = [Borda](../other_ranked_methods/borda.md).** Applying the ordinary net-preference and symmetric-Borda definitions directly to these weak rankings reproduces the approval count exactly. (The equivalent bookkeeping: when a ballot expresses indifference, award each candidate in a tied group the *average* of the scoring weights that group spans.) Whether *other* scoring rules also collapse to Approval depends on the convention used for indifference — for some, like k-approval, the adaptation that would make it work looks artificial.
- **Every profile has a [Condorcet winner](../topics/condorcet/).** Define "x beats y" as *more voters strictly prefer x to y than the reverse*. On dichotomous ballots that is precisely "more voters approve x than approve y" — which is transitive and always has a maximum. No cycles are possible.
- **Therefore Approval agrees with every Condorcet method** on this domain. One can fairly say that on dichotomous preferences, **Approval reconciles Borda and Condorcet** — the two poles that disagree nearly everywhere else.

The structural reason is one this library already has a page for: the disagreement between Borda and Condorcet lives entirely in the **cyclic component** of the weighted tournament, and on dichotomous ballots that component is always zero. See [the cycle–cocycle decomposition](../topics/cycle_cocycle_decomposition.md) — this is the same theorem viewed from the approval end, and [Copeland vs Borda — margins matter](../../method_comparisons/copeland_vs_borda_margins/README.md) is what it looks like when the cyclic part is *not* zero.

### The caveat that matters in a real election

Two conditions are doing quiet work above, and both are worth stating out loud:

1. **The majority relation is defined by net strict preference** — more voters preferring x to y than y to x — *not* by "more than half of all voters rank x above y." With many indifferences those are different relations, and the second one behaves badly.
2. **If the approval ballots were produced by compressing real rankings, the Condorcet winner of the uncompressed rankings can be somebody else.** The theorem is about a *domain*, not a property you can carry into an election where voters are doing the compressing.

Caveat 2 is not hypothetical, and this repo has it on file. In [Black Curtain #1](../../method_comparisons/black_curtain/), five voters score three candidates; three of them love Cal and loathe Ann, two the reverse, and *every* voter rates Bob near the top. On the underlying scores the engine reports a clean Condorcet winner:

```text
[Condorcet Winner]
  Condorcet Winner: Cal — matches the STAR winner
```

Now let those same five voters compress to approval at "a 3 or better is an approval" — the [same election as an Approval count](../../method_comparisons/black_curtain/cases/cases_pages/Black_Curtain_01a_c3_b5_approval.md):

```text
--- Approval Voting (single winner) ---
 Tabulating 5 ballots (any non-zero score = approval).

   Bob -- 5 (100%) -- Elected
   Cal -- 3 (60%)
   Ann -- 2 (40%)

[Approval Distribution] (how many candidates each ballot approved)
   10 approvals across 5 ballots — average 2.0 of 3 (range 2–2).
     approved 2: 5 ballots
```

Both results are correct, and together they are the theorem *and* its limit in five ballots:

| | Underlying scores/rankings | The same voters, compressed to approval |
|---|---|---|
| Cal vs Bob | Cal wins **3–2** (voters 1–3 score Cal above Bob) | Bob wins **2–0**, with **3 Equal Support** — voters 1–3 approve *both*, so they express no preference |
| Bob vs Ann | Bob **3–2** | Bob **3–0**, with **2 Equal Support** |
| Condorcet winner | **Cal** | **Bob** |
| Method winner | Cal (STAR, RCV-IRV, Choose-One) | **Bob** (Approval — *and* STAR, and every Condorcet method) |

On the compressed ballots Bob really is the Condorcet winner, exactly as the theorem promises — the dichotomous domain has no cycles, and Approval finds its winner. But the preference that decided the original election, *Cal over Bob*, was thrown away by the three voters who approved both. Argument 5 ("likely to elect the Condorcet winner") survives as a statement about tendencies; it is not a guarantee, and the gap is the compression itself.

Both columns are engine output, not arithmetic done here: the right-hand one is [case 01b](../../method_comparisons/black_curtain/cases/cases_pages/Black_Curtain_01b_c3_b5_dichotomous.md), the same five approval ballots read pairwise. **Worked in full, with both matrices side by side and what the Equal Support column is doing: [When compression moves the Condorcet winner](../../method_comparisons/black_curtain/condorcet_compression.md).**

## What to take from all this

- The **strong** criticisms of Approval are expressivity (criticism 2) and meaning (criticism 1). The popular ones — "unfair to voters who approve more," "violates one person one vote" — do not hold up, and conceding that makes the real critique land harder.
- **"Is Approval strategy-resistant?" is not purely an empirical question.** Answer "what does approving mean?" first; the strategy verdict follows from that answer.
- The **Borda = Condorcet** result is real and beautiful, and it is about a restricted domain. Quote it as a property of dichotomous preferences, never as "Approval elects the Condorcet winner."
- All of it is consistent with this library's own [honest limits](approval_honest_limits.md) page — which is worth noting, because that page was written from the STAR side and this material was not.

## Source

- **William S. Zwicker, "Introduction to the Theory of Voting,"** in *Handbook of Computational Social Choice* (Brandt, Conitzer, Endriss, Lang & Procaccia, eds., Cambridge University Press, 2016) — the approval-voting section, including the arguments and criticisms above, the three readings of "approve," and the *Approval = Borda = Condorcet* result. **Lean:** neutral; the standard academic reference, and the same chapter this repo leans on for [May's theorem](../topics/mays_theorem.md), the [SWF/SCF distinction](../topics/social_welfare_function.md), [what a method reads](../topics/what_a_method_reads.md) and the [cycle–cocycle decomposition](../topics/cycle_cocycle_decomposition.md).
- Works it cites, and which this page names: **Brams & Fishburn**, *Approval Voting* (2007) and **Laslier & Sanver** (eds.), *Handbook on Approval Voting* (2010) — both on the [books shelf](../books/rated_and_score_methods.md); **Balinski & Laraki** (2010) on the ambiguity as a fatal flaw (see [majority judgment](../voting_paradoxes/majority_judgment.md)); **Beaujard et al.** (2014) on Condorcet efficiency and consensual candidates; **Duddy et al.** (2013) on the mean-utility threshold; **Laslier** (2009) on the expected-winner threshold.

## See also

- [Approval Voting](approval_voting.md) — the ballot, the count, and how to read a result
- [Approval — Honest Limits](approval_honest_limits.md) — the same critiques from the practical side
- [Approval + Top-Two](approval_top_two.md) — what a second, head-to-head round recovers from a 0/1 ballot
- [Preference vs support](../scores_and_ranks/preference_vs_support.md) · [scores vs ranks](../scores_and_ranks/scores_vs_ranks.md) — the two questions a ballot can ask
- [Gibbard–Satterthwaite](../topics/gibbard_satterthwaite_theorem.md) — why "resistant" is the strongest any method gets
- [Black Curtain](../../method_comparisons/black_curtain/) — five voters, four methods, three different winners

# file: approval_in_the_literature.md
