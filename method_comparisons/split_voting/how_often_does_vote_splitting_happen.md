# How often does vote splitting actually happen?

*The rest of this folder shows **what** vote splitting is, in elections built to make it visible. This page answers the other question a skeptic will ask first: **how often does it happen in real American elections?** There is a published count — and reading it honestly means separating what it proves from what it merely flags.*

→ Concept: [the spoiler effect](../../00_start_here/topics/spoiler_effect.md) · [Choose-One / Plurality](../../00_start_here/topics/plurality.md) · how to read failure rates fairly: [severity × frequency](../paradoxes_and_whoops/reading_these_fairly.md)

---

## The number

The Center for Election Science's **[*America (Mis)Represented* — 2022 Election Report](https://electionscience.org/research-hub/2022-america-(mis)represented-report)** reviewed **all 5,662 national primary elections** of the 2022 cycle — congressional, statewide office, and state legislative — and found that **approximately 11.9%** had multiple candidates and a winner who did not receive a majority. The report's data source is its own **Vote Split Elections Project (2022)**.

Its state breakdown (limited to states that ran all three election types):

| State | Elections | Pct. vote split |
|---|--:|--:|
| New Hampshire | 232 | **44.8%** |
| Arizona | 75 | 44.0% |
| Nebraska | 33 | 33.3% |
| California | 160 | 32.5% |
| Nevada | 36 | 30.6% |

The report also notes that in the **New Hampshire State House**, candidates advanced to the general election with **as little as 8.8%** of the primary vote — because those are multi-seat districts where voters select several candidates.

> **Source lean, disclosed** (house rule): CES is the national advocacy organization for [Approval Voting](../../00_start_here/Approval_Voting/approval_voting.md) — see [advocacy organizations](../../00_start_here/topics/advocacy_organizations.md). The *count* is a straightforward tabulation of public results and there's no reason to doubt it. The *framing* — calling every such race a "vote split election" — is where an advocacy report and a teaching library should part company, and the rest of this page is why.

## The definition worth borrowing

One thing the report gets exactly right, and states more crisply than most sources: **vote splitting is the mechanism; the [spoiler effect](../../00_start_here/topics/spoiler_effect.md) is the outcome it produces.** Votes divide among candidates who, combined, would have been a majority — and *that division* is what lets a less-preferred candidate win. Keeping the two words distinct is worth doing, and this repo now does it the same way.

Note also what the arithmetic of their test really says. "Winner under 50%" and "the losers combined are a majority" are *the same statement*. So the measure is well-defined and consistent with the prose definition.

## What the 11.9% does and doesn't prove

**It does prove exposure.** In one out of every eight or nine 2022 primaries, the winner took office (or the nomination) without majority support, and the losing candidates' voters together outnumbered the winner's. Under a one-mark ballot, that is precisely the configuration in which a spoiler *can* operate. Nobody has to speculate about whether the setup occurs — it occurs constantly.

**It does not prove a flipped outcome.** "The losers sum to more than the winner" is arithmetic. "Those voters would have united behind one of them" is a claim about *preferences* — and a choose-one ballot never collects preferences. The report's own Figure 4 illustrates a 19% / 38% / 43% race and says the 19% and 38% candidates "share similar characteristics," so the split handed it to the 43%. That may well be true of that example, but **the vote totals alone cannot establish it.** Three mutually hostile candidates produce the same three numbers.

Two runnable counter-examples make the gap concrete.

### Counter-example 1 — a 41% winner that nothing spoiled

44 residents choose a street tree. First choices: **Aspen 18 (41%)**, Birch 14, Cedar 12. The winner is under half and the losers combined (26) are a majority, so this race counts as a "vote split election." Read the whole ballot and nothing was split:

```
--- Runoff (Preference) Matrix ---
                 |   * Aspen    |  * Birch    |    Cedar    |
-------------------------------------------------------------
       * Aspen > |     ---      |30 -  0 - 14 |32 -  0 - 12 |
       * Birch > | 14 -  0 - 30 |    ---      |32 -  0 - 12 |
         Cedar > | 12 -  0 - 32 |12 -  0 - 32 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Aspen — matches the STAR winner

Scoring Round
   Aspen         -- 180 -- First place
   Birch         -- 142 -- Second place
   Cedar         --  74

Automatic Runoff Round
   Aspen         -- 30 -- First place
   Birch         -- 14
 Aspen wins.
   Voters with a preference: 44 of 44 (no Equal Support).
   Aspen 30 (68%) vs Birch 14 (32%); majority = 23.
```

