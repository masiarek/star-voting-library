# Team lunch on a choose-one ballot — a dead tie (BV2257, q2rkfm)

*Generated from [`lunch_choose_one_dead_tie.yaml`](../lunch_choose_one_dead_tie.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../00_start_here) · **1 seat** · **Expected winner:** Sushi

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/q2rkfm) · **[results ↗](https://bettervoting.com/q2rkfm/results)** (election `q2rkfm`).

**Official tie-break (lot) order:** Sushi > Tacos > Pizza — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Five coworkers, three lunches, and the old ballot: mark one box.

Sushi 2 · Tacos 2 · Pizza 1 — and that is the entire count. Nothing on these
ballots can separate Sushi from Tacos, so the pre-published lot order decides.
The Pizza-fan is the one voter who could have broken the tie, and a choose-one
ballot gave them no way to say so.

Same five people, same opinions, on a 5-star ballot:
01_STAR/_main/cases/bv2184_fyy886_lunch_vote.yaml — where STAR elects Pizza,
the compromise everyone is happy with.

TIEBREAK — this case is NOT deterministic, on purpose. LH resolves the 2-2 tie
with the pre-published lot order below and elects Sushi. BetterVoting resolves
it at RANDOM (its frozen export records tieBreakType: "random"); the live run
happened to land on Sushi too, but a re-run could just as well say Tacos. That
is the honest state of a tied choose-one election, not an engine disagreement.

Live results (BV2257): https://bettervoting.com/q2rkfm/results
Lesson: 06_Other/Plurality/README.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Sushi,Tacos,Pizza
    1,    0,    0   # Sushi-lover
    1,    0,    0   # Sushi-lover
    0,    1,    0   # Taco-lover
    0,    1,    0   # Taco-lover
    0,    0,    1   # Pizza-fan
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/lunch_choose_one_dead_tie_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 5 ballots.

                   Sushi  Tacos  Pizza 
  Sushi-lover        X      -      -   
  Sushi-lover        X      -      -   
  Taco-lover         -      X      -   
  Taco-lover         -      X      -   
  Pizza-fan          -      -      X   

  Count the marks:  Sushi 2 · Tacos 2 · Pizza 1

 A 2-way tie for first: Sushi, Tacos — 2 mark(s) each.
   Counting the marks is all a choose-one ballot can do, so the ballots cannot break it;
   the pre-published lot order decides: ['Sushi', 'Tacos', 'Pizza'].

[Lot-decided tie — rare]
  ⚠ The result here was set by lot, not by the votes.

Winner — Choose-One / Plurality Voting Method (single winner)
 Sushi   (2 of 5 marks, by lot)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/Plurality/cases/lunch_choose_one_dead_tie.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
