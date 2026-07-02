# 04_Approval / multiwinner — Bloc Approval

Multi-winner Approval with the same 0/1 ballot: the `num_winners`
most-approved candidates win (bloc / at-large counting). Declared as
`voting_method: Approval_Multi_Winner` with `num_winners: ≥ 2`.

The case here, [`approval_bloc_2seats_c4_b6.yaml`](approval_bloc_2seats_c4_b6.yaml),
teaches the one thing that matters about bloc counting: it is **majoritarian**.
Six voters, four candidates, two seats — a 4-voter majority approving Amy (and
mostly Ben) takes **both** seats; the 2-voter minority behind Cora and Doug
gets nothing:

```text
--- Approval Voting (2 winners) ---
 Tabulating 6 ballots (any non-zero score = approval).
   Amy  -- 4 -- Elected
   Ben  -- 3 -- Elected
   Cora -- 2
   Doug -- 1

Winners — Approval Voting (2 winners)
  Amy, Ben
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/multiwinner/approval_bloc_2seats_c4_b6.yaml
```

The **proportional** Approval rules (SPAV, PAV, seq-Phragmén) run on the same
file via the [`abcvoting` engine](../../abcvoting_tabulation_engine/README_abcvoting_tabulation_engine.md)
— all of them break the sweep and give the minority its seat (Amy + Cora):

```bash
pip install abcvoting   # once
python abcvoting_tabulation_engine/abc_tabulation.py 04_Approval/multiwinner/approval_bloc_2seats_c4_b6.yaml
```

Same trade-off, score-ballot edition: Bloc STAR sweeps too
([`02_STAR_Bloc/`](../../02_STAR_Bloc/README_02_STAR_Bloc.md)); the
proportional STAR methods fix it ([`03_STAR_PR/`](../../03_STAR_PR/README_03_STAR_PR.md)).
Concepts: [Approval — Multi-Winner](../../00_start_here/Approval_Voting/approval_multiwinner.md).

# file: README_approval_multiwinner.md
