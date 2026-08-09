# BV2130 — Presidential Board Election (Proportional STAR = Allocated Score)

<!-- case-meta:start — managed by build_yaml_pages.py; edit the YAML, not these lines -->
**Method:** [Allocated Score (proportional STAR)](../01_Learn/README.md) · **7 seats** · **Expected winners:** Bernie Sanders (Democrat), Al Gore (Democrat), Barack Obama (Democrat), Cornel West (Independent), Chase Oliver (Libertarian), Kamala Harris (Democrat), Karina Garcia (Socialism and Liberation) · [full count →](cases/cases_pages/bv2130_presidential_board_star_pr.md)
<!-- case-meta:end -->

*A real 7-seat Proportional STAR election on BetterVoting (`bvhchj`): 51 candidates, 102 sparse ballots. LH's `allocated` engine reproduces BetterVoting's **first six seats exactly**; the **seventh diverges** (LH → Claudia De La Cruz, BV → Karina Garcia — both Socialism & Liberation). **Resolved 2026-08-06:** the engines agree — BV counted 100 ballots to LH's 102, giving a different Hare quota. The two missing ballots are [#1478](https://github.com/Equal-Vote/bettervoting/issues/1478).*

Reference files: [`bv2130_presidential_board_star_pr.yaml`](cases/bv2130_presidential_board_star_pr.yaml) (`voting_method: allocated`, 7 winners) · frozen export [`bv2130_presidential_board_star_pr_bv_export.json`](cases/bv2130_presidential_board_star_pr_bv_export.json) (BV `bvhchj`). Backs sheet row **BV2130**. The election also has a second race (party-alignment **Plurality**) that elects **Democrat**.

## Method mapping — BV `STAR_PR` = Allocated Score

BetterVoting's proportional method is exported as **`STAR_PR`**, which LH does *not* recognize by that name — it is the **Allocated Score** method (`voting_method: allocated`; LH's other proportional variants are `sss` and `rrv`, which give different results). So this is the proportional analog of the [#904](https://github.com/Equal-Vote/bettervoting/issues/904)/[#1086](https://github.com/Equal-Vote/bettervoting/issues/1086) naming point: `STAR_PR` needs mapping to a concrete rule before any engine can reproduce it.

## Result — 6 of 7 seats match, seat 7 diverges

| Seat | LH (`allocated`) | BetterVoting (`STAR_PR`) |
|:--:|---|---|
| 1–6 | Bernie Sanders, Al Gore, Barack Obama, Cornel West, Chase Oliver, Kamala Harris | **same** ✓ |
| 7 | **Claudia De La Cruz** (Soc. & Lib.) | **Karina Garcia** (Soc. & Lib.) |

The two methods agree that the last seat goes to a Socialism & Liberation candidate — proportionality is working — but disagree on *which one*. In LH's exact Allocated Score math Claudia is clearly ahead at the final allocation:

```
The highest-scoring candidate wins a seat.
  Claudia De La Cruz (Socialism and Liberation) -- 34 + 5745/21952 -- First place   (≈ 34.262)
  Karina Garcia      (Socialism and Liberation) -- 33 + 21901/21952                 (≈ 33.998)
 Claudia De La Cruz wins a seat.
```

Full audit copy: [`_main_tabulated/bv2130_presidential_board_star_pr_tabulated.txt`](cases/cases_tabulated/bv2130_presidential_board_star_pr_tabulated.txt).

## The finding — resolved 2026-08-06: it is the ballot count, not the method

BetterVoting's result carries `tieBreakType: "random"` and elected Karina over Claudia, while in LH's computation this is **not a tie** (Claudia leads by ~0.26 of a reweighted point). That framing invited two hypotheses — an implementation difference in surplus/reweighting/rounding, or a near-tie BV broke at random. **Both are wrong.** The engines compute the same thing; they were handed different elections.

**The algorithms agree.** BetterVoting's own unit tests for this method — `packages/backend/src/Tabulators/AllocatedScore.test.ts` — reproduce exactly in LH's `allocated`: "Basic Example" → Allison, Doug; "Single vote fractional surplus" → Allison, Doug; "Voters < Winners" → Allison, Bill, Carmen. Their fixtures are our fixtures.

**Precision is not the cause either.** `AllocatedScore.ts` uses `fraction.js`, i.e. exact rational arithmetic — the same exactness LH uses. A gap of 0.26 was never floating-point drift.

**The inputs differ.** The frozen export reports **`nTallyVotes: 100`, `nAbstentions: 2`** for this race. The YAML holds **102 ballots**. Both engines then compute the same Hare quota `V / seats` from different `V`:

| | ballots counted | Hare quota (7 seats) |
|---|--:|--:|
| BetterVoting | 100 | 14.2857 |
| LH | 102 | 14.5714 |

A different quota changes how much ballot weight each winner consumes, in **every** round. The effect compounds across six seats and finally flips the seventh.

**And the two missing ballots have a name.** BV drops a partial ballot whose marks are all equal, counting it as an abstention — [#1478](https://github.com/Equal-Vote/bettervoting/issues/1478). With 51 candidates and sparse ballots, this election is precisely the shape that triggers it.

That makes this case a **significant escalation of #1478** rather than a proportional-method defect. Filed as a count-level defect on a 4-ballot election where the winners happened to survive, the bug looked cosmetic. Here the two dropped ballots **change who holds a seat**. The seat-7 disagreement is the visible symptom; the discarded ballots are the disease.

*(What still deserves a maintainer's eye is narrower than it first appeared: BV labels the race `tieBreakType: "random"` on a seat that, on its own numbers, may not have been tied at all.)*

## Related

- Proportional STAR variants in LH: [`02a` allocated](cases/02a_c5_b63_proportional-allocated-score.yaml) · [`02b` sss](cases/02b_c5_b63_proportional-sss.yaml) · [`02c` rrv](cases/02c_c5_b63_proportional-rrv.yaml).
- The same random-tie-break family (single-winner / Bloc): [BV `jfk7pd`](../../01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) · [BV131](../../02_STAR_Bloc/02_Examples/bv131_guido_bloc.md) · [BV750](../../02_STAR_Bloc/02_Examples/bv750_tie_breaking_bloc.md).
