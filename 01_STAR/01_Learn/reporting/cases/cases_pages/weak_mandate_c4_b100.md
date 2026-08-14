---
search:
  exclude: true
---

# The seat nobody wanted — a field with no enthusiasm

*Generated from [`weak_mandate_c4_b100.yaml`](../weak_mandate_c4_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../README.md) · **1 seat** · **Expected winner:** Beth

## Scenario

A 100-ballot water-district board election in which nobody is popular. Two
candidates are widely known and widely disliked, one is barely known at all,
and one is a protest option. 82% of every score cast is a 1 or a 0; a
scattering of die-hards give a 4 or a 5. Somebody still has to win.

The point is not who won — it is what the report says about HOW they won.
Beth wins with 88 stars out of a possible 500: an average of 0.9 out of 5.
A Choose-One count would report "Beth, elected" and stop. STAR's scoring
round publishes the number that tells the winner to tread carefully, and
tells the next cycle's candidates that the seat is there for the taking.

Watch Colin's two averages. He is not disliked — he is unknown: 78 voters
left him blank, and the 22 who did rate him averaged 2.3, the highest real
support in the election. "Nobody has heard of him" and "everybody dislikes
him" produce nearly the same total, and only the Abs column tells them apart.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Arlo,Beth,Colin,Dara
   0,   0,   5,   0
   1,   0,   -,   1
   0,   1,   2,   0
   1,   1,   -,   1
   1,   0,   -,   2
   2,   0,   -,   0
   2,   0,   -,   1
   0,   0,   4,   0
   2,   0,   -,   0
   1,   2,   -,   0
   1,   1,   -,   1
   0,   1,   0,   0
   0,   2,   -,   0
   0,   1,   0,   0
   0,   1,   -,   0
   1,   0,   -,   0
   1,   5,   -,   0
   1,   0,   -,   2
   1,   2,   -,   0
   0,   0,   -,   0
   0,   1,   -,   0
   1,   1,   -,   0
   0,   1,   2,   0
   1,   1,   4,   0
   0,   2,   -,   0
   1,   0,   -,   0
   0,   1,   -,   0
   0,   0,   -,   0
   2,   0,   -,   0
   2,   0,   -,   1
   0,   0,   -,   0
   2,   0,   -,   1
   0,   0,   -,   0
   1,   0,   2,   0
   0,   0,   0,   0
   0,   1,   2,   0
   0,   1,   5,   0
   0,   2,   -,   0
   1,   0,   -,   1
   5,   0,   -,   0
   0,   1,   -,   0
   0,   0,   -,   2
   1,   4,   -,   0
   1,   2,   -,   0
   0,   1,   2,   0
   1,   5,   -,   0
   0,   1,   -,   0
   2,   1,   -,   0
   0,   1,   -,   2
   2,   0,   -,   0
   1,   1,   -,   0
   1,   1,   -,   0
   1,   1,   -,   1
   0,   1,   -,   0
   0,   1,   -,   0
   0,   0,   4,   0
   2,   0,   -,   0
   1,   0,   -,   1
   0,   1,   2,   0
   0,   0,   -,   2
   1,   0,   -,   0
   2,   0,   -,   0
   0,   2,   -,   0
   0,   1,   -,   0
   1,   5,   -,   0
   2,   0,   -,   0
   0,   0,   -,   2
   0,   0,   -,   5
   1,   2,   -,   0
   1,   1,   -,   0
   0,   1,   -,   1
   2,   1,   -,   1
   1,   1,   2,   0
   0,   1,   5,   0
   1,   0,   2,   0
   0,   1,   -,   0
   0,   1,   -,   0
   0,   1,   -,   0
   0,   1,   -,   0
   1,   1,   -,   0
   1,   4,   -,   0
   0,   1,   -,   0
   0,   0,   -,   2
   0,   2,   -,   0
   0,   2,   -,   0
   0,   0,   0,   0
   1,   1,   2,   0
   1,   1,   -,   0
   0,   1,   -,   0
   2,   1,   -,   0
   0,   0,   0,   0
   0,   0,   -,   5
   1,   0,   -,   4
   2,   1,   -,   0
   0,   1,   4,   0
   0,   0,   2,   0
   0,   1,   -,   0
   1,   2,   -,   0
   2,   0,   -,   0
   0,   0,   -,   0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Beth
  Approval = Colin   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Arlo,Beth,Colin,Dara
   15 ×    0,   1,    -,   0
    8 ×    2,   0,    -,   0
    6 ×    0,   2,    -,   0
    6 ×    1,   1,    -,   0
    5 ×    0,   1,    2,   0
    5 ×    1,   2,    -,   0
    5 ×    0,   0,    -,   0
    4 ×    0,   0,    -,   2
    3 ×    1,   0,    -,   1
    3 ×    1,   1,    -,   1
    3 ×    2,   0,    -,   1
    3 ×    1,   0,    -,   0
    3 ×    1,   5,    -,   0
    3 ×    0,   0,    0,   0
    3 ×    2,   1,    -,   0
    2 ×    1,   0,    -,   2
    2 ×    0,   0,    4,   0
    2 ×    0,   1,    0,   0
    2 ×    1,   0,    2,   0
    2 ×    0,   1,    5,   0
    2 ×    1,   4,    -,   0
    2 ×    0,   0,    -,   5
    2 ×    1,   1,    2,   0
    1 ×    0,   0,    5,   0
    1 ×    1,   1,    4,   0
    1 ×    5,   0,    -,   0
    1 ×    0,   1,    -,   2
    1 ×    0,   1,    -,   1
    1 ×    2,   1,    -,   1
    1 ×    1,   0,    -,   4
    1 ×    0,   1,    4,   0
    1 ×    0,   0,    2,   0
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Beth          -- 88 -- First place
   Arlo          -- 68 -- Second place
   Colin         -- 51
   Dara          -- 39
 Beth and Arlo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Beth          -- 43 -- First place
   Arlo          -- 27
   Equal Support -- 30
 Beth wins.
   Runoff math:
     100  ballots cast
   −  30  Equal Support (no preference between the two finalists)
     ───
      70  voters with a preference  (majority = 36)
           Beth 43 (61%)  ·  Arlo 27 (39%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Beth
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Arlo    |   * Beth    |    Colin    |     Dara    |
---------------------------------------------------------------------------
        * Arlo > |     ---      |27 - 30 - 43 |44 - 39 - 17 |40 - 49 - 11 |
        * Beth > | 43 - 30 - 27 |    ---      |48 - 35 - 17 |53 - 31 - 16 |
         Colin > | 17 - 39 - 44 |17 - 35 - 48 |    ---      |17 - 62 - 21 |
          Dara > | 11 - 49 - 40 |16 - 31 - 53 |21 - 62 - 17 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Beth — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Colin — loses every head-to-head matchup — elected by Approval!

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  Abs  | Total  Avg all  Avg rated
Arlo        1   0   0  15  33  51    0  |    68      0.7        0.7
Beth        3   2   0  11  43  41    0  |    88      0.9        0.9
Colin       3   4   0  10   0   5   78  |    51      0.5        2.3
Dara        2   1   0   7  11  79    0  |    39      0.4        0.4
  Avg all   = Total / all ballots — a blank counts as 0, so this is the Total the Scoring Round ranks on, per ballot.
  Avg rated = Total / the ballots that scored this candidate (Abs excluded) — support among voters who had an opinion.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/weak_mandate_c4_b100_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/01_Learn/reporting/cases/weak_mandate_c4_b100.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ballot & terminology basics](../../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [same_total_different_shape_c3_b7](same_total_different_shape_c3_b7.md)
