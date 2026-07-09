# A perfect 'Condorcet component' (30 voters) — every count ties; any winner is an artifact

*Generated from [`edelman_perfect_component_c3_b30.yaml`](../edelman_perfect_component_c3_b30.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The building block of Edelman's "Myth of the Condorcet Winner" argument
(22 Supreme Court Economic Review 207 (2015), Section III): 10 Ada>Ben>Cara,
10 Ben>Cara>Ada, 10 Cara>Ada>Ben — a perfectly symmetric Condorcet cycle.
Every pairwise vote is exactly 20-10 (in a cycle), every score sum is 70,
every candidate holds ten 5s. Edelman: "the only reasonable conclusion is
that all three alternatives are tied" — a bloc like this, he argues,
should cancel out of any larger electorate.

Watch the engine agree: the scoring round ties 70/70/70, the pairwise
tiebreaker ties 30/30/30, the five-star tiebreaker ties 10/10/10 — a true
dead rung, resolved only by the pre-published lot (pinned below), and the
engine flags "[Lot-decided tie — rare]: the result here was set by lot,
not by the votes." Then the cycle itself decides the runoff: whichever
two candidates the lot picks, one beats the other 20-10. The winner is
100% agenda artifact — which IS the lesson. LH-only (a BetterVoting
version would resolve its ties at random, so the result can't be frozen).
The 81-voter live case this bloc embeds into:
bv2173_gmfv4c_edelman_saari_cancellation.yaml

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cara
10:5,2,0   # Ada > Ben > Cara
10:0,5,2   # Ben > Cara > Ada
10:2,0,5   # Cara > Ada > Ben
```

## What the engine says

Full report from the [`_tabulated` mirror](../edelman_condorcet_myth_tabulated/edelman_perfect_component_c3_b30_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ada     |   * Ben     |     Cara    |
-------------------------------------------------------------
         * Ada > |     ---      |20 -  0 - 10 |10 -  0 - 20 |
         * Ben > | 10 -  0 - 20 |    ---      |20 -  0 - 10 |
          Cara > | 20 -  0 - 10 |10 -  0 - 20 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Ada > Ben > Cara > Ada)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 30 ballots.
Count × Ada,Ben,Cara
   10 ×   5,  2,   0
   10 ×   0,  5,   2
   10 ×   2,  0,   5

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ada        10   0   0  10   0  10  |    70   2.3
Ben        10   0   0  10   0  10  |    70   2.3
Cara       10   0   0  10   0  10  |    70   2.3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 70 -- Tied for first place
   Ben           -- 70 -- Tied for first place
   Cara          -- 70 -- Tied for first place
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Ada           -- 30 -- Tied for first place
   Ben           -- 30 -- Tied for first place
   Cara          -- 30 -- Tied for first place
   Equal Support --  0
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Ada           -- 10 -- Tied for first place
   Ben           -- 10 -- Tied for first place
   Cara          -- 10 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ada', 'Ben', 'Cara']

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
   Ada           -- 20 -- First place
   Ben           -- 10
   Equal Support --  0
 Ada wins.
   Runoff math:
     30  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     30  voters with a preference  (majority = 16)
           Ada 20 (67%)  ·  Ben 10 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ada
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/edelman_condorcet_myth/edelman_perfect_component_c3_b30.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2173_gmfv4c_edelman_saari_cancellation](bv2173_gmfv4c_edelman_saari_cancellation.md)
