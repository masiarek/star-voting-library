# A crowded race — Plurality's minority winner vs STAR's consensus

*Generated from [`minority_winner_c5_b20.yaml`](../minority_winner_c5_b20.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cole

## Scenario

Five candidates, twenty voters — the case for reading the whole ballot, shown
simply. Erik has a passionate base: 6 of 20 rank him first. The other 14 split
their first choices among Amy (5), Ben (4), Dana (3), and Cole (2) — and nearly
all of them score Erik a flat 0. Under Choose-One, Erik wins on **30%** while
**70% of voters actively opposed him** — the textbook minority/plurality winner.
Cole tells the opposite story: few first choices (only 2), but broad, warm
support across the room (most voters rate him 4). Reading the whole ballot finds
him: he leads STAR's scoring round (70) and wins the automatic runoff, and he
beats every rival head-to-head — the Condorcet winner. STAR and Ranked Robin both
elect Cole, the candidate a majority is genuinely glad about; only the
first-choice-only count crowns Erik. Same opinions, no strategy — the difference
is how much of the ballot the method reads.
Lesson: 00_start_here/topics/plurality.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amy, Ben, Cole, Dana, Erik
   0,   0,    2,    0,    5
   0,   0,    2,    0,    5
   0,   0,    2,    0,    5
   0,   0,    2,    0,    5
   0,   0,    2,    0,    5
   0,   0,    2,    0,    5
   5,   1,    4,    1,    0
   5,   1,    4,    1,    0
   5,   1,    4,    1,    0
   5,   1,    4,    1,    0
   5,   1,    4,    1,    0
   1,   5,    4,    1,    0
   1,   5,    4,    1,    0
   1,   5,    4,    1,    0
   1,   5,    4,    1,    0
   1,   1,    4,    5,    0
   1,   1,    4,    5,    0
   1,   1,    4,    5,    0
   2,   2,    5,    2,    0
   2,   2,    5,    2,    0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Cole
  Choose-One (Plurality) = Erik   (differs from STAR)
  RCV-IRV                = Amy   (differs from STAR)
  Note: 14 of 20 ballots (70%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: minority_winner_tabulated/minority_winner_c5_b20_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 20 ballots.
Count × Amy,Ben,Cole,Dana,Erik
    6 ×   0,  0,   2,   0,   5
    5 ×   5,  1,   4,   1,   0
    4 ×   1,  5,   4,   1,   0
    3 ×   1,  1,   4,   5,   0
    2 ×   2,  2,   5,   2,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cole          -- 70 -- First place
   Amy           -- 36 -- Second place
   Ben           -- 32
   Erik          -- 30
   Dana          -- 28
 Cole and Amy advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cole          -- 15 -- First place
   Amy           --  5
   Equal Support --  0
 Cole wins.
   Runoff math:
     20  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     20  voters with a preference  (majority = 11)
           Cole 15 (75%)  ·  Amy 5 (25%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cole
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Amy     |     Ben     |   * Cole    |     Dana    |     Erik    |
-----------------------------------------------------------------------------------------
         * Amy > |     ---      | 5 - 11 -  4 | 5 -  0 - 15 | 5 - 12 -  3 |14 -  0 -  6 |
           Ben > |  4 - 11 -  5 |    ---      | 4 -  0 - 16 | 4 - 13 -  3 |14 -  0 -  6 |
        * Cole > | 15 -  0 -  5 |16 -  0 -  4 |    ---      |17 -  0 -  3 |14 -  0 -  6 |
          Dana > |  3 - 12 -  5 | 3 - 13 -  4 | 3 -  0 - 17 |    ---      |14 -  0 -  6 |
          Erik > |  6 -  0 - 14 | 6 -  0 - 14 | 6 -  0 - 14 | 6 -  0 - 14 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Cole — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Amy         5   0   0   2   7   6  |    36   1.8
Ben         4   0   0   2   8   6  |    32   1.6
Cole        2  12   0   6   0   0  |    70   3.5
Dana        3   0   0   2   9   6  |    28   1.4
Erik        6   0   0   0   0  14  |    30   1.5
```

</details>

Everything in one file: the [`_tabulated` mirror](../minority_winner_tabulated/minority_winner_c5_b20_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minority_winner/minority_winner_c5_b20.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)
