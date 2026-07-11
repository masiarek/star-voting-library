# BetterVoting — website TO-DO (manual / UI testing backlog)

Repo-native backlog of **BetterVoting website / UI** tasks — things to test, learn, or verify on the live app that don't have a YAML/tabulation home. (Tabulation *cases* live in the auto-generated [BV registry](../../YAML_test_case_index/BV_registry.md); this page is for the hands-on UI work that the registry can't capture — complements the Google-Sheet QA, but versioned here with the docs.)

## Open

### Districts / precincts — learn the data-entry flow, then BV-back the summability demo
BetterVoting **supports districts** (this was simply never tested from our side — an earlier note wrongly assumed BV models only a single electorate). Learning the district data-entry flow would unlock a **live, BV-backed** version of the [summability demo](../../../method_comparisons/summability_demo/):

- **Learn / test:** how district data is entered in the BV builder (per-district ballot entry? a district field on each ballot? assignment after casting?), whether results expose **per-district subtotals**, and whether the combined tally is exactly their sum.
- **Then demonstrate:** enter District A and District B; show STAR's published score totals **+ pairwise matrix add up** to the combined result (summable), while the IRV race's district winners (B, B) **don't predict** the merged winner (B eliminated) — summability, live.
- **Then promote:** if it works, make it a BV-backed case (District A / District B / Combined), freeze the export, and drop the screenshots into the [summability hub](../../topics/summability/) — adding the live BV dimension the [`summability_demo`](../../../method_comparisons/summability_demo/) currently lacks (today it's LH-engine + arithmetic only).
- **Refs:** [summability topic hub](../../topics/summability/) · [summability_demo](../../../method_comparisons/summability_demo/) · creation tool: [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.md)

### BV STV tabulation crash — found via BV2171 / BV2172 (BV devs fixing it)
Both **BV2171 (`h93tm4`)** and **BV2172 (`bkwfjr`)** crash on their `/results` page — the ballots are intact (7 races, 100/8 votes each); it's BV's **tabulation** that fails. Root cause confirmed by the BetterVoting devs (Jackson Loper, 2026-07-09): a bug in **BV's STV tabulator** — *"whenever the final seat is won via quota by the last remaining candidate and there are surplus ballots to redistribute, results tabulation crashes."* Our `STV (1 seat)` race on the symmetric-centrist profile triggers it **consistently** (so BV2171 was NOT actually fine — same crash). **BV is shipping a fix.** (My earlier STAR-PR@1-seat suspicion was wrong — it's STV.)

- **When BV's fix lands:** re-check both `/results` pages. The elections need no recreation if the fix makes them tabulate — just **export Election + Ballots + Results** for each into `06_Other/_demo_dropbox/`, and I'll swap them into the frozen `_bv_export.json` files (currently Election + Ballots only — BV's "Ballot Data" button omits the tally; `pp2q4q`/BV2170 has a full one, so it's doable from the results view) and record the actual winners + random pole-tie draws (RCV-IRV / STV / Choose-One) in the case pages.
- **Only if BV can't recover these two elections:** recreate them (new bvids) via [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py) — the `_sq_races("Condorcet centrist (full/minimal)", …)` helpers already exist — **without clobbering the pending `ELECTIONS = [BV2174, BV2175]`** (move those to a `_CREATED_` block first), then repoint the [`symmetric_centrist_all_methods/`](../../../method_comparisons/symmetric_centrist_all_methods/) case files (yaml `bv_election_id` + results URLs, the `.md` pages, the frozen `_bv_export.json`) and regenerate registry/mirrors.
- **Keep the STV race** once BV fixes it — these cases now double as a regression check for this exact crash. Worth noting on the case pages that BV2171/BV2172 surfaced a live BV STV bug. Low urgency: every deterministic winner (Casey) is already LH-verified; this only completes the third-party proof. Refs: [symmetric_centrist_all_methods](../../../method_comparisons/symmetric_centrist_all_methods/) · [BV API / export notes](bv_api_election_creation_notes.md)

## Done

*(none yet)*
