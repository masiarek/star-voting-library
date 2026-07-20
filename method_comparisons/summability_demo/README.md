# Summability demo — one example, three methods

Runnable elections behind the **[Summability topic hub](../../00_start_here/topics/summability/)**. The point: *summability is a property of the **count**, not the ballot.* The same two districts are summable under STAR and Ranked Robin, and **not** under RCV-IRV.

## Files

| File(s) | Method | Summable? | Shows |
|---------|--------|:---:|-------|
| `irv_district_A.yaml`, `irv_district_B.yaml`, `irv_combined.yaml` | **RCV-IRV** | ❌ | B wins **both** districts but is *eliminated* when merged — no precinct subtotal predicts it |
| `star_district_A.yaml`, `star_district_B.yaml`, `star_combined.yaml` | **STAR** | ✅ | precinct **score totals + pairwise matrix add** to the combined winner |
| `rr_district_A.yaml`, `rr_district_B.yaml`, `rr_combined.yaml` | **Ranked Robin / RCV-RR** | ✅ | the **same ranked ballots** IRV couldn't combine — the **pairwise matrix adds** cell by cell and recovers B |

> **Note on the `rr_*` files.** Ranked Robin runs on the *same ranked ballots* as IRV (`irv_*`) — only the *count* differs — so the `rr_*` files carry **identical ballots** to `irv_*` and just set `voting_method: RankedRobin`. They exist so the exact **pairwise (For–Against–Equal) matrix** in the [RR write-up](../../00_start_here/RCV_Ranked_Robin/RCV_RR_summability.md) is reproducible **on the LH engine** (not only via the pref_voting cross-check): District A + District B add cell-by-cell to the Combined matrix, from which B beats A (11–9) and C (11–9). The folder stays a cross-method (IRV / STAR / RR) demo — it is **not** prefixed `RCV_RR_`.

## Run them

```bash
# STAR (summable) — score totals + matrix
cd STARVote_LH_tabulation_engine
python starvote_larry_hastings.py ../01_Single_winner/summability_demo/star_combined.yaml

# RCV-IRV (not summable) — B eliminated when districts merge
python starvote_larry_hastings.py ../01_Single_winner/summability_demo/irv_combined.yaml

# Ranked Robin on the SAME ballots — the summable pairwise matrix (LH engine)
python starvote_larry_hastings.py ../method_comparisons/summability_demo/cases/rr_combined.yaml

# Independent cross-check of the same ranked ballots (Copeland winner)
cd tools_adam/pref_voting_tabulation_engine
python pref_voting_tabulation.py ../../../method_comparisons/summability_demo/cases/rr_combined.yaml
```

## The three write-ups

- [STAR is summable](../../00_start_here/STAR_Voting/properties_and_limits/STAR_summability.md)
- [Ranked Robin is summable](../../00_start_here/RCV_Ranked_Robin/RCV_RR_summability.md)
- [IRV is *not* summable](../../00_start_here/RCV_IRV/RCV_IRV_lack_of_summability.md)

The STAR files are guarded by the positive test harness; the `rr_*` files carry `expected_winners` (B for all three) and tabulate to it on the LH engine, confirmed independently by the [`pref_voting` cross-check](../../00_start_here/tabulation_engines/cross_checking_with_pref_voting.md).
