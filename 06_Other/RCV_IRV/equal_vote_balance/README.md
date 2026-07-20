# Equal-vote balance — where RCV-IRV fails and Ranked Robin doesn't

Runnable proof that **RCV-IRV fails the Equal Vote "Test of Balance"**: two exactly-opposite ballots don't reliably cancel under sequential elimination. The concept and the full write-up: [RCV-IRV Fails the Equal Vote Criterion](../../../00_start_here/RCV_IRV/RCV_IRV_equal_vote.md). The mirror image — where opposite *score* ballots **do** cancel — is [equal & opposite (STAR)](../../../01_STAR/equal_and_opposite/).

Three candidates on a line: **Ada** (left), **Bruno** (center), **Cyrus** (right).

| File | Ballots | RCV-IRV | Condorcet / Ranked Robin |
|---|--:|---|---|
| [`balance_base_irv_c3_b9.yaml`](balance_base_irv_c3_b9.yaml) | 9 | **Bruno** (6–3) | **Bruno** (beats Ada 6–3, Cyrus 7–2) |
| [`balance_plus_opposite_c3_b15.yaml`](balance_plus_opposite_c3_b15.yaml) | 15 | **Ada** (10–5) | **still Bruno** (9–6, 10–5) |

The only difference between the two files is **three exact-opposite ballot pairs** (`Ada>Bruno>Cyrus` + its reverse `Cyrus>Bruno>Ada`). Those pairs are perfectly balanced — they cancel under Condorcet/Ranked Robin/STAR, leaving Bruno the winner. But RCV-IRV counts only first-choices, so they pile onto the two extremes and none onto the center: Bruno is squeezed out and Ada wins. **Balanced ballots, flipped winner** — the Test of Balance failing, via [center squeeze](../../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md).

```
# see the same ballots stay Bruno under the pairwise count:
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/RCV_IRV/equal_vote_balance/balance_plus_opposite_c3_b15.yaml   # RCV-IRV -> Ada
# (edit voting_method to RankedRobin to see Ranked Robin -> Bruno, the Condorcet winner)
```
