---
search:
  exclude: true
---

# BV15 — Plurality + abstentions: the turnout undercount (Andre/Blake, 12 ballots)

*Generated from [`bv15_4h89vj_plurality_abstain.yaml`](../bv15_4h89vj_plurality_abstain.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Andre

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4h89vj) · **[results ↗](https://bettervoting.com/4h89vj/results)** (election `4h89vj`).

## Scenario

A REAL BetterVoting election (BV id 4h89vj), "B15 - Basic - 2 candidates -
Plurality - Abstain". Live results: https://bettervoting.com/4h89vj/results
Frozen raw export: bv15_4h89vj_plurality_abstain_bv_export.json.

This is the Plurality instance of BetterVoting issue #740
(github.com/Equal-Vote/bettervoting/issues/740 — note: bettervoting#740, the
repo moved from star-server, the NUMBER stayed). #740 is a REPORTING gap, not
a tabulation error: BetterVoting's results widget shows only the MEANINGFUL
ballots as "voters" and drops the fully-abstained ones from the headline
turnout. The winner is right; the displayed voter count is short by exactly
the number of abstentions.

Twelve ballots, two candidates (choose-one):

  Andre,Blake
  1,0   × 5   Andre  (a choose-one vote for Andre)
  0,1   × 2   Blake  (a choose-one vote for Blake)
  -,-   × 5   blank  — true abstentions (no vote for anyone)

BetterVoting's own summaryData (in the frozen export) counts it CORRECTLY:
nTallyVotes = 7, nAbstentions = 5 (7 + 5 = 12 cast). Andre 5, Blake 2 -> Andre
wins. So the data is present; #740 is only that the results UI never surfaces
the 5 abstentions / the 12-ballot total — it reports the 7 as if that were
turnout.

This file matches BV's method: Plurality (choose-one, 0/1 ballots). (An earlier
version modelled it as STAR 5/0, on the mistaken belief that the LH engine had
no Plurality method — it does: single-winner Plurality tabulates via the STAR
path, multi-winner as SNTV.) The self-reconciling turnout line still prints the
accounting #740 is missing: "12 ballots cast − 5 no-preference = 7 voters with a
preference" — the "stats for nerds" turnout breakdown #740 asks BV to add.

## Parameters (from the YAML)

```yaml
bv_test_id: BV15
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Andre,Blake
1,0
1,0
1,0
1,0
1,0
0,1
0,1
-,-
-,-
-,-
-,-
-,-
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv15_4h89vj_plurality_abstain_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 12 ballots.

                   Andre  Blake 
                     X      -   
                     X      -   
                     X      -   
                     X      -   
                     X      -   
                     -      X   
                     -      X   
                     -      -   
                     -      -   
                     -      -   
                     -      -   
                     -      -   

  Count the marks:  Andre 5 · Blake 2
  (5 ballot(s) marked nobody.)

Winner — Choose-One / Plurality Voting Method (single winner)
 Andre   (5 of 12 marks)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/pet_real_bv_election/cases/bv15_4h89vj_plurality_abstain.yaml
```

## See also

- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abstention_reconciliation_min_c2_b6](abstention_reconciliation_min_c2_b6.md) · [best_pet_c7_b461](best_pet_c7_b461.md) · [flat_scores_abstention_c3_b8](flat_scores_abstention_c3_b8.md) · [small_abstention_c2_b5](small_abstention_c2_b5.md)
