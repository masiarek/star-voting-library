# abcvoting Tabulation Engine (multi-winner Approval / ABC rules)

Runs **approval-based committee (ABC)** rules from Martin Lackner's
[`abcvoting`](https://github.com/martinlackner/abcvoting) library — the
standard peer-reviewed toolkit for this family (companion to Lackner &
Skowron's book *Multi-Winner Voting with Approval Preferences*) — on this
repo's approval YAML files.

It does two jobs:

1. **Extends the LH engine.** The [LH engine](../STARVote_LH_tabulation_engine/)
   tabulates **bloc** Approval only (`voting_method: Approval_Multi_Winner` —
   the `num_winners` most-approved win). This wrapper adds the **proportional**
   rules on the *same ballots*: **SPAV** (`seqpav`), **PAV** (`pav`), and
   **seq-Phragmén** (`seqphragmen`) — the rules described in
   [Approval — Multi-Winner](../00_start_here/Approval_Voting/approval_multiwinner.md).
2. **Independent cross-check.** abcvoting's plain `av` rule must elect the
   same committee as the LH engine's bloc-Approval count — an outside witness
   that the LH approval tally is correct, in the same spirit as the
   [`pref_voting` cross-check](../pref_voting_tabulation_engine/) for ranked
   methods.

```bash
pip install abcvoting        # optional dependency — everything guards on it

python abcvoting_tabulation_engine/abc_tabulation.py 04_Approval/multiwinner/approval_bloc_2seats_c4_b6.yaml
python abcvoting_tabulation_engine/abc_tabulation.py FILE.yaml --rules av,seqpav,pav,seqphragmen --seats 3
```

On the repo's majority-sweep case (6 voters, 2 seats: a 4-voter majority
behind Amy/Ben, a 2-voter minority behind Cora/Doug) it prints:

```text
--- abcvoting: approval-based committee rules (2 seats) ---
 approval_bloc_2seats_c4_b6.yaml: 6 ballots, candidates: Amy, Ben, Cora, Doug
   av           Approval Voting (AV)                       ->  Amy, Ben
   seqpav       Sequential Proportional Approval Voting (seq-PAV) ->  Amy, Cora
   pav          Proportional Approval Voting (PAV)         ->  Amy, Cora
   seqphragmen  Phragmén's Sequential Rule (seq-Phragmén)  ->  Amy, Cora
   (av = bloc Approval, the LH engine's method; seqpav/pav/seqphragmen are proportional.)
```

Same ballots, two philosophies: bloc `av` lets the majority **sweep**;
every proportional rule gives the minority its seat.

Notes:

- **Ties:** an ABC rule can return *several* tied committees; all are printed
  (`[N tied committees]`).
- **Empty ballots** (no approvals) can't affect any ABC rule; they are dropped
  and the count reported.
- `abcvoting` offers many more rules (`monroe`, `cc`, `lexcc`, `rule-x`/MES, …) —
  pass any rule id via `--rules`. Exact PAV/Monroe use an ILP solver on large
  instances; the repo's small teaching cases compute instantly.
- Tested by
  [`tests/test_abcvoting_crosscheck.py`](../STARVote_LH_tabulation_engine/tests/test_abcvoting_crosscheck.py)
  (skips cleanly if `abcvoting` isn't installed).

# file: README_abcvoting_tabulation_engine.md
