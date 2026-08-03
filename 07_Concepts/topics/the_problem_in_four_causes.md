# The problem, in four causes — where a voter's influence actually gets lost

*A structural diagnosis, borrowed and extended. **Wesley H. Holliday** (UC Berkeley philosophy; a board member at Better Choices for Democracy) opens ["How to Make Every Voter Matter and Make Spoiler Effects Go Away"](https://www.betterchoices.vote/news/how-to-make-every-voter-matter-and-make-spoiler-effects-go-away) with an unusually clean move: state the problem in one sentence, then break it into **separate causes**, each with its **own** fix. That structure is worth stealing, because it kills the most common confusion in reform arguments — treating "voters don't matter" as one big grievance with one big answer. It isn't. There are at least four distinct places a voter's influence gets lost, they fail independently, and **fixing one does nothing for the others**.*

*We add a cause he leaves implicit — **vote splitting** — and mark it plainly as ours. Two disclosures up front: Better Choices is an **advocacy organization** for [Consensus Choice](../../05_Ranked_Robin/01_Learn/ranked_robin_vs_consensus_choice.md), so we cite the paper for its framing, not as a neutral referee — and this library [leans STAR](../../01_STAR/01_Learn/STAR_start_here.md) and says so. The checks below cut in every direction, including at us.*

→ Related: [our voting system is broken](our_voting_system_is_broken.md) (the deeper *is it worth fixing?* argument) · [the spoiler effect](spoiler_effect.md) · [wasted votes](wasted_votes.md) · [advocacy organizations](advocacy_organizations.md) · [GLOSSARY](../GLOSSARY.md)

---

## The problem, in one sentence

**In many US districts, a sizeable minority of voters cannot influence who represents them — even when they vote sincerely.**

Not "their side loses." Something narrower and worse: the ballot they cast is structurally incapable of changing the outcome, no matter what they write on it. Below, four places that happens.

**On the numbering.** Causes **1**, **2** and **4** are Holliday's three, in his order — his third is our fourth. **Cause 3 is ours**, inserted where it belongs: it is the direct consequence of Cause 2 and the mechanism behind the "spoiler effects" in his title.

| | Cause | Where the influence is lost | What actually fixes it |
|---|---|---|---|
| **1** | The real decision happens in a **partisan primary** | Before your ballot exists | An **open qualifying round** — *and a decent method inside it* |
| **2** | You are allowed **one mark** | At the ballot | A ballot that records support for **more than one** candidate |
| **3** | **Vote splitting** *(ours)* | Between voters who agree | A ballot or count where backing an ally **costs your favorite nothing** |
| **4** | The rule **ignores preferences you expressed** | At the count | A count that reads the **whole ballot** — every pairing, or every score |

---

## Cause 1 — the real election happened in a primary you couldn't vote in

In a safe district the general election is a formality: whoever wins the dominant party's primary wins the seat. That primary is often closed to everyone else. A voter registered outside that party gets a ballot only for the round whose result was never in doubt.

This is the one cause that has **nothing to do with the counting rule**. It's about who is allowed in the room.

> **In the margin.** Unite America's October 2024 analysis: **87%** of US House races — **380 seats** — were effectively determined in primaries decided by **7%** of eligible voters (**18.1 million** people), leaving roughly **101 million** voters with no meaningful say. (169 of those members faced no primary opponent at all.) Source: [Unite America](https://www.uniteamerica.org/articles/analysis-87-of-u-s-house-elections-already-determined-in-primaries-by-just-7-of-americans) — an advocacy group for open primaries, cited here for its own arithmetic.

**The fix, and the part usually left out.** Open the qualifying round to every voter regardless of party. But "open" is only half of it: **the method inside the qualifying round decides whether the fix works.** This library measured it — a Choose-One top-4 primary discards the consensus candidate **17.3%** of the time; swapping the same round to Approval takes that to **0.4%**, and adding a fifth slot instead only gets to 11.8%. The method matters roughly forty times more than the number of slots.

→ [Does the qualifying round throw away the consensus winner?](../../method_comparisons/qualifying_round_primary_method.md) — 2,000 trials per cell, seeded and self-testing, with the caveats stated.

## Cause 2 — you are allowed one mark

[Choose-One / Plurality](plurality.md) records the smallest thing a voter can say: a single name. Everything else you think — that you'd happily accept the second candidate, that the third is intolerable — is never written down, so it cannot be counted. If your favorite can't win, your ballot carries no usable information at all.

> **In the margin.** Which is why, under Choose-One, so many voters don't vote sincerely in the first place: the fear of "wasting" a vote pushes them off their favorite before the count ever runs. That's [strategic voting](strategic_voting.md) as a *tax on honesty* — and the third of the four [senses of "wasted vote"](wasted_votes.md).

**The fix.** A ballot that lets you express support for more than one candidate: rank them, approve several, or score each 0–5. All three reforms in play here start with this same step.

## Cause 3 — voters who agree get split apart *(the cause we're adding)*

Causes 1, 2 and 4 are about an **individual** voter's influence. This one is about a **group**: several candidates who appeal to the same voters divide that pool between them, and a side that agrees loses to a side that doesn't. Under one mark, the more choices your side is offered, the worse your side does.

Three reasons it deserves its own line rather than being folded into Cause 2:

1. **It hits majorities, not just minorities.** The paper's problem statement is about "a sizeable minority." Vote splitting can hand the seat to a candidate that **two-thirds of voters rank last**. That's not a minority losing influence — it's a majority losing the election.
2. **It is the mechanism the title names.** "Spoiler effects" don't appear from nowhere; the [spoiler effect](spoiler_effect.md) *is* vote splitting with a name attached to the candidate who caused it. State the mechanism and the promise in the title becomes checkable.
3. **It works before election day, too.** Because splitting is predictable, allies get pressured to drop out and donors get told not to fund a "spoiler." The choice is removed from the ballot before you see it. Nothing in the tally records that loss.

Here it is, run. A progressive coalition holds a clear 66%, split across three candidates; the Conservative holds 34% alone:

```
[Vote-splitting check]
  Choose-One first choices: Conservative 34, Green 24, Labour 22, SocialDem 20
  Plurality winner: Conservative (34, 34.0%)
  Bloc 'Coalition' = Green, Labour, SocialDem: combined 66 (66.0%); winner Conservative is OUTSIDE it.
  => VOTE SPLITTING: the 'Coalition' bloc is an outright majority (66 vs
     Conservative's 34) but split across 3 candidates, so Conservative won
     Choose-One. STAR elected Labour.

[Condorcet Loser]
  Condorcet Loser: Conservative — loses every head-to-head matchup — elected by Choose-One (Plurality)!
```

Same ballots, scored instead of picked, elect Labour — who also happens to beat every other candidate head-to-head. Want the whole count? → [`01_political_left_split`](../../method_comparisons/split_voting/_main/_main_pages/01_political_left_split.md) ([`.yaml`](../../method_comparisons/split_voting/_main/01_political_left_split.yaml)). The progression through every method, on one set of ballots, is [the split-voting set](../../method_comparisons/split_voting/README.md).

**The fix — and the honest fine print.** A *ranked ballot alone does not remove this.* It has to be a ballot where supporting an ally costs your favorite nothing ([Approval](../../04_Approval/01_Learn/approval_voting.md), [STAR](../../01_STAR/01_Learn/STAR_start_here.md)), or a count that compares every pair directly ([Ranked Robin / Consensus Choice](../../05_Ranked_Robin/01_Learn/ranked_robin.md)). [RCV-IRV](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md) genuinely reduces the classic split — a trailing ally is eliminated and their ballots transfer — but its eliminations introduce [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) instead. And STAR keeps a narrow, self-inflicted [residual](../../01_STAR/01_Learn/properties_and_limits/residual_vote_splitting.md): a faction can still split itself if it refuses to use the score ballot honestly. How often the *setup* for splitting exists in real US elections — read carefully, both ways — is [here](../../method_comparisons/split_voting/how_often_does_vote_splitting_happen.md).

## Cause 4 — the rule ignores preferences you already expressed

Now suppose you got the better ballot and ranked everyone honestly. The count can still decline to read most of it.

Under [RCV-IRV](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md), a ballot's later rankings are consulted **only** if the candidates above them are eliminated. So if your favorite survives to the final round and loses there, your 2nd and 3rd choices were never counted — you filled in a ranked ballot and were counted as a Choose-One voter. At the other end, a ballot whose ranked candidates are all eliminated is [set aside mid-count](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) and stops mattering. Neither is a bug in the implementation; it's what the rule does.

> **In the margin — and in proportion.** This is real and predictable in close three-way races: [Burlington 2009](../../method_comparisons/burlington_2009/README.md) and [Alaska's 2022 special](../../06_Other/RCV_IRV/concepts/case_studies/RCV_IRV_alaska_2022.md) both elected someone a majority ranked below the eliminated moderate. It is also **rare**: Condorcet failures showed up in **2 of 182** US RCV elections (Graham-Squire & McCune, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075)). Overstating the frequency is the fastest way to lose a technical audience — see [false claims about RCV-IRV](../../06_Other/RCV_IRV/concepts/rcv_irv_false_claims.md), which grades the anti-IRV lines too.

**The fix.** Count the whole ballot. Either compare **every pair of candidates head-to-head**, so every voter's opinion about every matchup counts equally ([Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md), [Consensus Choice](../../05_Ranked_Robin/01_Learn/ranked_robin_vs_consensus_choice.md), and the [pairwise-ballot variant](condorcet/better_choices_pairwise_ballot.md) that prints the matchups on the ballot itself) — or **score every candidate** and finish with a majority runoff between the top two ([STAR](../../01_STAR/01_Learn/STAR_start_here.md)), which reads every score and then prints the head-to-head check on the result.

---

## What each reform actually fixes

The point of splitting the problem into causes is that the answer is a grid, not a winner. Read down the columns:

| | Open primary alone | Choose-One | RCV-IRV | Approval | Ranked Robin / Consensus Choice | STAR |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **1** Decision made in the primary | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **2** Only one mark allowed | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **3** Vote splitting | ❌ | ❌ | ⚠️ reduced; [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) instead | ✅ | ✅ | ✅ *(narrow [residual](../../01_STAR/01_Learn/properties_and_limits/residual_vote_splitting.md))* |
| **4** Preferences expressed but not read | ❌ | ❌ | ❌ | ⚠️ reads one bit per candidate | ✅ every pair | ✅ every score, then a runoff |

Two things fall out of that grid, and they're the reason the four-cause framing earns its keep:

- **No voting method fixes Cause 1, and no primary reform fixes Causes 2–4.** They're orthogonal. A jurisdiction can adopt a great method and still have every real decision made in a closed primary; it can open its primaries and still split the vote in both rounds. Reform packages that pair the two (Alaska's top-4, Better Choices' qualifying round + pairwise general) are pairing them *because* of this.
- **Cause 1's fix has a method-shaped hole in it.** An open primary counted by Choose-One reintroduces Cause 3 one round earlier — which is exactly what our [simulation measures](../../method_comparisons/qualifying_round_primary_method.md).

## What this framing still leaves out

Honesty about scope, since a four-item list invites the reading that it's complete:

- **Single-member districts.** Every cause above assumes one seat per district. Roughly half the electorate ends up represented by someone they voted against no matter how good the count is — the fix there is [electing more than one](electing_more_than_one.md) ([proportional STAR](../../03_STAR_PR/README.md)), not a better single-winner rule.
- **Districting itself.** Safe seats are partly drawn, not just sorted. That's upstream of everything on this page.
- **"Every voter matters" is a direction, not a state.** No method makes every ballot decisive — that's impossible, not a design failure. The precise, defensible claim is that these reforms remove *structural* powerlessness (the split, the discarded preference, the closed round), and that's plenty. → [wasted votes](wasted_votes.md), [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md).

## The one-liner

> **"Voters don't lose their influence in one place — they lose it in four. Closed primaries take it before the ballot exists, one mark takes it at the ballot, vote splitting takes it from voters who agree, and an elimination count takes it from preferences already written down. Any reform that fixes only one should say so."**

---

*Sources: Wesley H. Holliday, ["How to Make Every Voter Matter and Make Spoiler Effects Go Away"](https://www.betterchoices.vote/news/how-to-make-every-voter-matter-and-make-spoiler-effects-go-away), Better Choices for Democracy (advocacy — cited for its framing and its own proposal, not as a neutral referee; the three-cause structure and the problem statement are his, the prose and Cause 3 are ours) · [Unite America, "87% of U.S. House Elections Already Determined in Primaries"](https://www.uniteamerica.org/articles/analysis-87-of-u-s-house-elections-already-determined-in-primaries-by-just-7-of-americans), 8 Oct 2024 (advocacy — cited for its arithmetic) · Graham-Squire & McCune, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075) (the 182-election database) · all drop-rate and tabulation numbers are this library's own, reproducible from the linked files.*
