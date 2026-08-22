---
search:
  exclude: true
---

# Rung 4 — the same nine voters, approving: Approval elects Gala too

*Generated from [`07e_apples_full_menu_approval.yaml`](../07e_apples_full_menu_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **1 seat** · **Expected winner:** Gala

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vq78wk) · **[results ↗](https://bettervoting.com/vq78wk/results)** (election `vq78wk` · test `BV2293`).

## Scenario

The same nine voters and the same eight-candidate menu, marking every candidate
they would be happy with rather than exactly one.

Gala 7 of 9 (78%), Granny Smith 6, Banana 2. The apple side's support adds up
instead of dividing, because a voter who likes six apples may now say so.

Approval and STAR reach the same answer here by different routes: Approval asks
who is acceptable to the most people, STAR asks that and then checks which of
the top two more voters actually prefer. On this electorate they agree, which
is the common case. The point of this rung is not which expressive method you
pick — it is that every ballot here which collects support for more than one
candidate LET the majority end the split, and on these ballots all of them did.
Not a guarantee in general: 05a is a score ballot whose faction split itself
anyway, and a Borda ballot positively rewards running clones.
Live results: https://bettervoting.com/vq78wk/results

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Granny Smith,Gala,Fuji,Honeycrisp,Pink Lady,Red Delicious,McIntosh,Banana
1,1,0,0,0,0,0,0   # Granny Smith person - Gala is fine too
1,1,0,0,0,0,0,0   # Gala person
1,1,1,0,0,0,0,0   # Fuji person
1,1,0,1,0,0,1,0   # Honeycrisp person
1,1,0,0,1,0,0,0   # Pink Lady person
0,1,0,0,0,1,0,0   # Red Delicious person
1,1,0,1,0,0,1,0   # McIntosh person
0,0,0,0,0,0,0,1   # banana person
0,0,0,0,0,0,0,1   # banana person
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/07e_apples_full_menu_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 9 ballots (any non-zero score = approval).

Ballots:
   columns = Granny Smith, Gala, Fuji, Honeycrisp, Pink Lady, Red Delicious, McIntosh, Banana      (1 = approve; 0 = not approved)
     2 × 1,1,0,0,0,0,0,0
     1 × 1,1,1,0,0,0,0,0
     2 × 1,1,0,1,0,0,1,0
     1 × 1,1,0,0,1,0,0,0
     1 × 0,1,0,0,0,1,0,0
     2 × 0,0,0,0,0,0,0,1

   Gala          -- 7 (78%) -- Elected
   Granny Smith  -- 6 (67%)
   Honeycrisp    -- 2 (22%)
   McIntosh      -- 2 (22%)
   Banana        -- 2 (22%)
   Fuji          -- 1 (11%)
   Pink Lady     -- 1 (11%)
   Red Delicious -- 1 (11%)

[Approval Distribution] (how many candidates each ballot approved)
   22 approvals across 9 ballots — average 2.4 of 8 (range 1–4).
     approved 1: 2 ballots
     approved 2: 3 ballots
     approved 3: 2 ballots
     approved 4: 2 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
                  |      Gala     |  Granny Smith |   Honeycrisp  |    McIntosh   |     Banana    |      Fuji     |   Pink Lady   | Red Delicious |
   ------------------------------------------------------------------------------------------------------------------------------------------------
   Gala           |       --      |      86%      |      29%      |      29%      |       0%      |      14%      |      14%      |      14%      |
   Granny Smith   |      100%     |       --      |      33%      |      33%      |       0%      |      17%      |      17%      |       0%      |
   Honeycrisp     |      100%     |      100%     |       --      |      100%     |       0%      |       0%      |       0%      |       0%      |
   McIntosh       |      100%     |      100%     |      100%     |       --      |       0%      |       0%      |       0%      |       0%      |
   Banana         |       0%      |       0%      |       0%      |       0%      |       --      |       0%      |       0%      |       0%      |
   Fuji           |      100%     |      100%     |       0%      |       0%      |       0%      |       --      |       0%      |       0%      |
   Pink Lady      |      100%     |      100%     |       0%      |       0%      |       0%      |       0%      |       --      |       0%      |
   Red Delicious  |      100%     |       0%      |       0%      |       0%      |       0%      |       0%      |       0%      |       --      |

Winner — Approval Voting (single winner)
  Gala
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/07e_apples_full_menu_approval.yaml
```

## See also

- [Vote splitting (worked set)](../../README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [07g_apples_full_menu_ranked_robin](07g_apples_full_menu_ranked_robin.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [08c_smallest_spoiler_ranked_robin](08c_smallest_spoiler_ranked_robin.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
