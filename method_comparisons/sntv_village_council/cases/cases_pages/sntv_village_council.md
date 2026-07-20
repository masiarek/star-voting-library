# Village Council by SNTV — a concentrated minority wins a seat

*Generated from [`sntv_village_council.yaml`](../sntv_village_council.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../00_start_here) · **2 seats** · **Expected winners:** Priya, Nora

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/y3tvxm) · **[results ↗](https://bettervoting.com/y3tvxm/results)** (election `y3tvxm`).

**Official tie-break (lot) order:** Nora > Omar > Priya — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Nine residents elect a 2-seat Village Council under SNTV (single non-transferable
vote): each voter casts ONE vote, and the two candidates with the most votes win.

The Downtown majority (5 voters) SPLITS between its two candidates — Nora (3) and
Omar (2). The Riverside minority (4 voters) CONCENTRATES all its votes on Priya.
So Priya tops the poll with 4 and takes a seat next to Nora (3); Omar (2) just
misses. Under Block Voting the 5-voter majority would take BOTH seats — SNTV's
single vote is exactly what lets a 44% minority (4 of 9) win representation, if it
concentrates. That vote-management pressure is why SNTV was used for multi-member
districts (Japan, Taiwan) before STV.

Reproduced on BetterVoting as multi-winner Plurality (BV2136) — BV elects the same
two. Companion: the full Block / Limited / SNTV family in
method_comparisons/multi_member_plurality.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Nora,Omar,Priya
3: 1,0,0
2: 0,1,0
4: 0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/sntv_village_council_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- SNTV (single non-transferable vote) — 2 winners ---
 Tabulating 9 ballots (1 vote/voter).

First-choice votes (most votes fill the seats):
   Priya     4  <- Elected
   Nora      3  <- Elected
   Omar      2

Winners — SNTV (single non-transferable vote), 2 seats:
   1. Priya   (4 votes)
   2. Nora   (3 votes)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/sntv_village_council/cases/sntv_village_council.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
