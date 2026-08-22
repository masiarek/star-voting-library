# A ranking does not determine a score result

*Handed a ranked profile, it is tempting to "just score it" — first choice 5, second 4, and so on — and read off what STAR would do. But a rank order is compatible with **many** score ballots, and score methods run on the **magnitudes**. So the conversion is not a translation; it is an added assumption, and it can decide the election.*

**Level: 301 · deep dive**

→ the distinction underneath: [scores vs. ranks](scores_vs_ranks.md) · what each direction costs: [the fidelity ladder](fidelity_ladder.md) · the sibling failure: [scale granularity can flip the winner](scale_granularity_flips_the_winner.md)

---

## The one idea

A ballot that says `Alice > Bilal > Cato` is silent on a question STAR must answer: **how much** more. `5,4,3` and `5,1,0` encode the same order and describe different voters — one mildly prefers Alice, the other barely tolerates Cato. The [scoring round](../../01_STAR/01_Learn/the_count/README.md) sums those numbers, so it can reach different finalists from the same ranking, and a different finalist can win.

This is not the same as [granularity](scale_granularity_flips_the_winner.md), the sibling page. There the *scale* changes (0–9 compressed to 0–5). Here the scale is fixed at 0–5 throughout and only the **spacing within it** moves. Same paper, same rungs, different habits.

## The cleanest demonstration

Seventy-four voters, four candidates, one preference order. Two ways of filling in the same 0–5 ballot:

| | ballots | STAR elects |
|---|---|---|
| [Consecutive scores](../../method_comparisons/equal_rank_irv/cases/equal_rank_cohesive_consecutive.yaml) | `5,5,5,4` · `5,5,3,4` · `5,3,5,4` · `4,5,5,5` · `4,4,4,5` | **Alice** |
| [Wide gaps](../../method_comparisons/equal_rank_irv/cases/equal_rank_cohesive_wide_gaps.yaml) | `5,5,5,0` · `5,5,0,3` · `5,0,5,3` · `0,5,5,5` · `0,0,0,5` | **Delia** |

Check the rows against each other: every one induces the identical ordering. Row 1 is `Alice=Bilal=Cato > Delia` in both. Row 5 is `Delia > Alice=Bilal=Cato` in both. **Nobody reordered anybody — only the gaps moved**, and the winner changed.

It is not an artifact of this library's engine, either. The pair is live as **[BV2297](https://bettervoting.com/j9wvv4/results)** (`j9wvv4`) — one election, two races — and BetterVoting independently elects Alice in the first and Delia in the second. Full lesson: [equal ranks on an IRV ballot](../../method_comparisons/equal_rank_irv/README.md).

## How to tell whether it matters — measure, don't assume

The question is never "could the spacing matter" (it always could) but "does it, here." That is checkable: enumerate the strictly-decreasing 0–5 assignments a ballot's rank levels admit, sample a few thousand profiles, and count who wins.

Run over 20,000 random encodings each, the three profiles in the equal-rank set come out very differently:

| Profile | STAR's winner across all valid 0–5 encodings |
|---|---|
| [A bare majority tops Amira](../../method_comparisons/equal_rank_irv/cases/equal_rank_majority_alternative.yaml) | **Basil 98.5%**, remainder exact scoring ties, nobody else ever |
| [Five voters](../../method_comparisons/equal_rank_irv/cases/equal_rank_five_voters.yaml) | **Aida 92.9%**, never Bram outright |
| [The cohesive-majority profile](../../method_comparisons/equal_rank_irv/cases/equal_rank_cohesive_consecutive.yaml) | Delia 35% · Alice 19% · Bilal 12% · Cato 11%, rest ties |

The first two are safe to quote. The third has no answer to quote — and saying so *is* the result.

## When the spacing can't bite

There is a good predictor: **a Condorcet winner anchors the outcome.** If one candidate beats every rival head-to-head, STAR's runoff will elect them from any finalist pairing that includes them, and the spacing only has to get them into the top two. Where the pairwise picture is a [cycle](../topics/condorcet/README.md) — as in the 74-voter profile above, which has one — there is nothing to anchor to, and the conversion carries the whole result.

That is exactly the contrast the [Copeland vs. Borda margins](../../method_comparisons/copeland_vs_borda_margins/README.md) page draws against [Condorcet's 1788 profile](../../method_comparisons/borda_condorcet_1788/README.md): the 1788 result is robust to the spacing, the margins one is not, and the difference is whether a Condorcet winner exists.

## The house rule

1. **Never quote a STAR winner for someone else's ranked profile from one encoding.** Sample the valid encodings and report the rate.
2. **If it is stable, say the number** — "Basil in 98.5% of encodings" is a much stronger claim than "STAR elects Basil," and it costs one paragraph.
3. **If it is not stable, ship the instability** rather than picking a winner: a matched pair, same cast, one encoding each, and a sentence saying the ranking does not determine the result.
4. **Say which convention produced a number**, always — the same discipline this library already applies to [Minimax's three readings of "worst loss"](../voting_paradoxes/minimax.md) and to a truncated ballot's unstated pairs.

## The witnesses in this library

- [Equal ranks on an IRV ballot](../../method_comparisons/equal_rank_irv/README.md) — the matched pair above; the encoding decides between Alice and Delia, and the profile has no Condorcet winner.
- [Margins matter](../../method_comparisons/copeland_vs_borda_margins/README.md) — Almond wins under 5/3/0, 5/4/0, 5/2/0 and 4/2/0; under a polarized **5/1/0** the scoring round promotes Cocoa instead, and Cocoa wins.
- [The 5-1-0 challenge](../../method_comparisons/star_5_1_0_challenge/README.md) — the same dial as a *strategy* rather than an artifact: what happens when voters deliberately choose the widest spacing.

## Related

- [Scores vs. ranks](scores_vs_ranks.md) · [preference vs. support](preference_vs_support.md) — why the extra information exists in the first place
- [The fidelity ladder](fidelity_ladder.md) — the general account of what each conversion direction loses
- [Scale granularity can flip the winner](scale_granularity_flips_the_winner.md) — the sibling: changing the *scale* rather than the spacing on it
- [Weak ranks](weak_ranks.md) — the ballot the equal-rank cases are written on

# file: ranking_does_not_determine_scores.md
