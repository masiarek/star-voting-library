# Alaska 2022 — a real RCV-IRV center squeeze, spoiler, *and* monotonicity failure

*Alaska's August 2022 U.S. House special election is the most-cited real-world example
of RCV-IRV misfiring — because it hit **three** of IRV's pathologies at once, in a
high-profile federal race. It's the case advocates on both sides keep pointing to.*

→ Interactive breakdown (Equal Vote): [realrcv.equal.vote/alaska22](https://realrcv.equal.vote/alaska22)
· concepts: [center squeeze](RCV_IRV_center_squeeze.md) · [non-monotonicity](RCV_IRV_non_monotonicity.md)
· [the spoiler effect](../spoiler_effect.md)

---

## What happened

Three candidates, one seat, counted by RCV-IRV (Hare):

- **Mary Peltola** (Democrat)
- **Sarah Palin** (Republican)
- **Nick Begich** (Republican)

The count, round by round (certified results):

| Round | Peltola | Palin | Begich |
|---|--:|--:|--:|
| **First choices** | 40.2% | 31.3% | **28.5%** ← fewest, eliminated |
| **After Begich's ballots transfer** | 51.5% ✅ | 48.5% | — |

Begich had the fewest first choices, so RCV-IRV eliminated him. His ballots split
roughly half to Palin, under a third to Peltola, and about a fifth **exhausted** (those
voters ranked only Begich). Peltola won the runoff over Palin.

## Why it's a teaching case: three failures in one election

**1. Center squeeze — the Condorcet winner was eliminated.**
Head-to-head, **Begich beat *both* Peltola and Palin** — he was the
[Condorcet winner](../RCV_Ranked_Robin/ranked_robin.md), the candidate a majority
preferred over each rival one-on-one. But because he was too few voters' *first* choice,
IRV cut him in the first round. That's the textbook [center squeeze](RCV_IRV_center_squeeze.md):
the broadly-acceptable middle candidate is knocked out for lacking first-place "core
support," even though he'd have won every direct matchup.

**2. Spoiler — Palin spoiled the race for Begich.**
Had Palin not run, Begich would have won (his support plus Palin's beats Peltola). Palin
couldn't win, but her presence changed *who did* — the definition of a
[spoiler](../spoiler_effect.md). So RCV-IRV did **not** deliver the spoiler-free election
it's marketed as.

**3. Non-monotonicity / favorite betrayal.**
The result was also a documented [monotonicity](RCV_IRV_non_monotonicity.md) failure:
a bloc of Palin-first voters would have gotten a **preferred** outcome (Begich instead of
Peltola) by ranking Peltola *higher* — i.e. by **not** putting their favorite first. IRV
punished sincere voting, exactly the [favorite-betrayal](../../interviews_conversations/favorite_betrayal_voting_301.md)
incentive reform is supposed to remove.

## Why it matters

Alaska 2022 isn't a contrived textbook ballot — it's a **real federal election** where
the winner was not the candidate a majority preferred head-to-head, and where a
losing candidate flipped the result. Methods that read the whole ballot handle this
cleanly: [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) (and any Condorcet method)
would have elected Begich, and [STAR](../STAR_Voting/STAR_start_here.md) resolves the
squeeze through its automatic runoff rather than by first-choice elimination. The
lesson isn't "ranked ballots are bad" — it's that the **tabulation** matters, and Hare
elimination is the part that failed here.

For a follow-on: after 2022, party elites pressured a Republican to drop out of the
2024 race to avoid a repeat — the real-world "exit incentive" a spoiler-prone method
creates (see [origins & spread](RCV_IRV_history.md)).

Sources: [Alaska 2022 — Equal Vote realrcv](https://realrcv.equal.vote/alaska22),
[2022 Alaska's at-large special election — Wikipedia](https://en.wikipedia.org/wiki/2022_Alaska%27s_at-large_congressional_district_special_election),
[Graham-Squire & McCune, "An Examination of the 2022 Alaska Special Election"](https://arxiv.org/abs/2209.04764)

# file: RCV_IRV_alaska_2022.md