[STAR](../../00_start_here/STAR_Voting/STAR_start_here.md), [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/why_ranked_robin.md) and [RCV-IRV](../../00_start_here/RCV_IRV/RCV-IRV-Hare.md) (Aspen 18 → 30 after Cedar's transfers) all elect Aspen — the same candidate Choose-One elected on 41%. The race was *exposed* to vote splitting; the outcome was not *changed* by it.

→ Source: [`06_sub_majority_not_spoiled.yaml`](_main/06_sub_majority_not_spoiled.yaml) · full report: [page](_main/_main_pages/06_sub_majority_not_spoiled.md) · [`_tabulated`](_main/_main_tabulated/06_sub_majority_not_spoiled_tabulated.txt)

Now contrast [`01_political_left_split.yaml`](_main/_main_pages/01_political_left_split.md), where a 34% winner *does* hide a flipped result — a candidate two-thirds of voters ranked last. **Same arithmetic signature, opposite verdict.** The screening test cannot tell these two races apart; only the fuller ballot can.

### Counter-example 2 — the multi-seat ceiling

The New Hampshire figure needs a second look, and the report itself supplies the reason: NH State House districts elect several members, and voters mark several names. **With k marks per voter, k × voters marks are cast in total, so no candidate can exceed 1/k of the votes cast** — 33% at 3 seats, 25% at 4, 9% at 11 — no matter how universally loved they are.

So in a multi-seat block-vote race, a sub-majority winner isn't evidence of anything. Here 30 voters mark 3 of 5 names, and **Alice is on every single ballot** — literal unanimity:

```
--- Block Voting (plurality-at-large) — 3 winners ---
 Tabulating 30 ballots (3 votes/voter).

Votes (most votes fill the seats):
   Alice    30  <- Elected
   Bruno    22  <- Elected
   Cleo     20  <- Elected
   Dev      10
   Esme      8
```

90 votes cast; Alice holds 30 of them — **33.3%**, her mathematical maximum. A rule that flags every leader under 50% flags this race, and every other multi-seat one, unanimity included. That is a denominator artifact. Since New Hampshire's 232 elections top the table and its multi-seat House primaries are a large share of them, at least part of that 44.8% is measuring seat count, not splitting.

→ Source: [`mmp_majority_ceiling.yaml`](../multi_member_plurality/cases/mmp_majority_ceiling.yaml) · full report: [page](../multi_member_plurality/cases/cases_pages/mmp_majority_ceiling.md) · [`_tabulated`](../multi_member_plurality/cases/cases_tabulated/mmp_majority_ceiling_tabulated.txt)

And note this cuts *against* block voting too, not for it: the test is blind to that method's actual pathology, which is a bare majority **sweeping every seat** ([`mmp_block_voting.yaml`](../multi_member_plurality/cases/cases_pages/mmp_block_voting.md) — a 60/40 electorate takes 3–0). The metric misses the real failure while flagging the healthy case.

## Two more things to keep straight

- **The denominator is primaries, not all elections.** The 11.9% is 11.9% *of 2022 primaries*; the report's gloss "about one in ten national elections" quietly drops the qualifier. Primaries are the races **most** prone to splitting — crowded fields, no party label to guide voters — so this is close to an upper bound, not a general-election rate.
- **Rarity cuts both ways, and we apply it symmetrically.** This library states rarity when it counts against our preferred conclusion — [2 Condorcet failures in 182 real IRV elections](../../00_start_here/RCV_IRV/), [cycles at ~1–5%](../../00_start_here/topics/strategic_pathologies.md). The same discipline applies here: report the honest measure and say what it measures.

## So what should we say?

Something narrower than the report, and more defensible:

> In roughly **one in eight** 2022 US primaries, the winner had no majority and the losers combined did. Choose-One cannot tell us how many of those were genuinely spoiled, **because the ballot never asked.** Every method in this library can tell us — which is itself the argument.

That last clause is the real finding. The reason "how often does vote splitting change results?" has no clean empirical answer is that the ballot in near-universal US use **destroys the evidence needed to answer it.** A [STAR](../../00_start_here/STAR_Voting/STAR_start_here.md) or ranked ballot produces a public record from which the counterfactual is directly checkable — as [Burlington 2009](../burlington_2009/) and [Alaska 2022](../alaska_2022/) both were, precisely because those elections collected more than one mark.

---

**See also:** [the split-voting demo set](README.md) · [minority winner](../minority_winner/README.md) — the canonical 34% case · [the pineapple progression](../minority_winner_progression/README.md) — 34% → 25% → 11% as the field grows · [Block, Limited & SNTV](../multi_member_plurality/multi_member_plurality.md)

# file: how_often_does_vote_splitting_happen.md
