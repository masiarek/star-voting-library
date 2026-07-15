# 04_Approval / multiwinner — Bloc Approval

Multi-winner Approval with the same 0/1 ballot: the `num_winners` most-approved candidates win (bloc / at-large counting). Declared as `voting_method: Approval_Multi_Winner` with `num_winners: ≥ 2`. Ballot mockup: [3-seat council ballot](../../00_start_here/Approval_Voting/img/approval_ballot_multiwinner_3seats.png).

Three cases, in teaching order:

1. [`approval_bloc_3seats_c6_b5.yaml`](approval_bloc_3seats_c6_b5.yaml) — the plain mechanics: 3-seat council, six candidates, five voters; sum the columns, top three win (Adams, Brown, Clark). Matches the ballot mockup.
2. [`approval_bloc_2seats_c4_b6.yaml`](approval_bloc_2seats_c4_b6.yaml) — the majority sweep + priority tie-break (below).
3. [`approval_bloc_4seats_c7_b12_lackner_skowron.yaml`](approval_bloc_4seats_c7_b12_lackner_skowron.yaml) — the running example from Lackner & Skowron's *Multi-Winner Voting with Approval Preferences* ([open access](https://doi.org/10.1007/978-3-031-09016-5)): AV ties {A,B,C,D} with {A,B,C,F}; PAV elects {A,B,C,F} outright — the committee that leaves fewer voters wholly unrepresented. **Its "shadow STAR" companion** runs the same profile through the STAR family (Bloc STAR / Allocated Score / SSS all seat D; only **RRV** recovers F, matching PAV): [Lackner & Skowron — approval and its shadow STAR](lackner_skowron_shadow_star.md). **Live on BetterVoting (BV27):** [`jt6r76` results ↗](https://bettervoting.com/jt6r76/results) — BV's Approval engine seats **A,B,C,F** (its random draw broke the D/F tie for F, and it *correctly flags* `tieBreakType: random`): [BV27 two-view case](bv27_jt6r76_lackner_approval_committee.md).

The flagship case, [`approval_bloc_2seats_c4_b6.yaml`](approval_bloc_2seats_c4_b6.yaml), teaches the one thing that matters about bloc counting: it is **majoritarian**. Six voters, four candidates, two seats — a 4-voter majority (all approve Amy, two also Ben) takes **both** seats; the 2-voter minority behind Cora and Doug gets nothing. Bonus lesson: Ben and Cora tie 2–2 for the last seat, and the engine's tie note shows candidate priority order breaking it for Ben:

```text
--- Approval Voting (2 winners) ---
 Tabulating 6 ballots (any non-zero score = approval).

Ballots:
   columns = Amy, Ben, Cora, Doug      (1 = approve; 0 / blank / marker = not approved)
   1,0,0,0
   1,1,0,0
   1,1,0,0
   1,0,0,0
   0,0,1,1
   0,0,1,0

   Amy  -- 4 -- Elected
   Ben  -- 2 -- Elected
   Cora -- 2
   Doug -- 1
  Note: Ben, Cora each have 2 approvals and tie for the last 1 seat.
        Candidate priority order (Ben > Cora) broke the tie: Ben elected, Cora not elected.

Winners — Approval Voting (2 winners)
  Amy, Ben
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/multiwinner/approval_bloc_2seats_c4_b6.yaml
```

The **proportional** Approval rules (SPAV, PAV, seq-Phragmén) run on the same file via the [`abcvoting` engine](../../06_Other/abcvoting_tabulation_engine/) — all of them break the sweep and give the minority its seat (Amy + Cora):

```bash
pip install abcvoting   # once
python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py 04_Approval/multiwinner/approval_bloc_2seats_c4_b6.yaml
```

Same trade-off, score-ballot edition: Bloc STAR sweeps too ([Bloc STAR](../../02_STAR_Bloc/)); the proportional STAR methods fix it ([proportional STAR](../../03_STAR_PR/)). Concepts: [Approval — Multi-Winner](../../00_start_here/Approval_Voting/Multiwinner_Approval/approval_multiwinner.md).

# file: README.md
