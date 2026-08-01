# Symmetric centrist (47/47/3/3) — RCV-IRV: the centrist is squeezed, the poles deadlock

*Generated from [`bv2170_pp2q4q_irv.yaml`](../bv2170_pp2q4q_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** Avery

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/pp2q4q) · **[results ↗](https://bettervoting.com/pp2q4q/results)** (election `pp2q4q`).

## Scenario

One of four races in the Symmetric Centrist election (BV2170, bvid pp2q4q; BV-confirmed). 100 voters, three candidates, ONE electorate tabulated four ways. Avery is the left pole, Blake the right pole, Casey the centrist Condorcet winner (beats each pole 53–47) — but Casey holds only 6 first choices. IRV eliminates Casey FIRST (fewest first choices), and Casey's 6 ballots split 3 to Avery, 3 to Blake, leaving Avery 50 vs Blake 50 — an EXACT TIE. The center squeeze throws out the candidate a majority actually prefers, and the two poles then deadlock.

Random tiebreak — NOT freezable, and the two engines split it differently. Because the electorate is perfectly symmetric between the poles, the final round is a genuine 50–50 tie. BetterVoting breaks it at RANDOM and this run elected Blake (frozen in the export). The LH RCV-IRV engine breaks the same tie with a stable seeded draw and lands on Avery (it does NOT honor lot_numbers — a true tie stays a tie). Neither winner is a property of the ballots: the lesson is the deadlock — once the centrist a majority prefers is squeezed out, either pole takes it on a coin flip. expected_winners records LH's deterministic-by-seed result (Avery); the frozen BV export shows Blake.

Live results: https://bettervoting.com/pp2q4q/results
Companion races: bv2170_pp2q4q_star.yaml, bv2170_pp2q4q_ranked_robin.yaml, bv2170_pp2q4q_plurality.yaml.
Overview page: bv2170_pp2q4q_symmetric_centrist.md

## Parameters (from the YAML)

```yaml
voting_method: IRV
num_winners: 1
expected_winners:
- Avery
bv_election_id: pp2q4q
bv_test_id: BV2170
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
47:Avery>Casey>Blake
47:Blake>Casey>Avery
3:Casey>Avery>Blake
3:Casey>Blake>Avery
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Symmetric centrist (47/47/3/3) — RCV-IRV: the centrist is squeezed, the poles deadlock
 Tabulating 100 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Avery             47  Hopeful
Blake             47  Hopeful
Casey              6  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Avery             50  Elected
Blake             50  Rejected
Casey              0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Avery
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Casey
   Outside (2):        Avery, Blake
   One member ⇒ Casey is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Avery is OUTSIDE the Smith set. ✗
      Every member of the set (Casey) beats Avery head-to-head, yet
      RCV-IRV elected Avery anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2170_pp2q4q_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/symmetric_centrist_bv2170/cases/bv2170_pp2q4q_irv.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../07_Concepts/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2170_pp2q4q_plurality](bv2170_pp2q4q_plurality.md) · [bv2170_pp2q4q_ranked_robin](bv2170_pp2q4q_ranked_robin.md) · [bv2170_pp2q4q_star](bv2170_pp2q4q_star.md)
