# Exercises — predict, then peek

Worked problems with solutions. Each exercise poses a small election, asks you to **commit to a prediction on paper**, and only then lets you open the solution — every part behind a click, with the engine's actual output embedded. The format is the classroom classic (practice problems *with* solutions), borrowed with attribution from Brendan W. Sullivan's *An Introduction to the Math of Voting Methods* (2022).

Three layers of answer key, so you can trust it:

1. **The collapsed solutions** on each exercise page — worked arithmetic plus the relevant slice of engine output.
2. **The runnable YAML** — each election is a real file you can tabulate yourself; the command is on every page.
3. **The `_tabulated` mirror** — the full audit report (preference matrix, Condorcet check, score distribution, method divergence), one per election in the `exercises_tabulated/` subfolder, linked from every exercise page. The `expected_winners` keys in the YAMLs are checked by the engine's regression suite, so the answers can't silently rot.

## The exercises

| Exercise | The question | Concepts | Files |
|---|---|---|---|
| **[1 — Two districts, one mayor](ex01_two_districts.md)** | Avery wins West. Avery wins East. Who wins the city? | consistency (join-consistency) · runoff pairing · Equal Support · why this is *not* a [summability](../../00_start_here/topics/summability/README.md) failure | [west](ex01_district_west.yaml) · [east](ex01_district_east.yaml) · [combined](ex01_district_combined.yaml) · live: [W↗](https://bettervoting.com/d3b9wc/results) [E↗](https://bettervoting.com/rhbfj7/results) [C↗](https://bettervoting.com/923q3d/results) |
| **[2 — The tenth ballot](ex02_tenth_ballot.md)** | A mislaid ballot scores the announced winner 5 of 5. Can counting it hurt him? | [participation](../../00_start_here/topics/participation/README.md) / no-show paradox · runoff-slot spoiler · which methods are immune | [nine ballots](ex02_nine_ballots.yaml) · [ten ballots](ex02_tenth_ballot.yaml) · [Bella withdraws](ex02_bella_exits.yaml) |

Both exercises live at the **Voting 301** end of the [curriculum](../../00_start_here/CURRICULUM.md) — they probe STAR's honest limits with sincere ballots, framed per [reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md).

## How to use them

Paper first: tabulate the scoring round, pick the finalists, run the runoff by hand. Then open the collapsed solution and check. Then run the file:

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex01_district_west.yaml
```

Teaching a group? Each exercise works as a live segment: show the ballots, take predictions, tabulate on screen, then argue about what the "right" winner even means.

## Sources & fairness

The ballot data is adapted from examples published on [RangeVoting.org](https://rangevoting.org) (a Score-voting advocacy site — its framing favors Score, the arithmetic is method-neutral) as posed in Sullivan's method-neutral textbook, with candidates renamed to house style. Both exercises show STAR *failing* a criterion on engineered ballots; that is deliberate — this repo teaches STAR with its limits stated honestly, and the counterweight pages ([STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md), the [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)) are linked from every solution.

*More exercises are welcome — candidates on deck: the 1994 Olympics figure-skating ballots (ranked → scored), and a Plurality-loser-wins-everything comparison. Follow this set's pattern: one page, predictions before reveals, runnable YAMLs, tested answer keys.*

# file: README.md
