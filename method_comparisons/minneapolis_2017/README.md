# Minneapolis 2017 — the big real election where RCV-IRV got it right

**Level: 201 · for debaters**

The honest counterweight to [Burlington 2009](../burlington_2009/README.md). Same investigation, opposite verdict: **105,928 real ballots**, 18 candidates plus write-ins, and every count in this library names the same mayor.

| Count | Winner |
|---|---|
| Choose-One Plurality (= round 1 first choices) | **Jacob Frey** — 26,104 |
| RCV-IRV (the rule actually in force) | **Jacob Frey** — won the final 46,704–34,970 |
| Any Condorcet count (Ranked Robin here) | **Jacob Frey** — beats all eighteen rivals head-to-head, **18–0** |

There is no center squeeze here, no cycle anywhere in the tournament, and no argument about who should have won. A repo that reproduces [Burlington](../burlington_2009/README.md) and [Alaska 2022](../alaska_2022/README.md) has to reproduce this too, or it is prosecuting rather than teaching — the [rarity of the failure cases](../../07_Concepts/topics/condorcet/README.md) is part of the evidence, and this is what the ordinary case looks like at full scale.

## What happened under RCV-IRV

```text title="Abridged for the lesson — not verbatim engine output"
ROUND 1                       PENULTIMATE                  FINAL
Frey          26104           Frey          39356          Frey    46704  Elected
Hoch          20122           Dehn          27357          Dehn    34970
Hodges        18905           Hodges        26865  out
Dehn          18100
Levy-Pounds   15715           Blank Votes   10906          Blank   22810
(+ 14 others)
```

Frey leads from the first count and is never headed. **Plurality would have named the same winner** — worth saying plainly in a library that criticises Plurality, because on this electorate the ranking changed nothing about the outcome.

## The number that still deserves an asterisk

Frey finishes on 46,704 of the 81,674 ballots still live — **57.2%** of those, and **44.1%** of the 105,928 people who actually voted. By the last round **24,254 ballots are out of the count** (22,847 exhausted, 1,369 blank, 38 truncated).

That is not apathy, it is arithmetic: Minneapolis allowed **three rankings against eighteen candidates**, so a voter who ranked three of the also-rans had no legal way to reach the final pair. Cite the 57.2% and the 44.1% together or neither — see [exhausted ballots](../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md).

## Where the count and the electorate do come apart

RCV-IRV got the **winner** right and the **runner-up** wrong.

```text
by head-to-head strength   Frey > Hodges > Hoch > Dehn > Levy-Pounds
IRV's last one standing    Frey, then ... Raymond Dehn
```

Dehn is the **fourth**-strongest of the five, yet he is the one left in the final pair — Hodges and Hoch were eliminated before him on first-choice counts, though both beat him head-to-head:

| Head-to-head | | |
|---|--:|:--|
| Betsy Hodges **beats** Raymond Dehn | 37,513 | 35,133 |
| Tom Hoch **beats** Raymond Dehn | 40,644 | 36,737 |

So "runner-up" under RCV-IRV means *last one eliminated*, not *second-strongest*, and the reported final margin **overstates** Frey's lead over his strongest challenger: he beats Hodges by 8,122 but Dehn by 11,734. This costs the method nothing on the winner and should not be inflated into a scandal — it is the ordinary consequence of eliminating on first choices, and it is exactly what a round-robin table is for.

The full tournament is a perfect transitive staircase — 18–0, 17–1, 16–2, all the way to 0–18, with the [Smith set](../../07_Concepts/topics/smith_set.md) a single name. Real electorates are not obliged to be this tidy; this one was.

## The cases

| Case (source) | Ballots | What it shows |
|---|--:|---|
| [page](cases/cases_pages/minneapolis_2017_irv.md) · [`minneapolis_2017_irv.yaml`](cases/minneapolis_2017_irv.yaml) | 105,928 | The instant runoff as it was actually counted, reproduced from the city's CVR. Frey elected; the exhaustion and the moving majority bar are the lesson. |
| [page](cases/cases_pages/minneapolis_2017_ranked_robin.md) · [`minneapolis_2017_ranked_robin.yaml`](cases/minneapolis_2017_ranked_robin.yaml) | 105,928 | The same ballots head-to-head. Frey is the Condorcet winner 18–0 — and the runner-up gap above is visible on sight. |

## Provenance, and how the ballots were converted

The CVR comes from [RCV Lab](../../07_Concepts/tabulation_engines/rcv_lab.md), which publishes it with the city's RCTab rules file:

```bash
curl -O https://rcv-lab.org/sample-data/minneapolis-mayor-2017/2017_minneapolis_mayor_cvr.xlsx
```

It is an ESS export — precinct, then three rank columns, then a count — with `undervote`, `overvote` and `UWI` labels. The conversion applies the published rules exactly: an **overvote skips to the next rank** rather than killing the ballot (269 ballots), a **repeated candidate is ignored** rather than exhausting (4,213), and a **second consecutive skipped rank truncates** the ballot there. That last rule sounds brutal and almost never is — of 13,456 ballots that hit it, 13,418 were trailing blanks with nothing after them, and only **38** actually discarded a later choice.

**Four independent numbers confirm the conversion**, none of them used to build it: the five leading first-choice tallies, the 1,369 blank ballots, that 38, and the final pair 46,704 / 34,970 — all match the published report. `pref_voting` separately confirms Frey as the unique Copeland winner (`AGREE ✓`).

Two honest discrepancies, both bookkeeping rather than result:

- **Round numbering.** The source reports six rounds, clearing write-ins alone and then thirteen candidates at once; this engine batch-eliminates on its own schedule and takes more rounds to get there. Every tally that appears in both reports is identical, including all four of the last rounds.
- **Exhausted totals differ by 37** out of 105,928 (0.03%) — an accounting boundary about which ballots count as exhausted and when. It was not chased down, and it moves no margin here: the smallest gap at stake is 1,196 votes.

## Running them

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minneapolis_2017/cases/minneapolis_2017_ranked_robin.yaml
```

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py method_comparisons/minneapolis_2017/cases/minneapolis_2017_ranked_robin.yaml
```

*Related: [Burlington 2009](../burlington_2009/README.md) · [Alaska 2022](../alaska_2022/README.md) · [exhausted ballots](../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md) · [Condorcet efficiency](../../07_Concepts/topics/condorcet/README.md) · [RCV Lab](../../07_Concepts/tabulation_engines/rcv_lab.md) · up: [method_comparisons](../README.md).*
