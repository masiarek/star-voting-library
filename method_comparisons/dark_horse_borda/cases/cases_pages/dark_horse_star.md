# Dark Horse — STAR elects the honest winner A (Borda would elect the dark horse D)

*Generated from [`dark_horse_star.yaml`](../dark_horse_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

The "Dark Horse 3" scenario (Jameson Quinn's strategic-pathology set). Four
candidates; D is a nobody — the honest LAST choice of every voter (zero honest
support). Three factions, each with its own favorite:
  34: A>B>C>D    33: B>A>C>D    33: C>A>B>D
Under the BORDA count, each faction can bury its rivals by ranking the nobody D
SECOND; if all three do it, D wins with a total of 200 to A's 168 — elected with
literally zero honest support (verified with pref_voting; see the README). That is
the Dark Horse pathology, and it is a prisoner's dilemma: any one faction defecting
profits, but if all defect, they all lose to D.
This file shows the fix. Scored honestly on 0-5 (favorite 5, the compromise ~1, the
nobody 0), STAR elects the honest utilitarian/Condorcet winner A (scoring round
A 236, B 232, C 198; runoff A 34-33). The [Divergence from STAR] block confirms
Ranked Robin also elects A. Neither method rewards burying a rival behind D — under
a score ballot you give BOTH your rival and D a 0, so D never rises. Quinn's own
prescription: "don't force people to dishonestly support D merely to oppose someone."
Concept: ../../00_start_here/topics/strategic_pathologies.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D
34:5,1,0,0   # A > B > C > D   (honest — favorite 5, nobody D 0)
33:1,5,1,0   # B > A > C > D
33:1,1,5,0   # C > A > B > D
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × A,B,C,D
   34 × 5,1,0,0
   33 × 1,5,1,0
   33 × 1,1,5,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 236 -- First place
   B             -- 232 -- Second place
   C             -- 198
   D             --   0
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 34 -- First place
   B             -- 33
   Equal Support -- 33
 A wins.
   Runoff math:
     100  ballots cast
   −  33  Equal Support (no preference between the two finalists)
     ───
      67  voters with a preference  (majority = 34)
           A 34 (51%)  ·  B 33 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |       * A       |      * B       |        C       |        D       |
------------------------------------------------------------------------------------------
              * A > |       ---       | 34 -  33 -  33 | 34 -  33 -  33 |100 -   0 -   0 |
              * B > |  33 -  33 -  34 |      ---       | 67 -   0 -  33 |100 -   0 -   0 |
                C > |  33 -  33 -  34 | 33 -   0 -  67 |      ---       | 66 -  34 -   0 |
                D > |   0 -   0 - 100 |  0 -   0 - 100 |  0 -  34 -  66 |      ---       |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A           34    0    0    0   66    0  |   236   2.4
B           33    0    0    0   67    0  |   232   2.3
C           33    0    0    0   33   34  |   198   2.0
D            0    0    0    0    0  100  |     0   0.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/dark_horse_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/dark_horse_borda/cases/dark_horse_star.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
