# Alaska's ranked-choice elections — the whole picture

*People (reasonably) get these tangled: **which** Alaska election was the famous "RCV broke" one? The **special** or the **general**? And didn't RCV work fine most of the time? This page is the map. Short version: Alaska has run many RCV races since 2022, and **exactly one** misfired — the August 2022 US House **special**. That's the one this repo models in depth; the rest are the honest backdrop that make it stand out.*

---

## How Alaska got RCV

Alaska voters passed **[Ballot Measure 2 (2020)](https://en.wikipedia.org/wiki/2020_Alaska_Measure_2)** (~50.6%), replacing party primaries + Choose-One with a **top-four nonpartisan primary** followed by an **RCV-IRV general election**, for all state and federal offices. It was **first used in 2022**. A 2024 measure to **repeal** it **failed by ~664 votes** (50.1% to keep) — so [Alaska kept RCV](https://alaskabeacon.com/2024/11/20/alaska-chooses-to-keep-ranked-choice-voting-begich-defeats-peltola-unofficial-results-show/) and used it again in 2024.

**"RCV" here means ranked ballots counted by instant runoff (IRV)** — the FairVote-style single-winner tabulation. Alaska's are single-winner races.

## The elections at a glance

| When | Race | Winner | Did RCV-IRV misfire? |
|---|---|---|---|
| **Aug 2022** | **US House — special** (Peltola / Begich / Palin) | **Peltola** | **YES — center squeeze.** Begich beat both head-to-head (the [Condorcet winner](../../topics/condorcet/)) but had the fewest first choices, so IRV eliminated him first. **← the case this repo models.** |
| Nov 2022 | US House — general (Peltola / Palin / Begich / Bye) | Peltola | **No.** Six months later the electorate had shifted; per Equal Vote's [Real RCV](https://realrcv.equal.vote/alaska22general), **Peltola was the Condorcet winner this time**, and IRV elected her. |
| Nov 2022 | US Senate (Murkowski / Tshibaka / Chesbro / …) | Lisa Murkowski | **No** — arguably RCV's best showing: the broadly-acceptable incumbent won by gathering cross-partisan second choices, an outcome a closed partisan primary might have denied her. |
| Nov 2022 | Governor | Mike Dunleavy | **No RCV rounds** — won an outright first-round majority, so no runoff was needed. |
| Nov 2022 | ~many state legislative races | (various) | No Condorcet failure reported. |
| **Nov 2024** | **US House** (Begich / Peltola / Howe) | **Begich** | **No** — the 2022 "victim" won cleanly this time ([51.3%](https://alaskabeacon.com/2024/11/20/alaska-chooses-to-keep-ranked-choice-voting-begich-defeats-peltola-unofficial-results-show/)), which also shows the 2022 special was a one-off, not a permanent distortion. |
| Nov 2024 | Ballot Measure 2 (repeal) | **Repeal failed** | RCV retained (50.1%). |

## The honest scorecard — credit where it's due

This is the part a fair critic must state out loud: **Alaska RCV mostly works.**

- The empirical study this repo scales its model from — **[Graham-Squire & McCune, arXiv:2301.12075](https://arxiv.org/abs/2301.12075)** — counted **13 Alaska RCV races in 2022 that actually reached a second (runoff) round**. Of those thirteen, **exactly one produced a Condorcet failure: the US House special.** The other twelve elected a candidate with no Condorcet objection.
- In the **2022 Senate race**, RCV is widely credited with a *better*, more representative result than the old system would have produced (a moderate incumbent surviving a same-party challenge by consolidating broad support).
- In **2024**, RCV ran again with **no reported Condorcet failure**, and Alaskans voted to keep it.

So the failures are **rare and specific**, not a constant. Across the whole national dataset, Condorcet failures showed up in only **two of 182** US RCV elections (Burlington 2009 and the Alaska 2022 special) — see the paper. Browse the ones that worked on Equal Vote's [Real RCV](https://realrcv.equal.vote) tool.

## So which one does this repo model, and why?

The **[August 2022 US House special](../../../method_comparisons/alaska_2022/README.md)** — because the *failure* is the teachable moment. We reproduce it as a runnable, four-count model (Plurality & IRV → Peltola; Ranked Robin & STAR → Begich, the Condorcet winner IRV cut), with a graduated explainer:

- **[101 — plain language](../../../method_comparisons/alaska_2022/alaska_101.md)** · **[201 — the vote math](../../../method_comparisons/alaska_2022/alaska_201.md)** · **[301 — every pathology + is this fair?](../../../method_comparisons/alaska_2022/alaska_301.md)**
- Prose write-up with real vote totals: **[Alaska 2022 — RCV-IRV case study](RCV_IRV_alaska_2022.md)**

## The takeaway — the fair version

The [center squeeze](../RCV_IRV_center_squeeze.md) is a **real, structural** flaw of IRV: it *can* eliminate the candidate a majority prefers, and in Alaska's August 2022 special it *did*, in a high-profile federal race. But it is **rare and conditional** — it only causes a wrong result when a genuine centrist Condorcet winner has too few first choices, which is *not* most elections (not even most Alaska ones).

So the honest case for [STAR](../../STAR_Voting/STAR_start_here.md) and [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md) is **not** "IRV always fails." It's: *IRV has a known, structural failure mode that has struck real elections — and methods that read the whole ballot avoid it entirely, at no cost to the races IRV already handles well.* Alaska is Exhibit A for both halves of that sentence.

---

*Sources: [Graham-Squire & McCune, arXiv:2301.12075](https://arxiv.org/abs/2301.12075) (the 182-election database; the 13 Alaska 2022 races; the two Condorcet failures) · [Alaska Beacon, Nov 2024](https://alaskabeacon.com/2024/11/20/alaska-chooses-to-keep-ranked-choice-voting-begich-defeats-peltola-unofficial-results-show/) (2024 House result + repeal outcome) · Equal Vote [Real RCV](https://realrcv.equal.vote) (per-election visualizations) · [Wikipedia: 2020 Alaska Measure 2](https://en.wikipedia.org/wiki/2020_Alaska_Measure_2) (neutral overview of the system).*
