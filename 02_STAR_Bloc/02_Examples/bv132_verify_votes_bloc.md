# BV132 — verify number of votes cast (Bloc STAR) · issue [#1073](https://github.com/Equal-Vote/bettervoting/issues/1073)

<!-- case-meta:start — managed by build_yaml_pages.py; edit the YAML, not these lines -->
**Method:** [Bloc STAR (multi-winner, majoritarian)](../../03_STAR_PR/01_Learn) · **2 seats** · **Expected winners:** C, B · [full count →](cases/cases_pages/bv132_verify_votes_bloc.md)
<!-- case-meta:end -->

*BetterVoting reports the wrong number of voters on a Bloc STAR election: it drops the two "flat" ballots (every candidate scored the same) as abstentions. The winners are still correct — the bug is the vote count / turnout, not the result.*

Reference files: [`bv132_verify_votes_bloc.yaml`](cases/bv132_verify_votes_bloc.yaml) (LH, `expected_winners: [C, B]`) · frozen export [`bv132_verify_votes_bloc_bv_export.json`](cases/bv132_verify_votes_bloc_bv_export.json) (BV election `3494cb`). Backs sheet row **BV132**.

## The election

Bloc STAR, 3 candidates, **2 seats**, 4 ballots — two of them flat:

```
A,B,C
1,1,1     ← flat (no preference)
5,5,5     ← flat (no preference)
1,2,3
1,2,3
```

## View 1 — BetterVoting (the bug)

BetterVoting's result page shows **"2 voters"** and scoring totals **A=2, B=4, C=6** — which is *only* the two `1,2,3` ballots. The two flat ballots have been dropped. (Winners shown: **C and B**.) The frozen export confirms why: its `summaryData` carries `nAbstentions: 2`, `nTallyVotes: 2` — BV classified the flat ballots as **abstentions**.

*(Drop the BV screenshot into an `img/` subfolder as `img/3494cb_result.png` to add it here.)*

## View 2 — the LH report (all four ballots counted)

The same ballots through the reference engine. Note **"Tabulating 4 ballots,"** the score distribution (each candidate's real total), and — the key line — the runoff denominator **"2 of 4 (2 Equal Support)"**: LH keeps the two flat ballots in the count as *Equal Support* (no preference) rather than discarding them.

--8<-- "02_STAR_Bloc/02_Examples/cases/cases_pages/bv132_verify_votes_bloc.md:report"
Full audit copy: [`_main_tabulated/bv132_verify_votes_bloc_tabulated.txt`](cases/cases_tabulated/bv132_verify_votes_bloc_tabulated.txt).

## The diagnostic (where the ballots go)

The frozen export localizes the defect precisely:

- **Ingestion is fine.** The export's `Ballots` array holds **all 4** ballots.
- **Tabulation drops them.** `summaryData` reports `nAbstentions: 2`, `nTallyVotes: 2`; the score totals (A=2/B=4/C=6) are only the two non-flat ballots. So BV treats a fully-flat ballot as an abstention and removes it from the count.
- **Winners are unaffected.** A flat ballot adds equally to every candidate and is Equal in every head-to-head, so it can never change a STAR/Bloc result — LH and BV both elect **C, B**. The visible harm is the wrong voter count / turnout (and any percentage or quorum computed from it).

## Related

- [#1407](https://github.com/Equal-Vote/bettervoting/issues/1407) — flat ballot mis-filed as abstention (the same root cause).
- [#1035](https://github.com/Equal-Vote/bettervoting/issues/1035) — `NaN` on equal ties/preferences (same ballot family).
- [#904](https://github.com/Equal-Vote/bettervoting/issues/904) — the export also labels `votingMethod: "STAR"` rather than "Bloc STAR".
- Concept: [Flat scores, ties & tie-breaking](../../01_STAR/09_Parked/Flat_scores_ties/README.md) · [why flat ballots don't change the winner](../../07_Concepts/topics/ties/why_contrived_tie_cases.md).
