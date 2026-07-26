# The Black Curtain

*Generated from [`Black_Curtain_01b_c3_b5_dichotomous.yaml`](../Black_Curtain_01b_c3_b5_dichotomous.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bob

## Scenario

The SAME five voters as Black_Curtain_01_c3_b5_hidden-consensus.yaml and
Black_Curtain_01a_c3_b5_approval.yaml — but here their APPROVAL marks are read
as a score ballot (approved = 5, not approved = 0), so the engine will print
the pairwise matrix and name the Condorcet winner OF THE COMPRESSED BALLOTS.
The magnitude is irrelevant: every head-to-head count below depends only on
the two-class ORDER (approved above not-approved), so 5/0 and 1/0 give an
identical matrix. 5/0 is used because the engine's built-in Approval
cross-check reads "a score of 3+ is an approval" and so misreads a 1/0 ballot
— see the note at the end of ../condorcet_compression.md.

On the original 0-5 scores, Cal is the Condorcet winner (beats Bob 3-2 and
Ann 3-2) and STAR elects Cal. Compress those same opinions to approve /
don't-approve at "a 3 or better is an approval" and the Condorcet winner
becomes BOB — legitimately: on these ballots Bob beats Cal 2-0, because the
three voters who approved BOTH now express no preference between them. The
Equal Support column in the matrix is exactly where the deciding information
went.

This is the runnable limit of the theory result that approval voting coincides
with Borda and with every Condorcet method on DICHOTOMOUS preferences (weak
rankings with two indifference classes). The equivalence is true of that
domain; it does not transfer to an election where voters do the compressing
themselves. Note too that Bob wins here under STAR as well as Approval — the
outcome is not a quirk of one method, it is the ballot having lost the
Cal-over-Bob preference.

Teaching page: ../condorcet_compression.md
Original video source: https://www.youtube.com/watch?v=5_ZMruwOZgw
See README.md in this folder.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Bob,Cal
0,5,5   # voter 1 — approved Bob and Cal; no preference between them
0,5,5   # voter 2 — approved Bob and Cal; no preference between them
0,5,5   # voter 3 — approved Bob and Cal; no preference between them
5,5,0   # voter 4 — approved Ann and Bob; no preference between them
5,5,0   # voter 5 — approved Ann and Bob; no preference between them
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Ann,Bob,Cal
    3 ×   0,  5,  5
    2 ×   5,  5,  0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bob           -- 25 -- First place
   Cal           -- 15 -- Second place
   Ann           -- 10
 Bob and Cal advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bob           -- 2 -- First place
   Cal           -- 0
   Equal Support -- 3
 Bob wins.
   Runoff math:
     5  ballots cast
   − 3  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Bob 2 (100%)  ·  Cal 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bob
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ann    |  * Bob    |  * Cal    |
-----------------------------------------------------
         Ann > |    ---     |0 - 2 - 3  |2 - 0 - 3  |
       * Bob > | 3 - 2 - 0  |   ---     |2 - 3 - 0  |
       * Cal > | 3 - 0 - 2  |0 - 3 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bob — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ann — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ann        2  0  0  0  0  3  |    10   2.0
Bob        5  0  0  0  0  0  |    25   5.0
Cal        3  0  0  0  0  2  |    15   3.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/Black_Curtain_01b_c3_b5_dichotomous_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/black_curtain/cases/Black_Curtain_01b_c3_b5_dichotomous.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [The Black Curtain (worked set)](../../README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [Black_Curtain_01_c3_b5_hidden-consensus](Black_Curtain_01_c3_b5_hidden-consensus.md) · [Black_Curtain_01a_c3_b5_approval](Black_Curtain_01a_c3_b5_approval.md) · [Black_Curtain_02_c3_b5_near-clones](Black_Curtain_02_c3_b5_near-clones.md) · [Black_Curtain_03_c3_b5_polarized-on-cal](Black_Curtain_03_c3_b5_polarized-on-cal.md) · [Black_Curtain_04_c4_b5_four-candidates](Black_Curtain_04_c4_b5_four-candidates.md)
