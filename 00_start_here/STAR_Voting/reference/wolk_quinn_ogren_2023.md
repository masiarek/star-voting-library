# The foundational STAR paper — Wolk, Quinn & Ogren (2023), claim-checked

*The peer-reviewed paper that introduced the two metrics this library leans on — **Voter Satisfaction Efficiency (VSE)** and **Pivotal Voter Strategic Incentive (PVSI)** — and made the academic case for STAR. Because the authors are STAR advocates, this page runs it through the same [claim-check recipe](../../../method_comparisons/fairvote_star_whitepaper/) we apply to every camp: concede the kernel, test what's testable, flag the overreach, disclose the lean — and let the fairness cut against STAR too.*

**Level: 301 → 401.** · Full text (open access): **[DOI 10.1007/s10602-022-09389-3](https://doi.org/10.1007/s10602-022-09389-3)** · local copy [`wolk_quinn_ogren_2023_star_vse.pdf`](wolk_quinn_ogren_2023_star_vse.pdf).

> **Wolk, S., Quinn, J. & Ogren, M. (2023).** "STAR Voting, equality of voice, and voter satisfaction: considerations for voting method reform." *Constitutional Political Economy* **34(3): 310–334.** Accepted 24 Dec 2022, published 20 Mar 2023. Open access (CC BY). Correction notice: 10.1007/s10602-023-09426-9.

---

## Why this paper matters to the library

Two numbers used throughout this repo trace back to here:

- **VSE** — the utilitarian-accuracy score behind "STAR tops the accuracy charts" (100% = always elect the utility-maximizing winner, 0% = a random winner). It is the modern form of [Bayesian Regret](../../topics/what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret).
- **PVSI** — the *Pivotal Voter Strategic Incentive*: how much a pivotal voter gains on average by voting strategically rather than honestly. Near **0%** means strategy rarely pays; **negative** means it backfires more often than it works. This is the peer-reviewed source behind the repo's "**STAR ≈ 1:1, IRV ≈ 3:1, Plurality ≈ 17:1** backfire ratios."

Until now the library used these figures while citing only a project website. This page anchors them to the peer-reviewed original.

## What the paper actually claims

1. **STAR = a 0–5 score ballot + an automatic top-two runoff** — designed to capture *both* preference order and preference strength, to be **summable** (unlike IRV), and to run on existing machines by addition.
2. **Reject pure pass/fail criteria; measure frequency × severity instead.** Following [Arrow (1950)](../../topics/what_makes_a_voting_method_good.md), every method fails *some* criterion, so binary checklists are "more divisive than constructive." Their alternative is statistical: build a generative electorate model, simulate, and measure how *often* and how *badly* each pathology bites.
3. **Favorite Betrayal (FB) and Later-No-Harm (LNH) are incompatible**, so a method should maximize both statistically rather than pass one and fail the other badly. STAR keeps FB-resistance and gives up LNH; **IRV does the opposite — and, to pass LNH, it ignores down-ballot preferences, which (per Dempsey 2018) is precisely why it cannot eliminate vote-splitting or the [center-squeeze](../../RCV_IRV/RCV_IRV_center_squeeze.md) spoiler.**
4. **The Equality Criterion** (their framing of one-person-one-vote): for any ballot there exists an opposite ballot that exactly cancels it. **Approval, Score, Smith/Minimax and STAR pass; Plurality and IRV fail.** They tie this to *Wesberry v. Sanders* and show it implies the weak mutual-majority criterion.
5. **Results.** On a clustered-spatial model (6 candidates, 101–5001 voters): **STAR and Smith/Minimax deliver the highest VSE** of all methods tested, Approval close behind — roughly **STAR ≈ Smith/Minimax > Approval Top Two > Approval > IRV > Plurality Top Two > Plurality**. On strategy (PVSI): STAR's only weak incentive (~2%) is to exaggerate scores *while keeping honest preference order*; **all dishonest STAR strategies — favorite betrayal, burial, bullet voting — are strongly disincentivized.** IRV's *most*-incentivized strategy is favorite betrayal; Plurality incentivizes it at ~14%; Approval's strongest is threshold-setting at ~10%.

## The kernel — what's solid (concede it)

- **Genuinely peer-reviewed**, in an economics journal, and **open access** — a real citable anchor, not a campaign PDF.
- **VSE and PVSI are rigorous, reusable and model-transparent.** Appendix B runs robustness checks across models and parameters, and the Python code is supplied. The VSE ordering (cardinal/Condorcet methods over IRV over Plurality) is **robust and independently corroborated** — see [expert consensus & IRV](../../topics/expert_consensus_and_irv.md).
- **Unusually candid about its own bias risk.** The authors state they "have done our best to avoid creating a model biased in favor of STAR," and note that Quinn's VSE work *predated* his STAR activism — he had **expected the data to favour Bucklin-style Majority Judgment, not STAR**. They deliberately chose a **clustered spatial model** so that Condorcet cycles occur at a *realistic* rate: neither the flood produced by [impartial culture](../../topics/election_simulation_models.md) nor the near-zero of a plain [spatial model](../../topics/spatial_voting_model.md). That is exactly the methodology this repo argues for.
- **The vote-splitting / center-squeeze critique of IRV is correct and load-bearing** — and it has actually happened: [Burlington 2009](../../../method_comparisons/burlington_2009/), [Alaska 2022](../../../method_comparisons/alaska_2022/).

## Test it — the runnable companions here

| The paper's claim | Run it in this library |
|---|---|
| STAR reads strength *and* order — three "winners" can differ | [Three notions of winner](../properties_and_limits/STAR_three_winner_notions.md) |
| IRV's center-squeeze spoiler, on real ballots | [Center squeeze](../../RCV_IRV/RCV_IRV_center_squeeze.md) · [Alaska 2022](../../../method_comparisons/alaska_2022/) · [Burlington 2009](../../../method_comparisons/burlington_2009/) |
| The FB/LNH tradeoff — and that STAR is *not* FB-proof | [Favorite betrayal](../properties_and_limits/favorite_betrayal_voting_301.md) · [FBC simulation](../../../06_Other/simulations/README.md) |
| STAR ≈ Smith/Minimax at the top → so where do they *disagree*? | [Ranked Robin](../../RCV_Ranked_Robin/README.md) · [30 STAR≠RR divergence samples](../../../05_Ranked_Robin/star_vs_rr_divergence/) |
| VSE/PVSI are model-dependent | [Election simulation models](../../topics/election_simulation_models.md) · [the simulations](../../../06_Other/simulations/README.md) |

## Read it critically — overreach, and the lean

- **Disclose the lean.** Lead author **Sara Wolk directs the Equal Vote Coalition**, the STAR advocacy organisation; Quinn and Ogren are longtime cardinal-voting researchers. This is *advocates presenting their own method*. Their candour (above) softens that but does not erase it.
- **The precision is oversold; the ordering is not.** Headline VSE percentages move with the voter model, candidate count and how strategic voters are (Appendix B). The **ranking** is robust; the **exact figures** are not constants — the same caution the [scorecard](../../../method_comparisons/single_winner_scorecard/README.md) already prints.
- **STAR does not strictly dominate — and the paper's own data says so.** On their results a **Condorcet method (Smith/Minimax) ties STAR on VSE and beats it on strategy-resistance**: Smith/Minimax disincentivises strategic voting *across the board*, while STAR retains a small (~2%) exaggeration incentive. The honest reading is "STAR is **co-best**, alongside a good Condorcet method," not "STAR wins outright." That is precisely the [STAR-vs-Ranked-Robin](../../RCV_Ranked_Robin/RCV_RR_honest_limits.md) tension this library teaches — and here it is a point *for* Ranked Robin.
- **The "Equality Criterion" is an advocate-introduced yardstick.** Worth the [criterion-built-to-fit-the-method](../../../method_comparisons/ordered_majority_rule/) check. In fairness it is **not** a mirror reverse-engineered to single out STAR — it is a reasonable vote-cancellation property, and several methods pass it including a Condorcet one. But it originates with the proponents, so cite it as *their* framing, not a settled field-standard criterion.
- **The infographic ratios are not verbatim in the paper.** The familiar "1:1 / 2.6:1 / 2.7:1 / 17.8:1" is Equal Vote's *works : backfires* presentation built on the VSE simulator; the paper itself reports **PVSI percentages** (STAR ~2%, Approval ~10%, Plurality ~14%, IRV favourite-betrayal-incentivised). Same underlying simulation — but attribute the ratio form to the infographic and the percentages to the paper.

## The honest bottom line

A strong, genuinely peer-reviewed contribution that hands the field two durable metrics and argues the accuracy-plus-strategy-resistance case for STAR with more candour about its own lean than most advocacy writing. Its firmest results — **cardinal and Condorcet methods beat IRV and Plurality on utilitarian accuracy, and STAR strongly disincentivises dishonest voting** — hold up and are corroborated elsewhere. Its softest spots are the usual ones: single-decimal VSE precision reads as more certain than a model-bound simulation can be, and the paper's own numbers show a good **Condorcet method matching or edging STAR** — so the fair takeaway is *STAR is co-best, not uniquely best*.

---

*See also: [STAR's honest limits](../properties_and_limits/STAR_honest_limits.md) · [What makes a good winner?](../../topics/what_makes_a_good_winner.md) · [In memoriam, Jameson Quinn](../../topics/in_memoriam_jameson_quinn.md) · [STAR resources](STAR_resources.md).*
