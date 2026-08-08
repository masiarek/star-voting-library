---
search:
  exclude: true
---

# Ossipoff's 303 — the first-round LEADER is eliminated

*Generated from [`bv2281_qycpbx_ossipoff_irv.yaml`](../bv2281_qycpbx_ossipoff_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** D

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/qycpbx) · **[results ↗](https://bettervoting.com/qycpbx/results)** (election `qycpbx` · test `BV2281`).

## Scenario

A constructed 5-candidate, 303-voter profile published on rangevoting.org
(Warren D. Smith's site, section 12, credited to Mike Ossipoff). Reproduced
here exactly as given, because it is a sharper example than the one it is
usually filed under.

The textbook center squeeze eliminates a Condorcet winner who holds FEW first
choices — that is the whole mechanism, and it lets a defender answer "well,
nobody actually wanted them first." This profile removes that answer.

C holds 100 of 303 first choices — the LARGEST first-choice bloc in the
field, ahead of D (53), B (51), A (50) and E (49). C is also the Condorcet
winner, and not narrowly: C beats A 202-101, B 202-101, D 201-102 and
E 201-102 — roughly two to one against every rival. RCV-IRV eliminates C in
round 3 and elects D.

The elimination order is what does it. E goes first (49), and every one of
those ballots reads E>D, so D climbs to 102. A goes next (50), and those
ballots read A>B, so B climbs to 101. C, who led the entire count on 100, is
now the lowest of the three left and is cut — at which point C's 100 ballots
read C>D and hand D the election 202-101.

Read this fairly. It is CONSTRUCTED, not a real election, so it proves that
RCV-IRV CAN do this, not that it usually does — Condorcet failures showed up
in 2 of 182 US RCV elections studied. Its one-dimensional layout (A-B-C-D-E
left to right, C in the middle) is the standard spatial model rather than a
transcript of any electorate. And the source page is score-voting advocacy
with a polemical tone; the PROFILE is arithmetic and reproduces exactly, which
is why it is here and the rhetoric is not.

Bare letters are deliberate: this is an abstract published illustration, and
A-E are the source's own labels.

BV-CONFIRMED. Race 1 of live election qycpbx (Test ID BV2281) is these 303
ballots counted by BetterVoting's own IRV tabulator, and it elects D, matching
this file exactly; race 2 is the same ballots under Ranked Robin and elects C.
tieBreakType 'none' in both. Frozen export: bv2281_qycpbx_bv_export.json.

Live on BetterVoting: https://bettervoting.com/qycpbx
Live results: https://bettervoting.com/qycpbx/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
50:A>B>C>D>E
51:B>A>C>D>E
100:C>D>B>E>A
53:D>E>C>B>A
49:E>D>C>B>A
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Ossipoff's 303 — the first-round LEADER is eliminated
 Tabulating 303 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
C                100  Hopeful
D                 53  Hopeful
B                 51  Hopeful
A                 50  Hopeful
E                 49  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
D                102  Hopeful
C                100  Hopeful
B                 51  Hopeful
A                 50  Rejected
E                  0  Rejected

ROUND 3
Candidate      Votes  Status
-----------  -------  --------
D                102  Hopeful
B                101  Hopeful
C                100  Rejected
A                  0  Rejected
E                  0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
D                202  Elected
B                101  Rejected
C                  0  Rejected
A                  0  Rejected
E                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  D
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 5): C
   Outside (4):        A, B, D, E
   One member ⇒ C is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner D is OUTSIDE the Smith set. ✗
      Every member of the set (C) beats D head-to-head, yet
      RCV-IRV elected D anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2281_qycpbx_ossipoff_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/rangevoting_irv_examples/cases/bv2281_qycpbx_ossipoff_irv.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../07_Concepts/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2281_qycpbx_ossipoff_ranked_robin](bv2281_qycpbx_ossipoff_ranked_robin.md) · [bv2282_hf3ckp_brams_irv](bv2282_hf3ckp_brams_irv.md) · [bv2282_hf3ckp_brams_ranked_robin](bv2282_hf3ckp_brams_ranked_robin.md)
