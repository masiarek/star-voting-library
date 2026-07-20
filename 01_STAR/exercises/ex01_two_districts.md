# Exercise 1 — Two districts, one mayor

*A city elects its mayor with STAR Voting. Out of curiosity, each of its two districts also runs the count on just its own nine ballots. West District's winner: **Avery**. East District's winner: **Avery**. The city's winner: work it out below — and write your prediction down first.*

**▶ Live on BetterVoting:** West [vote](https://bettervoting.com/d3b9wc) · **[results ↗](https://bettervoting.com/d3b9wc/results)** · East [vote](https://bettervoting.com/rhbfj7) · **[results ↗](https://bettervoting.com/rhbfj7/results)** · Combined [vote](https://bettervoting.com/923q3d) · **[results ↗](https://bettervoting.com/923q3d/results)** (elections `d3b9wc` / `rhbfj7` / `923q3d`, Test IDs BV2188–90; each also runs a **Ranked Robin** race on the same opinions — see "What about Elena?" below).

**You practice:** the scoring round · how the runoff pairing is chosen · the **consistency** criterion ([glossary](../../00_start_here/GLOSSARY.md)) — and why it is *not* the same thing as [summability](../../00_start_here/topics/summability/README.md).

Work each part on paper before opening its solution. The YAML files at the bottom are the same elections in runnable form; their `expected_winners` answer keys are regression-tested, and each `_tabulated` mirror is the full audit report.

## The ballots

Eighteen voters, nine per district, scores 0–5. Each district has three ballot styles (rows are candidates, columns are voter blocs):

**West District (9 ballots):**

| | ×5 voters | ×3 voters | ×1 voter |
|---|:---:|:---:|:---:|
| **Avery** | 3 | 5 | 5 |
| **Blake** | 3 | 5 | 3 |
| **Carmen** | 4 | 3 | 3 |
| **Diego** | 0 | 0 | 0 |
| **Elena** | 5 | 0 | 0 |

**East District (9 ballots)** — the same three styles with **Blake and Diego trading places**:

| | ×5 voters | ×3 voters | ×1 voter |
|---|:---:|:---:|:---:|
| **Avery** | 3 | 5 | 5 |
| **Blake** | 0 | 0 | 0 |
| **Carmen** | 4 | 3 | 3 |
| **Diego** | 3 | 5 | 3 |
| **Elena** | 5 | 0 | 0 |

## Your task

- **(a)** Tabulate West District alone — scoring round, then the automatic runoff. Who wins?
- **(b)** Tabulate East District alone. Who wins?
- **(c)** Both districts agree. Before computing anything: **write down your prediction** for the combined 18-ballot election, and how confident you are.
- **(d)** Tabulate all 18 ballots together. What changed — and at exactly which step?
- **(e)** Explain why plain **Score voting** (just add the points, highest total wins) could never behave this way, however you slice the electorate. Name the criterion.
- **(f)** *Bonus:* in the West runoff, only 1 ballot of 9 counted toward either finalist. Why is that correct, not a bug?

## Solutions

<details>
<summary><b>(a) West District</b></summary>

Score totals: Avery 5×3+3×5+1×5 = **35**, Blake 5×3+3×5+1×3 = **33**, Carmen 5×4+3×3+1×3 = **32**, Elena 5×5 = **25**, Diego **0**. Avery and Blake advance — and eight of the nine ballots score them *identically* (3-3 or 5-5), so the runoff is decided by the one voter who told them apart:

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Avery         -- 35 -- First place
   Blake         -- 33 -- Second place
   Carmen        -- 32
   Elena         -- 25
   Diego         --  0
 Avery and Blake advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Avery         -- 1 -- First place
   Blake         -- 0
   Equal Support -- 8
 Avery wins.
   Voters with a preference: 1 of 9 (8 Equal Support).
   Avery 1 (100%) vs Blake 0 (0%); majority = 1.
```

**West District: Avery.**

</details>

<details>
<summary><b>(b) East District</b></summary>

East is West with Blake and Diego trading places, so the arithmetic is identical with Diego in Blake's role: Avery **35**, Diego **33**, Carmen **32**, Elena **25**, Blake **0**. Avery vs Diego in the runoff; again 8 Equal Support ballots and one decided voter.

**East District: Avery** (runoff 1–0 over Diego).

</details>

<details>
<summary><b>(c) The prediction</b></summary>

There is no safe prediction — that is the exercise. Avery just won *both* districts with the *same* score total, so "Avery, obviously" feels forced. If you wrote that down with high confidence, part (d) is for you.

</details>

<details>
<summary><b>(d) The combined city — the winner flips</b></summary>

Line up the score totals and the flip announces itself:

| | West | East | **City** |
|---|:---:|:---:|:---:|
| **Avery** | 35 | 35 | **70** |
| Blake | 33 | 0 | 33 |
| **Carmen** | 32 | 32 | **64** |
| Diego | 0 | 33 | 33 |
| Elena | 25 | 25 | 50 |

Each district's **runner-up was local**: Blake's 33 points exist only in West, Diego's only in East. Carmen's 32-per-district was never enough to make a district runoff — but citywide her 64 is second only to Avery's 70. The runoff pairing changes from "Avery vs a local sidekick" to **Avery vs Carmen**, and that head-to-head was never Avery's: the two Elena blocs (10 of the 18 voters) all score Carmen 4 > Avery 3.

```text
Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Carmen        -- 10 -- First place
   Avery         --  8
   Equal Support --  0
 Carmen wins.
   Voters with a preference: 18 of 18 (no Equal Support).
   Carmen 10 (56%) vs Avery 8 (44%); majority = 10.
```

The engine also prints its [Runoff Reversal] block — Avery topped the scores, Carmen won the runoff — with the standard note that this is STAR working as designed, not a malfunction.

**The city: Carmen.** Avery won every district and lost the whole. The step that broke was not the addition (Avery still leads the citywide scores) — it was **who advances**: "second place" is not an additive fact.

</details>

<details>
<summary><b>(e) Why Score voting can't do this — the consistency criterion</b></summary>

This is the **consistency** criterion (also *join-consistency* or *reinforcement*): if every part of an electorate separately elects X, the combined electorate must elect X. Plain Score passes it by arithmetic: the city total is exactly the sum of the district totals, so a candidate who leads every district's sum leads the citywide sum — here Score elects Avery in West (35), in East (35), and in the city (70), unbothered. A classical result (H. P. Young) says essentially that only point-summing rules have this property; anything with a runoff, an elimination, or a pairwise stage — STAR, RCV-IRV, top-two runoffs, every Condorcet method — can fail it, because a *non-additive* question ("who is second?", "who survives this round?") sits between the ballots and the winner.

Two honest cautions before this becomes a talking point:

- **This is not a summability failure.** STAR remains fully [precinct-summable](../../00_start_here/STAR_Voting/properties_and_limits/STAR_summability.md): score totals and the [preference matrix](../../00_start_here/GLOSSARY.md) add across precincts, and officials run the two rounds *once* on the summed tallies. Nobody tabulates a citywide STAR seat district-by-district. What fails is only the *inference* "won every district ⇒ wins the whole."
- **What the criterion actually threatens is the headline.** "She carried both districts and still lost!" is a real communications liability after a close election — this exercise is the worked answer to it: carrying a district means winning *that district's runoff pairing*, and the pairing itself is what changed.
- **The paradox has a catalog page and an IRV-side sibling.** The general phenomenon is Felsenthal's *multiple-districts / reinforcement* paradox — see [the catalog page](../../00_start_here/voting_paradoxes/multiple_districts.md) — and the repo already runs the classic IRV-side demonstration live ([Felsenthal's reinforcement trio](../../method_comparisons/felsenthal_paradoxes/README.md), BV2147–49), where plurality-with-runoff commits the paradox and STAR happens to stay consistent. This exercise's trio (BV2188–90) is the other shoe: the constructive proof that STAR is not reinforcement-proof either.

</details>

<details>
<summary><b>(f) Bonus — the 1-of-9 runoff</b></summary>

Eight West ballots score the two finalists identically (the ×5 bloc gives 3-3, the ×3 bloc gives 5-5). They count at full weight in the scoring round — they are much of *why* Avery and Blake are the finalists — but in a head-to-head between equals they have no preference to give: they are **Equal Support**, not discounted and not "lost." The runoff summary line is built to self-reconcile so this never looks like missing votes: `Voters with a preference: 1 of 9 (8 Equal Support)`. See [Two Denominators, One Winner](../../00_start_here/STAR_Voting/the_count/runoff_percentages.md).

</details>

## What about Elena?

The on-screen report's `[Divergence from STAR]` block will have already whispered that something else is going on:

```text
[Divergence from STAR]
  STAR                   = Carmen
  Choose-One (Plurality) = Elena   (differs from STAR)
  RCV-IRV                = Elena   (differs from STAR)
  Approval               = Avery   (differs from STAR)
  RCV-RR (Condorcet)     = Elena   (differs from STAR)
```

Elena is the *first choice* of 10 of the 18 voters and the Condorcet winner (she beats every rival head-to-head), yet she finishes third on points: her supporters also scored Carmen generously (4) and Avery moderately (3), while her opponents gave her straight 0s. So this one engineered electorate splits the three defensible notions of "best winner" three ways — Score says Avery, majority/Condorcet logic says Elena, STAR's broad-compromise runoff says Carmen. Which notion *should* prevail is its own lesson: [three winner notions](../../00_start_here/STAR_Voting/properties_and_limits/STAR_three_winner_notions.md). The lesson *here* is narrower and method-internal: STAR's own answer changed when the electorate was sliced.

The live BetterVoting trio makes Elena visible too: each election carries a second race — the same opinions cast as ranked ballots (equal rankings allowed) under Ranked Robin — and Elena wins it 4–0 in West, East, and the city alike.

## Reading this fairly

A classroom construction, and it shows: mirror-image districts, three ballot styles, and (as the engine's own caveat notes) every ballot carrying tied scores somewhere. It demonstrates the *mechanism* of a consistency failure honestly; it says nothing about *frequency* in real electorates. Every method fails something — apply [the four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) before turning any single construction into a verdict, and see [STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md) for the balanced scorecard.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex01_district_west.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex01_district_east.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex01_district_combined.yaml
```

Sources: [ex01_district_west.yaml](cases/ex01_district_west.yaml) · [ex01_district_east.yaml](cases/ex01_district_east.yaml) · [ex01_district_combined.yaml](cases/ex01_district_combined.yaml). Full audit reports: [west](cases/cases_tabulated/ex01_district_west_tabulated.txt) · [east](cases/cases_tabulated/ex01_district_east_tabulated.txt) · [combined](cases/cases_tabulated/ex01_district_combined_tabulated.txt).

---

**Where these ballots come from.** Adapted (candidates renamed, prose our own) from a worked example published on [RangeVoting.org](https://rangevoting.org) — a Score-voting advocacy site, so its framing favors Score; the arithmetic is method-neutral — and posed as a districts exercise in Brendan W. Sullivan, *An Introduction to the Math of Voting Methods* (619 Wreath Publishing, 2022), ch. 5, a method-neutral general-education textbook whose practice-problems-with-solutions format this exercises set borrows.

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex01_two_districts.md
