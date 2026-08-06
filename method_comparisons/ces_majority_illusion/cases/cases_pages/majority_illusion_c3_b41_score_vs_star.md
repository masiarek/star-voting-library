---
search:
  exclude: true
---

# The majority illusion — Score elects Brian, STAR elects Alice

*Generated from [`majority_illusion_c3_b41_score_vs_star.yaml`](../majority_illusion_c3_b41_score_vs_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn) · **1 seat** · **Expected winner:** Alice

## Scenario

The centerpiece example from Aaron Hamlin's "The Majority Illusion: What
Voting Methods Can and Cannot Do" (Center for Election Science), scaled
from 41,000 voters to 41 countable ballots and rendered on the 0-5 STAR
ballot (the article uses a 0-10 utility scale).

The article prints it to make one point: the Condorcet winner is not
always the best winner. Alice beats both rivals head-to-head, yet Brian
has by far the highest average score — 4.2 against Alice's 2.6 — because
almost everyone likes Brian and 20 of 41 voters score Alice at rock
bottom. Score voting (and Approval) elect Brian. The article's conclusion
is that cardinal methods "target a different metric altogether."

Two things the article does not say about its own example.

FIRST: Alice does not merely beat everyone head-to-head. Twenty-one of
41 voters — an outright 51.2% ABSOLUTE MAJORITY — score her strictly
highest. So the example is not really an argument against the Condorcet
criterion; it is an argument against the MAJORITY CRITERION, the
strongest of the three senses of "majority" the article itself sorts.

SECOND: STAR does not follow Score here. Brian leads the scoring round
174 to 105 and Alice reaches the runoff second — then wins it 21 to 20.
STAR's automatic runoff re-imposes exactly the majoritarian check the
article is arguing against, and elects the absolute-majority winner.

The profile also sits precisely on Equal Vote's Relaxed Majority
Criterion boundary: Alice's majority gives ONE rival "max minus 1"
(Brian a 4) and their favorite survives. Give Colin a 3 as well and
Alice drops out of the finals and Brian wins — the same one-rival /
two-rivals hinge as the BV95a / BV95b pair.

## Ballots

The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| Ballot as marked | Voters | Alice | Brian | Colin |
|:--|:--:|:--:|:--:|:--:|
| <img src="../img/majority_illusion_c3_b41_score_vs_star_ballot_1.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — 21 voters: Alice 5, Brian 4, Colin 0."> | 21 | 5 | 4 | 0 |
| <img src="../img/majority_illusion_c3_b41_score_vs_star_ballot_2.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — 10 voters: Alice 0, Brian 5, Colin 0."> | 10 | 0 | 5 | 0 |
| <img src="../img/majority_illusion_c3_b41_score_vs_star_ballot_3.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — 10 voters: Alice 0, Brian 4, Colin 5."> | 10 | 0 | 4 | 5 |

The same ballots as the file records them:

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alice,Brian,Colin
21:5,4,0
10:0,5,0
10:0,4,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Alice
  Approval = Brian   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Brian)
 - Runoff Round Winner   = (Alice)
  Candidate Brian earned the highest total score, but
  Candidate Alice won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 41 ballots.
Count × Alice,Brian,Colin
   21 ×     5,    4,    0
   10 ×     0,    5,    0
   10 ×     0,    4,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Brian         -- 174 -- First place
   Alice         -- 105 -- Second place
   Colin         --  50
 Brian and Alice advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alice         -- 21 -- First place
   Brian         -- 20
   Equal Support --  0
 Alice wins.
   Runoff math:
     41  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     41  voters with a preference  (majority = 21)
           Alice 21 (51%)  ·  Brian 20 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alice
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Alice    |  * Brian    |    Colin    |
-------------------------------------------------------------
       * Alice > |     ---      |21 -  0 - 20 |21 - 10 - 10 |
       * Brian > | 20 -  0 - 21 |    ---      |31 -  0 - 10 |
         Colin > | 10 - 10 - 21 |10 -  0 - 31 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Alice — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Colin — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alice      21   0   0   0   0  20  |   105   2.6
Brian      10  31   0   0   0   0  |   174   4.2
Colin      10   0   0   0   0  31  |    50   1.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/majority_illusion_c3_b41_score_vs_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/ces_majority_illusion/cases/majority_illusion_c3_b41_score_vs_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/majority_illusion_c3_b41_score_vs_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [majority_illusion_c3_b41_two_rivals](majority_illusion_c3_b41_two_rivals.md)
