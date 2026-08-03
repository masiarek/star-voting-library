# 01_STAR/04_Real_Elections — real BetterVoting races, read end to end

Constructed examples make one idea clear; **real elections** prove the method survives contact with real ballots. Every set here is a live [BetterVoting](https://bettervoting.com) race imported into this repo and reconciled line by line against the [LH engine](../../07_Concepts/tabulation_engines/LH_starvote/README.md) — so you can see both how a result *looks* in the BV interface and how it *tallies* in an independent implementation.

That reconciliation is also how this repo finds BetterVoting bugs: where the two disagree, the disagreement is the lesson.

Levels follow the [curriculum](../../07_Concepts/CURRICULUM.md): 🟢 101 · 🟡 201 · 🔴 301.

| Set | Level | What it shows |
|---|:--:|---|
| ["What Makes the Best Pet?"](pet_real_bv_election/) | 🟡 201 | The whole pipeline on one race: 7 candidates, **461 ballots**, raw ballots → winner, read section by section. The worked example behind the [runoff percentages](../01_Learn/the_count/runoff_percentages.md) lesson. |
| [Runoff reversals on BV](runoff_reversal_bv_cases/) | 🟡 201 | Real elections where the Scoring-Round leader **loses** the Automatic Runoff to the finalist more voters prefer — STAR's headline behavior, not a constructed one. Two-view: BV screenshots beside the engine report. |
| [Abstain, blank & zero handling](abstain_bugs/) | 🟡 201 | Where BetterVoting and the engine **diverge**: BV counts an all-equal ballot (`0,0` *and* `5,5`) as an abstention, the engine counts an explicit score as a real vote. The visible symptom is BV's "0 tallied votes yet a winner" ([#884](https://github.com/Equal-Vote/bettervoting/issues/884)). |

---

**Related:** the constructed teaching progression → [02_Examples](../02_Examples/README.md) · the tie behaviors these races run into → [03_Criteria](../03_Criteria/README.md) · every BV-backed case in the library → [the BV registry](../../07_Concepts/YAML_test_case_index/BV_registry.md).
