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

100 voters, three candidates. Under Choose-One only *first* choices count:

| Candidate | First choices | |
|---|--:|:--|
| **Ada** | **34 — 34%** | ← wins |
| Ben | 33 | |
| Cleo | 33 | |

Ada takes office on **34%** — but **66 of the 100 voters scored her 0 or 1.** Two-thirds didn't want her; they just split their first choices between Ben and Cleo. Now read the *whole* ballot: Cleo is nobody's fiery favorite (33 first choices) but everybody's easy second — she leads STAR's scoring round (433), wins the automatic runoff over Ada **66–34**, and beats both rivals head-to-head (the Condorcet winner). **[STAR](../STAR_Voting/STAR_start_here.md) and [Ranked Robin](../RCV_Ranked_Robin/why_ranked_robin.md) both elect Cleo**, the candidate a majority is genuinely glad about; only first-choice counting crowns Ada. Same opinions, no strategy — the difference is how much of the ballot the method reads. (With a bigger field it gets starker — Choose-One winners can take office on 10–20%.) **▶ [See it live on BetterVoting](https://bettervoting.com/2p33qq/results)** (all three counts). The full worked page: [minority winner](../../method_comparisons/minority_winner/README.md) · the whole field lined up: [same opinions, every method](same_opinions_every_method.md).

**This isn't hypothetical — it's North Carolina.** A NC **primary** can be won with just over **30%** of the vote (the threshold was cut 50% → 40% → 30% to make runoffs *rarer*); below it, the runner-up may *request* a separate, low-turnout **"second primary."** The **general election** has **no minimum at all** — the most votes wins, even far below a majority, so a candidate most voters ranked low can still take office. STAR's fix uses the same ballot with an [automatic runoff](../STAR_Voting/the_count/STAR_Automatic_Runoff.md) built in: a majority-backed winner and no costly second trip to the polls. (NC's ranked-ballot history: [RCV-IRV in North Carolina](../RCV_IRV/case_studies/RCV_IRV_north_carolina.md).)

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
