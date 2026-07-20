# Food-Truck Row — two spots, five counts: vote-splitting, sweeps, and shares

One 100-voter electorate elects **two** food-truck spots five different ways — and gets three different parliaments: the majority with **zero** seats, the majority with **both** seats, and one seat per side. Nothing about the voters changes. Only the counting rule does.

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/fvg8y8) · **[results ↗](https://bettervoting.com/fvg8y8/results)** (election `fvg8y8`, Test ID BV2210 — all five races, all agreeing with the LH engine).

## The electorate

The **savory side is an outright 57-voter majority** that runs *three* trucks; the **sweet side is a disciplined 43-voter minority** on *two*. Within each side, voters score/rank their own trucks (5/4/3 by taste) and skip the other side's entirely.

| Count | first choice | score ballot | ranked ballot |
|:---:|---|---|---|
| 20 | Arepa | Arepa 5, Bao 4, Churro 3 | Arepa > Bao > Churro |
| 19 | Bao | Bao 5, Arepa 4, Churro 3 | Bao > Arepa > Churro |
| 18 | Churro | Churro 5, Arepa 4, Bao 3 | Churro > Arepa > Bao |
| 22 | Donut | Donut 5, Eclair 4 | Donut > Eclair |
| 21 | Eclair | Eclair 5, Donut 4 | Eclair > Donut |

## The same-opinion line-up

Rows are candidates, columns are counts — one electorate, read five ways:

| | first choices | SNTV (top-2) | Bloc STAR | Bloc Ranked Robin | STAR-PR | STV |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Arepa** (savory) | 20 | — | **seat** | **seat** (4–0) | **seat** | **seat** |
| **Bao** (savory) | 19 | — | **seat** | **seat** (3–1) | — | — |
| **Churro** (savory) | 18 | — | — | — | — | — |
| **Donut** (sweet) | 22 | **seat** | — | — | **seat** | **seat** |
| **Eclair** (sweet) | 21 | **seat** | — | — | — | — |
| *savory : sweet (57 : 43)* | | **0 : 2** | **2 : 0** | **2 : 0** | **1 : 1** | **1 : 1** |

## Count 1 — SNTV: the majority splits and loses everything

Each voter marks **one** truck; the top two counts win:

```text
First-choice votes (most votes fill the seats):
   Donut     22  <- Elected
   Eclair    21  <- Elected
   Arepa     20
   Bao       19
   Churro    18

Winners — SNTV (single non-transferable vote), 2 seats: Donut, Eclair
```

Fifty-seven percent of the room is first-choice savory — and holds **zero seats**, because one non-transferable vote split three ways tops out at 20. This is the classic SNTV failure: it punishes a side for offering *more choice*, and it's why SNTV jurisdictions develop machine-politics candidate-rationing. The engine's [Vote-splitting check] names it on the Bloc STAR file:

```text
[Vote-splitting check]
  Choose-One first choices: Donut 22, Eclair 21, Arepa 20, Bao 19, Churro 18
  Plurality winner: Donut (22, 22.0%)
  Bloc 'Savory' = Arepa, Bao, Churro: combined 57 (57.0%); winner Donut is OUTSIDE it.
  => VOTE SPLITTING: the 'Savory' bloc is an outright majority (57 vs
     Donut's 22) but split across 3 candidates, so Donut won Choose-One.
     STAR elected Arepa.
```

## Counts 2 & 3 — Bloc STAR and Bloc Ranked Robin: the majority sweeps

Better ballots cure the split — savory support pools across all three trucks on score and ranked ballots alike. But a **bloc** (majoritarian) count then hands the pooled majority *both* seats:

- **Bloc STAR:** Arepa (top scores + runoff) takes seat 1, Bao seat 2 — the sweet side's 43 voters scored both winners 0.
- **Bloc Ranked Robin:** every savory truck beats every sweet truck 57–43 head-to-head; the record's top two are Arepa (4–0) and Bao (3–1).

Note what this shows: **ranked ballots do not create proportionality.** Sweeps and shares are decided by the *count* (quotas and transfers), not the ballot shape. Majoritarian multi-winner is the right tool when the body *should* speak for the majority (a city's two at-large delegates voting as one voice) — and the wrong one when the body should *mirror* the room.

## Counts 4 & 5 — STAR-PR and STV: one seat per side

- **STAR-PR / Allocated Score:** Arepa wins seat 1; the quota of ballots that elected him is spent; the remaining live weight is majority-sweet, and Donut takes seat 2.
- **STV:** Droop quota 34. Churro's elimination pools the savory vote → Arepa elected; Eclair's elimination pools the sweet vote → Donut elected. (The count deliberately ends with a hopeful still standing — clear of the [BV sole-survivor STV crash](../../06_Other/STV/bv_stv_sole_survivor_crash/README.md).)

A 57:43 room, a 1:1 delegation — one seat per ~quota of voters, the [proportional representation](../../00_start_here/proportional_representation/README.md) promise kept by both the score-ballot and ranked-ballot routes.

## BV verification notes

All five live races agree with the LH engine, with no genuine tie anywhere (every rung 22/21/20/19/18 distinct by design). One display quirk for the record: BetterVoting banners the **STAR_PR** race "Tied!" with `tieBreakType: random` despite no tie existing — the same STAR_PR serializer quirk first seen on `89wwvr` ([exercise 12](../../01_STAR/exercises/ex12_bloc_vs_proportional.md)) and `jwxr3j`; this election is the **third confirming instance**. The elected pair itself is correct.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/food_truck_row/cases/bv2210_fvg8y8_sntv_split.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/food_truck_row/cases/bv2210_fvg8y8_bloc_star_sweep.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/food_truck_row/cases/bv2210_fvg8y8_bloc_rr_sweep.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/food_truck_row/cases/bv2210_fvg8y8_star_pr_share.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/food_truck_row/cases/bv2210_fvg8y8_stv_share.yaml
```

Full mirrors: [`food_truck_row_tabulated/`](cases/cases_tabulated/).

---

**Where this comes from.** Ballots and cast are this repo's own. Siblings: [sntv_village_council](../sntv_village_council/sntv_village_council.md) (the gentle SNTV intro this case escalates), [multi_member_plurality](../multi_member_plurality/) (block & limited voting), [pets_governance](../pets_governance/) (six methods, one electorate), [exercise 12](../../01_STAR/exercises/ex12_bloc_vs_proportional.md) (Bloc-vs-PR at whiteboard scale), and the seat-family map at [electing more than one](../../00_start_here/topics/electing_more_than_one.md).

# file: README.md
