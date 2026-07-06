# pet_poll_four_methods — one electorate, four methods, three winners (BV2132)

A single BetterVoting election (`ykjjhy`, Test ID **BV2132**) with **four races** over the same 22 voters and three pets (Dog, Cat, Fish) — Plurality, RCV-IRV, Approval, STAR. The ballots are made-up and tuned so the methods **disagree**, unlike Equal.Vote's `meta_pets` that inspired it.

**▶ Live results:** [bettervoting.com/ykjjhy/results](https://bettervoting.com/ykjjhy/results)

| Method | Winner | Why | yaml |
|--------|:---:|-----|:--:|
| Plurality | **Dog** | most first choices (9) — but 13/22 rank Dog last (spoiler/FPTP) | [`.yaml`](bv2132_ykjjhy_pet_plurality.yaml) |
| RCV-IRV | **Fish** | Cat (fewest first choices) eliminated first → center squeeze | [`.yaml`](bv2132_ykjjhy_pet_irv.yaml) |
| Approval | **Cat** | broad support — approved by 22 of 22 non-Dog partisans | [`.yaml`](bv2132_ykjjhy_pet_approval.yaml) |
| STAR | **Cat** | score leaders Cat & Fish advance; Cat wins runoff 15–7 | [`.yaml`](bv2132_ykjjhy_pet_star.yaml) |

**Cat is the Condorcet winner** (beats Dog 13–9, Fish 15–7) — it wins the two cardinal methods and loses the two that only read first choices / eliminate. Every race's winner is cross-checked: **LH engine = BetterVoting** on all four.

→ **Full lesson:** [bv2132_ykjjhy_pet_poll_four_methods.md](bv2132_ykjjhy_pet_poll_four_methods.md)

# file: README.md
