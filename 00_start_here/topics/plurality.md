# Plurality — Choose-One / First-Past-The-Post

*The status quo for most US single-winner elections, and the baseline every reform on this site improves on. **Mark exactly one candidate; whoever gets the most marks wins — even without a majority.** Simple to count, but it forces the problems the other methods are designed to fix.*

→ The problems it creates: [the spoiler effect](spoiler_effect.md) · [vote splitting & the equally-weighted vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md) · is IRV just plurality in sequence? [RCV-IRV and plurality](../RCV_IRV/RCV_IRV_and_plurality.md)

---

## How it works

Each voter marks **one** candidate. Add up the marks. The candidate with the **most** marks wins — a *plurality*, which need not be a majority. That's the whole method. Its other names: **Choose-One**, **First-Past-The-Post (FPTP)**, **single-mark**, **first-preference plurality (FPP)**.

## What's wrong with it

The single mark is the root of a whole family of problems:

- **Vote splitting & spoilers.** Similar candidates divide their shared supporters, so a less-preferred candidate can win with a minority. A candidate who can't win still changes who does — the [spoiler effect](spoiler_effect.md). Plurality is the method *most* susceptible to it.
- **Minority winners.** With three or more candidates, the winner routinely has **less than half** the vote — a *plurality/minority winner* a majority actively voted against.
- **Lesser-evil voting & favorite betrayal.** Because backing your true favorite can "waste" your vote or help your worst choice, voters are pressured to abandon their favorite for a viable front-runner — the [favorite-betrayal](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) incentive.
- **No expression.** One mark captures neither *order* (who's your second choice?) nor *strength* (how much do you like them?) — see [ballot styles](ballot_styles.md).
- **Two-party entrenchment.** These pressures push the field toward two viable candidates over time (**Duverger's law**).

### Show me — a minority winner, worked

Five candidates, twenty voters. Under Choose-One only *first* choices count:

| Candidate | First choices | |
|---|--:|:--|
| **Erik** | **6 — 30%** | ← wins |
| Amy | 5 | |
| Ben | 4 | |
| Dana | 3 | |
| Cole | 2 | |

Erik takes office on **30%** — while **70% ranked someone else first, and nearly all scored him a flat 0.** Now read the *whole* ballot: Cole had just 2 first choices but broad, warm support everywhere (most voters rate him 4). He leads STAR's scoring round (70), wins the automatic runoff, and beats every rival head-to-head — the Condorcet winner. **[STAR](../STAR_Voting/STAR_start_here.md) and [Ranked Robin](../RCV_Ranked_Robin/why_ranked_robin.md) both elect Cole**, the candidate a majority is genuinely glad about; only first-choice counting crowns Erik. Same opinions, no strategy — the difference is how much of the ballot the method reads. See the whole field lined up in [same opinions, every method](same_opinions_every_method.md); run this one: [`minority_winner_c5_b20.yaml`](../../method_comparisons/minority_winner/minority_winner_c5_b20.yaml).

## Its relationship to the other methods

Every method this library teaches is, in part, a fix for one of plurality's failures:

| Reform | What it changes about the single mark |
|---|---|
| [Approval](../Approval_Voting/approval_voting.md) | Mark **as many** candidates as you like — similar candidates stop splitting. |
| [RCV-IRV](../RCV_IRV/RCV-IRV-Hare.md) | **Rank** candidates; eliminate-and-transfer instead of one round. (In fact **plurality is just IRV with a ranking limit of 1** — see [RCV-IRV and plurality](../RCV_IRV/RCV_IRV_and_plurality.md).) |
| [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) | Rank, then compare **every pair head-to-head** — elects the majority-preferred candidate. |
| [Score / Range](../Range_Voting/range_voting.md) · [STAR](../STAR_Voting/STAR_start_here.md) | **Rate** each candidate 0–5 — captures order *and* strength; STAR adds a runoff. |

## Where it's used

Most US single-winner offices — Congress (in most states), governorships, state legislatures, and the plurality stage of countless local races — still use plurality, which is why the spoiler and vote-splitting stories in this library are not abstract.

Sources: [Plurality voting — Wikipedia](https://en.wikipedia.org/wiki/Plurality_voting), [First-past-the-post voting — Wikipedia](https://en.wikipedia.org/wiki/First-past-the-post_voting), [Duverger's law — Wikipedia](https://en.wikipedia.org/wiki/Duverger%27s_law)

# file: plurality.md
