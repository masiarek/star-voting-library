# Pets Governance — six positions, six methods (majoritarian vs proportional)

*One electorate elects a whole pet government six different ways. The lesson is the sharpest divide in multi-winner voting: **majoritarian methods hand every seat to the majority; proportional methods seat the minority.** All six races are reproducible on BetterVoting (see "On BetterVoting" below), and all six are cross-checked against our LH engine.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kcf8vf) · **[results ↗](https://bettervoting.com/kcf8vf/results)** (election `kcf8vf`, Test ID **BV2134**). Frozen export: [`pets_gov_bv2134_kcf8vf_bv_export.json`](cases/pets_gov_bv2134_kcf8vf_bv_export.json).

## The electorate

22 voters in two parties:

- **Furries** (majority, 13 voters): Dog, Cat, Fish — score their own high, the Others low; rank `Dog > Cat > Fish > Bird > Rabbit > Hamster`.
- **Others** (minority, 9 voters): Bird, Rabbit, Hamster — the mirror image; rank `Bird > Rabbit > Hamster > Fish > Cat > Dog`.

The majority is 59%, the minority 41% — so a fair 3-seat body "should" be roughly 2–1.

## Five positions, five methods

| Position | Method | Seats | Winners | Character |
|----------|--------|:---:|---------|-----------|
| **Mayor** | [Ranked Robin](cases/pets_gov_ranked_robin.yaml) | 1 | **Dog** | Condorcet — majority's consensus |
| **Council** | [Bloc STAR](cases/pets_gov_bloc_star.yaml) | 3 | **Dog, Fish, Cat** | majoritarian — **majority sweeps** |
| **Committee** | [Approval](cases/pets_gov_approval.yaml) | 2 | **Dog, Cat** | majoritarian — majority again |
| **Council (PR)** | [STAR-PR](cases/pets_gov_star_pr.yaml) | 3 | **Bird, Dog, Fish** | proportional — **minority seated** |
| **Delegates** | [STV](cases/pets_gov_stv.yaml) | 3 | **Dog, Bird, Cat** | proportional — minority seated |
| **Neighborhood Reps** | [Bloc Plurality (SNTV)](cases/pets_gov_bloc_plurality.yaml) | 2 | **Dog, Bird** | concentrated votes → minority seated |

Every winner is tabulated by the LH engine (`starvote_larry_hastings.py`); mirrors are in `pets_governance_tabulated/`.

## The one lesson

Give the **same** 59/41 electorate three seats:

- **Bloc STAR** and **STV** read identical intent, but Bloc STAR gives the majority **all three** (Dog, Fish, Cat) while STV gives **two to the majority and one to the minority** (Dog, Cat + Bird). That's the whole majoritarian-vs-proportional distinction in one comparison.
- **STAR-PR** agrees with STV that the minority earns a seat (Bird), differing only on the majority's third pick (Fish vs Cat) — two proportional methods, nearly the same body.
- The single-winner offices (**Mayor** by Ranked Robin, and the 2-seat **Committee** by Approval) are inherently majoritarian here: with a cohesive 59% bloc, the majority's favorites win. Dog is the Condorcet winner, so *every* Condorcet method would also elect Dog mayor.

So a minority that is **shut out** of the Council-by-Bloc and the Committee is **represented** on the Council-by-PR and the Delegates — same voters, different rules.

## On BetterVoting

All five races are reproducible on BetterVoting. BV's `runBlocTabulator` is a generic bloc/sequential multi-winner driver used by STAR, Approval, Plurality and Ranked Robin — so **Bloc STAR** is `voting_method: STAR` with `num_winners: 3`, and **Bloc Approval** is `voting_method: Approval` with `num_winners: 2` (the bloc behavior comes from the winner count, not a separate method). STAR-PR, STV and Ranked Robin map directly. This set is created as a single multi-race BV election (BV2134); the winners above are the LH tabulation, cross-checked against BetterVoting's own tabulators.

The **sixth** position — **Neighborhood Reps by Bloc Plurality / SNTV (2 seats)** — elects **Dog, Bird**: with choose-one ballots each party's votes concentrate on its champion, so the minority's Bird takes the second seat (SNTV landing ~proportional, unlike Bloc Approval which gave the majority both seats). It's cross-checked like the rest: the LH engine now does **multi-winner Plurality (SNTV)** — `Plurality` + `num_winners>1` elects the top-N by first-choice count — and **Bloc Ranked Robin** (`RankedRobin` + `num_winners>1`, top-N by record). So all six races are LH-tabulated *and* BV-confirmed.

**Confirmed on BetterVoting (`kcf8vf`).** All six races match: BV's `runBlocTabulator` (Bloc STAR, Bloc Approval, Bloc Plurality), Allocated-Score PR, and STV elect exactly the seats our engines do. The only cosmetic difference is **seat order** in STAR-PR — BV reports Dog, Bird, Fish; LH reports Bird, Dog, Fish — the *same three winners*, just a different order of election.

## See also

- Folder overview: [pets_governance — README](README.md)
- The single-winner siblings: [BV2133 — Pet poll II (four winners)](../pet_poll_four_winners/bv2133_dyxrbr_pet_poll_four_winners.md) and [BV2132 — Pet poll (three winners)](../pet_poll_four_methods/bv2132_ykjjhy_pet_poll_four_methods.md)
- STAR-PR / proportional background: [03_STAR_PR](../../03_STAR_PR/) · [Ranked Robin](../../05_Ranked_Robin/)
