---
search:
  exclude: true
---

# Brams 1982 — twenty-one voters, and the Condorcet winner goes out second

*Generated from [`bv2282_hf3ckp_brams_irv.yaml`](../bv2282_hf3ckp_brams_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** B

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/hf3ckp) · **[results ↗](https://bettervoting.com/hf3ckp/results)** (election `hf3ckp` · test `BV2282`).

## Scenario

A 21-voter, 4-candidate profile from Stephen J. Brams, "The AMS Nomination
Procedure Is Vulnerable to 'Truncation of Preferences'," Notices of the
American Mathematical Society 29:2 (February 1982), 136-138 — reproduced via
rangevoting.org, which cites it as an RCV-IRV example.

Counted by Hare: B leads on 7 first choices, F (3) is eliminated and sends 3
to N, then G is eliminated on 6 and sends all 6 to B, who wins 13 of 21. But
G beats B head-to-head 14-7, and beats N 13-8 and F 18-3 — G is the Condorcet
winner, and is eliminated one round before the finish.

It is the smallest example in this folder: 21 ballots, checkable on paper in
about a minute, which is what makes it the one to hand someone who does not
want to take a 303-voter profile on trust.

PROVENANCE, STATED CAREFULLY. The profile is Brams's; the RCV-IRV reading is
rangevoting.org's. Brams's paper is about vulnerability to PREFERENCE
TRUNCATION — voters ranking only some candidates — which is a different
argument from the Condorcet failure shown here, and we could not confirm from
the abstract whether the AMS procedure of the day was Hare specifically. So:
cite Brams for the ballots, and cite this file for what Hare does with them.
Do not write "Brams showed that IRV..." — he did not, in this paper.

Candidate labels B, G, N, F are Brams's own and are kept for traceability to
the source, which is why they are neither alphabetical nor in reading order.

BV-CONFIRMED. Race 1 of live election hf3ckp (Test ID BV2282) is these 21
ballots counted by BetterVoting's own IRV tabulator, and it elects B, matching
this file exactly; race 2 is the same ballots under Ranked Robin and elects G.
tieBreakType 'none' in both. Frozen export: bv2282_hf3ckp_bv_export.json.

Live on BetterVoting: https://bettervoting.com/hf3ckp
Live results: https://bettervoting.com/hf3ckp/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
7:B>G>N>F
6:G>B>N>F
5:N>G>B>F
3:F>N>G>B
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Brams 1982 — twenty-one voters, and the Condorcet winner goes out second
 Tabulating 21 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
B                  7  Hopeful
G                  6  Hopeful
N                  5  Hopeful
F                  3  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
N                  8  Hopeful
B                  7  Hopeful
G                  6  Rejected
F                  0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
B                 13  Elected
N                  8  Rejected
G                  0  Rejected
F                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  B
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): G
   Outside (3):        B, N, F
   One member ⇒ G is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner B is OUTSIDE the Smith set. ✗
      Every member of the set (G) beats B head-to-head, yet
      RCV-IRV elected B anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2282_hf3ckp_brams_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/rangevoting_irv_examples/cases/bv2282_hf3ckp_brams_irv.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2281_qycpbx_ossipoff_irv](bv2281_qycpbx_ossipoff_irv.md) · [bv2281_qycpbx_ossipoff_ranked_robin](bv2281_qycpbx_ossipoff_ranked_robin.md) · [bv2282_hf3ckp_brams_ranked_robin](bv2282_hf3ckp_brams_ranked_robin.md)
