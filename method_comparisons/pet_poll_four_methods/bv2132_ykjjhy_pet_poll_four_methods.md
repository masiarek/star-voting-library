# BV2132 — Pet poll: four methods, one electorate, three winners

*Our own answer to Equal.Vote's meta_pets ("What Makes the Best Pet?"), rebuilt small and **tuned so the methods actually disagree**. The same 22 voters rank the same three pets (Dog, Cat, Fish), tallied four ways in one BetterVoting election. The result splits three ways — and the candidate a majority actually prefers wins only the two "good" methods.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ykjjhy) · **[results ↗](https://bettervoting.com/ykjjhy/results)** (election `ykjjhy`, Test ID **BV2132**).

Frozen export: [`bv2132_ykjjhy_pet_poll_four_methods_bv_export.json`](bv2132_ykjjhy_pet_poll_four_methods_bv_export.json).

## The electorate

Twenty-two voters in three blocs, each with a clear preference order:

```text
 9 voters:  Dog > Cat > Fish      (Dog partisans)
 7 voters:  Fish > Cat > Dog      (Fish partisans)
 6 voters:  Cat > Fish > Dog      (Cat first)
```

**Cat is the Condorcet winner** — beats Dog 13–9 and Fish 15–7 head-to-head — but has the fewest *first* choices (6). That single fact is what makes the methods diverge.

## Four methods, three winners

| Race | Reads | Winner | Our engine | BetterVoting | yaml |
|------|-------|:---:|:---:|:---:|:--:|
| **Plurality** (choose one) | first choices | **Dog** | Dog | Dog | [`…_plurality.yaml`](bv2132_ykjjhy_pet_plurality.yaml) |
| **RCV-IRV** | ranked, elimination | **Fish** | Fish | Fish | [`…_irv.yaml`](bv2132_ykjjhy_pet_irv.yaml) |
| **Approval** | approve any | **Cat** | Cat | Cat | [`…_approval.yaml`](bv2132_ykjjhy_pet_approval.yaml) |
| **STAR** | score 0–5 | **Cat** | Cat | Cat | [`…_star.yaml`](bv2132_ykjjhy_pet_star.yaml) |

Every race's winner is cross-checked: our LH engine (`starvote_larry_hastings.py`) and BetterVoting's tabulator **agree on all four**.

## Why they split

- **Plurality → Dog.** Dog has the most first choices (9), so choose-one hands it the win — even though 13 of 22 voters rank Dog *last*. Classic first-past-the-post: a polarizing plurality beats a broadly-liked majority. Cat, the consensus, is a *spoiler'd* also-ran with 6 first choices.
- **RCV-IRV → Fish.** IRV looks past first choices, but it eliminates the **fewest-first-choice** candidate each round — that's Cat (6). Cat's ballots transfer to Fish, which then beats Dog 13–9. The Condorcet winner is **squeezed out before the final round** — a textbook center squeeze.
- **Approval → Cat** and **STAR → Cat.** Both let voters express support beyond one name, so Cat's broad acceptability shows up: Cat is approved by 22 of 22 non-Dog-partisans, and in STAR advances on score (78) then wins the runoff 15–7. These two methods recover the Condorcet winner.

So the candidate a majority actually prefers head-to-head (**Cat**) wins **Approval and STAR** and loses **Plurality and IRV** — the whole argument for cardinal methods in one 22-voter poll.

## Per-race engine reports

Each race's full LH tabulation is in its `_tabulated` mirror:

- Plurality → [`…_plurality_tabulated.txt`](pet_poll_four_methods_tabulated/bv2132_ykjjhy_pet_plurality_tabulated.txt) (Dog 9, Fish 7, Cat 6)
- RCV-IRV → [`…_irv_tabulated.txt`](pet_poll_four_methods_tabulated/bv2132_ykjjhy_pet_irv_tabulated.txt) (Cat eliminated R1 → Fish 13, Dog 9)
- Approval → [`…_approval_tabulated.txt`](pet_poll_four_methods_tabulated/bv2132_ykjjhy_pet_approval_tabulated.txt) (Cat 22, Fish 13, Dog 9)
- STAR → [`…_star_tabulated.txt`](pet_poll_four_methods_tabulated/bv2132_ykjjhy_pet_star_tabulated.txt) (Cat 78 & Fish 62 advance; Cat wins runoff 15–7)

## Provenance

Created via [`create_bv_test_election.py`](../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py) as a single multi-race BV election (`ykjjhy`) with made-up ballots — the first multi-race case built through the script. BetterVoting's Results for all four races match our engines exactly.

## The pets set

- **BV2132 — Pet poll (three winners)** — this one (Cat wins Approval *and* STAR).
- [BV2133 — Pet poll II (four winners)](../pet_poll_four_winners/bv2133_dyxrbr_pet_poll_four_winners.md) — a 4th pet splits Approval from STAR too, so all four methods disagree.
- [Pets Governance (five methods, LH-only)](../pets_governance/pets_gov_five_positions.md) — multi-winner: majoritarian sweep vs proportional representation.

## See also

- Folder overview: [pet_poll_four_methods — README](README.md)
- The single-method center-squeeze counterpart: [BV2131 — Tennessee (Ranked Robin)](../../05_Ranked_Robin/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md)
- The real inspiration: Equal.Vote's `meta_pets` ("What Makes the Best Pet?"), whose four methods barely diverge — this case tunes the ballots so they do.
- [Condorcet efficiency — topic hub](../../00_start_here/topics/condorcet/README.md) · [Glossary](../../00_start_here/GLOSSARY.md)
