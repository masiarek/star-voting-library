# BV2133 — Pet poll II: four methods, four winners

*The sequel to [BV2132](../pet_poll_four_methods/bv2132_ykjjhy_pet_poll_four_methods.md), tuned harder: add a fourth pet and every method elects a **different** one. The sharpest possible "the method chooses the winner" demonstration — 32 voters, one ballot set, four winners.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dyxrbr) · **[results ↗](https://bettervoting.com/dyxrbr/results)** (election `dyxrbr`, Test ID **BV2133**).

Frozen export: [`bv2133_dyxrbr_pet_poll_four_winners_bv_export.json`](bv2133_dyxrbr_pet_poll_four_winners_bv_export.json).

## The electorate

Four pets (Dog, Cat, Fish, Bird), 32 voters in four blocs:

```text
 9 voters:  Bird > Cat > Fish > Dog       scores  Dog0 Cat2 Fish1 Bird4
10 voters:  Fish > Cat > Bird > Dog       scores  Dog2 Cat4 Fish5 Bird3
 7 voters:  Dog  > Cat > Fish > Bird      scores  Dog3 Cat2 Fish1 Bird0   (mild Dog fans)
 6 voters:  Dog  > Cat > Fish > Bird      scores  Dog5 Cat2 Fish1 Bird0   (die-hard Dog fans)
```

## Four methods, four winners

| Race | Winner | Our engine | BetterVoting | Why | yaml |
|------|:---:|:---:|:---:|-----|:--:|
| **Plurality** | **Dog** | Dog | Dog | most first choices (13) — but 19 rank Dog last | [`.yaml`](bv2133_dyxrbr_pet2_plurality.yaml) |
| **RCV-IRV** | **Fish** | Fish | Fish | Bird then Cat eliminated; transfers pile on Fish (19–13) | [`.yaml`](bv2133_dyxrbr_pet2_irv.yaml) |
| **Approval** | **Bird** | Bird | Bird | widely approved (19) at the 3+ threshold | [`.yaml`](bv2133_dyxrbr_pet2_approval.yaml) |
| **STAR** | **Cat** | Cat | Cat | score leaders Cat (84) & Fish (72) advance; Cat wins runoff 22–10 | [`.yaml`](bv2133_dyxrbr_pet2_star.yaml) |

Every race is cross-checked **LH engine = BetterVoting**. Four methods, four different pets — nobody wins twice.

## Why every method picks someone else

- **Plurality → Dog.** Dog owns the biggest first-choice bloc (13) from two tiers of Dog fans, so choose-one crowns it — despite 19 of 32 voters ranking Dog dead last.
- **RCV-IRV → Fish.** Dog can't grow (everyone else ranks it last). Bird (9) is eliminated first, lifting Cat; then Cat is squeezed out and its transfers land on **Fish**, which passes Dog 19–13.
- **Approval → Bird.** At a "3-or-more = approve" bar, Bird collects the 9 Bird-firsts plus the 10 Fish-firsts (who also approve Bird) = 19 — more than anyone. Broad acceptability, not first-place passion.
- **STAR → Cat.** Cat is nobody's favorite but everyone's solid second — top score total (84), and it wins the head-to-head runoff against Fish 22–10. The consensus candidate.

## Provenance

Created via [`create_bv_test_election.py`](../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py) as one multi-race BV election (`dyxrbr`) with made-up ballots tuned for a four-way split. BetterVoting's four race results match our engines exactly.

## The pets set

- [BV2132 — Pet poll (three winners)](../pet_poll_four_methods/bv2132_ykjjhy_pet_poll_four_methods.md) — the gentler original (Cat wins Approval *and* STAR).
- **BV2133 — Pet poll II (four winners)** — this one.
- [Pets Governance (five methods, LH-only)](../pets_governance/pets_gov_five_positions.md) — multi-winner: majoritarian vs proportional.

## See also

- Folder overview: [pet_poll_four_winners — README](README.md)
- [Condorcet efficiency — topic hub](../../00_start_here/topics/condorcet/README.md) · [Glossary](../../00_start_here/GLOSSARY.md)
