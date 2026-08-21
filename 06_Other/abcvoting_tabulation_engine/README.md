# ABCvoting Tabulation Engine (multi-winner Approval / ABC rules)

Runs **approval-based committee (ABC)** rules from Martin Lackner's [`abcvoting`](https://github.com/martinlackner/abcvoting) library — the standard peer-reviewed toolkit for this family (companion to Lackner & Skowron's book *Multi-Winner Voting with Approval Preferences*) — on this repo's approval YAML files.

It does two jobs:

1. **Extends the LH engine.** The [LH engine](../../STARVote_LH_tabulation_engine/README.md) tabulates **bloc** Approval only (`voting_method: Approval_Multi_Winner` — the `num_winners` most-approved win). This wrapper adds the **proportional** rules on the *same ballots*: **SPAV** (`seqpav`), **PAV** (`pav`), and **seq-Phragmén** (`seqphragmen`) — the rules described in [Approval — Multi-Winner](../../04_Approval/01_Learn/Multiwinner_Approval/approval_multiwinner.md). It also carries **SAV** (`sav`), [Satisfaction Approval Voting](../../04_Approval/01_Learn/Multiwinner_Approval/satisfaction_approval_voting.md) — one vote per *ballot*, split among the marks — which is in the default rule set precisely because it is the rule most likely to *disagree* with `av` on the same ballots.
2. **Independent cross-check.** abcvoting's plain `av` rule must elect the same committee as the LH engine's bloc-Approval count — an outside witness that the LH approval tally is correct, in the same spirit as the [`pref_voting` cross-check](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/README.md) for ranked methods.

```bash
pip install abcvoting        # optional dependency — everything guards on it

python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py 04_Approval/02_Examples/multiwinner/cases/approval_bloc_2seats_c4_b6.yaml
python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py FILE.yaml --rules av,seqpav,pav,seqphragmen --seats 3
```

On the repo's majority-sweep case (6 voters, 2 seats: a 4-voter majority behind Amy — two of them also approving Ben — and a 2-voter minority behind Cora/Doug) it prints:

```text
--- abcvoting: approval-based committee rules (2 seats) ---
 approval_bloc_2seats_c4_b6.yaml: 6 ballots, candidates: Amy, Ben, Cora, Doug
   av           Approval Voting (AV)                       ->  Amy, Ben  |  Amy, Cora  [2 tied committees]
   seqpav       Sequential Proportional Approval Voting (seq-PAV) ->  Amy, Cora
   pav          Proportional Approval Voting (PAV)         ->  Amy, Cora
   seqphragmen  Phragmén's Sequential Rule (seq-Phragmén)  ->  Amy, Cora
   (av = bloc Approval, the LH engine's method; seqpav/pav/seqphragmen are proportional.)
```

Same ballots, two philosophies: bloc `av` ties the majority's second candidate with the minority's first (the LH engine breaks that tie for the majority by priority order); every proportional rule gives the minority its seat **decisively**.

## `abc_axiom_check.py` — the axioms, not just the winners

[`abc_axiom_check.py`](abc_axiom_check.py) is the second tool here, and it answers a different question: not *who won* but *what the rule guarantees*. It encodes all thirty counterexample profiles from Lackner & Skowron's Appendix A and replays them, so the recomputed Table 3.1 in [04_Approval/03_Criteria](../../04_Approval/03_Criteria/README.md) is a computed result rather than a transcription.

```bash
python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose
python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --search 400
```

It implements Definitions 3.1–3.7 directly (dominance, committee monotonicity, both support-monotonicity variants, consistency, inclusion-strategyproofness) and is honest about the asymmetry: an `✗` cell is *demonstrated* by its witness, while a `✓` is *cited* — no finite replay proves a universal claim, which is what `--search` is for and what it cannot do. Gated by [`tests/test_abc_axioms.py`](../../STARVote_LH_tabulation_engine/tests/test_abc_axioms.py).

Notes:

- **Ties:** every rule is run **irresolute** (`resolute=False`, passed explicitly) — an ABC rule can return *several* tied committees, and all are printed (`[N tied committees]`). The flag is explicit because the library's *sequential* rules (`seqpav`, `seqphragmen`, `equal-shares`) default to resolute, silently breaking a candidate tie by smallest index — ballot-header column order here; until 2026-08-20 the wrapper inherited that default, so `seqpav` / `seqphragmen` results quoted from earlier runs may hide a tie. A rule with no irresolute form (`greedy-monroe`) falls back to resolute and its line says so.
- **Empty ballots** (no approvals) can't affect any ABC rule; they are dropped and the count reported.
- `abcvoting` offers many more rules (`monroe`, `cc`, `lexcc`, `rule-x`/MES, …) — pass any rule id via `--rules`. Exact PAV/Monroe use an ILP solver on large instances; the repo's small teaching cases compute instantly.
- Tested by [`tests/test_abcvoting_crosscheck.py`](../../STARVote_LH_tabulation_engine/tests/test_abcvoting_crosscheck.py) (skips cleanly if `abcvoting` isn't installed).

# file: README.md
