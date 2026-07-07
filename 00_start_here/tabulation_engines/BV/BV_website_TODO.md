# BetterVoting — website TO-DO (manual / UI testing backlog)

Repo-native backlog of **BetterVoting website / UI** tasks — things to test, learn, or verify on the live app that don't have a YAML/tabulation home. (Tabulation *cases* live in the auto-generated [BV registry](../../YAML_test_case_index/BV_registry.md); this page is for the hands-on UI work that the registry can't capture — complements the Google-Sheet QA, but versioned here with the docs.)

## Open

### Districts / precincts — learn the data-entry flow, then BV-back the summability demo
BetterVoting **supports districts** (this was simply never tested from our side — an earlier note wrongly assumed BV models only a single electorate). Learning the district data-entry flow would unlock a **live, BV-backed** version of the [summability demo](../../../method_comparisons/summability_demo/):

- **Learn / test:** how district data is entered in the BV builder (per-district ballot entry? a district field on each ballot? assignment after casting?), whether results expose **per-district subtotals**, and whether the combined tally is exactly their sum.
- **Then demonstrate:** enter District A and District B; show STAR's published score totals **+ pairwise matrix add up** to the combined result (summable), while the IRV race's district winners (B, B) **don't predict** the merged winner (B eliminated) — summability, live.
- **Then promote:** if it works, make it a BV-backed case (District A / District B / Combined), freeze the export, and drop the screenshots into the [summability hub](../../topics/summability/) — adding the live BV dimension the [`summability_demo`](../../../method_comparisons/summability_demo/) currently lacks (today it's LH-engine + arithmetic only).
- **Refs:** [summability topic hub](../../topics/summability/) · [summability_demo](../../../method_comparisons/summability_demo/) · creation tool: [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.md)

## Done

*(none yet)*
