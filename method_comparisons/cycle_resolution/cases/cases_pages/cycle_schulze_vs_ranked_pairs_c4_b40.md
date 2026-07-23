# Same ballots, different Condorcet rule — Schulze says Ana, Ranked Pairs says Bruno, Split Cycle says both

*Generated from [`cycle_schulze_vs_ranked_pairs_c4_b40.yaml`](../cycle_schulze_vs_ranked_pairs_c4_b40.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ana

**Official tie-break (lot) order:** Ana > Bruno > Chloe > Diego — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The second worked profile behind "Cycle Resolution — why Minimax, Ranked Pairs,
and Schulze exist" (00_start_here/RCV_Ranked_Robin/cycle_resolution.md): the
point at which the Condorcet family stops agreeing. 40 members of a mural
committee rank four designs. Majority preference cycles:

    Ana beats Diego by 12 · Diego beats Bruno by 10 · Bruno beats Ana by 4

with Chloe hanging off the side (she loses to Ana and Bruno by 18 each, but
beats Diego by 12 — which is what pulls the whole field into the Smith set).
There is no Condorcet winner, and Copeland — the count under Ranked Robin —
ties Ana and Bruno at +1 each.

Now the refined rules split, on identical ballots:

    Minimax       Ana      (her worst defeat, 4, is the mildest in the field)
    Schulze       Ana
    Ranked Pairs  Bruno    (locks the big margins first, and they favor Bruno)
    Split Cycle   Ana AND Bruno

Split Cycle is the interesting one, and not because it is indecisive: it
discards the weakest defeat in every cycle, which erases Bruno>Ana (4) and
Diego>Bruno (10) alike, leaving BOTH Ana and Bruno undefeated. Its claim is
that Schulze and Ranked Pairs are not discovering a winner here — they are
applying a convention to a tie the ballots genuinely do not break. Split Cycle
hands the tie back rather than resolving it silently, which is why its winner
set is always a superset of theirs.

Verified with pref_voting:
  uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py \
    method_comparisons/cycle_resolution/cases/cycle_schulze_vs_ranked_pairs_c4_b40.yaml

LH-only (no BetterVoting election): the LH result is a Copeland tie, broken by
margin then lot, and BV breaks the same tie at random — so this one cannot be
frozen on BV. The companion case where every rule agrees:
cycle_copeland_ties_c4_b21.yaml

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
7:Ana>Bruno>Chloe>Diego
8:Bruno>Ana>Chloe>Diego
14:Diego>Bruno>Ana>Chloe
11:Chloe>Ana>Diego>Bruno
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/cycle_schulze_vs_ranked_pairs_c4_b40_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 40 ballots (ranked ballots).

Ballots:
     7 × Ana > Bruno > Chloe > Diego
     8 × Bruno > Ana > Chloe > Diego
    14 × Diego > Bruno > Ana > Chloe
    11 × Chloe > Ana > Diego > Bruno

Round-Robin — every pair, head-to-head (For – Against):
   Bruno  beats Ana     22 – 18
   Ana    beats Chloe   29 – 11
   Ana    beats Diego   26 – 14
   Bruno  beats Chloe   29 – 11
   Diego  beats Bruno   25 – 15
   Chloe  beats Diego   26 – 14

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |     Ana      |   Bruno     |   Chloe     |   Diego     |
--------------------------------------------------------------------
    Ana > |     ---      |18 -  0 - 22 |29 -  0 - 11 |26 -  0 - 14 |
  Bruno > | 22 -  0 - 18 |    ---      |29 -  0 - 11 |15 -  0 - 25 |
  Chloe > | 11 -  0 - 29 |11 -  0 - 29 |    ---      |26 -  0 - 14 |
  Diego > | 14 -  0 - 26 |25 -  0 - 15 |14 -  0 - 26 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ana        2–1–0         2     +26  Diego, Chloe
    2  Bruno      2–1–0         2     +12  Ana, Chloe
    3  Diego      1–2–0         1     -14  Bruno
    4  Chloe      1–2–0         1     -24  Diego

Winner — Ranked Robin (RCV-RR): Ana
   *** 2 candidates tie for the most wins (Ana, Bruno) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/cycle_resolution/cases/cycle_schulze_vs_ranked_pairs_c4_b40.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_copeland_ties_c4_b21](cycle_copeland_ties_c4_b21.md)
