# Chicken / Burr dilemma — Approval, honest: A and B tie 60-60 (the trap)

*Generated from [`chicken_approval.yaml`](../chicken_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** A

## Scenario

The same electorate as chicken_star, under APPROVAL voting with honest ballots: the 60
A/B voters approve both allies (utility above the midpoint), the 40 C voters approve C.
Result: A 60, B 60 — an exact tie (broken here only by candidate priority order), with
C safely defeated at 40. This is the chicken / Burr dilemma: the honest cooperative play
leaves A and B in a dead heat, so each side is tempted to bullet-vote (approve only its
favorite) to win outright — a slippery slope that, if both sides defect far enough, lets
the majority-opposed C slip through. The A/B tie is the whole point (as with Jefferson &
Burr in 1800), so this case is LH/pref_voting-verified rather than frozen from a random
BetterVoting tie-break. STAR removes the slope entirely — see chicken_star.yaml.
Concept: ../../00_start_here/topics/strategic_pathologies.md.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Count:A,B,C
35:1,1,0   # approve A and B
25:1,1,0   # approve A and B
40:0,0,1   # approve C
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/chicken_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 100 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C      (1 = approve; 0 / blank / marker = not approved)
    60 × 1,1,0
    40 × 0,0,1

   A -- 60 (60%) -- Elected
   B -- 60 (60%)
   C -- 40 (40%)
  Note: A, B each have 60 approvals and tie for the last 1 seat.
        Candidate priority order (A > B) broke the tie: A elected, B not elected.

[Approval Distribution] (how many candidates each ballot approved)
   160 approvals across 100 ballots — average 1.6 of 3 (range 1–2).
     approved 1: 40 ballots
     approved 2: 60 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   A    |   B    |   C    |
   -------------------------------
   A  |   --   |  100%  |   0%   |
   B  |  100%  |   --   |   0%   |
   C  |   0%   |   0%   |   --   |

Winner — Approval Voting (single winner)
  A
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/chicken_dilemma/cases/chicken_approval.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [chicken_star](chicken_star.md)
