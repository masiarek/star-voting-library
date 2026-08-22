---
search:
  exclude: true
---

# Rung 4 — the same nine voters, ranked: RCV-IRV also elects Gala

*Generated from [`07f_apples_full_menu_irv.yaml`](../07f_apples_full_menu_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** Gala

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vq78wk) · **[results ↗](https://bettervoting.com/vq78wk/results)** (election `vq78wk` · test `BV2293`).

## Scenario

The same nine voters and the same eight-candidate menu, ranked rather than
scored. Stated plainly because this page is not a sales pitch: RCV-IRV FIXES
this spoiler. A ranked ballot lets an apple person say "any apple before the
banana", eliminations transfer those votes instead of stranding them, and the
apple side consolidates on Gala.

Ending the classic spoiler is the thing instant-runoff was designed to do and
it does it. IRV's own well-known failure is a different one — center squeeze,
where a broadly-liked compromise is eliminated early for holding too few FIRST
choices — and this election is not an example of it.

One honest caveat about this particular file: seven candidates start tied on a
single first choice each, so the early elimination ORDER is settled by
tie-breaking rather than by the voters. The eventual winner is robust to that
(every apple's ballots flow to other apples), but do not quote the round-by-
round sequence as if the voters chose it.
Live results: https://bettervoting.com/vq78wk/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
1:Granny Smith>Gala>Fuji>McIntosh>Honeycrisp>Pink Lady>Red Delicious>Banana
1:Gala>Granny Smith>Fuji>Honeycrisp>Pink Lady>McIntosh>Red Delicious>Banana
1:Fuji>Gala>Granny Smith>Honeycrisp>Pink Lady>McIntosh>Red Delicious>Banana
1:Honeycrisp>Gala>Granny Smith>McIntosh>Fuji>Pink Lady>Red Delicious>Banana
1:Pink Lady>Gala>Granny Smith>Fuji>Honeycrisp>Red Delicious>McIntosh>Banana
1:Red Delicious>Gala>Granny Smith>Fuji>Banana>Honeycrisp>Pink Lady>McIntosh
1:McIntosh>Gala>Granny Smith>Honeycrisp>Fuji>Pink Lady>Red Delicious>Banana
1:Banana>Granny Smith>Red Delicious>Gala>Fuji>Honeycrisp>Pink Lady>McIntosh
1:Banana>Granny Smith>Gala>Fuji>Honeycrisp>Pink Lady>Red Delicious>McIntosh
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Rung 4 — the same nine voters, ranked: RCV-IRV also elects Gala
 Tabulating 9 ballots (ranked ballots).

ROUND 1
Candidate        Votes  Status
-------------  -------  --------
Banana               2  Hopeful
Gala                 1  Hopeful
Granny Smith         1  Hopeful
Fuji                 1  Hopeful
Red Delicious        1  Hopeful
Honeycrisp           1  Hopeful
McIntosh             1  Hopeful
Pink Lady            1  Rejected

ROUND 2
Candidate        Votes  Status
-------------  -------  --------
Gala                 2  Hopeful
Banana               2  Hopeful
Granny Smith         1  Hopeful
Fuji                 1  Hopeful
Red Delicious        1  Hopeful
Honeycrisp           1  Hopeful
McIntosh             1  Rejected
Pink Lady            0  Rejected

ROUND 3
Candidate        Votes  Status
-------------  -------  --------
Gala                 3  Hopeful
Banana               2  Hopeful
Granny Smith         1  Hopeful
Fuji                 1  Hopeful
Honeycrisp           1  Hopeful
Red Delicious        1  Rejected
McIntosh             0  Rejected
Pink Lady            0  Rejected

ROUND 4
Candidate        Votes  Status
-------------  -------  --------
Gala                 4  Hopeful
Banana               2  Hopeful
Granny Smith         1  Hopeful
Fuji                 1  Hopeful
Honeycrisp           1  Rejected
Red Delicious        0  Rejected
McIntosh             0  Rejected
Pink Lady            0  Rejected

FINAL RESULT
Candidate        Votes  Status
-------------  -------  --------
Gala                 5  Elected
Banana               2  Rejected
Granny Smith         1  Rejected
Fuji                 1  Rejected
Honeycrisp           0  Rejected
Red Delicious        0  Rejected
McIntosh             0  Rejected
Pink Lady            0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Gala

--- Transfers and inactive ballots (what the round tables leave out) ---
The tables above give each candidate's round total but not where a
transferred vote came FROM, nor how many ballots stopped counting.
Both are recomputed from the ballots, using the eliminations the
count above actually made.

ROUND 1 — 9 of 9 ballots still active; majority = 5
   Pink Lady eliminated with 1:
      → Gala                      1

ROUND 2 — 9 of 9 ballots still active; majority = 5
   McIntosh eliminated with 1:
      → Gala                      1

ROUND 3 — 9 of 9 ballots still active; majority = 5
   Red Delicious eliminated with 1:
      → Gala                      1

ROUND 4 — 9 of 9 ballots still active; majority = 5
   Honeycrisp eliminated with 1:
      → Gala                      1

FINAL ROUND — 9 of 9 ballots still active; majority = 5
   Gala                      5  (55.6% of the still-active)  ← elected
   Banana                    2  (22.2% of the still-active)
   Granny Smith              1  (11.1% of the still-active)
   Fuji                      1  (11.1% of the still-active)
   Never exhausted, never transferred:
      2 ballots held by Banana carried a lower ranking that was never read
      1 ballot held by Granny Smith carried a lower ranking that was never read
      1 ballot held by Fuji carried a lower ranking that was never read
      (the count stopped here, so those preferences did nothing).

Inactive ballots at the final round: 0 of 9 (0.0%).
   Gala's 5 is a majority of the 9 still active AND of all 9 cast (55.6%).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 8): Gala
   Outside (7):        Granny Smith, Fuji, McIntosh, Honeycrisp, Pink Lady, Red Delicious, Banana
   One member ⇒ Gala is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Gala is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/07f_apples_full_menu_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/07f_apples_full_menu_irv.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../07_Concepts/topics/center_squeeze/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
