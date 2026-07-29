# BV2131 — Tennessee capital: Ranked Robin elects the Condorcet center (Nashville)

*Generated from [`bv2131_tennessee_condorcet_center_vqyqkr.yaml`](../bv2131_tennessee_condorcet_center_vqyqkr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../concepts) · **1 seat** · **Expected winner:** Nashville

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vqyqkr) · **[results ↗](https://bettervoting.com/vqyqkr/results)** (election `vqyqkr`).

**Official tie-break (lot) order:** Memphis > Nashville > Chattanooga > Knoxville — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The textbook Tennessee example, and the first BV-backed Ranked Robin case. Four cities; each voter ranks by geographic distance; blocs weighted by population (Memphis 42, Nashville 26, Chattanooga 15, Knoxville 17). On ONE ranked ballot set the three methods split three ways: plurality would elect Memphis (largest first-choice bloc), RCV-IRV elects Knoxville (Nashville is squeezed out in round 2), and Ranked Robin elects the geographic-center consensus, Nashville — who beats every rival head-to-head, the Condorcet winner. Cross-verified: LH native run_ranked_robin, BetterVoting RankedRobin.ts, and pref_voting's Copeland all elect Nashville (Copeland 3, no tiebreak needed). Live results: https://bettervoting.com/vqyqkr/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
42:Memphis>Nashville>Chattanooga>Knoxville
26:Nashville>Chattanooga>Knoxville>Memphis
15:Chattanooga>Knoxville>Nashville>Memphis
17:Knoxville>Chattanooga>Nashville>Memphis
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 100 ballots (ranked ballots).

Ballots:
    42 × Memphis > Nashville > Chattanooga > Knoxville
    26 × Nashville > Chattanooga > Knoxville > Memphis
    15 × Chattanooga > Knoxville > Nashville > Memphis
    17 × Knoxville > Chattanooga > Nashville > Memphis

Round-Robin — every pair, head-to-head (For – Against):
   Nashville    beats Memphis       58 – 42
   Chattanooga  beats Memphis       58 – 42
   Knoxville    beats Memphis       58 – 42
   Nashville    beats Chattanooga   68 – 32
   Nashville    beats Knoxville     68 – 32
   Chattanooga  beats Knoxville     83 – 17

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
                |    Memphis    |  Nashville   | Chattanooga  |  Knoxville   |
------------------------------------------------------------------------------
      Memphis > |      ---      |42 -  0 - 58  |42 -  0 - 58  |42 -  0 - 58  |
    Nashville > | 58 -  0 - 42  |     ---      |68 -  0 - 32  |68 -  0 - 32  |
  Chattanooga > | 58 -  0 - 42  |32 -  0 - 68  |     ---      |83 -  0 - 17  |
    Knoxville > | 58 -  0 - 42  |32 -  0 - 68  |17 -  0 - 83  |     ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate    W–L–T  Copeland  Margin  Beats
    1  Nashville    3–0–0         3     +88  Chattanooga, Knoxville, Memphis
    2  Chattanooga  2–1–0         2     +46  Knoxville, Memphis
    3  Knoxville    1–2–0         1     -86  Memphis
    4  Memphis      0–3–0         0     -48  —

Winner — Ranked Robin (RCV-RR): Nashville
   beats every opponent head-to-head — the Condorcet winner.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): Nashville
   Outside (3):        Memphis, Chattanooga, Knoxville
   One member ⇒ Nashville is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Nashville is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 00_start_here/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2131_tennessee_condorcet_center_vqyqkr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/rr_vs_irv_plurality/cases/bv2131_tennessee_condorcet_center_vqyqkr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
