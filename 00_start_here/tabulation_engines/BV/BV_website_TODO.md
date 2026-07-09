# BetterVoting — website TO-DO (manual / UI testing backlog)

Repo-native backlog of **BetterVoting website / UI** tasks — things to test, learn, or verify on the live app that don't have a YAML/tabulation home. (Tabulation *cases* live in the auto-generated [BV registry](../../YAML_test_case_index/BV_registry.md); this page is for the hands-on UI work that the registry can't capture — complements the Google-Sheet QA, but versioned here with the docs.)

## Open

### Districts / precincts — learn the data-entry flow, then BV-back the summability demo
BetterVoting **supports districts** (this was simply never tested from our side — an earlier note wrongly assumed BV models only a single electorate). Learning the district data-entry flow would unlock a **live, BV-backed** version of the [summability demo](../../../method_comparisons/summability_demo/):

- **Learn / test:** how district data is entered in the BV builder (per-district ballot entry? a district field on each ballot? assignment after casting?), whether results expose **per-district subtotals**, and whether the combined tally is exactly their sum.
- **Then demonstrate:** enter District A and District B; show STAR's published score totals **+ pairwise matrix add up** to the combined result (summable), while the IRV race's district winners (B, B) **don't predict** the merged winner (B eliminated) — summability, live.
- **Then promote:** if it works, make it a BV-backed case (District A / District B / Combined), freeze the export, and drop the screenshots into the [summability hub](../../topics/summability/) — adding the live BV dimension the [`summability_demo`](../../../method_comparisons/summability_demo/) currently lacks (today it's LH-engine + arithmetic only).
- **Refs:** [summability topic hub](../../topics/summability/) · [summability_demo](../../../method_comparisons/summability_demo/) · creation tool: [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.md)

### Redo BV2172 (bkwfjr) — the election broke on BetterVoting
The full 100-voter "Condorcet centrist, all seven methods" election **[BV2172 / `bkwfjr`](https://bettervoting.com/bkwfjr/results)** went wrong on BV (results/tabulation side — the ballots exported fine: 7 races, 100 votes each). Its minimal twin **BV2171 / `h93tm4`** is OK.

- **Recreate it:** add a fresh BV2172 spec to [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py) and run it — the `_sq_races("Condorcet centrist (full)", 47, 3)` helper already exists (used by the original). **Don't clobber the pending `ELECTIONS = [BV2174, BV2175]`** (the no-show pair) — move those to a `_CREATED_` block or add BV2172 alongside them, then run. It gets a **new bvid**.
- **If it breaks again, isolate the cause:** prime suspect is the **STAR-PR race at `num_winners: 1`** (a proportional method with one seat) — if BV rejects/mis-tabulates it, drop that race (STAR-PR(1) ≡ STAR) and keep the other six. (BV2171 has the same race and was reportedly fine, so it may have been transient.)
- **Then update the case files** in [`method_comparisons/symmetric_centrist_all_methods/`](../../../method_comparisons/symmetric_centrist_all_methods/): repoint `bv2172_bkwfjr_*` → the new bvid (yaml `bv_election_id` + results URL, the `.md` page, rename the frozen `_bv_export.json`), regenerate the registry/mirrors, commit.

### Re-export BV2171 + BV2172 with the Results block (frozen exports are incomplete)
The frozen `_bv_export.json` for **BV2171 (`h93tm4`)** and **BV2172** currently hold only **Election + Ballots — no Results**. BV's "Ballot Data" export button omits the computed tally; the Results block only appears when you export from the **results view / after the election is finalized** (BV2170 `pp2q4q` has it, so it's doable).

- Re-export each from its `/results` page (finalize/close if prompted), drop the JSON in `_demo_dropbox/`, and I'll swap it into the two `_bv_export.json` files.
- Then the case pages can record **BV's actual random tie-break draws** for the RCV-IRV / STV / Choose-One pole ties (currently documented as "random, pending finalized export"). Low priority — every deterministic winner (Casey) is already LH-verified; this only completes the third-party proof.
- Refs: [symmetric_centrist_all_methods](../../../method_comparisons/symmetric_centrist_all_methods/) · [BV API / export notes](bv_api_election_creation_notes.md)

## Done

*(none yet)*
