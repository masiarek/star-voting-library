---
search:
  exclude: true
---

# Weak Condorcet loser — STAR elects a candidate who beats nobody

*Generated from [`wcl_c3_b5_star.yaml`](../wcl_c3_b5_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/concepts) · **1 seat** · **Expected winner:** Ben

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/c73pfw) · **[results ↗](https://bettervoting.com/c73pfw/results)** (election `c73pfw`).

## Scenario

Five voters, three candidates: Ada, Ben, Cora.

A CONDORCET LOSER loses every head-to-head. A WEAK Condorcet loser is the
ties-allowed version: they lose OR TIE every head-to-head — that is, they
BEAT NOBODY. Every strict Condorcet loser is a weak one; the converse fails,
and the gap between the two is exactly one pairwise tie.

Here the pairwise results are:
  Ada beats Ben  3-2      Ada beats Cora 3-2      Ben ties Cora 2-2
So Ada is the (strict) Condorcet winner, and BOTH Ben and Cora beat nobody —
they are jointly weak Condorcet losers. Note the non-uniqueness: unlike a
strict Condorcet loser, a weak one need not be alone.

Scoring Round: Ben 18, Cora 16, Ada 15. Ada is polarizing — three voters give
her a 5 and two give her a 0 — so the broadly-acceptable pair advances and the
Condorcet winner is eliminated before the runoff.

Automatic Runoff: Ben vs Cora is the 2-2 pairwise TIE (one voter scored both
4, so they are Equal Support). STAR's first tiebreaker is the higher score,
and Ben wins it.

The result: STAR elects Ben, a weak Condorcet loser. And it had no choice —
BOTH finalists beat nobody, so whichever won the tiebreak was going to be one.

Why this cannot happen with a STRICT Condorcet loser: a strict loser loses the
runoff to the other finalist by definition, so STAR can never elect one. The
weak version slips through precisely because a TIE is not a loss, and a tie
hands the decision to the tiebreaker instead. That single word — "or ties" —
is the whole difference between a criterion STAR passes and one it fails.

Honest framing: this is a knife-edge construction. It needs an exact pairwise
tie between the two finalists, which is vanishingly rare in any electorate
large enough to matter. Read it as "the criterion is failed" (a possibility
result), not as "this happens in practice."

## Parameters (from the YAML)

```yaml
voting_method: STAR
num_winners: 1
expected_winners: [Ben]
bv_election_id: c73pfw
bv_test_id: BV2249
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cora
5,4,4   # loves Ada; Ben and Cora equally acceptable -> Equal Support in the runoff
5,4,1   # loves Ada, tolerates Ben, dislikes Cora
5,4,3   # loves Ada, tolerates Ben and Cora
0,3,4   # rejects Ada, prefers Cora over Ben
0,3,4   # rejects Ada, prefers Cora over Ben
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Ben
  Choose-One (Plurality) = Ada   (differs from STAR)
  RCV-IRV                = Ada   (differs from STAR)
  RCV-RR (Condorcet)     = Ada   (differs from STAR)
  Note: 1 of 5 ballots (20%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/wcl_c3_b5_star_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/wcl_c3_b5_star_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Ada,Ben,Cora
    2 ×   0,  3,   4
    1 ×   5,  4,   4
    1 ×   5,  4,   1
    1 ×   5,  4,   3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ben           -- 18 -- First place
   Cora          -- 16 -- Second place
   Ada           -- 15
 Ben and Cora advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ben           -- 2 -- Tied for first place
   Cora          -- 2 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Ben           -- 18 -- First place
   Cora          -- 16
 Ben wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ben
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ada    |  * Ben    |  * Cora   |
-----------------------------------------------------
         Ada > |    ---     |3 - 0 - 2  |3 - 0 - 2  |
       * Ben > | 2 - 0 - 3  |   ---     |2 - 1 - 2  |
      * Cora > | 2 - 0 - 3  |2 - 1 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ada — STAR elected Ben instead (Ada was eliminated in the scoring round)

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: Ben, Cora (winless — pairwise ties) — Ben elected by STAR, Approval!

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        3  0  0  0  0  2  |    15   3.0
Ben        0  3  2  0  0  0  |    18   3.6
Cora       0  3  1  0  1  0  |    16   3.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/wcl_c3_b5_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/weak_condorcet_loser/cases/wcl_c3_b5_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/STAR_OUTLIER_RR_WITH_IRV/wcl_c3_b5_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [wcl_c3_b5_approval](wcl_c3_b5_approval.md)
