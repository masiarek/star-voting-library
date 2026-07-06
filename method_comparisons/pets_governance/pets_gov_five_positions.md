# Pets Governance — five positions, five methods (majoritarian vs proportional)

*One electorate elects a whole pet government five different ways. The lesson is the sharpest divide in multi-winner voting: **majoritarian methods hand every seat to the majority; proportional methods seat the minority.** LH-only (Bloc STAR and multi-winner Approval aren't BetterVoting methods).*

## The electorate

22 voters in two parties:

- **Furries** (majority, 13 voters): Dog, Cat, Fish — score their own high, the Others low; rank `Dog > Cat > Fish > Bird > Rabbit > Hamster`.
- **Others** (minority, 9 voters): Bird, Rabbit, Hamster — the mirror image; rank `Bird > Rabbit > Hamster > Fish > Cat > Dog`.

The majority is 59%, the minority 41% — so a fair 3-seat body "should" be roughly 2–1.

## Five positions, five methods

| Position | Method | Seats | Winners | Character |
|----------|--------|:---:|---------|-----------|
| **Mayor** | [Ranked Robin](pets_gov_ranked_robin.yaml) | 1 | **Dog** | Condorcet — majority's consensus |
| **Council** | [Bloc STAR](pets_gov_bloc_star.yaml) | 3 | **Dog, Fish, Cat** | majoritarian — **majority sweeps** |
| **Committee** | [Approval](pets_gov_approval.yaml) | 2 | **Dog, Cat** | majoritarian — majority again |
| **Council (PR)** | [STAR-PR](pets_gov_star_pr.yaml) | 3 | **Bird, Dog, Fish** | proportional — **minority seated** |
| **Delegates** | [STV](pets_gov_stv.yaml) | 3 | **Dog, Bird, Cat** | proportional — minority seated |

Every winner is tabulated by the LH engine (`starvote_larry_hastings.py`); mirrors are in [`pets_governance_tabulated/`](pets_governance_tabulated/).

## The one lesson

Give the **same** 59/41 electorate three seats:

- **Bloc STAR** and **STV** read identical intent, but Bloc STAR gives the majority **all three** (Dog, Fish, Cat) while STV gives **two to the majority and one to the minority** (Dog, Cat + Bird). That's the whole majoritarian-vs-proportional distinction in one comparison.
- **STAR-PR** agrees with STV that the minority earns a seat (Bird), differing only on the majority's third pick (Fish vs Cat) — two proportional methods, nearly the same body.
- The single-winner offices (**Mayor** by Ranked Robin, and the 2-seat **Committee** by Approval) are inherently majoritarian here: with a cohesive 59% bloc, the majority's favorites win. Dog is the Condorcet winner, so *every* Condorcet method would also elect Dog mayor.

So a minority that is **shut out** of the Council-by-Bloc and the Committee is **represented** on the Council-by-PR and the Delegates — same voters, different rules.

## Why LH-only

BetterVoting's methods are Plurality, IRV, STV, STAR, STAR-PR, Approval, and Ranked Robin — it has **no Bloc STAR**, and its Approval is single-winner. Two of these five races (Bloc STAR; multi-winner Approval) can't be built on BV, so the whole set is kept LH-only for coherence. The BV-supported races here (STAR-PR, STV, Ranked Robin) match BetterVoting's own tabulators if reproduced there.

## See also

- Folder overview: [pets_governance — README](README.md)
- The single-winner siblings: [BV2133 — Pet poll II (four winners)](../pet_poll_four_winners/bv2133_dyxrbr_pet_poll_four_winners.md) and [BV2132 — Pet poll (three winners)](../pet_poll_four_methods/bv2132_ykjjhy_pet_poll_four_methods.md)
- STAR-PR / proportional background: [03_STAR_PR](../../03_STAR_PR/) · [Ranked Robin](../../05_Ranked_Robin/)
