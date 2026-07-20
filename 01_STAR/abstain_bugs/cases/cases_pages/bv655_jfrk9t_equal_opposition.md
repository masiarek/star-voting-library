# BV655 — 'equal opposition' (all-0) mislabeled as Abstained

*Generated from [`bv655_jfrk9t_equal_opposition.yaml`](../bv655_jfrk9t_equal_opposition.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Option 1

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/jfrk9t) · **[results ↗](https://bettervoting.com/jfrk9t/results)** (election `jfrk9t`).

## Scenario

This is Race 1 of BetterVoting election jfrk9t (the election has two races — see
the .md page for the Race 2 contrast). Two voters, two options:

- Ballot 1 scores **both options 0** — an explicit "equal opposition" (the voter
  actively rejects everyone), NOT a non-vote.
- Ballot 2 scores Option 1 a 5 and leaves Option 2 unscored (`&` = the BetterVoting
  `null`).

Option 1 wins (score 5 vs 0, and the runoff 1-0). The teaching point is what
happens to Ballot 1: because its marks are all-equal, the current STAR policy
(bettervoting#884) counts it as an **abstention** (BetterVoting reports
nAbstentions = 1), and the UI/CSV label it "Abstained — No preference was
expressed." But an all-0 ballot is an explicit rejection, not the same as leaving
the ballot blank.

**LH diverges here:** the LH engine counts an explicit all-0 ballot as a real tally
vote (it registers as "Equal Support" in the runoff, not an abstention — LH reports
nAbstentions = 0). Only a truly blank ballot abstains in LH. Both engines still
elect Option 1, but they disagree on the count — and LH's treatment matches the view
that an explicit 0 is a cast vote, not a non-vote (the heart of the bettervoting#884
dispute; the UI/export mislabel is bettervoting#1090).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Option 1,Option 2
0,0
5,&
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Option 1,Option 2
       0,       0
       5,       &

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Option 1      -- 5 -- First place
   Option 2      -- 0 -- Second place
 Option 1 and Option 2 advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Option 1      -- 1 -- First place
   Option 2      -- 0
   Equal Support -- 1
 Option 1 wins.
   Runoff math:
     2  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Option 1 1 (100%)  ·  Option 2 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Option 1
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |  * Option 1  | * Option 2  |
-----------------------------------------------
    * Option 1 > |     ---      | 1 - 1 - 0   |
    * Option 2 > |  0 - 1 - 1   |    ---      |

[Condorcet Winner]
  Condorcet Winner: Option 1 — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total   Avg
Option 1   1  0  0  0  0  1    0  |     5   2.5
Option 2   0  0  0  0  0  1    1  |     0   0.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv655_jfrk9t_equal_opposition_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/abstain_bugs/cases/bv655_jfrk9t_equal_opposition.yaml
```

## See also

- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../00_start_here/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv11_6xhfp8_full_equal_support](bv11_6xhfp8_full_equal_support.md) · [bv1570_6hv7jf_undecided_plurality](bv1570_6hv7jf_undecided_plurality.md)
