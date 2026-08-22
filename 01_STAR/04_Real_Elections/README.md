# 01_STAR/04_Real_Elections — real BetterVoting races, read end to end

Constructed examples make one idea clear; **real elections** prove the method survives contact with real ballots. Every set here is a live [BetterVoting](https://bettervoting.com) race imported into this repo and reconciled line by line against the [LH engine](../../07_Concepts/tabulation_engines/LH_starvote/README.md) — so you can see both how a result *looks* in the BV interface and how it *tallies* in an independent implementation.

That reconciliation is also how this repo finds BetterVoting bugs: where the two disagree, the disagreement is the lesson.

Levels follow the [curriculum](../../07_Concepts/CURRICULUM.md): 🟢 101 · 🟡 201 · 🔴 301.

| Set | Level | What it shows |
|---|:--:|---|
| ["What Makes the Best Pet?"](pet_real_bv_election/README.md) | 🟡 201 | The whole pipeline on one race: 7 candidates, **461 ballots**, raw ballots → winner, read section by section. The worked example behind the [runoff percentages](../01_Learn/the_count/runoff_percentages.md) lesson. |
| [Runoff reversals on BV](runoff_reversal_bv_cases/README.md) | 🟡 201 | Real elections where the Scoring-Round leader **loses** the Automatic Runoff to the finalist more voters prefer — STAR's headline behavior, not a constructed one. Two-view: BV screenshots beside the engine report. |
| [Abstain, blank & zero handling](abstain_bugs/README.md) | 🟡 201 | Where BetterVoting and the engine **diverge**: BV counts an all-equal ballot (`0,0` *and* `5,5`) as an abstention, the engine counts an explicit score as a real vote. The visible symptom is BV's "0 tallied votes yet a winner" ([#884](https://github.com/Equal-Vote/bettervoting/issues/884)). |
| [Goodberry's Best Flavor 2026](goodberrys_best_flavor/README.md) | 🟢 101 | **Open now** — a live poll, not an import: ten frozen-custard flavors, paper ballots at the Cary NC shop plus a QR code, no seed ballots. The frozen export is the mint-time snapshot (zero votes), so this set is the *before* picture; re-freeze it when the poll closes and the reconciliation joins the rows above. |
| [Florida 2026 — four STAR races](florida_2026_star_poll/README.md) | 🟡 201 | A public poll runs the **2026 Florida statewide ballot** as four STAR races on one open, all-candidate field — the contest the closed partisan primary cannot hold. Small (25 ballots) and self-selected, so it settles nothing about Florida; what it shows is what the ballot *records*: an unaffiliated candidate placing 4th on secondary support, and a Senate runoff decided by **7 of 25 voters** because 18 scored both finalists the same. Also a live instance of the `0`-vs-blank abstention divergence in three races at once. |
| [Does scale usage matter? (pres24)](pres24_range_usage/README.md) | 🔴 301 | **2,772 real ballots**, 8 candidates — the public 2024 presidential poll, imported to answer a live question: 14% of ballots never used both ends of the 0–5 scale. Reproduces the figure, then shows the winner is invariant (the scoring leader is also the Condorcet winner) while the *second* finalist slot is a coin flip from sampling noise. Also finds the flagged ballots carry **more** runoff weight than average. |

---

**Related:** the constructed teaching progression → [02_Examples](../02_Examples/README.md) · the tie behaviors these races run into → [03_Criteria](../03_Criteria/README.md) · every BV-backed case in the library → [the BV registry](../../07_Concepts/YAML_test_case_index/BV_registry.md).
