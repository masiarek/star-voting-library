# The whole Condorcet family splits — Minimax & Schulze pick Ava, Ranked Pairs picks Ben, on one set of ballots

*Generated from [`cycle_family_splits_c5_b77.yaml`](../cycle_family_splits_c5_b77.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ava

**Official tie-break (lot) order:** Ava > Ben > Cole > Dana > Ezra — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The five-candidate profile behind the "…but they don't always agree" table in
00_start_here/RCV_Ranked_Robin/cycle_resolution.md. 77 members of a program
committee rank five finalists, and majority preference is knotted about as
badly as it can be: there is no Condorcet winner and the Smith set is ALL FIVE
candidates — every finalist is in a beat-cycle with the rest.

On these identical ballots the Condorcet family gives four different answers:

    Copeland (Ranked Robin)  Ava, Ben   (tie — both go 2-2; LH breaks it by margin)
    Minimax                  Ava
    Schulze (beat path)      Ava
    Ranked Pairs             Ben
    Split Cycle              Ava, Ben

Minimax and Schulze land on Ava (her worst defeat is the mildest); Ranked Pairs
locks the biggest margins first and they carry Ben; Copeland can't separate the
two, and Split Cycle deliberately returns both. That is the entire lesson of the
cycle-resolution page in one election: "Condorcet method" names a FAMILY, and
inside a cycle the family stops agreeing.

The LH engine tabulates the Copeland column (= Ranked Robin) and breaks the
Ava/Ben tie by total margin, then lot. The other four rules are printed by:
  uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py \
    method_comparisons/cycle_resolution/cases/cycle_family_splits_c5_b77.yaml

LH-only (no BetterVoting election): the result is a Copeland tie, and BV breaks
Copeland ties at random, so this can't be frozen on BV. Constructed by search
and verified with pref_voting (it is NOT a profile from the literature — an
earlier draft mis-attributed a 100-voter version to Heitzig; this replaces it
with a real, reproducible one). Companion: cycle_schulze_vs_ranked_pairs_c4_b40.yaml.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:Ezra>Ava>Dana>Ben>Cole
7:Ezra>Cole>Ava>Dana>Ben
14:Ben>Ava>Ezra>Cole>Dana
8:Dana>Ben>Ava>Ezra>Cole
5:Cole>Ava>Dana>Ezra>Ben
11:Dana>Ben>Ava>Cole>Ezra
13:Ezra>Cole>Ava>Ben>Dana
7:Ben>Ava>Cole>Ezra>Dana
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/cycle_family_splits_c5_b77_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 77 ballots (ranked ballots).

Ballots:
    12 × Ezra > Ava > Dana > Ben > Cole
     7 × Ezra > Cole > Ava > Dana > Ben
    14 × Ben > Ava > Ezra > Cole > Dana
     8 × Dana > Ben > Ava > Ezra > Cole
     5 × Cole > Ava > Dana > Ezra > Ben
    11 × Dana > Ben > Ava > Cole > Ezra
    13 × Ezra > Cole > Ava > Ben > Dana
     7 × Ben > Ava > Cole > Ezra > Dana

Round-Robin — every pair, head-to-head (For – Against):
   Ava   beats Ezra   45 – 32
   Ezra  beats Dana   53 – 24
   Ben   beats Ezra   40 – 37
   Ezra  beats Cole   54 – 23
   Ava   beats Dana   58 – 19
   Ben   beats Ava    40 – 37
   Ava   beats Cole   52 – 25
   Dana  beats Ben    43 – 34
   Cole  beats Dana   46 – 31
   Ben   beats Cole   52 – 25

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |     Ezra     |    Ava      |    Dana     |    Ben      |    Cole     |
---------------------------------------------------------------------------------
  Ezra > |     ---      |32 -  0 - 45 |53 -  0 - 24 |37 -  0 - 40 |54 -  0 - 23 |
   Ava > | 45 -  0 - 32 |    ---      |58 -  0 - 19 |37 -  0 - 40 |52 -  0 - 25 |
  Dana > | 24 -  0 - 53 |19 -  0 - 58 |    ---      |43 -  0 - 34 |31 -  0 - 46 |
   Ben > | 40 -  0 - 37 |40 -  0 - 37 |34 -  0 - 43 |    ---      |52 -  0 - 25 |
  Cole > | 23 -  0 - 54 |25 -  0 - 52 |46 -  0 - 31 |25 -  0 - 52 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ava        3–1–0         3     +76  Ezra, Cole, Dana
    2  Ben        3–1–0         3     +24  Ava, Ezra, Cole
    3  Ezra       2–2–0         2     +44  Cole, Dana
    4  Cole       1–3–0         1     -70  Dana
    5  Dana       1–3–0         1     -74  Ben

Winner — Ranked Robin (RCV-RR): Ava
   *** 2 candidates tie for the most wins (Ava, Ben) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/cycle_resolution/cases/cycle_family_splits_c5_b77.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_copeland_ties_c4_b21](cycle_copeland_ties_c4_b21.md) · [cycle_schulze_vs_ranked_pairs_c4_b40](cycle_schulze_vs_ranked_pairs_c4_b40.md)
