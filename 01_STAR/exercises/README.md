# Exercises — predict, then peek

Worked problems with solutions. Each exercise poses a small election, asks you to **commit to a prediction on paper**, and only then lets you open the solution — every part behind a click, with the engine's actual output embedded. The format is the classroom classic (practice problems *with* solutions), borrowed with attribution from Brendan W. Sullivan's *An Introduction to the Math of Voting Methods* (2022).

Three layers of answer key, so you can trust it:

1. **The collapsed solutions** on each exercise page — worked arithmetic plus the relevant slice of engine output.
2. **The runnable YAML** — each election is a real file you can tabulate yourself; the command is on every page.
3. **The `_tabulated` mirror** — the full audit report (preference matrix, Condorcet check, score distribution, method divergence), one per election in the `exercises_tabulated/` subfolder, linked from every exercise page. The `expected_winners` keys are checked by the engine's regression suite for every single-winner score file; the multi-winner, Approval, and ranked files (9, 12, 13's approval variants, 14) document their keys the same way, so the answers can't silently rot.
4. **The frozen BetterVoting export** — BV-backed exercises keep their full `*_bv_export.json` (Election + Ballots + Results) beside the YAML: the canonical record of the live election at freeze time, even if strangers vote on the public pages later.

## The exercises

| Exercise | The question | Concepts | Files |
|---|---|---|---|
| **[1 — Two districts, one mayor](ex01_two_districts.md)** | Avery wins West. Avery wins East. Who wins the city? | consistency (join-consistency) · runoff pairing · why this is *not* a [summability](../../00_start_here/topics/summability/README.md) failure | [west](ex01_district_west.yaml) · [east](ex01_district_east.yaml) · [combined](ex01_district_combined.yaml) · live: [W↗](https://bettervoting.com/d3b9wc/results) [E↗](https://bettervoting.com/rhbfj7/results) [C↗](https://bettervoting.com/923q3d/results) |
| **[2 — The tenth ballot](ex02_tenth_ballot.md)** | A mislaid ballot scores the announced winner 5 of 5. Can counting it hurt him? | [participation](../../00_start_here/topics/participation/README.md) / no-show paradox · runoff-slot spoiler | [nine](ex02_nine_ballots.yaml) · [ten](ex02_tenth_ballot.yaml) · [Bella exits](ex02_bella_exits.yaml) |
| **[3 — One electorate, five verdicts](ex03_five_verdicts.md)** | Nine snack ballots, five tabulations. How many different winners? | ballot vs method · the Condorcet loser wins Choose-One · Approval bridge rule | [yaml](ex03_five_verdicts.yaml) · live: [↗](https://bettervoting.com/ywqhq4/results) |
| **[4 — Lillehammer 1994](ex04_olympics_1994.md)** | Real Olympic judges' ballots: Score says Kerrigan, STAR says Baiul. Which matches history? | rank→score maps · Score vs STAR · Pareto dominance | [yaml](ex04_olympics_1994.yaml) |
| **[5 — The squeezed bridge-builder](ex05_center_squeeze.md)** | Every voter scores Brook 3+. Does RCV-IRV ever find that out? | [center squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md) · Condorcet winner · first-choice bottleneck | [yaml](ex05_center_squeeze.yaml) · live: [↗](https://bettervoting.com/6bry7c/results) |
| **[6 — Bullet voting backfires](ex06_bullet_backfire.md)** | Four fans zero their second choice to lift their favorite. What do they wake up to? | [bullet voting](../../00_start_here/topics/strategic_voting.md) · when the gamble is safe and when it detonates | [honest](ex06_bullet_honest.yaml) · [strategic](ex06_bullet_backfire.yaml) · live: [H↗](https://bettervoting.com/x4dkfd/results) [S↗](https://bettervoting.com/7f4f7q/results) |
| **[7 — The vanishing votes](ex07_vanishing_votes.md)** | "3 of 9 voters had a preference." Did six votes vanish? | [Equal Support](../../00_start_here/STAR_Voting/the_count/runoff_percentages.md) · the two denominators · zero vs blank | [yaml](ex07_vanishing_votes.yaml) |
| **[8 — Build your own reversal](ex08_build_a_reversal.md)** | Construct "top scorer loses" yourself — then prove 3 voters is the floor. | constructive design · breadth vs depth · a minimality proof | [2-cand](ex08_minimal_reversal_2c.yaml) · [3-cand](ex08_minimal_reversal_3c.yaml) |
| **[9 — Game night: nobody is unbeatable](ex09_game_night_cycle.md)** | A rock-paper-scissors cycle with no Condorcet winner. Who deserves game night? | pairwise matrix · [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md)'s ladder · Smith set · (LH-only: BV would coin-flip) | [yaml](ex09_game_night_cycle.yaml) *(ranked ballots)* |
| **[10 — Later-no-harm, both readings](ex10_later_no_harm.md)** | Did the fans' generous 3s harm Amir — or did their 0s hide Bess? | [later-no-harm](../../00_start_here/GLOSSARY.md) · LNH ≠ favorite betrayal · the trade IRV makes instead | [reticent](ex10_reticent.yaml) · [generous](ex10_generous.yaml) · live: [R↗](https://bettervoting.com/g6q42v/results) [G↗](https://bettervoting.com/yyhj9x/results) |
| **[11 — Recruit a spoiler](ex11_recruit_a_spoiler.md)** | Brett's campaign can't flip a voter — so it adds a candidate. Under which counting rules does the trick pay? | [spoiler effect](../../00_start_here/topics/spoiler_effect.md) · clones · vote-splitting as ballot design | [base](ex11_two_way_base.yaml) · [spoiler added](ex11_spoiler_added.yaml) · live: [B↗](https://bettervoting.com/ggg7hd/results) [S↗](https://bettervoting.com/93gjx6/results) |
| **[12 — Two seats, one neighborhood](ex12_bloc_vs_proportional.md)** | Same ten ballots: Bloc STAR seats Asa + Bram; Allocated Score seats Asa + Cleo. Which board is "fair"? | [multi-winner design](../../00_start_here/topics/electing_more_than_one.md) · Bloc vs proportional · quotas spend ballot weight | [bloc](ex12_bloc_sweep.yaml) · [allocated](ex12_proportional_share.yaml) · live: [↗](https://bettervoting.com/89wwvr/results) |
| **[13 — Where do you draw the line?](ex13_draw_the_line.md)** | One honest electorate, three approval thresholds — three different Approval winners (and Score vs STAR split too). | [Approval](../../04_Approval/README.md)'s free parameter · no canonical sincere ballot · devolution to Choose-One | [opinions](ex13_opinions.yaml) · [3+](ex13_approve3.yaml) · [4+](ex13_approve4.yaml) · [5s](ex13_bullet.yaml) · live: [↗](https://bettervoting.com/qdtqf2/results) |
| **[14 — The transfer machine](ex14_transfer_machine.md)** | Follow one STV ballot: 4/5 of it elects Austen, the last 1/5 rides on to elect Camus. | Droop quota · surplus & elimination transfers · proportionality on ranked ballots · a live BV bug, documented | [yaml](ex14_two_novels.yaml) · [fullranks probe](ex14_two_novels_fullranks.yaml) · live: [vote↗](https://bettervoting.com/tk776t) *(BV results error — see page)* |

**A suggested path:** start with the reading drills (**3**, **7**), then the mechanisms (**5**, **6**, **11**), then the criteria probes (**1**, **2**, **10**), then the capstones (**4**, **8**, **9**) — and finish in the multi-winner wing (**12**, **14**) with the ballot-design coda (**13**). The set sits at the **Voting 201–301** end of the [curriculum](../../00_start_here/CURRICULUM.md), framed per [reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md).

## How to use them

Paper first: tabulate the scoring round, pick the finalists, run the runoff by hand. Then open the collapsed solution and check. Then run the file:

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex01_district_west.yaml
```

Teaching a group? Each exercise works as a live segment: show the ballots, take predictions, tabulate on screen, then argue about what the "right" winner even means.

## Sources & fairness

Exercises 1–2 adapt ballot data from [RangeVoting.org](https://rangevoting.org) (a Score-voting advocacy site — its framing favors Score, the arithmetic is method-neutral) as posed in Sullivan's method-neutral textbook; exercise 3 borrows his one-electorate-many-methods format with this repo's own ballots; exercise 4 uses the real 1994 Olympics ordinals as reproduced there; exercises 5–14 are original to this repo (13 borrows Sullivan's imposing-approvals-on-scores move). The criticism is deliberately symmetric: STAR fails criteria in 1, 2, and 10; RCV-IRV takes the hit in 5 (and inside 10); Choose-One in 3 and 11; a *strategy* fails in 6; and 7 and 9 are pure reading drills. Exercise 13 puts Approval's threshold on the bench — with Score and STAR disagreeing on the same opinions in the same breath — and 12 and 14 have no villain at all: majoritarian vs proportional is a design choice, stated as one. Every solution links the counterweight pages ([STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md), [the four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)).

*More exercises are welcome — on deck: a quorum/turnout drill, a scale-granularity flip (0–5 vs 0–9 moving a finalist), and a Ranked Robin burial probe. Follow the set's pattern: one page, predictions before reveals, runnable YAMLs, tested answer keys.*

# file: README.md
