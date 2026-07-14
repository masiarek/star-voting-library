# The Post-it election, seven ways — Approval: Pink, if approving means any support

*Generated from [`bv2177_v8r66y_approval.yaml`](../bv2177_v8r66y_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Pink

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/v8r66y) · **[results ↗](https://bettervoting.com/v8r66y/results)** (election `v8r66y`).

## Scenario

One of seven races in the Post-it seven-ways election (BV2177, bvid v8r66y;
BV-confirmed) — the BV2176 electorate from Equal Vote's video "Updated: How
does RCV work? — With Post-its!" (https://youtu.be/Vte4nly_Neg), run through
every method BetterVoting supports. This race converts the video's 0-5
scores to Approval ballots with the most natural rule: approve = any
support (score above 0). Because the video's scores use only 0/3/4/5, any
threshold from 1 to 3 casts these exact same approvals. Result: Pink 12,
Purple 10, Blue 10, Green 8 — PINK wins, carried by the six Green fans who
scored their LAST choice a 3. The conversion is the election: had voters
approved only 4s and 5s, Blue would win (10/9/8/5); only 5s, Purple
(7/6/4/3). Three thresholds, three winners — a lesson in why "just make it
Approval" is never neutral. See the fairness lesson page:
postit_video_fair_and_balanced.md.

Live results: https://bettervoting.com/v8r66y/results
Companion races: BV2176's bv2176_p8dp28_star.yaml / _irv.yaml /
_ranked_robin.yaml (identical ballots to the BV2177 STAR/IRV/RR/STV races)
and bv2177_v8r66y_plurality.yaml.
Overview page: bv2177_v8r66y_seven_methods.md

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Purple,Green,Blue,Pink
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
0,1,1,1
0,1,1,1
0,1,1,1
0,1,1,1
0,1,1,1
0,1,1,1
0,0,1,1
0,0,1,1
0,1,1,1
1,0,1,0
1,1,0,1
1,0,0,1
0,0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../postit_rcv_example_tabulated/bv2177_v8r66y_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 20 ballots (any non-zero score = approval).

Ballots:
   columns = Purple, Green, Blue, Pink      (1 = approve; 0 / blank / marker = not approved)
     7 × 1,0,0,0
     7 × 0,1,1,1
     2 × 0,0,1,1
     1 × 1,0,1,0
     1 × 1,1,0,1
     1 × 1,0,0,1
     1 × 0,0,0,1

   Pink   -- 12 (60%) -- Elected
   Purple -- 10 (50%)
   Blue   -- 10 (50%)
   Green  -- 8 (40%)

[Approval Distribution] (how many candidates each ballot approved)
   40 approvals across 20 ballots — average 2.0 of 4 (range 1–3).
     approved 1: 8 ballots
     approved 2: 4 ballots
     approved 3: 8 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
           |  Pink  | Purple |  Blue  | Green  |
   ---------------------------------------------
   Pink    |   --   |  17%   |  75%   |  67%   |
   Purple  |  20%   |   --   |  10%   |  10%   |
   Blue    |  90%   |  10%   |   --   |  70%   |
   Green   |  100%  |  12%   |  88%   |   --   |

Winner — Approval Voting (single winner)
  Pink
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/postit_rcv_example/bv2177_v8r66y_approval.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2176_p8dp28_irv](bv2176_p8dp28_irv.md) · [bv2176_p8dp28_ranked_robin](bv2176_p8dp28_ranked_robin.md) · [bv2176_p8dp28_star](bv2176_p8dp28_star.md) · [bv2177_v8r66y_plurality](bv2177_v8r66y_plurality.md) · [bv2178_8kg698_irv](bv2178_8kg698_irv.md) · [bv2178_8kg698_ranked_robin](bv2178_8kg698_ranked_robin.md) · [bv2178_8kg698_star](bv2178_8kg698_star.md)
