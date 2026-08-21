---
search:
  exclude: true
---

# Matchups won, not preference votes — the rung that eliminates a Condorcet loser

*Generated from [`tie_break_ladder_matchups_eliminate_loser.yaml`](../tie_break_ladder_matchups_eliminate_loser.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara > Doug — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

A four-way scoring-round tie in which the FIRST rung has to do real work, and the
two plausible readings of that rung disagree.
All four candidates finish the scoring round on 11. Ada, Ben and Cara form a
head-to-head cycle (Ada beats Ben, Ben beats Cara, Cara beats Ada); Doug loses to
all three, so he is the Condorcet loser. But Doug also holds the most maximum-score
votes — two 5s to everyone else's one.
The published Equal Vote protocol resolves a tie of three or more by "comparing the
tied candidates head to head and eliminating the candidate(s) who lost the most
match-ups", so Doug goes out on rung 1 with zero matchups won and never reaches the
five-star rung. Read the rung instead as a SUM of pairwise preference votes and all
four tie at 6, Doug survives to rung 2, and his two 5s carry him into the runoff —
a candidate no voter majority prefers over anyone.
This case exists to hold the engine to the first reading. A symmetric tie cannot
test it, because perfect symmetry ties both statistics; the tie has to be
asymmetric in matchups and symmetric in score, which is what these five ballots do.
Note what the answer key can and cannot see: Ada wins under BOTH readings, because
a candidate who loses every matchup also loses the runoff he was wrongly advanced
into. What changes is the FINALIST PAIR — Ada vs Ben when the rung is read
correctly, Doug vs Ada when it is not — so the guard here is the _tabulated mirror
(checked by tests/test_tabulated_mirrors_current.py), not expected_winners. A
regression shows up as "Doug -- 0" disappearing from the first tiebreaker.
The lot order is published so nothing in the case depends on column order.
See 07_Concepts/tabulation_engines/tiebreak_ladders.md and
01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cara,Doug
0,0,0,5      # Doug bloc — a 5 for Doug, nothing for anyone else
0,0,0,5      # Doug bloc
5,4,2,1      # Ada first
2,5,4,0      # Ben first
4,2,5,0      # Cara first
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Ada
  Choose-One (Plurality) = Doug   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Ada,Ben,Cara,Doug
    2 ×   0,  0,   0,   5
    1 ×   5,  4,   2,   1
    1 ×   2,  5,   4,   0
    1 ×   4,  2,   5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 11 -- Tied for first place
   Ben           -- 11 -- Tied for first place
   Cara          -- 11 -- Tied for first place
   Doug          -- 11 -- Tied for first place
 There's a four-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Ada           -- 2 -- Tied for first place
   Ben           -- 2 -- Tied for first place
   Cara          -- 2 -- Tied for first place
   Doug          -- 0
   Equal Support -- 0
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Ada           -- 1 -- Tied for first place
   Ben           -- 1 -- Tied for first place
   Cara          -- 1 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ada', 'Ben', 'Cara', 'Doug']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ada', 'Ben', 'Cara']
  Resolved: ['Ada', 'Ben'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 2 -- First place
   Ben           -- 1
   Equal Support -- 2
 Ada wins.
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Ada 2 (67%)  ·  Ben 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ada
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
        Note: Ada, Ben, Cara and Doug tied at 11 in the Scoring Round, and the
              lot rung (the ballots could not separate them) advanced Ada and
              Ben. The * marks who advanced, not who scored highest.

               |   * Ada    |  * Ben    |    Cara   |    Doug   |
-----------------------------------------------------------------
       * Ada > |    ---     |2 - 2 - 1  |1 - 2 - 2  |3 - 0 - 2  |
       * Ben > | 1 - 2 - 2  |   ---     |2 - 2 - 1  |3 - 0 - 2  |
        Cara > | 2 - 2 - 1  |1 - 2 - 2  |   ---     |3 - 0 - 2  |
        Doug > | 2 - 0 - 3  |2 - 0 - 3  |2 - 0 - 3  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Ada > Ben > Cara > Ada)

[Condorcet Loser]
  Condorcet Loser: Doug — loses every head-to-head matchup — elected by Choose-One (Plurality)!

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        1  1  0  1  0  2  |    11   2.2
Ben        1  1  0  1  0  2  |    11   2.2
Cara       1  1  0  1  0  2  |    11   2.2
Doug       2  0  0  0  1  2  |    11   2.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/tie_break_ladder_matchups_eliminate_loser_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/03_Criteria/tie_break_ladder/cases/tie_break_ladder_matchups_eliminate_loser.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2180_fp62p2_ice_cream_ladder](bv2180_fp62p2_ice_cream_ladder.md) · [bv2276_qhjyr2_second_finalist_tie](bv2276_qhjyr2_second_finalist_tie.md) · [bv830_vb3xv2_no_condorcet_tie_score](bv830_vb3xv2_no_condorcet_tie_score.md)
